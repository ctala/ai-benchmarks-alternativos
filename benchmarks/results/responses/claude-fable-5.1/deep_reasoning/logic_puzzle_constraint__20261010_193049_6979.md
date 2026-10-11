# Claude Fable 5.1 — deep_reasoning/logic_puzzle_constraint

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 4.56 | quality: 5.0
- latency_total: 15.145s | tokens_per_second: 84.4
- input_tokens: 159 | output_tokens: 1279

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

# Resolución paso a paso

Numero las posiciones de izquierda a derecha: **1, 2, 3, 4**.

## Restricción más fuerte primero
**La azul NO está en los extremos** → la azul solo puede estar en la posición **2** o **3**. Esto divide el problema en dos casos.

---

## Caso A: Azul en la posición 3

La roja debe estar a la izquierda de la azul → roja en posición 1 o 2.

- **A1: Roja en 1** → quedan las posiciones 2 y 4 para verde y blanca. Pero la verde debe estar **al lado** de la blanca, y las posiciones 2 y 4 no son adyacentes. ❌
- **A2: Roja en 2** → quedan las posiciones 1 y 4 para verde y blanca. Tampoco son adyacentes. ❌

**Conclusión: la azul no puede estar en la posición 3.**

---

## Caso B: Azul en la posición 2

La roja debe estar a la izquierda de la azul → la única posición posible es la **1**.

Quedan las posiciones 3 y 4 para verde y blanca, que **sí son adyacentes** ✅.

Ahora verifico la última restricción (verde no al lado de la roja): la roja está en 1, y la verde estaría en 3 o en 4. Ninguna de esas es adyacente a la 1 ✅.

Esto deja dos sub-casos:

- **B1: Roja – Azul – Verde – Blanca**
  - Roja (1) a la izquierda de azul (2) ✅
  - Verde (3) al lado de blanca (4) ✅
  - Azul no en extremos ✅
  - Verde (3) no al lado de roja (1) ✅

- **B2: Roja – Azul – Blanca – Verde**
  - Roja (1) a la izquierda de azul (2) ✅
  - Verde (4) al lado de blanca (3) ✅
  - Azul no en extremos ✅
  - Verde (4) no al lado de roja (1) ✅

---

## Respuesta

Lo que se puede determinar con certeza es que la **roja está en la posición 1** y la **azul en la posición 2**. Sin embargo, con las pistas dadas, **el acertijo tiene dos soluciones válidas**:

1. **Roja – Azul – Verde – Blanca**
2. **Roja – Azul – Blanca – Verde**

Ninguna de las cuatro pistas distingue entre verde y blanca en las posiciones 3 y 4, así que haría falta una pista adicional (por ejemplo, "la blanca está en un extremo") para que la solución fuera única.