# GPT-6 Luna — deep_reasoning/code_bug_subtle

- model_id: `openai/gpt-6-luna`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 27.947s | tokens_per_second: 93.6
- input_tokens: 212 | output_tokens: 2615

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

El caso problemático es que **la MAD puede ser cero** aunque los datos no sean todos iguales.

Si una mayoría estricta de los valores es igual a la mediana —al menos `floor(n/2) + 1` valores—, entonces la mediana de las desviaciones absolutas es `0`. Por tanto:

```python
threshold = 3 * mad  # 0
```

y el filtro conserva únicamente los valores exactamente iguales a la mediana. Cualquier valor distinto se descarta, por pequeño que sea su diferencia.

Por ejemplo, con `[10, 10, 10, 11, 11]`, la mediana es `10` y la MAD es `0`. El filtro elimina los dos `11` y devuelve `10`, aunque no sean necesariamente valores atípicos.

No es un fallo de ejecución: es una degeneración del criterio basado en MAD cuando hay muchos valores repetidos. La solución depende de la política deseada; por ejemplo, tratar explícitamente `mad == 0` y usar otro criterio o decidir no filtrar en ese caso.

Aparte, hay otro caso límite: si `data` está vacía, la primera rama intenta dividir `sum(data)` entre `len(data)`, es decir, entre cero.