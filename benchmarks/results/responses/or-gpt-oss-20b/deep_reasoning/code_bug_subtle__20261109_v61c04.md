# GPT-OSS 20B — deep_reasoning/code_bug_subtle

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 5.67 | quality: 5.0
- latency_total: 23.77s | tokens_per_second: 137.7
- input_tokens: 273 | output_tokens: 3273

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

El “bug” no está en la lógica de la media ni en el cálculo de la mediana, sino en la forma en que se manejan los **datos vacíos**.

```python
def remove_outliers_and_average(data):
    if len(data) < 3:
        return sum(data) / len(data)      # <‑‑ aquí
```

Cuando `data` es una lista vacía (`len(data) == 0`), la condición `len(data) < 3` se cumple y la función intenta devolver

```python
sum([]) / 0     # 0 / 0
```

lo que provoca un `ZeroDivisionError`.  
El caso se escapa a la vista porque la mayoría de las veces se llama con al menos un elemento, pero si por error o por diseño se pasa una lista vacía, la función falla.

**Cuándo ocurre**  
- Sólo cuando se invoca `remove_outliers_and_average([])`.

**Por qué**  
- La función no contempla la posibilidad de que la lista esté vacía; la división por `len(data)` no comprueba que el denominador sea distinto de cero.

**Cómo corregirlo (opcional)**  
```python
def remove_outliers_and_average(data):
    if len(data) == 0:
        raise ValueError("Cannot compute average of an empty dataset")
    if len(data) < 3:
        return sum(data) / len(data)
    ...
```

O simplemente devolver `None` o `float('nan')` para indicar que no hay datos disponibles.