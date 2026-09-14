# Fugu Max — deep_reasoning/code_bug_subtle

- model_id: `sakana/fugu-max`
- success: True  | final: 4.51 | quality: 5.0
- latency_total: 181.452s | tokens_per_second: 76.4
- input_tokens: 379 | output_tokens: 13854

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

El bug está en el manejo del caso `mad == 0`.

Aparece cuando **más de la mitad de los datos son exactamente iguales a la mediana**. En ese caso, las desviaciones absolutas `abs(x - median)` tendrán mayoría de ceros, por lo que su mediana (`mad`) será `0`.

Entonces:

```python
threshold = 3 * mad  # => 0
```

La condición del filtro queda:

```python
abs(x - median) <= 0
```

que solo se cumple si `x == median`. Por tanto, **todos los valores distintos de la mediana se descartan**, aunque no sean atípicos reales.

Ejemplo concreto:

```python
remove_outliers_and_average([5, 5, 5, 6, 7])
```

- `median = 5`
- desviaciones: `[0, 0, 0, 1, 2]`
- `mad = 0`
- `threshold = 0`
- `filtered = [5, 5, 5]`
- resultado: `5.0`

Aquí `6` y `7` se eliminan aunque probablemente no deberían considerarse outliers solo por haber mayoría de `5`s.

Es un fallo lógico/estadístico, no una excepción.