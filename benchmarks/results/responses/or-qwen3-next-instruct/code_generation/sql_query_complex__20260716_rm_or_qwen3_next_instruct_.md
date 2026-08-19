# Qwen 3-Next 80B Instruct — code_generation/sql_query_complex

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.15 | quality: 9.8
- latency_total: 4.062s | tokens_per_second: 180.2
- input_tokens: 153 | output_tokens: 732
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos especificados:

```sql
SELECT 
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    COUNT(o.id) AS total_orders,
    SUM(o.total) AS total_revenue,
    AVG(o.total) AS avg_order_value,
    (
        SELECT p.category
        FROM order_items oi2
        JOIN products p ON oi2.product_id = p.id
        WHERE oi2.order_id IN (
            SELECT o2.id 
            FROM orders o2 
            WHERE o2.customer_id = c.id 
              AND o2.status = 'completed'
        )
        GROUP BY p.category
        ORDER BY SUM(oi2.quantity * oi2.unit_price) DESC
        LIMIT 1
    ) AS categoria_mas_comprada
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
WHERE o.status = 'completed'
  AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY c.id, c.name, c.email, c.country
HAVING COUNT(o.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

### Explicación de la consulta:

- **`JOIN` entre tablas**: Conectamos `customers` → `orders` → `order_items` para obtener todos los datos necesarios.
- **Filtros**:
  - `o.status = 'completed'`: Solo órdenes completadas.
  - `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`: Últimos 6 meses (asumiendo MySQL; si usas otro DB, ajusta la función de fechas).
- **Agrupación**: Por cliente (`c.id`) para calcular métricas por cliente.
- **`HAVING COUNT(o.id) >= 3`**: Solo clientes con al menos 3 órdenes completadas.
- **`SUM(o.total)`**: Revenue total del cliente.
- **`AVG(o.total)`**: Valor promedio por orden.
- **Subconsulta anidada para `categoria_mas_comprada`**:
  - Busca la categoría más comprada por el cliente en sus órdenes completadas, calculando el revenue por categoría (cantidad × precio unitario).
  - Ordena por revenue descendente y toma solo la primera (`LIMIT 1`).
- **Ordenamiento y límite**: Por `total_revenue DESC` y solo top 10.

### Notas importantes:

- **`o.total`** se asume que ya contiene el total de la orden (incluyendo impuestos, descuentos, etc.), como sugiere el nombre del campo. Si en realidad `o.total` es solo la suma de `quantity * unit_price` sin calcular, podrías reemplazarlo por `SUM(oi.quantity * oi.unit_price)` en lugar de `SUM(o.total)`. Pero según tu esquema, `orders.total` parece ser un campo calculado, así que lo usamos directamente.
- Si usas **PostgreSQL**, reemplaza `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` por `CURRENT_DATE - INTERVAL '6 months'`.
- Si usas **SQL Server**, usa `DATEADD(MONTH, -6, GETDATE())`.

Esta consulta es eficiente y escalable para el escenario descrito.