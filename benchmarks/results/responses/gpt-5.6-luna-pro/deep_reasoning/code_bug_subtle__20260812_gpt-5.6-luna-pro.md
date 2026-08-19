# GPT-5.6 Luna Pro — deep_reasoning/code_bug_subtle

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 3.49 | quality: 2.5
- latency_total: 35.825s | tokens_per_second: 166.1
- input_tokens: 7883 | output_tokens: 5950

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

El fallo ocurre cuando `data` está vacío:

```python
remove_outliers_and_average([])
```

Como `len(data) < 3`, se ejecuta directamente:

```python
return sum(data) / len(data)
```

Para una lista vacía:

- `sum([])` vale `0`
- `len([])` vale `0`

Por tanto, se intenta calcular `0 / 0`, lo que produce:

```python
ZeroDivisionError: division by zero
```

El caso de una lista con uno o dos elementos sí funciona, porque el denominador es distinto de cero.

Una corrección sería tratar explícitamente el caso vacío:

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

Con números reales finitos, `filtered` no queda vacío: por la propia definición de la mediana siempre hay al menos algunos valores cuya desviación es como máximo el MAD.