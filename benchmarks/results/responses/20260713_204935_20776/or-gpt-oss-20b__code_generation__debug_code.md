# GPT-OSS 20B — code_generation/debug_code

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.04 | quality: 9.8
- latency_total: 10.833s | tokens_per_second: 94.4
- input_tokens: 270 | output_tokens: 1023
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, abordando todos los bugs y mejorando el código con explicaciones detalladas.

## Respuesta completa

## 1. Bug #1 – **Division por cero si no hay órdenes “pending”**

```python
average = total / len(processed)
```

Si *processed* está vacío (`len(processed) == 0`) el cálculo del promedio provoca una excepción `ZeroDivisionError`.  
**Solución**: comprobar el tamaño de la lista antes de dividir o devolver `0` (o `None`) cuando no haya órdenes procesadas.

---

## 2. Bug #2 – **Mutación del diccionario original**

```python
order['final_price'] = final_price
order['status'] = 'processed'
processed.append(order)
```

Al modificar el diccionario `order` dentro del bucle, también se altera el elemento que ya existe en la lista `orders`.  
**Solución**: crear una copia del diccionario antes de modificarlo. Una copia superficial (`dict(order)`) es suficiente porque los valores son primitivos (números, cadenas).

---

## 3. Bug #3 – **`count` incorrecto**

```python
'count': len(orders)
```

`count` debe representar cuántas órdenes realmente fueron procesadas, no el total de órdenes recibidas.  
**Solución**: usar `len(processed)`.

---

## Código corregido

```python
def process_orders(orders):
    """
    Procesa las órdenes que están en estado 'pending'.

    Devuelve:
        - processed: lista de órdenes procesadas (copia de los originales).
        - total: suma de los precios finales.
        - average: precio promedio de las órdenes procesadas.
        - count: número de órdenes procesadas.
    """
    total = 0.0
    processed = []

    for order in orders:
        if order.get('status') == 'pending':
            # Hacemos una copia para no mutar el diccionario original
            order_copy = dict(order)

            # Calculamos el descuento (10 % si el total > 100)
            discount = order_copy['total'] * 0.1 if order_copy['total'] > 100 else 0

            final_price = order_copy['total'] - discount
            order_copy.update({
                'final_price': final_price,
                'status': 'processed'
            })

            total += final_price
            processed.append(order_copy)

    count = len(processed)
    # Evitamos la división por cero
    average = total / count if count > 0 else 0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': count
    }
```

### ¿Qué cambió?

| Cambio | Por qué |
|--------|---------|
| `dict(order)` | Evita mutar el diccionario original. |
| `count = len(processed)` | `count` ahora refleja la cantidad de órdenes procesadas. |
| `average = total / count if count > 0 else 0` | Se previene la división por cero. |
| Comentarios y docstring | Mejor legibilidad. |

Con estas correcciones el algoritmo es seguro, no modifica los datos de entrada y devuelve la métrica correcta.