# GPT-5.5 — deep_reasoning/code_bug_subtle

- model_id: `gpt-5.5`
- success: True  | final: 4.89 | quality: 4.26
- latency_total: 53.668s | tokens_per_second: 66.5
- input_tokens: 212 | output_tokens: 3567
- judge_score: 1.6 | justificación: 

## Respuesta completa

El bug sutil está en el caso en que `mad == 0`.

Cuando eso ocurre, esta línea:

```python
threshold = 3 * mad
```

produce:

```python
threshold = 0
```

y entonces el filtro queda así:

```python
filtered = [x for x in data if abs(x - median) <= 0]
```

Es decir: **solo conserva valores exactamente iguales a la mediana**. Cualquier valor distinto, aunque sea mínimamente distinto, se elimina como “outlier”.

Ejemplo:

```python
data = [10, 10, 10, 11]
```

Paso a paso:

```python
median = 10
```

Las desviaciones absolutas son:

```python
[abs(10-10), abs(10-10), abs(10-10), abs(11-10)]
# [0, 0, 0, 1]
```

La mediana de esas desviaciones es:

```python
mad = 0
```

Entonces:

```python
threshold = 3 * 0 = 0
```

Y el filtro conserva solo:

```python
[10, 10, 10]
```

El `11` se elimina, aunque no necesariamente sea un outlier real.

Falla exactamente cuando **más de la mitad de los datos son iguales a la mediana**, porque en ese caso la mediana de las desviaciones absolutas es `0`.

Por ejemplo:

```python
[5, 5, 5, 5.1]
[1, 1, 1, 2]
[100, 100, 100, 101, 102]
```

En todos esos casos `mad == 0`, el umbral se vuelve cero y el algoritmo descarta cualquier valor que no sea exactamente la mediana.

Además, hay otro caso límite más obvio:

```python
remove_outliers_and_average([])
```

entra aquí:

```python
if len(data) < 3:
    return sum(data) / len(data)
```

y hace división por cero. Pero el bug sutil del algoritmo de outliers es el caso `mad == 0`.