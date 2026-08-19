# Nemotron 3 Base 33B (DGX Spark Q4_K_M) — code_generation/sql_query_complex

- model_id: `nemotron3:33b-q4_K_M`
- success: True  | final: 7.23 | quality: 9.24
- latency_total: 34.012s | tokens_per_second: 65.6
- input_tokens: 161 | output_tokens: 2230
- judge_score: 4.6 | justificación: 

## Respuesta completa

**SQL (PostgreSQL‑style)**  

```sql
/* 1️⃣  Orders that are completed and that have been created in the last 6 months */
WITH filtered_orders AS (
    SELECT  o.id,
            o.customer_id,
            o.status,
            o.created_at
    FROM    orders o
    WHERE   o.status = 'completed'
      AND   o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

/* 2️⃣  One row per customer with the basic aggregates (orders count & revenue) */
customer_agg AS (
    SELECT  c.id                                   AS customer_id,
            c.name,
            c.email,
            c.country,
            COUNT(o.id)                              AS total_orders,
            SUM(oi.quantity * oi.unit_price)         AS total_revenue
    FROM    customers c
    JOIN    filtered_orders o      ON c.id = o.customer_id
    JOIN    order_items oi         ON oi.order_id = o.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING  COUNT(o.id) >= 3                         -- al menos 3 órdenes
),

/* 3️⃣  Category that each customer bought the most (by quantity) */
category_top AS (
    SELECT  c.id                                   AS customer_id,
            p.category                             AS categoria_mas_comprada,
            SUM(oi.quantity)                       AS qty,
            ROW_NUMBER() OVER (PARTITION BY c.id
                               ORDER BY SUM(oi.quantity) DESC) AS rn
    FROM    filtered_orders o
    JOIN    order_items oi ON oi.order_id = o.id
    JOIN    products p      ON p.id = oi.product_id
    GROUP BY c.id, p.category
    QUALIFY rn = 1                                   -- keep only the top category per customer
),

/* 4️⃣  Join the category information to the aggregated customer data */
final_result AS (
    SELECT  ca.customer_id,
            ca.name,
            ca.email,
            ca.country,
            ca.total_orders,
            ca.total_revenue,
            ca.total_revenue / ca.total_orders      AS avg_order_value,
            ct.categoria_mas_comprada
    FROM    customer_agg ca
    LEFT JOIN category_top ct
           ON ct.customer_id = ca.customer_id
)

-- 5️⃣  Top 10 customers by total revenue, ordered descending
SELECT  name,
        email,
        country,
        total_orders,
        total_revenue,
        avg_order_value,
        categoria_mas_comprada
FROM    final_result
ORDER BY total_revenue DESC
LIMIT 10;
```

### Qué hace cada parte  

| CTE / bloque | Propósito |
|--------------|-----------|
| **filtered_orders** | Selecciona solo las órdenes *completed* creadas en los últimos 6 meses. |
| **customer_agg** | Agrupa por cliente y calcula: <br>• `total_orders` (número de órdenes) <br>• `total_revenue` (suma de `quantity × unit_price` de todas las líneas de cada orden). <br>Filtra con `HAVING COUNT(o.id) >= 3`. |
| **category_top** | Para cada cliente cuenta la cantidad total de unidades compradas por categoría y, usando `ROW_NUMBER()`, queda solo la categoría con la mayor suma (la “categoría más comprada”). |
| **final_result** | Une los datos del cliente con la categoría más comprada. Calcula `avg_order_value = total_revenue / total_orders`. |
| **SELECT final** | Devuelve las columnas solicitadas, ordena por `total_revenue` descendente y limita a los 10 primeros. |

> **Nota:** Si tu motor SQL no soporta `QUALIFY`, reemplaza la última línea de `category_top` por una sub‑consulta con `ROW_NUMBER()` y filtra por `rn = 1`. El resto de la query es estándar y debería funcionar en PostgreSQL, MySQL 8+, SQL Server, Oracle (con ligeras adaptaciones de sintaxis).