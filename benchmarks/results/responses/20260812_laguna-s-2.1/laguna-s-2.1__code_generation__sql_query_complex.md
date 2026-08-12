# Poolside Laguna S 2.1 — code_generation/sql_query_complex

- model_id: `poolside/laguna-s-2.1`
- success: True  | final: 9.11 | quality: 9.8
- latency_total: 6.204s | tokens_per_second: 94.1
- input_tokens: 199 | output_tokens: 584
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos:

```sql
SELECT 
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id) AS avg_order_value,
    (
        SELECT p.category
        FROM order_items oi2
        JOIN orders o2 ON oi2.order_id = o2.id
        JOIN products p ON oi2.product_id = p.id
        WHERE o2.customer_id = c.id
          AND o2.status = 'completed'
          AND o2.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
        GROUP BY p.category
        ORDER BY SUM(oi2.quantity) DESC
        LIMIT 1
    ) AS categoria_mas_comprada
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
WHERE o.status = 'completed'
  AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY c.id, c.name, c.email, c.country
HAVING COUNT(DISTINCT o.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

Esta consulta:

1. **Filtra órdenes completadas** de los últimos 6 meses usando `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`
2. **Agrupa por cliente** para calcular métricas consolidadas
3. **Calcula todas las columnas requeridas**:
   - `total_orders`: Cuenta distinta de órdenes
   - `total_revenue`: Suma de (cantidad × precio unitario)
   - `avg_order_value`: Revenue total dividido por número de órdenes
   - `categoria_mas_comprada`: Subconsulta que encuentra la categoría con más unidades vendidas
4. **Filtra clientes con al menos 3 órdenes** usando `HAVING COUNT(DISTINCT o.id) >= 3`
5. **Ordena por revenue total descendente** y limita a 10 resultados

La subconsulta para `categoria_mas_comprada` asegura que solo considere órdenes completadas de los últimos 6 meses, manteniendo consistencia con el filtro principal.