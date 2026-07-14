# Qwen 3-Next 80B Instruct — code_generation/sql_query_complex

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 8.862s | tokens_per_second: 87.1
- input_tokens: 153 | output_tokens: 772
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos solicitados:

```sql
SELECT 
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    COUNT(o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    ROUND(
        AVG(oi.quantity * oi.unit_price), 
        2
    ) AS avg_order_value,
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
  AND o.created_at >= NOW() - INTERVAL '6 months'
GROUP BY c.id, c.name, c.email, c.country
HAVING COUNT(o.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

### Explicación de la consulta:

1. **JOINs necesarios**:
   - `customers` → `orders` (para关联 cliente y sus órdenes)
   - `orders` → `order_items` (para obtener los productos y precios de cada orden)

2. **Filtros aplicados**:
   - `o.status = 'completed'`: Solo órdenes completadas.
   - `o.created_at >= NOW() - INTERVAL '6 months'`: Últimos 6 meses (funciona en PostgreSQL; si usas MySQL o SQL Server, ajusta la sintaxis según tu DB).

3. **Agrupación**:
   - `GROUP BY c.id, c.name, c.email, c.country`: Agrupamos por cliente para calcular métricas por cliente.

4. **HAVING**:
   - `HAVING COUNT(o.id) >= 3`: Solo clientes con al menos 3 órdenes completadas.

5. **Cálculos**:
   - `SUM(oi.quantity * oi.unit_price)`: Revenue total por cliente.
   - `AVG(...)`: Valor promedio por orden (redondeado a 2 decimales).
   - Subconsulta anidada: Para encontrar la categoría más comprada por cada cliente, sumando el revenue por categoría y tomando la que más aporta.

6. **Orden y límite**:
   - `ORDER BY total_revenue DESC LIMIT 10`: Top 10 por revenue.

---

### Nota sobre la subconsulta de `categoria_mas_comprada`:
- La subconsulta dentro del `SELECT` se ejecuta para cada cliente y devuelve la categoría con mayor revenue acumulado en sus órdenes completadas.
- Es eficiente y clara, aunque en bases de datos muy grandes puede optimizarse con `ROW_NUMBER()` si se usa PostgreSQL 13+ o similar.

### Adaptación para otros SGBD:

- **MySQL**: Cambia `INTERVAL '6 months'` por `DATE_SUB(NOW(), INTERVAL 6 MONTH)`
- **SQL Server**: Usa `DATEADD(MONTH, -6, GETDATE())`
- **Oracle**: Usa `ADD_MONTHS(SYSDATE, -6)`

Si me dices qué SGBD usas, te doy la versión específica.