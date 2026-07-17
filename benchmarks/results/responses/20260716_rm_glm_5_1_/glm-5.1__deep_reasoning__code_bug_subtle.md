# GLM-5.1 — deep_reasoning/code_bug_subtle

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 97.868s | tokens_per_second: 83.7
- input_tokens: 215 | output_tokens: 8192
- judge_score: 4.0 | justificación: La respuesta identifica correctamente el bug sutil relacionado con el cálculo de la desviación absoluta mediana (MAD) y el filtrado de datos, proporcionando un análisis detallado de casos extremos, aunque la utilidad práctica para un emprendedor podría ser limitada.

## Respuesta completa

El objetivo es identificar un bug sutil en el código proporcionado, sin ejecutarlo, y explicar exactamente cuándo falla y por qué.

Vamos a analizar el código paso a paso.

Función `find_median(numbers)`:
- Ordena los números.
- Calcula `n = len(sorted_nums)`.
- Calcula `mid = n // 2`.
- Si `n` es par, devuelve el promedio de los dos elementos centrales: `(sorted_nums[mid - 1] + sorted_nums[mid]) / 2`.
- Si `n` es impar, devuelve el elemento central: `sorted_nums[mid]`.
Esta función parece correcta para calcular la mediana.

Función `remove_outliers_and_average(data)`:
- Si `len(data) < 3`, devuelve el promedio.
- Calcula la mediana: `median = find_median(data)`.
- Calcula la desviación absoluta mediana (MAD): `mad = find_median([abs(x - median) for x in data])`.
- Calcula el umbral: `threshold = 3 * mad`.
- Filtra los datos: `filtered = [x for x in data if abs(x - median) <= threshold]`.
- Devuelve el promedio de los filtrados: `sum(filtered) / len(filtered)`.

¿Dónde puede estar el bug?

Pensemos en casos extremos o específicos:
1. ¿Qué pasa si `data` está vacío? `len(data) < 3` lo captura, pero si `len(data) == 0`, `sum(data) / len(data)` dará ZeroDivisionError. Sin embargo, el problema dice "un bug sutil que solo aparece en ciertos casos" y el hint dice "piensa en qué pasa con datos específicos, no en el algoritmo general". Un array vacío es muy obvio, no sutil. Asumamos que `data` no está vacío.

2. ¿Qué pasa si `mad` es 0?
Si `mad == 0`, entonces `threshold = 0`.
La condición para filtrar sería `abs(x - median) <= 0`, lo que significa `x == median`.
Si todos los elementos de `data` son iguales, `mad` será 0.
Si `mad` es 0, `filtered` contendrá solo los elementos exactamente iguales a la mediana.
Si hay elementos repetidos que son la mediana, `filtered` no estará vacío.
Pero, ¿qué pasa si `mad` es 0 debido a que más de la mitad de los elementos son idénticos, pero hay otros elementos diferentes?
Ejemplo: `data = [1, 1, 1, 100, 1000]`.
Mediana = 1.
Desviaciones: `[0, 0, 0, 99, 999]`.
MAD = 0.
Threshold = 0.
Filtrado: `abs(x - 1) <= 0` -> `x == 1`.
`filtered = [1, 1, 1]`.
`sum(filtered) / len(filtered) = 3 / 3 = 1`. Esto funciona.

3. ¿Qué pasa si `filtered` queda vacío?
Si `threshold = 0` y ningún elemento es exactamente la mediana (por ejemplo, si la mediana es el promedio de dos números y no hay ningún elemento con ese valor exacto).
Ejemplo: `data = [1, 3]`. `len(data) < 3`, devuelve `2`.
Ejemplo: `data = [1, 3, 5]`. Mediana = 3. MAD = median([2, 0, 2]) = 2. Threshold = 6. Filtrado = [1, 3, 5].
Ejemplo: `data = [1, 2, 3, 4]`. Mediana = 2.5.
Desviaciones: `[1.5, 0.5, 0.5, 1.5]`.
MAD = median([0.5, 0.5, 1.5, 1.5]) = 1.0.
Threshold = 3.0.
Filtrado = [1, 2, 3, 4]. Funciona.

