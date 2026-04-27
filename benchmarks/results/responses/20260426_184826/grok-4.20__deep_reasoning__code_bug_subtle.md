# Grok 4.20 — deep_reasoning/code_bug_subtle

- model_id: `x-ai/grok-4.20`
- success: True  | final: 5.99 | quality: 5.68
- latency_total: 10.182s | tokens_per_second: 82.3
- input_tokens: 323 | output_tokens: 838
- judge_score: 3.2 | justificación: 

## Respuesta completa

**El bug sutil está en la función `find_median` cuando se calcula el MAD.**

### ¿Cuándo falla?

Falla **cuando el conjunto de datos tiene un número par de elementos** y se calcula el `mad = find_median(...)` de las desviaciones absolutas.

### ¿Por qué falla?

Mira esta parte del código:

```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2   # ← Aquí está el bug
    else:
        return sorted_nums[mid]
```

Cuando `n` es par, se está haciendo la **media aritmética** de los dos valores centrales. Esto es correcto **si los números son continuos**, pero **en el contexto del MAD (Median Absolute Deviation)**, la convención estadística estándar es usar el **valor central inferior** (o a veces el superior), **no** su promedio.

### Caso concreto donde se rompe:

Imagina este dataset (muy común en datos reales):

```python
data = [1, 2, 2, 3, 4, 10, 100]
```

1. `median = find_median(data)` → `n=7` (impar) → `median = 3` (correcto)
2. Desviaciones absolutas: `[2, 1, 1, 0, 1, 7, 97]`
3. `mad = find_median(...)` → ahora `n=7` (impar) → `mad = 1` (correcto)

Hasta aquí bien.

Pero cambia ligeramente los datos a un caso con **longitud par** en las desviaciones:

```python
data = [1, 1, 2, 3, 10, 100]   # 6 elementos
```

- `median = 2.5` (promedio de 2 y 3)
- Desviaciones absolutas: `[1.5, 1.5, 0.5, 0.5, 7.5, 97.5]`
- Ordenadas: `[0.5, 0.5, 1.5, 1.5, 7.5, 97.5]`
- `n=6` (par) → `mid = 3`
- `mad = (sorted[2] + sorted[3]) / 2 = (1.5 + 1.5)/2 = 1.5`

**El valor correcto estadísticamente** (y el que se usa en casi todas las implementaciones robustas) sería `1.5` o `0.5` según la convención, pero **no** el promedio de los dos centrales en este contexto.

El problema más grave aparece cuando el promedio produce un valor que hace que el filtro `<= threshold` se comporte de forma **inestable o inconsistente** con pequeñas variaciones en los datos.

### La corrección recomendada:

```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        # Convención estándar para MAD: usar el valor inferior (o superior)
        return sorted_nums[mid - 1]   # o sorted_nums[mid], pero ser consistente
    else:
        return sorted_nums[mid]
```

O aún mejor, usar `statistics.median_low()` o `statistics.median_high()` explícitamente cuando se calcula el MAD.

**Resumen**: El bug es que el `find_median` usa promedio en caso par, lo cual es matemáticamente correcto para la mediana de datos, **pero estadísticamente incorrecto/noconsistente** cuando se usa para calcular el MAD. Esto produce comportamientos sutiles y no reproducibles según la paridad de la longitud de los datos.