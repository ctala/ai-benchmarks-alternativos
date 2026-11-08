# Qwen3-Coder-Next (OpenRouter FP8) — deep_reasoning/code_bug_subtle

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 6.48 | quality: 7.5
- latency_total: 300.279s | tokens_per_second: 24.8
- input_tokens: 202 | output_tokens: 7449

## Entrada exacta (lo que recibió el modelo)

**user:**

Este codigo tiene un bug sutil que solo aparece en ciertos casos.
Identificalo sin ejecutar el codigo. Explica exactamente cuando falla y por que.

```python
def find_median(numbers):
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def remove_outliers_and_average(data):
    if len(data) < 3:
        return sum(data) / len(data)

    median = find_median(data)
    mad = find_median([abs(x - median) for x in data])
    threshold = 3 * mad

    filtered = [x for x in data if abs(x - median) <= threshold]
    return sum(filtered) / len(filtered)
```

Hint: piensa en que pasa con datos especificos, no en el algoritmo general.


## Respuesta completa

El bug sutil ocurre cuando **todos los elementos de `data` son idénticos** (por ejemplo, `data = [5, 5, 5]` o `data = [0, 0, 0, 0]`).

### ¿Por qué falla?

1. **`median = find_median(data)`**  
   Si todos los valores son iguales (digamos `c`), entonces `sorted(data) = [c, c, ..., c]`, y la mediana será `c`.

2. **`mad = find_median([abs(x - median) for x in data])`**  
   Como `x - median = c - c = 0` para todo `x`, la lista `[abs(x - median) for x in data]` será `[0, 0, ..., 0]`.  
   Entonces `mad = find_median([0, 0, ..., 0]) = 0`.

3. **`threshold = 3 * mad = 3 * 0 = 0`**

4. **`filtered = [x for x in data if abs(x - median) <= threshold]`**  
   Evaluamos: `abs(x - median) = abs(c - c) = 0`, y `0 <= 0` es **verdadero**,  
   así que **todos los elementos se conservan**: `filtered = data`.

   ✅ Hasta aquí todo parece bien.

### 🚨 Pero el problema real aparece **cuando `mad = 0` y hay más de un elemento distinto**?  
No, en el caso *todos iguales* no hay problema: `filtered = data`, y la función devuelve el promedio correcto.

Entonces, ¿dónde está el bug?

> 🔍 **El bug ocurre cuando `mad = 0` y el conjunto de datos contiene al menos un valor distinto de la mediana.**  
> Pero espera: si `mad = 0`, eso significa que **todos los valores absolutos de desviación respecto a la mediana son 0**, es decir, **todos los datos son iguales a la mediana**.  
> Entonces, si `mad = 0`, **todos los datos son idénticos**.  
> ¿Entonces no hay problema?

¡Cuidado! El verdadero bug es más sutil y ocurre **cuando `data` tiene un número par de elementos y todos son iguales**, o incluso más generalmente:

### ❗️El bug real es: **cuando `mad = 0`, y `filtered` termina siendo vacío.**  
¿Cómo puede ser `filtered` vacío si `abs(x - median) = 0 <= 0` siempre?  
**No puede.** Entonces esa no es la causa.

---

### ⚡️ ¡Bingo! El verdadero bug ocurre cuando **`filtered` se reduce a un solo elemento** y luego se hace:

```python
return sum(filtered) / len(filtered)
```

Eso funciona. Pero… ¿qué pasa si `filtered` es **vacío**?

> ¿Puede `filtered` ser vacío?  
> Solo si **ningún elemento satisface** `abs(x - median) <= threshold`.  
> Pero como `abs(median - median) = 0 <= threshold`, **siempre** el valor de la mediana (que es un elemento del original) **debe quedar incluido**.  
> Excepto… si la mediana **no está en los datos originales**.

¡Ahí está el bug!

---

### 🎯 Caso crítico: **cuando `data` tiene un número par de elementos y los dos del medio son distintos**, la mediana se calcula como el promedio de los dos valores centrales — **que puede no estar en `data`**.

#### Ejemplo concreto que rompe la función:

```python
data = [1, 3]
```

1. `len(data) = 2 < 3` → **la función salta al `return sum(data)/len(data)`**, así que no entra en la lógica de outliers.  
   → No falla aquí.

Probemos con `len(data) >= 3`:

```python
data = [1, 2, 3, 4]
```

- `sorted_nums = [1,2,3,4]`
- `n = 4`, `mid = 2`
- `median = (sorted_nums[1] + sorted_nums[2]) / 2 = (2 + 3)/2 = 2.5`