¿Cuándo podría `mad` ser 0 y la mediana no ser un valor en la lista?
Si la lista tiene un número par de elementos y la mediana es un valor decimal (ej. 2.5), y todos los elementos son distintos de 2.5.
Pero para que `mad` sea 0, la mediana de las desviaciones absolutas debe ser 0.
Si la mediana de las desviaciones absolutas es 0, significa que al menos la mitad de las desviaciones absolutas son 0.
Si la desviación absoluta es 0, significa que `abs(x - median) == 0`, o sea, `x == median`.
Si al menos la mitad de los elementos son iguales a la mediana, entonces la mediana debe ser ese valor.
Por lo tanto, si `mad == 0`, la mediana tiene que ser un elemento de la lista (o hay un empate, pero el promedio de dos elementos iguales es ese elemento, así que sigue estando en la lista).
Espera, si `data = [1, 1, 2, 2]`. Mediana = 1.5.
Desviaciones: `[0.5, 0.5, 0.5, 0.5]`. MAD = 0.5. Threshold = 1.5.
Filtrado: `abs(x - 1.5) <= 1.5` -> `x` en `[0, 3]`. Todos pasan.

¿Y si `data = [1, 1, 1, 2]`?
Mediana = 1. MAD = 0. Threshold = 0.
Filtrado = `[1, 1, 1]`. Promedio = 1.

¿Cuándo `filtered` puede quedar vacío?
Si `threshold` es negativo. Pero `mad` es una desviación, siempre es `>= 0`. Así que `threshold >= 0`.
Si `threshold = 0` y no hay elementos iguales a la mediana, pero ya vimos que eso es imposible.
Si `len(filtered) == 0`, entonces `sum(filtered) / len(filtered)` dará ZeroDivisionError.
¿Puede `filtered` estar vacío?
Solo si `abs(x - median) > threshold` para todos los `x`.
Si `threshold = 3 * mad`.
Si `mad = 0`, `threshold = 0`. Como vimos, si `mad = 0`, la mediana está en la lista, así que al menos un elemento pasa.
¿Qué pasa si `mad` es muy pequeño y todos los elementos están muy lejos?
No, la mediana siempre está a distancia 0 de sí misma, y la MAD se basa en la distancia a la mediana. La MAD de un conjunto no vacío es la mediana de esas distancias. Al menos la mitad de los elementos tienen una distancia `<= MAD`. Por lo tanto, al menos la mitad de los elementos tienen `abs(x - median) <= MAD <= 3 * MAD = threshold`. Así que `filtered` nunca estará vacío.

Entonces, ¿dónde está el bug?
Vamos a revisar la definición de MAD.
El MAD se suele definir como la mediana de las desviaciones absolutas de los datos respecto a su mediana. Eso es lo que hace el código.
Sin embargo, en estadística, para usar el MAD como estimador de la desviación estándar, se suele multiplicar por una constante (1.4826 para distribuciones normales), pero eso es una convención, no un bug.

Revisemos la lógica de nuevo.
```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]
```

¿Qué pasa si `numbers` tiene longitud 0?
`n = 0`. `mid = 0`.
`n % 2 == 0` es True.
Devuelve `(sorted_nums[-1] + sorted_nums[0]) / 2`.
¡Ah! Si `numbers` está vacío, `sorted_nums` está vacío, y `sorted_nums[-1]` y `sorted_nums[0]` lanzarán `IndexError`.
Pero en `remove_outliers_and_average`, si `len(data) < 3`, no se llama a `find_median`.
Si `len(data) >= 3`, `data` tiene al menos 3 elementos.
Se llama a `find_median(data)`, que funciona bien.
Se llama a `find_median([abs(x - median) for x in data])`. Esta lista tiene la misma longitud que `data`, así que al menos 3 elementos. Funciona bien.

¿Puede la lista de desviaciones absolutas estar vacía? No, porque `data` no está vacío.
¿Hay algún problema con los tipos de datos? No se especifica.

Pensemos en otro caso.
¿Qué pasa si `data` tiene 3 elementos?
`len(data) < 3` es False.
`median = find_median(data)`.
`mad = find_median([abs(x - median) for x in data])`.
`threshold = 3 * mad`.
`filtered = [x for x in data if abs(x - median) <= threshold]`.
`return sum(filtered) / len(filtered)`

