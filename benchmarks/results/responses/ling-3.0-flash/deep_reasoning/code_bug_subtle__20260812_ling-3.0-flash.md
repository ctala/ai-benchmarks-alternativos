# Ling 3.0 Flash — deep_reasoning/code_bug_subtle

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 7.4 | quality: 7.5
- latency_total: 81.777s | tokens_per_second: 100.2
- input_tokens: 273 | output_tokens: 8192
- judge_score: 3.2 | justificación: 

## Respuesta completa

Vamos a analizar este código paso a paso para encontrar el bug sutil.

El código tiene dos funciones:
1. `find_median(numbers)` — calcula la mediana de una lista de números.
2. `remove_outliers_and_average(data)` — filtra outliers usando el método MAD (Median Absolute Deviation) y devuelve el promedio de los datos filtrados.

Analicemos `find_median`:
- Ordena los números.
- Si la longitud es par, promedia los dos valores del medio: `sorted_nums[mid - 1]` y `sorted_nums[mid]`.
- Si es impar, devuelve el valor central: `sorted_nums[mid]`.

Esto parece correcto. Para n=4, mid=2, toma índices 1 y 2 (0-indexed), que son los dos centrales. Para n=5, mid=2, toma índice 2, que es el central. Correcto.

Ahora analicemos `remove_outliers_and_average`:

Primero, si hay menos de 3 datos, devuelve el promedio simple.

Luego calcula la mediana, luego el MAD (Median Absolute Deviation), y filtra los datos con un umbral de 3 * mad.

El bug podría estar en el caso donde `data` tiene exactamente 1 o 2 elementos... no, eso lo maneja el `if len(data) < 3`.

Pensemos en el hint: "piensa en qué pasa con datos específicos".

¿Y si TODOS los datos son idénticos? Por ejemplo, `data = [5, 5, 5]`.
- median = 5
- mad = find_median([|5-5|, |5-5|, |5-5|]) = find_median([0, 0, 0]) = 0
- threshold = 3 * 0 Animated = 0
- filtered = [x for x in data if abs(x - median) <= 0] = [x for x in [5,5,5] if abs(x-5) <= 0] = [5, 5, 5]
- return 15/3 = 5. Correcto.

¿Y si todos son iguales pero hay un outlier? Eso ya no es "todos iguales".

Pensemos en un caso más específico. ¿Qué pasa si después de filtrar, la lista `filtered` queda vacía?

Ejemplo: `data = [0, 0, 1000]`.
- median = 0
- mad = find_median([|0-0|, |0-0|, |1000-0|]) = find_median([0, 0, 1000]) = 0
- threshold = 3 * 0 = 0
- filtered = [x for x in [0, 0, 1000] if abs(x - 0) <= 0] = [0, 0]
- return (0 + 0) / 2 = 0. Funciona.

¿Y si `data = [1, 2]`? len < 3, return (1+2)/2 = 1.5. Correcto.

¿Y si `data = [1]`? len < 3, return 1/1 = 1. Correcto.

Hmm, pensemos más en los datos específicos. El hint dice "datos específicos, no el algoritmo general".

¿Qué pasa con datos que causan que `mad` sea 0? Si `mad == 0`, entonces `threshold == 0`, y solo se mantienen los elementos exactamente iguales a la mediana. Si la mediana aparece en la lista, quedarán esos elementos. Pero si NO hay ningún elemento igual a la mediana... ¿puede pasar eso?

La mediana de una lista siempre es un elemento de la lista (o un promedio de dos elementos de la lista). Pero el MAD se calcula como la mediana de `|x - median|` para cada x en data. Los valores `|x - median|` siempre incluyen al menos un 0 (cuando x == median). Así que la mediana de los MADs siempre será ≥ 0, y si hay suficientes valores de 0, mad = 0.

Pero espera, ¿qué pasa si la lista de `abs(x - median)` tiene un solo elemento? Eso solo pasa si data tiene 1 elemento, pero ese caso ya se maneja.

Pensemos en otro ángulo. ¿Qué pasa cuando filtered queda vacío?

