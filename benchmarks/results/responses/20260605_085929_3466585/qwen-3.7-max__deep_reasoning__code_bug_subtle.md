# Qwen 3.7 Max — deep_reasoning/code_bug_subtle

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 4.45 | quality: 6.16
- latency_total: 1093.665s | tokens_per_second: 45.2
- input_tokens: 228 | output_tokens: 49449
- judge_score: 3.6 | justificación: 

## Respuesta completa

# Bug identificado: MAD = 0 causa filtrado agresivo e incorrecto

## Cuándo falla

El bug aparece cuando **más de la mitad de los elementos en `data` tienen el mismo valor**.

Por ejemplo, con `data = [5, 5, 5, 5, 6]`:

## Por qué falla — traza paso a paso

```python
data = [5, 5, 5, 5, 6]

# 1. Mediana:
sorted_nums = [5, 5, 5, 5, 6]   →   median = 5

# 2. Desviaciones respecto a la mediana:
[abs(5-5), abs(5-5), abs(5-5), abs(5-5), abs(6-5)]
= [0, 0, 0, 0, 1]

# 3. MAD (mediana de las desviaciones):
sorted = [0, 0, 0, 0, 1]   →   mad = 0   ← AQUÍ ESTÁ EL PROBLEMA

# 4. Umbral:
threshold = 3 * 0 = 0

# 5. Filtrado:
filtered = [x for x in data if abs(x - 5) <= 0]
# Solo los valores exactamente iguales a 5 pasan:
filtered = [5, 5, 5, 5]    ← el 6 fue eliminado

# 6. Resultado:
return 20 / 4 = 5.0
```

## La raíz del problema

Cuando más de la mitad de los datos son idénticos, **la mitad de las desviaciones son 0**, por lo que la mediana de las desviaciones (MAD) es necesariamente **0**. Esto hace que `threshold = 3 * 0 = 0`, y la condición `abs(x - median) <= 0` solo deja pasar valores **exactamente iguales** a la mediana.

Esto es un bug porque elimina valores que **no son verdaderos outliers**. Un caso más claro:

```python
data = [5, 5, 5, 5, 5.1, 5.2, 5.3]
# Resultado: 5.0  (elimina 5.1, 5.2 y 5.3 que claramente no son outliers)
```

## Por qué es sutil

- El algoritmo **parece correcto** en su lógica general.
- No produce un crash, sino un **resultado silenciosamente incorrecto**.
- Solo se manifiesta con un patrón específico de datos (mayoría idéntica).
- La solución requeriría manejar el caso `MAD = 0` explícitamente, por ejemplo usando un umbral mínimo o un método alternativo de detección de outliers cuando la MAD es cero.