¿Qué pasa si `data = [1, 2, 1000000]`?
Mediana = 2.
Desviaciones: `[1, 0, 999998]`.
MAD = 1.
Threshold = 3.
Filtrado: `abs(1 - 2) <= 3` (True), `abs(2 - 2) <= 3` (True), `abs(1000000 - 2) <= 3` (False).
`filtered = [1, 2]`.
`sum(filtered) / len(filtered) = 3 / 2 = 1.5`.

¿Qué pasa si `data = [1, 1, 1]`?
Mediana = 1.
Desviaciones: `[0, 0, 0]`.
MAD = 0.
Threshold = 0.
Filtrado: `[1, 1, 1]`.
Promedio = 1.

¿Qué pasa si `data = [1, 1, 2]`?
Mediana = 1.
Desviaciones: `[0, 0, 1]`.
MAD = 0.
Threshold = 0.
Filtrado: `[1, 1]`.
Promedio = 1.

¿Qué pasa si `data = [1, 2, 2]`?
Mediana = 2.
Desviaciones: `[1, 0, 0]`.
MAD = 0.
Threshold = 0.
Filtrado: `[2, 2]`.
Promedio = 2.

¿Qué pasa si `data = [1, 2, 3]`?
Mediana = 2.
Desviaciones: `[1, 0, 1]`.
MAD = 1.
Threshold = 3.
Filtrado: `[1, 2, 3]`.
Promedio = 2.

¿Qué pasa si `data = [1, 2, 3, 4, 5]`?
Mediana = 3.
Desviaciones: `[2, 1, 0, 1, 2]`.
MAD = 1.
Threshold = 3.
Filtrado: `[1, 2, 3, 4, 5]`.
Promedio = 3.

¿Qué pasa si `data = [1, 2, 3, 100]`? (4 elementos)
Mediana = 2.5.
Desviaciones: `[1.5, 0.5, 0.5, 97.5]`.
MAD = median([0.5, 0.5, 1.5, 97.5]) = 1.0.
Threshold = 3.0.
Filtrado: `[1, 2, 3]`.
Promedio = 2.0.

Pensemos en el hint: "piensa en qué pasa con datos específicos, no en el algoritmo general".
¿Qué tipo de datos específicos?
- Datos negativos.
- Datos flotantes.
- Datos donde la mediana es flotante y MAD es 0 (imposible como vimos).
- Datos con ceros.
- Datos donde TODOS son outliers. Pero vimos que siempre al menos la mitad pasan el filtro, porque `abs(x - median) <= MAD` para al menos la mitad de los elementos, y `MAD <= 3 * MAD`.
- Datos donde la mediana es un número muy grande y MAD es 0. Funciona.
- Datos donde el umbral filtra TODOS los elementos... ¿puede pasar eso?
Si `threshold` es 0 y no hay elementos iguales a la mediana.
¿Puede `threshold` ser 0 y no haber elementos iguales a la mediana?
Si `mad = 0`, significa que la mediana de las desviaciones absolutas es 0.
Para que la mediana de una lista de números no negativos sea 0, al menos la mitad de los números deben ser 0.
Las desviaciones absolutas son `abs(x - median)`.
Si al menos la mitad de las desviaciones absolutas son 0, entonces al menos la mitad de los elementos `x` cumplen `x == median`.
Si al menos la mitad de los elementos cumplen `x == median`, entonces la mediana tiene que ser ese valor.
Por lo tanto, SIEMPRE habrá elementos en `filtered` si `mad = 0`.

¿Y si `threshold` no es 0?
Si `mad > 0`, `threshold > 0`. Como la mediana de las desviaciones absolutas es `mad`, al menos la mitad de las desviaciones absolutas son `<= mad`.
Como `mad <= 3 * mad = threshold`, al menos la mitad de los elementos cumplirán `abs(x - median) <= threshold`.
Por lo tanto, `len(filtered)` NUNCA será 0. Así que `ZeroDivisionError` en `sum(filtered) / len(filtered)` no ocurrirá por la lista vacía.

Espera, ¿y si `len(data) < 3`?
El código dice:
```python
if len(data) < 3:
    return sum(data) / len(data)
```
¿Qué pasa si `data` es una lista vacía `[]`?
`len(data) < 3` es True.
`sum([]) / len([])` -> `0 / 0` -> `ZeroDivisionError`.
¿Es este el bug sutil?
Un array vacío es un caso específico. Si `data = []`, falla.
¿Qué pasa si `data = [5]`? `len(data) < 3` es True. `sum([5]) / len([5])` -> `5 / 1 = 5`. Funciona.
¿Qué pasa si `data = [5, 10]`? Funciona.

