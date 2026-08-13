# GPT-5.6 Terra Pro — code_generation/debug_code

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.34 | quality: 9.7
- latency_total: 7.351s | tokens_per_second: 280.4
- input_tokens: 4349 | output_tokens: 2061
- judge_score: 5 | justificación: La respuesta identifica y corrige con precisión los errores en el código, proporciona una solución clara y bien estructurada, y ofrece una explicación detallada que es altamente útil para un emprendedor.

## Entrada exacta (lo que recibió el modelo)

**user:**

Este codigo tiene varios bugs. Identificalos y corrige:

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

Explica cada bug y da la version corregida.


## Respuesta completa

Los problemas son:

1. **División por cero**  
   Si no hay órdenes con estado `"pending"`, `processed` queda vacío. Entonces `len(processed)` es `0` y esta línea falla:

   ```python
   average = total / len(processed)
   ```

   Debe devolverse, por ejemplo, `0` como promedio cuando no se procesó ninguna orden.

2. **Mutación de los diccionarios originales**  
   Estas líneas modifican directamente los diccionarios que vienen en `orders`:

   ```python
   order['final_price'] = final_price
   order['status'] = 'processed'
   ```

   Como los diccionarios son objetos mutables, quien llamó a la función verá sus órdenes originales modificadas. Hay que crear una copia antes de cambiar sus campos.

3. **`count` incorrecto**  
   Actualmente devuelve el número total de órdenes recibidas:

   ```python
   'count': len(orders)
   ```

   Pero el resultado representa las órdenes procesadas, así que debe ser:

   ```python
   'count': len(processed)
   ```

Versión corregida:

```python
def process_orders(orders):
    total = 0
    processed = []

    for order in orders:
        if order.get('status') == 'pending':
            order_total = order.get('total', 0)

            discount = order_total * 0.1 if order_total > 100 else 0
            final_price = order_total - discount

            # Copia para no modificar la orden original.
            processed_order = order.copy()
            processed_order['final_price'] = final_price
            processed_order['status'] = 'processed'

            total += final_price
            processed.append(processed_order)

    count = len(processed)
    average = total / count if count > 0 else 0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': count
    }
```

Ejemplo:

```python
orders = [
    {'id': 1, 'status': 'pending', 'total': 150},
    {'id': 2, 'status': 'completed', 'total': 50},
    {'id': 3, 'status': 'pending', 'total': 80}
]

result = process_orders(orders)

print(result)
# {
#     'processed': [
#         {'id': 1, 'status': 'processed', 'total': 150, 'final_price': 135.0},
#         {'id': 3, 'status': 'processed', 'total': 80, 'final_price': 80}
#     ],
#     'total': 215.0,
#     'average': 107.5,
#     'count': 2
# }

print(orders)
# Las órdenes originales conservan su estado original:
# [
#     {'id': 1, 'status': 'pending', 'total': 150},
#     {'id': 2, 'status': 'completed', 'total': 50},
#     {'id': 3, 'status': 'pending', 'total': 80}
# ]
```