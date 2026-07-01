# North Mini Code — code_generation/sql_query_complex

- model_id: `cohere/north-mini-code:free`
- success: True  | final: 8.24 | quality: 8.67
- latency_total: 34.391s | tokens_per_second: 57.1
- input_tokens: 140 | output_tokens: 1963

## Respuesta completa

**Consulta – “Top 10 clientes por revenue (últimos 6 meses)”**

```sql
/* -------------------------------------------------------------
   1️⃣  Estadísticas de clientes (orders completados en los últimos 6 meses)
   ------------------------------------------------------------- */
WITH customer_stats AS (
    SELECT
        c.id            AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id)               AS total_orders,
        SUM(oi.quantity * oi.unit_price)  AS total_revenue
    FROM customers c

    /* Pedidos completados dentro del período de 6 meses */
    JOIN orders o
          ON o.customer_id = c.id
         AND o.status = 'completed'
         AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'

    /* Artículos del pedido (precio en el momento de la compra) */
    JOIN order_items oi
          ON oi.order_id = o.id

    GROUP BY c.id, c.name, c.email, c.country

    /* Mantener solo los que realizaron ≥ 3 pedidos */
    HAVING COUNT(DISTINCT o.id) >= 3
),


/* -------------------------------------------------------------
   2️⃣  Cantidad por categoría para cada cliente (mismo período)
   ------------------------------------------------------------- */
, customer_category AS (
    SELECT
        cs.customer_id,
        p.category,
        SUM(oi.quantity) AS qty_by_cat
    FROM customer_stats cs

    /* Volver a unir orders y order_items para obtener las categorías */
    JOIN orders o
          ON o.customer_id = cs.customer_id
         AND o.status = 'completed'
         AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'

    JOIN order_items oi
          ON oi.order_id = o.id

    JOIN products p
          ON p.id = oi.product_id

    GROUP BY cs.customer_id, p.category
),


/* -------------------------------------------------------------
   3️⃣  Elegir la categoría con mayor cantidad para cada cliente
   ------------------------------------------------------------- */
, most_purchased AS (
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY qty_by_cat DESC
        ) AS rn
    FROM customer_category
)


/* -------------------------------------------------------------
   4️⃣  Consulta final – Top 10 por total_revenue
   ------------------------------------------------------------- */
SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    /* Avg order value – proteger contra división por cero */
    cs.total_revenue / NULLIF(cs.total_orders,0) AS avg_order_value,
    mp.category AS most_purchased_category
FROM customer_stats cs

/* Unir solo la categoría principal (rn = 1) */
LEFT JOIN most_purchased mp
       ON mp.customer_id = cs.customer_id
      AND mp.rn = 1

ORDER BY cs.total_revenue DESC
LIMIT 10;
```

**¿Qué hace?**

| CTE | Propósito |
|-----|---------|
| **customer_stats** | Calcula, por cliente, `total_orders` y `total_revenue` para pedidos **completados** dentro de los últimos 6 meses. Mantiene solo a aquellos con **≥ 3 pedidos** (`HAVING`). |
| **customer_category** | Para cada cliente, suma las cantidades (`qty_by_cat`) por `category` (todavía limitado al mismo período y a pedidos completados). |
| **most_purchased** | Asigna un número de fila a cada categoría por cliente, ordenada por cantidad descendente; la primera fila (`rn = 1`) es la “categoría más comprada”. |
| **Consulta final** | Devuelve las 10 columnas solicitadas, ordenadas por `total_revenue` descendente. `avg_order_value` se calcula como `total_revenue / total_orders` (con `NULLIF` para evitar una división por cero). `most_purchased_category` proviene del CTE `most_purchased`. |

**Notas / Ajustes**

* **Función de fecha** – La expresión `CURRENT_DATE - INTERVAL '6 months'` es el estilo estándar de ANSI‑SQL (funciona en PostgreSQL, Redshift, Snowflake, etc.). Si estás en MySQL, usa `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`; en SQL Server, `DATEADD(month, -6, GETDATE())`.
* **Precio** – La consulta utiliza `order_items.unit_price` (el precio en el momento de la compra). Si prefieres el precio actual de `products.price`, reemplaza `oi.quantity * oi.unit_price` con `oi.quantity * p.price`.
* **Empates** – `ROW_NUMBER()` elige una sola categoría cuando hay un empate. Si deseas conservar *todas* las categorías que comparten la cantidad máxima, reemplaza `ROW_NUMBER()` con `RANK()` o `DENSE_RANK()` y ajusta la unión en consecuencia.
* **Ordenación** – La ordenación final (`ORDER BY total_revenue DESC`) garantiza que se devuelvan los 10 clientes con mayor revenue; `LIMIT 10` limita el conjunto de resultados.

Puedes copiar esta consulta directamente en tu cliente SQL (reemplazando los nombres de las tablas/columnas si son diferentes) y te dará el Top‑10 de clientes según tus especificaciones. ¡Feliz consulta!