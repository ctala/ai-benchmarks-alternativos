# Kimi K2.6 — code_generation/sql_query_complex

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.19 | quality: 9.8
- latency_total: 66.918s | tokens_per_second: 59.8
- input_tokens: 159 | output_tokens: 4003
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

 Aquí tienes la query usando **CTEs** para mantenerla limpia y modular. Está escrita en **SQL estándar (PostgreSQL-compatible)**; al final te dejo las adaptaciones para MySQL/SQL Server si las necesitas.

```sql
WITH recent_completed_orders AS (
    /* 1. Filtrar órdenes completadas de los últimos 6 meses */
    SELECT 
        o.id AS order_id,
        o.customer_id
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_stats AS (
    /* 2. Métricas por cliente: órdenes, revenue y AOV */
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT rco.order_id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM recent_completed_orders rco
    JOIN customers c ON rco.customer_id = c.id
    JOIN order_items oi ON rco.order_id = oi.order_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT rco.order_id) >= 3
),
category_ranking AS (
    /* 3. Categoría más comprada por cliente (por cantidad total) */
    SELECT 
        c.id AS customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY c.id 
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn
    FROM customers c
    JOIN recent_completed_orders rco ON c.id = rco.customer_id
    JOIN order_items oi ON rco.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY c.id, p.category
)
/* 4. Resultado final: unir métricas con la categoría #1 */
SELECT 
    cs.name,
    cs.email,
    cs.country AS pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.total_revenue / cs.total_orders, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_stats cs
JOIN category_ranking cr 
    ON cs.customer_id = cr.customer_id 
    AND cr.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación paso a paso

| CTE | Qué hace |
|-----|----------|
| `recent_completed_orders` | Filtra solo órdenes `completed` creadas en los últimos 6 meses. |
| `customer_stats` | Calcula `total_orders`, `total_revenue` (sumando `quantity * unit_price`) y aplica el `HAVING >= 3` para descartar clientes con menos de 3 órdenes. |
| `category_ranking` | Suma la cantidad comprada por categoría y asigna un ranking (`ROW_NUMBER`) por cliente. El `ORDER BY ... p.category ASC` sirve como desempate determinista. |
| SELECT final | Une las métricas con la categoría ganadora (`rn = 1`), calcula el AOV y ordena por revenue descendente. |

### Notas para otros motores SQL

- **MySQL / MariaDB**: Cambia el filtro de fecha a  
  `AND o.created_at >= DATE_SUB(NOW(), INTERVAL 6 MONTH)`  
  (MySQL 8.0+ soporta CTEs y window functions).
- **SQL Server**: Cambia el filtro de fecha a  
  `AND o.created_at >= DATEADD(MONTH, -6, GETDATE())`  
  y usa `TOP 10` en lugar de `LIMIT 10`.
- **SQLite**: No soporta `INTERVAL` directamente; usa `DATE('now', '-6 months')`.

### Variante opcional
Si prefieres que **"categoría más comprada"** se mida por **revenue** en vez de por cantidad de unidades, solo cambia el `ORDER BY` dentro del `ROW_NUMBER()` de `category_ranking`:

```sql
ORDER BY SUM(oi.quantity * oi.unit_price) DESC, p.category ASC
```