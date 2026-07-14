# Nemotron Nano 9B v2 — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-nano-9b-v2:free`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 65.528s | tokens_per_second: 43.8
- input_tokens: 156 | output_tokens: 2868
- judge_score: 5.0 | justificación: 

## Respuesta completa



Aquí tienes la consulta SQL que cumple con todos los requisitos especificados:

```sql
WITH customer_data AS (
  SELECT 
    c.id AS customer_id,
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    (SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id)) AS avg_order_value
  FROM orders o
  JOIN customers c ON o.customer_id = c.id
  JOIN order_items oi ON o.id = oi.order_id
  JOIN products p ON oi.product_id = p.id
  WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
  GROUP BY c.id, c.name, c.email, c.country
  HAVING COUNT(DISTINCT o.id) >= 3
),
category_rank AS (
  SELECT 
    customer_id,
    category,
    SUM(quantity) AS total_quantity
  FROM order_items
  JOIN products ON order_items.product_id = products.id
  WHERE order_id IN (
    SELECT id FROM orders 
    WHERE status = 'completed' 
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
  )
  GROUP BY customer_id, category
)
SELECT 
  cd.name,
  cd.email,
  cd.country,
  cd.total_orders,
  cd.total_revenue,
  cd.avg_order_value,
  (SELECT cr.category 
   FROM category_rank cr 
   WHERE cr.customer_id = cd.customer_id 
   ORDER BY cr.total_quantity DESC 
   LIMIT 1) AS categoria_mas_comprada
FROM customer_data cd
ORDER BY cd.total_revenue DESC
LIMIT 10;
```

### Explicación de los componentes clave:

1. **Filtrado de órdenes completadas en los últimos 6 meses**:
   - `WHERE o.status = 'completed' AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'`

2. **Cálculo de métricas por cliente**:
   - `customer_data` CTE calcula:
     - `total_orders`: Contador de órdenes distintas por cliente
     - `total_revenue`: Suma de `quantity * unit_price` para todas las órdenes
     - `avg_order_value`: Revenue promedio por orden

3. **Filtrado de clientes con al menos 3 órdenes**:
   - `HAVING COUNT(DISTINCT o.id) >= 3` en el CTE `customer_data`

4. **Determinación de la categoría más comprada**:
   - `category_rank` CTE agrupa por cliente y categoría para calcular la cantidad total comprada por cada categoría
   - Subeconsulta en la selección principal que obtiene la categoría con mayor cantidad por cliente

5. **Ordenamiento y límite**:
   - `ORDER BY total_revenue DESC LIMIT 10` para obtener los 10 clientes líderes

### Notas importantes:
- La consulta asume que `created_at` es tipo `DATE` o `TIMESTAMP`. Si es `TIMESTAMP`, ajusta el filtro temporal según tus necesidades.
- En caso de empate en la categoría más comprada, se devolverá la primera alfabéticamente. Si necesitas manejar empates de forma específica, se requeriría lógica adicional.
- Las relaciones entre tablas se mantienen mediante joins adecuados para garantizar integridad de datos.
