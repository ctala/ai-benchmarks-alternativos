# Tencent Hy4 — code_generation/sql_query_complex

- model_id: `tencent/hy4`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 34.874s | tokens_per_second: 103.5
- input_tokens: 168 | output_tokens: 3609
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

Aquí tienes la query. Está escrita en **PostgreSQL / SQL estándar** (compatible también con MySQL 8+, Snowflake, BigQuery, etc., con un pequeño ajuste de fechas que indico al final).

```sql
WITH recent_orders AS (
    -- 1. Filtramos primero el periodo y el estatus
    SELECT id, customer_id, total
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_metrics AS (
    -- 2. Agregamos revenue SIN unir todavía con order_items (evita duplicar el total)
    SELECT 
        customer_id,
        COUNT(*)      AS total_orders,
        SUM(total)    AS total_revenue,
        AVG(total)    AS avg_order_value
    FROM recent_orders
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),
category_qty AS (
    -- 3. Sumamos unidades por categoría SOLO de las órdenes del periodo
    SELECT 
        ro.customer_id,
        p.category,
        SUM(oi.quantity) AS qty
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    JOIN products p     ON p.id = oi.product_id
    GROUP BY ro.customer_id, p.category
),
ranked_categories AS (
    -- 4. Rankeamos para quedarnos con la categoría top (con desempate alfabético)
    SELECT 
        customer_id,
        category AS categoria_mas_comprada,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY qty DESC, category ASC
        ) AS rn
    FROM category_qty
)
SELECT 
    c.name                  AS nombre,
    c.email,
    c.country               AS pais,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    rc.categoria_mas_comprada
FROM customer_metrics cm
JOIN customers c 
    ON c.id = cm.customer_id
LEFT JOIN ranked_categories rc 
    ON rc.customer_id = cm.customer_id 
   AND rc.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### 💡 Decisiones clave (y un error común que evitamos)

1. **El trampa del *Fan-out***: Si haces un `JOIN` directo entre `orders` y `order_items` y luego un `SUM(o.total)`, el revenue se multiplicará por la cantidad de ítems de cada orden (ej. una orden de $100 con 3 ítems sumaría $300). Por eso calculo `total_revenue` en un CTE aparte y solo uso `order_items` para la categoría.
2. **`categoria_mas_comprada`**: Se define por **unidades vendidas** (`SUM(quantity)`) en lugar de por número de filas, que suele ser la definición de negocio más precisa. Usé `ROW_NUMBER()` con un desempate alfabético (`category ASC`) para que el resultado sea determinista si un cliente compra exactamente la misma cantidad de dos categorías.
3. **`avg_order_value`**: `AVG(total)` es más seguro que `SUM(total)/COUNT(*)` porque evita problemas de división entera en algunos motores.
4. **Asunción sobre las 3 órdenes**: Asumí que las *"al menos 3 órdenes completadas"* también deben caer **dentro de los últimos 6 meses**. Si en realidad quisieras que el mínimo de 3 órdenes sea **histórico** (pero el revenue solo de 6 meses), habría que sacar el `HAVING` a un CTE sin el filtro de fecha y hacerle `JOIN` a `recent_orders`. Dime si es ese tu caso y te la ajusto.

### 🔧 Ajuste según tu base de datos

| Motor | Cambio en la fecha | Cambio en el límite |
| :--- | :--- | :--- |
| **PostgreSQL** | `CURRENT_DATE - INTERVAL '6 months'` ✅ | `LIMIT 10` ✅ |
| **MySQL 8+** | `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` | `LIMIT 10` ✅ |
| **SQL Server** | `DATEADD(MONTH, -6, GETDATE())` | `SELECT TOP 10 ...` (quitar `LIMIT`) |
| **BigQuery** | `DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)` | `LIMIT 10` ✅ |

> *Tip de performance*: Asegúrate de tener un índice compuesto en `orders(status, created_at, customer_id)` para que el primer CTE vuele. 🚀