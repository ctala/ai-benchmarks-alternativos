# Gemini 3.1 Flash Lite — deep_reasoning/code_bug_subtle

- model_id: `google/gemini-3.1-flash-lite-preview`
- success: True  | final: 6.07 | quality: 4.34
- latency_total: 4.615s | tokens_per_second: 191.1
- input_tokens: 244 | output_tokens: 882
- judge_score: 1.6 | justificación: 

## Respuesta completa

El bug sutil ocurre cuando la **Desviación Absoluta de la Mediana (MAD) es igual a 0**.

### ¿Cuándo falla?
El código falla cuando **más de la mitad de los elementos del conjunto de datos son idénticos**.

Por ejemplo, si pasas `data = [10, 10, 10, 10, 100]`:
1. `median` será `10`.
2. La lista de diferencias absolutas respecto a la mediana será `[0, 0, 0, 0, 90]`.
3. `mad` (la mediana de esa lista) será `0`.
4. `threshold` será `3 * 0 = 0`.
5. `filtered` será `[x for x in data if abs(x - 10) <= 0]`, lo que resulta en `[10, 10, 10, 10]`.
6. Esto funciona bien aquí, pero **si el conjunto es, por ejemplo, `[10, 10, 10, 100, 100]`**:
   - `median` es `10`.
   - Diferencias: `[0, 0, 0, 90, 90]`.
   - `mad` es `0`.
   - `filtered` será `[x for x in data if abs(x - 10) <= 0]`, es decir, `[10, 10, 10]`.
   - Hasta ahí parece bien, pero imagina un caso donde la mediana no sea uno de los valores repetidos o donde el umbral 0 elimine datos que consideras "válidos".

### El problema crítico (División por cero o sesgo lógico)
El problema real ocurre si **todos los elementos de la lista son iguales** (ej. `[5, 5, 5, 5]`) o si la mayoría son iguales y el `mad` resultante es `0`.

1. **El caso extremo `[5, 5, 5]`**:
   - `mad` es `0`.
   - `filtered` es `[5, 5, 5]`.
   - El resultado es correcto.

2. **El "bug" de lógica de filtrado**:
   Si tienes un conjunto de datos donde la variabilidad es muy baja (pero no inexistente), el `mad` puede ser tan pequeño que el umbral `3 * mad` se vuelve arbitrariamente restrictivo.

   **El error fatal ocurre aquí:**
   Si `data = [1, 1, 1, 1, 100]`:
   - `median = 1`
   - `mad = 0`
   - `threshold = 0`
   - `filtered` termina siendo `[1, 1, 1, 1]` (se elimina el 100).
   - **Pero, ¿qué pasa si el usuario quería conservar los datos?** Al ser `mad = 0`, el umbral es `0`. Esto significa que **cualquier valor que no sea exactamente igual a la mediana es eliminado**, independientemente de qué tan lejos esté.

### En resumen:
El bug es que **si la mediana de las desviaciones absolutas es 0, el filtro se vuelve un filtro de igualdad estricta**. 

Si el conjunto de datos tiene una moda muy fuerte (más del 50% de los datos son iguales), el `mad` se vuelve 0 y el algoritmo descarta automáticamente cualquier valor que sea diferente a la mediana, **incluso si esos valores no son outliers en absoluto**. En un escenario de datos reales, esto causa una pérdida de información masiva y un sesgo estadístico severo.

**Adicionalmente:** Si `filtered` llega a estar vacío (aunque en este código específico es difícil por la lógica de `mad`), ocurriría un `ZeroDivisionError` en `sum(filtered) / len(filtered)`.