# GPT-5.4 — deep_reasoning/code_bug_subtle

- model_id: `gpt-5.4`
- success: True  | final: 6.44 | quality: 6.11
- latency_total: 14.663s | tokens_per_second: 74.3
- input_tokens: 212 | output_tokens: 1090
- judge_score: 2.6 | justificación: 

## Respuesta completa

El bug sutil está en `remove_outliers_and_average`, específicamente en esta parte:

```python
mad = find_median([abs(x - median) for x in data])
threshold = 3 * mad

filtered = [x for x in data if abs(x - median) <= threshold]
return sum(filtered) / len(filtered)
```

## Cuándo falla

Falla cuando el `mad` vale `0`.

Eso ocurre en ciertos conjuntos de datos donde **la mediana existe, pero al menos la mitad de las distancias a la mediana son 0**. En la práctica, pasa cuando muchos valores son iguales a la mediana.

### Ejemplo típico

```python
data = [10, 10, 10, 10, 100]
```

- `median = 10`
- Desviaciones absolutas: `[0, 0, 0, 0, 90]`
- La mediana de esas desviaciones (`mad`) es `0`
- Entonces `threshold = 3 * 0 = 0`

El filtrado queda:

```python
filtered = [x for x in data if abs(x - 10) <= 0]
```

o sea:

```python
filtered = [10, 10, 10, 10]
```

Aquí no falla aún.

---

## El caso exacto donde rompe

Rompe cuando `mad == 0` **y ningún elemento es exactamente igual a la mediana**.

Entonces el umbral es 0, y la condición:

```python
abs(x - median) <= 0
```

solo acepta elementos exactamente iguales a `median`.

Si no hay ninguno, `filtered` queda vacío y esta línea explota:

```python
return sum(filtered) / len(filtered)
```

porque hace división por cero.

---

## Ejemplo concreto

```python
data = [1, 1, 2, 2]
```

Veámoslo:

- `sorted_nums = [1, 1, 2, 2]`
- `n = 4`
- `median = (1 + 2) / 2 = 1.5`

Ahora las desviaciones absolutas:

```python
[abs(1 - 1.5), abs(1 - 1.5), abs(2 - 1.5), abs(2 - 1.5)]
= [0.5, 0.5, 0.5, 0.5]
```

- `mad = 0.5`
- `threshold = 1.5`

Aquí no falla. Así que este no es el caso.

Probemos uno donde `mad = 0` pero la mediana no esté en los datos.

```python
data = [1, 1, 1, 2, 2, 2]
```

- `median = (1 + 2) / 2 = 1.5`
- Desviaciones: `[0.5, 0.5, 0.5, 0.5, 0.5, 0.5]`
- `mad = 0.5`

Tampoco.

Entonces hay que afinar más: para que `mad = 0`, la mediana de las desviaciones debe ser 0, lo que implica que al menos la mitad de los elementos tienen desviación 0. Pero si la desviación es 0, entonces esos elementos son exactamente iguales a la mediana. Eso significa que si `mad = 0`, **sí tiene que haber elementos iguales a la mediana**.

Por tanto, el bug no es “`mad == 0` y no hay elementos iguales a la mediana”, porque eso realmente no puede ocurrir.

---

## Entonces, ¿cuál es el bug real?

El bug sutil está en el caso:

```python
if len(data) < 3:
    return sum(data) / len(data)
```

Si `data` es una lista vacía:

```python
data = []
```

entonces entra en:

```python
if len(data) < 3:
    return sum(data) / len(data)
```

y hace:

```python
0 / 0
```

lo que produce `ZeroDivisionError`.

---

## Por qué es sutil

Porque:

- Para listas de tamaño 1 o 2 funciona.
- Para la mayoría de entradas “normales” de tamaño mayor también funciona.
- Solo falla con un caso específico: `data = []`.

Y además el resto del código parece estar pensando en casos estadísticos normales, así que es fácil olvidar la entrada vacía.

---

## Resumen

### Bug
No se maneja el caso de lista vacía.

### Dónde
En:

```python
if len(data) < 3:
    return sum(data) / len(data)
```

### Cuándo falla
Cuando:

```python
data == []
```

### Por qué
Porque intenta dividir entre cero:

```python
sum([]) / len([])  # 0 / 0
```

---

Si quieres, también puedo señalar otro problema menos obvio relacionado con `find_median([])` y cómo blindar ambas funciones correctamente.