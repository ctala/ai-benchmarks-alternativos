# GPT-5.5 — code_generation/debug_code

- model_id: `gpt-5.5`
- success: True  | final: 7.01 | quality: 9.32
- latency_total: 9.034s | tokens_per_second: 73.4
- input_tokens: 222 | output_tokens: 663
- judge_score: 4.8 | justificación: 

## Respuesta completa

Estos son los bugs indicados y cómo corregirlos:

## Bugs

### 1. División por cero si no hay órdenes `pending`

En esta línea:

```python
average = total / len(processed)
```

si no se procesó ninguna orden, `processed` estará vacío y `len(processed)` será `0`, causando:

```python
ZeroDivisionError
```

Debe controlarse ese caso.

---

### 2. Se muta el diccionario original

Dentro del bucle se modifica directamente `order`:

```python
order['final_price'] = final_price
order['status'] = 'processed'
```

Como `order` es una referencia al diccionario original dentro de `orders`, esto altera los datos originales. Para evitarlo, se debe crear una copia antes de modificarla.

---

### 3. `count` debería ser `len(processed)`

Actualmente se retorna:

```python
'count': len(orders)
```

Pero eso cuenta todas las órdenes recibidas, no las órdenes procesadas. Lo correcto es:

```python
'count': len(processed)
```

---

## Versión corregida

```python
def process_orders(orders):
    total = 0
    processed = []

    for order in orders:
        if order['status'] == 'pending':
            discount = order['total'] * 0.1 if order['total'] > 100 else 0
            final_price = order['total'] - discount

            processed_order = order.copy()
            processed_order['final_price'] = final_price
            processed_order['status'] = 'processed'

            total += final_price
            processed.append(processed_order)

    average = total / len(processed) if processed else 0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': len(processed)
    }
```

## Ejemplo

```python
orders = [
    {'id': 1, 'status': 'pending', 'total': 150},
    {'id': 2, 'status': 'completed', 'total': 80},
    {'id': 3, 'status': 'pending', 'total': 50}
]

result = process_orders(orders)

print(result)
print(orders)
```

Resultado esperado:

```python
{
    'processed': [
        {'id': 1, 'status': 'processed', 'total': 150, 'final_price': 135.0},
        {'id': 3, 'status': 'processed', 'total': 50, 'final_price': 50}
    ],
    'total': 185.0,
    'average': 92.5,
    'count': 2
}
```

Y la lista original `orders` no se modifica.