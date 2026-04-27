# Grok 4.20 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.20`
- success: True  | final: 7.48 | quality: 9.24
- latency_total: 9.27s | tokens_per_second: 42.4
- input_tokens: 263 | output_tokens: 393
- judge_score: 4.6 | justificación: 

## Respuesta completa

**✅ Query SQL optimizada:**

```sql
WITH customer_stats AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) as total_orders,
        SUM(o.total) as total_revenue,
        ROUND(AVG(o.total), 2) as avg_order_value,
        MAX(o.created_at) as last_order_date,
        -- Categoría más comprada
        FIRST_VALUE(p.category) OVER (
            PARTITION BY c.id 
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC
        ) as categoria_mas_comprada
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
      AND o.status = 'completed'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
)

SELECT 
    name,
    email,
    country,
    total_orders,
    total_revenue,
    avg_order_value,
    categoria_mas_comprada
FROM customer_stats
ORDER BY total_revenue DESC
LIMIT 10;
```

### Notas importantes:

- Usa `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` para los últimos 6 meses (MySQL).
- Si estás usando **PostgreSQL**, reemplaza la parte de fecha por:
  ```sql
  o.created_at >= CURRENT_DATE - INTERVAL '6 months'
  ```

- La columna `categoria_mas_comprada` considera el **revenue** generado por categoría (no solo cantidad).

---

¿Quieres también una versión para **PostgreSQL** o con **ventana para obtener la categoría más comprada de forma más robusta**?