# Seed 2.0 Code — code_generation/sql_query_complex

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.09 | quality: 7.96
- latency_total: 38.77s | tokens_per_second: 52.8
- input_tokens: 182 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, abordando los requisitos de la consulta SQL compleja con un enfoque estructurado. Ofrece una buena profundidad al considerar diferentes aspectos de la consulta, como el cálculo de métricas y la lógica de filtrado. La claridad es alta, con una explicación paso a paso que facilita la comprensión. Es útil para un emprendedor, ya que proporciona una base sólida para implementar la consulta SQL.

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


Okay, let's tackle this SQL query step by step. First, I need to remember all the requirements. Let's list them again to make sure I don't miss anything.

First, the tables involved: orders, customers, order_items, products. The output needs to be top 10 customers by total revenue last 6 months, columns: nombre (customer name), email, pais (country), total_orders, total_revenue, avg_order_value, categoria_mas_comprada (most bought category). Also, only customers with at least 3 completed orders, ordered by total_revenue DESC, top 10.

First, let's break down each part. First, the base: customers and their completed orders in the last 6 months. Let's start with filtering orders first: status = 'completed', created_at in the last 6 months. Wait, how to calculate last 6 months? Depends on SQL dialect, but standard is something like created_at >= CURRENT_DATE - INTERVAL '6 months'? Or DATE_SUB for MySQL, but maybe use standard or note, but let's make it as common as possible, maybe mention dialect notes later.

First, the filters:
1. Orders: status = 'completed'
2. Orders created in last 6 months
3. Customers have COUNT(DISTINCT orders.id) >= 3, right? Because total_orders is the count of their completed orders in that period? Wait yes, total_orders is the number of orders they have here.

Now, the metrics:
- total_revenue: sum of (quantity * unit_price) from order_items for their orders? Wait wait, wait: the orders table has a 'total' column. Wait, which one to use? Oh, but order_items has quantity and unit_price, which should add up to the order's total. But maybe better to use order_items to calculate revenue per product, but also total revenue. Wait, but let's confirm: total_revenue is the total money the customer spent, right? So either sum(orders.total) for their completed orders, or sum(order_items.quantity * order_items.unit_price). Which is better? Well, if orders.total is reliable, that's easier, but when we need to get categories, we have to join order_items and products anyway, so maybe calculate total_revenue from order_items to be consistent? Wait but maybe orders.total is after taxes or discounts? Hmm, the problem says "revenue total", so probably either is okay, but let's note that, but let's see: let's first structure the joins.

First, the joins needed: customers JOIN orders ON customers.id = orders.customer_id, then order_items ON orders.id = order_items.order_id, then products ON order_items.product_id = products.id. But wait, we have two types of aggregations here: one is customer-level metrics (total_orders, total_revenue, avg_order_value) and another is per customer per category to get the most bought category. Oh right, that's the tricky part: categoria_mas_comprada, which is the category the customer bought the most of. How to calculate that?

So first, let's split the problem into two parts:
1. Calculate all the customer-level aggregates (name, email, country, total_orders, total_revenue, avg_order_value) for eligible customers (>=3 completed orders, last 6 months).
2. Calculate for each customer, their most purchased category.
Then join these two parts together, then take top 10 by total_revenue DESC.

Wait, but how to calculate most purchased category? What's "most bought"? By quantity? By revenue? The problem says "categoria_mas_comprada", which usually is by number of units, or maybe number of orders? Wait no, let's check the order_items: each line is quantity of a product. So most bought would be sum(quantity) per category per customer, highest sum. Or maybe sum of revenue per category? The problem doesn't specify, so we need to define that in comments, say "asumiendo que 'mas comprada' es por cantidad total de unidades, se puede ajustar por revenue si es necesario".

Okay, so let's outline step by step:

First, filter the orders first:
- orders.status = 'completed'
- orders.created_at >= (fecha actual menos 6 meses). Let's use standard SQL: CURRENT_DATE - INTERVAL '6 months', but note that for MySQL it's DATE_SUB(CURDATE(), INTERVAL 6 MONTH), for SQL Server DATEADD(month, -6, GETDATE()), etc. But let's use standard first, mention dialects.