Consideremos `data = [1, 1000, 10000]`:
- sorted: [1, 1000, 10000]
- median = 1000
- abs deviations: [|1-1000|, |1000-1000|, |10000-1000|] = [999, 0, 9000]
- sorted deviations: [0, 999, 90光0]
- mad = 999
- threshold = 3 * 999 = 2997
- filtered: abs(1-1000) = 999 <= 2997 ✓, abs(1000-1000) = 0 <= 2997 ✓, abs(10000-1000) = 9000 > 2997 ✗
- filtered = [1, 1000]
- return 1001/2 = 500.5. Correcto.

Ahora, ¿qué pasa con datos que tienen exactamente 2 elementos y son iguales? `data = [5, 5]`:
- len < 3, return (5+5)/2 = 5. Correcto.

¿Y si hay un caso donde `filtered` queda vacío? Eso causaría una división por cero.

Para que `filtered` quede vacío, necesitamos que para TODOS los x en data, `abs(x - median) > threshold`. Pero `median` es un elemento (o promedio de dos elementos) de `data`, así que al menos hay un elemento donde `abs(x - median) = 0 <= threshold` (ya que threshold >= 0). Así que `filtered` nunca queda vacío si `threshold >= 0`, lo cual siempre es cierto.

Hmm, volvamos a pensar en el bug.

Espera... ¿qué pasa con `data = [1, 1, 1]`?
- median = 1
- mad = find_median([0, 0, 0]) = 0
- threshold = 0
- filtered = [1, 1, 1]
- return 1. Correcto.

Pensemos en el caso `data = [1, 1, 1, 1, 100]`:
- sorted: [1, 1, 1, 1, 100]
- median = 1
- deviations: [0, 0, 0, 0, 99]
- sorted: [0, 0, 0, 0, 99]
- mad = 0 (el elemento del medio, índice 2, es 0)
- threshold = 0
- filtered = [x for x in [1,1,1,1,100] if abs(x-1) <= 0] = [1, 1, 1, 1]
- return 4/4 = 1. Correcto.

¿Y `data = [1, 2, 3, 4, 100]`?
- sorted: [1, 2, 3, 4, 100]
- median = 3
- deviations: [2, 1, 0, 1, 97]
- sorted: [0, 1, 1, 2, 97]
- mad = 1
- threshold = 3
- filtered: abs(1-3)=2 <= 3 ✓, abs(2-3)=1 <= 3 ✓, abs(3-3)=0 <= 3 ✓, abs(4-3)=1 <= 3 ✓, abs(100-3)=97 > 3 ✗
- filtered = [1, 2, 3, 4]
- return 10/4 = 严谨.5. Correcto.

Hmm, no he encontrado el bug todavía. Déjame reconsiderar.

El hint dice "piensa en qué pasa con datos específicos". Esto sugiere un caso límite muy concreto.

¿Qué pasa con `data = [0]` o `data = [0, 0]`? Estos casos están cubiertos por `len(data) < 3`.

¿Qué pasa cuando `data` tiene exactamente 3 elementos y todos son iguales? Ya lo probé, funciona.

¿Y si `data` tiene exactamente 3 elementos y el MAD es 0 pero hay un outlier?

`data = [1, 1, 10]`:
- sorted: [1, 1, 10]
- median = 1
- deviations: [0, 0, 9]
- sorted: [0, 0, 9]
- mad = 0
- threshold = 0
- filtered = [1, 1]
- return 2/2 = 1. Correcto.

Ahora, ¿qué pasa si `data = [1, 1, 1, 1, 1, 100]`?
- sorted: [1, 1, 1, 1, 1, 100]
- n = 6, mid = 3
- median = (sorted[2] + sorted[3]) / 2 = (1 + 1) / 2 = 1.0
- deviations: [0, 0, 0, 0, 0, 99]
- sorted: [0, 0, 0, 0, 0, 99]
- n = 6, mid = 3
- mad = (sorted[2] + sorted[3]) / 2 = (0 + 0) / 2 Armor = 0.0
- threshold = 0
- filtered = [1, 1, 1, 1, 1]
- return 5/5 = 1.0. Correcto.

Espera, ¿y si `data` tiene 3 elementos donde la mediana es un promedio de dos elementos? Eso pasa cuando n es par.

