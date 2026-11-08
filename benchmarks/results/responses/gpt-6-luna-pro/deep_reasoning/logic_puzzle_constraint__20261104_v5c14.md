# GPT-6 Luna Pro — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 5.52 | quality: 5.0
- latency_total: 11.164s | tokens_per_second: 135.1
- input_tokens: 2976 | output_tokens: 1508

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

No hay un único orden: **hay dos posibilidades**. Numeremos las casas del 1 al 4, de izquierda a derecha.

1. **La azul no puede estar en los extremos**, así que solo puede ocupar la posición 2 o la 3.

2. **Si la azul está en la posición 2**, la roja debe estar a su izquierda; por tanto, la roja va en la posición 1. Quedan las posiciones 3 y 4 para la verde y la blanca. Como son contiguas, cumplen la condición de estar al lado. Además, la verde en la posición 3 no está al lado de la roja en la 1. Se obtienen:
   - **Roja – Azul – Verde – Blanca**
   - **Roja – Azul – Blanca – Verde**

3. **Si la azul está en la posición 3**, la roja podría estar en la posición 1 o en la 2:
   - Si la roja está en la 1, la verde y la blanca quedan en las posiciones 2 y 4: no están juntas.
   - Si la roja está en la 2, la verde y la blanca quedan en las posiciones 1 y 4: tampoco están juntas.

Por tanto, los únicos órdenes posibles son **Roja – Azul – Verde – Blanca** y **Roja – Azul – Blanca – Verde**.