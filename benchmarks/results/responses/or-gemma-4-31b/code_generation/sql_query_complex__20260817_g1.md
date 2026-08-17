# Gemma 4 31B — code_generation/sql_query_complex

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 15.22s | tokens_per_second: 54.6
- input_tokens: 173 | output_tokens: 831
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

Para lograr esto, necesitamos combinar varias tablas y utilizar una **Subquery** o un **CTE (Common Table Expression)** para determinar la categoría más comprada por cada cliente, ya que es un cálculo independiente al de las sumas totales.

Aquí tienes la query optimizada:

```sql
WITH CustomerStats AS (
    -- Calculamos los totales y filtramos por fecha y status
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
MostBoughtCategory AS (
    -- Determinamos la categoría más comprada por cada cliente
    SELECT DISTINCT ON (o.customer_id)
        o.customer_id,
        p.category
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id, p.category
    ORDER BY o.customer_id, COUNT(oi.id) DESC
)
SELECT 
    cs.name, 
    cs.email, 
    cs.country, 
    cs.total_orders, 
    cs.total_revenue, 
    cs.avg_order_value, 
    mbc.category AS categoria_mas_comprada
FROM CustomerStats cs
JOIN MostBoughtCategory mbc ON cs.id = mbc.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación técnica de la solución:

1.  **`CustomerStats` (CTE):** 
    *   Filtramos las órdenes por `status = 'completed'` y la fecha (últimos 6 meses).
    *   Usamos `GROUP BY` para agrupar por cliente.
    *   Aplicamos el filtro `HAVING COUNT(o.id) >= 3` para asegurar que solo entren clientes con al menos 3 órdenes.
2.  **`MostBoughtCategory` (CTE):** 
    *   Aquí hacemos un join entre órdenes, ítems y productos.
    *   Utilizo `DISTINCT ON (o.customer_id)` (Sintaxis de PostgreSQL) junto con `ORDER BY COUNT(...) DESC`. Esto selecciona únicamente la fila con la categoría que tiene la mayor cantidad de productos comprados por ese cliente. 
    *   *Nota: Si usas MySQL, podrías reemplazar esto con una subquery usando `RANK()` o `ROW_NUMBER()`.*
3.  **Query Final:** 
    *   Unimos ambos resultados mediante el `customer_id`.
    *   Ordenamos por `total_revenue DESC` y limitamos a los 10 primeros.

### Consideraciones según tu motor de base de datos:
*   **PostgreSQL:** La query funcionará tal cual.
*   **MySQL:** Cambia `CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(NOW(), INTERVAL 6 MONTH)` y, dado que MySQL no tiene `DISTINCT ON`, deberías usar una Window Function (`ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY count DESC)`) para obtener la categoría más comprada.