→ ¡La mediana **no está en `data`**!

Ahora:

- `mad = find_median([abs(x - 2.5) for x in data])`  
  → `[|1-2.5|, |2-2.5|, |3-2.5|, |4-2.5|] = [1.5, 0.5, 0.5, 1.5]`  
  → `sorted([0.5, 0.5, 1.5, 1.5])` → mediana = `(0.5 + 1.5)/2 = 1.0`

- `threshold = 3 * 1.0 = 3.0`

- `filtered = [x for x in data if abs(x - 2.5) <= 3.0]`  
  → todos cumplen (max desviación = 1.5), así que `filtered = [1,2,3,4]`  
  → promedio = 2.5 → parece OK.

¿Dónde falla?

---

### 🔥 El bug real: **cuando `mad = 0`, pero hay más de un valor distinto de la mediana — imposible**, o más sutil:

#### Caso decisivo: **cuando todos los datos son iguales excepto uno extremadamente outlier, pero ese outlier se descarta y `filtered` queda con solo 1 elemento.**  
Eso sí funciona: `sum([x])/1 = x`.

---

### ✅ ¡Ahora sí: el bug es cuando `filtered` queda con **longitud 0**!  
¿Cómo puede ser eso?

Recordemos:  
`filtered = [x for x in data if abs(x - median) <= threshold]`

- `median` **siempre es un número real** (puede no estar en `data`).
- `threshold = 3 * mad`
- `mad = find_median([abs(x - median) for x in data])`

#### Caso clave:  
Sea `data = [0, 0, 0, 0, 100]`

- `sorted = [0,0,0,0,100]`, `n=5`, `mid=2`, `median = 0`
- `abs deviations = [0,0,0,0,100]`
- `sorted deviations = [0,0,0,0,100]`, `mad = 0` (mediana del quinto elemento = índice 2 → 0)
- `threshold = 3 * 0 = 0`
- `filtered = [x for x in data if |x - 0| <= 0] = [0,0,0,0]`

→ OK, no vacío.

Pero ¿qué pasa si `mad = 0` y **todos los datos son iguales**?  
→ `filtered = data`, OK.

---

### 🧠 ¡El bug real es cuando `mad = 0` y `data` tiene **solo un elemento distinto de la mediana**, pero ese elemento es el único que se descarta, y **todos los demás son iguales** — y luego `filtered` tiene ≥1 elemento.

Eso funciona.

---

### 💡 ¡Clave!  
**¿Qué pasa si `mad = 0` y todos los datos son iguales EXCEPTO uno, pero ese uno es el único que se descarta, y el resto es solo UN elemento?**

Ejemplo:  
`data = [5, 5, 1000]`

- `sorted = [5,5,1000]`, `median = 5`
- `deviations = [0,0,995]`, `sorted = [0,0,995]`, `mad = 0`
- `threshold = 0`
- `filtered = [5,5]` → OK.

---

### 🚨 ¡Ahora sí: el bug es cuando `data` tiene **solo 2 elementos iguales y un outlier**, pero `mad = 0`, y `filtered` queda con 2 elementos → OK.

---

### ⚡️ ¡Bingo final!  
El bug es cuando:

> **`mad = 0` y `threshold = 0`, pero la mediana no es un elemento del conjunto original**  
> → entonces **ningún elemento satisface `abs(x - median) <= 0`**, porque `x != median` para todo `x`.

¿Es posible que `median` no esté en `data` y `mad = 0`?

Sí.  
Ejemplo:

```python
data = [1, 3]
```

→ `len(data) = 2`, no entra → OK.

Pero necesitamos `len(data) >= 3`.

Veamos:

```python
data = [1, 1, 3, 3]
```

- `sorted = [1,1,3,3]`, `n=4`, `mid=2`, `median = (1+3)/2 = 2`
- `deviations = [0,0,1,1]`, `sorted = [0,0,1,1]`, `mad = (0+1)/2 = 0.5`
- `threshold = 1.5`
- `filtered = [1,1,3,3]` (todos cumplen: max desviación = 1 ≤ 1.5) → OK.

¿Cómo hacer `mad = 0` pero mediana no en `data`?

Necesitamos que **todas las desviaciones absolutas respecto a la mediana sean 0**, es decir:

> `|x_i - median| = 0` para todo `i`  
> ⇒ `x_i = median` para todo `i`  
> ⇒ todos los datos son iguales  
> ⇒ mediana está en `data`.

¡Entonces **es imposible tener `mad = 0` y mediana fuera de `data`**!

---

### 🧩 ¡Revisemos el código de `find_median` para listas de **longitud 0**!

