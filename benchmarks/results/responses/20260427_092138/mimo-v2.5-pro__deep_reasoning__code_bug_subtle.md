# MiMo V2.5-Pro (Xiaomi) — deep_reasoning/code_bug_subtle

- model_id: `mimo-v2.5-pro`
- success: True  | final: 7.25 | quality: 7.57
- latency_total: 34.201s | tokens_per_second: 51.7
- input_tokens: 462 | output_tokens: 1768
- judge_score: 4.4 | justificación: 

## Respuesta completa

# El Bug: MAD igual a cero

## El problema

El bug ocurre cuando **MAD (Median Absolute Deviation) es igual a 0**.

Esto sucede cuando **la mayoría de los datos son iguales a la mediana**. En ese momento:

```
threshold = 3 * 0 = 0
```

Y el filtro se convierte en:

```python
abs(x - median) <= 0  →  solo x == median sobrevive
```

**Todo valor que no sea exactamente la mediana se elimina como "outlier"**, sin importar cuán razonable sea.

## Ejemplo concreto

```python
remove_outliers_and_average([1, 5, 5, 5, 10])
```

Paso a paso:

| Paso | Resultado |
|---|---|
| `median` | **5** |
| Desviaciones absolutas | `[4, 0, 0, 0, 5]` |
| `MAD` | mediana de `[0, 0, 0, 4, 5]` = **0** |
| `threshold` | `3 * 0` = **0** |
| Filtro `abs(x - 5) <= 0` | Solo pasan: `[5, 5, 5]` ❌ |
| Resultado | **5.0** |

Pero el promedio real de los datos es **(1+5+5+5+10)/5 = 5.2**, y claramente `1` no es un outlier.

## ¿Cuándo se activa?

Para **n impar**: cuando al menos `(n//2 + 1)` valores son iguales a la mediana.

```
[1, 5, 5, 5, 10]     → 3 de 5 son iguales a la mediana  ✗
[1, 2, 5, 5, 5, 5, 10] → 4 de 7 son iguales a la mediana  ✗
[10, 10, 10, 10, 10]  → todos iguales, pero filtered = todos → resultado correcto por casualidad
```

## La raíz del problema

La MAD es una medida de dispersión **robusta**, pero cuando los datos tienen una moda muy concentrada, colapsa a cero, haciendo el threshold absurdamente agresivo. Es un caso conocido en estadística robusta.

## Fix

```python
mad = find_median([abs(x - median) for x in data])
if mad == 0:
    # Usar desviación estándar como fallback, o retornar la media directamente
    return sum(data) / len(data)
threshold = 3 * mad
```

O de forma más elegante, usar un epsilon mínimo:

```python
threshold = 3 * max(mad, 1e-10)
```