# Qwen 3-Next 80B Instruct — code_generation/sql_query_complex

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 9.29 | quality: 10.0
- latency_total: 3.34s | tokens_per_second: 221.3
- input_tokens: 153 | output_tokens: 739
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL completa y bien estructurada que cumple con todos los requisitos especificados.

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

Aquí tienes la consulta SQL que cumple con todos los requisitos especificados:

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
   - `customers` → `orders` → `order_items` para obtener los detalles de las compras.
   - No se necesita un join directo con `products` para el cálculo del revenue (ya que `unit_price` está en `order_items`), pero sí se usa en la subconsulta para la categoría más comprada.

2. **Filtros**:
   - `o.status = 'completed'`: Solo órdenes completadas.
   - `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`: Últimos 6 meses (asumiendo MySQL; si usas otro DB, ajusta la función de fechas).

3. **Agrupación y agregación**:
   - `GROUP BY c.id, c.name, c.email, c.country`: Agrupa por cliente.
   - `COUNT(o.id)` → total_orders.
   - `SUM(oi.quantity * oi.unit_price)` → total_revenue.
   - `AVG(oi.quantity * oi.unit_price)` → avg_order_value.

4. **Subconsulta para `categoria_mas_comprada`**:
   - Para cada cliente, busca la categoría con mayor revenue total en sus órdenes completadas.
   - Usa una subconsulta correlacionada que agrupa por categoría y ordena por revenue descendente, tomando solo la primera (`LIMIT 1`).

5. **Filtro HAVING**:
   - `HAVING COUNT(o.id) >= 3`: Solo clientes con al menos 3 órdenes completadas.

6. **Orden y límite**:
   - `ORDER BY total_revenue DESC LIMIT 10`: Top 10 por revenue.

> ✅ **Nota**: Esta consulta está escrita para **MySQL**. Si estás usando otra base de datos (como PostgreSQL, SQL Server, etc.), la función de fechas cambiará:
> - **PostgreSQL**: `CURRENT_DATE - INTERVAL '6 months'`
> - **SQL Server**: `DATEADD(MONTH, -6, GETDATE())`

¿Quieres que la adapte a otro sistema de base de datos?