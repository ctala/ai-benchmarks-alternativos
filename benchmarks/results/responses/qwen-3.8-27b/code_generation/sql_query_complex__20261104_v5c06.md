# Qwen 3.8 27B — code_generation/sql_query_complex

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.94 | quality: 9.8
- latency_total: 286.577s | tokens_per_second: 36.5
- input_tokens: 203 | output_tokens: 10472
- judge_score: 5.0 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estas tablas:
- orders (id, customer_id, total, status, created_at)
- customers (id, name, email, country, created_at)
- order_items (id, order_id, product_id, quantity, unit_price)
- products (id, name, category, price)

Escribe una query SQL que muestre:
- Top 10 clientes por revenue total en los ultimos 6 meses
- Con columnas: nombre, email, pais, total_orders, total_revenue, avg_order_value, categoria_mas_comprada
- Ordena por total_revenue DESC
- Solo clientes con al menos 3 ordenes completadas (status = 'completed')


## Respuesta completa



Aquí tienes una query usando **window functions** (`ROW_NUMBER`) para obtener la **categoría más comprada** por cliente.

> Asumo que el **revenue** se toma de `orders.total` y que las **3 ordenes completadas** se cuentan dentro de los últimos 6 meses.

```sql
WITH completed_orders AS (
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_totals AS (
    SELECT
        customer_id,
        COUNT(*) AS total_orders,
        ROUND(COALESCE(SUM(total), 0), 2) AS total_revenue,
        ROUND(COALESCE(AVG(total), 0), 2) AS avg_order_value
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_sales AS (
    SELECT
        co.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue,
        SUM(oi.quantity) AS category_quantity
    FROM completed_orders co
    JOIN order_items oi
        ON oi.order_id = co.id
    JOIN products p
        ON p.id = oi.product_id
    WHERE p.category IS NOT NULL
    GROUP BY
        co.customer_id,
        p.category
),
top_category AS (
    SELECT
        customer_id,
        category AS categoria_mas_comprada
    FROM (
        SELECT
            customer_id,
            category,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id
                ORDER BY
                    category_revenue DESC,
                    category_quantity DESC,
                    category
            ) AS rn
        FROM category_sales
    ) ranked
    WHERE rn = 1
)
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    ct.total_orders,
    ct.total_revenue,
    ct.avg_order_value,
    COALESCE(tc.categoria_mas_comprada, 'N/A') AS categoria_mas_comprada
FROM customer_totals ct
JOIN customers c
    ON c.id = ct.customer_id
LEFT JOIN top_category tc
    ON tc.customer_id = ct.customer_id
ORDER BY
    ct.total_revenue DESC
LIMIT 10;
```

Notas:

1. **Fecha “últimos 6 meses”**  
   La sintaxis usada es estilo PostgreSQL:
   ```sql
   CURRENT_DATE - INTERVAL '6 months'
   ```

   En MySQL podrías usar:
   ```sql
   DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
   ```

   En SQL Server:
   ```sql
   DATEADD(MONTH, -6, GETDATE())
   ```

2. **Categoría más comprada**  
   Aquí está calculada por **revenue** de las líneas del pedido.  
   Si la quieres por **unidades compradas**, cambia el `ORDER BY` dentro del `ROW_NUMBER` a:
   ```sql
   ORDER BY
       category_quantity DESC,
       category_revenue DESC,
       category
   ```

3. **Revenue desde `order_items`**  
   Si no quieres usar `orders.total` y prefieres calcular el revenue desde:
   ```sql
   oi.quantity * oi.unit_price
   ```
   entonces deberías ajustar `customer_totals` para que sume ese valor en vez de `orders.total`.