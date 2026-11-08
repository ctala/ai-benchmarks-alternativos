# Gemma 4 26B MoE (3.8B activos) — code_generation/sql_query_complex

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 9.12 | quality: 10.0
- latency_total: 12.3s | tokens_per_second: 74.2
- input_tokens: 173 | output_tokens: 913
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

Para resolver este problema, necesitamos realizar varias uniones (JOINs) y utilizar una **Common Table Expression (CTE)** o una subconsulta para calcular la categoría más comprada de forma independiente, ya que es una métrica de agregación distinta a las sumas de dinero.

Aquí tienes la query optimizada para PostgreSQL/Standard SQL:

```sql
WITH customer_stats AS (
    -- Paso 1: Calcular métricas básicas de ventas por cliente
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
customer_top_category AS (
    -- Paso 2: Identificar la categoría más comprada por cliente usando una Window Function
    SELECT 
        customer_id,
        category,
        RANK() OVER (PARTITION BY customer_id ORDER BY SUM(oi.quantity) DESC) as rank_cat
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- Paso 3: Unir todo y obtener el Top 10
SELECT 
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.avg_order_value, 2) AS avg_order_value,
    ctc.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN customer_top_category ctc ON cs.customer_id = ctc.customer_id AND ctc.rank_cat = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación técnica:

1.  **`customer_stats` (CTE 1):**
    *   Filtra las órdenes por `status = 'completed'` y el rango de tiempo de los últimos 6 meses.
    *   Utiliza `HAVING COUNT(o.id) >= 3` para cumplir con el requisito de clientes recurrentes.
    *   Calcula el total de órdenes, el revenue y el promedio por cliente.

2.  **`customer_top_category` (CTE 2):**
    *   Este es el paso más complejo. No podemos simplemente agrupar por categoría en la query principal porque colapsaría las filas de los clientes.
    *   Usamos `RANK() OVER (PARTITION BY customer_id ORDER BY SUM(oi.quantity) DESC)` para enumerar las categorías de cada cliente según la cantidad de productos comprados. La categoría con `rank = 1` es la más popular.

3.  **Query Principal:**
    *   Une las estadísticas de los clientes con la categoría ganadora (donde el rango es 1).
    *   Usa `LEFT JOIN` por seguridad, por si algún cliente no tuviera items asociados (aunque es improbable por la lógica de negocio).
    *   Aplica el `ORDER BY total_revenue DESC` y el `LIMIT 10` para obtener el ranking solicitado.

**Nota sobre compatibilidad:**
*   Si usas **MySQL**, cambia `CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(NOW(), INTERVAL 6 MONTH)`.
*   Si usas **SQL Server**, cambia la sintaxis de fecha por `DATEADD(month, -6, GETDATE())`.