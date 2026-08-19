# Solar Pro 4 — code_generation/sql_query_complex

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 25.197s | tokens_per_second: 24.9
- input_tokens: 196 | output_tokens: 628
- judge_score: 5 | justificación: La respuesta es precisa, relevante y profunda, abordando todos los requisitos de la consulta SQL compleja con claridad y ofreciendo insights útiles, como el manejo de empates en la categoría más comprada y consideraciones de rendimiento.

## Respuesta completa

Aquí tienes la query SQL que cumple con todos los requisitos:

```sql
WITH clientes_6m AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        ROUND(AVG(o.total), 2) AS avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
categoria_top AS (
    SELECT 
        ci.customer_id,
        p.category,
        COUNT(oi.id) AS cantidad_items,
        ROW_NUMBER() OVER (
            PARTITION BY ci.customer_id 
            ORDER BY COUNT(oi.id) DESC, p.category ASC
        ) AS rn
    FROM order_items oi
    INNER JOIN orders o ON oi.order_id = o.id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY ci.customer_id, p.category
)
SELECT 
    cl.name AS nombre,
    cl.email,
    cl.country AS pais,
    cl.total_orders,
    cl.total_revenue,
    cl.avg_order_value,
    ct.category AS categoria_mas_comprada
FROM clientes_6m cl
LEFT JOIN categoria_top ct ON cl.id = ct.customer_id AND ct.rn = 1
ORDER BY cl.total_revenue DESC
LIMIT 10;
```

### 🔍 Notas importantes:
1. **`INTERVAL '6 months'`**: Es sintaxis estándar en PostgreSQL. Si usas otro motor, ajusta la comparación de fecha:
   - **MySQL**: `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`
   - **SQL Server**: `o.created_at >= DATEADD(month, -6, GETDATE())`
   - **SQLite**: `o.created_at >= DATE('now', '-6 months')`
2. **Manejo de empates en `categoria_mas_comprada`**: Se usa `ROW_NUMBER()` con `p.category ASC` como desempate. Si prefieres devolver **todas** las categorías empatadas, cambia `ROW_NUMBER()` por `RANK()` y ajusta el `JOIN` para permitir múltiples filas por cliente (o usa `STRING_AGG`/`GROUP_CONCAT` según tu SGBD).
3. **Rendimiento**: Asumiendo índices en `orders(customer_id, status, created_at)`, `order_items(order_id, product_id)` y `products(id)`, esta query es eficiente y evita subqueries correlacionados en el SELECT.