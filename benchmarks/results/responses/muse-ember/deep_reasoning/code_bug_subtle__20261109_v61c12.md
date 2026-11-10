# Muse Ember — deep_reasoning/code_bug_subtle

- model_id: `meta/muse-ember`
- success: True  | final: 5.23 | quality: 5.0
- latency_total: 18.279s | tokens_per_second: 505.0
- input_tokens: 213 | output_tokens: 9231

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

El bug está en `remove_outliers_and_average`, no en `find_median`. Es la degeneración del MAD cuando hay muchos valores repetidos.

### Cuándo ocurre

Exactamente cuando **más de la mitad de los datos son idénticos** — y por tanto ese valor es la mediana.

Ejemplo: `[10, 10, 10, 10, 11, 12]`

### Por qué falla

1. La mediana es `10`.
2. Las desviaciones son `[0, 0, 0, 0, 1, 2]`. Como la mayoría son `0`, la mediana de las desviaciones también es `0`:
   `mad = 0`.
3. Entonces `threshold = 3 * mad = 0`.
4. El filtro queda:
   ```python
   [x for x in data if abs(x - median) <= 0]
   ```
   Es decir, solo sobreviven los valores **exactamente iguales a la mediana**. Todo lo demás, por cercano que sea, se clasifica como outlier.

En el ejemplo, `filtered = [10, 10, 10, 10]` y la función devuelve `10.0`, descartando `11` y `12` aunque no son outliers en absoluto. El resultado es la mediana, no la media de los no-outliers.

Es un fallo silencioso: como el filtro usa `<=`, los puntos de la mediana sí pasan y no hay `ZeroDivisionError`, pero el promedio devuelto es incorrecto. En datos sin mayoría repetida, `mad > 0` y el algoritmo funciona como se espera; el bug solo aparece con ese patrón específico de datos.