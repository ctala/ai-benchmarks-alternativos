# Qwen 3-Next 80B Thinking (NIM) — code_generation/sql_query_complex

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.58 | quality: 7.36
- latency_total: 23.666s | tokens_per_second: 86.5
- input_tokens: 152 | output_tokens: 2048
- judge_score: 3.4 | justificación: 

## Respuesta completa

Okay, let's see. I need to write a SQL query that shows the top 10 customers by total revenue in the last 6 months. The columns required are nombre, email, pais, total_orders, total_revenue, avg_order_value, and categoria_mas_comprada. They should be ordered by total_revenue descending, and only customers with at least 3 completed orders.

First, let me break down the tables. We have orders, customers, order_items, and products. 

The main table here is customers, but we need to join with orders to get the orders. Then order_items to get the revenue from each order. Products to get the category for the most purchased category.

Wait, the category_mas_comprada is the most purchased category for each customer. So for each customer, we need to find which category they bought the most of. Hmm, that might require a subquery or a window function.

Let me start by thinking about the total_revenue. For each customer, the total revenue would be the sum of (quantity * unit_price) for all their completed orders in the last 6 months.

But the status must be 'completed' for the orders. So first, we need to filter orders where status = 'completed' and created_at is within the last 6 months.

Wait, the problem says "ultimos 6 meses" which is last 6 months. So in SQL, we can use created_at >= current_date - interval '6 months' or something similar. But the exact syntax might depend on the database, but assuming standard SQL.

Now, to get the top 10 customers with at least 3 completed orders.

So steps:

1. Join orders with customers to get customer info.
2. Join order_items to get the revenue per order item.
3. Join products to get the category for each product in order_items.

But for the total_revenue, it's sum of (quantity * unit_price) for each order item in completed orders.

Also, for total_orders, we need to count the number of completed orders for the customer, but only counting orders where status is 'completed'.

Wait, the problem says "solo clientes con al menos 3 ordenes completadas", so we need to count the number of completed orders per customer, and filter those with count >=3.

So first, perhaps group by customer_id, filter for completed orders in the last 6 months.

But the created_at for the orders is in the orders table. So when filtering for last 6 months, we look at orders.created_at.

So first, let's create a subquery or join to get the orders that are completed and within the last 6 months.

Wait, but the orders status is 'completed', so in the orders table, status = 'completed', and created_at >= current_date - 6 months.

So for each customer, we need to get all completed orders in the last 6 months.

Then, for each customer, calculate total_revenue as sum of (order_items.quantity * order_items.unit_price) for all their completed orders.

Also, total_orders would be the count of completed orders for that customer in the period.

But the problem says "al menos 3 ordenes completadas", so the count of completed orders (for the customer) must be >=3.

Then, for each customer, we need to find the most purchased category. So for each customer, look at all order_items from completed orders in the period, join with products to get category, then for each category, sum the quantity or count the number of items? Wait, the most purchased category. So probably the category that has the highest total quantity sold to the customer. Or maybe the category that has the highest number of items. Wait, the problem says "categoria_mas_comprada" which translates to "most purchased category". So probably the category that the customer bought the most in terms of quantity. So for each customer, sum the quantity per category, then pick the category with the highest sum.

But how to get that. Maybe using a subquery that groups by customer_id and category, then uses a window function to rank the categories per customer, then pick the top one.

So for the main query, the steps would be:

- Join orders, order_items, products, customers.

- Filter orders where status = 'completed' and created_at >= current_date - 6 months.

- Then for each customer, calculate total_revenue, total_orders, avg_order_value (which would be total_revenue / total_orders).

- Then for the category, need to find the category with the highest total quantity for that customer.

So let's structure this.

First, create a CTE or subquery that gets all the relevant data.

Let me outline:

WITH customer_data AS (
    SELECT 
        c.id AS customer_id,
        c.name AS nombre,
        c.email AS email,
        c.country AS pais,
        o.id AS order_id,
        oi.quantity,
        oi.unit_price,
        p.category
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
)

Then, for total_revenue, total_orders, etc., but also need to calculate the category.

But for the category, perhaps another CTE.

Alternatively, in the main query, group by customer_id, and then for each customer, compute the sum of quantity * unit_price for revenue, count orders for total_orders, etc.

But for the most purchased category, we need to find the category with the highest sum of quantity for that customer.

So for each customer, group by category, sum quantity, then select the category with max sum.

So perhaps using a subquery for the category.

So the steps:

1. For each customer, calculate total_orders, total_revenue, avg_order_value.

2. For each customer, find the category with the highest total quantity.

So in SQL, to get the category_mas_comprada, perhaps using a subquery with ROW_NUMBER() or RANK().

For example:

SELECT customer_id, category, SUM(quantity) as total_quantity
FROM customer_data
GROUP BY customer_id, category

Then for each customer, rank these by total_quantity DESC, and pick the top one.

So maybe:

WITH customer_data AS (
    ... (as above)
),
category_rank AS (
    SELECT 
        customer_id,
        category,
        SUM(quantity) as total_quantity,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY SUM(quantity) DESC) as rn
    FROM customer_data
    GROUP BY customer_id, category
)
Then in the main query, select the category where rn=1.

So the main query would join these.

Let's try to build the full query.

First, the customer_data CTE.

But also, for total_orders, we need to count the number of orders per customer. But each order has multiple items, but total_orders is the count of orders (not items), so for each customer, count the distinct order_id in the customer_data.

Wait, yes. Because total_orders is the number of completed orders, so each order is counted once per customer.

So in the customer_data CTE, each row is an order item. So for total_orders, we need to count distinct order_id for each customer.

But perhaps in the main query, when grouping by customer, the total_orders would be COUNT(DISTINCT order_id).

Similarly, total_revenue is SUM(quantity * unit_price).

avg_order_value would be total_revenue / total_orders.

So let's structure:

WITH customer_data AS (
    SELECT 
        c.id AS customer_id,
        c.name AS nombre,
        c.email AS email,
        c.country AS pais,
        o.id AS order_id,
        oi.quantity,
        oi.unit_price,
        p.category
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
category_rank AS (
    SELECT 
        customer_id,
        category,
        SUM(quantity) as total_quantity,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY SUM(quantity) DESC) as rn
    FROM customer_data
    GROUP BY customer_id, category
),
aggregated_data AS (
    SELECT 
        customer_id,
        nombre,
        email,
        pais,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(quantity * unit_price) AS total_revenue,
        SUM(quantity * unit_price) / COUNT(DISTINCT order_id) AS avg_order_value
    FROM customer_data
    GROUP BY customer_id, nombre, email, pais
    HAVING COUNT(DISTINCT order_id) >= 3
)
SELECT 
    a.nombre,
    a.email,
    a.pais,
    a.total_orders,
    a.total_revenue,
    a.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM aggregated_data a
JOIN category_rank cr ON a.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY a.total_revenue DESC
LIMIT 10;

Wait, but in aggregated_data, we're grouping by customer_id, nombre, email, pais. Because in the customer_data CTE, those columns are selected, but when grouping, we need to group by all non-aggregated columns. So yes, in aggregated_data, the GROUP BY should include customer_id, nombre, email, pais.

But maybe the customer_id is unique per customer, so the nombre, email, pais would be the same for each customer_id, so grouping by customer_id is sufficient