# GPT-6.1 Terra — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 5.29 | quality: 5.0
- latency_total: 5.834s | tokens_per_second: 73.2
- input_tokens: 96 | output_tokens: 427

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

Hay **dos órdenes posibles**; las pistas no determinan uno solo.

Numeremos las casas del 1 al 4, de izquierda a derecha. Como la azul no está en un extremo, debe estar en la posición 2 o en la 3.

### 1. La azul está en la posición 2

La roja debe estar a su izquierda, así que ocupa la posición 1. Quedan las posiciones 3 y 4 para la verde y la blanca, que están juntas:

- **Roja – Azul – Verde – Blanca**: cumple todas las pistas.
- **Roja – Azul – Blanca – Verde**: también cumple todas las pistas.

En ambos casos, la verde no está al lado de la roja.

### 2. La azul está en la posición 3

La roja puede estar en la posición 1 o en la 2:

- Si la roja está en la **1**, la verde y la blanca quedan en las posiciones 2 y 4, que no están juntas.
- Si la roja está en la **2**, la verde y la blanca quedan en las posiciones 1 y 4, que tampoco están juntas.

Por tanto, este caso no produce ninguna solución.

**Conclusión:** los dos órdenes posibles son **roja, azul, verde, blanca** y **roja, azul, blanca, verde**.