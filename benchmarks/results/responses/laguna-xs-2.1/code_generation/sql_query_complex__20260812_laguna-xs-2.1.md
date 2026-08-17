# Poolside Laguna XS 2.1 — code_generation/sql_query_complex

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 9.08 | quality: 9.8
- latency_total: 15.494s | tokens_per_second: 192.1
- input_tokens: 171 | output_tokens: 2976
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y de gran utilidad práctica, cumpliendo con todos los requisitos de la consulta SQL solicitada.

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

Aquí tienes la consulta SQL que cumple con todos los requisitos:

```sql
SELECT 
    c.name,
    c.email,
    c.country,
    customer_stats.total_orders,
    customer_stats.total_revenue,
    ROUND(customer_stats.total_revenue / customer_stats.total_orders, 2) AS avg_order_value,
    top_category.category AS categoria_mas_comprada
FROM (
    SELECT 
        c.id AS customer_id,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue
    FROM customers c
    JOIN orders o 
        ON c.id = o.customer_id
        AND o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
    GROUP BY c.id
    HAVING COUNT(DISTINCT o.id) >= 3
) AS customer_stats
JOIN customers c 
    ON customer_stats.customer_id = c.id
LEFT JOIN (
    SELECT 
        customer_id,
        category,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC) AS rank
    FROM (
        SELECT 
            o.customer_id,
            p.category,
            SUM(oi.quantity) AS total_quantity
        FROM order_items oi
        JOIN orders o 
            ON oi.order_id = o.id
            AND o.status = 'completed'
            AND o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)
        JOIN products p 
            ON oi.product_id = p.id
        GROUP BY o.customer_id, p.category
    ) AS category_counts
) AS top_category 
    ON customer_stats.customer_id = top_category.customer_id 
    AND top_category.rank = 1
ORDER BY customer_stats.total_revenue DESC
LIMIT 10;
```

**Explicación detallada:**

1. **Subconsulta principal (`customer_stats`):**
   - Filtra órdenes completadas (`status = 'completed'`) en los últimos 6 meses
   - Agrupa por cliente para calcular:
     - `total_orders`: Cantidad de órdenes únicas
     - `total_revenue`: Suma de los totales de las órdenes
   - Usa `HAVING` para filtrar solo clientes con al menos 3 órdenes

2. **Cálculo de valor promedio:**
   - Se calcula como `total_revenue / total_orders` con redondeo a 2 decimales

3. **Subconsulta para categoría más comprada (`top_category`):**
   - Primero agrupa por cliente y categoría para sumar cantidades
   - Usa `ROW_NUMBER()` para ordenar categorías por cantidad descendente
   - Filtra solo la categoría con mayor cantidad (`rank = 1`)

4. **Joins y estructura final:**
   - Une los resultados con la tabla de clientes para obtener información personal
   - Usa LEFT JOIN para manejar casos donde no haya categorías (aunque no debería ocurrir con datos válidos)
   - Ordena por revenue descendente y limita a top 10

**Características clave:**
- Manejo correcto de fechas con `DATE_SUB`
- Uso de ventanas para obtener la categoría más relevante
- Filtrado previo de órdenes inválidas en ambas consultas
- Agregación precisa de cantidades y revenue
- Inclusión de todos los campos solicitados con nombres en español