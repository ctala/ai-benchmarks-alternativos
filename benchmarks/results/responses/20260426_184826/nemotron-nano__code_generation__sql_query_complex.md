# Nemotron 3 Nano 30B — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.83 | quality: 9.24
- latency_total: 23.41s | tokens_per_second: 97.4
- input_tokens: 160 | output_tokens: 2281
- judge_score: 4.6 | justificación: 

## Respuesta completa

**Consulta SQL**

```sql
/*  Top 10 clientes con mayor revenue en los últimos 6 meses
    (solo órdenes completadas y al menos 3 de ellas)                */
SELECT
    c.name                                   AS nombre,
    c.email                                  AS email,
    c.country                                AS pais,
    COUNT(o.id)                              AS total_orders,
    SUM(o.total)                             AS total_revenue,
    AVG(o.total)                             AS avg_order_value,
    /* categoría que el cliente ha comprado más (por cantidad) */
    cat_most_frequent.category               AS categoria_mas_comprada
FROM customers AS c
/* --------------------------------------------------------------- */
JOIN orders AS o          ON o.customer_id = c.id
/* --------------------------------------------------------------- */
WHERE o.status = 'completed'                                 -- solo órdenes terminadas
  AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH) -- últimos 6 meses
GROUP BY c.id, c.name, c.email, c.country
HAVING COUNT(o.id) >= 3                                      -- al menos 3 órdenes completadas
/* --------------------------------------------------------------- */
ORDER BY total_revenue DESC
LIMIT 10;
```

### Detalle del cálculo de **categoria_mas_comprada**

```sql
(SELECT p.category
 FROM order_items AS oi
 JOIN products AS p ON oi.product_id = p.id
 WHERE oi.order_id IN (
        SELECT o.id
        FROM orders AS o
        WHERE o.customer_id = c.id
          AND o.status = 'completed'
          AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
      )
 GROUP BY p.category
 ORDER BY SUM(oi.quantity) DESC          -- mayor cantidad total
 LIMIT 1
) AS cat_most_frequent
```

### Explicación paso a paso

| Paso | Qué hace | Comentario |
|------|----------|------------|
| **Filtrado de órdenes** | `WHERE o.status='completed' AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` | Sólo consideramos órdenes terminadas y dentro del rango de los últimos 6 meses. |
| **Agrupación por cliente** | `GROUP BY c.id, c.name, c.email, c.country` | Cada fila de la consulta agrupa todos los pedidos de un cliente. |
| **Contar y sumar** | `COUNT(o.id) AS total_orders`, `SUM(o.total) AS total_revenue`, `AVG(o.total) AS avg_order_value` | Obtención de número de órdenes, revenue total y valor medio por orden. |
| **Cliente con ≥ 3 órdenes** | `HAVING COUNT(o.id) >= 3` | Excluimos a los clientes que no cumplen esa condición. |
| **Ordenamiento y límite** | `ORDER BY total_revenue DESC LIMIT 10` | Obtención de los 10 clientes con mayor revenue. |
| **Categoría más comprada** | Sub‑consulta que suma `quantity` por `category` dentro de los pedidos del cliente y devuelve la categoría con mayor suma. | Se usa `LIMIT 1` para quedarse con la categoría de mayor movimiento (en unidades). |

> **Nota:**  
> - Si prefieres que la categoría se base en **revenue** en lugar de **cantidad**, cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)` en la sub‑consulta.  
> - La cláusula `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` asume que la base de datos es MySQL/MariaDB. En PostgreSQL usarías `CURRENT_DATE - INTERVAL '6 months'`. Ajusta según tu motor.  

Esta consulta devuelve exactamente las columnas solicitadas, ordenadas por `total_revenue` de mayor a menor, y solo incluye clientes que hayan realizado al menos 3 órdenes completadas en los últimos seis meses.