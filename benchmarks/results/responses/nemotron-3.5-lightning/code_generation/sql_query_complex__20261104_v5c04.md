# Nemotron 3.5 Lightning — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 8.96 | quality: 9.16
- latency_total: 3.156s | tokens_per_second: 204.7
- input_tokens: 160 | output_tokens: 646
- judge_score: 4.4 | justificación: 

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

Aquí tienes la consulta SQL. Estructura la consulta en capas: primero filtra los pedidos completados de los últimos 6 meses, luego agrupa por cliente para calcular las métricas solicitadas y finalmente une con la tabla de productos para determinar la categoría más comprada.

```sql
SELECT 
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(o.total) AS total_revenue,
    AVG(o.total) AS avg_order_value,
    (
        SELECT p2.category
        FROM order_items oi2
        JOIN products p2 ON oi2.product_id = p2.id
        WHERE oi2.order_id = o.id
        GROUP BY p2.category
        ORDER BY SUM(oi2.quantity) DESC
        LIMIT 1
    ) AS categoria_mas_comprada
FROM 
    customers c
JOIN 
    orders o ON c.id = o.customer_id
WHERE 
    o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
GROUP BY 
    c.id, c.name, c.email, c.country
HAVING 
    total_orders >= 3
ORDER BY 
    total_revenue DESC
LIMIT 10;
```

### Explicación de la query:

1.  **Filtrado (`WHERE`)**:
    *   `o.status = 'completed'`: Solo pedidos completados.
    *   `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`: Solo los últimos 6 meses.

2.  **Agrupación (`GROUP BY`)**:
    *   Agrupamos por cliente (`c.id`) para poder calcular totales y promedios.

3.  **Métricas calculadas**:
    *   `COUNT(DISTINCT o.id) AS total_orders`: Contamos los pedidos únicos por cliente.
    *   `SUM(o.total) AS total_revenue`: Suma del total de los pedidos.
    *   `AVG(o.total) AS avg_order_value`: Promedio del total de los pedidos.

4.  **Subquery para `categoria_mas_comprada`**:
    *   Dado que un cliente puede comprar productos de diferentes categorías en un solo pedido, y queremos la categoría "más comprada" a nivel general, la subquery recorre todos los `order_items` del cliente.
    *   Agrupa por categoría y selecciona la que tiene la mayor suma de cantidades (`SUM(oi2.quantity) DESC`), tomando solo la primera (`LIMIT 1`).

5.  **Filtrado final (`HAVING`)**:
    *   `total_orders >= 3`: Solo incluimos clientes que hayan tenido al menos 3 órdenes.

6.  **Ordenamiento y límite**:
    *   `ORDER BY total_revenue DESC`: De mayor a menor ingreso.
    *   `LIMIT 10`: Top 10 clientes.