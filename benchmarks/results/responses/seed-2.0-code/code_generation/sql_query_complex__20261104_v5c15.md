# Seed 2.0 Code — code_generation/sql_query_complex

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 74.7s | tokens_per_second: 73.7
- input_tokens: 182 | output_tokens: 5508
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos, incluyendo el cálculo de métricas y la identificación de la categoría más comprada, lo que la hace altamente útil para un emprendedor.

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

### Consulta SQL Explicada (Compatible con **PostgreSQL** por defecto, adaptada a otros motores al final)
Se usan **CTEs (Common Table Expressions)** para modularizar la lógica y facilitar el mantenimiento. Cumplimos TODOS los requisitos:

---

#### Paso a Paso de la Lógica:
1. **Filtrar órdenes válidas**: Solo completadas (`status = 'completed'`) en los **últimos 6 meses**.
2. **Clientes elegibles**: Solo aquellos con **al menos 3 órdenes válidas**.
3. **Calcular métricas**: `total_revenue` (suma de productos vendidos), `avg_order_value` (promedio por orden).
4. **Categoría más comprada**: Por cliente, la categoría con **más unidades vendidas** (desempate por nombre de categoría si hay empate).
5. **Top 10**: Ordenar por `total_revenue DESC` y limitar a 10.

---

### Consulta Final
```sql
WITH 
-- 1. Órdenes VÁLIDAS: Completadas en los ÚLTIMOS 6 MESES
cte_orders_validas AS (
    SELECT
        o.id AS order_id,
        o.customer_id
    FROM orders o
    WHERE
        o.status = 'completed'
        -- Ajustar fecha según motor: PostgreSQL usa INTERVAL '6 months', MySQL usa DATE_SUB(...)
        AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

-- 2. Clientes ELEGIBLES: Con AL MENOS 3 órdenes válidas
cte_clientes_elegibles AS (
    SELECT
        ov.customer_id,
        COUNT(DISTINCT ov.order_id) AS total_orders -- Conteo de órdenes (evita duplicados)
    FROM cte_orders_validas ov
    GROUP BY ov.customer_id
    HAVING COUNT(DISTINCT ov.order_id) >= 3 -- Filtro de mínimo 3 órdenes
),

-- 3. Métricas de Revenue y Valor Promedio por Orden
cte_revenue_cliente AS (
    SELECT
        ov.customer_id,
        -- Revenue = Suma de (cantidad * precio unitario) de items de órdenes válidas
        SUM(oi.quantity * oi.unit_price) AS total_revenue,
        -- Promedio por orden = Total Revenue / Número de órdenes (casteo a NUMERIC para evitar división entera)
        SUM(oi.quantity * oi.unit_price)::NUMERIC / ce.total_orders AS avg_order_value
    FROM cte_orders_validas ov
    JOIN order_items oi ON ov.order_id = oi.order_id -- Unir con items de la orden
    JOIN cte_clientes_elegibles ce ON ov.customer_id = ce.customer_id -- Solo clientes elegibles
    GROUP BY ov.customer_id, ce.total_orders
),

-- 4. Categorías Rankeadas por Cliente (para encontrar la más comprada)
cte_categorias_rankeadas AS (
    SELECT
        ov.customer_id,
        p.category AS categoria,
        SUM(oi.quantity) AS unidades_compradas, -- Medida: Cantidad de unidades (cambia por valor si quieres)
        -- Rankear por cliente: Primero por unidades DESC, luego por categoría ASC (desempate)
        ROW_NUMBER() OVER (
            PARTITION BY ov.customer_id
            ORDER BY SUM(oi.quantity) DESC, p.category ASC
        ) AS rn -- rn = 1 es la categoría MÁS COMPRADA
    FROM cte_orders_validas ov
    JOIN order_items oi ON ov.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.id -- Unir con productos para obtener categoría
    JOIN cte_clientes_elegibles ce ON ov.customer_id = ce.customer_id
    GROUP BY ov.customer_id, p.category
),

-- 5. Categoría MÁS COMPRADA por Cliente (solo rn = 1)
cte_categoria_top AS (
    SELECT
        customer_id,
        categoria AS categoria_mas_comprada
    FROM cte_categorias_rankeadas
    WHERE rn = 1
)

-- Consulta FINAL: Unir todas las métricas con datos del cliente
SELECT
    c.name AS nombre,
    c.email,
    c.country AS pais,
    ce.total_orders,
    rc.total_revenue,
    rc.avg_order_value,
    ct.categoria_mas_comprada
FROM customers c
JOIN cte_clientes_elegibles ce ON c.id = ce.customer_id
JOIN cte_revenue_cliente rc ON c.id = rc.customer_id
JOIN cte_categoria_top ct ON c.id = ct.customer_id
ORDER BY rc.total_revenue DESC -- Ordenar por Revenue MAYOR a MENOR
LIMIT 10; -- Top 10
```

---

### Modificaciones Comunes (Según Tu Necesidad)
#### 1. Usar el campo `total` de la tabla `orders` en vez de `order_items` para Revenue
Si prefieres usar el valor total de la orden (incluye impuestos/envíos si es el caso), modifica `cte_revenue_cliente`:
```sql
cte_revenue_cliente AS (
    SELECT
        ov.customer_id,
        SUM(o.total) AS total_revenue, -- Usar el campo total de orders
        SUM(o.total)::NUMERIC / ce.total_orders AS avg_order_value
    FROM cte_orders_validas ov
    JOIN orders o ON ov.order_id = o.id -- Unir con orders para obtener su total
    JOIN cte_clientes_elegibles ce ON ov.customer_id = ce.customer_id
    GROUP BY ov.customer_id, ce.total_orders
)
```

#### 2. Categoría más comprada por **valor** (no por unidades)
Cambia el `ORDER BY` en `cte_categorias_rankeadas`:
```sql
ROW_NUMBER() OVER (
    PARTITION BY ov.customer_id
    ORDER BY SUM(oi.quantity * oi.unit_price) DESC, p.category ASC -- Por valor en vez de unidades
) AS rn
```

---

### Adaptación a Otros Motores de BD
#### MySQL:
- Cambia la condición de fecha: `AND o.created_at >= DATE_SUB(CURRENT_DATE(), INTERVAL 6 MONTH)`
- Cambia el casteo a numérico: `CAST(SUM(oi.quantity * oi.unit_price) AS DECIMAL(10,2)) / ce.total_orders AS avg_order_value`

#### SQL Server:
- Usa `TOP 10` en la consulta final: `SELECT TOP 10 c.name AS nombre, ...`
- Cambia la fecha: `AND o.created_at >= DATEADD(MONTH, -6, GETDATE())`
- Cambia el casteo: `CONVERT(DECIMAL(10,2), SUM(oi.quantity * oi.unit_price)) / ce.total_orders AS avg_order_value`

---

### Cumplimiento de Requisitos
✅ Top 10 por revenue en últimos 6 meses  
✅ Columnas pedidas: `nombre`, `email`, `pais`, `total_orders`, `total_revenue`, `avg_order_value`, `categoria_mas_comprada`  
✅ Filtro de mínimo 3 órdenes completadas  
✅ Ordenado por `total_revenue DESC`  
✅ Uso de CTEs para legibilidad y mantenimiento