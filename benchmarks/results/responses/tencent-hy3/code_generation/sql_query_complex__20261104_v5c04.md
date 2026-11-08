# Tencent Hy3 — code_generation/sql_query_complex

- model_id: `tencent/hy3`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 67.636s | tokens_per_second: 72.4
- input_tokens: 163 | output_tokens: 4899
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

Aquí tienes una query SQL (usando CTEs y funciones de ventana para mayor claridad y eficiencia) que cumple con todos tus requisitos. 

Está escrita con una sintaxis estándar tipo PostgreSQL, pero incluyo una nota para MySQL.

```sql
WITH orders_last_6m AS (
    -- 1. Filtramos solo órdenes completadas de los últimos 6 meses
    SELECT 
        id AS order_id,
        customer_id,
        total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= NOW() - INTERVAL '6 months' 
      -- Nota para MySQL: usa created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
),
customer_metrics AS (
    -- 2. Calculamos las métricas por cliente y filtramos los que tienen >= 3 órdenes
    SELECT 
        o.customer_id,
        COUNT(o.order_id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM orders_last_6m o
    GROUP BY o.customer_id
    HAVING COUNT(o.order_id) >= 3
),
customer_top_category AS (
    -- 3. Determinamos la categoría más comprada por cada cliente
    SELECT 
        o.customer_id,
        p.category,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC -- Ordenamos por revenue de la categoría
            -- (Si "más comprada" se refiere a cantidad de productos, usa: ORDER BY SUM(oi.quantity) DESC)
        ) AS rn
    FROM orders_last_6m o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY o.customer_id, p.category
)
-- 4. Query final: unimos todo y limitamos a los top 10
SELECT 
    c.name AS nombre,
    c.email AS email,
    c.country AS pais,
    cm.total_orders,
    ROUND(cm.total_revenue, 2) AS total_revenue,
    ROUND(cm.avg_order_value, 2) AS avg_order_value,
    ctc.category AS categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c ON cm.customer_id = c.id
JOIN customer_top_category ctc ON cm.customer_id = ctc.customer_id AND ctc.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación de la lógica:
1. **`orders_last_6m`**: Aísla el universo de datos a solo las órdenes `completed` de los últimos 6 meses. Esto asegura que tanto el revenue como el conteo de órdenes respeten ese rango.
2. **`customer_metrics`**: Agrupa por cliente, suma el revenue total, saca el promedio y cuenta las órdenes. El `HAVING COUNT >= 3` garantiza la restricción de mínimo de 3 órdenes.
3. **`customer_top_category`**: Cruza con `order_items` y `products` para sumar el valor (o cantidad) por categoría por cada cliente. Usamos `ROW_NUMBER()` para rankear las categorías y quedarnos solo con la #1 (`rn = 1`).
4. **Query principal**: Hacemos `JOIN` con la tabla `customers` para traer nombre, email y país, y ordenamos por revenue descendente para quedarnos con el Top 10.

*Nota: Si tu motor de base de datos es MySQL 5.x (que no soporta CTEs con `WITH`), puedo convertirla a subqueries anidados, aunque te recomiendo fuertemente usar esta versión si tienes MySQL 8+ o PostgreSQL.*