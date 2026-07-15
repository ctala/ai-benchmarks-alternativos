# Claude Haiku 4.5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 8.81 | quality: 9.8
- latency_total: 4.879s | tokens_per_second: 187.3
- input_tokens: 178 | output_tokens: 914
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando tanto una solución directa como una alternativa más precisa para calcular la categoría más comprada.

## Respuesta completa

# Query SQL - Top 10 Clientes por Revenue

```sql
SELECT 
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue,
    ROUND(SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id), 2) AS avg_order_value,
    p.category AS categoria_mas_comprada
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
INNER JOIN order_items oi ON o.id = oi.order_id
INNER JOIN products p ON oi.product_id = p.id
WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY c.id, c.name, c.email, c.country
HAVING COUNT(DISTINCT o.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

## Explicación:

| Parte | Descripción |
|-------|-------------|
| **INNER JOINs** | Conecta todas las tablas necesarias |
| **WHERE** | Filtra por órdenes completadas en los últimos 6 meses |
| **GROUP BY** | Agrupa por cliente |
| **HAVING** | Filtra solo clientes con 3+ órdenes |
| **COUNT(DISTINCT o.id)** | Cuenta órdenes únicas por cliente |
| **SUM(oi.quantity * oi.unit_price)** | Calcula revenue total |
| **ROUND()** | Redondea a 2 decimales |
| **LIMIT 10** | Devuelve solo los top 10 |

---

## Versión alternativa con subconsulta (para la categoría más comprada)

Si necesitas más precisión en la categoría más comprada:

```sql
SELECT 
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) AS total_revenue,
    ROUND(SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id), 2) AS avg_order_value,
    (
        SELECT p.category
        FROM order_items oi2
        INNER JOIN products p ON oi2.product_id = p.id
        INNER JOIN orders o2 ON oi2.order_id = o2.id
        WHERE o2.customer_id = c.id 
            AND o2.status = 'completed'
            AND o2.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
        GROUP BY p.category
        ORDER BY SUM(oi2.quantity) DESC
        LIMIT 1
    ) AS categoria_mas_comprada
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id
INNER JOIN order_items oi ON o.id = oi.order_id
WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY c.id, c.name, c.email, c.country
HAVING COUNT(DISTINCT o.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

**Nota:** La subconsulta en SELECT es más precisa pero más lenta. Usa la primera versión si el rendimiento es crítico.