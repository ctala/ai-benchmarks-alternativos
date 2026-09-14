# Mercury 2.5 — code_generation/debug_code

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.54 | quality: 10.0
- latency_total: 2.801s | tokens_per_second: 516.9
- input_tokens: 231 | output_tokens: 1448
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y de gran utilidad práctica, abordando todos los errores y proporcionando una solución completa.

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



Aquí tienes el análisis de los errores y la solución corregida.

### Explicación de los Bugs

1.  **División por cero:** Si la lista `processed` queda vacía (porque no hay órdenes pendientes), calcular el promedio divide por cero, lo que lanza una excepción `ZeroDivisionError`.
2.  **Mutación del original:** El bucle modifica directamente los diccionarios dentro de la lista `orders` (agregando `final_price` y cambiando `status`). Esto genera efectos secundarios no deseados en el código que llama a la función.
3.  **Contador incorrecto:** El campo `count` devuelve el número total de órdenes de entrada, en lugar de cuántas fueron realmente procesadas.

### Versión Corregida

```python
def process_orders(orders):
    total = 0
    processed = []
    for order in orders:
        if order['status'] == 'pending':
            # Crear copia para evitar mutar la entrada original
            order_copy = order.copy()
            discount = order_copy['total'] * 0.1 if order_copy['total'] > 100 else 0
            final_price = order_copy['total'] - discount
            order_copy['final_price'] = final_price
            order_copy['status'] = 'processed'
            total += final_price
            processed.append(order_copy)

    # Evitar división por cero si no hay elementos procesados
    average = total / len(processed) if processed else 0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': len(processed)
    }
```