# Qwen 3.6 35B base (OpenRouter FP8) — code_generation/sql_query_complex

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 74.928s | tokens_per_second: 71.9
- input_tokens: 161 | output_tokens: 5385
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



Aquí tienes la query optimizada. Utiliza **CTEs** para separar la lógica de agregación de clientes y la de categorías, evitando así el duplicado de revenue por tener múltiples items por orden.

```sql
WITH customer_stats AS (
    -- 1. Agregamos métricas por cliente (solo órdenes completadas en últimos 6 meses)
    SELECT 
        c.id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue
    FROM orders o
    JOIN customers c ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6' MONTH
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
top_categories AS (
    -- 2. Calculamos la categoría más comprada por cliente (basado en cantidad total)
    SELECT 
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_qty,
        ROW_NUMBER() OVER(PARTITION BY o.customer_id ORDER BY SUM(oi.quantity) DESC) as rn
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6' MONTH
    GROUP BY o.customer_id, p.category
)
-- 3. Unimos ambas lógicas y aplicamos filtros finales
SELECT 
    cs.nombre,
    cs.email,
    cs.pais,
    cs.total_orders,
    cs.total_revenue,
    ROUND(cs.total_revenue / cs.total_orders, 2) AS avg_order_value,
    tc.category AS categoria_mas_comprada
FROM customer_stats cs
LEFT JOIN top_categories tc 
    ON cs.id = tc.customer_id AND tc.rn = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### 🔍 Notas importantes:
1. **Compatibilidad de fechas**: 
   - `CURRENT_DATE - INTERVAL '6' MONTH` funciona en **PostgreSQL**.
   - En **MySQL** cámbialo por: `o.created_at >= DATE_SUB(CURRENT_DATE, INTERVAL 6 MONTH)`
   - En **SQL Server**: `o.created_at >= DATEADD(month, -6, CAST(GETDATE() AS DATE))`
2. **`categoria_mas_comprada`**: Se calcula sumando `quantity` por categoría. Si prefieres que sea por **ingresos** (`SUM(quantity * unit_price)`) o por **número de líneas** (`COUNT(*)`), solo cambia la columna dentro del `SUM()` o `COUNT()` en el CTE `top_categories`.
3. **`ROW_NUMBER()` vs `RANK()`**: `ROW_NUMBER()` elige una categoría aleatoria en caso de empate. Si quieres mostrar **todas** las categorías empatadas al top, reemplaza `ROW_NUMBER()` por `RANK()`.
4. **`avg_order_value`**: Se calcula como `total_revenue / total_orders`. El `HAVING COUNT(o.id) >= 3` garantiza que no haya división por cero.

¿Necesitas que ajuste algo según tu motor de base de datos o la lógica de "más comprada"?