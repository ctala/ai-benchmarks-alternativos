# Qwen 3.5 35B — code_generation/sql_query_complex

- model_id: `qwen/qwen3.5-35b-a3b`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 22.122s | tokens_per_second: 191.5
- input_tokens: 161 | output_tokens: 4237
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

Aquí tienes la consulta SQL utilizando **PostgreSQL** como referencia principal (debido a su manejo robusto de ventanas y fechas), aunque es fácilmente adaptable a otros motores como MySQL ajustando la sintaxis de las fechas.

La estrategia se divide en dos partes usando **CTEs (Common Table Expressions)** para mantener el código legible:
1.  **`customer_metrics`**: Calcula los KPIs básicos (órdenes, ingresos) filtrando por estado y tiempo.
2.  **`category_analysis`**: Determina cuál es la categoría favorita de cada cliente usando funciones de ventana (`ROW_NUMBER`).

```sql
WITH customer_metrics AS (
    -- 1. Agregar métricas base por cliente (últimos 6 meses, status 'completed')
    SELECT
        c.id AS customer_id,
        c.name AS nombre,
        c.email,
        c.country AS pais,
        COUNT(o.id) AS total_orders,
        SUM(o.total) AS total_revenue
    FROM customers c
    INNER JOIN orders o ON c.id = o.customer_id
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 MONTH'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
),
category_analysis AS (
    -- 2. Calcular la categoría más comprada por cliente (basado en valor monetario)
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity * oi.unit_price) AS category_revenue,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id 
            ORDER BY SUM(oi.quantity * oi.unit_price) DESC
        ) as rn
    FROM orders o
    INNER JOIN order_items oi ON o.id = oi.order_id
    INNER JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
      AND o.created_at >= NOW() - INTERVAL '6 MONTH'
    GROUP BY o.customer_id, p.category
)
-- 3. Unir resultados finales
SELECT
    cm.nombre,
    cm.email,
    cm.pais,
    cm.total_orders,
    cm.total_revenue,
    ROUND((cm.total_revenue::NUMERIC / NULLIF(cm.total_orders, 0)), 2) AS avg_order_value,
    ca.category AS categoria_mas_comprada
FROM customer_metrics cm
INNER JOIN category_analysis ca 
    ON cm.customer_id = ca.customer_id 
    AND ca.rn = 1  -- Tomar solo la primera categoría (la que tiene rn = 1)
ORDER BY cm.total_revenue DESC
LIMIT 10;
```

### Explicación de los componentes clave:

1.  **Filtro de Tiempo y Estado**:
    *   `o.created_at >= NOW() - INTERVAL '6 MONTH'`: Limita el análisis a los últimos 6 meses.
    *   `o.status = 'completed'`: Solo cuenta órdenes finalizadas exitosamente.
2.  **Filtro de Clientes Activos**:
    *   `HAVING COUNT(o.id) >= 3`: En la CTE `customer_metrics`, descartamos clientes con menos de 3 órdenes completadas en este periodo.
3.  **Categoría Principal (`ROW_NUMBER`)**:
    *   Usamos `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ... DESC)` dentro de `category_analysis`. Esto asigna un número `1` a la categoría que generó más ingresos para ese cliente específico. Luego filtramos `AND ca.rn = 1` para obtener solo esa categoría.
4.  **Valores Numéricos**:
    *   `NULLIF(cm.total_orders, 0)`: Evita errores de división por cero si teóricamente hubiera un caso raro donde las órdenes sean 0.
    *   `::NUMERIC`: Asegura que la división para `avg_order_value` devuelva decimales y no enteros truncados.
5.  **Compatibilidad (MySQL)**:
    *   Si usas **MySQL**, cambia `NOW() - INTERVAL '6 MONTH'` por `NOW() - INTERVAL 6 MONTH` y elimina el casting `::NUMERIC` (usa `CAST(... AS DECIMAL)` o simplemente dividiendo ya suele funcionar bien en versiones modernas).

### Consideraciones sobre los datos:
*   **Revenue**: Se usa `orders.total` para el ingreso total del cliente (lo que pagó realmente) y `order_items` para desglosar la categoría (para ver qué productos impulsaron ese ingreso).
*   **Empates en Categoría**: Si dos categorías tienen exactamente el mismo monto de ventas para un cliente, `ROW_NUMBER` elegirá una arbitrariamente.