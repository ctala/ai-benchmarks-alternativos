# Nemotron 3 Super — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 128.572s | tokens_per_second: 22.7
- input_tokens: 160 | output_tokens: 2914
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

Aquí tienes una consulta SQL usando **CTEs** (tablas temporales con `WITH`). Está escrita en sintaxis estándar (funciona en PostgreSQL, MySQL 8+, SQL Server con pequeños ajustes en el intervalo de fechas).

```sql
WITH recent_orders AS (
    -- Órdenes completadas en los últimos 6 meses (relativo a la fecha más reciente)
    SELECT id, customer_id
    FROM orders
    WHERE status = 'completed'
      AND created_at >= (
          SELECT MAX(created_at) FROM orders
      ) - INTERVAL '6 months'
),
customer_agg AS (
    -- Métricas por cliente: cantidad de órdenes y revenue total
    SELECT 
        ro.customer_id,
        COUNT(*) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    GROUP BY ro.customer_id
    HAVING COUNT(*) >= 3
),
customer_category AS (
    -- Categoría más comprada por cliente (por cantidad de unidades)
    SELECT 
        ro.customer_id,
        p.category,
        SUM(oi.quantity) AS qty,
        ROW_NUMBER() OVER (
            PARTITION BY ro.customer_id 
            ORDER BY SUM(oi.quantity) DESC, p.category
        ) AS rn
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY ro.customer_id, p.category
)
SELECT 
    c.name        AS nombre,
    c.email       AS email,
    c.country     AS pais,
    ca.total_orders,
    ca.total_revenue,
    ROUND(ca.total_revenue / ca.total_orders, 2) AS avg_order_value,
    cc.category   AS categoria_mas_comprada
FROM customer_agg ca
JOIN customers c ON c.id = ca.customer_id
JOIN customer_category cc 
    ON cc.customer_id = ca.customer_id 
   AND cc.rn = 1
ORDER BY ca.total_revenue DESC
LIMIT 10;
```

### Explicación paso a paso

1. **`recent_orders`**: Filtra solo órdenes con `status = 'completed'` creadas en los últimos 6 meses. La ventana de tiempo se calcula dinámicamente respecto a la `MAX(created_at)` de la tabla `orders`, así no depende de la fecha actual del servidor.
2. **`customer_agg`**: Agrupa por cliente y calcula:
   - `total_orders`: número de órdenes válidas.
   - `total_revenue`: suma de `quantity × unit_price` de todos los ítems de esas órdenes.
   - `HAVING COUNT(*) >= 3`: descarta clientes con menos de 3 órdenes.
3. **`customer_category`**: Para cada cliente, suma la cantidad comprada por categoría y usa `ROW_NUMBER()` para quedarse solo con la categoría que tenga más unidades (`rn = 1`). Si hay empate, desempata alfabéticamente por nombre de categoría.
4. **Consulta final**: Une clientes con sus métricas y su categoría top, calcula el `avg_order_value`, ordena por `total_revenue` descendente y limita a los 10 primeros.

### Notas por motor de base de datos

| Motor | Ajuste en el filtro de fecha |
|-------|------------------------------|
| **PostgreSQL** | `INTERVAL '6 months'` (tal cual) |
| **MySQL** | `INTERVAL 6 MONTH` (sin comillas simples) |
| **SQL Server** | `DATEADD(month, -6, (SELECT MAX(created_at) FROM orders))` |
| **SQLite** | `date((SELECT MAX(created_at) FROM orders), '-6 months')` |

Si prefieres usar el campo `total` de la tabla `orders` en lugar de recalcularlo desde `order_items`, reemplaza `SUM(oi.quantity * oi.unit_price)` por `SUM(o.total)` y haz el join directamente con `orders`.