# GPT-OSS 120B — code_generation/sql_query_complex

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.58 | quality: 9.8
- latency_total: 104.073s | tokens_per_second: 11.8
- input_tokens: 195 | output_tokens: 1226
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

**SQL (compatible con PostgreSQL / MySQL‑8+).**  
La consulta está dividida en varios CTE para que sea más legible y para poder reutilizar los cálculos intermedios (revenue por orden, categoría más comprada, etc.).

```sql
/* -------------------------------------------------------------
   TOP 10 clientes por revenue en los últimos 6 meses
   ------------------------------------------------------------- */
WITH
/* 1️⃣ Órdenes completadas en los últimos 6 meses */
filtered_orders AS (
    SELECT
        o.id          AS order_id,
        o.customer_id,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= (CURRENT_DATE - INTERVAL '6 month')
),

/* 2️⃣ Revenue de cada orden (sum(quantity * unit_price)) */
order_revenue AS (
    SELECT
        fo.order_id,
        fo.customer_id,
        SUM(oi.quantity * oi.unit_price) AS order_total
    FROM filtered_orders fo
    JOIN order_items oi
          ON oi.order_id = fo.order_id
    GROUP BY fo.order_id, fo.customer_id
),

/* 3️⃣ Estadísticas por cliente (total orders, total revenue, avg order value) */
customer_stats AS (
    SELECT
        o.customer_id,
        COUNT(*)                         AS total_orders,
        SUM(o.order_total)               AS total_revenue,
        AVG(o.order_total)               AS avg_order_value
    FROM order_revenue o
    GROUP BY o.customer_id
    HAVING COUNT(*) >= 3                -- al menos 3 órdenes completadas
),

/* 4️⃣ Cantidad comprada por categoría para cada cliente */
category_qty AS (
    SELECT
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS qty
    FROM filtered_orders fo
    JOIN order_items oi   ON oi.order_id = fo.order_id
    JOIN products p       ON p.id = oi.product_id
    GROUP BY fo.customer_id, p.category
),

/* 5️⃣ La categoría “más comprada” (máxima qty) por cliente */
category_rank AS (
    SELECT
        c.customer_id,
        c.category,
        c.qty,
        ROW_NUMBER() OVER (PARTITION BY c.customer_id
                           ORDER BY c.qty DESC, c.category) AS rn
    FROM category_qty c
),

/* 6️⃣ Unimos todo con los datos del cliente */
final AS (
    SELECT
        cu.name,
        cu.email,
        cu.country,
        cs.total_orders,
        cs.total_revenue,
        cs.avg_order_value,
        cr.category AS categoria_mas_comprada
    FROM customer_stats cs
    JOIN customers cu
          ON cu.id = cs.customer_id
    LEFT JOIN category_rank cr
           ON cr.customer_id = cs.customer_id
          AND cr.rn = 1                     -- solo la categoría top
)
SELECT *
FROM final
ORDER BY total_revenue DESC
LIMIT 10;
```

### Qué hace cada parte

| CTE | Propósito |
|-----|-----------|
| **filtered_orders** | Selecciona solo las órdenes con `status = 'completed'` y con `created_at` dentro de los últimos 6 meses. |
| **order_revenue** | Calcula el revenue de cada orden (`quantity * unit_price`). |
| **customer_stats** | Agrupa por cliente y calcula: <br>• `total_orders` (número de órdenes) <br>• `total_revenue` (suma de los revenues de sus órdenes) <br>• `avg_order_value` (promedio por orden). <br>Aplica el filtro de **mínimo 3 órdenes**. |
| **category_qty** | Suma la cantidad (`quantity`) comprada por categoría para cada cliente. |
| **category_rank** | Usa `ROW_NUMBER()` para quedarnos con la categoría de mayor cantidad (desempate por nombre de categoría). |
| **final** | Une los datos del cliente (`customers`) con los stats y la categoría top. |
| **SELECT final** | Devuelve los 10 clientes con mayor `total_revenue`, ordenados descendente. |

### Resultado esperado

| name | email | country | total_orders | total_revenue | avg_order_value | categoria_mas_comprada |
|------|-------|---------|--------------|---------------|------------------|------------------------|
| …    | …     | …       | …            | …             | …                | …                      |

Los 10 registros mostrados cumplen todas las condiciones solicitadas:
- **Periodo:** últimos 6 meses.  
- **Estado:** solo órdenes `completed`.  
- **Umbral:** al menos 3 órdenes por cliente.  
- **Columnas:** nombre, email, país, número total de órdenes, revenue total, valor medio por orden y categoría más comprada.  
- **Orden:** `total_revenue` descendente.  