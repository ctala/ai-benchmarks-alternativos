# GPT-6 Luna — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-6-luna`
- success: True  | final: 5.68 | quality: 5.0
- latency_total: 8.376s | tokens_per_second: 69.8
- input_tokens: 96 | output_tokens: 585

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

Hay **dos órdenes posibles**, así que las pistas no determinan uno solo. Probemos las ubicaciones posibles de la casa azul, que no puede estar en los extremos:

1. **Azul en la posición 2.**  
   La roja debe estar a su izquierda, así que queda en la posición 1. Las posiciones 3 y 4 son para la verde y la blanca; como deben estar juntas, pueden ir en cualquiera de estos dos órdenes:
   - **Roja – Azul – Verde – Blanca**
   - **Roja – Azul – Blanca – Verde**  
   
   En ambos casos, la verde no está al lado de la roja.

2. **Azul en la posición 3.**  
   La roja tendría que estar en la posición 1 o en la 2. En ambos casos, las dos posiciones restantes para la verde y la blanca serían la 2 y la 4, o la 1 y la 4: no son posiciones contiguas. Por tanto, no se cumple que la verde esté al lado de la blanca.

**Conclusión:** las únicas posibilidades son **Roja – Azul – Verde – Blanca** y **Roja – Azul – Blanca – Verde**.