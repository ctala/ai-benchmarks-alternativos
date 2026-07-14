# Nemotron 3 Nano Omni 30B-A3B Reasoning — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 9.19 | quality: 9.8
- latency_total: 11.457s | tokens_per_second: 145.2
- input_tokens: 160 | output_tokens: 1664
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL completa y bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

**Consulta SQL (MySQL / MariaDB)**  

```sql
SELECT
    c.name                                   AS nombre,
    c.email                                  AS email,
    c.country                                AS pais,
    COUNT(o.id)                              AS total_orders,
    SUM(oi.quantity * oi.unit_price)         AS total_revenue,
    SUM(oi.quantity * oi.unit_price) / COUNT(o.id) AS avg_order_value,
    /* categoría que generó mayor facturación para ese cliente */
    ( SELECT p.category
      FROM customers      c2
      JOIN orders         o2  ON o2.customer_id = c2.id
      JOIN order_items    oi2 ON oi2.order_id   = o2.id
      JOIN products       p   ON p.id           = oi2.product_id
      WHERE c2.id = c.id                         -- mismo cliente
        AND o2.status = 'completed'
        AND o2.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)
      GROUP BY p.category
      ORDER BY SUM(oi2.quantity * oi2.unit_price) DESC
      LIMIT 1
    )                                        AS categoria_mas_comprada
FROM customers      c
JOIN orders         o  ON o.customer_id = c.id
JOIN order_items    oi ON oi.order_id   = o.id
WHERE o.status = 'completed'
  AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)   -- últimos 6 meses
GROUP BY c.id, c.name, c.email, c.country
HAVING COUNT(o.id) >= 3                                   -- al menos 3 órdenes
ORDER BY total_revenue DESC
LIMIT 10;      -- Top 10
```

### Explicación paso a paso  

| Paso | Qué hace | Detalle |
|------|----------|---------|
| **1. Filtrado de órdenes** | `WHERE o.status = 'completed' AND o.created_at >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` | Sólo órdenes *completadas* dentro del último medio año. |
| **2. Agrupación por cliente** | `GROUP BY c.id, c.name, c.email, c.country` | Calculamos métricas por cada cliente. |
| **3. Total de órdenes** | `COUNT(o.id) AS total_orders` | Número de órdenes (distintas) del cliente. |
| **4. Ingresos totales** | `SUM(oi.quantity * oi.unit_price) AS total_revenue` | Suma de `quantity × unit_price` de todas las líneas de los pedidos del cliente. |
| **5. Valor medio de pedido** | `SUM(oi.quantity * oi.unit_price) / COUNT(o.id) AS avg_order_value` | Ingresos totales divididos por la cantidad de órdenes. |
| **6. Categoría más comprada** | Sub‑consulta que suma el ingreso por categoría y devuelve la que tiene mayor total. | Se consideran sólo los pedidos del cliente y del período seleccionado. |
| **7. Condición de mínimo 3 órdenes** | `HAVING COUNT(o.id) >= 3` | Excluimos clientes con menos de 3 órdenes completadas. |
| **8. Orden y límite** | `ORDER BY total_revenue DESC LIMIT 10` | Top 10 clientes por mayor facturación. |

> **Nota:** La sintaxis `DATE_SUB(CURDATE(), INTERVAL 6 MONTH)` está pensada para MySQL/MariaDB.  
> Si usas otro motor (PostgreSQL, SQL Server, Oracle, …) adapta la función de cálculo de fechas, por ejemplo:  
> - PostgreSQL: `o.created_at >= CURRENT_DATE - INTERVAL '6 months'`  
> - SQL Server: `o.created_at >= DATEADD(month, -6, GETDATE())`  
> - Oracle: `o.created_at >= ADD_MONTHS(SYSDATE, -6)`  

Esta consulta cumple con todos los requisitos solicitados. ¡Éxitos!