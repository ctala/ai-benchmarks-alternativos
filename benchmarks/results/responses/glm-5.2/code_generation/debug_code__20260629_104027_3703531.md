# GLM 5.2 — code_generation/debug_code

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.17 | quality: 9.16
- latency_total: 8.62s | tokens_per_second: 97.0
- input_tokens: 231 | output_tokens: 836
- judge_score: 4.4 | justificación: 

## Respuesta completa

El código tiene tres bugs principales que deben corregirse:

1. **División por cero**: Si no hay órdenes con `status == 'pending'`, la lista `processed` quedará vacía y `len(processed)` será `0`. Al calcular `average = total / len(processed)` se produce una excepción `ZeroDivisionError`.  
2. **Mutación del diccionario original**: Se modifican directamente los diccionarios de la lista `orders` (`order['final_price'] = ...` y `order['status'] = ...`). Esto altera los datos de entrada, lo cual es un efecto secundario no deseado.  
3. **`count` incorrecto**: Se devuelve `len(orders)` (todas las órdenes) en lugar de `len(processed)` (solo las procesadas). El campo debería reflejar cuántas órdenes se procesaron realmente.

### Versión corregida

```python
def process_orders(orders):
    total = 0
    processed = []
    for order in orders:
        if order['status'] == 'pending':
            # Copia superficial para no mutar el original
            order_copy = order.copy()
            discount = order_copy['total'] * 0.1 if order_copy['total'] > 100 else 0
            final_price = order_copy['total'] - discount
            order_copy['final_price'] = final_price
            order_copy['status'] = 'processed'
            total += final_price
            processed.append(order_copy)

    # Evitar división por cero
    average = total / len(processed) if processed else 0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': len(processed)   # ahora cuenta solo las procesadas
    }
```

**Notas adicionales**:
- Si los diccionarios de orden contienen estructuras anidadas (listas, otros dicts), se debería usar `copy.deepcopy(order)` en lugar de `order.copy()` para evitar mutaciones indirectas.
- Se ha optado por devolver `average = 0` cuando no hay órdenes procesadas; esto puede ajustarse a `None` u otro valor según el requisito.