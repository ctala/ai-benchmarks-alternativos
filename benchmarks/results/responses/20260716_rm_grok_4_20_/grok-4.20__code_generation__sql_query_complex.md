# Grok 4.20 — code_generation/sql_query_complex

- model_id: `x-ai/grok-4.20`
- success: True  | final: 8.98 | quality: 9.8
- latency_total: 4.08s | tokens_per_second: 149.3
- input_tokens: 324 | output_tokens: 609
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

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
        ROUND(SUM(o.total)::numeric / COUNT(DISTINCT o.id), 2) as avg_order_value,
        MODE() WITHIN GROUP (ORDER BY p.category) as categoria_mas_comprada
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.created_at >= CURRENT_DATE - INTERVAL '6 months'
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

### Notas sobre la query:

- Usa `CURRENT_DATE - INTERVAL '6 months'` para los últimos 6 meses (más preciso que `NOW()`).
- `MODE() WITHIN GROUP` es la forma más eficiente de obtener la **categoría más comprada**.
- Se calcula el `avg_order_value` a partir del `total` de la orden (no de los items individuales).
- Solo se consideran órdenes con `status = 'completed'`.
- El `HAVING` filtra correctamente clientes con al menos 3 órdenes completadas.

---

**Versión alternativa** (si tu base de datos no soporta `MODE()` — como MySQL 5.7 o inferior):

```sql
WITH customer_stats AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) as total_orders,
        SUM(o.total) as total_revenue,
        ROUND(SUM(o.total)::numeric / COUNT(DISTINCT o.id), 2) as avg_order_value,
        (ARRAY_AGG(p.category ORDER BY COUNT(*) DESC))[1] as categoria_mas_comprada
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.created_at >= CURRENT_DATE - INTERVAL '6 months'
      AND o.status = 'completed'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
)
SELECT *
FROM customer_stats
ORDER BY total_revenue DESC
LIMIT 10;
```

¿Quieres también una versión compatible con **MySQL 8.0**?