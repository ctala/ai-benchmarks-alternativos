# Nemotron Super 49B v1.5 (NIM) — code_generation/sql_query_complex

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 6.9 | quality: 9.72
- latency_total: 146.838s | tokens_per_second: 28.2
- input_tokens: 156 | output_tokens: 4139
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL que cumple con los requisitos especificados:

```sql
WITH customer_orders AS (
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        o.id AS order_id,
        oi.quantity,
        oi.unit_price,
        p.category
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
    AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)
),
customer_summary AS (
    SELECT
        customer_id,
        name,
        email,
        country,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(quantity * unit_price) AS total_revenue,
        SUM(quantity * unit_price) / COUNT(DISTINCT order_id) AS avg_order_value
    FROM customer_orders
    GROUP BY customer_id, name, email, country
    HAVING COUNT(DISTINCT order_id) >= 3
),
top_category AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY SUM(quantity) DESC) AS rank
    FROM customer_orders
    GROUP BY customer_id, category
)
SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    tc.category AS categoria_mas_comprada
FROM customer_summary cs
JOIN top_category tc ON cs.customer_id = tc.customer_id AND tc.rank = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de la Consulta:

1. **`customer_orders` (CTE):**
   - Se unen las tablas `customers`, `orders`, `order_items` y `products` para obtener todos los datos relevantes.
   - Se filtran solo los pedidos completados (`status = 'completed'`) y dentro de los últimos 6 meses (`created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)`).

2. **`customer_summary` (CTE):**
   - Se agrupa por cliente para calcular:
     - `total_orders`: Número de órdenes completadas (contando órdenes únicas con `COUNT(DISTINCT order_id)`).
     - `total_revenue`: Ingreso total por cliente (suma de `quantity * unit_price`).
     - `avg_order_value`: Valor promedio por órden (total_revenue dividido por total_orders).
   - Se filtran clientes con al menos 3 órdenes completadas (`HAVING COUNT(DISTINCT order_id) >= 3`).

3. **`top_category` (CTE):**
   - Se calcula la categoría más comprada por cada cliente, ordenando por la cantidad total comprada (`SUM(quantity) DESC`).
   - Se usa `ROW_NUMBER()` para asignar un ranking a cada categoría por cliente, y se selecciona solo la categoría con `rank = 1`.

4. **Consulta Final:**
   - Se une `customer_summary` con `top_category` para obtener la categoría más comprada por cliente.
   - Se ordena el resultado por `total_revenue` en orden descendente y se limita a los primeros 10 clientes.

### Notas Adicionales:
- **Cálculo de `avg_order_value`:** Se realiza como `total_revenue / total_orders` para obtener el valor promedio por orden, en lugar de promediar los valores individuales de los artículos.
- **Categoría más comprada:** Se define como la categoría con la mayor cantidad total de unidades adquiridas por cliente. Si se prefiere basarse en el ingreso total (`quantity * unit_price`), se puede modificar el `ORDER BY` en `top_category` a `SUM(quantity * unit_price) DESC`.

Esta consulta proporciona una solución eficiente y clara para el problema planteado, utilizando CTEs para estructurar y organizar el cálculo de los datos requeridos.