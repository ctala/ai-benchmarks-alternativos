# Nemotron Nano 9B v2 (NIM) — code_generation/sql_query_complex

- model_id: `nvidia/nvidia-nemotron-nano-9b-v2`
- success: True  | final: 7.1 | quality: 9.72
- latency_total: 84.782s | tokens_per_second: 51.1
- input_tokens: 156 | output_tokens: 4331
- judge_score: 4.8 | justificación: 

## Respuesta completa



Aquí tienes la consulta SQL que cumple con todos los requisitos especificados:

```sql
WITH customer_category_revenue AS (
    SELECT 
        c.id AS customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
    GROUP BY c.id, p.category
),
customer_max_category AS (
    SELECT 
        customer_id,
        category
    FROM (
        SELECT 
            customer_id,
            category,
            ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY category_revenue DESC) AS rn
        FROM customer_category_revenue
    ) AS ranked
    WHERE rn = 1
)
SELECT 
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    (SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id)) AS avg_order_value,
    cm.category AS categoria_mas_comprada
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN order_items oi ON o.id = oi.order_id
JOIN products p ON oi.product_id = p.id
JOIN customer_max_category cm ON c.id = cm.customer_id
WHERE o.status = 'completed'
  AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
GROUP BY c.id, c.name, c.email, c.country, cm.category
HAVING COUNT(DISTINCT o.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

### Explicación de la consulta:

1. **Filtrado de órdenes completadas en los últimos 6 meses**:
   - Se filtran las órdenes con `status = 'completed'` y `created_at` en los últimos 6 meses usando `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.

2. **Cálculo de revenue por categoría por cliente**:
   - Se crea una CTE (`customer_category_revenue`) que calcula el revenue por categoría para cada cliente.

3. **Determinación de la categoría más comprada**:
   - Se usa una CTE adicional (`customer_max_category`) con `ROW_NUMBER()` para identificar la categoría con el mayor revenue por cliente.

4. **Cálculo de métricas por cliente**:
   - Se unen todas las tablas necesarias y se calculan:
     - `total_orders`: cantidad de órdenes completadas.
     - `total_revenue`: suma del revenue total.
     - `avg_order_value`: revenue promedio por orden.
     - `categoria_mas_comprada`: categoría con mayor revenue (usando la CTE `customer_max_category`).

5. **Filtrado y ordenamiento**:
   - Se filtra para incluir solo clientes con al menos 3 órdenes completadas (`HAVING COUNT(DISTINCT o.id) >= 3`).
   - Se ordena por `total_revenue` en orden descendente y se limitan a los 10 primeros.

### Notas:
- La consulta asume que `NOW()` y `DATE_SUB` son funciones válidas en tu base de datos (comunes en MySQL). Si usas otra base de datos, ajusta la sintaxis de fecha según corresponda.
- La categoría más comprada se define como la que genera el mayor revenue. Si prefieres usar la cantidad de unidades vendidas, ajusta `category_revenue` a `SUM(oi.quantity)`.
