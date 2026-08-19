# Qwen 3-Next 80B Thinking — code_generation/sql_query_complex

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 7.34 | quality: 7.72
- latency_total: 11.888s | tokens_per_second: 172.3
- input_tokens: 155 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

Okay, let's tackle this SQL query. So the user wants the top 10 customers by total revenue in the last 6 months. The columns needed are name, email, country, total_orders, total_revenue, avg_order_value, and categoria_mas_comprada. They also need to have at least 3 completed orders. And sort by total_revenue descending.

First, I need to figure out how to get the revenue. Revenue comes from the order_items, which has quantity and unit_price. So for each order, the total revenue would be sum(quantity * unit_price). But the 'orders' table has a 'total' column. Wait, maybe the 'total' in orders is already the sum of order Items. But maybe not necessarily. The problem says "revenue total", so probably the sum of order_items' (quantity * unit_price) per order.

But the 'orders' table has a 'total' column. Maybe that's the total for that order. So perhaps we can use that. But to be safe, maybe we should calculate it from order_items. However, the problem might expect using the ' total' in orders. Let me check the schema again.

 orders table has id, customer_id, total, status, created_at. So 'total' is per order. So for each order, the 'total' field is the total revenue for that order. So to get total_revenue for a customer, we can sum the 'total' from orders where status is 'completed' and created_at is within last 6 months.

But the user says "top 10 customers by revenue total in the last 6 months", so we need to filter orders created in last 6 months, and only completed ones.

Wait, the ' status = 'completed' ' is part of the condition for the orders. So for the customer's total_revenue, we only consider completed orders in the last 6 months.

But the ' total_orders' is the count of completed orders in that period. So for each customer, we need to count the number of completed orders in the last 6 months, and only include those with at least 3.

So first step: join orders with customers, and order_items maybe for some parts. Wait, but for total_re Revenue, if ' orders.total' is the total per order, then we can just sum that from the orders table. So for total_revenue: sum(orders.total) for completed orders in last 6 months.

Similarly, total_orders is count(orders.id) for those orders.

 avg_order_value would be total_revenue / total_orders.

 Now, the 'categoria_mas_comprada' (most bought category). So for each customer, we need to find the category that they've ordered the most. That would involve looking at order_items, which has product_id. Then products table has category. So for each customer, sum the quantities per category, then pick the category with highest sum.

So to get the most bought category, we need to join order_items with products to get the category, then group by customer and category, sum the quantities, then pick the top category per customer.

But how to get that in the main query.

So the query structure:

- Start with customers, join with orders (filtering for status 'completed' and created within last 6 months), then join order_items and products for the category part.

But for the top 10, we need to aggregate per customer.

Let's break it down.

First, for the main aggregations ( total_orders, total_re revenue, avg_order_value):

SELECT c.name, c.email, c.country, COUNT(o.id) as total_orders, SUM(o.total) as total_revenue, SUM(o.total) / COUNT(o.id) as avg_order_value

FROM customers c
JOIN orders o ON c.id = o.customer_id
WHERE o.status = 'completed' AND o.created_at >= NOW() - INTERVAL '6 months'
GROUP BY c.id, c.name, c.email, c.country
HAV COUNT(o.id) >= 3
ORDER by total_revenue DESC
LIMIT 10

But then we need to add 'categoria_mas_comprada'. That's a bit more complex.

For the most bought category per customer, we need to:

- For each customer, get all their order items (from completed orders in last 6 months), join with products to get category.

- Then for each customer and category, sum the quantities.

- Then pick the category with the highest sum.

So, for example, in a subquery or CTE.

So perhaps:

We can create a CTE to get the most bought category for each customer.

But how to integrate that into the main query.

Alternatively, in the main query, for each customer, find the category with the highest sum of quantities.

But SQL can't directly do that in the SELECT clause. We need to aggregate per customer and category, then pick the top one.

One way is to use a subquery or a CTE for the most bought category.

Let's try:

First, for the main part, get the top 10 customers with total_orders, etc., then join with a subquery that gets the most bought category for each customer.

