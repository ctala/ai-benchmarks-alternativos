# Qwen 3.5 397B — code_generation/sql_query_complex

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.38 | quality: 10.0
- latency_total: 79.291s | tokens_per_second: 64.2
- input_tokens: 161 | output_tokens: 5087
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL optimizada utilizando **CTEs (Common Table Expressions)** para mantener la lógica organizada. Esta consulta es compatible con motores modernos como **PostgreSQL** o **MySQL 8.0+**.

```sql
WITH CustomerOrderStats AS (
    -- 1. Calcular métricas principales por cliente (órdenes y revenue)
    -- Filtramos por estado y fecha aquí para asegurar consistencia
    SELECT
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months' -- Nota: Ver sintaxis de fecha abajo*
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
CategoryStats AS (
    -- 2. Calcular cantidad de productos comprados por categoría por cliente
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
),
RankedCategories AS (
    -- 3. Rankear las categorías para cada cliente y quedarse con la #1
    SELECT
        customer_id,
        category,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC) AS rn
    FROM CategoryStats
)
-- 4. Unir las métricas del cliente con su categoría más comprada
SELECT
    cos.name AS nombre,
    cos.email AS email,
    cos.country AS pais,
    cos.total_orders AS total_orders,
    cos.total_revenue AS total_revenue,
    CAST(cos.total_revenue AS DECIMAL(10,2)) / cos.total_orders AS avg_order_value,
    rc.category AS categoria_mas_comprada
FROM CustomerOrderStats cos
INNER JOIN RankedCategories rc ON cos.customer_id = rc.customer_id AND rc.rn = 1
ORDER BY cos.total_revenue DESC
LIMIT 10;
```

### Notas importantes sobre la consulta:

1.  **Sintaxis de Fecha:**
    *   La línea `o.created_at >= NOW() - INTERVAL '6 months'` es estándar en **PostgreSQL**.
    *   Si usas **MySQL**, cámbiala por: `o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
2.  **Cálculo de Revenue:** Se utiliza la columna `orders.total` asumiendo que refleja el monto final de la transacción. Si necesitaras calcularlo desde los ítems, deberías usar `SUM(oi.quantity * oi.unit_price)` en el primer CTE.
3.  **Categoría Más Comprada:** Se determina mediante la **cantidad total de ítems** (`SUM(oi.quantity)`). Si hubiera un empate en cantidades, `ROW_NUMBER` seleccionará una arbitrariamente.
4.  **Filtros:**
    *   El filtro de `status = 'completed'` y la ventana de `6 meses` se aplican en ambos CTEs principales para asegurar que la categoría más comprada corresponda a las mismas órdenes que generan el revenue.
    *   El filtro de `>= 3 ordenes` se aplica en el primer CTE (`CustomerOrderStats`) antes del join final.
5.  **Avg Order Value:** Se hace un `CAST` a `DECIMAL` para asegurar que la división devuelva decimales y no un entero truncado (dependiendo de la configuración de tu base de datos).