¿Hay algún otro caso?
¿Qué pasa si `data` contiene elementos que no son numéricos? El código asume que son numéricos.
¿Qué pasa si `data = [1, 2, 3]` y la mediana es 2, pero hay un error de precisión flotante?
Por ejemplo, `data = [1.0, 2.0, 3.0]`. Funciona.

Revisemos el cálculo de la mediana.
```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]
```
Si `numbers` está vacío, `n = 0`, `mid = 0`.
`n % 2 == 0` es True.
Devuelve `(sorted_nums[-1] + sorted_nums[0]) / 2`.
Si `numbers` está vacío, esto da `IndexError`.
Pero en `remove_outliers_and_average`, `find_median` solo se llama si `len(data) >= 3`.
Y la lista que se le pasa a `find_median` la segunda vez es `[abs(x - median) for x in data]`, que tiene la misma longitud que `data`, por lo que también es `>= 3`.
Así que `find_median` nunca se llama con una lista vacía desde `remove_outliers_and_average`.

Entonces, el bug de la lista vacía en `remove_outliers_and_average` es real: si `data = []`, se lanza `ZeroDivisionError`.
¿Es este el bug sutil? Un `ZeroDivisionError` con una lista vacía es bastante común, pero el hint dice "un bug sutil que solo aparece en ciertos casos. Piensa en qué pasa con datos específicos".
¿Qué pasa si `data` es `[0, 0]`? `len < 3`, devuelve `0/2 = 0`.
¿Qué pasa si `data` es `[0]`? Devuelve `0/1 = 0`.

Pensemos en otros datos específicos.
¿Qué pasa si `data = [1, 1, 1, 1, 1, 1, 1]`?
Mediana = 1. MAD = 0. Threshold = 0.
Filtrado = `[1, 1, 1, 1, 1, 1, 1]`.
Promedio = 1.

¿Qué pasa si `data` tiene elementos que se cancelan?
`data = [-1, 0, 1]`
Mediana = 0.
Desviaciones: `[1, 0, 1]`.
MAD = 1.
Threshold = 3.
Filtrado = `[-1, 0, 1]`.
Promedio = 0.

¿Qué pasa si `data = [1, 2, 3, 4, 5, 1000000]`?
Mediana = 3.5.
Desviaciones: `[2.5, 1.5, 0.5, 0.5, 1.5, 999996.5]`.
MAD = 1.5.
Threshold = 4.5.
Filtrado = `[1, 2, 3, 4, 5]`.
Promedio = 3.

¿Qué pasa si `data` tiene muchos números repetidos?
`data = [0, 0, 0, 0, 100]`
Mediana = 0.
Desviaciones: `[0, 0, 0, 0, 100]`.
MAD = 0.
Threshold = 0.
Filtrado = `[0, 0, 0, 0]`.
Promedio = 0.

Espera. ¿Qué pasa si `data` tiene números que son outliers, pero `mad` es 0?
Si `data = [1, 1, 1, 1, 100]`.
Mediana = 1.
MAD = 0.
Threshold = 0.
Filtrado = `[1, 1, 1, 1]`.
Promedio = 1.

¿Qué pasa si `data = [1, 1, 100, 100, 100]`?
Mediana = 100.
Desviaciones: `[99, 99, 0, 0, 0]`.
MAD = 0.
Threshold = 0.
Filtrado = `[100, 100, 100]`.
Promedio = 100.

Pensemos en la definición de MAD.
A veces, el MAD se multiplica por una constante `b = 1.4826` para que sea consistente con la desviación estándar en distribuciones normales. Pero no multiplicarlo no es un "bug", es una decisión de diseño. El código usa `3 * mad`, que es un umbral típico si no se multiplica por la constante (si se multiplicara, sería `3 * 1.4826 * mad ≈ 4.44 * mad`). No es un bug.

¿Y si `data` tiene longitud 3, pero dos de ellos son iguales?
`data = [1, 1, 100]`
Mediana = 1.
MAD = 0.
Threshold = 0.
Filtrado = `[1, 1]`.
Promedio = 1.

