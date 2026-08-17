# Kimi K3 — deep_reasoning/code_bug_subtle

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.06 | quality: 7.5
- latency_total: 214.904s | tokens_per_second: 32.7
- input_tokens: 308 | output_tokens: 7033
- judge_score: 1.4 | justificación: 

## Respuesta completa

# El bug: cuando MAD = 0, el umbral colapsa a cero

El problema está en esta línea:

```python
threshold = 3 * mad
```

Si `mad == 0`, entonces `threshold == 0`, y el filtro se convierte en:

```python
filtered = [x for x in data if abs(x - median) <= 0]
```

Es decir: **solo sobreviven los valores exactamente iguales a la mediana**. Todo lo demás —sin importar qué tan cerca esté— se clasifica como outlier.

## ¿Cuándo ocurre exactamente?

`mad = 0` sucede cuando **más de la mitad de los valores son idénticos** (lo cual fuerza a que ese valor repetido sea la mediana, y que la mediana de las desviaciones sea 0).

## Trazado con datos concretos

```python
remove_outliers_and_average([1, 1, 1, 2])
```

1. `median = 1`
2. Desviaciones: `[0, 0, 0, 1]`
3. `mad = find_median([0, 0, 0, 1]) = 0`
4. `threshold = 0`
5. `filtered = [1, 1, 1]` ← el `2` fue eliminado
6. Retorna `1.0`

El valor `2` **no es un outlier** en `[1, 1, 1, 2]`, pero la función lo descarta silenciosamente. Con `[10, 10, 10, 11]` pasa igual: un valor a solo 1 unidad de distancia se trata como si fuera `1000000`.

El caso mínimo que lo dispara es incluso `[1, 1, 2]` → retorna `1.0` en lugar de `1.33`.

## Por qué es sutil

1. **No lanza excepción**: retorna un número perfectamente válido (el valor repetido), así que el error pasa desapercibido.
2. **A veces "funciona" por accidente**: con `[5, 5, 5, 5, 5, 500]` el outlier real sí se elimina correctamente, lo que oculta el bug en muchos tests.
3. **El código se ve correcto**: el algoritmo MAD con factor 3 es estándar; el problema es que el MAD como estimador de escala se rompe cuando es 0 — la ventana de aceptación colapsa a un punto y el método pierde toda noción de escala (no distingue 0.001 de distancia de 10⁶).

## La corrección

Hay que manejar explícitamente el caso `mad == 0`:

```python
if mad == 0:
    # No hay escala para detectar outliers; no filtrar
    return sum(data) / len(data)
```

(o usar un fallback como la desviación absoluta media, o un epsilon).

## Bonus: un segundo bug

`remove_outliers_and_average([])` lanza `ZeroDivisionError`, porque el guard `len(data) < 3` incluye el caso `len(data) == 0` y luego divide por `len(data)`. Menos sutil, pero también está ahí.