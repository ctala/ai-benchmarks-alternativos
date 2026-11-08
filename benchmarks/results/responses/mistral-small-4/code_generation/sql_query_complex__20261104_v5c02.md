# Mistral Small 4 — code_generation/sql_query_complex

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 9.28 | quality: 9.8
- latency_total: 4.433s | tokens_per_second: 150.9
- input_tokens: 159 | output_tokens: 669
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y ofrece una solución completa y bien estructurada que un emprendedor podría usar directamente, con una explicación clara de cada parte de la consulta.

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

Aquí tienes la consulta SQL que resuelve tu requerimiento:

```sql
WITH customer_orders AS (
    SELECT
        c.id AS customer_id,
        c.name AS customer_name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM
        customers c
    JOIN
        orders o ON c.id = o.customer_id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        c.id, c.name, c.email, c.country
    HAVING
        COUNT(o.id) >= 3
),

top_categories AS (
    SELECT
        o.customer_id,
        p.category AS top_category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue,
        RANK() OVER (PARTITION BY o.customer_id ORDER BY SUM(oi.quantity * oi.unit_price) DESC) AS category_rank
    FROM
        orders o
    JOIN
        order_items oi ON o.id = oi.order_id
    JOIN
        products p ON oi.product_id = p.id
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
    GROUP BY
        o.customer_id, p.category
)

SELECT
    co.customer_name,
    co.email,
    co.country,
    co.total_orders,
    co.total_revenue,
    ROUND(co.avg_order_value, 2) AS avg_order_value,
    tc.top_category AS categoria_mas_comprada
FROM
    customer_orders co
JOIN
    top_categories tc ON co.customer_id = tc.customer_id AND tc.category_rank = 1
ORDER BY
    co.total_revenue DESC
LIMIT 10;
```

Explicación:

1. **customer_orders**: CTE que calcula las métricas principales por cliente:
   - Nombre, email y país del cliente
   - Total de órdenes completadas
   - Revenue total (suma de todos los pedidos)
   - Valor promedio por orden
   - Filtra por órdenes completadas en los últimos 6 meses
   - Solo incluye clientes con al menos 3 órdenes

2. **top_categories**: CTE que identifica la categoría más comprada por cada cliente:
   - Calcula el revenue por categoría para cada cliente
   - Usa RANK() para identificar la categoría principal
   - Solo mantiene la categoría con rank = 1 (la más comprada)

3. La consulta final:
   - Une los resultados de ambos CTEs
   - Selecciona solo las columnas requeridas
   - Redondea el valor promedio de la orden
   - Ordena por revenue total descendente
   - Limita a los top 10 clientes

Nota: Asegúrate de que el campo `status` en la tabla orders realmente use el valor 'completed' para órdenes terminadas. Si usa otro valor como 'completed' o 'ship', ajusta la consulta en consecuencia.