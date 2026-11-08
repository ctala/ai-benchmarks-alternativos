# Claude Fable 5.1 — code_generation/sql_query_complex

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.73 | quality: 9.6
- latency_total: 18.005s | tokens_per_second: 89.1
- input_tokens: 223 | output_tokens: 1605
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

```sql
WITH ordenes_recientes AS (
    SELECT
        o.id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

resumen_clientes AS (
    SELECT
        customer_id,
        COUNT(*)      AS total_orders,
        SUM(total)    AS total_revenue,
        AVG(total)    AS avg_order_value
    FROM ordenes_recientes
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

categoria_por_cliente AS (
    SELECT
        orr.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS gasto_categoria,
        ROW_NUMBER() OVER (
            PARTITION BY orr.customer_id
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC, SUM(oi.quantity) DESC
        ) AS rn
    FROM ordenes_recientes orr
    JOIN order_items oi ON oi.order_id = orr.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY orr.customer_id, p.category
)

SELECT
    c.name                                   AS nombre,
    c.email,
    c.country                                AS pais,
    rc.total_orders,
    ROUND(rc.total_revenue, 2)               AS total_revenue,
    ROUND(rc.avg_order_value, 2)             AS avg_order_value,
    cpc.category                             AS categoria_mas_comprada
FROM resumen_clientes rc
JOIN customers c
    ON c.id = rc.customer_id
LEFT JOIN categoria_por_cliente cpc
    ON cpc.customer_id = rc.customer_id
   AND cpc.rn = 1
ORDER BY rc.total_revenue DESC
LIMIT 10;
```

**Notas sobre la query:**

- **`ordenes_recientes`**: filtra una sola vez las órdenes completadas de los últimos 6 meses y se reutiliza en los otros CTEs, así el criterio es consistente en todas las métricas.
- **`resumen_clientes`**: calcula órdenes, revenue y ticket promedio usando `orders.total`. El `HAVING COUNT(*) >= 3` aplica el mínimo de órdenes.
- **`categoria_por_cliente`**: suma el gasto (`quantity * unit_price`) por cliente y categoría, y con `ROW_NUMBER()` se queda con la categoría de mayor gasto. Usé la cantidad total como desempate; si prefieres definir "más comprada" por unidades en lugar de dinero, solo invierte el orden del `ORDER BY` dentro del `OVER`.
- **`LEFT JOIN`** en la categoría para que un cliente no desaparezca si por alguna inconsistencia de datos no tuviera `order_items`.

**Ajustes según el motor de base de datos:**

| Motor | Cambio |
|---|---|
| PostgreSQL | Funciona tal cual. |
| MySQL 8+ | Cambiar el filtro de fecha por `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`. |
| SQL Server | Fecha: `o.created_at >= DATEADD(MONTH, -6, CAST(GETDATE() AS DATE))` y reemplazar `LIMIT 10` por `SELECT TOP 10`. |

Si quisieras que `total_revenue` se calcule desde `order_items` en vez de `orders.total` (por ejemplo, si `total` incluye envío o impuestos), puedo ajustarte la versión.