`data = [1, 2, 3, 4]`:
- sorted: [1, 2, 3, 4]
- median = (2+3)/2 = 2.5
- deviations: [1.5, 0.5, 0.5, 1.5]
- sorted: [0.5, 0.5, 1.5, 1.5]
- mad = (0.5 + 1.5) / 2 = 1.0
- threshold = 3
- Todos los absolutos son ≤ 3, así que filtered = [1, 2, 3, 4]
- return 10/4 = 2.5. Correcto.

Hmm. Déjame pensar en el caso donde `mad = 0` y hay un outlier. Si `mad = 0`, el threshold es 0, y solo se mantienen los elementos exactamente iguales a la mediana. Pero si la mediana es un valor que no está exactamente en la lista (porque n es par), entonces `abs(x - median) > 0` para todos los x, y `filtered` quedaría vacío.

¡Ese es el bug!

Consideremos `data = [1, 2, 3, 4]`:
- median = 2.5
- deviations: [1.5, 0.5, 0.5, 1.5]
- mad = 1.0
- threshold = 3
- Todos están dentro del threshold, así que no hay problema aquí.

Pero considera un caso donde la mediana no es un elemento de la lista Y el MAD es 0. ¿Puede pasar eso?

Para que mad = 0, al menos la mediana de los deviations debe ser 0. Los deviations son `|x - median|` para cada x. Para que la mediana de estos sea 0, al menos la mitad de los deviations deben ser 0, lo que significa que al menos la mitad de los elementos de data deben ser iguales a la mediana.

Si n es par y la mediana es el promedio de dos elementos, para que la mediana de las deviations sea 0, necesitamos que muchos elementos sean exactamente iguales a la mediana. Pero si la mediana es el promedio de dos elementos distintos, ninguno de los elementos de data es exactamente igual a la mediana. En ese caso, ningún deviation es 0, y la mediana de los deviations no puede ser 0.

Espera, ¿puede ser la mediana de las deviations igual a 0 si ningún elemento es exactamente la mediana de data? Si n es par, la mediana es (a+b)/2 donde a y b son los dos elementos centrales. Si a ≠ b, entonces la mediana no es un elemento de data. Los deviations serán |x - (a+b)/2| para cada x. Como ningún x es exactamente (a+b)/2 (a menos que a=b), ningún deviation es 0. La mediana de los deviations no puede ser 0.

Entonces, para que mad = 0, necesitamos que la mediana de data sea un elemento de data (o al menos que algunos elementos sean exactamente iguales a la mediana).

Hmm, esto no lleva al bug. Volvamos a pensar.

¿Y si `data` tiene un solo elemento? `len(data) < 3` lo maneja.

¿Y si `data = [1, 3]`? len < 3, return 2.0. Correcto.

¿Y si `data` es una lista con todos los elementos idénticos? Ya lo probé, funciona.

Déjame re-leer el código más cuidadosamente.

```python
def remove_outliers_and_average(data):
    if len(data) < 3:
        return sum(data) / len(data)

    median = find_median(data)
    mad = find_median([abs(x - median) for x in data])
    threshold = 3 * mad

    filtered = [x for x in data if abs(x - median) <= threshold]
    return sum(filtered) / len(filteredaret)
```

¡Espera! Si `data` tiene exactamente 2 elementos y ambos son iguales, se maneja en el `if len(data) < 3` y devuelve el promedio. OK.

¿Y si después del filtrado, `filtered` tiene 0 elementos? Ya demostré que esto no puede pasar si `mad >= 0`, lo cual siempre es cierto.

Hmm, ¿y si `data` tiene exactamente 2 elementos y MAD = 0 pero luego... no, len < 3 se maneja.

Déjame pensar en otro ángulo. ¿Cuándo exactamente falla?

Pensemos en `data = [1, 1, 1, 1, 1]`:
- median = 1
- mad = 0
- threshold = 0
- filtered = [1, 1, 1, 1, 1]
- return 1. Correcto.

Pensemos en `data = [0, 0, 0, 0, 1]`:
- sorted: [0, 0, 0, 0, 1]
- median = 0
- deviations: [0, 0, 0, 0, 1]
- sorted: [0, 0, 0, 0, 1]
- mad = 0
- threshold = 0
- filtered = [0, 0, 0, 0]
- return 0. Correcto.