¿Qué pasa si `data = [1, 100, 100]`?
Mediana = 100.
MAD = 0.
Threshold = 0.
Filtrado = `[100, 100]`.
Promedio = 100.

¿Qué pasa si `data` tiene longitud 4 y la mediana es un valor que no está en la lista, y MAD es 0?
`data = [1, 1, 100, 100]`
Mediana = 50.5.
Desviaciones: `[49.5, 49.5, 49.5, 49.5]`.
MAD = 49.5.
Threshold = 148.5.
Filtrado = `[1, 1, 100, 100]`.
Promedio = 50.5.

¿Puede MAD ser 0 si la mediana no está en la lista?
Si `mad = 0`, al menos la mitad de las desviaciones absolutas son 0.
Si `abs(x - median) = 0`, entonces `x = median`.
Si al menos la mitad de los elementos son `median`, entonces la mediana tiene que ser `median`.
Para listas de longitud par, la mediana es el promedio de los dos centrales.
Si al menos la mitad de los elementos son `M`, los dos elementos centrales tienen que ser `M`.
Por lo tanto, la mediana será `M`, que está en la lista.
Así que si `mad = 0`, la mediana siempre es un elemento de la lista, y `threshold = 0` filtrará todo excepto los elementos `median`.

¿Puede `filtered` estar vacío?
Solo si `threshold < 0`, lo cual es imposible ya que `mad >= 0`.
Solo si `abs(x - median) > threshold` para todo `x`. Pero siempre hay al menos un `x` (la mediana) donde `abs(x - median) = 0 <= threshold`. Así que `filtered` siempre tiene al menos un elemento, a menos que la mediana no esté en la lista y `threshold = 0`, lo cual demostramos que es imposible.

Revisemos de nuevo el código de `find_median`.
```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]
```
Si `numbers` tiene 1 elemento, `n = 1`, `mid = 0`.
`1 % 2 != 0`, devuelve `sorted_nums[0]`. Correcto.
Si `numbers` tiene 2 elementos, `n = 2`, `mid = 1`.
`2 % 2 == 0`, devuelve `(sorted_nums[0] + sorted_nums[1]) / 2`. Correcto.
Si `numbers` tiene 3 elementos, `n = 3`, `mid = 1`.
Devuelve `sorted_nums[1]`. Correcto.

¿Y si `numbers` está vacío?
`n = 0`, `mid = 0`.
`0 % 2 == 0`, devuelve `(sorted_nums[-1] + sorted_nums[0]) / 2`.
Si `numbers` está vacío, lanza `IndexError`.
Pero en `remove_outliers_and_average`, `find_median` se llama con `data` y `[abs(x - median) for x in data]`.
Si `len(data) >= 3`, `data` no está vacío, y la lista por comprensión tampoco.
Así que `find_median` no se llama vacía desde ahí.

¿Y si `len(data) < 3`?
```python
if len(data) < 3:
    return sum(data) / len(data)
```
Si `data = []`, lanza `ZeroDivisionError`.
Si `data = [1]`, devuelve 1.
Si `data = [1, 2]`, devuelve 1.5.

¿Es el bug el `ZeroDivisionError` cuando `data = []`?
Es un bug, pero ¿es "sutil" y "solo aparece en ciertos casos"?
A lo mejor se refiere a cuando `data` tiene un solo elemento y ese elemento es 0.
`data = [0]`. `sum([0]) / len([0])` -> `0 / 1 = 0`. No hay error.

Espera, ¿qué pasa si `data = [1, 1]`?
`len(data) < 3` -> `sum([1, 1]) / len([1, 1])` -> `2 / 2 = 1`.

¿Qué pasa si `data = [1, 2, 3]`?
Mediana = 2.
MAD = 1.
Threshold = 3.
Filtrado = `[1, 2, 3]`.
Promedio = 2.

Pensemos en el tipo de datos. ¿Qué pasa si `data` contiene enteros y el promedio se espera que sea flotante?
En Python 3, `/` siempre devuelve flotante. Así que no hay problema de división entera.

¿Qué pasa si `data` contiene números negativos?
`data = [-5, -4, -3, -2, -1]`
Mediana = -3.
Desviaciones: `[2, 1, 0, 1, 2]`.
MAD = 1.
Threshold = 3.
Filtrado = `[-5, -4, -3, -2, -1]`.
Promedio = -3.

