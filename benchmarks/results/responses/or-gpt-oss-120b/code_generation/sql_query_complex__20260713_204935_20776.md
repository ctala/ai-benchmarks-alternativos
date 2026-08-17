# GPT-OSS 120B — code_generation/sql_query_complex

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.89 | quality: 9.8
- latency_total: 22.063s | tokens_per_second: 45.2
- input_tokens: 208 | output_tokens: 998
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

**SQL (compatible con PostgreSQL / MySQL / SQL Server)**  

```sql
/*  Top 10 clientes por revenue total en los últimos 6 meses
    - Sólo se consideran órdenes con status = 'completed'
    - Se exige al menos 3 órdenes en ese período
    - Se calculan: total de órdenes, revenue total, promedio por orden
      y la categoría más comprada por cada cliente
*/

WITH fecha_limite AS (
    SELECT DATEADD(MONTH, -6, CURRENT_DATE) AS desde   -- MySQL / SQL‑Server: CURRENT_DATE
    -- En PostgreSQL usar: (CURRENT_DATE - INTERVAL '6 months') AS desde
),

ordenes_filtradas AS (
    SELECT o.id,
           o.customer_id,
           o.total,
           o.created_at
    FROM   orders o
    JOIN   fecha_limite f ON o.created_at >= f.desde
    WHERE  o.status = 'completed'
),

-- Agrupamos por cliente para obtener totales y número de órdenes
cliente_resumen AS (
    SELECT  c.id               AS customer_id,
            c.name,
            c.email,
            c.country,
            COUNT(o.id)        AS total_orders,
            SUM(o.total)       AS total_revenue,
            AVG(o.total)       AS avg_order_value
    FROM    customers c
    JOIN    ordenes_filtradas o ON o.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING  COUNT(o.id) >= 3                     -- al menos 3 órdenes completadas
),

-- Determinamos la categoría más comprada por cliente
categoria_mas_comprada AS (
    SELECT  c.id   AS customer_id,
            p.category,
            SUM(oi.quantity) AS qty_total,
            ROW_NUMBER() OVER (PARTITION BY c.id
                               ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM    customers c
    JOIN    ordenes_filtradas o   ON o.customer_id = c.id
    JOIN    order_items oi        ON oi.order_id = o.id
    JOIN    products p            ON p.id = oi.product_id
    GROUP BY c.id, p.category
)

SELECT  r.name,
        r.email,
        r.country,
        r.total_orders,
        r.total_revenue,
        r.avg_order_value,
        cmc.category AS categoria_mas_comprada
FROM    cliente_resumen r
LEFT JOIN (
        SELECT customer_id, category
        FROM   categoria_mas_comprada
        WHERE  rn = 1
) cmc
      ON cmc.customer_id = r.customer_id
ORDER BY r.total_revenue DESC
LIMIT 10;          -- MySQL / PostgreSQL
-- En SQL Server usar: TOP 10 en el SELECT y quitar LIMIT
```

### Explicación paso a paso  

| Paso | Qué hace | Por qué |
|------|----------|----------|
| `fecha_limite` | Calcula la fecha de corte (hoy ‑ 6 meses). | Limita el análisis a los últimos 6 meses. |
| `ordenes_filtradas` | Selecciona solo órdenes **completed** dentro del rango. | Cumple con el filtro de estado y de tiempo. |
| `cliente_resumen` | Agrupa por cliente y calcula: <br>• `total_orders` <br>• `total_revenue` <br>• `avg_order_value` | Provee los indicadores solicitados y filtra clientes con ≥ 3 órdenes (`HAVING`). |
| `categoria_mas_comprada` | Suma la cantidad comprada por categoría para cada cliente y usa `ROW_NUMBER()` para quedarnos con la de mayor cantidad. | Obtiene la categoría que más compró cada cliente. |
| `SELECT final` | Junta los dos CTE y muestra los campos requeridos, ordenados por revenue descendente y limitados a 10. | Produce el reporte solicitado. |

#### Adaptaciones rápidas  

* **SQL Server** – Cambia `LIMIT 10` por `TOP 10` en el `SELECT` y usa `GETDATE()` en vez de `CURRENT_DATE`.  
* **PostgreSQL** – Usa `(CURRENT_DATE - INTERVAL '6 months')` en el CTE `fecha_limite`.  
* Si la columna `total` de **orders** no representa el revenue (por ejemplo, si hay descuentos), puedes recomponerlo sumando `order_items.quantity * order_items.unit_price` en su lugar.  

Con esta consulta obtendrás los 10 clientes más valiosos del último semestre, con toda la información solicitada.