# Muse Spark 1.3 — deep_reasoning/code_bug_subtle

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 4.92 | quality: 5.0
- latency_total: 34.206s | tokens_per_second: 151.3
- input_tokens: 212 | output_tokens: 5176

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

El bug no está en `find_median`, está en esto:

```python
mad = find_median([abs(x - median) for x in data])
threshold = 3 * mad
filtered = [x for x in data if abs(x - median) <= threshold]
```

En general funciona. Falla silenciosamente - no con excepción, con resultado malo - en un caso específico: **cuando el MAD es 0**.

### Cuando pasa

El MAD es la mediana de las desviaciones absolutas:

```
mad = mediana( |x - mediana| )
```

`mad == 0` cuando **más del 50% de los datos son exactamente iguales a la mediana**.

Eso es muy común: sensores congelados, notas, precios, votos, etc.

Ejemplo mínimo:

```python
data = [10, 10, 10, 10, 20]
```

Traza sin ejecutar:

1. `sorted_nums = [10,10,10,10,20]`, `n=5`, `mid=2`
   `median = sorted_nums[2] = 10`
2. desviaciones = `[0,0,0,0,10]`
   ordenadas = `[0,0,0,0,10]`, `n=5`, `mid=2`
   `mad = 0`
3. `threshold = 3 * 0 = 0`
4. `filtered = [x for x in data if abs(x-10) <= 0]`
   Solo pasa lo que sea `== 10` exacto:
   `filtered = [10,10,10,10]`
5. `return sum(filtered)/len(filtered) = 10.0`

Hasta aquí parece "bien", quitó el 20. El problema se ve con variación normal:

```python
data = [10, 10, 10, 10, 10, 10.1, 10.2]
```

mediana = 10, desviaciones = `[0,0,0,0,0,0.1,0.2]`, mad = 0, threshold = 0, filtered = solo los 10.

`10.1` y `10.2` no son outliers, es ruido normal, pero como `threshold` es 0, **cualquier diferencia mínima, por pequeña que sea, se clasifica como outlier**.

La función deja de hacer un "promedio robusto" y colapsa a:

> devuelve la mediana, ignorando todo lo demás.

### Por qué

Porque `abs(x - median) <= 3*mad` con `mad=0` se convierte en `abs(x - median) <= 0`, es decir `x == median`.

Es sutil porque con datos variados `mad > 0` y el filtro se comporta de forma razonable. Solo colapsa cuando hay una masa puntual >50% idéntica a la mediana, que es justo cuando `find_median` de desviaciones devuelve 0.

El arreglo clásico es proteger ese caso:

```python
if mad == 0:
    return median # o promedio sin filtrar, o usar otro estimador
```

Sin eso, el bug es silencioso: no lanza `ZeroDivisionError` - `filtered` siempre contiene al menos los valores iguales a la mediana - simplemente devuelve un promedio wrong.