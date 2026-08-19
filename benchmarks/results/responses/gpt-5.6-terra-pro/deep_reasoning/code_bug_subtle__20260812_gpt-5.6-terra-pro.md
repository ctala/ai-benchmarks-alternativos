# GPT-5.6 Terra Pro — deep_reasoning/code_bug_subtle

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 3.06 | quality: 2.5
- latency_total: 35.724s | tokens_per_second: 145.7
- input_tokens: 7045 | output_tokens: 5206

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

El bug principal aparece cuando `data` es una lista vacía:

```python
remove_outliers_and_average([])
```

La condición:

```python
if len(data) < 3:
    return sum(data) / len(data)
```

incluye el caso `len(data) == 0`.

Entonces se evalúa:

```python
sum([]) / len([])
# 0 / 0
```

y Python lanza:

```python
ZeroDivisionError: division by zero
```

No falla con listas de uno o dos elementos:

```python
[5]       # 5 / 1: funciona
[5, 10]   # 15 / 2: funciona
```

Falla exactamente con `[]` en `remove_outliers_and_average`.

Además, si alguien llama directamente a:

```python
find_median([])
```

el fallo es distinto: intenta acceder a `sorted_nums[-1]` y produce `IndexError`.

Una corrección explícita sería:

```python
def remove_outliers_and_average(data):
    if not data:
        raise ValueError("data no puede estar vacío")

    if len(data) < 3:
        return sum(data) / len(data)

    median = find_median(data)
    mad = find_median([abs(x - median) for x in data])
    threshold = 3 * mad

    filtered = [x for x in data if abs(x - median) <= threshold]
    return sum(filtered) / len(filtered)
```

Bajo la suposición de números reales finitos, para una lista no vacía `filtered` no queda vacío: la mediana, o alguno de los valores centrales, siempre queda dentro del umbral. Si se permiten `NaN` o infinitos, pueden aparecer otros casos problemáticos, por ejemplo `[float("nan")] * 3`, porque las comparaciones con `NaN` son siempre falsas y `filtered` puede quedar vacío.