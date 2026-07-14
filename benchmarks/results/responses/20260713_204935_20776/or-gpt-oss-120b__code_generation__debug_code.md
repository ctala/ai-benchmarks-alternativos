# GPT-OSS 120B — code_generation/debug_code

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 21.892s | tokens_per_second: 45.5
- input_tokens: 283 | output_tokens: 995
- judge_score: 5.0 | justificación: 

## Respuesta completa

**Explicación de los bugs**

| Nº | Descripción del problema | Consecuencia |
|---|---------------------------|--------------|
| 1 | **División por cero**: `average = total / len(processed)` se ejecuta aunque `processed` pueda estar vacío (por ejemplo cuando ninguna orden tiene `status == 'pending'`). | Lanza `ZeroDivisionError` y la función se corta. |
| 2 | **Mutación del diccionario original**: dentro del bucle se modifica directamente `order['final_price']` y `order['status']`. Como `order` es una referencia al mismo objeto que está dentro de la lista `orders` pasada por parámetro, la lista original queda alterada. | El llamador de la función ve sus datos cambiados inesperadamente, lo que rompe la inmutabilidad esperada y puede producir errores en otras partes del programa. |
| 3 | **Campo `count` equivocado**: se devuelve `len(orders)`, que es el número total de órdenes recibidas, pero el requisito (según el comentario) es que `count` indique cuántas órdenes fueron realmente procesadas. | El informe de la función muestra un número que no coincide con la lista `processed`. |

---

## Versión corregida

```python
from copy import deepcopy
from typing import List, Dict, Any

def process_orders(orders: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Procesa las órdenes con estado 'pending'.

    - No modifica la lista/los diccionarios recibidos.
    - Calcula el total, el promedio y la cantidad de órdenes procesadas.
    - Evita división por cero cuando no hay órdenes pendientes.
    """
    total = 0.0
    processed: List[Dict[str, Any]] = []

    for order in orders:
        # Nos aseguramos de que la orden tenga las claves esperadas
        if order.get('status') != 'pending':
            continue

        # Copiamos la orden para no mutar la original
        order_copy = deepcopy(order)

        # Aplicamos el descuento (10 % si total > 100)
        discount = order_copy['total'] * 0.1 if order_copy['total'] > 100 else 0.0
        final_price = order_copy['total'] - discount

        # Guardamos la información calculada
        order_copy['final_price'] = final_price
        order_copy['status'] = 'processed'

        # Acumulamos resultados
        total += final_price
        processed.append(order_copy)

    # Evitamos división por cero
    average = total / len(processed) if processed else 0.0

    return {
        'processed': processed,
        'total': total,
        'average': average,
        'count': len(processed)          # número de órdenes realmente procesadas
    }
```

### Qué se cambió y por qué

1. **Prevención de división por cero**  
   ```python
   average = total / len(processed) if processed else 0.0
   ```
   Si `processed` está vacío, devolvemos `0.0` como promedio (puede ajustarse a `None` si se prefiere).

2. **No mutar el input**  
   - Se usa `deepcopy(order)` para crear una copia completa de cada diccionario antes de modificarlo.  
   - Alternativamente, se podría copiar solo los campos necesarios con `{**order, ...}`; `deepcopy` es más seguro cuando los valores pueden ser objetos mutables (listas, dicts anidados).

3. **`count` correcto**  
   ```python
   'count': len(processed)
   ```
   Ahora el conteo refleja exactamente cuántas órdenes fueron procesadas.

4. **Validaciones menores**  
   - `order.get('status')` evita lanzar `KeyError` si la clave falta.  
   - Se tipa la función (`List[Dict[str, Any]]` → `Dict[str, Any]`) para mayor claridad y para que herramientas de análisis estático (mypy, pyright) ayuden a detectar errores.

5. **Documentación y tipado**  
   Se añadió una docstring y anotaciones de tipos, lo que facilita el mantenimiento y la comprensión del código.

Con estas correcciones la función es segura, predecible y cumple con los requisitos planteados.