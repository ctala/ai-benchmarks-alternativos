# Hermes 4 70B — deep_reasoning/code_bug_subtle

- model_id: `nousresearch/hermes-4-70b`
- success: True  | final: 7.1 | quality: 7.57
- latency_total: 4.34s | tokens_per_second: 70.3
- input_tokens: 235 | output_tokens: 305
- judge_score: 4.4 | justificación: 

## Respuesta completa

El bug ocurre cuando todos los datos son iguales, por ejemplo, `data = [5,5,5,5]`:

1. `find_median` devolverá `5` (promedio en caso de par)
2. `mad` será `find_median([0,0,0,0])` → `0`
3. `threshold = 0`
4. `filtered` será `[x for x in data if abs(x-5) <= 0]` → **lista vacía**
5. `sum(filtered)/len(filtered)` intentará dividir por cero

Esto causa un error de división por cero solo cuando TODOS los datos son idénticos. La condición `len(data) < 3` no evita esto para `n ≥ 3`

---

Solución simple: añadir una condición especial cuando `mad == 0`:

```python
def remove_outliers_and_average(data):
    if len(data) < 3:
        return sum(data) / len(data)

    median = find_median(data)
    mad = find_median([abs(x - median) for x in data])
    threshold = 3 * mad

    if threshold == 0:  # <— Solución
        return median  # Todos los datos son iguales
    
    filtered = [x for x in data if abs(x - median) <= threshold]
    return sum(filtered) / len(filtered)
```