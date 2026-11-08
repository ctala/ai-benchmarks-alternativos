# GPT-6 Astra — deep_reasoning/code_bug_subtle

- model_id: `openai/gpt-6-astra`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 18.95s | tokens_per_second: 37.7
- input_tokens: 212 | output_tokens: 714

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

El caso sutil es **`mad == 0`**: el filtro pierde toda tolerancia y conserva únicamente los valores exactamente iguales a la mediana.

Por ejemplo:

```python
data = [10, 10, 10, 11, 12]
```

Sin ejecutar nada, se obtiene:

```text
median     = 10
desviaciones = [0, 0, 0, 1, 2]
mad        = 0
threshold  = 0
filtered   = [10, 10, 10]
resultado  = 10.0
```

Así, se eliminan `11` y `12` aunque sus diferencias sean pequeñas. Para datos finitos y con aritmética exacta, esto sucede cuando **más de la mitad de los valores coinciden**: más de la mitad de las desviaciones son cero y, por tanto, su mediana también.

**Matiz importante:** esto no provoca por sí mismo una división entre cero. Los valores iguales a la mediana cumplen `0 <= 0` y permanecen en `filtered`. Es una degeneración del criterio estadístico, no necesariamente un resultado incorrecto: depende de qué quieras considerar un atípico. Falta definir una política para ese caso.

Hay, además, dos fallos de ejecución concretos:

- **Entrada vacía:** `remove_outliers_and_average([])` entra en la primera rama y calcula `0 / 0`, provocando `ZeroDivisionError`.
- **Valores `NaN`:** por ejemplo, `[float("nan")] * 3` produce una mediana y un umbral `NaN`. Como las comparaciones `<=` con `NaN` son falsas, `filtered` queda vacío y la última línea provoca `ZeroDivisionError`.

En resumen: si la pista apunta a muchos valores repetidos, el problema es el **umbral cero por MAD cero**, no que desaparezcan todos los elementos. Una corrección requiere decidir explícitamente qué hacer cuando `mad == 0`, además de validar la entrada.