# Kimi K2.7 Code — deep_reasoning/code_bug_subtle

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 4.53 | quality: 5.0
- latency_total: 361.211s | tokens_per_second: 59.0
- input_tokens: 230 | output_tokens: 21300

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

El bug está en `remove_outliers_and_average`, no en `find_median`.

### Cuándo falla

Falla cuando un mismo valor aparece en **más de la mitad de los datos** (es una moda mayoritaria).  
Por ejemplo:

```python
remove_outliers_and_average([1, 1, 1, 2, 3])
```

### Por qué falla

1. Si un valor ocupa más del 50 % de las observaciones, ese valor es la mediana.
2. Entonces más de la mitad de las desviaciones `abs(x - median)` son `0`.
3. Como la mediana de esa lista de desviaciones es `0`, se obtiene `mad = 0`.
4. El umbral se anula: `threshold = 3 * 0 = 0`.
5. La condición de filtrado se convierte en:

   ```python
   abs(x - median) <= 0
   ```

   es decir, `x == median`.

En lugar de eliminar valores atípicos por dispersión, el algoritmo conserva solo los valores **exactamente iguales a la mediana** y descarta todo lo demás, aunque esos otros valores sean inliers.

En el ejemplo:

- `median = 1`
- desviaciones: `[0, 0, 0, 1, 2]`
- `mad = 0`
- `threshold = 0`
- filtrado: `[1, 1, 1]`
- resultado: `1.0`

El `2` y el `3` se descartan silenciosamente.

### Otros ejemplos que lo provocan

```python
[5, 5, 5, 6]        # devuelve 5.0, descarta el 6
[0, 0, 0, 1]        # devuelve 0.0, descarta el 1
[1, 1, 2]           # devuelve 1.0, descarta el 2
```

### Corrección

Hay que tratar el caso degenerado `mad == 0`. Cuando la MAD es cero no hay una estimación robusta de escala disponible; se puede recurrir, por ejemplo, a la media directa:

```python
if mad == 0:
    return sum(data) / len(data)
```

o usar otro estimador de dispersión (como el IQR) cuando `mad` se anule.

---

**Nota aparte:** si `data` es una lista vacía, `sum(data) / len(data)` lanzará `ZeroDivisionError`; eso es un chequeo de precondición, no el bug sutil que describe la pregunta.