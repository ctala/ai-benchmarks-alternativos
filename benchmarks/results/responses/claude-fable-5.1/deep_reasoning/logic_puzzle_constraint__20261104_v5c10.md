# Claude Fable 5.1 — deep_reasoning/logic_puzzle_constraint

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 4.55 | quality: 5.0
- latency_total: 15.216s | tokens_per_second: 88.9
- input_tokens: 159 | output_tokens: 1352

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

## Planteamiento

Numeremos las posiciones de izquierda a derecha: **1, 2, 3, 4**.

Restricciones:
1. Roja a la izquierda de Azul (no necesariamente pegadas).
2. Verde al lado de Blanca.
3. Azul NO en los extremos → Azul está en la posición **2 o 3**.
4. Verde NO al lado de Roja.

La restricción 3 es la más limitante, así que empiezo por ahí.

---

## Caso A: Azul en la posición 3

Por la regla 1, Roja debe estar a la izquierda de Azul → Roja en la posición 1 o 2.

- **Roja en 1:** quedan libres las posiciones 2 y 4 para Verde y Blanca. Pero 2 y 4 no son adyacentes → viola la regla 2. ❌
- **Roja en 2:** quedan libres las posiciones 1 y 4. Tampoco son adyacentes → viola la regla 2. ❌

**Conclusión: Azul no puede estar en la posición 3.**

---

## Caso B: Azul en la posición 2

Por la regla 1, Roja debe estar a la izquierda → la única opción es **Roja en 1**.

Quedan las posiciones 3 y 4 para Verde y Blanca, que sí son adyacentes → cumple la regla 2. ✔

Ahora compruebo la regla 4 (Verde no al lado de Roja). Roja está en 1, así que su única vecina es la posición 2 (Azul). Verde está en 3 o 4, nunca pegada a Roja → cumple la regla 4 en ambas variantes. ✔

Dos subcasos:
- **Roja – Azul – Verde – Blanca** ✔ (cumple las 4 reglas)
- **Roja – Azul – Blanca – Verde** ✔ (cumple las 4 reglas)

---

## Respuesta

Con las pistas dadas, la **Roja va en la posición 1 y la Azul en la posición 2**; eso queda totalmente determinado. Sin embargo, el orden de Verde y Blanca en las posiciones 3 y 4 **no queda fijado**, porque ninguna regla distingue entre ellas una vez que están a la derecha de la Azul.

Soluciones válidas:
- **Roja, Azul, Verde, Blanca**
- **Roja, Azul, Blanca, Verde**

Para que el acertijo tuviera una única solución haría falta una pista adicional (por ejemplo, "la Blanca está en un extremo" daría Roja–Azul–Verde–Blanca).