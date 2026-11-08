# Gemma 4 31B — code_generation/sql_query_complex

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 9.869s | tokens_per_second: 82.3
- input_tokens: 173 | output_tokens: 812
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

Para lograr este resultado, necesitamos combinar varias tablas y utilizar una **subconsulta** o un **CTE (Common Table Expression)** para determinar la categoría más comprada por cada cliente, ya que es un cálculo agregado diferente al del revenue.

Aquí tienes la query optimizada:

```sql
WITH CustomerStats AS (
    -- Calculamos las métricas principales de ventas
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
    -- Determinamos la categoría más comprada por cliente
    SELECT 
        o.customer_id,
        p.category,
        COUNT(*) as product_count,
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
JOIN CategoryRanking cr ON cs.customer_id = cr.customer_id
WHERE cr.rank = 1 -- Solo nos quedamos con la categoría top de cada cliente
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación de la solución:

1.  **`CustomerStats` (CTE):** 
    *   Filtra las órdenes por estado `'completed'` y el rango de tiempo (últimos 6 meses).
    *   Calcula el conteo de órdenes, la suma del revenue y el promedio.
    *   Aplica el filtro `HAVING COUNT(o.id) >= 3` para asegurar que solo entren clientes con al menos 3 compras.
2.  **`CategoryRanking` (CTE):**
    *   Une las órdenes con los productos para contar cuántas veces aparece cada categoría por cliente.
    *   Utiliza la función de ventana `ROW_NUMBER()`. Esta asigna el número `1` a la categoría que más veces se repite para cada cliente (`PARTITION BY o.customer_id ORDER BY COUNT(*) DESC`).
3.  **Query Final:**
    *   Une ambos bloques de datos.
    *   Filtra `cr.rank = 1` para obtener únicamente la categoría más comprada.
    *   Ordena por el revenue total de forma descendente y limita el resultado a los 10 primeros.

**Nota sobre compatibilidad:** He utilizado `CURRENT_DATE - INTERVAL '6 months'`, que es estándar en **PostgreSQL**. Si usas **MySQL**, deberías cambiar esa línea por `o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)`.