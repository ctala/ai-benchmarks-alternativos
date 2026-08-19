# KAT Coder Air v2.5 — code_generation/sql_query_complex

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.23 | quality: 9.8
- latency_total: 4.838s | tokens_per_second: 184.0
- input_tokens: 161 | output_tokens: 890
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada y detallada que cumple con los requisitos especificados.

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



Aquí tienes la query SQL:

```sql
WITH ordenes_recientes AS (
    -- Órdenes completadas en los últimos 6 meses
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total AS order_total,
        oi.product_id,
        oi.quantity,
        p.category
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),
metricas_cliente AS (
    -- Métricas agregadas por cliente
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT o.order_id) AS total_orders,
        SUM(o.order_total) AS total_revenue,
        AVG(o.order_total) AS avg_order_value
    FROM ordenes_recientes o
    JOIN customers c ON o.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT o.order_id) >= 3
),
categoria_top AS (
    -- Categoría más comprada por cliente (más unidades)
    SELECT 
        customer_id,
        category AS categoria_mas_comprada,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY SUM(quantity) DESC
        ) AS rn
    FROM ordenes_recientes
    GROUP BY customer_id, category
)
SELECT 
    m.name,
    m.email,
    m.country,
    m.total_orders,
    m.total_revenue,
    ROUND(m.avg_order_value, 2) AS avg_order_value,
    c.categoria_mas_comprada
FROM metricas_cliente m
LEFT JOIN categoria_top c ON m.customer_id = c.customer_id AND c.rn = 1
ORDER BY m.total_revenue DESC
LIMIT 10;
```

## Explicación:

| CTE | Propósito |
|-----|-----------|
| `ordenes_recientes` | Une órdenes, items y productos, filtrando por estado 'completed' y últimos 6 meses |
| `metricas_cliente` | Agrupa por cliente calculando total_orders, total_revenue y avg_order_value, con HAVING >= 3 órdenes |
| `categoria_top` | Usa `ROW_NUMBER()` para obtener la categoría con más unidades compradas por cada cliente |

## Notas:
- **`ROUND(avg_order_value, 2)`** redondea a 2 decimales para mejor legibilidad
- **`LEFT JOIN`** en `categoria_top` asegura que no se pierdan clientes si no tienen items
- **`ROW_NUMBER()`** permite obtener la categoría #1 por cliente eficientemente
- La fecha se calcula dinámicamente con `CURRENT_DATE - INTERVAL '6 months'`

Si usas **MySQL**, cambia `CURRENT_DATE - INTERVAL '6 months'` por `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` y `ROUND()` funciona igual.