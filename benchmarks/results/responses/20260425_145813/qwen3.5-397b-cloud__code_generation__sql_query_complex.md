# Qwen 3.5 397B (Ollama Cloud) — code_generation/sql_query_complex

- model_id: `qwen3.5:397b-cloud`
- success: True  | final: 8.15 | quality: 9.72
- latency_total: 78.365s | tokens_per_second: 54.5
- input_tokens: 161 | output_tokens: 4274
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes la consulta SQL optimizada utilizando **CTEs (Common Table Expressions)** para mantener la legibilidad y el rendimiento.

Esta consulta está escrita en **SQL Estándar (compatible con PostgreSQL y MySQL 8.0+)**.

```sql
WITH orders_last_6_months AS (
    -- 1. Filtramos las órdenes completadas de los últimos 6 meses
    SELECT 
        id, 
        customer_id, 
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL '6 months'
),
customer_metrics AS (
    -- 2. Calculamos las métricas por cliente (órdenes y revenue)
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue
    FROM customers c
    JOIN orders_last_6_months o ON c.id = o.customer_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3  -- Solo clientes con al menos 3 órdenes
),
category_ranking AS (
    -- 3. Determinamos la categoría más comprada por cada cliente
    SELECT 
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders_last_6_months o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
)
-- 4. Unimos todo y seleccionamos los Top 10
SELECT 
    cm.name AS nombre,
    cm.email AS email,
    cm.country AS pais,
    cm.total_orders AS total_orders,
    cm.total_revenue AS total_revenue,
    (cm.total_revenue * 1.0 / cm.total_orders) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN category_ranking cr ON cm.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:

1.  **`orders_last_6_months`**: Filtra primero la tabla de órdenes para reducir el volumen de datos antes de hacer joins complejos. Se filtra por `status = 'completed'` y la fecha.
2.  **`customer_metrics`**: Agrupa por cliente para contar las órdenes y sumar el revenue total. La cláusula `HAVING` asegura que solo entren clientes con 3 o más compras.
3.  **`category_ranking`**: Esta es la parte más compleja.
    *   Une órdenes con items y productos.
    *   Agrupa por cliente y categoría sumando la cantidad (`quantity`).
    *   Usa una **Window Function** (`ROW_NUMBER`) para rankear las categorías de cada cliente de mayor a menor cantidad comprada.
4.  **SELECT Final**:
    *   Une las métricas del cliente con su categoría rankeada #1 (`rn = 1`).
    *   Calcula el `avg_order_value` (multiplico por `1.0` para asegurar que la división sea decimal y no entera).
    *   Ordena por revenue y limita a 10.

### Notas de compatibilidad:

*   **Fecha (Intervalo):**
    *   **PostgreSQL:** `NOW() - INTERVAL '6 months'` (Como está en el ejemplo).
    *   **MySQL:** `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
    *   **SQL Server:** `DATEADD(MONTH, -6, GETDATE())`.
*   **División Decimal:** En algunas bases de datos (como SQL Server o PostgreSQL con tipos enteros), dividir dos enteros trunca el resultado. Multiplicar por `1.0` o usar `CAST(... AS DECIMAL)` asegura que el `avg_order_value` tenga decimales.