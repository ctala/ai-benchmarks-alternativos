# Claude Opus 4.8 — code_generation/sql_query_complex

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 19.548s | tokens_per_second: 94.3
- input_tokens: 221 | output_tokens: 1843
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada y considerando diferentes motores de base de datos.

## Respuesta completa

# Query SQL: Top 10 Clientes por Revenue

```sql
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(o.total) AS total_revenue,
    ROUND(AVG(o.total), 2) AS avg_order_value,
    (
        SELECT p.category
        FROM order_items oi
        JOIN orders o2 ON oi.order_id = o2.id
        JOIN products p ON oi.product_id = p.id
        WHERE o2.customer_id = c.id
          AND o2.status = 'completed'
          AND o2.created_at >= CURRENT_DATE - INTERVAL '6 months'
        GROUP BY p.category
        ORDER BY SUM(oi.quantity) DESC
        LIMIT 1
    ) AS categoria_mas_comprada
FROM customers c
JOIN orders o ON o.customer_id = c.id
WHERE o.status = 'completed'
  AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
GROUP BY c.id, c.name, c.email, c.country
HAVING COUNT(DISTINCT o.id) >= 3
ORDER BY total_revenue DESC
LIMIT 10;
```

## Explicación de los componentes clave

| Requisito | Implementación |
|-----------|---------------|
| **Últimos 6 meses** | `o.created_at >= CURRENT_DATE - INTERVAL '6 months'` |
| **Solo completadas** | `WHERE o.status = 'completed'` |
| **Mínimo 3 órdenes** | `HAVING COUNT(DISTINCT o.id) >= 3` |
| **Ordenar por revenue** | `ORDER BY total_revenue DESC` |
| **Top 10** | `LIMIT 10` |
| **Categoría más comprada** | Subquery correlacionada por cantidad total |

## Notas importantes

1. **Sintaxis de fecha**: El ejemplo usa PostgreSQL. Para otros motores:
   - **MySQL**: `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`
   - **SQL Server**: `o.created_at >= DATEADD(MONTH, -6, GETDATE())`

2. **`COUNT(DISTINCT o.id)`**: Uso `DISTINCT` por seguridad, aunque agrupando solo por órdenes no habría duplicados en esta query.

3. **`categoria_mas_comprada`**: La subquery calcula la categoría con mayor cantidad (`quantity`) comprada. Si prefieres por **revenue** en lugar de cantidad, cambia:
   ```sql
   ORDER BY SUM(oi.quantity * oi.unit_price) DESC
   ```

## Alternativa con CTE (más legible y eficiente)

Si tu motor lo soporta, esta versión evita la subquery correlacionada:

```sql
WITH clientes_top AS (
    SELECT
        c.id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        ROUND(AVG(o.total), 2) AS avg_order_value
    FROM customers c
    JOIN orders o ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
    ORDER BY total_revenue DESC
    LIMIT 10
),
categorias AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
SELECT
    ct.nombre,
    ct.email,
    ct.pais,
    ct.total_orders,
    ct.total_revenue,
    ct.avg_order_value,
    cat.category AS categoria_mas_comprada
FROM clientes_top ct
LEFT JOIN categorias cat
    ON cat.customer_id = ct.id AND cat.rn = 1
ORDER BY ct.total_revenue DESC;
```

**Ventaja de la versión con CTE**: procesa la categoría más comprada una sola vez con `ROW_NUMBER()` en lugar de ejecutar una subquery por cada fila, lo que mejora el rendimiento con muchos datos.

¿Quieres que la adapte a un motor específico o que añada algún filtro adicional (por país, por rango de fechas exacto, etc.)?