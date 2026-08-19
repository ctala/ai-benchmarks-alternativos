# Grok 4.6 — code_generation/debug_code

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.3 | quality: 9.72
- latency_total: 14.848s | tokens_per_second: 70.0
- input_tokens: 431 | output_tokens: 1040
- judge_score: 4.8 | justificación: 

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

## Bugs

**1. División por cero**  
Si no hay órdenes con `status == 'pending'`, `processed` queda vacío y `total / len(processed)` lanza `ZeroDivisionError`.

**2. Mutación del original**  
Se escribe sobre el mismo dict (`order['final_price']`, `order['status']`) y se hace `append` de esa misma referencia. Quien llamó a la función ve sus datos cambiados.

**3. `count` incorrecto**  
`len(orders)` cuenta todas las órdenes, no las procesadas. El comentario del enunciado pide `len(processed)`.

---

## Versión corregida

```python
def process_orders(orders):
    total = 0
    processed = []

    for order in orders:
        if order.get('status') == 'pending':
            processed_order = dict(order)  # copia: no muta el original
            discount = processed_order['total'] * 0.1 if processed_order['total'] > 100 else 0
            final_price = processed_order['total'] - discount
            processed_order['final_price'] = final_price
            processed_order['status'] = 'processed'
            total += final_price
            processed.append(processed_order)

    count = len(processed)
    average = total / count if count else 0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': count,
    }
```

- `average` es `0` si no hay pendientes (también podrías devolver `None` si encaja mejor con el dominio).
- `dict(order)` es copia superficial; basta si solo tocas claves de primer nivel.
- `order.get('status')` evita `KeyError` si falta la clave.