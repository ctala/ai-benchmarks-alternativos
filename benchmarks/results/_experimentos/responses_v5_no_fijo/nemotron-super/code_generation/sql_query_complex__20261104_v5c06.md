# Nemotron 3 Super — code_generation/sql_query_complex

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.72 | quality: 9.56
- latency_total: 12.057s | tokens_per_second: 93.6
- input_tokens: 160 | output_tokens: 1128
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

```sql
WITH recent_orders AS (
    SELECT o.id,
           o.customer_id
    FROM orders o
    WHERE o.status = 'completed'
      AND o.created_at >= DATE_SUB(
            (SELECT MAX(created_at) FROM orders),
            INTERVAL 6 MONTH
          )
),

order_stats AS (
    SELECT ro.customer_id,
           COUNT(*)                               AS total_orders,
           SUM(oi.quantity * oi.unit_price)      AS total_revenue,
           SUM(oi.quantity * oi.unit_price) / COUNT(*) AS avg_order_value
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    GROUP BY ro.customer_id
),

customer_category AS (
    SELECT ro.customer_id,
           p.category,
           SUM(oi.quantity) AS qty
    FROM recent_orders ro
    JOIN order_items oi ON oi.order_id = ro.id
    JOIN products p ON p.id = oi.product_id
    GROUP BY ro.customer_id, p.category
),

ranked_category AS (
    SELECT customer_id,
           category,
           ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY qty DESC) AS rn
    FROM customer_category
)

SELECT  c.name,
        c.email,
        c.country AS pais,
        os.total_orders,
        os.total_revenue,
        os.avg_order_value,
        rc.category AS categoria_mas_comprada
FROM customers c
JOIN order_stats os ON c.id = os.customer_id
LEFT JOIN ranked_category rc
       ON c.id = rc.customer_id
      AND rc.rn = 1                     -- la categoría con mayor cantidad comprada
WHERE os.total_orders >= 3
ORDER BY os.total_revenue DESC
LIMIT 10;
```

**Explicación breve**

1. **recent_orders** – selecciona solo las órdenes completadas de los últimos 6 meses (usando la fecha máxima de la tabla como referencia).  
2. **order_stats** – agrupa por cliente para obtener `total_orders`, `total_revenue` y `avg_order_value`.  
3. **customer_category** – suma la cantidad de cada producto comprada por cliente y categoría.  
4. **ranked_category** – asigna un número de fila dentro de cada cliente ordenado por la cantidad, de modo que `rn = 1` corresponde a la categoría más comprada.  
5. En la consulta final se unen los datos del cliente, se filtran aquellos con al menos 3 órdenes completadas, se ordenan por `total_revenue` descendente y se limitan a los top 10.  

Las columnas solicitadas son: `nombre`, `email`, `pais`, `total_orders`, `total_revenue`, `avg_order_value` y `categoria_mas_comprada`.