# Seed 2.1 Turbo — code_generation/sql_query_complex

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 6.65 | quality: 7.28
- latency_total: 38.475s | tokens_per_second: 53.2
- input_tokens: 197 | output_tokens: 2048
- judge_score: 4.0 | justificación: 

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


El usuario necesita una query SQL con varias condiciones, a continuación se detallan los requisitos del informe, las tablas involucradas y la lógica de filtrado preliminar: se requiere un ranking de los 10 clientes con mayor ingreso total en los últimos 6 meses, con columnas específicas, ordenado por ingreso total descendente, y solo se incluirán clientes con al menos 3 órdenes completadas. Se usarán las tablas orders, customers, order_items y products, y se filtrarán las órdenes completadas creadas en los últimos 6 meses. Se ha confirmado que se contarán las órdenes de forma única, y para calcular la categoría de producto más comprada por cada cliente será necesario unir las tablas de items de orden y productos.

I've clarified that order counting must use COUNT(DISTINCT) to avoid duplicate counts from multi-item orders. I've confirmed the most purchased product category will be calculated by unit sales, with tie-breaking handled via window functions, and I'll build the query in layers starting with joining order and order item data. For the customer-level metrics calculation, I will use the existing total order amount field from the orders table to ensure data consistency, and will strictly avoid duplicate counting issues when joining relevant tables.

I found that directly joining the orders and order_items tables would cause duplicate summation of order totals, so I've adjusted the query structure to use separate subqueries for customer order statistics and top product category calculation. The first subquery will aggregate order metrics from the orders table, and I've finalized its grouping rules and calculation logic.

I've added the HAVING COUNT(id) >= 3 filter to the first subquery to screen out eligible customers. I've also finalized the logic of the second subquery, which will calculate each customer's most purchased product category by unit sales, with revenue as an optional alternative.

To resolve tie-breaks in the top product category calculation, I'll use ROW_NUMBER() with a secondary alphabetical sort on category to ensure deterministic results, and later join the two subqueries with the customers table to get required customer details. The join logic between the two subqueries and the customers table has been confirmed, with INNER JOIN chosen as it is sufficient, and the 6-month order date filter will be added later.

I've confirmed the 6-month date filter has different implementations across SQL engines, with a cross-engine compatible version available that needs corresponding engine-specific notes. The exact value for the 'completed' order status is now finalized, and I'm starting to build the query step by step, having drafted the core fields for the order statistics subquery.
