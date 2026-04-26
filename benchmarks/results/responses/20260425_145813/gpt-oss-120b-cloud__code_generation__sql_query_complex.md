# GPT-OSS 120B (Ollama Cloud) — code_generation/sql_query_complex

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 8.08 | quality: 9.52
- latency_total: 14.648s | tokens_per_second: 85.6
- input_tokens: 208 | output_tokens: 1254
- judge_score: 4.8 | justificación: 

## Respuesta completa

**Consulta SQL (compatible con PostgreSQL / MySQL 8+)**  

```sql
/*  Top‑10 clientes por revenue en los últimos 6 meses
    – al menos 3 órdenes completadas
    – muestra la categoría más comprada por cada cliente                */
WITH filtered_orders AS (
    /* Órdenes completadas en los últimos 6 meses */
    SELECT  o.id,
            o.customer_id,
            o.created_at
    FROM    orders o
    WHERE   o.status = 'completed'
      AND   o.created_at >= CURRENT_DATE - INTERVAL '6 months'
),

order_revenue AS (
    /* Revenue por orden (suma de quantity * unit_price) */
    SELECT  fo.customer_id,
            fo.id               AS order_id,
            SUM(oi.quantity * oi.unit_price) AS order_total
    FROM    filtered_orders fo
    JOIN    order_items oi ON oi.order_id = fo.id
    GROUP BY fo.customer_id, fo.id
),

customer_stats AS (
    /* Estadísticas agregadas por cliente */
    SELECT  c.id                         AS customer_id,
            c.name,
            c.email,
            c.country,
            COUNT(orv.order_id)          AS total_orders,
            SUM(orv.order_total)         AS total_revenue,
            AVG(orv.order_total)        AS avg_order_value
    FROM    customers c
    JOIN    order_revenue orv
            ON orv.customer_id = c.id
    GROUP BY c.id, c.name, c.email, c.country
    HAVING  COUNT(orv.order_id) >= 3          -- al menos 3 órdenes completadas
),

category_per_customer AS (
    /* Suma de cantidad por categoría y cliente */
    SELECT  c.id               AS customer_id,
            p.category,
            SUM(oi.quantity)   AS qty_in_category
    FROM    customers c
    JOIN    filtered_orders fo
            ON fo.customer_id = c.id
    JOIN    order_items oi
            ON oi.order_id = fo.id
    JOIN    products p
            ON p.id = oi.product_id
    GROUP BY c.id, p.category
),

best_category AS (
    /* Categoría con mayor cantidad comprada por cliente */
    SELECT  customer_id,
            category AS categoria_mas_comprada
    FROM (
        SELECT  customer_id,
                category,
                qty_in_category,
                ROW_NUMBER() OVER (PARTITION BY customer_id
                                   ORDER BY qty_in_category DESC) AS rn
        FROM    category_per_customer
    ) t
    WHERE   rn = 1
)

SELECT  cs.name,
        cs.email,
        cs.country,
        cs.total_orders,
        cs.total_revenue,
        cs.avg_order_value,
        bc.categoria_mas_comprada
FROM    customer_stats cs
LEFT JOIN best_category bc
       ON bc.customer_id = cs.customer_id
ORDER BY cs.total_revenue DESC
LIMIT 10;
```

### Explicación paso a paso  

| Paso | Qué hace | Por qué es necesario |
|------|----------|----------------------|
| **filtered_orders** | Selecciona solo las órdenes con `status = 'completed'` y cuya fecha está dentro de los últimos 6 meses. | Limita el análisis al periodo solicitado y a órdenes finalizadas. |
| **order_revenue** | Calcula el revenue de cada orden (`quantity * unit_price`). | Necesitamos el valor total de cada orden para después sumar por cliente y obtener el promedio. |
| **customer_stats** | Agrupa por cliente y calcula: <br>• `total_orders` <br>• `total_revenue` (suma de todos los `order_total`) <br>• `avg_order_value` (media por orden). <br>Aplica `HAVING COUNT >= 3`. | Produce las métricas principales y filtra a los clientes con al menos 3 órdenes completadas. |
| **category_per_customer** | Suma la cantidad de productos comprados por categoría para cada cliente. | Necesario para determinar cuál es la categoría más comprada. |
| **best_category** | Con una ventana (`ROW_NUMBER`) elige, por cliente, la categoría con mayor `qty_in_category`. | Obtiene la **categoría_mas_comprada** requerida. |
| **SELECT final** | Une los datos de `customer_stats` con `best_category`, ordena por `total_revenue` descendente y limita a los 10 primeros. | Presenta la tabla final con todas las columnas solicitadas. |

#### Notas de compatibilidad  

- **PostgreSQL**: la sintaxis `INTERVAL '6 months'` y las funciones de ventana (`ROW_NUMBER()`) funcionan tal cual.  
- **MySQL 8.0+**: reemplazar `CURRENT_DATE - INTERVAL '6 months'` por `CURRENT_DATE - INTERVAL 6 MONTH` y todo lo demás es idéntico.  
- Si utilizas **SQL Server**, cambia la expresión de intervalo a `DATEADD(MONTH, -6, GETDATE())` y adapta los alias de ventana (`OVER (PARTITION BY ...)`).  

Con esta consulta obtienes los diez clientes que más han generado ingresos en los últimos seis meses, junto con sus datos de contacto, número y valor medio de órdenes, y la categoría que más han comprado.