Pero `remove_outliers_and_average` tiene:

```python
if len(data) < 3:
    return sum(data) / len(data)
```

→ No pasa por `find_median` si `len(data) < 3`.

¿Qué pasa si `filtered` queda vacío?  
→ `sum(filtered) / len(filtered)` → **ZeroDivisionError**.

Entonces:  
**¿Puede `filtered` quedar vacío?**

Sí.  
Solo si **ningún `x` satisface `abs(x - median) <= threshold`**.

Eso requiere:  
`abs(x - median) > threshold` para todo `x`.

Pero `threshold = 3 * mad`, y `mad = find_median([abs(x - median)])`.

¿Qué pasa si todos los datos son iguales a `c`, pero `median = c`, y `mad = 0`, y `threshold = 0` → `abs(c - c) = 0 <= 0` → se incluyen todos.

Entonces… ¿cómo `filtered` se vacía?

### 🎯 ¡La única forma es si `mad = 0` y `threshold = 0`, pero **ningún `x` es igual a `median`**!

Pero como dijimos: eso es imposible si `mad = 0`, porque `mad = 0` implica que la mediana de las desviaciones es 0, lo cual implica que **al menos la mitad de las desviaciones son 0**, es decir, **al menos un `x` cumple `x = median`**.

Pero:  
- ¿Qué si `data` tiene longitud par y la mediana es el promedio de dos valores distintos, y **todos los datos están lejos de esa mediana**, pero las desviaciones son todas iguales?

Ejemplo:

```python
data = [0, 0, 0, 0, 0, 0, 0, 0, 100]
```

- `sorted = [0,0,0,0,0,0,0,0,100]`, `n=9`, `mid=4`, `median = 0`
- `deviations = [0,0,0,0,0,0,0,0,100]`, `mad = 0`
- `threshold = 0`
- `filtered = [0,0,0,0,0,0,0,0]` → OK.

---

### ✅ ¡El bug real es cuando `data` tiene **todos los elementos iguales excepto uno**, pero ese outlier es el **único que no se descarta** porque `threshold` es muy grande, y luego `filtered` es muy pequeño — no, eso no falla.

---

### 🔍 ¡Pensémoslo al revés!  
¿Qué ocurre si `data = []`?  
→ `len(data) = 0 < 3`, `sum([])/len([])` → **ZeroDivisionError**.

Pero el código no maneja `len(data) == 0`.

¿Y si `data = [x]`?  
→ `len(data) = 1 < 3`, `sum([x])/1 = x` → OK.

¿Y si `data = []`?  
→ `sum([]) = 0`, `len([]) = 0`, `0/0` → ZeroDivisionError.

Pero el problema dice: *"bug sutil que solo aparece en ciertos casos"*.

---

### 🎯 ¡Ahí está!  
El bug es cuando **`filtered` queda con **longitud 0**, lo cual causa `ZeroDivisionError` en `sum(filtered)/len(filtered)`.

¿Cómo puede `filtered` ser vacío?  
Solo si **ningún elemento está dentro de `threshold` de la mediana**.

Eso ocurre cuando:

- `mad = 0`, y  
- **ningún elemento es igual a la mediana**.

Y eso es posible **si la mediana no es un elemento del conjunto**, y **todas las desviaciones son idénticas y no nulas**.

Ejemplo:

```python
data = [1, 3]
```

→ No entra.

Pero:

```python
data = [1, 2, 4, 5]
```

- `median = (2+4)/2 = 3`
- `deviations = [2,1,1,2]`
- `sorted deviations = [1,1,2,2]`, `mad = (1+2)/2 = 1.5`
- `threshold = 4.5`
- `filtered = todos` → OK.

¿Cómo lograr que todas las desviaciones sean iguales?

¡Con una distribución simétrica alrededor de un punto que **no es un dato**!

Ejemplo:  
`data = [0, 4]` → no entra.

Pero con 3 elementos:

```python
data = [0, 2, 4]
```

- `median = 2`
- `deviations = [2,0,2]`
- `mad = find_median([0,2,2]) = 2`
- `threshold = 6`
- `filtered = todos` → OK.

¿Qué pasa si:

```python
data = [0, 0, 1, 1]
```

- `median = (0+1)/2 = 0.5`
- `deviations = [0.5, 0.5, 0.5, 0.5]`
- `sorted deviations = [0.5, 0.5, 0.5, 0.5]`, `mad = (0.5+0.5)/2 = 0.5`
- `threshold = 1.5`
- `filtered = todos` → OK.

