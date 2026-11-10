# Claude Fable 5.2 — deep_reasoning/code_bug_subtle

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 4.5 | quality: 5.0
- latency_total: 21.592s | tokens_per_second: 98.3
- input_tokens: 340 | output_tokens: 2122

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

## El bug: la MAD vale 0 cuando más de la mitad de los datos son iguales

**Cuándo falla exactamente:** cuando una mayoría estricta de los valores (más del 50 %) son idénticos.

**Por qué:**

1. Si más de la mitad de los valores son iguales a `v`, la mediana es `v`.
2. Las desviaciones `abs(x - median)` son entonces 0 en más de la mitad de los casos, así que la mediana de esas desviaciones (la MAD) también es 0.
3. Por tanto `threshold = 3 * 0 = 0`.
4. El filtro `abs(x - median) <= 0` solo deja pasar los valores exactamente iguales a la mediana. Cualquier otro valor se descarta como outlier, aunque difiera en 0.0001.

**Ejemplo:**

```python
remove_outliers_and_average([10, 10, 10, 10, 11])
```

- mediana = 10
- desviaciones = `[0, 0, 0, 0, 1]`, luego MAD = 0
- threshold = 0
- filtered = `[10, 10, 10, 10]`: el 11 se elimina
- devuelve **10.0**, cuando lo correcto sería **10.2** (el 11 no es un outlier)

Un caso peor es `[0, 0, 0, 1, 1]`, que descarta el 40 % de los datos y devuelve `0.0` en vez de `0.4`.

**Por qué es sutil:** no lanza ninguna excepción. Uno esperaría un `ZeroDivisionError` por `filtered` vacío, pero eso no ocurre con números finitos, porque los valores iguales a la mediana siempre pasan el filtro. La función devuelve un número plausible pero incorrecto. Con datos continuos y variados casi nunca se nota. Aparece con datos redondeados, discretos, de sensores con poca resolución o con muchos valores repetidos.

**Posible arreglo:**

```python
if mad == 0:
    return sum(data) / len(data)   # sin dispersión robusta no se puede filtrar
```

Otra opción es usar una medida de dispersión alternativa (desviación media absoluta, IQR) cuando la MAD sea 0.

**Bug secundario, menos sutil:** con `data = []`, la guarda `len(data) < 3` entra en `sum(data) / len(data)` y lanza `ZeroDivisionError`.