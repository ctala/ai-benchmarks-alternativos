# GPT-OSS 120B — deep_reasoning/code_bug_subtle

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 3.62 | quality: 2.5
- latency_total: 84.754s | tokens_per_second: 31.1
- input_tokens: 260 | output_tokens: 2634

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

**Resumen del fallo**

El código explota cuando la lista que se le pasa a `remove_outliers_and_average` está vacía:

```python
>>> remove_outliers_and_average([])
ZeroDivisionError: division by zero
```

El error se produce porque la rama “*caso pequeño*” (`len(data) < 3`) supone que siempre hay al menos un elemento y hace:

```python
return sum(data) / len(data)     # ← len(data) es 0
```

Dividir por cero lanza `ZeroDivisionError`.  
Aunque el resto del algoritmo (cálculo de la mediana, del MAD, etc.) también fallaría con una lista vacía, el punto donde el programa se rompe primero es ese `return` de la rama corta.

---

## Por qué el resto del algoritmo no ayuda

* `find_median([])` también produciría un `IndexError` (`sorted_nums[mid]` con una lista vacía), pero esa función **nunca se llama** cuando `len(data) == 0` porque la rama `if len(data) < 3` se ejecuta antes.
* En cualquier caso donde la lista tenga al menos un elemento (aunque sea 1 o 2) la división es segura, porque `len(data)` será 1 o 2 y el promedio está bien definido.

---

## Cuándo exactamente falla

| Entrada                     | Longitud | Rama que se ejecuta | Operación que falla                |
|-----------------------------|----------|----------------------|------------------------------------|
| `[]`                         | 0        | `if len(data) < 3:`  | `sum(data) / len(data)` → 0/0     |
| Cualquier otra lista vacía  | 0        | idem                 | idem                               |

Cualquier otro caso (1 elemento, 2 elementos, 3 o más) funciona sin lanzar excepción.

---

## Cómo arreglarlo

Hay varias formas simples de prevenir el error:

```python
def remove_outliers_and_average(data):
    if not data:                     # <-- caso vacío
        raise ValueError("La lista no puede estar vacía")
        # o bien: return 0.0  (dependiendo de lo que se quiera)
    
    if len(data) < 3:
        return sum(data) / len(data)

    # resto del algoritmo …
```

Otra alternativa es devolver `float('nan')` o cualquier valor “neutral” que tenga sentido en el contexto de la aplicación.

---

### Conclusión

El **bug sutil** no está en la lógica estadística (mediana, MAD, umbral) sino en la **asunción implícita de que la lista nunca está vacía**. Cuando esa asunción se rompe, el cálculo del promedio en la rama “*menos de tres elementos*” provoca una división por cero. Detectar y manejar explícitamente la lista vacía elimina el fallo.