# Qwen 3.6 Max — code_generation/sql_query_complex

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 8.08 | quality: 10.0
- latency_total: 100.138s | tokens_per_second: 42.2
- input_tokens: 161 | output_tokens: 4221
- judge_score: 5.0 | justificación: 

## Respuesta completa

Aquí tienes una query robusta, legible y compatible con la mayoría de motores SQL modernos (PostgreSQL, MySQL 8+, SQL Server, Oracle). Usa CTEs para separar la lógica y evitar cálculos duplicados.

```sql
WITH filtered_orders AS (
    -- 1. Filtramos solo órdenes completadas de los últimos 6 meses
    SELECT id, customer_id
    FROM orders
    WHERE status = 'completed'
      AND created_at >= CURRENT_DATE - INTERVAL '6 months'
),
customer_metrics AS (
    -- 2. Agregamos métricas principales por cliente
    SELECT 
        c.id AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(DISTINCT fo.id) AS total_orders,
        SUM(oi.quantity * oi.unit_price) AS total_revenue
    FROM customers c
    JOIN filtered_orders fo ON c.id = fo.customer_id
    JOIN order_items oi ON fo.id = oi.order_id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(DISTINCT fo.id) >= 3
),
category_ranking AS (
    -- 3. Rankeamos categorías por cantidad comprada por cliente
    SELECT 
        fo.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER (
            PARTITION BY fo.customer_id 
            ORDER BY SUM(oi.quantity) DESC
        ) as rn
    FROM filtered_orders fo
    JOIN order_items oi ON fo.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    GROUP BY fo.customer_id, p.category
)
-- 4. Resultado final
SELECT 
    cm.name,
    cm.email,
    cm.country,
    cm.total_orders,
    ROUND(cm.total_revenue, 2) AS total_revenue,
    ROUND(cm.total_revenue / cm.total_orders, 2) AS avg_order_value,
    cr.category AS categoria_mas_comprada
FROM customer_metrics cm
LEFT JOIN category_ranking cr 
    ON cm.customer_id = cr.customer_id AND cr.rn = 1
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### 🔍 Puntos clave de la query:
1. **`filtered_orders`**: Centraliza el filtro de fecha y estado. Evita repetir lógica y mejora el plan de ejecución.
2. **`COUNT(DISTINCT fo.id)`**: Necesario porque al hacer `JOIN` con `order_items` cada orden se multiplica por sus ítems. El `DISTINCT` garantiza que contamos órdenes, no líneas de detalle.
3. **`categoria_mas_comprada`**: Se calcula con `ROW_NUMBER()` particionado por cliente. En caso de empate, se elige una arbitrariamente. Si necesitas desempatar (ej. por revenue o alfabéticamente), avísame y ajusto el `ORDER BY` dentro de la ventana.
4. **`unit_price` vs `products.price`**: Se usa `order_items.unit_price` porque refleja el precio real al momento de la compra (histórico), no el precio actual del catálogo.

### ⚙️ Notas de compatibilidad por motor:
| Elemento | PostgreSQL / MySQL 8+ | SQL Server | Oracle |
|----------|----------------------|------------|--------|
| Últimos 6 meses | `CURRENT_DATE - INTERVAL '6 months'` | `DATEADD(month, -6, GETDATE())` | `ADD_MONTHS(SYSDATE, -6)` |
| Limitar a 10 | `LIMIT 10` | `SELECT TOP 10 ...` (al inicio) | `FETCH FIRST 10 ROWS ONLY` (al final) |
| Funciones ventana | ✅ Soportadas | ✅ Soportadas | ✅ Soportadas |

Si me indicas tu motor de base de datos exacto, te devuelvo la versión 100% ajustada a su sintaxis. ¿Necesitas también un índice recomendado para optimizar esta consulta?