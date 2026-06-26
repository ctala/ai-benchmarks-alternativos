# Kimi K2.7 Code — code_generation/debug_code

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 7.76 | quality: 9.72
- latency_total: 27.242s | tokens_per_second: 41.8
- input_tokens: 229 | output_tokens: 1139
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí está el análisis de los **bugs** y la versión corregida.

## Bugs encontrados

| # | Bug | Explicación |
|---|-----|-------------|
| 1 | **División por cero** | Si no hay órdenes con `status == 'pending'`, `processed` queda vacío, por lo que `total / len(processed)` lanza `ZeroDivisionError`. |
| 2 | **Mutación del diccionario original** | Al hacer `order['final_price'] = ...` y `order['status'] = 'processed'`, se modifican los diccionarios originales de la lista `orders`. Esto puede causar efectos secundarios inesperados fuera de la función. |
| 3 | **`count` incorrecto** | `count` devuelve `len(orders)`, que es la cantidad total de órdenes recibidas, no la cantidad de órdenes realmente procesadas. Debería ser `len(processed)`. |

---

## Código corregido

```python
from copy import deepcopy

def process_orders(orders):
    total = 0
    processed = []

    for order in orders:
        if order.get('status') == 'pending':
            # Evitamos mutar el diccionario original usando una copia
            processed_order = deepcopy(order)

            # Cálculo del descuento
            discount = processed_order['total'] * 0.1 if processed_order['total'] > 100 else 0
            final_price = processed_order['total'] - discount

            # Actualizamos la copia, no la original
            processed_order['final_price'] = final_price
            processed_order['status'] = 'processed'

            total += final_price
            processed.append(processed_order)

    # Evitamos división por cero
    average = total / len(processed) if processed else 0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': len(processed)
    }
```

---

## Cambios clave

1. **Copia profunda con `deepcopy`**: así no modificamos los diccionarios originales de `orders`. Si las órdenes no tienen estructuras anidadas, `dict(order)` también funciona, pero `deepcopy` es más seguro.
2. **Uso de `.get()`**: `order.get('status')` evita un error si alguna orden no tiene la clave `status`.
3. **Protección contra división por cero**: `average = total / len(processed) if processed else 0`.
4. **`count` corregido**: ahora es `len(processed)`, es decir, la cantidad de órdenes que efectivamente fueron procesadas.

---

## Ejemplo de uso

```python
orders = [
    {'id': 1, 'status': 'pending', 'total': 120},
    {'id': 2, 'status': 'completed', 'total': 80},
    {'id': 3, 'status': 'pending', 'total': 90},
]

result = process_orders(orders)

print(result)
# {
#     'processed': [
#         {'id': 1, 'status': 'processed', 'total': 120, 'final_price': 108.0},
#         {'id': 3, 'status': 'processed', 'total': 90, 'final_price': 90.0}
#     ],
#     'total': 198.0,
#     'average': 99.0,
#     'count': 2
# }

# Las órdenes originales no fueron modificadas
print(orders)
# [
#     {'id': 1, 'status': 'pending', 'total': 120},
#     {'id': 2, 'status': 'completed', 'total': 80},
#     {'id': 3, 'status': 'pending', 'total': 90}
# ]
```

Con estas correcciones, la función es más segura, no produce efectos secundarios y devuelve los datos correctos.