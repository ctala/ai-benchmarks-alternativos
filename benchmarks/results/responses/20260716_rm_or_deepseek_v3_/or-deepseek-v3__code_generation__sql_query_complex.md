# DeepSeek V3 — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.98 | quality: 9.8
- latency_total: 10.053s | tokens_per_second: 76.7
- input_tokens: 158 | output_tokens: 771
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL completa y bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

Aquí tienes la consulta SQL que cumple con todos los requisitos:

```sql
WITH ultimos_6_meses AS (
    SELECT DATE_SUB(CURDATE(), INTERVAL 6 MONTH) AS fecha_inicio
),
clientes_revenue AS (
    SELECT 
        c.id AS cliente_id,
        c.name AS nombre,
        c.email AS email,
        c.country AS pais,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value,
        ROW_NUMBER() OVER (ORDER BY SUM(o.total) DESC) AS revenue_rank
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    CROSS JOIN ultimos_6_meses um
    WHERE o.status = 'completed'
      AND o.created_at >= um.fecha_inicio
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),
categoria_favorita AS (
    SELECT 
        o.customer_id,
        p.category AS categoria_mas_comprada,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC, SUM(oi.quantity * oi.unit_price) DESC
        ) AS categoria_rank
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    INNER JOIN ultimos_6_meses um ON o.created_at >= um.fecha_inicio
    WHERE o.status = 'completed'
    GROUP BY o.customer_id, p.category
)
SELECT 
    cr.nombre,
    cr.email,
    cr.pais,
    cr.total_orders,
    cr.total_revenue,
    ROUND(cr.avg_order_value, 2) AS avg_order_value,
    cf.categoria_mas_comprada
FROM clientes_revenue cr
LEFT JOIN categoria_favorita cf 
    ON cr.cliente_id = cf.customer_id 
    AND cf.categoria_rank = 1
WHERE cr.revenue_rank <= 10
ORDER BY cr.total_revenue DESC;
```

**Explicación de la consulta:**

1. **CTE `ultimos_6_meses`**: Define la fecha de inicio para el período de 6 meses
2. **CTE `clientes_revenue`**:
   - Calcula métricas clave por cliente
   - Filtra órdenes completadas en los últimos 6 meses
   - Aplica filtro de mínimo 3 órdenes completadas
   - Asigna ranking por revenue total
3. **CTE `categoria_favorita`**:
   - Determina la categoría más comprada por cada cliente
   - Prioriza por cantidad total de productos, luego por revenue
4. **Consulta final**:
   - Combina las métricas con la categoría favorita
   - Limita a top 10 clientes por revenue
   - Ordena por total_revenue descendente

**Notas importantes:**
- La categoría más comprada se determina primero por la cantidad total de productos, y si hay empate, por el revenue total en esa categoría
- Se usa `CURDATE()` para calcular la fecha actual, ajusta según tu sistema de base de datos si es necesario
- El cálculo de `avg_order_value` se redondea a 2 decimales para mejor presentación