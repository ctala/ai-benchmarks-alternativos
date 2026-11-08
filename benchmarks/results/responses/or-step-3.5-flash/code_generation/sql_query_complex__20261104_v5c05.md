# Step 3.5 Flash — code_generation/sql_query_complex

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.68 | quality: 9.8
- latency_total: 49.007s | tokens_per_second: 91.1
- input_tokens: 160 | output_tokens: 4466
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
WITH completed_orders AS (
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL 6 MONTH
),
order_items_with_category AS (
    SELECT 
        o.customer_id,
        oi.order_id,
        oi.quantity,
        p.category
    FROM completed_orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
),
customer_category_summary AS (
    SELECT 
        customer_id,
        category,
        SUM(quantity) AS total_quantity
    FROM order_items_with_category
    GROUP BY customer_id, category
),
ranked_categories AS (
    SELECT 
        customer_id,
        category,
        total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY total_quantity DESC, category ASC
        ) AS rn
    FROM customer_category_summary
),
customer_orders_summary AS (
    SELECT 
        customer_id,
        COUNT(order_id) AS total_orders,
        SUM(total) AS total_revenue
    FROM completed_orders
    GROUP BY customer_id
    HAVING COUNT(order_id) >= 3
)
SELECT 
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    cos.total_orders,
    cos.total_revenue,
    ROUND(cos.total_revenue / cos.total_orders, 2) AS avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customer_orders_summary cos
JOIN customers c ON cos.customer_id = c.id
LEFT JOIN ranked_categories rc 
    ON cos.customer_id = rc.customer_id AND rc.rn = 1
ORDER BY cos.total_revenue DESC
LIMIT 10;
```

**Explicación:**
1. **`completed_orders`**: Filtra órdenes completadas en los últimos 6 meses.
2. **`order_items_with_category`**: Une las órdenes con sus items y productos para obtener la categoría de cada producto comprado.
3. **`customer_category_summary`**: Agrupa por cliente y categoría, sumando la cantidad total de productos comprados en cada categoría.
4. **`ranked_categories`**: Asigna un ranking a las categorías por cliente según la cantidad total de productos comprados (en caso de empate, usa el orden alfabético de la categoría).
5. **`customer_orders_summary`**: Calcula el total de órdenes y revenue por cliente, filtrando solo aquellos con al menos 3 órdenes completadas.
6. **Consulta final**: Combina la información del cliente con sus métricas y la categoría más comprada (rn=1). Ordena por `total_revenue` descendente y limita a 10 resultados.