# DiffusionGemma 26B-A4B (DGX Spark Q8_0) — code_generation/sql_query_complex

- model_id: `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0`
- success: True  | final: 8.06 | quality: 9.16
- latency_total: 115.488s | tokens_per_second: 17.7
- input_tokens: 0 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

## Respuesta completa

thought

*   `orders`: (id, customer_id, total, status, created_at)
*   `customers`: (id, name, email, country, created_at)
*   `order_items`: (id, order_id, product_id, quantity, unit_price)
*   `products`: (id, name, category, price)

    *   Top 10 customers by total revenue.
    *   Timeframe: Last 6 months.
    *   Columns: `name`, `email`, `country`, `total_orders`, `total_revenue`, `avg_order_value`, `categoria_mas_comprada`.
    *   Sorting: `total_revenue DESC`.
    *   Filter: At least 3 completed orders (`status = 'completed'`).

    *   *Step 1: Basic metrics (Revenue, Order Count, Avg Value).*
        Join `customers` and `orders`.
        Filter by `status = 'completed'` and `created_at >= NOW() - INTERVAL '6 months'`.
        Group by customer details.
        Filter `HAVING COUNT(orders.id) >= 3`.

    *   *Step 2: Most purchased category per customer.*
        This is the trickiest part because it requires counting occurrences of categories per customer and then picking the top one.
        This involves joining `orders`, `order_items`, and `products`.
        A window function like `ROW_NUMBER()` or `RANK()` is usually the best approach here.

    *   *Step 3: Combine everything.*
        Use Common Table Expressions (CTEs) to calculate the metrics and the category ranking separately, then join them together.

    *   *CTE 1: Customer Metrics*
        ```sql
        SELECT
            c.id,
            c.name,
            c.email,
            c.country,
            COUNT(o.id) as total_orders,
            SUM(o.total) as total_revenue,
            AVG(o.total) as avg_order_value
        FROM customers c
        JOIN orders o ON c.id = o.customer_id
        WHERE o.status = 'completed'
          AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
        GROUP BY c.id, c.name, c.email, c.country
        HAVING COUNT(o.id) >= 3
        ```

    *   *CTE 2: Category Ranking*
        ```sql
        SELECT
            o.customer_id,
            p.category,
            ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rank
        FROM orders o
        JOIN order_items oi ON o.id = oi.order_id
        JOIN products p ON oi.product_id = p.id
        WHERE o.status = 'completed'
          AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
        GROUP BY o.customer_id, p.category
        ```

    *   *Final Query:*
        Join CTE 1 and CTE 2 (where rank = 1).
        Limit 10.

    *   I'll use standard SQL (PostgreSQL compatible, as it's the most common for these types of requests, but I'll mention the date syntax for intervals).
    *   Wait, the `categoria_mas_comprada` should be based on the quantity of items or the frequency of orders? Usually, "most purchased" implies frequency or total quantity. I'll use frequency (`COUNT(*)`

    ```sql
    WITH customer_metrics AS (
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
    category_ranking AS (
        -- Calculamos la categoría más comprada por cada cliente
        SELECT
            o.customer_id,
            p.category,
            ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rn
        FROM orders o
        JOIN order_items oi ON o.id = oi.order_id
        JOIN products p ON oi.product_id = p.id
        WHERE o.status = 'completed'
          AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
        GROUP BY o.customer_id, p.category
    )
    SELECT
        cm.name,
        cm.email,
        cm.country,
        cm.total_orders,
        cm.total_revenue,
        cm.avg_order_value,
        cr.category AS categoria_mas_comprada
    FROM customer_metrics cm
    JOIN category_ranking cr ON cm.id = cr.customer_id AND cr.rn = 1
    ORDER BY cm.total_revenue DESC
    LIMIT 10;
    ```

    *   Top 10? Yes (`LIMIT 10`).
    *   Last 6 months? Yes (`INTERVAL '6 months'`).
    *   Columns correct? Yes.
    *   Order by revenue DESC? Yes.
    *   At least 3 completed orders? Yes (`HAVING COUNT >= 3`).Para resolver esta consulta, lo más limpio es utilizar **CTEs (Common Table Expressions)** para separar la lógica: primero calculamos las métricas generales del cliente y luego identificamos cuál es su categoría favorita, para finalmente unirlo todo.

Aquí tienes la query (escrita en compatible con PostgreSQL/Standard SQL):

```sql
WITH customer_stats AS (
    -- 1. Calculamos métricas básicas y filtramos clientes
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
category_counts AS (
    -- 2. Identificamos la categoría más comprada por cada cliente
    SELECT 
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id ORDER BY COUNT(*) DESC) as rank
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- 3. Unimos todo y obtenemos el Top 10
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    cc.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN category_counts cc ON cs.id = cc.customer_id AND cc.rank = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:

1.  **`customer_stats`**:
    *   Filtra las órdenes por estado `completed`.
    *   Filtra el tiempo (últimos 6 meses).
    *   Agrupa por cliente para sumar el revenue, contar órdenes y sacar el promedio.
    *   Usa `HAVING COUNT(o.id) >= 3` para cumplir con el requisito mínimo de órdenes.
2.  **`category_counts`**:
    *   Hace un `join` entre `orders`, `order_items` y `products` para saber qué compró cada cliente.
    *   Usa la función de ventana `ROW_NUMBER()` para asignar el número 1 a la categoría que más veces aparece para cada cliente (`COUNT(*) DESC`).
3.  **Select Final**:
    *   Une las métricas del cliente con el ranking de categorías.
    *   Filtra por `cc.rank = 1` para traer solo la categoría principal.
    *   Ordena por ingresos de mayor a menor y limita a los 10 primeros.

**