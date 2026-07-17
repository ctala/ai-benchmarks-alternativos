# GPT-OSS 120B — code_generation/sql_query_complex

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.83 | quality: 9.8
- latency_total: 35.855s | tokens_per_second: 43.1
- input_tokens: 195 | output_tokens: 1545
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

**Consulta (compatible con PostgreSQL / MySQL 8+)**  

```sql
/* --------------------------------------------------------------
   1️⃣  Datos de los últimos 6 meses y sólo órdenes completadas
   -------------------------------------------------------------- */
WITH customer_orders AS (
    SELECT
        c.id               AS customer_id,
        c.name,
        c.email,
        c.country,
        o.id               AS order_id,
        oi.quantity,
        oi.unit_price,
        p.category,
        (oi.quantity * oi.unit_price) AS line_total          -- importe de la línea
    FROM customers      c
    JOIN orders         o  ON o.customer_id = c.id
    JOIN order_items    oi ON oi.order_id   = o.id
    JOIN products       p  ON p.id          = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'      -- PostgreSQL
      -- AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)  -- MySQL
),

/* --------------------------------------------------------------
   2️⃣  Agregación por cliente (total de órdenes, revenue, avg)
   -------------------------------------------------------------- */
agg_customer AS (
    SELECT
        customer_id,
        name,
        email,
        country,
        COUNT(DISTINCT order_id)                         AS total_orders,
        SUM(line_total)                                  AS total_revenue,
        SUM(line_total) / COUNT(DISTINCT order_id)       AS avg_order_value
    FROM customer_orders
    GROUP BY customer_id, name, email, country
    HAVING COUNT(DISTINCT order_id) >= 3                -- al menos 3 órdenes
),

/* --------------------------------------------------------------
   3️⃣  Categoría más comprada por cliente
   -------------------------------------------------------------- */
category_rank AS (
    SELECT
        customer_id,
        category,
        SUM(quantity)                                   AS qty,
        ROW_NUMBER() OVER (PARTITION BY customer_id
                           ORDER BY SUM(quantity) DESC) AS rn
    FROM customer_orders
    GROUP BY customer_id, category
)

/* --------------------------------------------------------------
   4️⃣  Resultado final (Top‑10 por revenue)
   -------------------------------------------------------------- */
SELECT
    a.name            AS nombre,
    a.email           AS email,
    a.country         AS pais,
    a.total_orders    AS total_orders,
    a.total_revenue   AS total_revenue,
    a.avg_order_value AS avg_order_value,
    cr.category       AS categoria_mas_comprada
FROM agg_customer      a
JOIN category_rank    cr
      ON cr.customer_id = a.customer_id
     AND cr.rn = 1                     -- la categoría con mayor cantidad
ORDER BY a.total_revenue DESC
LIMIT 10;
```

### ¿Qué hace cada bloque?

| Bloque | Propósito |
|--------|-----------|
| **customer_orders** | Extrae, para los últimos 6 meses, todas las líneas de pedido de clientes con órdenes `status = 'completed'`. Calcula el importe de cada línea (`quantity * unit_price`). |
| **agg_customer** | Agrupa por cliente y calcula:<br>• `total_orders` (n.º de órdenes distintas)<br>• `total_revenue` (suma de los importes de línea)<br>• `avg_order_value` (revenue ÷ total orders)<br>Filtra clientes con **≥ 3** órdenes completadas. |
| **category_rank** | Para cada cliente suma la cantidad comprada por categoría y asigna un ranking (`ROW_NUMBER`) ordenado de mayor a menor cantidad. El registro con `rn = 1` es la categoría más comprada. |
| **SELECT final** | Une los dos agregados, conserva solo la categoría top (`rn = 1`), ordena por `total_revenue` descendente y devuelve los 10 mejores clientes. |

### Adaptaciones rápidas

* **MySQL 5.x** (sin window functions) → la parte `category_rank` puede hacerse con una sub‑consulta que utilice `MAX()` y `GROUP_CONCAT()` o una tabla derivada con `JOIN` y `ORDER BY … LIMIT 1` por cliente.  
* **Formato de fechas** → si tu columna `created_at` es `TIMESTAMP` o `DATETIME`, la condición de 6 meses sigue funcionando con `CURRENT_DATE` / `CURDATE()`.  

Con esta consulta obtienes exactamente la información solicitada: nombre, email, país, número total de órdenes, revenue total, valor medio de orden y la categoría más comprada, todo para los 10 clientes con mayor revenue en los últimos seis meses.