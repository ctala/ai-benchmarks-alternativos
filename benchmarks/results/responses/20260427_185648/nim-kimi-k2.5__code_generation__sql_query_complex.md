# Kimi K2.5 (NIM) — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 6.27 | quality: 5.92
- latency_total: 56.258s | tokens_per_second: 36.4
- input_tokens: 156 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

 Aquí tienes la query SQL (compatible con MySQL 8.0+, PostgreSQL o SQL Server con ajustes mínimos):

```sql
WITH customer_metrics AS (
    -- Calcular métricas de órdenes por cliente
    SELECT 
        o.customer_id,
        COUNT(*) as total_orders,
        SUM(o.total) as total_revenue
    FROM orders o
    WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)  -- MySQL
    -- Para PostgreSQL: AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    -- Para SQL Server: AND o.created_at >=