Next, eligible customers: those with COUNT(DISTINCT orders.id) >=3 in that period.

Now, customer-level metrics:
- nombre: customers.name
- email: customers.email
- pais: customers.country
- total_orders: COUNT(DISTINCT orders.id) → because each order is unique, count of completed orders for the customer in the period.
- total_revenue: let's see, if we use order_items: SUM(order_items.quantity * order_items.unit_price). Or SUM(orders.total). Wait, but if an order has no items? Unlikely, but to be consistent, since we need order_items for categories, let's use SUM(oi.quantity * oi.unit_price) as total_revenue. But let's note that if orders.total is the correct value (including taxes, discounts, etc.), we can use SUM(o.total) instead.
- avg_order_value: total_revenue / total_orders, right? Because average order value is total spent divided by number of orders. Or AVG(o.total) if we use orders.total. That makes sense.

Now, the tricky part: categoria_mas_comprada. Let's think: for each customer, group their order items by product category, sum the quantity (or revenue, but let's pick quantity first, note that), then rank the categories per customer, then pick the top one.

How to do that? Window functions! We can use ROW_NUMBER() or RANK() partitioned by customer id, ordered by sum of quantity descending. That way, the top category gets row number 1.

But wait, what if there's a tie? Like two categories with same sum. Then ROW_NUMBER() will pick one arbitrarily, RANK() will give both 1. The problem says "categoria_mas_comprada", singular, so maybe we need to handle ties, maybe pick the first alphabetically, or note that. Let's adjust the ORDER BY in the window function to handle ties: ORDER BY sum_quantity DESC, category ASC, so if tie, pick the one that comes first alphabetically.

Okay, so let's structure the CTEs (Common Table Expressions) because this is complex, CTEs make it readable. Let's list the CTEs we need:

1. First CTE: customer_order_metrics. This is to get the customer-level metrics (total_orders, total_revenue, avg_order_value) and filter eligible customers (>=3 completed orders, last 6 months). Wait, but we need to make sure that we only count completed orders in the last 6 months, right?

Wait, let's define first the base data: all completed orders in last 6 months, linked to customers, order items, products. Let's maybe have a base CTE? Or split into:

CTE 1: valid_orders. This gets all orders that are completed and in the last 6 months. Columns: order_id, customer_id, order_total (o.total), order_date.
Definition:
SELECT id AS order_id, customer_id, total AS order_total, created_at
FROM orders
WHERE status = 'completed'
AND created_at >= CURRENT_DATE - INTERVAL '6 months';

CTE 2: customer_order_agg. This aggregates per customer from valid_orders, gets total_orders, total_revenue (either sum of order totals or sum of order items, let's pick sum of order totals first? Wait no, wait we need order items for categories, so maybe another CTE that joins valid_orders with order_items and products.

CTE 3: customer_category_data. This joins valid_orders with order_items and products, to get per customer, per category, the total quantity bought, total revenue per category.
Definition:
SELECT 
    vo.customer_id,
    p.category,
    SUM(oi.quantity) AS total_quantity_category,
    SUM(oi.quantity * oi.unit_price) AS total_revenue_category
FROM valid_orders vo
JOIN order_items oi ON vo.order_id = oi.order_id
JOIN products p ON oi.product_id = p.id
GROUP BY vo.customer_id, p.category;

Then, CTE 4: customer_top_category. This ranks the categories per customer, picks the top one.
Definition:
SELECT 
    customer_id,
    category AS categoria_mas_comprada,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id 
        ORDER BY total_quantity_category DESC, category ASC
    ) AS rn
FROM customer_category_data
-- We want only the top one, so filter rn=1 later
QUALIFY rn = 1; -- Wait, QUALIFY is supported in BigQuery, Snowflake, PostgreSQL 13+, but not all. Oh right, for older PostgreSQL or MySQL, we need to use a subquery or CTE and filter rn=1. So better to not use QUALIFY, just make the CTE have rn, then filter where rn=