# Llama 4 Maverick — code_generation/sql_query_complex

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 9.18 | quality: 10.0
- latency_total: 8.588s | tokens_per_second: 103.5
- input_tokens: 151 | output_tokens: 889
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

Para resolver este problema, debemos realizar una serie de pasos que involucran filtrar datos, realizar cálculos y unir tablas. A continuación, te proporciono la query SQL que debería cumplir con los requisitos solicitados.

### Paso 1: Entender las tablas y los campos necesarios

- **orders**: `id`, `customer_id`, `total`, `status`, `created_at`
- **customers**: `id`, `name`, `email`, `country`
- **order_items**: `id`, `order_id`, `product_id`, `quantity`, `unit_price`
- **products**: `id`, `name`, `category`

### Paso 2: Filtrar y calcular los datos necesarios

Necesitamos:
1. Filtrar órdenes completadas en los últimos 6 meses.
2. Calcular `total_orders`, `total_revenue`, y `avg_order_value` por cliente.
3. Identificar la categoría más comprada por cada cliente.

### Paso 3: Query SQL

```sql
WITH 
-- CTE para órdenes completadas en los últimos 6 meses
completed_orders AS (
    SELECT o.customer_id, o.id, o.total
    FROM orders o
    WHERE o.status = 'completed' AND o.created_at >= NOW() - INTERVAL 6 MONTH
),

-- CTE para calcular total_orders, total_revenue por cliente
customer_revenue AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(co.id) AS total_orders,
        SUM(co.total) AS total_revenue
    FROM customers c
    JOIN completed_orders co ON c.id = co.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(co.id) >= 3
),

-- CTE para calcular avg_order_value
avg_order_value_calc AS (
    SELECT 
        id,
        total_revenue / total_orders AS avg_order_value
    FROM customer_revenue
),

-- CTE para identificar la categoría más comprada por cliente
most_bought_category AS (
    SELECT 
        c.id,
        p.category,
        ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM customers c
    JOIN completed_orders co ON c.id = co.customer_id
    JOIN order_items oi ON co.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY c.id, p.category
)

SELECT 
    cr.name,
    cr.email,
    cr.country,
    cr.total_orders,
    cr.total_revenue,
    aov.avg_order_value,
    mbc.category AS categoria_mas_comprada
FROM customer_revenue cr
JOIN avg_order_value_calc aov ON cr.id = aov.id
JOIN most_bought_category mbc ON cr.id = mbc.id AND mbc.rn = 1
ORDER BY cr.total_revenue DESC
LIMIT 10;
```

### Explicación

1. **CTE (Common Table Expressions)**: Utilizamos CTEs para simplificar la query y hacerla más legible. 
   - `completed_orders`: Filtra órdenes completadas en los últimos 6 meses.
   - `customer_revenue`: Calcula `total_orders` y `total_revenue` por cliente, considerando solo aquellos con al menos 3 órdenes.
   - `avg_order_value_calc`: Calcula `avg_order_value` dividiendo `total_revenue` por `total_orders`.
   - `most_bought_category`: Identifica la categoría más comprada por cada cliente usando `ROW_NUMBER()` para ordenar y seleccionar la categoría con mayor cantidad comprada.

2. **JOINs y GROUP BY**: Unimos las tablas necesarias y agrupamos los datos según sea necesario para realizar los cálculos.

3. **Filtros y Orden**: Aplicamos los filtros necesarios (como `status = 'completed'` y `COUNT(co.id) >= 3`) y ordenamos los resultados por `total_revenue DESC`, limitando a los top 10 clientes.

Esta query debería proporcionar la información solicitada, mostrando a los top 10 clientes por revenue total en los últimos 6 meses, junto con las columnas solicitadas y ordenadas según el revenue total de manera descendente.