# GPT-6.1 Terra — deep_reasoning/code_bug_subtle

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 6.79 | quality: 7.5
- latency_total: 13.104s | tokens_per_second: 80.6
- input_tokens: 212 | output_tokens: 1056

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

El caso sutil es **MAD igual a cero**. Por ejemplo:

```python
data = [10, 10, 10, 11, 12]
```

La mediana es `10` y las desviaciones son `[0, 0, 0, 1, 2]`. Su mediana, el MAD, es `0`, así que el umbral también es `0`. El filtro conserva únicamente los valores exactamente iguales a `10` y devuelve `10.0`; descarta incluso `11` y `12`.

Con datos reales finitos, el MAD es cero cuando **más de la mitad de los valores son iguales a la mediana**. Si además hay valores distintos, todos ellos se eliminan, por cercanos que sean. Esto puede ser indeseado para datos con muchos valores repetidos, aunque el resultado sí es coherente con la regla implementada: sin una especificación de qué debe considerarse *outlier*, no puede afirmarse que siempre sea incorrecto.

Hay también un fallo inequívoco: con `data = []`, la primera rama intenta calcular `0 / 0` y lanza `ZeroDivisionError`. En cambio, para datos no vacíos y finitos, un MAD de cero **no deja el filtro vacío**: conserva al menos los valores iguales a la mediana.

Una corrección para el caso degenerado requiere decidir qué hacer cuando `mad == 0`, por ejemplo conservar todos los datos o aplicar otro criterio; no existe una solución universal sin conocer el contexto.