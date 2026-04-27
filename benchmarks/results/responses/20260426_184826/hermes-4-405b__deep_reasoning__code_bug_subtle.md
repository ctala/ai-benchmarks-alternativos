# Hermes 4 405B — deep_reasoning/code_bug_subtle

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 5.74 | quality: 4.4
- latency_total: 13.875s | tokens_per_second: 36.0
- input_tokens: 235 | output_tokens: 499
- judge_score: 2.4 | justificación: 

## Respuesta completa

El bug sutil ocurre cuando el conjunto de datos contiene **valores exactamente iguales al umbral de corte** (3 * MAD), y además, estos valores son **los únicos que superan el umbral**. En esta situación, el filtro los retiene (debido a `<=`), pero si su inclusión/exclusión altera la mediana original, el cálculo del MAD y el threshold se basan en una mediana que ya no representa correctamente el conjunto filtrado.

### Ejemplo concreto:
Supongamos `data = [0, 0, 0, 0, 0, 3.0]`:
1. **Mediana inicial**: 0.0  
2. **MAD**: Mediana de `|x - 0|` → `[0, 0, 0, 0, 0, 3.0]` → **0.0**  
3. **Threshold**: 3 * 0.0 = **0.0**  
4. **Filtro**: Conserva solo los `x` donde `|x - 0| <= 0.0` → `[0, 0, 0, 0, 0]` (el `3.0` se descarta).  

**Problema**: El `3.0` se usó para calcular la mediana inicial (0.0) pero se descarta en el filtrado. Si el `3.0` se excluyera correctamente desde el principio, la mediana sería 0.0 (misma), pero en casos donde su inclusión afecte la mediana, el MAD y el threshold no reflejarían el conjunto final.

### Condición específica de fallo:
- Existen valores **exactamente iguales a `3 * MAD`**.
- Estos valores **no aparecen en el conjunto final** tras el filtrado.
- Su inclusión en el cálculo inicial de la mediana **altera el resultado** respecto a si se hubieran excluido desde el principio.

El algoritmo no actualiza la mediana después del filtrado, asumiendo que la mediana inicial es representativa del conjunto limpio, lo cual no siempre es cierto cuando los outliers exactos al umbral son críticos para el cálculo inicial.