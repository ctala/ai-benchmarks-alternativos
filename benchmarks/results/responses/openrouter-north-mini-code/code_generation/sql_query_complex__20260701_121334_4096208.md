# North Mini Code — code_generation/sql_query_complex

- model_id: `cohere/north-mini-code:free`
- success: True  | final: 8.56 | quality: 9.34
- latency_total: 55.739s | tokens_per_second: 36.7
- input_tokens: 140 | output_tokens: 2045

## Respuesta completa

**Consulta – “Top 10 clientes por revenue (últimos 6 meses)”**

```sql
/* -------------------------------------------------------------
   Resultado (Top 10 clientes por revenue total en los últimos 6 meses)
   -------------------------------------------------------------
   • Solo se tienen en cuenta los pedidos COMPLETADOS.
   • Se muestran solo los clientes con ≥ 3 pedidos completados en el período.
   • Las columnas son exactamente las que pediste.
   ------------------------------------------------------------- */

WITH completed_orders AS (
    /* 1️⃣  Pedidos completados de los últimos 6 meses – agregamos el revenue por cliente */
    SELECT
        c.id                 AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,               -- número de pedidos
        SUM(o.total)         AS total_revenue               -- revenue (order.total ya incluye todo)
    FROM customers c
    JOIN orders o
          ON o.customer_id = c.id
         AND o.status = 'completed'
         /* ---------------------------  Filtro de fecha (ajusta a tu BD) ----------- */
         AND o.created_at >=
             CASE
                 /* SQL Server / PostgreSQL / MySQL (5.7+) – usa la función de tu BD */
                 WHEN TRIM(LOWER(SUBSTR(&#39;SQL_SERVER&#39;,1,1))) = 's' THEN DATEADD(month, -6, CURRENT_TIMESTAMP)
                 WHEN TRIM(LOWER(SUBSTR(&#39;POSTGRES&#39;,1,1))) = 'p' THEN CURRENT_DATE - INTERVAL &#39;6 months&#39;
                 ELSE DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)   /* MySQL */
             END
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3                /* al menos 3 pedidos completados */
),
category_qty AS (
    /* 2️⃣  Cantidad total comprada por cliente y categoría (mismo período) */
    SELECT
        c.customer_id,
        p.category,
        SUM(oi.quantity) AS qty
    FROM completed_orders c                -- reutilizamos el CTE anterior (ya filtrado)
    JOIN orders o
          ON o.customer_id = c.customer_id
         AND o.status = 'completed'
    JOIN order_items oi
          ON oi.order_id = o.id
    JOIN products p
          ON p.id = oi.product_id
    GROUP BY c.customer_id, p.category
),
top_category AS (
    /* 3️⃣  Elegimos la *categoría más comprada* por cliente (cantidad) */
    SELECT
        customer_id,
        category AS categoria_mas_comprada,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY qty DESC) AS rn
    FROM category_qty
)
SELECT
    co.name,
    co.email,
    co.country,
    co.total_orders,
    co.total_revenue,
    /* media por pedido – protegemos de una división por cero (no debería ocurrir) */
    co.total_revenue / NULLIF(co.total_orders, 0) AS avg_order_value,
    tc.categoria_mas_comprada
FROM completed_orders co
LEFT JOIN top_category tc
       ON tc.customer_id = co.customer_id
      AND tc.rn = 1                     /* solo la mejor categoría */
ORDER BY co.total_revenue DESC
LIMIT 10;      -- top 10
```

### Cómo funciona

| CTE | Propósito |
|-----|---------|
| **completed_orders** | Calcula, por cliente, el número de pedidos (`total_orders`) y el revenue total (`total_revenue`) para los últimos 6 meses **solo** para pedidos con `status = 'completed'`. También aplica el filtro `HAVING` (≥ 3 pedidos). |
| **category_qty** | Para cada cliente y categoría, suma las cantidades (`quantity`) de los artículos vendidos en el mismo período, usando los mismos filtros de `orders`. |
| **top_category** | Usa `ROW_NUMBER()` para elegir la categoría con mayor cantidad total por cliente (si hay un empate, se elige una arbitrariamente). |
| **SELECT final** | Devuelve las 10 filas con mayor `total_revenue`, mostrando el nombre, email, país, total_orders, total_revenue, avg_order_value y la `categoria_mas_comprada`. |

### Notas sobre la **función de fecha**

El filtro de fecha usa una expresión `CASE` que puedes adaptar al dialecto exacto de SQL que usas:

| BD | Función de fecha para “últimos