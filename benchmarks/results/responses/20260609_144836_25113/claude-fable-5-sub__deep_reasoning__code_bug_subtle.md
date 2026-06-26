# Claude Fable 5 (suscripción) — deep_reasoning/code_bug_subtle

- model_id: `claude-fable-5`
- success: True  | final: 6.38 | quality: 8.5
- latency_total: 28.817s | tokens_per_second: 73.8
- input_tokens: 2 | output_tokens: 2127

## Respuesta completa

## El bug: MAD = 0 cuando la mayoría de los valores son iguales a la mediana

El algoritmo (filtro por MAD, Median Absolute Deviation) es correcto en general, pero tiene un caso degenerado clásico:

**Si al menos la mitad de los datos son idénticos a la mediana, el MAD es 0.**

Sigamos el flujo con `data = [5, 5, 5, 5, 6, 7]`:

1. `median = 5`
2. Desviaciones: `[0, 0, 0, 0, 1, 2]`
3. `mad = find_median([0, 0, 0, 0, 1, 2])` → mediana de los dos del medio = `(0+0)/2` = **0**
4. `threshold = 3 * 0 = 0`
5. `filtered = [x for x in data if abs(x - 5) <= 0]` → **solo sobreviven los valores exactamente iguales a 5**
6. Retorna `5.0`

El `6` y el `7` **no son outliers** — están a 1 y 2 unidades de la mediana en un dataset cuyo rango es 2 — pero el filtro los descarta igual. El resultado correcto (promedio sin outliers reales) sería `5.5`, no `5.0`.

### Por qué es sutil

- Con datos "normales" (variabilidad distribuida) el MAD nunca es 0 y la función se comporta perfectamente. Pasa cualquier test con datos aleatorios continuos.
- Solo falla con datos de **baja varianza con valores repetidos** — exactamente el tipo de datos que aparece en producción (mediciones discretas, sensores con resolución limitada, ratings, conteos).
- No lanza excepción ni produce `NaN`: retorna un número plausible pero **silenciosamente sesgado**, que es lo peor que puede hacer un bug.
- Caso extremo: `[5, 5, 5, 100]` → MAD = 0, descarta el 100 (correcto por suerte). Pero `[5, 5, 5, 5.1]` → también descarta el 5.1, que claramente no es outlier.

Nota: nunca llega a `ZeroDivisionError` en la división final, porque `abs(x - median) <= 0` siempre se cumple para los valores iguales a la mediana, así que `filtered` nunca queda vacío en este caso (con n par y la mediana fuera del dataset, igual sobrevive el punto más cercano porque `MAD >= desviación_mínima`).

### Bug secundario

`remove_outliers_and_average([])` → entra al branch `len(data) < 3` → `sum([]) / len([])` → **ZeroDivisionError**. Lista vacía no está manejada.

### Fix típico

```python
mad = find_median([abs(x - median) for x in data])
if mad == 0:
    return sum(data) / len(data)  # o usar fallback: desviación estándar / IQR
```

La convención estándar (scipy/statsmodels) es: si MAD = 0, no se puede usar como escala robusta y hay que caer a otro estimador o no filtrar.