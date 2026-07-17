# Nemotron 3 Nano Omni 30B-A3B Reasoning — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 9.02 | quality: 9.8
- latency_total: 8.134s | tokens_per_second: 222.3
- input_tokens: 160 | output_tokens: 1808
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y prácticamente útil, proporcionando una consulta SQL bien estructurada que cumple con los requisitos especificados, con una profundidad adecuada al incluir una subconsulta para la categoría más comprada.

## Respuesta completa

**SQL (MySQL / MariaDB)**  

```sql
/*  Top 10 clientes con al menos 3 órdenes completadas en los últimos 6 meses
    mostrando: nombre, email, país, total de órdenes, revenue total,
    valor medio por orden y la categoría que más ha comprado                */
SELECT
    c.name                                      AS nombre,
    c.email                                     AS email,
    c.country                                   AS pais,
    COUNT(o.id)                                 AS total_orders,
    SUM(oi.quantity * oi.unit_price)            AS total_revenue,
    ROUND( SUM(oi.quantity * oi.unit_price) / COUNT(o.id) , 2) AS avg_order_value,
    /* categoría con mayor gasto (revenue) para ese cliente */
    ( SELECT p.category
      FROM order_items oi_cat
      JOIN products p      ON p.id = oi_cat.product_id
      WHERE oi_cat.order_id = o.id               -- solo los ítems del cliente
      GROUP BY p.category
      ORDER BY SUM(oi_cat.quantity * oi_cat.unit_price) DESC
      LIMIT 1
    )                                           AS categoria_mas_comprada
FROM   orders       o
JOIN   customers    c  ON c.id = o.customer_id
JOIN   order_items  oi ON oi.order_id = o.id
WHERE  o.status = 'completed'
  AND  o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)   -- últimos 6 meses
GROUP BY c.id, c.name, c.email, c.country                -- agrupar por cliente
HAVING COUNT(o.id) >= 3                                   -- al menos 3 órdenes
ORDER BY total_revenue DESC
LIMIT 10;
```

### Explicación paso a paso  

| Paso | Qué hace | Detalle |
|------|----------|---------|
| **FROM / JOIN** | Une las tablas `orders → customers → order_items` | Necesario para poder contar órdenes y sumar los importes por cliente. |
| **WHERE** | Filtra sólo órdenes **completadas** (`status = 'completed'`) y que se hayan creado en los **últimos 6 meses** (`created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`). |
| **GROUP BY** | Agrupa los resultados por cliente (`c.id`). | Con esto podemos contar y sumar por cliente. |
| **COUNT(o.id)** | `total_orders` – número de órdenes del cliente. |
| **SUM(oi.quantity * oi.unit_price)** | `total_revenue` – facturación total del cliente en el período. |
| **AVG_ORDER_VALUE** | `total_revenue / total_orders`, redondeado a 2 decimales. |
| **Sub‑query de la categoría** | Busca, dentro de los ítems del cliente, la categoría con mayor suma de `quantity * unit_price`. Usa `GROUP BY p.category` y `ORDER BY … DESC LIMIT 1`. |
| **HAVING** | Garantiza que el cliente tenga **al menos 3 órdenes** (`COUNT(o.id) >= 3`). |
| **ORDER BY total_revenue DESC** | Ordena de mayor a menor revenue. |
| **LIMIT 10** | Devuelve solo los 10 primeros clientes. |

> **Nota:** Si tu motor de base de datos es PostgreSQL, la sintaxis es idéntica salvo por la función de fecha (`CURRENT_DATE - INTERVAL '6 months'`) y por la disponibilidad de `ROW_NUMBER()` si prefieres usar una CTE para la categoría más comprada. El resto del query funciona tal cual.