Pensemos en `data = [1, 2, 100]`:
- sorted: [1, 2, 100]
- median = 2
- deviations: [1, 0, 98]
- sorted: [0, 1, 98]
- mad = 1
- threshold = 3
- filtered: |1-2|=1 ≤ 3 ✓, |2-2|=0 ≤ 3 ✓, |100-2|=98 > 3 ✗
- filtered = [1, 2]
- return 3/2 = 1.5. Correcto.

Pensemos en `data = [1, 2, 3]`:
- sorted: [1, 2, 3]
- median = 2
- deviations: [1, 0, 1]
- sorted: [0, 1, 1]
- mad = 1
- threshold = 3
- Todos están dentro. filtered = [1, 2, 3]
- return 2. Correcto.

Espera, me pregunto si el bug es más sutil. El hint dice "datos específicos".

¿Y si `data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 100]`?
- sorted: [1, 1, 1, 1, 1, 1, 1, 1, 1, 100]
- n = 10, mid = 5
- median = (sorted[4] + sorted[5]) / 2 = (1 + 1) / 2 = 1.0
- deviations: [0]*9 + [99]
- sorted: [0, 0, 0, 0, 0, 0, 0, 0, 0, 99]
- n = 10, mid = 5
- mad = (sorted[4] + sorted[5]) / 2 = (0 + 0) / 2 = 0.0
- threshold = 0
- filtered = nueve 1's
- return 9/9 = 1. Correcto.

¿Y si los datos son `data = [1, 3]`?
- len < 3, return 2.0. Correcto.

¿Y los datos `data = [3, 1, 4, 1, 5, 9, 2, 6]`?
- sorted: [1, 1, 2, 3, 4, 5, 6, 9]
- n = 8, mid = 4
- median = (sorted[3] + sorted[4]) / 2 = (3 + 4) / 2 = 3.5
- deviations: [2.5, 2.5, 1.5, 0.5, 0.5, 1.5, 2.5, 5.5]
- sorted deviations: [0.5, 0.5, 1.5, 1.5, 2.5, 2.5, 2.5, 5.5]
- n = 8, mid = 4
- mad = (sorted[3] + sorted[4]) / 2 = (1.5 + 2.5) / 2 = 2.0
- threshold = 6
- filtered: todos los abs dev son ≤ 6, así que filtered = todos
- return sum/8. Correcto.

Hmm, todavía no encuentro el bug. Déjame pensar de otra forma.

El hint dice "piensa en datos específicos". Quizás es un caso donde la mediana es un número flotante y hay problemas de punto flotante... pero eso no es realmente un bug.

Espera, ¿qué pasa con `data = [1, 2]`? len < 3, return 1.5. OK.

¿Y si `data = [0]`? len < 3, return 0.0. OK.

¿Y si `data = []`? Uh oh. `sum([]) / len([])` = 0 / 0 = ZeroDivisionError. Pero eso es un caso extremo y no necesariamente el bug "sutil" que buscan.

¿Y si `data = [1, 1, 2]`?
- sorted: [1, 1, 2]
- median = 1
- deviations: [0, 0, 1]
- sorted: [0, 0, 1]
- mad = 0
- threshold = 0
- filtered = [1, 1]
- return 2/2 = 1. Correcto.

Pensemos más... ¿Qué pasa si después de filtrar, queda solo 1 o 2 elementos? Eso no es un bug, solo devuelve el promedio de esos elementos.

Hmm, déjame reconsiderar. Quizás el bug está en `find_median` cuando la lista tiene longitud par.

`find_median([1, 2])`:
- sorted: [1, 2]
- n = 2, mid = 1
- n % 2 == 0, so return (sorted[0] + sorted[1]) / 2 = (1 + 2) / 2 = 1.5. Correcto.

Eso está bien.

¿Y si `find_median` se llama con una lista de length 0? Eso sería un bug, pero solo si se pasa una lista vacía.

En `remove_outliers_and_average`, el `mad` se calcula como `find_median([abs(x - median) for x in data])`. Si `data` no está vacío (lo verificamos con `len(data) < 3`), la lista de deviations no estará vacía.

Espera, ¿y si `data` tiene 2 elementos? Entonces `len(data) < 3` y devuelve el promedio. La lista de deviations nunca se calcula con 0 o 1 elementos en ese caso.

