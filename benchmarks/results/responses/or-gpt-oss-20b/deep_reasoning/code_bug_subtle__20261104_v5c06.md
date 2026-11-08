# GPT-OSS 20B — deep_reasoning/code_bug_subtle

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 5.6 | quality: 5.0
- latency_total: 43.128s | tokens_per_second: 110.8
- input_tokens: 260 | output_tokens: 4780

## Entrada exacta (lo que recibió el modelo)

**user:**

Este codigo tiene un bug sutil que solo aparece en ciertos casos.
Identificalo sin ejecutar el codigo. Explica exactamente cuando falla y por que.

```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def remove_outliers_and_average(data):
    if len(data) < 3:
        return sum(data) / len(data)

    median = find_median(data)
    mad = find_median([abs(x - median) for x in data])
    threshold = 3 * mad

    filtered = [x for x in data if abs(x - median) <= threshold]
    return sum(filtered) / len(filtered)
```

Hint: piensa en que pasa con datos especificos, no en el algoritmo general.


## Respuesta completa

**Bug**  
El fallo aparece cuando la función recibe una lista vacía (`data == []`).  
En ese caso se llega a la rama

```python
if len(data) < 3:
    return sum(data) / len(data)
```

y `len(data)` vale 0.  
`sum(data)` devuelve 0, pero al dividirlo por `len(data)` se produce una  
`ZeroDivisionError`:

```
ZeroDivisionError: division by zero
```

**Cuándo falla**  
Solo cuando `data` está vacío. Con cualquier otro conjunto de datos (1, 2, 3… elementos) el código funciona correctamente.

**Por qué**  
La condición `len(data) < 3` incluye también el caso `len(data) == 0`.  
Para una lista vacía la media no está definida y la función intenta calcularla
dividiendo por cero.  
Para evitarlo habría que comprobar explícitamente `len(data) == 0` y devolver
por ejemplo `None`, lanzar una excepción propia o manejar el caso de otra manera.

Así, el bug es sutil porque no aparece con los tamaños de datos habituales, pero sí con la entrada “vacía”.