# GLM 5.2 — code_generation/debug_code

- model_id: `z-ai/glm-5.2`
- success: True  | final: 7.72 | quality: 8.96
- latency_total: 29.154s | tokens_per_second: 45.1
- input_tokens: 231 | output_tokens: 1315
- judge_score: 4.4 | justificación: 

## Respuesta completa

El código tiene tres bugs principales:

1. **División por cero**  
   Si no hay órdenes con `status == 'pending'`, la lista `processed` queda vacía y `len(processed)` es `0`. Al calcular `average = total / len(processed)` se produce un `ZeroDivisionError`.

2. **Mutación del diccionario original**  
   Se modifican directamente los diccionarios de la lista de entrada con `order['final_price'] = ...` y `order['status'] = 'processed'`. Esto altera los datos originales, lo cual es un efecto secundario no deseado.

3. **`count` incorrecto**  
   Se devuelve `len(orders)`, que cuenta todas las órdenes recibidas, pero debería ser `len(processed)`, ya que solo se procesaron las órdenes pendientes.

Versión corregida:

```python
def process_orders(orders):
    total = 0
    processed = []

    for order in orders:
        if order.get('status') == 'pending':
            order_total = order['total']
            discount = order_total * 0.1 if order_total > 100 else 0
            final_price = order_total - discount

            # Crear una copia para no mutar el original
            new_order = {
                **order,
                'final_price': final_price,
                'status': 'processed'
            }

            total += final_price
            processed.append(new_order)

    count = len(processed)
    average = total / count if count > 0 else 0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': count
    }
```

Cambios principales:
- Se crea un nuevo diccionario `new_order` con `{**order, ...}` para evitar modificar el original.
- Se calcula `average` con una guarda `if count > 0 else 0` para evitar la división por cero.
- `count` ahora usa `len(processed)`, reflejando correctamente cuántas órdenes fueron procesadas.