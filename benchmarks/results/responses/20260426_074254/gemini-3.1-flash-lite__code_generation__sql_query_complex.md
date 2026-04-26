# Gemini 3.1 Flash Lite — code_generation/sql_query_complex

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 7.95 | quality: 9.72
- latency_total: 3.058s | tokens_per_second: 255.1
- input_tokens: 161 | output_tokens: 780
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para resolver este requerimiento, necesitamos realizar varias operaciones: filtrar por fecha y estado, agrupar por cliente, calcular métricas y determinar la categoría más comprada mediante una subconsulta o una función de ventana.

Aquí tienes la query SQL:

```sql
WITH CustomerStats AS (
    -- Calculamos métricas básicas por cliente
    SELECT 
        c.id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
CategoryRanking AS (
    -- Determinamos la categoría más comprada por cada cliente
    SELECT 
        o.customer_id,
        p.category,
        COUNT(*) as cat_count,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rank
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cr.category AS categoria_mas_comprada
FROM CustomerStats cs
JOIN CategoryRanking cr ON cs.id = cr.customer_id AND cr.rank = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:

1.  **`CustomerStats` (CTE):** Filtra las órdenes que están `completed` y que ocurrieron en los últimos 6 meses. Agrupa por cliente para obtener las métricas solicitadas (`total_orders`, `total_revenue`, `avg_order_value`) y aplica el filtro del `HAVING COUNT(*) >= 3`.
2.  **`CategoryRanking` (CTE):** Esta parte es crucial. Unimos `orders` con `order_items` y `products` para contar cuántas veces cada cliente ha comprado en cada categoría. Usamos `ROW_NUMBER()` particionado por `customer_id` para identificar cuál es la categoría con mayor frecuencia (`rank = 1`).
3.  **Consulta Final:** Unimos ambos resultados. Seleccionamos el top 10 ordenado por `total_revenue` de forma descendente.

**Notas:**
*   **Sintaxis:** He utilizado `INTERVAL '6 months'`, que es estándar en PostgreSQL. Si usas **MySQL**, cámbialo por `DATE_SUB(NOW(), INTERVAL 6 MONTH)`. Si usas **SQL Server**, usa `DATEADD(month, -6, GETDATE())`.
*   **Rendimiento:** Si la base de datos es muy grande, asegúrate de tener índices en `orders.customer_id`, `orders.status` y `orders.created_at`.