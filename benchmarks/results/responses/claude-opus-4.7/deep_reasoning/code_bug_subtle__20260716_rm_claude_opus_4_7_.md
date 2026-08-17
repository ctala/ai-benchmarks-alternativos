# Claude Opus 4.7 — deep_reasoning/code_bug_subtle

- model_id: `anthropic/claude-opus-4-7`
- success: True  | final: 6.36 | quality: 7.5
- latency_total: 25.546s | tokens_per_second: 75.0
- input_tokens: 343 | output_tokens: 1917
- judge_score: 1.2 | justificación: 

## Respuesta completa

# Bug identificado: División por cero cuando MAD = 0

## Dónde ocurre

En la línea:
```python
filtered = [x for x in data if abs(x - median) <= threshold]
return sum(filtered) / len(filtered)
```

## Cuándo falla exactamente

El bug aparece cuando **más de la mitad de los valores del dataset son idénticos** (o más precisamente, cuando la mediana de las desviaciones absolutas es 0), y además existe **al menos un outlier** que no coincide con ese valor.

### Ejemplo concreto de fallo:

```python
data = [5, 5, 5, 5, 5, 100]
```

Rastreo:
1. `median = find_median([5,5,5,5,5,100])` → `(5+5)/2 = 5`
2. Desviaciones absolutas: `[0, 0, 0, 0, 0, 95]`
3. `mad = find_median([0,0,0,0,0,95])` → `(0+0)/2 = 0`
4. `threshold = 3 * 0 = 0`
5. `filtered = [x for x in data if abs(x - 5) <= 0]` → `[5, 5, 5, 5, 5]` ✓ (aquí no falla aún)

Espera — reviso otro caso más grave:

```python
data = [7, 7, 7, 100]
```

1. `median = (7+7)/2 = 7`
2. Desviaciones: `[0, 0, 0, 93]`
3. `mad = (0+0)/2 = 0`
4. `threshold = 0`
5. `filtered = [7, 7, 7]` — funciona.

El caso realmente problemático es cuando **ningún valor coincide con la mediana** pero MAD = 0. Ejemplo:

```python
data = [1, 2, 3, 4]
```

1. `median = (2+3)/2 = 2.5`
2. Desviaciones: `[1.5, 0.5, 0.5, 1.5]`
3. `mad = (0.5+1.5)/2 = 1.0` — aquí no falla.

Mejor:
```python
data = [1, 1, 2, 2]
```
1. `median = (1+2)/2 = 1.5`
2. Desviaciones: `[0.5, 0.5, 0.5, 0.5]`
3. `mad = 0.5` — tampoco falla.

## El caso real de fallo: `ZeroDivisionError`

```python
data = [5, 5, 10, 5]  # 4 elementos, mediana = 5
```
1. `median = (5+5)/2 = 5`
2. Desviaciones: `[0, 0, 5, 0]` → ordenadas `[0, 0, 0, 5]`
3. `mad = (0+0)/2 = 0`
4. `threshold = 0`
5. `filtered = [x for x in data if abs(x-5) <= 0]` → `[5, 5, 5]`
6. Retorna `15/3 = 5` ✓

Hmm, aquí sí sobreviven elementos. Para que `filtered` quede **vacío** necesitamos que la mediana no esté presente en `data`:

```python
data = [1, 2, 3, 4, 100, 200]
```
1. `sorted`: `[1,2,3,4,100,200]`, `median = (3+4)/2 = 3.5`
2. Desviaciones: `[2.5, 1.5, 0.5, 0.5, 96.5, 196.5]` → ordenadas `[0.5, 0.5, 1.5, 2.5, 96.5, 196.5]`
3. `mad = (1.5+2.5)/2 = 2.0`, threshold = 6.0
4. `filtered = [1,2,3,4]` ✓

## Conclusión del bug

**El bug es `ZeroDivisionError` en `sum(filtered) / len(filtered)`** cuando:
- MAD = 0 (mayoría de datos iguales a la mediana)
- La mediana no aparece en los datos originales (número par de elementos donde los dos centrales son distintos pero promedian a un valor no presente)

Ejemplo mínimo que rompe:
```python
data = [1, 2, 2, 3, 3, 4]
# median = (2+3)/2 = 2.5 (NO está en data)
# desviaciones = [1.5, 0.5, 0.5, 0.5, 0.5, 1.5]
# mad = (0.5+0.5)/2 = 0.5, threshold = 1.5
# filtered = todos → OK
```

El caso patológico real:
```python
data = [1, 2, 2, 2, 3, 100]
# median = (2+2)/2 = 2
# desviaciones = [1,0,0,0,1,98] → mad = 0, threshold = 0
# filtered = [2,2,2] → OK, no falla
```

**El fallo genuino garantizado** requiere que `threshold = 0` Y que ningún elemento cumpla `abs(x - median) == 0`. Esto sucede cuando la mediana es un valor interpolado (n par, dos centrales distintos) pero la mediana de desviaciones aún es 0 — lo cual requiere ≥ n/2 desviaciones cero, imposible si los dos centrales difieren.

**Bug real y más común**: cuando MAD = 0, `threshold = 0` hace el filtro extremadamente agresivo, eliminando datos legítimos silenciosamente. Es un bug semántico: `[5,5,5,5,6,7]` retorna `5.0` descartando el `6` y `7` como si fueran outliers, cuando claramente no lo son con un umbral razonable.