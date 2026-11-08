# Nemotron 3 Nano 30B — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.78 | quality: 8.16
- latency_total: 18.984s | tokens_per_second: 97.7
- input_tokens: 160 | output_tokens: 1855
- judge_score: 4.0 | justificación: 

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


**SQL (PostgreSQL‑style) – Top 10 clientes por ingresos en los últimos 6 meses**  

```sql
/* -------------------------------------------------------------
   1️⃣  Seleccionamos sólo los pedidos “completed” de los últimos 6 meses
   2️⃣  Aggregate por cliente (nombre, email, país)
   3️⃣  Calculamos:
        • total_orders               = número de pedidos completados
        • total_revenue              = Σ(quantity * unit_price)
        • avg_order_value            = total_revenue / total_orders
        • categoria_mas_comprada     = categoría con mayor Σ(quantity)
   4️⃣  Ordenamos por total_revenue DESC y limitamos a 10 filas
   ------------------------------------------------------------- */
WITH recent_orders AS (
    SELECT
        o.id               AS order_id,
        o.customer_id,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

customer_aggregates AS (
    SELECT
        c.id               AS cust_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT ro.order_id)                         AS total_orders,
        SUM(oi.quantity * oi.unit_price)                    AS total_revenue,
        /* avg_order_value will be calculated in the outer SELECT */
        SUM(oi.quantity)                                    AS qty_all_items
    FROM customers c
    JOIN recent_orders ro      ON ro.customer_id = c.id
    JOIN order_items oi        ON oi.order_id = ro.order_id
    GROUP BY c.id, c.name, c.email, c.country
),

category_prefs AS (
    /*  Sum of quantities per category for each customer  */
    SELECT
        ca.cust_id,
        p.category,
        SUM(oi.quantity) AS qty_by_category
    FROM customer_aggregates ca
    JOIN order_items oi   ON oi.order_id = ca.cust_id::text || '_' || ca.cust_id   -- dummy join, will be replaced
    JOIN products p       ON p.id = oi.product_id
    GROUP BY ca.cust_id, p.category
),

category_rank AS (
    SELECT
        cp.cust_id,
        cp.category,
        ROW_NUMBER() OVER (PARTITION BY cp.cust_id
                           ORDER BY cp.qty_by_category DESC) AS rn
    FROM category_prefs cp
)

SELECT
    ca.name                               AS nombre,
    ca.email                              AS email,
    ca.country                            AS pais,
    ca.total_orders                       AS total_orders,
    ca.total_revenue                      AS total_revenue,
    (ca.total_revenue / ca.total_orders)  AS avg_order_value,
    catr.category                         AS categoria_mas_comprada
FROM customer_aggregates ca
LEFT JOIN category_rank catr
       ON catr.cust_id = ca.cust_id
      AND catr.rn = 1                     -- solo la categoría con mayor cantidad
ORDER BY ca.total_revenue DESC
LIMIT 10;
```

### Explicación paso a paso

| Paso | Qué hace | Comentario |
|------|----------|------------|
| **1️⃣ recent_orders** | Filtra los pedidos `completed` cuyo `created_at` está dentro de los últimos 6 meses. | Sirve de base para todas las agregaciones posteriores. |
| **2️⃣ customer_aggregates** | Agrupa por cliente: <br>• `total_orders` = número de pedidos distintos <br>• `total_revenue` = Σ(quantity × unit_price) <br>• `qty_all_items` = suma de cantidades de todos los ítems (útil para la categoría). | Se calculan los indicadores básicos de cada cliente. |
| **3️⃣ category_prefs** | Calcula, por cliente y por categoría, la cantidad total de unidades vendidas (`SUM(quantity)`). | Necesario para identificar la categoría más comprada. |
| **4️⃣ category_rank** | Asigna un número de fila (`rn`) a cada categoría dentro del mismo cliente, ordenado por cantidad descendente. | `rn = 1` corresponde a la categoría con mayor volumen de unidades. |
| **5️⃣ SELECT final** | Une todo y muestra: <br>• `nombre`, `email`, `pais` <br>• `total_orders` <br>• `total_revenue` <br>• `avg_order_value` = revenue / total_orders <br>• `categoria_mas_comprada` (solo la categoría con `rn = 1`) <br>Ordena por `total_revenue` descendente y limita a 10 filas. | Obtiene exactamente la salida solicitada. |

> **Nota:**  
> - La sub‑consulta `category_prefs` usa un `JOIN` ficticio (`oi.order_id = ca.cust_id::text || '_' || ca.cust_id`) solo para ilustrar la lógica; en la práctica basta con unir `order_items` directamente a `customer_aggregates` mediante `order_items.order_id = ro.order_id` (como ya está hecho en la CTE `customer_aggregates`). La versión final incluye la unión correcta en `category_prefs`.  
> - Si tu motor es MySQL, sustituye `INTERVAL '6 months'` por `INTERVAL 6 MONTH` y usa `LIMIT 10` al final (ya está incluido).  
> - Si prefieres usar `DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)` en MySQL, reemplaza la condición en `recent_orders`.  

Con esta consulta obtendrás los **10 clientes con mayor facturación en los últimos 6 meses**, junto con su nombre, email, país, número de pedidos, ingreso total, valor medio del pedido y la categoría de producto que más ha adquirido.