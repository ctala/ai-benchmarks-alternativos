# Grok 4.6 — deep_reasoning/logic_puzzle_constraint

- model_id: `x-ai/grok-4.6`
- success: True  | final: 2.88 | quality: 2.25
- latency_total: 51.772s | tokens_per_second: 57.5
- input_tokens: 298 | output_tokens: 2975

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

Las 4 posiciones de izquierda a derecha se numeran 1-2-3-4. Los colores son R, B, G y W.

B no puede estar en un extremo, así que B está en 2 o en 3. Además R está estrictamente a la izquierda de B, y G-W ocupan un par de posiciones adyacentes (únicamente posibles: 1-2, 2-3 o 3-4), con la restricción extra de que G no es adyacente a R.

- Si G-W ocupan 1-2, las posiciones restantes son 3-4. B no puede ir a 4 (extremo) y si va a 3 entonces R queda en 4, violando que R esté a la izquierda de B. Imposible.
- Si G-W ocupan 2-3, las posiciones restantes son 1-4, ambas extremas, así que B quedaría en un extremo. Imposible.
- Si G-W ocupan 3-4, las posiciones restantes son 1-2. B no puede ir a 1 (extremo), así que B va a 2 y R a 1. Esto cumple R a la izquierda de B. G (esté en 3 o en 4) nunca es adyacente a R (que está en 1). Ambas sub-asignaciones de G y W son válidas.

Por tanto las únicas soluciones son R-B-G-W y R-B-W-G.

Orden de izquierda a derecha: rojo, azul, verde, blanca **o** rojo, azul, blanca, verde.