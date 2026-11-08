# Mercury 3 — deep_reasoning/code_bug_subtle

- model_id: `inception/mercury-3`
- success: True  | final: 5.25 | quality: 5.0
- latency_total: 17.129s | tokens_per_second: 683.7
- input_tokens: 216 | output_tokens: 11711

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

El bug está en `remove_outliers_and_average` cuando se le pasa una **lista vacía**.

```python
remove_outliers_and_average([])
```

### Por qué falla

La primera condición es:

```python
if len(data) < 3:
    return sum(data) / len(data)
```

Para `data = []`, se cumple `len([]) < 3`, así que intenta ejecutar:

```python
sum([]) / len([])
```

que equivale a:

```python
0 / 0
```

y lanza `ZeroDivisionError`.

La guarda fue pensada para manejar listas pequeñas no vacías (de 1 o 2 elementos), pero no excluye el caso de lista vacía. Es el único caso con datos numéricos finitos en el que la función falla de forma directa.