# GPT-6 Luna Pro — deep_reasoning/code_bug_subtle

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 7.02 | quality: 7.5
- latency_total: 57.163s | tokens_per_second: 103.0
- input_tokens: 6830 | output_tokens: 5886

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

El caso sutil es **MAD igual a cero**. Para datos numéricos finitos, si eso ocurre, `threshold` también vale cero y el filtro conserva únicamente los valores exactamente iguales a la mediana. Así, valores distintos —aunque sean variaciones legítimas y no outliers— se descartan todos.

Por ejemplo, con `[1, 1, 2]`:

- La mediana es `1`.
- Las desviaciones absolutas son `[0, 0, 1]`, cuya mediana (MAD) es `0`.
- El umbral es `0`, así que se filtran y conservan solo los `1`.
- La función devuelve `1`, en vez de promediar los datos restantes según otro criterio previsto.

Esto ocurre cuando hay suficientes valores iguales a la mediana para que la mediana de las desviaciones sea cero: al menos la mitad de los datos si la longitud es impar, o más de la mitad si es par.

Además, hay un error independiente: con `data = []`, la rama `len(data) < 3` intenta dividir `0 / 0` y produce `ZeroDivisionError`.