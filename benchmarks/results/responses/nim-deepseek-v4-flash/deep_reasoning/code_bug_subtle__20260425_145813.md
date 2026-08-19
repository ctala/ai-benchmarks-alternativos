# DeepSeek V4 Flash (NIM) — deep_reasoning/code_bug_subtle

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 6.56 | quality: 6.73
- latency_total: 14.721s | tokens_per_second: 38.5
- input_tokens: 225 | output_tokens: 567
- judge_score: 3.8 | justificación: 

## Respuesta completa

El bug está en la línea:

```python
mad = find_median([abs(x - median) for x in data])
```

**¿Cuándo falla?**  
Falla cuando todos los valores en `data` son exactamente iguales. Por ejemplo: `data = [5, 5, 5]`.

**Explicación paso a paso:**

1. `find_median([5, 5, 5])` → mediana = 5
2. `[abs(x - 5) for x in data]` → `[0, 0, 0]`
3. `find_median([0, 0, 0])` → mediana = 0
4. `mad = 0`
5. `threshold = 3 * 0 = 0`
6. `filtered = [x for x in data if abs(x - 5) <= 0]` → `[5, 5, 5]` (se conservan todos)
7. `sum(filtered) / len(filtered)` → `15 / 3 = 5` → **esto funciona bien**

**Pero el error real ocurre cuando hay un outlier extremo que hace que MAD sea 0 aunque no todos los datos sean iguales.**  
Ejemplo: `data = [1, 1, 1, 1000]`

1. Mediana = 1
2. Desviaciones absolutas: `[0, 0, 0, 999]`
3. Mediana de esas desviaciones = 0 (porque la mitad de los valores son 0)
4. `threshold = 0`
5. `filtered = [x for x in data if abs(x - 1) <= 0]` → `[1, 1, 1]`
6. Se descarta el 1000 completamente
7. Resultado: 1.0

**El bug sutil:**  
Cuando la mediana de las desviaciones absolutas (MAD) es 0, el threshold se vuelve 0, y se filtran **todos** los puntos que no sean exactamente iguales a la mediana. Esto puede descartar datos legítimos que simplemente están algo alejados, dejando solo los valores repetidos, lo que da una falsa impresión de que no hay variabilidad.

**Condición exacta de fallo:**  
El bug aparece cuando más de la mitad de los datos tienen el mismo valor (el valor de la mediana), haciendo que MAD = 0, y luego se descartan todos los demás puntos por más cercanos que estén.