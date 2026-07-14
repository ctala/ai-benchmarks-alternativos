# MiniMax M2.5 — code_generation/sql_query_complex

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.58 | quality: 9.56
- latency_total: 12.357s | tokens_per_second: 80.7
- input_tokens: 181 | output_tokens: 997
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL completa y bien estructurada que cumple con los requisitos especificados.

## Respuesta completa

# Query SQL para Top 10 Clientes por Revenue

Aquí tienes la consulta completa:

```sql
WITH customer_metrics AS (
    -- Métricas básicas del cliente
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue,
        AVG(o.total) AS avg_order_value
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
),
category_purchases AS (
    -- Cantidad comprada por categoría por cliente
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)
-- Query final
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    cm.total_revenue,
    cm.avg_order_value,
    cp.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN category_purchaseS cp 
    ON cm.customer_id = cp.customer_id 
    AND cp.rn = 1
WHERE cm.total_orders >= 3
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

## Explicación de las partes

| Parte | Descripción |
|-------|-------------|
| **customer_metrics** | Calcula total_orders, total_revenue y avg_order_value por cliente |
| **category_purchases** | Determina la categoría más comprada usando ROW_NUMBER() |
| **Filtros** | `status = 'completed'` y últimos 6 meses |
| **WHERE final** | Excluye clientes con menos de 3 órdenes |

## Notas

- **Según tu esquema**, `orders.total` ya contiene el total de la orden
- **Si prefieres calcular desde order_items**, cambia el `SUM(o.total)` por:
  ```sql
  SUM(oi.quantity * oi.unit_price) AS total_revenue
  ```
- **Compatible con** PostgreSQL. Para MySQL, cambia:
  - `INTERVAL '6 months'` → `INTERVAL 6 MONTH`
  - `CURRENT_DATE` → `CURDATE()`