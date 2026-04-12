"""
Tests de generacion de codigo.
Evalua capacidad de coding para automatizaciones.
"""

TESTS = [
    {
        "name": "python_api_integration",
        "description": "Generar integracion con API REST",
        "messages": [
            {"role": "user", "content": """Escribe una funcion Python que:
1. Haga GET a https://api.example.com/products con autenticacion Bearer token
2. Filtre productos con precio > 100
3. Retorne una lista de dicts con solo {id, name, price}
4. Maneje errores de red y timeout (10 segundos)
5. Incluya retry con backoff exponencial (max 3 intentos)

Usa httpx y no dependencias externas adicionales."""},
        ],
        "criteria": {
            "min_words": 50,
            "required_sections": ["def", "httpx", "retry", "Bearer", "timeout"],
            "language": "en",
        },
    },
    {
        "name": "n8n_workflow_json",
        "description": "Generar workflow de N8N en JSON",
        "messages": [
            {"role": "user", "content": """Genera un workflow de N8N en JSON que:
1. Se active con un webhook POST
2. Extraiga el campo "email" y "message" del body
3. Use un nodo de IA (OpenAI) para clasificar el mensaje como "soporte", "ventas" o "otro"
4. Segun la clasificacion, envie el email a un canal de Slack diferente:
   - soporte -> #support
   - ventas -> #sales
   - otro -> #general

Dame el JSON completo del workflow."""},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": ["webhook", "openai", "slack", "nodes"],
            "language": "en",
        },
    },
    {
        "name": "sql_query_complex",
        "description": "Generar query SQL compleja",
        "messages": [
            {"role": "user", "content": """Tengo estas tablas:
- orders (id, customer_id, total, status, created_at)
- customers (id, name, email, country, created_at)
- order_items (id, order_id, product_id, quantity, unit_price)
- products (id, name, category, price)

Escribe una query SQL que muestre:
- Top 10 clientes por revenue total en los ultimos 6 meses
- Con columnas: nombre, email, pais, total_orders, total_revenue, avg_order_value, categoria_mas_comprada
- Ordena por total_revenue DESC
- Solo clientes con al menos 3 ordenes completadas (status = 'completed')"""},
        ],
        "criteria": {
            "min_words": 50,
            "required_sections": ["SELECT", "JOIN", "GROUP BY", "ORDER BY", "HAVING"],
            "language": "en",
        },
    },
    {
        "name": "debug_code",
        "description": "Identificar y corregir bugs",
        "messages": [
            {"role": "user", "content": """Este codigo tiene varios bugs. Identificalos y corrige:

```python
def process_orders(orders):
    total = 0
    processed = []
    for order in orders:
        if order['status'] == 'pending':
            discount = order['total'] * 0.1 if order['total'] > 100 else 0
            final_price = order['total'] - discount
            order['final_price'] = final_price
            order['status'] = 'processed'
            total += final_price
            processed.append(order)

    average = total / len(processed)

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': len(orders)
    }

# Bugs a encontrar:
# 1. Division por cero si no hay ordenes pending
# 2. Muta el diccionario original
# 3. 'count' deberia ser len(processed), no len(orders)
```

Explica cada bug y da la version corregida."""},
        ],
        "criteria": {
            "min_words": 100,
            "required_sections": ["bug", "division", "cero", "corregid"],
            "language": "es",
        },
    },
]
