# Tencent Hy4 preview — deep_reasoning/code_bug_subtle

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.47 | quality: 7.5
- latency_total: 183.264s | tokens_per_second: 61.3
- input_tokens: 252 | output_tokens: 11232

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

Asumiendo Python 3 y datos numéricos normales, el bug sutil está aquí:

```python
threshold = 3 * mad
```

cuando `mad == 0`.

Falla cuando **más de la mitad de los valores son exactamente iguales a la mediana**. En ese caso:

```python
median = m
devs = [abs(x - m) for x in data]
mad = 0
threshold = 0
```

Entonces el filtro:

```python
filtered = [x for x in data if abs(x - median) <= threshold]
```

se convierte implícitamente en:

```python
filtered = [x for x in data if x == median]
```

Es decir, **elimina cualquier valor distinto de la mediana**, aunque no sea realmente un outlier.

Ejemplo:

```python
remove_outliers_and_average([1, 1, 1, 2])
```

Cálculo interno:

```python
median = 1
devs = [0, 0, 0, 1]
mad = 0
threshold = 0
filtered = [1, 1, 1]
return 1.0
```

El valor `2` se descarta, aunque no necesariamente sea un outlier.

Condición exacta: si `n = len(data)` y `n >= 3`, el fallo ocurre cuando al menos `n // 2 + 1` elementos son exactamente iguales a la mediana. Equivalentemente: cuando una mayoría estricta de los datos tiene el mismo valor.

Aparte, hay otro caso límite más evidente:

```python
remove_outliers_and_average([])
```

provoca `ZeroDivisionError`, porque entra en:

```python
return sum(data) / len(data)
```

con `len(data) == 0`.