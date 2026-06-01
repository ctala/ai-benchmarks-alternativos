# DeepSeek V4 Flash (OpenRouter) — code_generation/sql_query_complex

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.51 | quality: 9.72
- latency_total: 22.209s | tokens_per_second: 113.2
- input_tokens: 152 | output_tokens: 2514
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL solicitada, que obtiene el top 10 de clientes con mayor ingreso total en los últimos 6 meses, cumpliendo con los filtros y columnas especificados.

```sql
WITH 
-- Órdenes completadas en los últimos 6 meses
ordenes_ultimos_meses AS (
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),

-- Estadísticas por cliente (nombre, email, país, total órdenes, ingresos, valor promedio)
stats_clientes AS (
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        SUM(o.total) / NULLIF(COUNT(DISTINCT o.id), 0) AS avg_order_value
    FROM customers c
    INNER JOIN ordenes_ultimos_meses o ON c.id = o.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.id) >= 3
),

-- Cantidad total comprada por categoría por cliente
cantidad_por_categoria AS (
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty
    FROM ordenes_ultimos_meses o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
),

-- Ranking de categorías por cliente (la más comprada, y por orden alfabético si hay empate)
ranking_categorias AS (
    SELECT 
        customer_id,
        category,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY total_qty DESC, category ASC
        ) AS rn
    FROM cantidad_por_categoria
)

-- Resultado final
SELECT 
    s.name,
    s.email,
    s.country,
    s.total_orders,
    s.total_revenue,
    s.avg_order_value,
    r.category AS categoria_mas_comprada
FROM stats_clientes s
LEFT JOIN ranking_categorias r ON s.id = r.customer_id AND r.rn = 1
ORDER BY s.total_revenue DESC
LIMIT 10;
```

### Explicación breve
1. **Filtro temporal**: Solo órdenes con `status = 'completed'` y creadas en los últimos 6 meses.  
2. **Clientes con al menos 3 órdenes completadas**: Aplicado mediante `HAVING COUNT(DISTINCT o.id) >= 3` en el mismo período.  
3. **Cálculos**:
   - `total_revenue`: suma de `total` de las órdenes.  
   - `avg_order_value`: ingreso total entre número de órdenes.  
   - `categoria_mas_comprada`: se obtiene sumando la cantidad de productos por categoría y seleccionando la primera según el ranking (mayor cantidad; en caso de empate, alfabéticamente).  
4. **Resultado** ordenado por `total_revenue` descendente y limitado a 10 filas.

> **Nota**: Si tu gestor de base de datos usa otra sintaxis para intervalos (por ejemplo, `DATE_SUB(NOW(), INTERVAL 6 MONTH)` en MySQL), ajusta la línea `CURRENT_DATE - INTERVAL '6 months'` según corresponda.