# GPT-OSS 20B — code_generation/sql_query_complex

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.3 | quality: 10.0
- latency_total: 14.351s | tokens_per_second: 116.1
- input_tokens: 195 | output_tokens: 1666
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

Aquí tienes una solución que funciona en la mayoría de los SGBD SQL (PostgreSQL, MySQL 8+, SQL‑Server 2012+, Oracle 12c+).  
El enfoque se basa en:

1. **Filtrar** solo pedidos “completed” de los últimos 6 meses.  
2. **Calcular** el revenue de cada pedido (suma de `quantity * unit_price`).  
3. **Agrupar** por cliente para obtener:
   * `total_orders` – número de pedidos completados.  
   * `total_revenue` – suma de todos los revenue de sus pedidos.  
   * `avg_order_value` – `total_revenue / total_orders`.  
4. **Obtener la categoría más comprada** del cliente mediante una subconsulta correlacionada.  
5. **Filtrar** clientes que tengan ≥ 3 pedidos y, finalmente,  
6. **Ordenar** por `total_revenue` y limitar a los 10 primeros.

```sql
/* 1. Calcular el revenue de cada pedido completado en los últimos 6 meses  */
WITH order_revenue AS (
    SELECT
        o.id                  AS order_id,
        o.customer_id,
        SUM(oi.quantity * oi.unit_price) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.id, o.customer_id
),

/* 2. Resúmenes por cliente (solo con ≥ 3 pedidos) */
customer_summary AS (
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(or.order_id)                AS total_orders,
        SUM(or.revenue)                   AS total_revenue,
        SUM(or.revenue) / NULLIF(COUNT(or.order_id),0) AS avg_order_value
    FROM customers c
    JOIN order_revenue or ON or.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(or.order_id) >= 3
)

SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,

    /* 3. Categoría más comprada por cada cliente */
    (
        SELECT p.category
        FROM order_items oi
        JOIN products p ON oi.product_id = p.id
        JOIN orders o ON oi.order_id = o.id
        WHERE o.customer_id = cs.id
          AND o.status = 'completed'
          AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
        GROUP BY p.category
        ORDER BY SUM(oi.quantity) DESC
        LIMIT 1
    ) AS category_mas_comprada

FROM customer_summary cs
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación rápida

| Paso | Qué hace | Por qué |
|------|----------|---------|
| 1 | `order_revenue` | Calcula el revenue por pedido (útil para evitar repetir la suma). |
| 2 | `customer_summary` | Agrupa por cliente y filtra los que tienen al menos 3 pedidos. |
| 3 | Subconsulta correlacionada | Encuentra la categoría con mayor cantidad comprada por ese cliente. |
| 4 | `ORDER BY total_revenue DESC LIMIT 10` | Devuelve los 10 clientes con mayor revenue. |

Si tu RDBMS no soporta CTEs (`WITH`) o la función `INTERVAL`, adapta la sintaxis (por ejemplo, en MySQL usar `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`).

¡Listo! Esta query te devuelve las columnas solicitadas con los clientes top 10 por revenue de los últimos 6 meses.