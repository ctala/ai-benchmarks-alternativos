# GLM 5.3 — deep_reasoning/code_bug_subtle

- model_id: `z-ai/glm-5.3`
- success: True  | final: 4.5 | quality: 5.0
- latency_total: 251.769s | tokens_per_second: 79.9
- input_tokens: 222 | output_tokens: 20109

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

# El bug: cuando hay un "valor mayoritario", MAD = 0 y el filtro se degenera

**Condición exacta de fallo:** `len(data) >= 3` **y más de la mitad de los elementos son idénticos entre sí** (existe un valor que aparece más de `n/2` veces), con al menos un elemento distinto. Esto es exactamente equivalente a que `mad == 0`.

En ese caso, la función clasifica como *outlier* a **todo valor diferente de la mediana, sin importar qué tan cerca esté**, y devuelve como "promedio" simplemente el valor mayoritario.

## Traza con el dato mínimo: `[1, 1, 2]`

1. `median = 1`
2. Desviaciones absolutas: `[0, 0, 1]`
3. `mad = find_median([0, 0, 1])` = **0**
4. `threshold = 3 * 0` = **0**
5. `filtered = [x for x in data if abs(x - 1) <= 0]` → `[1, 1]` (el 2 queda fuera: `|2-1| = 1 > 0`)
6. Retorna `1.0`

No hay ningún outlier real en `[1, 1, 2]` — el 2 es un dato perfectamente normal — y aun así se elimina en silencio. El promedio real es ≈1.33.

## Por qué ocurre

MAD es la **mediana** de las desviaciones absolutas. Si más de la mitad de los puntos coinciden, más de la mitad de las desviaciones son exactamente `0`, y la mediana de las desviaciones es `0`. El factor 3 es un multiplicador de "tolerancia" (3 MADs), pero **3 × 0 = 0**: la tolerancia colapsa a cero y el criterio `abs(x - median) <= 0` solo admite copias exactas de la mediana.

## Por qué es sutil

- **No crashea:** cuando MAD = 0, la mediana siempre es uno de los datos, así que `filtered` nunca queda vacío y la división final siempre funciona. (Puedes demostrar que `filtered` jamás puede ser vacío: con MAD > 0, al menos la mitad de las desviaciones son ≤ MAD < 3·MAD.)
- **La salida se ve plausible** (es simplemente el valor repetido).
- **Con datos "de libro" funciona perfecto:** `[1, 2, 3, 4, 100]` → mediana 3, MAD 1, umbral 3, filtra el 100, devuelve 2.5. ✓
- **El patrón disparador es común en datos reales:** sensores trabados en una lectura, ceros en datos de conteo, valores redondeados/cuantizados, escalas discretas.

Otros ejemplos:

- `[5.0, 5.0, 5.0, 5.0, 5.1]` → `5.0` (el 5.1 no es outlier, pero se descarta).
- `[0, 0, 0, 1, 1]` → `0.0` (descarta el 40% de los datos sin que haya outlier alguno; media real 0.4).
- **Caso invertido:** `[100, 100, 100, 1, 2]` → mediana 100, MAD 0, devuelve `100.0`: *conserva* los outliers (que son mayoría) y *borra* los datos buenos.

## Fix

```python
mad = find_median([abs(x - median) for x in data])
if mad == 0:
    # Sin dispersión medible: el umbral degeneraría en 0
    # y borraría todo lo distinto de la mediana.
    return sum(data) / len(data)  # o caer a otro criterio (IQR, desv. estándar...)
threshold = 3 * mad
```

---

**Nota aparte** (bug adicional, pero burdo, no sutil): `remove_outliers_and_average([])` revienta con `ZeroDivisionError` en la rama `len(data) < 3`, porque hace `sum([]) / len([])` = 0/0. Ese falla ruidosamente; el de MAD = 0 falla en silencio, y eso es lo que lo hace peligroso.