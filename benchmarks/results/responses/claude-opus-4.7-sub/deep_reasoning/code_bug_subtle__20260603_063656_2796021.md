# Claude Opus 4.7 (suscripción) — deep_reasoning/code_bug_subtle

- model_id: `claude-opus-4-7`
- success: True  | final: 3.88 | quality: 3.33
- latency_total: 37.305s | tokens_per_second: 74.9
- input_tokens: 6 | output_tokens: 2793
- judge_score: 1.2 | justificación: 

## Respuesta completa

# Bug: MAD = 0 colapsa el threshold y filtra datos legítimos

## El bug

Cuando **más de la mitad de los valores son idénticos al mediano** (o más exactamente, cuando más de la mitad de las desviaciones absolutas son cero), `mad` vale 0 → `threshold = 3 * 0 = 0` → la condición `abs(x - median) <= 0` solo deja pasar los valores exactamente iguales al mediano. Todos los demás (incluyendo valores perfectamente legítimos) son descartados como "outliers".

## Cuándo falla exactamente

Falla siempre que en `data` haya:

- **n impar**: el elemento del medio de las desviaciones es 0, es decir, **más de la mitad** de los valores son iguales al mediano.
- **n par**: los dos elementos centrales de las desviaciones son 0, es decir, **al menos la mitad** de los valores son iguales al mediano.

## Ejemplo concreto

```python
data = [0, 0, 0, 0, 0, 0, 0, 3, 5, 8]
```

Traza paso a paso:

1. `median = find_median(data)` → 0 (los dos centrales son 0 y 0)
2. Desviaciones: `[0, 0, 0, 0, 0, 0, 0, 3, 5, 8]`
3. `mad = find_median(...)` → **0** (los centrales otra vez son 0 y 0)
4. `threshold = 3 * 0 = 0`
5. `filtered = [x for x in data if abs(x - 0) <= 0]` → `[0, 0, 0, 0, 0, 0, 0]`
6. Retorna `0 / 7 = 0.0`

**Los valores 3, 5 y 8 — que no son outliers en ningún sentido razonable — fueron eliminados**, y la función devuelve 0 en lugar de algo parecido a `1.6` (promedio real).

## Otro caso típico

```python
data = [1, 1, 1, 1, 5, 10, 100]
```

- median = 1, deviations = `[0,0,0,0,4,9,99]`, MAD = 0
- Retorna `1.0`, descartando incluso el `5` y el `10` que claramente no eran outliers extremos respecto al `100`.

## Por qué es sutil

- El algoritmo MAD funciona perfecto en datos "normales" con dispersión > 0.
- Tests con `[1, 2, 3, 4, 5, 100]` pasarían sin problema.
- Solo explota con **datos con muchos repetidos en el centro de la distribución**: sensores que reportan ceros, contadores que se quedan estancados, encuestas con respuesta modal dominante, series con baseline plano + picos esporádicos.
- No tira excepción, no rompe — silenciosamente devuelve un número incorrecto, lo cual es peor.

## Fix idiomático

Detectar `mad == 0` y o bien hacer fallback a desviación estándar / IQR, o saltarse el filtrado:

```python
if mad == 0:
    return sum(data) / len(data)  # o usar std como fallback
```

(El factor `1.4826` para hacer MAD comparable a σ tampoco está, pero eso es elección de diseño, no bug.)