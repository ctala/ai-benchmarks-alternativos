# GPT-6 Luna Pro — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 5.58 | quality: 5.0
- latency_total: 9.488s | tokens_per_second: 168.0
- input_tokens: 3098 | output_tokens: 1594

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

1. **La azul debe estar en la posición 2 o 3**, porque no puede estar en un extremo.

2. **Si la azul está en la posición 2**, la roja tiene que estar en la posición 1. Las posiciones 3 y 4 quedan para la verde y la blanca. Como son contiguas, cumplen que la verde está al lado de la blanca; y la verde no queda al lado de la roja. Hay dos órdenes válidos:
   - **Roja – Azul – Verde – Blanca**
   - **Roja – Azul – Blanca – Verde**

3. **Si la azul está en la posición 3**, la roja tendría que estar en la posición 1 o 2:
   - Si la roja está en la posición 1, la verde y la blanca ocuparían las posiciones 2 y 4, que no son contiguas.
   - Si la roja está en la posición 2, ocuparían las posiciones 1 y 4, que tampoco son contiguas.

Por tanto, las únicas soluciones son **Roja – Azul – Verde – Blanca** y **Roja – Azul – Blanca – Verde**.