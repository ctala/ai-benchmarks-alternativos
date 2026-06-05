# Qwen 3.7 Max — code_generation/debug_code

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 7.59 | quality: 9.52
- latency_total: 20.963s | tokens_per_second: 64.8
- input_tokens: 244 | output_tokens: 1358
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Análisis y Corrección de Bugs

## Bug 1: División por cero

```python
average = total / len(processed)
```

**Problema:** Si ninguna orden tiene estado `'pending'`, la lista `processed` queda vacía y `len(processed)` es `0`. Esto lanza un `ZeroDivisionError` en tiempo de ejecución.

**Corrección:** Validar antes de dividir, retornando `0` como promedio cuando no hay órdenes procesadas.

---

## Bug 2: Mutación del diccionario original

```python
order['final_price'] = final_price
order['status'] = 'processed'
```

**Problema:** Se modifica directamente el diccionario original que viene en la lista `orders`. Esto es un **efecto secundario** peligroso: si el llamador usa la lista original después de invocar esta función, encontrará los datos alterados (estado cambiado a `'processed'` y clave `final_price` añadida).

**Corrección:** Crear una copia superficial de cada orden con `.copy()` antes de modificarla.

---

## Bug 3: `count` incorrecto

```python
'count': len(orders)
```

**Problema:** `len(orders)` cuenta **todas** las órdenes (incluyendo las que no están `'pending'`). El campo `count` debería reflejar cuántas órdenes fueron realmente procesadas.

**Corrección:** Cambiar a `len(processed)`.

---

## Código Corregido

```python
def process_orders(orders):
    total = 0
    processed = []

    for order in orders:
        if order['status'] == 'pending':
            # FIX Bug 2: copiar el diccionario para no mutar el original
            order_copy = order.copy()

            discount = order_copy['total'] * 0.1 if order_copy['total'] > 100 else 0
            final_price = order_copy['total'] - discount

            order_copy['final_price'] = final_price
            order_copy['status'] = 'processed'

            total += final_price
            processed.append(order_copy)

    # FIX Bug 1: proteger contra división por cero
    average = total / len(processed) if len(processed) > 0 else 0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        # FIX Bug 3: contar solo las órdenes procesadas
        'count': len(processed)
    }
```

## Verificación rápida

```python
# Caso sin órdenes pending → ya no rompe
print(process_orders([{'status': 'shipped', 'total': 50}]))
# {'processed': [], 'total': 0, 'average': 0, 'count': 0}

# Caso normal → el original no se muta
original = [{'status': 'pending', 'total': 200}]
result = process_orders(original)
print(original[0])   # {'status': 'pending', 'total': 200}  ← intacto
print(result['count'])  # 1
print(result['average'])  # 180.0
```