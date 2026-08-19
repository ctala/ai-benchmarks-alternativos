# MiniMax M2.7 (directo) — code_generation/sql_query_complex

- model_id: `MiniMax-M2.7`
- success: True  | final: 6.12 | quality: 6.32
- latency_total: 33.42s | tokens_per_second: 61.3
- input_tokens: 181 | output_tokens: 2048
- judge_score: 3.0 | justificación: 

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

# Query SQL - Top 10 Clientes por Revenue

```sql
WITH orders_last_6_months AS (
    -- Paso 1: Órdenes completadas de los últimos 6 meses
    SELECT 
        id,
        customer_id,
        total
    FROM orders
    WHERE created_at >= CURRENT_DATE - INTERVAL '6 months'
      AND status = 'completed'
),
customer_totals AS (
    -- Paso 2: Métricas agregadas por cliente (min 3 órdenes)
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    INNER JOIN orders_last_6_months o ON c.id = o.customer_id
    GROUP BY c.id, c.name,