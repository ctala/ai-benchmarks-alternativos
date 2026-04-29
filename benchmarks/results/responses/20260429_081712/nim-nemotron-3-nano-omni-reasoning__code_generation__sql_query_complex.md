# Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM) — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning`
- success: True  | final: 7.48 | quality: 9.52
- latency_total: 7.984s | tokens_per_second: 251.9
- input_tokens: 157 | output_tokens: 2011
- judge_score: 4.8 | justificación: 

## Respuesta completa

**Consulta SQL (PostgreSQL)**  

```sql
/* 1️⃣  Resumen de cada cliente (orders, revenue, avg) */
WITH rev AS (
    SELECT
        c.id                                    AS cust_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id)                             AS total_orders,
        SUM(o.total)                            AS total_revenue,
        AVG(o.total)                            AS avg_order_value
    FROM customers c
    JOIN orders o
          ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3                     -- al menos 3 órdenes
),

/* 2️⃣  Categoría más comprada por cliente (por cantidad de unidades) */
cat AS (
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity)                        AS total_qty,
        ROW_NUMBER() OVER (PARTITION BY o.customer_id
                           ORDER BY SUM(oi.quantity) DESC) AS rn   -- la fila con mayor qty
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.id
    JOIN products p      ON p.id = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
)

-- 3️⃣  Unimos ambos CTE y quedamos con la categoría de mayor qty (rn = 1)
SELECT
    r.cust_id,
    r.name,
    r.email,
    r.country,
    r.total_orders,
    r.total_revenue,
    r.avg_order_value,
    c.category AS categoria_mas_comprada
FROM rev r
JOIN cat c
      ON c.customer_id = r.cust_id
     AND c.rn = 1                     -- solo la categoría más frecuente
ORDER BY r.total_revenue DESC
LIMIT 10;
```

### ¿Qué hace cada parte?

| Paso | Descripción |
|------|-------------|
| **`rev` CTE** | Agrupa por cliente y calcula: <br>• `total_orders` (cantidad de órdenes completadas) <br>• `total_revenue` (suma del campo `total` de la tabla `orders`) <br>• `avg_order_value` (promedio de `total`) <br>Filtra por estado *completed*, por fechas de los últimos 6 meses y por al menos 3 órdenes (`HAVING COUNT(o.id) >= 3`). |
| **`cat` CTE** | Para cada pedido completo en el mismo período, suma la cantidad de unidades (`quantity`) de los productos pertenecientes a cada categoría. Usa `ROW_NUMBER()` para identificar, por cliente, la categoría con la mayor suma de unidades (`rn = 1`). |
| **SELECT final** | Une el resumen de ingresos (`rev`) con la categoría más comprada (`cat`) y ordena por `total_revenue` descendente, limitando a los 10 primeros clientes. |

### Columnas devueltas

| Columna | Significado |
|---------|--------------|
| `name` | Nombre del cliente |
| `email` | Email del cliente |
| `country` | País del cliente |
| `total_orders` | Número de órdenes completadas en los últimos 6 meses |
| `total_revenue` | Ingreso total (suma de `orders.total`) |
| `avg_order_value` | Valor medio de cada orden (`total_revenue / total_orders`) |
| `categoria_mas_comprada` | Categoría de producto que el cliente compró con mayor cantidad de unidades en ese periodo |

Esta consulta cumple con todos los requisitos: top 10 clientes por revenue en los últimos 6 meses, solo clientes con ≥ 3 órdenes completadas, y muestra la categoría más comprada.