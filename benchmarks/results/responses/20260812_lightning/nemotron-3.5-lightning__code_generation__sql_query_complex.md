# Nemotron 3.5 Lightning — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.06 | quality: 10.0
- latency_total: 6.973s | tokens_per_second: 684.6
- input_tokens: 160 | output_tokens: 4774
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL detallada que cumple con todos los requisitos especificados.

## Respuesta completa

Here's a SQL query that matches all your requirements. It's written for PostgreSQL / MySQL 8+/SQLite (standard SQL syntax with window functions).

```sql
WITH customer_totals AS (
    -- Aggregates per customer: orders count & total revenue in last 6 months
    SELECT c.id AS customer_id,
           c.name, c.email, c.country,
           COUNT(DISTINCT o.id) AS total_orders,
           SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3           -- at least 3 completed orders
),

category_ranking AS (
    -- Ranks product categories per customer by total quantity sold
    SELECT c.id AS customer_id,
           p.category,
           ROW_NUMBER() OVER (PARTITION BY c.id 
                              ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, p.category
),

top_category AS (
    -- Picks the #1 category per customer (most purchased by quantity)
    SELECT customer_id, category AS categoria_mas_comprada
    FROM category_ranking
    WHERE rn = 1
)

-- Final result: join totals + top category, order & limit
SELECT ct.name, 
       ct.email, 
       ct.country, 
       ct.total_orders, 
       ct.total_revenue, 
       ct.total_revenue / ct.total_orders AS avg_order_value,
       tc.categoria_mas_comprada
FROM customer_totals ct
JOIN top_category tc ON ct.customer_id = tc.customer_id
ORDER BY ct.total_revenue DESC
LIMIT 10;
```

### 🔍 How it works:
1. **`customer_totals`**: Joins all tables, filters for `status = 'completed'` and `created_at` within the last 6 months. Groups by customer, counts distinct orders, and sums revenue (`quantity * unit_price`). The `HAVING` clause ensures only customers with ≥3 orders are kept.
2. **`category_ranking`**: For the same filtered set, groups by customer + product category, sums `quantity` per category, and uses `ROW_NUMBER()` to rank them. The highest-quantity category gets `rn = 1`.
3. **`top_category`**: Filters to only the top-ranked category per customer.
4. **Final SELECT**: Joins the aggregated customer data with their top category, computes `avg_order_value` as `total_revenue / total_orders`, and returns the top 10 by `total_revenue DESC`.

### 📐 Assumptions / Notes:
- "Most purchased category" is interpreted as the category with the **highest total quantity** of items bought. If you prefer it by revenue per category, change `SUM(oi.quantity) DESC` to `SUM(oi.quantity * oi.unit_price) DESC` in `category_ranking`.
- Date syntax `CURRENT_DATE - INTERVAL '6 months'` works in PostgreSQL, MySQL 8+, and SQLite. Adjust slightly for other dialects if needed.
- `unit_price` and `quantity` from `order_items` are used for revenue calculation, as per your schema.