¿Qué pasa si `data` es `[1, 2, 3, 100, 101, 102]`?
Mediana = 52.5.
Desviaciones: `[51.5, 50.5, 49.5, 47.5, 48.5, 49.5]`.
MAD = 49.5.
Threshold = 148.5.
Filtrado = todos.

¿Qué pasa si `data = [1, 2, 3, 1000]`?
Mediana = 2.5.
Desviaciones: `[1.5, 0.5, 0.5, 997.5]`.
MAD = 1.0.
Threshold = 3.0.
Filtrado = `[1, 2, 3]`.
Promedio = 2.0.

¿Qué pasa si `data = [1, 2, 1000, 1001]`?
Mediana = 501.0.
Desviaciones: `[500, 499, 499, 500]`.
MAD = 499.5.
Threshold = 1498.5.
Filtrado = todos.

¿Qué pasa si `data` tiene una distribución tal que `mad = 0` y `threshold = 0`?
`data = [1, 1, 1, 1, 1]`
Mediana = 1.
Desviaciones: `[0, 0, 0, 0, 0]`.
MAD = 0.
Threshold = 0.
Filtrado = `[1, 1, 1, 1, 1]`.
Promedio = 1.

¿Qué pasa si `data = [1, 1, 1, 1, 100]`?
Mediana = 1.
Desviaciones: `[0, 0, 0, 0, 99]`.
MAD = 0.
Threshold = 0.
Filtrado = `[1, 1, 1, 1]`.
Promedio = 1.

¿Qué pasa si `data = [1, 1, 1, 100, 100]`?
Mediana = 1.
Desviaciones: `[0, 0, 0, 99, 99]`.
MAD = 0.
Threshold = 0.
Filtrado = `[1, 1, 1]`.
Promedio = 1.

¿Qué pasa si `data = [1, 1, 100, 100, 100]`?
Mediana = 100.
Desviaciones: `[99, 99, 0, 0, 0]`.
MAD = 0.
Threshold = 0.
Filtrado = `[100, 100, 100]`.
Promedio = 100.

Espera, ¿y si `data = [1, 1, 1, 2]`?
Mediana = 1.
MAD = 0.
Threshold = 0.
Filtrado = `[1, 1, 1]`.
Promedio = 1.

¿Hay algún caso donde `mad = 0` y `filtered` esté vacío?
Si `data = [1, 2, 3]`. Mediana = 2. MAD = 1.
Para que `mad = 0`, la mediana de `[abs(x - median) for x in data]` debe ser 0.
Esto significa que al menos la mitad de los elementos de `data` son iguales a la mediana.
Si al menos la mitad de los elementos son iguales a la mediana, entonces la mediana es ese valor, y ese valor está en la lista.
Cuando `threshold = 0`, filtramos `abs(x - median) <= 0`, lo que significa `x == median`.
Como al menos la mitad de los elementos son iguales a la mediana, `filtered` contendrá al menos la mitad de los elementos.
Así que `len(filtered)` será al menos `len(data) // 2`.
No estará vacío.

¿Y si `mad` es negativo? `abs()` siempre devuelve un valor no negativo, así que `mad >= 0`.

¿Y si `data` tiene `NaN` o `inf`?
Si `data` tiene `inf`, `sorted_nums` pondrá `inf` al final.
La mediana podría ser `inf`.
`abs(x - inf)` será `inf` para cualquier `x` finito, y `0` si `x` es `inf`.
Si `data = [1, 2, inf]`.
Mediana = 2.
Desviaciones: `[1, 0, inf]`.
MAD = 1.
Threshold = 3.
Filtrado = `[1, 2]`.
Promedio = 1.5.

Si `data = [1, inf, inf]`.
Mediana = `inf`.
Desviaciones: `[inf, 0, 0]`.
MAD = 0.
Threshold = 0.
Filtrado = `[inf, inf]`.
Promedio = `inf`.

¿Y si `data = [1, 2, 3]` pero con enteros?
No hay problema.