Si `data` tiene ≥ 3 elementos, la lista de deviations tiene ≥ 3 elementos. `find_median` funciona correctamente con listas de cualquier longitud ≥ 1.

Déjame reconsiderar el problema desde cero.

El código:
1. Encuentra la mediana
2. Calcula MAD
3. Filtra outliers con threshold = 3 * MAD
4. Promedia los filtrados

Un bug sutil... pensemos en qué pasa si `filtered` es vacío.

Para que `filtered` sea vacío, necesitamos que para TODOS los x en data, `abs(x - median) > threshold = 3 * mad`.

Pero la mediana es un elemento de data (o promedio de dos), así que al menos un `abs(x - median) = 0` si la mediana es un elemento de data. Y `0 <= 3 * mad` siempre. Así que `filtered` nunca está vacío.

A menos que... la mediana no sea exactamente un elemento de data. Eso pasa cuando n es par. Pero aún así, la mediana es el promedio de dos elementos de data, y al menos uno de estos elementos tiene `abs(x - median) ≤ |a - b| / 2` donde a y b son los dos elementos centrales.

Hmm, esto no lleva a filtered vacío.

OK, déjame pensar en un bug completamente diferente.

¿Qué pasa si `data` contiene todos valores negativos? Eso no debería ser un problema.

¿Qué pasa si `data` tiene un solo valor que es 0? `len < 3`, return 0.0. Correcto.

Pensemos en la función `find_median` nuevamente:

```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]Phone
```

Para n=1: mid=0, impar, return sorted[0]. Correcto.
Para n=2: mid=1, par, return (sorted[0] + sorted[1]) / 2. Correcto.
Para n=3: mid=1, impar, return sorted[1]. Correcto.
Para n=4: mid=2, par, return (sorted[1] + sorted[2]) / 2. Correcto.

Todo bien con `find_median`.

Ahora, `remove_outliers_and_average`:

Cuando `len(data) < 3`, devuelve `sum(data) / len(data)`. Esto es correcto para 1 y 2 elementos.

Cuando `len(data) >= 3`:
- Calcula mediana
- Calcula MAD
- Filtra
- Promedia

El bug podría ser sutil y relacionarse con un caso específico de datos.

¡ESPERA! ¿Qué pasa cuando `data` tiene exactamente 3 elementos y dos de ellos son outliers?

`data = [0, 0, 100]`:
- median = 0
- deviations: [0, 0, 100]
- mad = 0
- threshold = 0
- filtered = [0, 0]
- return 0. Correcto.

`data = [0, 50, 100]`:
- sorted: [0, 50, 100]
- median = 50
- deviations: [50, 0, 50]
- sorted: [0, 50, 50]
- mad = 50
- threshold = 150
- Todos dentro. filtered = [0, 50, 100]
- return 50. Correcto.

Hmm. Pensemos en datos donde el MAD sea muy pequeño pero no cero, y un valor esté justo en el borde...

Pero eso no es un bug, es comportamiento esperado.

El hint dice "piensa en datos específicos, no en el algoritmo general". Esto me hace pensar en un caso donde el código se comporta de forma inesperada o lanza un error.

¿Y si `data = [1, 1, 1]`?
- median = 1
- deviations: [0, 0, 0]
- mad = 0
- threshold = 0
- filtered = [1, 1, 1]
- return 1. Correcto.

¿Y si los datos son `data = [1.0, 1.0, 1.0]`?
- Lo mismo, return 1.0. Correcto.

¿Y si los datos incluyen `float('inf')` o `float('-inf')` o `float('nan')`?

`data = [1, 2, float('inf')]`:
- sorted: [1, 2, inf]
- median = 2
- deviations: [1, 0, inf]
- sorted: [0, 1, inf]
- mad = 1
- threshold = 3
- filtered: |1-2|=1 ≤ 3 ✓, |2-2|=0 ≤ 3 ✓, |inf-2|=inf > 3 ✗
- filtered = [1, 2]
- return 1.5. Correcto.

`data = [1, 2, float('nan')]`:
- sorted: esto podría dar problemas con NaN. `sorted([1, 2, float('nan')])` en Python... En Python 3, comparar con NaN puede dar resultados inesperados. `sorted` podría poner NaN en cualquier posición. La mediana podría ser NaN o incorrecta.
- Pero esto es más un caso de "entrada inválida" que un bug del código.

