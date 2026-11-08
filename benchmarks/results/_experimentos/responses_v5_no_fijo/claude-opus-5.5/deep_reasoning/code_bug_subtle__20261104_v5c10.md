# Claude Opus 5.5 — deep_reasoning/code_bug_subtle

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.27 | quality: 10.0
- latency_total: 22.055s | tokens_per_second: 103.0
- input_tokens: 340 | output_tokens: 2271

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

# El bug: cuando la MAD vale 0, el umbral desaparece

## Cuándo falla

Falla cuando **más de la mitad de los valores son idénticos**. En ese caso la MAD (mediana de las desviaciones absolutas) vale `0`, así que:

```python
threshold = 3 * mad   # = 0
```

y el filtro se convierte en:

```python
filtered = [x for x in data if abs(x - median) <= 0]
```

Es decir, **solo sobreviven los valores exactamente iguales a la mediana**. Cualquier otro valor se descarta como "outlier", aunque esté muy cerca.

## Ejemplo concreto

```python
data = [10, 10, 10, 11, 12]
```

1. `median = 10`
2. Desviaciones: `[0, 0, 0, 1, 2]`, así que `mad = 0`
3. `threshold = 0`
4. `filtered = [10, 10, 10]`
5. Devuelve **`10.0`**

El promedio correcto es **`10.6`**. Ni 11 ni 12 son outliers, pero se eliminan.

Otro caso más extremo:

```python
[5, 5, 5, 5, 6, 7]   # devuelve 5.0; el promedio real es 5.5
```

## Por qué es sutil

- Con datos continuos y variados (floats de sensores, por ejemplo) casi nunca ocurre, así que los tests típicos pasan.
- No lanza ninguna excepción: **devuelve silenciosamente un resultado incorrecto**.
- Aparece con datos discretos o repetitivos: valoraciones del 1 al 5, conteos enteros, precios redondeados o lecturas saturadas de un sensor. Con esos datos, que la mayoría de los valores coincidan es muy común.

El problema de fondo es que la MAD mide la dispersión de la mitad central de los datos. Si esa mitad no tiene dispersión, el algoritmo concluye que *cualquier* desviación es infinitamente anómala.

## Corrección posible

```python
mad = find_median([abs(x - median) for x in data])
if mad == 0:
    # Sin dispersión robusta: no se puede juzgar qué es outlier.
    # Alternativas: no filtrar, usar la desviación media absoluta,
    # o usar un umbral mínimo (epsilon).
    return sum(data) / len(data)
threshold = 3 * mad
```

La práctica habitual es usar la desviación media absoluta como respaldo cuando la MAD es 0, o escalar la MAD por 1.4826 y aplicar un umbral mínimo.

## Otros problemas menores

- **`data = []`**: la rama `len(data) < 3` ejecuta `sum([]) / 0` y lanza `ZeroDivisionError`.
- **Con `inf`**: por ejemplo `[inf, inf, inf]`. La resta `inf - inf` da `nan`, las comparaciones con `nan` son siempre `False`, `filtered` queda vacío y se produce `ZeroDivisionError` en el `return` final.

Con aritmética normal, `filtered` nunca queda vacío. Incluso con MAD = 0 siempre hay al menos un elemento igual a la mediana. Por eso el bug principal no hace que el programa falle: produce resultados incorrectos en silencio.