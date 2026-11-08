# GLM 5.3 — code_generation/sql_query_complex

- model_id: `z-ai/glm-5.3`
- success: True  | final: 7.99 | quality: 9.6
- latency_total: 51.091s | tokens_per_second: 96.3
- input_tokens: 156 | output_tokens: 4919
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

Aquí tienes la query (sintaxis PostgreSQL):

```sql
WITH lineas AS (
    -- Items de órdenes completadas en los últimos 6 meses
    SELECT
        o.customer_id,
        o.id                            AS order_id,
        p.category,
        oi.quantity,
        oi.quantity * oi.unit_price     AS line_total
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p     ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
stats_clientes AS (
    SELECT
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT l.order_id)  AS total_orders,
        SUM(l.line_total)           AS total_revenue
    FROM lineas l
    JOIN customers c ON c.id = l.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT l.order_id) >= 3
),
categorias AS (
    -- Ranking de categorías por cliente según dinero gastado
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id
            ORDER BY SUM(line_total) DESC, category ASC
        ) AS rn
    FROM lineas
    GROUP BY customer_id, category
)
SELECT
    s.name     AS nombre,
    s.email,
    s.country  AS pais,
    s.total_orders,
    ROUND(s.total_revenue, 2)              AS total_revenue,
    ROUND(s.total_revenue / s.total_orders, 2) AS avg_order_value,
    cat.category                           AS categoria_mas_comprada
FROM stats_clientes s
LEFT JOIN categorias cat
       ON cat.customer_id = s.id AND cat.rn = 1
ORDER BY s.total_revenue DESC
LIMIT 10;
```

**Decisiones y supuestos:**

- **Filtros combinados**: interpreto que tanto el revenue como el mínimo de 3 órdenes aplican sobre el mismo conjunto (órdenes `completed` dentro de los últimos 6 meses). Si el mínimo de 3 órdenes fuera histórico, habría que relajar el filtro en `stats_clientes`.
- **Revenue desde `order_items`**: calculo `quantity * unit_price` en vez de usar `orders.total`, porque así el revenue y la categoría provienen de los mismos datos a nivel línea. Si confías en `orders.total`, puedes simplificar el CTE `stats_clientes` con `SUM(o.total)` y `AVG(o.total)` sin unir `order_items`.
- **`categoria_mas_comprada`**: la defino como la categoría con más **dinero gastado**. Si prefieres "más unidades compradas", cambia `SUM(line_total)` por `SUM(quantity)` en el ORDER BY del `ROW_NUMBER()`. El `category ASC` es un desempate determinista.
- **`COUNT(DISTINCT order_id)`**: necesario porque un cliente con múltiples líneas por orden contaría órdenes de más si usaras `COUNT(*)`.

**Compatibilidad por dialecto:**

- **MySQL 8+**: cambia la fecha a `CURDATE() - INTERVAL 6 MONTH` (requiere MySQL 8 por las CTEs y window functions).
- **SQL Server**: usa `DATEADD(MONTH, -6, GETDATE())` y `SELECT TOP 10` en lugar de `LIMIT`.
- **SQLite**: `DATE('now', '-6 months')`.

Un detalle a considerar: si dos clientes empatan justo en el puesto 10, `LIMIT 10` corta arbitrariamente. Si necesitas manejar empates, se puede usar `RANK()` o `FETCH FIRST 10 ROWS WITH TIES` (Postgres 13+).