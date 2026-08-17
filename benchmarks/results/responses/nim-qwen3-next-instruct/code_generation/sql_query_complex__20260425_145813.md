# Qwen 3-Next 80B Instruct (NIM) — code_generation/sql_query_complex

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 7.6 | quality: 9.44
- latency_total: 12.157s | tokens_per_second: 52.0
- input_tokens: 150 | output_tokens: 632
- judge_score: 4.6 | justificación: 

## Respuesta completa

Claro, aquí tienes una consulta SQL que cumple con todos los requisitos que mencionaste:

```sql
SELECT 
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    COUNT(o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    AVG(oi.quantity * oi.unit_price) AS avg_order_value,
    (
        SELECT p2.category
        FROM orders o2
        JOIN order_items oi2 ON o2.id = oi2.order_id
        JOIN products p2 ON oi2.product_id = p2.id
        WHERE o2.customer_id = c.id 
          AND o2.status = 'completed'
        GROUP BY p2.category
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

1. **Join entre tablas**:  
   - `customers` → `orders` → `order_items` → `products` (para calcular revenue y obtener categoría).

2. **Filtros aplicados**:  
   - Solo órdenes con `status = 'completed'`.  
   - Solo órdenes de los últimos 6 meses (`created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`).  
   - Solo clientes con al menos 3 órdenes (`HAVING COUNT(o.id) >= 3`).

3. **Cálculos**:  
   - `total_revenue`: suma de `quantity * unit_price` para todas las órdenes del cliente.  
   - `avg_order_value`: promedio del valor de cada orden (suma de items por orden / número de órdenes).  
   - `total_orders`: número de órdenes completadas del cliente.

4. **Categoría más comprada**:  
   - Subconsulta correlacionada que, para cada cliente, agrupa por categoría de producto, suma el revenue por categoría y toma la que más generó ingresos (`LIMIT 1`).

5. **Orden y límite**:  
   - Ordenado por `total_revenue DESC` y limitado a los 10 primeros.

> ✅ **Nota**: Esta consulta asume que estás usando **MySQL** (por el uso de `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`). Si usas otro SGBD como PostgreSQL, SQL Server o SQLite, la sintaxis de fechas cambiaría ligeramente. ¿Quieres la versión para otro sistema?