# Inkling Small — code_generation/sql_query_complex

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 7.73 | quality: 9.34
- latency_total: 300.47s | tokens_per_second: 19.7
- input_tokens: 155 | output_tokens: 5905

## Respuesta completa

Aquí tienes la query. Usa **CTEs** para evitar duplicados al unir con `order_items`, y una **función de ventana** (`ROW_NUMBER`) para elegir la categoría más comprada por cliente.

> **Nota sobre la fecha:** La sintaxis `CURRENT_DATE - INTERVAL '6 months'` es para PostgreSQL. Si usas **MySQL**, cambia esa línea por `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)`. Si usas **SQL Server**, usa `o.created_at >= DATEADD(month, -6, CAST(GETDATE() AS DATE))` y reemplaza `LIMIT 10` por `TOP 10` al inicio del `SELECT`.

```sql
WITH orders_6m AS (
    /* 1. Órdenes completadas en los últimos 6 meses */
    SELECT 
        o.id AS order_id,
        o.customer_id,
        o.total
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'  -- Ajusta según tu DB
),

client_stats AS (
    /* 2. Métricas por cliente (solo los que tengan >= 3 órdenes) */
    SELECT 
        customer_id,
        COUNT(*) AS total_orders,
        SUM(total) AS total_revenue,
        AVG(total) AS avg_order_value
    FROM orders_6m
    GROUP BY customer_id
    HAVING COUNT(*) >= 3
),

category_sales AS (
    /* 3. Cantidad (o valor) comprada por categoría en ese período */
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS qty_bought
        -- Si prefieres por valor: SUM(oi.quantity * oi.unit_price) AS rev_cat
    FROM orders_6m o
    JOIN order_items oi ON oi.order_id = o.order_id
    JOIN products p    ON p.id = oi.product_id
    GROUP BY o.customer_id, p.category
),

ranked_categories AS (
    /* 4. Elegir la categoría más comprada por cliente */
    SELECT 
        customer_id,
        category AS categoria_mas_comprada,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id 
            ORDER BY qty_bought DESC, category ASC
        ) AS rn
    FROM category_sales
)

/* 5. Resultado final */
SELECT 
    c.name,
    c.email,
    c.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    rc.categoria_mas_comprada
FROM client_stats cs
JOIN customers c ON c.id = cs.customer_id
LEFT JOIN ranked_categories rc 
    ON rc.customer_id = cs.customer_id 
    AND rc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### ¿Qué hace paso a paso?

| Paso | Descripción |
|------|-------------|
| `orders_6m` | Filtra solo órdenes `completed` de los últimos 6 meses. |
| `client_stats` | Agrupa por cliente, suma revenue, cuenta órdenes y aplica `HAVING COUNT(*) >= 3`. |
| `category_sales` | Une con `order_items` + `products` para sumar cantidad por categoría **solo de esas órdenes**. |
| `ranked_categories` | Usa `ROW_NUMBER()` para quedarse con la #1 por cliente. |
| `SELECT final` | Une con `customers`, ordena por revenue y limita a 10. |

### Variaciones rápidas:
- **Categoría por valor (dinero)**: en `category_sales` cambia `SUM(oi.quantity)` por `SUM(oi.quantity * oi.unit_price)`.
- **Filtro global de 3 órdenes** (si quisieras contar todas las `completed` de la historia, no solo las últimas 6): crea un CTE adicional `all_completed` con `COUNT(*)` global y haz `JOIN` con `client_stats`; luego calcula `total_revenue` solo sobre `orders_6m`.