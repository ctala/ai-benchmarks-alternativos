# Ministral 14B — code_generation/sql_query_complex

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 14.581s | tokens_per_second: 50.7
- input_tokens: 147 | output_tokens: 739
- judge_score: 5.0 | justificación: 

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

# Query SQL para Top 10 clientes por revenue en últimos 6 meses

```sql
WITH
-- Filtrar órdenes completadas en los últimos 6 meses
recent_completed_orders AS (
    SELECT
        o.id AS order_id,
        o.customer_id,
        o.total AS order_total,
        o.created_at
    FROM
        orders o
    WHERE
        o.status = 'completed'
        AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
),

-- Calcular revenue por cliente y categoría
customer_revenue_by_category AS (
    SELECT
        rco.customer_id,
        p.category AS product_category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue
    FROM
        recent_completed_orders rco
    JOIN
        order_items oi ON rco.order_id = oi.order_id
    JOIN
        products p ON oi.product_id = p.id
    GROUP BY
        rco.customer_id, p.category
),

-- Obtener la categoría más comprada por cliente
top_category_per_customer AS (
    SELECT
        customer_id,
        product_category AS categoria_mas_comprada,
        category_revenue AS top_category_revenue
    FROM
        customer_revenue_by_category
    WHERE
        (customer_id, category_revenue) IN (
            SELECT
                customer_id,
                MAX(category_revenue)
            FROM
                customer_revenue_by_category
            GROUP BY
                customer_id
        )
),

-- Agregar datos del cliente
customer_stats AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT rco.order_id) AS total_orders,
        SUM(rco.total) AS total_revenue,
        AVG(rco.total) AS avg_order_value,
        tc.categoria_mas_comprada
    FROM
        customers c
    JOIN
        recent_completed_orders rco ON c.id = rco.customer_id
    LEFT JOIN
        top_category_per_customer tc ON c.id = tc.customer_id
    GROUP BY
        c.id, c.name, c.email, c.country, tc.categoria_mas_comprada
    HAVING
        COUNT(DISTINCT rco.order_id) >= 3
)

-- Seleccionar los top 10 clientes
SELECT
    name,
    email,
    country,
    total_orders,
    total_revenue,
    ROUND(avg_order_value, 2) AS avg_order_value,
    categoria_mas_comprada
FROM
    customer_stats
ORDER BY
    total_revenue DESC
LIMIT 10;
```

## Explicación:

1. **recent_completed_orders**: Filtra solo órdenes completadas en los últimos 6 meses
2. **customer_revenue_by_category**: Calcula el revenue por categoría para cada cliente
3. **top_category_per_customer**: Identifica la categoría con mayor revenue para cada cliente
4. **customer_stats**: Agrupa toda la información del cliente con sus métricas:
   - Total de órdenes
   - Revenue total
   - Valor promedio de pedido
   - Categoría más comprada
   - Solo incluye clientes con ≥3 órdenes completadas
5. **Resultado final**: Ordena por revenue descendente y limita a los 10 primeros

Nota: El valor promedio de pedido se redondea a 2 decimales para mejor presentación. Si necesitas más precisión, puedes eliminar el ROUND().