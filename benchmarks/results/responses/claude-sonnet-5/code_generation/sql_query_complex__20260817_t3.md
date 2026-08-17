# Claude Sonnet 5 — code_generation/sql_query_complex

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 16.267s | tokens_per_second: 106.7
- input_tokens: 221 | output_tokens: 1735
- judge_score: 5 | justificación: La respuesta es precisa, relevante, y profundiza en la tarea al proporcionar una consulta SQL bien estructurada que cumple con todos los requisitos especificados, incluyendo el cálculo de la categoría más comprada por cliente. La claridad y organización de la consulta facilitan su comprensión y aplicación, haciéndola altamente útil para un emprendedor.

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
WITH ordenes_periodo AS (
    -- Filtramos órdenes completadas de los últimos 6 meses
    SELECT
        o.id,
        o.customer_id,
        o.total,
        o.created_at
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

resumen_cliente AS (
    -- Métricas agregadas por cliente
    SELECT
        customer_id,
        COUNT(id)          AS total_orders,
        SUM(total)         AS total_revenue,
        AVG(total)         AS avg_order_value
    FROM ordenes_periodo
    GROUP BY customer_id
    HAVING COUNT(id) >= 3
),

categoria_por_cliente AS (
    -- Cantidad comprada por cliente y categoría, solo dentro del periodo/órdenes relevantes
    SELECT
        op.customer_id,
        p.category,
        SUM(oi.quantity) AS unidades_compradas
    FROM ordenes_periodo op
    JOIN order_items oi ON oi.order_id = op.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY op.customer_id, p.category
),

categoria_top AS (
    -- Rankeamos categorías por cliente y nos quedamos con la #1
    SELECT
        customer_id,
        category,
        unidades_compradas,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY unidades_compradas DESC
        ) AS rn
    FROM categoria_por_cliente
)

SELECT
    c.name                              AS nombre,
    c.email,
    c.country                           AS pais,
    rc.total_orders,
    rc.total_revenue,
    ROUND(rc.avg_order_value, 2)        AS avg_order_value,
    ct.category                         AS categoria_mas_comprada
FROM resumen_cliente rc
JOIN customers c
    ON c.id = rc.customer_id
LEFT JOIN categoria_top ct
    ON ct.customer_id = rc.customer_id
   AND ct.rn = 1
ORDER BY rc.total_revenue DESC
LIMIT 10;
```

### Notas sobre la query

1. **`ordenes_periodo`**: filtra únicamente órdenes con `status = 'completed'` dentro de los últimos 6 meses, evitando recalcular esta condición varias veces.

2. **`resumen_cliente`**: agrupa por cliente y aplica el filtro `HAVING COUNT(id) >= 3` para asegurar mínimo 3 órdenes completadas.

3. **`categoria_por_cliente` + `categoria_top`**: calculan la categoría con más unidades compradas por cliente usando `ROW_NUMBER()`. Si prefieres que "más comprada" se defina por **revenue** en lugar de unidades, cambia:
   ```sql
   SUM(oi.quantity) AS unidades_compradas
   ```
   por:
   ```sql
   SUM(oi.quantity * oi.unit_price) AS revenue_categoria
   ```

4. **`LEFT JOIN` con `categoria_top`**: por si algún cliente cumple las órdenes pero no tiene items registrados (edge case), evitando perder la fila del cliente.

5. Ajusta `CURRENT_DATE - INTERVAL '6 months'` según el motor de BD:
   - PostgreSQL: tal como está.
   - MySQL: `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`
   - SQL Server: `DATEADD(MONTH, -6, GETDATE())`