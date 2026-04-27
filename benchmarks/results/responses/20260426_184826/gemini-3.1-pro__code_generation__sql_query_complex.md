# Gemini 3.1 Pro — code_generation/sql_query_complex

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 6.57 | quality: 7.92
- latency_total: 17.894s | tokens_per_second: 114.2
- input_tokens: 161 | output_tokens: 2044
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para resolver esta consulta de manera eficiente y limpia, la mejor estrategia es usar **CTEs (Common Table Expressions)**. Esto nos permite separar el cálculo de las métricas de las órdenes por un lado, y el cálculo de la categoría más comprada (usando *Window Functions*) por el otro.

Aquí tienes la query SQL (escrita en estándar SQL/PostgreSQL, que es compatible con la mayoría de motores modernos):

```sql
WITH OrderStats AS (
    -- 1. Calculamos las métricas principales por cliente (últimos 6 meses, completadas, min 3 órdenes)
    SELECT 
        customer_id,
        COUNT(id) AS total_orders,
        SUM(total) AS total_revenue,
        ROUND(AVG(total), 2) AS avg_order_value
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY customer_id
    HAVING COUNT(id) >= 3
),
CategoryRanking AS (
    -- 2. Contamos cuántos productos de cada categoría compró cada cliente en ese periodo
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) as rank
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
