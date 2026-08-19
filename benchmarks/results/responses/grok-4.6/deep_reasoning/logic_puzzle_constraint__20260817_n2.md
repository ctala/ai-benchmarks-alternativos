# Grok 4.6 — deep_reasoning/logic_puzzle_constraint

- model_id: `x-ai/grok-4.6`
- success: True  | final: 4.92 | quality: 5.0
- latency_total: 29.495s | tokens_per_second: 55.9
- input_tokens: 298 | output_tokens: 1649

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

Las 4 casas ocupan las posiciones 1-2-3-4 de izquierda a derecha. Los colores son R, B, G y W. Las restricciones son:

- pos(R) < pos(B)
- G y W ocupan posiciones adyacentes
- B no está en 1 ni en 4 (luego B está en 2 o en 3)
- G y R no son adyacentes

**Caso B en 2.**  
Entonces R sólo puede estar en 1. Quedan las posiciones 3 y 4 para G y W, que son adyacentes, así que la condición de vecindad se cumple automáticamente. Además G (esté en 3 o en 4) nunca es adyacente a R (que está en 1). Por tanto ambas asignaciones son válidas:

- R B G W
- R B W G

**Caso B en 3.**  
R puede estar en 1 o en 2.

- Si R está en 1, quedan las posiciones 2 y 4 para G y W, que no son adyacentes. Imposible.
- Si R está en 2, quedan las posiciones 1 y 4 para G y W, que no son adyacentes. Imposible.

Por tanto el único lugar posible para B es la posición 2 (con R forzosamente en 1). Las dos únicas soluciones son las ya indicadas: roja-azul-verde-blanca o roja-azul-blanca-verde.