# Gemma 4 31B (Spark llama-server Q4_K_M) — code_generation/sql_query_complex

- model_id: `gemma-4-31B-it-Q4_K_M.gguf`
- success: True  | final: 8.03 | quality: 9.72
- latency_total: 81.494s | tokens_per_second: 9.8
- input_tokens: 173 | output_tokens: 795
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para lograr este resultado, necesitamos combinar varias tablas y utilizar una **Subquery** o un **CTE (Common Table Expression)** para determinar la categoría más comprada, ya que es un cálculo agregado diferente al del revenue.

Aquí tienes la query optimizada:

```sql
WITH CustomerStats AS (
    -- Calculamos las métricas generales de ventas por cliente
    SELECT 
        c.id AS customer_id,
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
        RANK() OVER (PARTITION BY o.customer_id ORDER BY COUNT(oi.id) DESC) as rank_cat
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
JOIN CategoryRanking cr ON cs.customer_id = cr.customer_id
WHERE cr.rank_cat = 1 -- Solo traemos la categoría número 1 de cada cliente
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de los pasos:

1.  **`CustomerStats` (CTE):** 
    *   Filtra las órdenes por estado `'completed'` y la fecha de los últimos 6 meses.
    *   Utiliza `HAVING COUNT(o.id) >= 3` para cumplir la condición de clientes con al menos 3 órdenes.
    *   Calcula el revenue total y el promedio por pedido.

2.  **`CategoryRanking` (CTE):**
    *   Une las tablas de órdenes, ítems y productos.
    *   Utiliza la función de ventana `RANK()` para numerar las categorías de cada cliente basándose en la cantidad de productos comprados (`COUNT`). La categoría más frecuente recibe el `rank_cat = 1`.

3.  **Query Final:**
    *   Une ambos resultados mediante el `customer_id`.
    *   Filtra `WHERE cr.rank_cat = 1` para evitar duplicados en caso de que un cliente haya comprado en varias categorías.
    *   Ordena por `total_revenue DESC` y limita el resultado a los 10 mejores.

**Nota sobre sintaxis:** He utilizado `CURRENT_DATE - INTERVAL '6 months'`, que es estándar en **PostgreSQL**. Si usas **MySQL**, deberías cambiarlo por `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.