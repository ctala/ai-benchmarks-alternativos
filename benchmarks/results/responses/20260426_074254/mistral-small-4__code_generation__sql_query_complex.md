# Mistral Small 4 — code_generation/sql_query_complex

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 7.55 | quality: 8.0
- latency_total: 2.597s | tokens_per_second: 96.6
- input_tokens: 159 | output_tokens: 251
- judge_score: 4.0 | justificación: 

## Respuesta completa

```sql
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    COUNT(o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    (SUM(oi.quantity * oi.unit_price) / COUNT(o.id)) AS avg_order_value,
    (
        SELECT p.category
        FROM order_items oi2
        JOIN products p ON oi2.product_id = p.id
        WHERE oi2.order_id = o.id
        GROUP BY p.category
        ORDER BY SUM(oi2.quantity) DESC
        LIMIT 1
    ) AS categoria_mas_comprada
FROM
    customers c
JOIN
    orders o ON c.id = o.customer_id
JOIN
    order_items oi ON o.id = oi.order_id
WHERE
    o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
GROUP BY
    c.id, c.name, c.email, c.country
HAVING
    COUNT(o.id) >= 3
ORDER BY
    total_revenue DESC
LIMIT 10;
```