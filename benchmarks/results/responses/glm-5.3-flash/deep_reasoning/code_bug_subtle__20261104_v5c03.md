# GLM 5.3 Flash — deep_reasoning/code_bug_subtle

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 5.02 | quality: 5.0
- latency_total: 158.348s | tokens_per_second: 76.6
- input_tokens: 222 | output_tokens: 12133

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

# El bug: cuando MAD = 0, el filtro colapsa

El problema está en la interacción entre `mad`, `threshold` y el filtro:

```python
mad = find_median([abs(x - median) for x in data])
threshold = 3 * mad
filtered = [x for x in data if abs(x - median) <= threshold]
```

Si **más de la mitad de los valores del dataset son idénticos**, entonces `MAD = 0`, por lo tanto `threshold = 0`, y el filtro se convierte en:

```python
abs(x - median) <= 0   #  →  solo sobreviven valores EXACTAMENTE iguales a la mediana
```

La función degenera en "devolver el valor más frecuente", descartando silenciosamente todo lo demás.

## Cuándo falla exactamente

`MAD = 0` si y solo si **un mismo valor aparece estrictamente más de `n/2` veces**. ¿Por qué?

- Si un valor `v` ocupa más de la mitad de las posiciones, la mediana del dataset es necesariamente `v` (las posiciones centrales del arreglo ordenado caen dentro del bloque de `v`).
- Entonces al menos `⌊n/2⌋ + 1` desviaciones absolutas son `0`, y la mediana de esas desviaciones es `0`.

## Ejemplo paso a paso

```python
remove_outliers_and_average([21.0, 21.0, 21.0, 21.0, 21.0, 21.0, 22.0])
```

1. `median = 21.0`
2. Desviaciones: `[0, 0, 0, 0, 0, 0, 1.0]` → su mediana es `0` → `MAD = 0`
3. `threshold = 3 * 0 = 0`
4. Filtro: solo pasan los `21.0`; el `22.0` se descarta aunque está a solo 1 unidad.
5. Retorna `21.0` en vez de `≈21.14`.

Y no hace falta que sea un outlier: con `[5.0]*60 + [5.1]*40`, el MAD es 0 (60 ceros entre 100 desviaciones), se descartan **los 40 valores legítimos de 5.1**, y la función devuelve `5.0` cuando el promedio real es `5.04`.

## Por qué es sutil

- **Falla en silencio**: no hay excepción; devuelve un número plausible. Peor que un crash.
- **El factor 3× no salva nada**: `3 * 0 = 0`. Todo el margen de seguridad depende de que MAD > 0.
- **Es paradójico**: se usa MAD por ser *robusto*, pero es robusto contra outliers, no contra *empates* (ties). Ante una masa de puntos idénticos, el estimador de escala colapsa a cero.
- **Los tests típicos no lo detectan**: con datos continuos aleatorios (`random.uniform`), la probabilidad de empates exactos es 0. Aparece con datos reales: sensores de baja resolución, enteros, conteos, monedas.

## Fix

```python
mad = find_median([abs(x - median) for x in data])
if mad == 0:
    # Sin dispersión alrededor de la mediana: usar otra medida de escala
    mad = sum(abs(x - median) for x in data) / len(data)
    if mad == 0:        # todos los valores idénticos, nada que filtrar
        return median
threshold = 3 * mad
```

(O alternativamente: si `MAD == 0`, no filtrar y devolver el promedio directo, o usar IQR como respaldo.)

## Casos límite secundarios (menores)

- `remove_outliers_and_average([])` → `ZeroDivisionError` en la rama `len(data) < 3`.
- `find_median([])` llamada directamente → `IndexError` (`sorted_nums[mid - 1]` con lista vacía).
- Si los datos contienen `NaN` en posición media (ej. `[1, float('nan'), 3]`), la mediana puede ser `NaN`, todas las comparaciones del filtro dan `False`, `filtered` queda vacío y estalla el `len(filtered)` en la división.

Pero el bug estructural —el que el código lleva dentro siempre que hay datos repetidos— es el colapso del MAD a cero.