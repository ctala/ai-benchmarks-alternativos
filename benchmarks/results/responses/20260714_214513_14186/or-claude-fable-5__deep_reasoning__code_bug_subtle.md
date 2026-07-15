# Claude Fable 5 — deep_reasoning/code_bug_subtle

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 4.46 | quality: 5.0
- latency_total: 28.636s | tokens_per_second: 71.5
- input_tokens: 338 | output_tokens: 2048
- judge_score: 2.0 | justificación: La respuesta identifica incorrectamente el problema como relacionado con el MAD, que no está presente en el código proporcionado, y no aborda el verdadero bug en la función 'remove_outliers_and_average'.

## Respuesta completa

# El bug: MAD = 0 con datos repetidos

## Dónde está

El problema está en esta línea:

```python
threshold = 3 * mad
```

**Cuando la mitad o más de los datos son idénticos, el MAD (Median Absolute Deviation) vale 0**, y por lo tanto `threshold = 0`. El filtro se convierte en:

```python
filtered = [x for x in data if abs(x - median) <= 0]
```

Es decir: **solo sobreviven los valores exactamente iguales a la mediana**. Todo lo demás se descarta como "outlier", aunque sean valores perfectamente normales.

## Ejemplo concreto donde falla

```python
data = [5, 5, 5, 6, 7]
```

Trazando a mano:
1. `median = 5` (elemento central de `[5, 5, 5, 6, 7]`)
2. Desviaciones absolutas: `[0, 0, 0, 1, 2]`
3. `mad = find_median([0, 0, 0, 1, 2]) = 0` ← aquí colapsa todo
4. `threshold = 3 * 0 = 0`
5. `filtered = [5, 5, 5]` → devuelve `5.0`

El resultado correcto (sin outliers reales) sería `(5+5+5+6+7)/5 = 5.6`. El código descartó el `6` y el `7` como si fueran anomalías, **cuando no lo son**.

## Por qué es sutil

- Con datos "bien distribuidos" (sin muchos duplicados), el MAD nunca es 0 y el código funci