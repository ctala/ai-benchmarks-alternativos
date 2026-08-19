# Qwen 3-Next 80B Thinking — code_generation/sql_query_complex

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 5.17 | quality: 4.84
- latency_total: 20.526s | tokens_per_second: 99.8
- input_tokens: 155 | output_tokens: 2048
- judge_score: 1.6 | justificación: 

## Respuesta completa

Okay, let's see. I need to write a SQL query that shows the top 10 customers by total revenue in the last 6 months. The columns required are name, email, country, total_orders, total_re revenue, avg_order_value, and categoria_mas_comprada. Also, only customers with at least 3 completed orders. Order by total_revenue descending.

Hmm, first, I need to join the relevant tables. The main tables involved are orders, customers, order_items, and products. But since we're looking at revenue, the order_items table has the unit_price and quantity, so total revenue per order would be sum of (quantity * unit_price) for each order. But wait, the orders table has a 'total' column. Wait, maybe the ' total' in orders is already the total for that order? Or is it a calculated field? The problem statement says "orders (id, customer_id, total, status, created_at)" so total might be the total for the order. But then why is there order_items with unit_price and quantity? Maybe the 'total' in orders is redundant, or perhaps it's the sum of order_items. But the question says "top 10 clientes por revenue total", so maybe the ' total' in the orders table is the total revenue per order. Or maybe it's better to calculate it from order_items. But the problem gives both, so perhaps the ' total' in the orders table is the sum of order_items. But to be safe, perhaps we should calculate the revenue per order by summing (quantity * unit_price) from order_items. Because sometimes ' total' in the orders table might not be up-to-date. But the problem statement doesn't specify. However, the ' total' column in orders might already be the correct total. But the order_items table has unit_price and quantity, so maybe the ' total' in orders is the sum of (quantity * unit_price) for that order. But to be accurate, perhaps the ' total' in the orders table is the total, but the problem statement says " revenue total", so maybe the ' total' column in orders is the revenue for that order. So for each order, the ' total' is the total revenue. But then, if we group by customer, we can sum the ' total' from orders. However, if the ' total' in the orders table is not the same as the sum from order_items, then there's a problem. But the problem statement doesn't specify, so perhaps we should take the ' total' column from the orders table. But maybe the ' total' in the orders table is a calculated field, but to be precise, perhaps the ' total' in the orders table is the sum of (quantity * unit_price) for all order_items in that order. So for example, if an order has 2 items, each with unit_price 10 and quantity 1, then the ' total' would be 20. So in that case, the ' total' in the orders table is correct. But to be safe, maybe the ' total' column is indeed the sum. So for the purpose of this query, we can use the ' total' column from the orders table to get the revenue per order. But the problem says " revenue total", so perhaps that's correct.

But let's check: the ' total' in the orders table is likely the total for that order. So for each order, the ' total' is the sum of (quantity * unit_price) for all items in that order. So for the total_re revenue per customer, we can sum the ' total' column from the orders table for each customer's completed orders in the last 6 months.

But the problem says " last 6 months", so we need to filter orders created_at within the last 6 months. But the ' created_at' is in the orders table. So for each order, we check if created_at is >= current_date - 6 months. But depending on the SQL dialect, the syntax varies. For example, in MySQL, it's DATE_SUB(now(), INTERVAL 6 MONTH), or in PostgreSQL, it's now() - '6 months'::interval. But the problem doesn't specify the SQL dialect, but maybe using standard syntax. However, in many SQLs, it's possible to use a where clause like created_at >= current_date - 180 days, but better to use interval.

But the exact syntax might depend. Let's assume we're using MySQL. So for the where clause, orders.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH).

But the problem says " last 6 months", so from 6 months ago up to now.

Now, the steps:

1. Join the orders table with customers to get customer details (name, email, country).

2. We need to filter where status='completed', and created_at in last 6 months.

3. For each customer, we need to get:

- total_orders: count of completed orders in the last 6 months (with status 'completed').

- total_re revenue: sum of ' total' from orders for those orders.

- avg_order_value: total_re revenue divided by total_orders.

- categoria_mas_comprada: the most purchased category. How to get that? For each customer, we need to look at all order items in their completed orders in the last 6 months, then for each product's category, count the quantity, and find the category with the highest total quantity. Or, if multiple, pick one. So for example, for a given customer, sum the quantity for each category in their order items, then pick the category with the highest sum.

But how to get that. For the ' categoria_mas_comprada', we need to first join order_items with products to get the category. Then, for each customer, we can group by category, sum the quantity, then pick the top category. But in SQL, to get the most frequent category (by sum of quantity), we can use a subquery or a window function.

Alternatively, we can use a common table expression (CTE) or a derived table to compute the most purchased category per customer.

But in the main query, for each customer, we need to select the category with the highest sum of quantity. So, for example:

SELECT customer_id, category, SUM(quantity) as total_quantity
FROM order_items
JOIN products ON order_items.product_id = products.id
WHERE ... (orders status and created_at)
GROUP by customer_id, category
 then for each customer, pick the category with highest total_quantity.

But how to get that in the main query. perhaps using a subquery with RROW_NUMBER() over (partition by customer_id order by total_quantity desc) to get the top category.

But this complicates the query. Let's see.

Alternatively, use a subquery for the most purchased category per customer.

So steps:

- First, for all completed orders in last 6 months, get the customer id, and for each order item, get the product's category and quantity.

- Then, for each customer, sum the quantity per category.

- Then, for each customer, find the category with the highest sum.

- Then, join that back to the main customer data.

But this requires a subquery or a CTE.

Alternatively, in some databases, you can use a first_value or something, but standard approach is to use a subquery with row_number.

So, for example:

WITH category_counts as (
    SELECT 
        o.customer_id,
        p.category,
 SUM(oi.quantity) as total_quantity,
 ROW_NUMBER() over (partition by o.customer_id order by SUM(oi.quantity) desc) as rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
    GROUP BY o.customer_id, p.category
)
then, in the main query, we can select from this CTE where rn=1.

But then, we need to group the main customer data by customer id, and for each, get the top category from this CCTE.

But the main query would also need to aggregate the total_orders, etc.

So let's structure the query step by step.

First, filter the orders for 'completed' status in last 6 months. Then, for each customer, sum the ' total' for total_re revenue, count the orders for total_orders, and then for the average, total_re revenue / total_orders.

But for the ' categoria_mas_comprada', we need to get the most purchased category per customer.

So the query would:

SELECT 
    c.name, 
    c.email, 
    c.country, 
    COUNT(o.id) as total_orders, 
    SUM(o.total) as total_revenue, 
    SUM(o.total) / COUNT(o.id) as avg_order_value, 
    (SELECT category 
 from ... ) as categoria_mas_comprada
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.status = 'completed'
 AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
 GROUP by c.id 
HAVing COUNT(o.id) >= 3
 ORDER by total_revenue DESC
 LIMIT 10

But the problem is the ' categoria_mas_comprada' part. How to get that in the main query.

Alternatively, we can precompute the most purchased category for each customer in a subquery, then join it.

So let's create a CTE for the top category per customer.

WITH top_categories as (
    SELECT 
        customer_id,
        category,
        SUM(oi.quantity) as total_quantity,
        ROW_NUMBER() over (partition by customer_id order by SUM(oi.quantity) desc