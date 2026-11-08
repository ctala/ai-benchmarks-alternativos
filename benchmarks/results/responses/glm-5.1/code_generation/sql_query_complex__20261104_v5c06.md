# GLM-5.1 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 24.055s | tokens_per_second: 71.8
- input_tokens: 156 | output_tokens: 1726
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

```sql
WITH customer_revenue AS (
    SELECT 
        c.id   AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id)                       AS total_orders,
        SUM(oi.quantity * oi.unit_price)           AS total_revenue
    FROM customers c
    JOIN orders o       ON o.customer_id = c.id
    JOIN order_items oi ON oi.order_id   = o.id
    WHERE o.status      = 'completed'
      AND o.created_at  >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
customer_category AS (
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON oi.order_id   = o.id
    JOIN products p     ON p.id          = oi.product_id
    WHERE o.status      = 'completed'
      AND o.created_at  >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)
SELECT 
    cr.name,
    cr.email,
    cr.country,
    cr.total_orders,
    cr.total_revenue,
    ROUND(cr.total_revenue / cr.total_orders, 2) AS avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_revenue cr
LEFT JOIN customer_category cc 
       ON cc.customer_id = cr.customer_id 
      AND cc.rn = 1
ORDER BY cr.total_revenue DESC
LIMIT 10;
```

### Notas sobre la implementación

1. **Cálculo de revenue**: Usé `oi.quantity * oi.unit_price` desde `order_items` en lugar de `orders.total`, ya que es la fuente de verdad a nivel de línea. Si prefieres usar `orders.total`, elimina el JOIN con `order_items` en el primer CTE y cambia el SUM.

2. **Filtro de 6 meses**: `DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)` es sintaxis **MySQL**. Equivalentes:
   - PostgreSQL: `CURRENT_DATE - INTERVAL '6 months'` o `NOW() - INTERVAL '6 months'`
   - SQL Server: `DATEADD(month, -6, GETDATE())`
   - BigQuery: `DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)`
   - Snowflake: `DATEADD(month, -6, CURRENT_DATE())`

3. **Categoría más comprada**: En el CTE `customer_category` sumo la cantidad (`quantity`) por cliente y categoría, y con `ROW_NUMBER()` me quedo con la de mayor volumen. El `ORDER BY ... p.category ASC` es solo para desempate determinista.

4. **`COUNT(DISTINCT o.id)`**: Necesario porque el JOIN con `order_items` multiplica las filas por cada línea de la orden, lo que inflaría el conteo si usáramos `COUNT(*)`.

5. **`HAVING >= 3`**: Se aplica **después** del filtro de `status = 'completed'` y del rango de 6 meses, así que cuenta solo órdenes completadas recientes.

6. **`LEFT JOIN`** al final: por seguridad, por si un cliente tuviera órdenes sin items válidos (no debería pasar con datos limpios, pero evita perder filas).

Si quieres que el "top 10" sea solo entre los que ya cumplen las condiciones (lo cual ya hace esta query), está correcto. Si en cambio quisieras top 10 global y luego filtrar, el orden de las cláusulas cambiaría.