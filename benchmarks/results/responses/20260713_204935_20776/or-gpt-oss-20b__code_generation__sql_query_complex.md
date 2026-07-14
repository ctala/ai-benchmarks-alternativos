# GPT-OSS 20B — code_generation/sql_query_complex

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.85 | quality: 9.56
- latency_total: 17.785s | tokens_per_second: 92.0
- input_tokens: 195 | output_tokens: 1636
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, cumpliendo con todos los requisitos de la consulta SQL compleja.

## Respuesta completa

**SQL (PostgreSQL‑style)**  

```sql
-- 1️⃣  Orders that are finished and fall in the last 6 months
WITH recent_orders AS (
    SELECT o.id        AS order_id,
           o.customer_id,
           o.created_at
    FROM   orders o
    WHERE  o.status = 'completed'
      AND  o.created_at >= NOW() - INTERVAL '6 months'
),

-- 2️⃣  Revenue & order‑count per customer (only those with ≥3 orders)
customer_stats AS (
    SELECT  ro.customer_id,
            COUNT(DISTINCT ro.order_id)                                  AS total_orders,
            SUM(oi.quantity * oi.unit_price)                            AS total_revenue,
            SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT ro.order_id) AS avg_order_value
    FROM   recent_orders ro
    JOIN   order_items oi ON oi.order_id = ro.order_id
    GROUP  BY ro.customer_id
    HAVING COUNT(DISTINCT ro.order_id) >= 3
),

-- 3️⃣  Quantity of each category per customer
category_qty AS (
    SELECT  ro.customer_id,
            p.category,
            SUM(oi.quantity)                                    AS qty,
            ROW_NUMBER() OVER (PARTITION BY ro.customer_id
                               ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM   recent_orders ro
    JOIN   order_items oi ON oi.order_id = ro.order_id
    JOIN   products p     ON p.id = oi.product_id
    GROUP  BY ro.customer_id, p.category
),

-- 4️⃣  Keep only the top‑category per customer
most_purchased AS (
    SELECT customer_id,
           category AS categoria_mas_comprada
    FROM   category_qty
    WHERE  rn = 1
)

-- 5️⃣  Final result – join with customer data
SELECT  c.name           AS nombre,
        c.email,
        c.country        AS pais,
        cs.total_orders,
        cs.total_revenue,
        cs.avg_order_value,
        mp.categoria_mas_comprada
FROM   customer_stats cs
JOIN   customers c   ON c.id = cs.customer_id
LEFT JOIN most_purchased mp ON mp.customer_id = cs.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación rápida

| Paso | Qué hace | Por qué |
|------|----------|---------|
| 1️⃣ | Filtra las órdenes completadas de los últimos 6 meses. | Para limitar el análisis a los datos recientes. |
| 2️⃣ | Calcula `total_orders`, `total_revenue` y `avg_order_value` por cliente, y mantiene solo los clientes con ≥ 3 órdenes. | Necesitamos clientes con al menos 3 pedidos. |
| 3️⃣ | Suma la cantidad de productos por categoría para cada cliente y añade un número de fila (`rn`) que ordena las categorías por cantidad. | Para identificar la categoría más comprada. |
| 4️⃣ | Selecciona la categoría con `rn = 1` (la más comprada) para cada cliente. | Extrae la categoría principal. |
| 5️⃣ | Une todo con la tabla `customers`, ordena por `total_revenue` y limita a los 10 primeros. | Presenta la tabla solicitada. |

El resultado muestra:

- **nombre**, **email**, **pais**  
- **total_orders** (número de pedidos completos)  
- **total_revenue** (ingresos totales en los últimos 6 meses)  
- **avg_order_value** (ingreso medio por pedido)  
- **categoria_mas_comprada** (categoría con mayor cantidad comprada)

Y está ordenado por el mayor `total_revenue`.