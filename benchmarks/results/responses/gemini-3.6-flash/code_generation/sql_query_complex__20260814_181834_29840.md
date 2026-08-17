# Gemini 3.6 Flash — code_generation/sql_query_complex

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 6.91 | quality: 7.44
- latency_total: 9.522s | tokens_per_second: 214.7
- input_tokens: 161 | output_tokens: 2044
- judge_score: 3.8 | justificación: 

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

Aquí tienes la consulta SQL utilizando **CTEs (Common Table Expressions)** y **Funciones de Ventana (Window Functions)**. Esta estructura es la más eficiente y limpia, ya que evita duplicación de datos al calcular montos y obtener la categoría más comprada.

```sql
WITH filtered_orders AS (
    -- 1. Filtramos las órdenes completadas de los últimos 6 meses
    SELECT 
        id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 month'
),

customer_metrics AS (
    -- 2. Calculamos métricas por cliente y filtramos aquellos con al menos 3 órdenes
    SELECT 
        customer_id,
        COUNT(id) AS total_orders,
        SUM(total) AS total_revenue,
        ROUND(AVG(total), 2) AS avg_order_value
    FROM filtered_orders
    GROUP BY customer_id
    HAVING COUNT(id) >= 3
),

category_ranking AS (
    -- 3. Determinamos la categoría más comprada (por cantidad) para cada cliente
    SELECT 
        fo.customer_id,
        p.category,
        