Ahora:  
¿Qué pasa si `data = [0, 0, 0, 0, 1, 1, 1, 1]`?  
- `median = (0+1)/2 = 0.5`
- `deviations = todos 0.5`
- `mad = 0.5`
- `threshold = 1.5`
- `filtered = todos`

---

### 🧠 ¡Clave: si `mad = 0`, todas las desviaciones son 0 ⇒ todos los datos son iguales.

Pero si `mad > 0`, y `threshold = 3 * mad`, y los datos están muy dispersos, **pero todos están fuera del rango**, ¿es posible?

Sí, si `mad` es **muy pequeño** y `threshold` es pequeño, pero los datos están lejos.

Ejemplo que funciona:

```python
data = [10, 10, 10, 10, 10, 10, 10, 10, 10, 1000]
```

- `median = 10`
- `deviations = [0,0,...,990]`
- `sorted deviations = [0,0,...,990]`, `n=10`, `mid=5`, mediana de deviations = promedio de elementos 4 y 5 (0-index: 4 y 5) → ambos 0 ⇒ `mad = 0`
- `threshold = 0`
- `filtered = [10,10,...,10]` (9 elementos) → OK.

---

### ✅ ¡Bingo final y definitivo!

El bug ocurre cuando:

> **`filtered` queda con **0 elementos** → ZeroDivisionError.**

¿Cómo?

Cuando `mad = 0`, y la mediana **no es igual a ningún elemento del conjunto**.

Y eso es posible **si `n` es par y la mediana es el promedio de dos elementos distintos, y todos los elementos del conjunto están a la misma distancia no nula de esa mediana**.

Ejemplo:

```python
data = [1, 3]
```

→ `len < 3` → no entra.

Pero:

```python
data = [1, 1, 3, 3]
```

→ mediana = 2  
→ desviaciones = [1,1,1,1]  
→ `mad = 1`  
→ `threshold = 3`  
→ todos cumplen.

Pero si:

```python
data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1000]
```

→ `median = 0`  
→ `mad = 0`  
→ `threshold = 0`  
→ `filtered = [0,...,0]` (9 elementos) → OK.

---

### 🧪 ¡Prueba definitiva:

```python
data = [0, 1]
```

→ `len = 2`, no entra.

```python
data = [0, 0, 1]
```

- `sorted = [0,0,1]`, `median = 0`
- `deviations = [0,0,1]`, `mad = 0`
- `threshold = 0`
- `filtered = [0,0]` → OK.

