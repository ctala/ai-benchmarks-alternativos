# Claude Sonnet 4.6 (ultimo Anthropic) — deep_reasoning/code_bug_subtle

- model_id: `anthropic/claude-sonnet-4-6`
- success: True  | final: 4.86 | quality: 5.0
- latency_total: 16.236s | tokens_per_second: 55.4
- input_tokens: 263 | output_tokens: 900
- judge_score: 4.6 | justificación: 

## Respuesta completa

## Bug Identificado

### El problema: División por cero cuando `mad = 0`

Cuando `mad` (Median Absolute Deviation) es `0`, el `threshold` también es `0`.

```python
threshold = 3 * mad  # threshold = 3 * 0 = 0
```

Esto significa que el filtro se convierte en:

```python
filtered = [x for x in data if abs(x - median) <= 0]
```

Lo cual solo conserva elementos **exactamente iguales a la mediana**.

---

### ¿Cuándo ocurre exactamente?

Cuando **más de la mitad de los datos son idénticos**:

```python
remove_outliers_and_average([5, 5, 5, 1, 100])
# La mediana es 5
# MAD = find_median([0, 0, 0, 4, 95]) = 0  ← mayoría son ceros
# threshold = 0
# filtered = [5, 5, 5]  ← funciona aquí por casualidad
```

```python
remove_outliers_and_average([5, 5, 5, 5, 1, 100])
# La mediana es 5
# MAD = find_median([0, 0, 0, 0, 4, 95]) = 0
# threshold = 0
# filtered = [5, 5, 5, 5]  ← sigue funcionando
```

**El caso que ROMPE todo:**

```python
remove_outliers_and_average([5, 5, 5, 5, 5, 5])
# mediana = 5, MAD = 0, threshold = 0
# filtered = [5, 5, 5, 5, 5, 5]  ← ok

remove_outliers_and_average([4, 5, 5, 5, 5, 6])
# mediana = 5, MAD = 0, threshold = 0
# filtered = [5, 5, 5, 5]  ← silenciosamente descarta 4 y 6 ✗
```

### El bug más crítico:

```python
remove_outliers_and_average([1, 2, 3])
# mediana = 2
# MAD = find_median([1, 0, 1]) = 1
# threshold = 3 → ok

remove_outliers_and_average([2, 2, 3])
# mediana = 2
# MAD = find_median([0, 0, 1]) = 0  ← MAD es 0
# threshold = 0
# filtered = [2, 2]  ← el 3 es DESCARTADO silenciosamente
# retorna 2.0 en vez de 2.33...
```

---

### Por qué es sutil

| Característica | Detalle |
|---|---|
| **No lanza excepción** | `filtered` nunca queda vacío si la mediana está en los datos |
| **Retorna un número** | Parece correcto pero es incorrecto |
| **Solo falla con datos "casi uniformes"** | Precisamente cuando menos sospecharías outliers |

---

### Fix

```python
if mad == 0:
    # Usar desviación estándar como fallback, o un threshold absoluto
    std = (sum((x - median)**2 for x in data) / len(data)) ** 0.5
    threshold = 3 * std if std > 0 else float('inf')
else:
    threshold = 3 * mad
```