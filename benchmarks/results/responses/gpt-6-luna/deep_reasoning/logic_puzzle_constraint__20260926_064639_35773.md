# GPT-6 Luna — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-6-luna`
- success: True  | final: 5.79 | quality: 5.0
- latency_total: 6.543s | tokens_per_second: 109.9
- input_tokens: 96 | output_tokens: 719

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

Numeremos las posiciones de izquierda a derecha: 1, 2, 3 y 4. La casa azul no puede estar en los extremos, así que solo puede ocupar la posición 2 o la 3.

**Caso 1: azul en la posición 2.**  
La roja debe estar a su izquierda, así que tiene que ir en la posición 1. Quedan las posiciones 3 y 4 para la verde y la blanca. Como están una al lado de la otra, ambas opciones cumplen las condiciones:

- **Roja – Azul – Verde – Blanca**
- **Roja – Azul – Blanca – Verde**

En los dos órdenes, la verde no está al lado de la roja.

**Caso 2: azul en la posición 3.**  
La roja tendría que estar en la posición 1 o en la 2.

- Si la roja está en la **1**, la verde y la blanca ocuparían las posiciones 2 y 4: no estarían una al lado de la otra.
- Si la roja está en la **2**, la verde y la blanca ocuparían las posiciones 1 y 4: tampoco estarían una al lado de la otra.

Por tanto, **hay dos órdenes posibles**, no uno solo:

1. **Roja – Azul – Verde – Blanca**
2. **Roja – Azul – Blanca – Verde**