# GPT-OSS 120B — code_generation/sql_query_complex

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.98 | quality: 9.8
- latency_total: 16.324s | tokens_per_second: 96.1
- input_tokens: 208 | output_tokens: 1568
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

**SQL (compatible con PostgreSQL, MySQL 8+, SQL Server, etc.)**

```sql
/* --------------------------------------------------------------
   1️⃣  Datos de cada orden (solo completadas y de los últimos 6 meses)
   -------------------------------------------------------------- */
WITH orders_last_6m AS (
    SELECT  o.id               AS order_id,
            o.customer_id,
            o.created_at,
            SUM(oi.quantity * oi.unit_price) AS order_total      -- revenue de la orden
    FROM    orders      o
    JOIN    order_items oi ON oi.order_id = o.id
    WHERE   o.status = 'completed'
      AND   o.created_at >= CURRENT_DATE - INTERVAL '6 months'   -- últimos 6 meses
    GROUP BY o.id, o.customer_id, o.created_at
),

/* --------------------------------------------------------------
   2️⃣  Agregación por cliente (total de órdenes, revenue, avg‑value)
   -------------------------------------------------------------- */
cust_agg AS (
    SELECT  o.customer_id,
            COUNT(*)                         AS total_orders,
            SUM(o.order_total)               AS total_revenue,
            AVG(o.order_total)               AS avg_order_value
    FROM    orders_last_6m o
    GROUP BY o.customer_id
    HAVING  COUNT(*) >= 3                    -- al menos 3 órdenes completadas
),

/* --------------------------------------------------------------
   3️⃣  Categoría más comprada por cliente
   -------------------------------------------------------------- */
cat_agg AS (
    SELECT  o.customer_id,
            p.category,
            SUM(oi.quantity)                         AS qty,
            ROW_NUMBER() OVER (
                PARTITION BY o.customer_id
                ORDER BY SUM(oi.quantity) DESC
            )                                        AS rn   -- 1 = categoría top
    FROM    orders      o
    JOIN    order_items oi ON oi.order_id = o.id
    JOIN    products    p  ON p.id = oi.product_id
    WHERE   o.status = 'completed'
      AND   o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)

/* --------------------------------------------------------------
   4️⃣  Resultado final
   -------------------------------------------------------------- */
SELECT
    cu.name      AS nombre,
    cu.email     AS email,
    cu.country   AS pais,
    ca.total_orders,
    ca.total_revenue,
    ca.avg_order_value,
    ct.category  AS categoria_mas_comprada
FROM    cust_agg            ca
JOIN    customers           cu ON cu.id = ca.customer_id
LEFT JOIN cat_agg           ct ON ct.customer_id = ca.customer_id
                                 AND ct.rn = 1               -- solo la top‑category
ORDER BY ca.total_revenue DESC
LIMIT 10;
```

### Qué hace cada bloque

| Bloque | Propósito |
|--------|-----------|
| **orders_last_6m** | Obtiene, para cada orden completada en los últimos 6 meses, el **revenue** de la orden (`quantity * unit_price`). |
| **cust_agg** | Agrupa por cliente y calcula: <br>• `total_orders` (n.º de órdenes completadas) <br>• `total_revenue` (suma de los revenues de sus órdenes) <br>• `avg_order_value` (revenue medio por orden). <br>El `HAVING` garantiza al menos 3 órdenes. |
| **cat_agg** | Para el mismo rango de tiempo, suma la cantidad comprada por categoría y, usando `ROW_NUMBER`, marca la categoría con mayor cantidad (`rn = 1`). |
| **SELECT final** | Une la agregación del cliente con la tabla `customers` (para nombre, email, país) y con la categoría top. Ordena por `total_revenue` descendente y limita a los 10 mejores. |

### Ajustes rápidos si usas otro SGBD

| SGBD | Cambios menores |
|------|-----------------|
| **MySQL 8+** | `CURRENT_DATE - INTERVAL 6 MONTH` (en vez de `'6 months'`). |
| **SQL Server** | `GETDATE() - INTERVAL '6 months'` → `DATEADD(MONTH, -6, GETDATE())`. |
| **Oracle** | `SYSDATE - INTERVAL '6' MONTH`. |

Con esta consulta obtienes exactamente lo que pediste: los **10 clientes con mayor revenue** en los últimos seis meses, con su información de contacto, número y valor medio de órdenes, y la categoría que más han comprado. ¡Éxitos!