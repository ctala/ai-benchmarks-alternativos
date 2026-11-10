# Claude Fable 5.2 — deep_reasoning/logic_puzzle_constraint

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 4.77 | quality: 5.0
- latency_total: 10.811s | tokens_per_second: 107.2
- input_tokens: 159 | output_tokens: 1159

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

Numero las posiciones de izquierda a derecha: 1, 2, 3, 4.

## Paso 1: ¿Dónde puede estar la azul?

La azul no está en los extremos, así que solo puede estar en la posición 2 o en la 3.

## Paso 2: Azul en la posición 3

La roja debe estar a su izquierda, es decir, en la posición 1 o 2.

- **Roja en 1:** quedan las posiciones 2 y 4 para verde y blanca. No son adyacentes, así que la verde no estaría al lado de la blanca. ❌
- **Roja en 2:** quedan las posiciones 1 y 4 para verde y blanca. Tampoco son adyacentes. ❌

La azul no puede estar en la posición 3.

## Paso 3: Azul en la posición 2

La roja debe estar a su izquierda, así que solo puede estar en la posición 1. Quedan las posiciones 3 y 4 para verde y blanca, que son adyacentes entre sí. Hay dos opciones:

- **Roja, Azul, Verde, Blanca**
  - Roja (1) a la izquierda de azul (2) ✅
  - Verde (3) al lado de blanca (4) ✅
  - Azul no está en un extremo ✅
  - Verde (3) no está al lado de roja (1) ✅

- **Roja, Azul, Blanca, Verde**
  - Roja (1) a la izquierda de azul (2) ✅
  - Verde (4) al lado de blanca (3) ✅
  - Azul no está en un extremo ✅
  - Verde (4) no está al lado de roja (1) ✅

## Conclusión

Con las pistas dadas, el acertijo tiene **dos soluciones válidas**:

1. **Roja – Azul – Verde – Blanca**
2. **Roja – Azul – Blanca – Verde**

Lo que sí queda determinado es que la roja está en la posición 1 y la azul en la 2. Las pistas no permiten decidir el orden de la verde y la blanca en las posiciones 3 y 4. La cuarta pista (verde no al lado de roja) no descarta nada, porque la azul siempre queda entre ellas. Haría falta una pista adicional, por ejemplo "la blanca está en un extremo", para tener una solución única.