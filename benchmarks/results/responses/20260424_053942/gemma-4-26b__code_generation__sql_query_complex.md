# Gemma 4 26B MoE (3.8B activos) — code_generation/sql_query_complex

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 7.6 | quality: 9.72
- latency_total: 17.704s | tokens_per_second: 49.4
- input_tokens: 173 | output_tokens: 875
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para resolver esta consulta, necesitamos realizar varias agrupaciones y utilizar una **Common Table Expression (CTE)** o una subconsulta para determinar la categoría más comprada de cada cliente, ya que esa información requiere un nivel de agregación distinto al de los totales del cliente.

Aquí tienes la query optimizada para PostgreSQL/Standard SQL:

```sql
WITH customer_stats AS (
    -- Paso 1: Calcular métricas básicas de ventas por cliente
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
customer_top_category AS (
    -- Paso 2: Identificar la categoría más comprada por cada cliente
    SELECT DISTINCT ON (o.customer_id)
        o.customer_id,
        p.category
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
    ORDER BY o.customer_id, SUM(oi.quantity) DESC
)
-- Paso 3: Unir todo para el reporte final
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    ctc.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN customer_top_category ctc ON cs.customer_id = ctc.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:

1.  **`customer_stats` (CTE):**
    *   Filtra las órdenes por `status = 'completed'` y por el rango de tiempo de los últimos 6 meses.
    *   Agrupa por cliente para calcular el `total_revenue`, el conteo de órdenes y el promedio.
    *   Utiliza `HAVING COUNT(o.id) >= 3` para cumplir con el requisito de clientes recurrentes.

2.  **`customer_top_category` (CTE):**
    *   Aquí hacemos un "join" profundo: `orders` $\to$ `order_items` $\to$ `products`.
    *   Agrupamos por cliente y categoría para sumar la cantidad de productos comprados (`SUM(oi.quantity)`).
    *   **Truco de SQL:** He utilizado `DISTINCT ON (o.customer_id)` (característico de PostgreSQL). Esto permite tomar solo la primera fila de cada grupo de cliente después de ordenar por la cantidad de productos de mayor a menor, obteniendo así su categoría favorita de forma eficiente.

3.  **Consulta Final:**
    *   Une las métricas financieras con la categoría ganadora mediante un `LEFT JOIN`.
    *   Aplica el `ORDER BY total_revenue DESC` y el `LIMIT 10` para obtener el ranking solicitado.

**Nota de compatibilidad:** Si utilizas **MySQL** o **SQL Server** (que no soportan `DISTINCT ON`), la segunda CTE se debería resolver usando una función de ventana como `ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY SUM(quantity) DESC)`.