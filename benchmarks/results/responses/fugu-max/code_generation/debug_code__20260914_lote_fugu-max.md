# Fugu Max — code_generation/debug_code

- model_id: `sakana/fugu-max`
- success: True  | final: 8.56 | quality: 9.8
- latency_total: 5.199s | tokens_per_second: 95.4
- input_tokens: 299 | output_tokens: 496
- judge_score: 5 | justificación: La respuesta identifica y corrige todos los errores con precisión, es relevante y proporciona una solución clara y útil.

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

Los bugs son:

1. **División por cero**  
   Si no hay órdenes con estado `pending`, `processed` queda vacío y `total / len(processed)` provoca `ZeroDivisionError`.

2. **Mutación de las órdenes originales**  
   El código modifica directamente cada diccionario recibido:
   ```python
   order['final_price'] = final_price
   order['status'] = 'processed'
   ```
   Esto cambia la información del objeto original fuera de la función.

3. **Conteo incorrecto**  
   `len(orders)` cuenta todas las órdenes, incluidas las que no estaban pendientes. El conteo debe ser `len(processed)`.

Versión corregida:

```python
def process_orders(orders):
    total = 0
    processed = []

    for order in orders:
        if order['status'] == 'pending':
            # Crear una copia para no modificar la orden original
            processed_order = order.copy()

            discount = (
                processed_order['total'] * 0.1
                if processed_order['total'] > 100
                else 0
            )

            final_price = processed_order['total'] - discount

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

La función ahora:

- Evita la división por cero.
- Devuelve copias de las órdenes procesadas sin modificar las originales.
- Cuenta únicamente las órdenes realmente procesadas.