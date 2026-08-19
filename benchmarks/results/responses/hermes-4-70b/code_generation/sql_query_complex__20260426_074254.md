# Hermes 4 70B — code_generation/sql_query_complex

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 7.44 | quality: 8.84
- latency_total: 5.83s | tokens_per_second: 65.7
- input_tokens: 168 | output_tokens: 383
- judge_score: 4.6 | justificación: 

## Respuesta completa

```sql
SELECT
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id) AS avg_order_value,
    CASE 
        WHEN SUM(CASE WHEN p.category = 'Electronics' THEN oi.quantity ELSE 0 END) >= 
             SUM(CASE WHEN p.category = 'Books' THEN oi.quantity ELSE 0 END) AND
             SUM(CASE WHEN p.category = 'Electronics' THEN oi.quantity ELSE 0 END) >= 
             SUM(CASE WHEN p.category = 'Clothing' THEN oi.quantity ELSE 0 END) THEN 'Electronics'
        WHEN SUM(CASE WHEN p.category = 'Books' THEN oi.quantity ELSE 0 END) >= 
             SUM(CASE WHEN p.category = 'Electronics' THEN oi.quantity ELSE 0 END) AND
             SUM(CASE WHEN p.category = 'Books' THEN oi.quantity ELSE 0 END) >= 
             SUM(CASE WHEN p.category = 'Clothing' THEN oi.quantity ELSE 0 END) THEN 'Books'
        ELSE 'Clothing'
    END AS categoria_mas_comprada
FROM
    customers c
JOIN
    orders o ON c.id = o.customer_id
JOIN
    order_items oi ON o.id = oi.order_id
JOIN
    products p ON oi.product_id = p.id
WHERE
    o.status = 'completed'
    AND o.created_at >= DATEADD(MONTH, -6, GETDATE())
GROUP BY
    c.name,
    c.email,
    c.country
HAVING
    COUNT(DISTINCT o.id) >= 3
ORDER BY
    total_revenue DESC
LIMIT 10;
```