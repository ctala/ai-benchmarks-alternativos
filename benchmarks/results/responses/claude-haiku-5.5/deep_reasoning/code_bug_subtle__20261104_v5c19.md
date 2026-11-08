# Claude Haiku 5.5 — deep_reasoning/code_bug_subtle

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 5.45 | quality: 5.0
- latency_total: 14.548s | tokens_per_second: 194.3
- input_tokens: 340 | output_tokens: 2827

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

## Bug principal: MAD = 0 descarta casi todos los datos

**Cuándo ocurre:** cuando más de la mitad de los valores son idénticos al mediano. Entonces más de la mitad de las desviaciones `|x - median|` son 0, y la mediana de esas desviaciones también es 0.

**Ejemplo:**
```python
remove_outliers_and_average([1, 1, 1, 1, 1, 2, 3])
```

1. `median = 1`
2. Desviaciones: `[0, 0, 0, 0, 0, 1, 2]`
3. `mad = find_median(...) = 0`
4. `threshold = 3 * 0 = 0`
5. `filtered` conserva solo los valores con `abs(x - 1) <= 0`, es decir, los `1`
6. Resultado: `1.0`

Los valores `2` y `3` se descartan aunque no sean necesariamente outliers. Con `threshold = 0`, el filtro se reduce a "igual a la mediana", así que cualquier dato distinto desaparece, sin importar qué tan cerca esté.

**Por qué ocurre:** el umbral `3 * MAD` depende de que el MAD sea una escala de dispersión positiva. Cuando el MAD es 0, el criterio pierde sentido: no hay escala y el filtro se vuelve binario. Esto no produce un error visible, sino un resultado silenciosamente incorrecto, por eso es sutil.

**Corrección posible:** usar un umbral de respaldo cuando el MAD es 0, por ejemplo la media de las desviaciones absolutas, o no filtrar si el MAD es 0. Hay que decidir explícitamente cuál es el comportamiento esperado.

## Bug secundario: lista vacía

```python
remove_outliers_and_average([])
```

`len(data) < 3` es verdadero, así que se ejecuta `sum(data) / len(data)`, que es `0 / 0`. Esto lanza `ZeroDivisionError`. El caso `len == 0` necesita un manejo propio.

## Lo que no falla

El filtrado nunca deja `filtered` vacío. Si el MAD es 0, al menos la mitad de los valores son iguales a la mediana, así que la mediana está en los datos y sobrevive al filtro. Si el MAD es mayor que 0, al menos la mitad de los valores tienen desviación ≤ MAD ≤ threshold, así que también sobreviven. Por eso la división por `len(filtered)` es segura para listas no vacías.