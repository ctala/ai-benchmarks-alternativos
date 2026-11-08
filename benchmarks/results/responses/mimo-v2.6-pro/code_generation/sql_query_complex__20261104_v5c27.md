# MiMo V2.6 Pro — code_generation/sql_query_complex

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.62 | quality: 9.8
- latency_total: 31.034s | tokens_per_second: 63.9
- input_tokens: 152 | output_tokens: 1984
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

## Query SQL

```sql
WITH customer_category_rank AS (
    -- CTE 1: Rankea la categoría más comprada (por cantidad) por cada cliente
    SELECT
        o.customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity,
        ROW_NUMBER() OVER (
            PARTITION BY o.customer_id
            ORDER BY SUM(oi.quantity) DESC
        ) AS rn
    FROM orders        o
    JOIN order_items   oi ON oi.order_id   = o.id
    JOIN products      p  ON p.id          = oi.product_id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY o.customer_id, p.category
),
customer_stats AS (
    -- CTE 2: Calcula métricas principales por cliente (≥ 3 órdenes completadas)
    SELECT
        c.id              AS customer_id,
        c.name,
        c.email,
        c.country,
        COUNT(o.id)       AS total_orders,
        SUM(o.total)      AS total_revenue,
        AVG(o.total)      AS avg_order_value
    FROM customers  c
    JOIN orders     o ON o.customer_id = c.id
    WHERE o.status = 'completed'
      AND o.created_at >= CURRENT_DATE - INTERVAL '6 months'
    GROUP BY c.id, c.name, c.email, c.country
    HAVING COUNT(o.id) >= 3
)
-- Consulta final
SELECT
    cs.name,
    cs.email,
    cs.country,
    cs.total_orders,
    cs.total_revenue,
    cs.avg_order_value,
    ccr.category      AS categoria_mas_comprada
FROM customer_stats       cs
LEFT JOIN customer_category_rank ccr
       ON cs.customer_id = ccr.customer_id
      AND ccr.rn         = 1
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

---

## Explicación paso a paso

### 🔹 CTE `customer_category_rank`
| Paso | Qué hace |
|------|----------|
| **JOIN** | Cruza `orders → order_items → products` para obtener la categoría de cada ítem |
| **WHERE** | Filtra solo órdenes **completadas** en los **últimos 6 meses** |
| **GROUP BY** | Agrupa por cliente y categoría |
| **ROW_NUMBER()** | Asigna `1` a la categoría con **mayor cantidad total comprada** por cliente |

### 🔹 CTE `customer_stats`
| Paso | Qué hace |
|------|----------|
| **JOIN** | Cruza `customers → orders` |
| **WHERE** | Filtra solo órdenes **completadas** en los **últimos 6 meses** |
| **GROUP BY** | Agrupa por cliente |
| **HAVING ≥ 3** | Solo deja clientes con al menos **3 órdenes completadas** |
| **Métricas** | `total_orders`, `total_revenue` (SUM de `orders.total`), `avg_order_value` (AVG) |

### 🔹 Consulta final
| Paso | Qué hace |
|------|----------|
| **LEFT JOIN** | Une las métricas del cliente con su categoría más comprada (`rn = 1`) |
| **ORDER BY** | Ordena por `total_revenue` descendente |
| **LIMIT 10** | Se queda con el **Top 10** |

---

## ⚠️ Notas de dialecto

| Dialecto | Sintaxis de "últimos 6 meses" |
|----------|-------------------------------|
| **PostgreSQL** | `o.created_at >= CURRENT_DATE - INTERVAL '6 months'` ✅ *(usado arriba)* |
| **MySQL** | `o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` |
| **SQL Server** | `o.created_at >= DATEADD(MONTH, -6, GETDATE())` |
| **SQLite** | `o.created_at >= DATE('now', '-6 months')` |

> **Sobre `categoria_mas_comprada`:** Se usa `SUM(oi.quantity)` como criterio. Si prefieres rankear por **ingresos** de la categoría, sustituye por `SUM(oi.quantity * oi.unit_price)` en la CTE `customer_category_rank`.