Pensemos en el hint de nuevo: "piensa en qué pasa con datos específicos, no en el algoritmo general".
¿Qué datos específicos podrían causar un problema?
- Listas vacías.
- Listas con un solo elemento.
- Listas con dos elementos.
- Listas donde todos los elementos son iguales.
- Listas donde la mediana es un número flotante y la comparación `abs(x - median) <= threshold` falla por precisión flotante.
- Listas con enteros donde la mediana es un flotante (ej. `[1, 2]`), pero `len(data) >= 3` así que no entra en el primer `if`.
- Listas donde `threshold` se calcula como `3 * mad`, y `mad` es 0, por lo que `threshold` es 0. Ya vimos que esto no vacía la lista.
- Listas donde la mediana es un número flotante, y `abs(x - median)` no es exactamente 0 cuando `x` es la mediana.
Ejemplo: `data = [1, 2, 3, 4]`.
Mediana = 2.5.
Desviaciones: `[1.5, 0.5, 0.5, 1.5]`.
MAD = 1.0.
Threshold = 3.0.
Filtrado: `abs(x - 2.5) <= 3.0`. Todos pasan.

¿Qué pasa si `data` tiene números enteros, pero la mediana es un flotante que NO está en la lista original?
Ejemplo: `data = [1, 2, 3, 4]`.
Mediana = 2.5.
`mad = 1.0`.
`threshold = 3.0`.
`abs(1 - 2.5) = 1.5 <= 3.0`.
`abs(2 - 2.5) = 0.5 <= 3.0`.
`abs(3 - 2.5) = 0.5 <= 3.0`.
`abs(4 - 2.5) = 1.5 <= 3.0`.
Todos pasan.

¿Puede pasar que `threshold` sea menor que la desviación de TODOS los elementos?
Si `threshold` es muy pequeño, pero como `threshold = 3 * mad`, y `mad` es la mediana de las desviaciones, al menos la mitad de las desviaciones son `<= mad`. Por lo tanto, al menos la mitad de las desviaciones son `<= 3 * mad = threshold`. Así que siempre habrá al menos `n/2` elementos en `filtered`.

Espera. ¿Y si `data` es una lista de enteros y `threshold` se calcula como entero, pero `mad` es un flotante?
`mad` es flotante si la mediana de las desviaciones es flotante.
Las desviaciones son `abs(x - median)`. Si `median` es flotante, las desviaciones son flotantes.
Si `median` es entero, las desviaciones son enteras (si `x` es entero).
Entonces `mad` puede ser entero.
Si `mad = 1`, `threshold = 3`.
`abs(x - median) <= 3`. Funciona correctamente.

¿Y si `data` tiene elementos repetidos y la mediana es flotante?
`data = [1, 1, 2, 2]`.
Mediana = 1.5.
Desviaciones: `[0.5, 0.5, 0.5, 0.5]`.
MAD = 0.5.
Threshold = 1.5.
Filtrado: `abs(x - 1.5) <= 1.5`.
`abs(1 - 1.5) = 0.5 <= 1.5`.
`abs(2 - 1.5) = 0.5 <= 1.5`.
Todos pasan.

¿Y si `data = [1, 1, 1, 2]`?
Mediana = 1.
MAD = 0.
Threshold = 0.
Filtrado: `abs(x - 1) <= 0`.
`x = 1` -> `0 <= 0` (True).
`x = 2` -> `1 <= 0` (False).
`filtered = [1, 1, 1]`.
Promedio = 1.

¿Qué pasa si `data = [1, 2, 2, 2]`?
Mediana = 2.
MAD = 0.
Threshold = 0.
Filtrado: `abs(x - 2) <= 0`.
`x = 1` -> `1 <= 0` (False).
`x = 2` -> `0 <= 0` (True).
`filtered = [2, 2, 2]`.
Promedio = 2.

¿Qué pasa si `data` tiene longitud 3, y la mediana es 0?
`data = [-1, 0, 1]`.
Mediana = 0.
MAD = 1.
Threshold = 3.
Filtrado = `[-1, 0, 1]`.

Pensemos en el caso donde `data` tiene longitud 0.
`len(data) < 3` es True.
`sum(data) / len(data)` -> `0 / 0` -> `ZeroDivisionError`.
¿Es este el bug?
Es un bug, sí. Pero el hint dice "un bug sutil que solo aparece en ciertos casos".
Un array vacío es un caso específico.
¿Hay algún otro caso?
¿Qué pasa si `data` tiene longitud 2?
`data = [1, 2]`.
`len(data) < 3` es True.
`sum([1, 2]) / len([1, 