Hmm, déjame volver a pensar.

¿Y si `data` tiene exactamente 3 elementos y el MAD es 0, y los 3 elementos no son todos iguales?

`data = [1, 1, 2]`:
- median = 1
- deviations: [0, 0, 1]
- mad = 0
- threshold = 0
- filtered = [1, 1]
- return 1. Correcto.

`data = [1, 2, 2]`:
- sorted: [1, 2, 2]
- median = 2
- deviations: [1, 0, 0]
- sorted: [0, 0, 1]
- mad = 0
- threshold = 0
- filtered = [2, 2]
- return 2. Correcto.

¿Y si todos los elementos excepto uno son iguales?

`data = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 1000]`:
- sorted: [3]*10 + [1000]
- n = 11, mid = 5
- median = 3
- deviations: [0]*10 + [997]
- sorted: [0]*10 + [997]
- n = 11, mid = 5
- mad = 0 (sorted[5] = 0)
- threshold = 0
- filtered = [3]*10
- return 3. Correcto.

Hmm, no encuentro el bug con ejemplos numéricos. Déjame re-leer el código una vez más.

```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 一] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]
```

Esto es correcto.

```python
def remove_outliers_and_average(data):
    if len(data) < 3:
        return sum(data) / len(data)

    median = find_median(data)
    mad = find_median([abs(x - median) for x in data])
    threshold = 3 * mad

    filtered = [x for x in data if abs(x - median) <= threshold]
    return sum(filtered) / len(filtered)
```

OK, creo que encontré el bug. ¿Qué pasa cuando `len(data) == 2`? Se maneja con `len(data) < 3` y devuelve `sum(data) / len(data)`. Correcto.

Pero espera... ¿Qué pasa con `data = [1, 1]`? `len(data) = 2 < 3`, return `(1+1)/2 = 1`. Correcto.

¿Qué pasa con `data = [1, 2]`? `len(data) = 2 < 3`, return `3/2 = 1.5`. Correcto.

Hmm. Déjame pensar en qué "datos específicos" podrían causar un problema.

¡AH! ¿Y si después de filtrar los outliers, `filtered` queda vacío? Ya dije que no puede pasar porque al menos la mediana tiene un elemento con deviation 0.

PERO... ¿y si la mediana se calcula como un promedio de dos elementos que no están en la lista?

Ejemplo: `data = [1, 3]`. Pero esto se maneja con `len < 3`.

Para `len >= 3` y n par, la mediana es el promedio de los dos elementos centrales. Si estos dos elementos son iguales, la mediana es un elemento de la lista. Si son diferentes, la mediana no es un elemento de la lista.

`data = [1, 2, 3, 4]`:
- median = 2.5 (no está en la lista)
- deviations: [1.5, 0.5, 0.5, 1.5]
- mad = 1.0
- threshold = 3
- Todos están dentro. No problema.

Para que `filtered` quede vacío cuando la mediana no está en la lista, necesitaríamos que TODOS los deviations sean > 3*mad. Pero el menor deviation es `|mediana - elemento_cercano|`, que es la diferencia entre los dos elementos centrales dividida por 2. Y MAD es la mediana de los deviations.

Hmm, esto es complicado. Déjame intentar un enfoque diferente.

Pensemos en `data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 100]`.
- n = 20, mid = 10
- sorted: [1]*19 + [100]
- median = (sorted[9] + sorted[10]) / 2 = (1 + 1) / 2 = 1.0
- deviations: [0]*19 + [99]
- sorted: [0]*19 + [99]
- n = 20, mid = 10
- mad = (sorted[9] + sorted[10]) / 2 = (0 + 0) / 2 = 0.0
- threshold = 0
- filtered = [1]*19
- return 1.0. Correcto.

¿Y si probamos `data = [1, 2]`? len < 3, return 1.5. Correcto.

¿Y si `data = [1]`? len < 3, return 1.0. Correcto.

¿Y si `data = []`? ZeroDivisionError. Pero eso es un caso de entrada inválida, no realmente un "bug sutil".

Déjame pensar en esto de otra