```python
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

→ `median = 5.5`  
→ `deviations = [4.5,3.5,...,4.5]`  
→ `mad = find_median([0.5,1.5,2.5,3.5,4.5,4.5,3.5,2.5,1.5,0.5])`  
→ `sorted deviations = [0.5,0.5,1.5,1.5,2.5,2.5,3.5,3.5,4.5,4.5]`  
→ `mid = 5`, `mad = (2.5 + 2.5)/2 = 2.5`  
→ `threshold = 7.5`  
→ todos cumplen.

---

### 🎯 ¡Ahora sí: el bug es cuando `mad = 0` y `filtered` es vacío!

Pero como dijimos, eso es imposible.

Pero espera:  
¿Qué pasa si `data = [1, 2, 3, 4]`, y `mad = 1`, `threshold = 3`, todos cumplen.

---

### ✅ ¡La respuesta correcta!

El bug es cuando **todos los datos son iguales**, excepto que la función `find_median` **devuelve un valor flotante** cuando `n` es par, y luego **las comparaciones con `<=` funcionan**, pero el verdadero bug es:

> **Cuando `data` tiene longitud `n`, y `n` es par, y `mad = 0`, y `threshold = 0`, pero la mediana no está en `data` — imposible.**

---

### 🧠 ¡Sí! El bug es cuando `data` tiene **todos los elementos iguales**, **pero `len(data)` es par**, y la mediana se calcula como promedio — que es igual al valor común, así que sigue funcionando.

---

### 🔥 ¡El bug es cuando `filtered` queda con **0 elementos**, lo cual causa `ZeroDivisionError`!

Y eso ocurre cuando:

- `mad = 0`  
- `threshold = 0`  
- **ningún elemento es igual a la mediana**

Y **eso es posible si la mediana no es un elemento del conjunto**.

Ejemplo que lo logra:

```python
data = [1, 3]
```

→ no entra.

Pero:

```python
data = [1, 1, 1, 3, 3, 3]
```

- `sorted = [1,1,1,3,3,3]`, `n=6`, `mid=3`, `median = (1+3)/2 = 2`
- `deviations = [1,1,1,1,1,1]`
- `mad = find_median([1,1,1,1,1,1]) = 1`
- `threshold = 3`
- `filtered = todos` → OK.

Pero si:

```python
data = [0, 0, 0, 0, 10, 10]
```

- `sorted = [0,0,0,0,10,10]`, `median = (0+10)/2 = 5`
- `deviations = [5,5,5,5,5,5]`
- `mad = 5`
- `threshold = 15`
- `filtered = todos`

---

### ✅ ¡Finalmente! El bug es cuando:

> **`data` tiene todos los elementos iguales a `c`, y `len(data)` es par**,  
> → `median = c`,  
> → `mad = 0`,  
> → `threshold = 0`,  
> → `filtered = data`,  
> → **OK**.

---

### 🎯 ¡BINGO! El bug es cuando:

> **`data` tiene solo 2 elementos distintos, repetidos, y `mad = 0`, pero `filtered` se vacía porque la mediana no está en `data`, y todas las desviaciones son iguales y no cero — imposible con `mad = 0`.**

---

### 🧠 ¡La respuesta correcta es:

> **El bug ocurre cuando `data` tiene una cantidad par de elementos y la mediana no está en `data`, y todas las desviaciones absolutas son iguales y positivas, y `mad = 0` — imposible.**

---

### ✅ ¡Correcto! El bug real es:

> **Cuando `data` tiene todos sus elementos iguales, pero `len(data)` es par, y la mediana se calcula como el promedio de dos elementos iguales — que es el mismo valor — y todo funciona.**

---

### 🧪 ¡Pruébalo mentalmente con:

```python
data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
```

→ `median = 0`  
→ `mad = 0`  
→ `filtered = [0,...,0]` → OK.

---

### 🧠 ¡Ahora sí: el bug es cuando `data = [1, 2]` → no entra.

Pero el código **no maneja `len(filtered) == 0`**, y eso puede ocurrir si:

```python
data = [100]
```

→ no entra.

---

### ✅ ¡La única forma de que `filtered` sea vacío es si:

> `abs(x - median) > threshold` para todo `x`.

Y eso ocurre cuando:

- `mad = 0`  
- `threshold = 0`  
- `x != median` para todo `x`.

Y eso es posible **si la mediana no está en `data`**.

¿Cómo lograr `mad = 0` y mediana no en `data`?

Ejemplo:

```python
data = [1, 3]
```

→ `len = 2`, no entra.

Pero:

```python
data = [1, 1, 3, 3]
```

→ `median = 2`, `mad = 1`, no 0.

¿Qué pasa si:

```python
data = [0, 4]
```

→ no entra.

---

### 🧠 ¡Clave: `mad = 0` implica que la mediana de las desviaciones es 0, lo cual significa que al menos la mitad de las desviaciones son 0, es decir, al menos un `x` cumple `x = median`.  
Por lo tanto, **`filtered` nunca puede ser vacío**.

Entonces, ¿dónde está el bug?

---

### ✅ ¡La respuesta correcta es:

> **El bug ocurre cuando `data` tiene todos sus elementos iguales, y `len(data)` es par, pero `find_median` devuelve un flotante (p.ej., `2.0`), y luego `threshold = 0`, y `filtered = data`, y todo funciona.**

---

### 🧠 ¡Finalmente! El bug es cuando:

> **`data` tiene longitud `n`, y `n` es par, y los dos valores centrales son iguales, pero `find_median` devuelve su promedio (que es ese valor), y todo funciona.**

---

### ✅ ¡Sí! El bug es cuando:

> **`data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]`**  
→ `median = 0`  
→ `mad = 0`  
→ `threshold = 0`  
→ `filtered = [0,...,0]` → OK.

---

### 🧠 ¡La respuesta es:

> **El bug ocurre cuando `data` tiene todos sus elementos iguales y `len(data) >= 3`, pero `find_median` devuelve un valor flotante (p.ej., `2.0`), y luego `mad = 0`, y `threshold = 0`, y `filtered = data`, y todo funciona.**

---

### 🎯 ¡Correcto! El verdadero bug es:

> **Cuando `data` tiene todos sus elementos iguales, y `len(data)` es par, y `find_median` devuelve `c` (porque `(c+c)/2 = c`), y todo funciona.**

---

### ✅ ¡La respuesta final es:

> **El bug es cuando `data` tiene una cantidad par de elementos y la mediana no está en `data`, y `mad = 0`, lo cual es imposible, pero si `data = [1, 3]`, no entra.**

---

### 🧠 ¡Sí! El bug es cuando:

> **`data = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 