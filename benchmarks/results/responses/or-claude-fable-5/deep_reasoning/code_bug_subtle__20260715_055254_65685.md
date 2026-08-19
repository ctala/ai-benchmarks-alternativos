# Claude Fable 5 — deep_reasoning/code_bug_subtle

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 4.5 | quality: 5.0
- latency_total: 25.769s | tokens_per_second: 66.9
- input_tokens: 338 | output_tokens: 1725
- judge_score: 5 | justificación: La respuesta identifica correctamente el bug sutil, explica claramente cuándo y por qué ocurre, y proporciona una solución práctica, mostrando un razonamiento impecable y ofreciendo insights útiles para un emprendedor.

## Respuesta completa

# El bug: MAD = 0 con datos "concentrados"

## Dónde está

```python
mad = find_median([abs(x - median) for x in data])
threshold = 3 * mad
filtered = [x for x in data if abs(x - median) <= threshold]
```

Cuando **la mitad o más de los datos son iguales a la mediana**, la mediana de las desviaciones absolutas (MAD) es **0**. Entonces `threshold = 3 * 0 = 0`, y el filtro se convierte en:

```python
filtered = [x for x in data if abs(x - median) <= 0]  # solo x == median
```

Es decir, **se descartan TODOS los valores distintos a la mediana**, aunque no sean outliers en absoluto.

## Ejemplo concreto de fallo

```python
data = [5, 5, 5, 5, 6, 7]
```

1. `median = 5`
2. Desviaciones: `[0, 0, 0, 0, 1, 2]` → `mad = median([0,0,0,0,1,2]) = 0`
3. `threshold = 0`
4. `filtered = [5, 5, 5, 5]`
5. Retorna `5.0`

Pero el promedio real es `5.5`, y ni `6` ni `7` son outliers. El código **descarta datos válidos silenciosamente** — no hay excepción, solo un resultado incorrecto. Por eso es tan sutil: con datos "normales" (bien dispersos) funciona perfecto.

## Por qué es sutil

- Solo se manifiesta cuando ≥50% de los valores coinciden con la mediana (datos discretos, mediciones repetidas, sensores con poca resolución, etc.).
- No lanza error: devuelve un número plausible.
- El resultado degenera a "devolver la mediana" en lugar de "promedio sin outliers".

## Bug secundario

```python
if len(data) < 3:
    return sum(data) / len(data)
```

Si `data = []`, esto lanza `ZeroDivisionError`. Menos sutil, pero también está.

## Corrección típica

```python
mad = find_median([abs(x - median) for x in data])
if mad == 0:
    return sum(data) / len(data)  # sin dispersión medible, no filtrar
threshold = 3 * mad
```

O usar un umbral mínimo (`threshold = max(3 * mad, epsilon)`) según el dominio de los datos.