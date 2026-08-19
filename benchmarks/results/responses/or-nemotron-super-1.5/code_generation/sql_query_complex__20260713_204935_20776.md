# Nemotron Super 49B v1.5 — code_generation/sql_query_complex

- model_id: `nvidia/llama-3.3-nemotron-super-49b-v1.5`
- success: True  | final: 8.66 | quality: 9.8
- latency_total: 66.365s | tokens_per_second: 53.7
- input_tokens: 163 | output_tokens: 3563
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una consulta SQL bien estructurada que cumple con todos los requisitos especificados.

## Respuesta completa

Aquí está la consulta SQL que cumple con los requisitos especificados:

```sql
WITH customer_category AS (
    SELECT 
        c.id AS customer_id,
        p.category,
        SUM(oi.quantity) AS total_quantity
    FROM customers c
    JOIN orders o ON c.id = o.customer_id
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL 6 MONTH
    GROUP BY c.id, p.category
),
ranked_categories AS (
    SELECT 
        customer_id,
        category,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY total_quantity DESC) AS rn
    FROM customer_category
)
SELECT 
    c.name,
    c.email,
    c.country,
    COUNT(DISTINCT o.id) AS total_orders,
    SUM(oi.quantity * oi.unit_price) AS total_revenue,
    SUM(oi.quantity * oi.unit_price) / COUNT(DISTINCT o.id) AS avg_order_value,
    rc.category AS categoria_mas_comprada
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN order_items oi ON o.id = oi.order_id
LEFT JOIN ranked_categories rc 
    ON c.id = rc.customer_id 
    AND rc.rn = 1
WHERE 
    o.status = 'completed'
    AND o.created_at >= CURRENT_DATE - INTERVAL 6 MONTH
GROUP BY 
    c.id, c.name, c.email, c.country, rc.category
HAVING 
    COUNT(DISTINCT o.id) >= 3
ORDER BY 
    total_revenue DESC
LIMIT 10;
```

**Explicación detallada:**

1. **CTE `customer_category`:**
   - Calcula la cantidad total de productos comprados por cada cliente y categoría.
   - Filtra órdenes completadas en los últimos 6 meses.

2. **CTE `ranked_categories`:**
   - Asigna un número de fila a cada categoría por cliente, ordenando por cantidad total descendente.
   - La categoría con `rn = 1` es la más comprada por cada cliente.

3. **Consulta principal:**
   - **Uniones:** Conecta clientes, órdenes, artículos de órdenes y categorías más compradas.
   - **Filtros:** Solo órdenes completadas en los últimos 6 meses.
   - **Agrupación:** Por cliente y su categoría más comprada.
   - **Cálculos:**
     - `total_orders`: Conta órdenes únicas por cliente.
     - `total_revenue`: Suma el valor total de todos los artículos.
     - `avg_order_value`: Promedio de valor por orden (revenue total / número de órdenes).
   - **Condición `HAVING`:** Filtra clientes con al menos 3 órdenes.
   - **Ordenamiento y límite:** Ordena por revenue descendente y limita a 10 resultados.

Esta consulta proporciona los datos solicitados de manera eficiente utilizando tablas temporales (CTEs) para calcular la categoría más comprada por cliente.