But how to get the most bought category for each customer.

For example:

SELECT customer_id, category
FROM (
 SELECT oi.customer_id, p.category, SUM(oi.quantity) as total_quantity,
 ROW_NUMBER() OVER (PARTITION by customer_id ORDER by SUM(oi.quantity) DESC) as rn
 FROM order_items oi
 JOIN products p ON oi.product_id = p.id
 JOIN orders o ON oi.order_id = o.id
 WHERE o.status = 'completed' AND o.created_at >= NOW() - INTERVAL '6 months'
 GROUP by customer_id, p.category
) as sub
WHERE rn = 1

But wait, in order_items, there's no customer_id directly. Because order_items has order_id, and the order has customer_id. So to get the customer_id, need to join with orders.

So in the subquery for the most bought category:

- We need to join order_items with orders to get the customer_id from the order.

So the subquery would:

- from order_items, join with orders (to get customer_id and check status and created_at), then join with products to get category.

Then group by customer_id and category, sum quantities, then for each customer, select the category with the highest sum.

So in the main query, we can left join this result to get the most bought category.

So putting it all together:

First, the main query for the top 10 customers with their stats ( total_orders, etc.), then join with the most bought category.

But let's structure the query step by step.

First, the main SELECT:

SELECT c.name, c.email, c.country, 
 COUNT(o.id) as total_orders, 
 SUM(o.total) as total_revenue, 
 SUM(o.total) / COUNT(o.id) as avg_order_value,
 most.category as categoria_mas_comprada
FROM customers c
JOIN orders o ON c.id = o.customer_id
LEFT JOIN ( 
 ... subquery for most bought category ...
) as most ON c.id = most.customer_id
WHERE o.status = 'completed' 
 AND o.created_at >= NOW() - INTERVAL '6 months'
 GROUP by c.id, c.name, c.email, c.country, most.category
HAVing COUNT(o.id) >= 3
ORDER by total_revenue DESC
LIMIT 10

Wait, but the 'most' CTE would have a customer_id and category. But in the main query, when we group by c.id, etc., the ' most.category' would be from the joined subquery. But the problem is that the ' most' subquery, for each customer, has one row (the top category). So the LEFT JOIN would add that category.

But in the main query, the grouping is by c.id, and the ' most' is a single row per customer, so it's okay.

But in the HAVING clause, we need to count the number of completed orders for each customer. So the main query's grouping is per customer, so the COUNT(o.id) is correct.

But in the ' most' subquery, we need to make sure that we only consider the same time period and status.

Let's write the subquery for ' most':

SELECT customer_id, category
FROM (
 SELECT o.customer_id, p.category, SUM(oi.quantity) as total_quantity,
 ROW_NUMBER() OVER (PARTITION by o.customer_id ORDER by SUM(oi.quantity) DESC) as rn
 FROM order_items oi
 JOIN products p on oi.product_id = p.id
 JOIN orders o ON oi.order_id = o.id
 WHERE o.status = 'completed' 
 AND o.created_at >= NOW() - INTERVAL '6 months'
 GROUP BY o.customer_id, p.category
) as sub
WHERE rn = 1

Yes. So this subquery will give for each customer, the category with the highest sum of quantities in the last 6 months for completed orders.

Then, in the main query, we left join this on customer_id.

So putting it all together:

SELECT 
 c.name, 
 c.email, 
 c.country, 
 COUNT(o.id) as total_orders, 
 SUM(o.total) as total_re Revenue,
 SUM(o.total) / COUNT(o.id) as avg_order_value,
 most.category as categoria_mas_comprada
FROM 
 customers c
JOIN 
 orders o ON c.id = o.customer_id
LEFT JOIN (
 SELECT 
  customer_id, 
  category 
 from (
  SELECT 
   o.customer_id, 
   p.category, 
   SUM(oi.quantity) as total_quantity,
   ROW_NUMBER() OVER (PARTITION by o.customer_id ORDER by SUM(oi.quantity) DESC) as rn
  FROM 
   order_items oi 
  JOIN