# Tencent Hy4 — deep_reasoning/logic_puzzle_constraint

- model_id: `tencent/hy4`
- success: True  | final: 5.1 | quality: 5.0
- latency_total: 65.343s | tokens_per_second: 106.2
- input_tokens: 130 | output_tokens: 6937

## Entrada exacta (lo que recibió el modelo)

**user:**

Hay 4 casas en una calle, cada una de un color diferente.
- La casa roja esta a la izquierda de la azul (no necesariamente adyacente)
- La casa verde esta al lado de la blanca
- La casa azul NO esta en los extremos
- La casa verde NO esta al lado de la roja

En que orden estan las casas de izquierda a derecha?
Explica tu razonamiento paso a paso probando cada posibilidad.


## Respuesta completa

Para resolverlo de forma rigurosa y **probar cada posibilidad sin dejar ninguna fuera**, vamos a usar un árbol de decisiones. 

Numeraremos los lugares del **1 al 4** (de izquierda a derecha) y usaremos estas letras para evitar confusiones:
🔴 **R** = Roja | 🔵 **A** = Azul | 🟢 **V** = Verde | ⚪ **B** = Blanca

Existen **24 combinaciones iniciales** (4 × 3 × 2 × 1). En lugar de escribirlas en una lista aburrida, las agruparemos por la pista más restrictiva. Al sumar los grupos verificaremos que efectivamente evaluamos las 24.

---

### Paso 1: Partir por la casa Azul (Regla 3)
La regla dice: *"La Azul NO está en los extremos"*. Repartimos las 24 combinaciones según dónde está la **A**:

* ❌ **A en posición 1** → **6 combinaciones descartadas** (es extremo, y además la Roja no tendría lugar a su izquierda).
* ❌ **A en posición 4** → **6 combinaciones descartadas** (es extremo).
* 🔍 **A en posición 3** → **6 combinaciones** → pasan al **Caso II**.
* 🔍 **A en posición 2** → **6 combinaciones** → pasan al **Caso I**.

*(6 + 6 + 6 + 6 = 24. Ya tenemos el 100% mapeado).*

---

### Paso 2: Probar las 6 combinaciones del Caso II (`A = 3`)
Tenemos `[ ?, ?, A, ? ]`. Aplicamos la **Regla 1** (*R a la izquierda de A*):
* De entrada, mueren **2 combinaciones** donde la Roja estaba en el 4 (ej. `V-B-A-R`). Quedan 4 por probar.

**Subcaso II.a: Roja en 1** (2 combinaciones: `R-V-A-B` y `R-B-A-V`)
* Probamos la **Regla 2** (*V al lado de B*): A la Verde y la Blanca les tocan las posiciones **2 y 4**. Están separadas por la Azul en el 3. **No son adyacentes**. ❌ *Mueren ambas.*

**Subcaso II.b: Roja en 2** (2 combinaciones: `V-R-A-B` y `B-R-A-V`)
* Probamos la **Regla 2**: Les tocan las posiciones **1 y 4**. Mucho más separadas. **No son adyacentes**. ❌ *Mueren ambas.*

> 🧹 **Resultado:** Las **6 combinaciones** con la Azul en el 3 son imposibles. Las tachamos todas.

---

### Paso 3: Probar las 6 combinaciones del Caso I (`A = 2`)
Tenemos `[ ?, A, ?, ? ]`. Aplicamos la **Regla 1** (*R < 2*):
* El único sitio a la izquierda del 2 es el 1. Mueren de golpe **4 combinaciones** (donde la Roja intentaba estar en 3 o 4). 
* 👉 **La Roja está SI O SÍ en el 1:** `[ R, A, ?, ? ]`. Solo nos quedan **2 combinaciones** por evaluar.

Aplicamos la **Regla 2** (*V al lado de B*): Los huecos 3 y 4 **sí son vecinos** ✅. Probamos las 2 formas de sentarlos, cotejando la última regla (*V NO al lado de R*):

| Combinación restante | Regla 2 (V junto a B) | Regla 4 (V NO junto a R) | Veredicto |
| :--- | :--- | :--- | :--- |
| **1️⃣ `[R, A, V, B]`** | V(3) y B(4) ✅ | V está en 3, R en 1. La Azul(2) las separa ✅ | **¡VÁLIDA!** |
| **2️⃣ `[R, A, B, V]`** | B(3) y V(4) ✅ | V está en 4, R en 1. Hay 2 casas entre ellas ✅ | **¡VÁLIDA!** |

---

### 🏁 Conclusión (Y una pequeña trampa)

Al probar sistemáticamente las 24 posibilidades, el enunciado **no da una sola respuesta, sino DOS órdenes válidos**. Ambos cumplen las 4 reglas al pie de la letra:

1. 🔴 🔵 🟢 ⚪ → **Roja, Azul, Verde, Blanca**
2. 🔴 🔵 ⚪ 🟢 → **Roja, Azul, Blanca, Verde**

| Regla | Opción 1 | Opción 2 |
| :--- | :--- | :--- |
| Roja a la izq. de Azul | `1 < 2` ✅ | `1 < 2` ✅ |
| Verde al lado de Blanca | `3 y 4` ✅ | `4 y 3` ✅ |
| Azul fuera de extremos | Posición `2` ✅ | Posición `2` ✅ |
| Verde NO al lado de Roja | Separadas por la Azul ✅ | Separadas por 2 casas ✅ |

*(💡 **Nota:** Si este acertijo te lo pasaron esperando una única solución, le falta una pista de desempate. Por ejemplo, si añadieran *"La Verde está a la derecha de la Blanca"*, sobreviviría solo la **Opción 2**).*