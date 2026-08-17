# GPT-5.6 Luna — code_generation/debug_code

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.85 | quality: 9.8
- latency_total: 3.993s | tokens_per_second: 145.8
- input_tokens: 222 | output_tokens: 582
- judge_score: 5 | justificación: La respuesta identifica y corrige con precisión los bugs, proporciona una solución clara y relevante, y ofrece utilidad práctica al evitar la mutación de datos originales y manejar correctamente el cálculo del promedio.

## Respuesta completa

Los bugs son:

1. **División por cero**  
   Si no hay órdenes con estado `pending`, `processed` queda vacío y `total / len(processed)` provoca `ZeroDivisionError`.

2. **Mutación de las órdenes originales**  
   El código modifica directamente cada diccionario recibido:

   ```python
   order['final_price'] = final_price
   order['status'] = 'processed'
   ```

   Esto cambia la lista o los diccionarios originales que recibió la función.

3. **Conteo incorrecto**  
   `len(orders)` cuenta todas las órdenes, incluidas las que no estaban pendientes. El conteo debe ser el de las órdenes procesadas: `len(processed)`.

Versión corregida:

```python
def process_orders(orders):
    total = 0
    processed = []

    for order in orders:
        if order['status'] == 'pending':
            order_total = order['total']
            discount = order_total * 0.1 if order_total > 100 else 0
            final_price = order_total - discount

            # Crear una copia para no modificar la orden original
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

Cuando no hay órdenes pendientes, `average` será `0` y la función no lanzará una excepción. Además, las órdenes originales permanecerán sin cambios.