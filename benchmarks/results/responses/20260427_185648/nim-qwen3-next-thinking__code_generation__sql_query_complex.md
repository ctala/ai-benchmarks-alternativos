# Qwen 3-Next 80B Thinking (NIM) — code_generation/sql_query_complex

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.68 | quality: 7.36
- latency_total: 19.392s | tokens_per_second: 105.6
- input_tokens: 152 | output_tokens: 2048
- judge_score: 3.4 | justificación: 

## Respuesta completa

Okay, let's see. I need to write an SQL query that shows the top 10 customers by total revenue in the last 6 months. The columns required are nombre, email, pais, total_orders, total_revenue, avg_order_value, and categoria_mas_comprada. They also need to be ordered by total_revenue descending, and only customers with at least 3 completed orders.

First, let me break down the requirements. The data comes from multiple tables: orders, customers, order_items, products. So I'll need to join these tables.

The main tables involved are customers and orders. But to get revenue, I need to look at order_items and products because revenue per order would be quantity * unit_price for each item, then summed up per order. Wait, but the orders table has a total column. Hmm, maybe the total in orders is already the sum of the order_items. But maybe not. The problem says "revenue total", so perhaps the total in orders is the total for the order. But maybe the order_items have unit_price and quantity, so the revenue for each item is quantity * unit_price, and the order's total would be the sum of those. However, the orders table does have a 'total' column. Maybe that's the total revenue for the order. So perhaps we can just use orders.total for each order.

But the question says "top 10 clientes por revenue total", so maybe the total revenue is the sum of orders.total for each customer. However, the problem also says "only customers with at least 3 ordenes completadas (status = 'completed')". So first, we need to filter orders with status 'completed', and count the number of completed orders per customer, then only include those with count >=3.

Wait, but the problem says "al menos 3 ordenes completadas", so status='completed' and count of orders per customer >=3.

Now, the time frame is "ultimos 6 meses", so created_at >= current date minus 6 months. Depending on the SQL dialect, but usually it's something like DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH) or NOW() - INTERVAL 6 MONTH.

So first, join orders and customers. Then, for each customer, sum their orders' total where status is 'completed' and created_at is in the last 6 months. But also need to count the number of completed orders.

But also, the category_mas_comprada: the most purchased category. So for each customer, what's the category that has the highest total quantity or highest revenue? Wait, the problem says "categoria_mas_comprada", which translates to "most purchased category". So probably the category with the highest total quantity or highest revenue. But the problem doesn't specify, but typically "most purchased" would be the category with the highest count of items sold, or highest revenue from that category. But maybe it's the category that the customer bought the most items from. Let me check the problem statement again. The column is "categoria_mas_comprada", which is "most purchased category". So perhaps the category that the customer has ordered the most items from. So sum of quantity per category, and pick the category with highest sum.

But to get that, for each customer, we need to look at the order_items, join with products to get category, then group by category, sum the quantity, and pick the top category.

But how to get the top category for each customer. That's a bit tricky. Maybe using a subquery or a window function.

So the steps for the query:

1. Filter orders that are completed and within the last 6 months.

2. Join with customers to get customer details.

3. For each customer, calculate total_revenue (sum of orders.total), total_orders (count of orders), avg_order_value (total_revenue / total_orders).

4. For categoria_mas_comprada, need to find the category that has the highest sum of quantity for that customer.

But how to do that.

Let me think. So for each customer, we need to look at all their completed orders in the last 6 months, then for each order's items, join with products to get category, then sum the quantity per category, and then select the category with the maximum sum.

This can be done with a subquery or a CTE. Maybe using a window function like ROW_NUMBER() to rank the categories by quantity per customer.

So perhaps:

First, create a CTE that gets all the order items for completed orders in the last 6 months, then join with products to get category.

Then, for each customer, sum the quantity per category.

Then, for each customer, pick the category with the highest sum.

But how to get the top category per customer. So for each customer, order by sum(quantity) descending and pick the first.

So maybe:

WITH customer_categories AS (
    SELECT 
        c.id AS customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    JOIN customers c ON o.customer_id = c.id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id, p.category
),
ranked_categories AS (
    SELECT 
        customer_id,
        category,
        total_quantity,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC) AS rn
    FROM customer_categories
)
SELECT ... 

Then in the main query, for each customer, join with ranked_categories where rn =1 to get the top category.

But maybe also need to consider if multiple categories have same quantity, but probably the problem just wants one, so take the first one.

Now, putting it all together.

Also, need to ensure that the customer has at least 3 completed orders. So first, for each customer, count the number of completed orders in the last 6 months. So perhaps first filter customers with count >=3.

So the steps:

- Get the list of customers who have >=3 completed orders in the last 6 months.

- For each such customer, compute total_revenue (sum of orders.total), total_orders (count), avg_order_value (total_revenue / total_orders), and the top category.

So the query structure:

SELECT 
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    COUNT(o.id) AS total_orders,
    SUM(o.total) AS total_revenue,
    SUM(o.total) / COUNT(o.id) AS avg_order_value,
    (SELECT p.category 
     FROM order_items oi
     JOIN products p ON oi.product_id = p.id
     WHERE oi.order_id IN (SELECT id FROM orders WHERE customer_id = c.id AND status = 'completed' AND created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH))
     GROUP BY p.category
     ORDER BY SUM(oi.quantity) DESC
     LIMIT 1) AS categoria_mas_comprada
FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
GROUP BY c.id
HAVING COUNT(o.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;

But wait, the problem is that the subquery for categoria_mas_comprada might not be efficient. Also, the way the subquery is written, it might not correctly group by customer. Because for each customer, the subquery is selecting the category from their own orders.

Alternatively, maybe better to use a CTE for the top category.

But another problem: the customer might have multiple orders, and for each order, the items are in order_items. So to get the category per customer, we need to sum the quantities across all order_items for that customer.

So perhaps better to first aggregate the categories per customer.

Another approach: use a LEFT JOIN to get the category info, then group by customer and category, then rank.

Let me try to structure it properly.

First, let's get all completed orders in last 6 months:

SELECT 
    c.id AS customer_id,
    c.name,
    c.email,
    c.country,
    o.id AS order_id,
    o.total,
    oi.product_id,
    oi.quantity,
    p.category
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH);

Now, for each customer, sum the quantity per category.

Then, for each customer, find the category with highest sum.

So using a CTE.

WITH customer_orders AS (
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        o.id AS order_id,
        o.total,
        oi.quantity,
        p.category
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
),
category_counts AS (
    SELECT 
        customer_id,
        category,
        SUM(quantity) AS total_quantity
    FROM customer_orders
    GROUP BY customer_id, category
),
top_category AS (
    SELECT 
        customer_id,
        category,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC) AS rn
    FROM category_counts
)
SELECT 
    c.name AS nombre,
   