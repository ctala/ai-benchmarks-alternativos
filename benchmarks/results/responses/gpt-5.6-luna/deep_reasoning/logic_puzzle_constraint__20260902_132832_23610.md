# GPT-5.6 Luna — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 5.63 | quality: 5.0
- latency_total: 7.834s | tokens_per_second: 81.8
- input_tokens: 96 | output_tokens: 641

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

No hay una única solución: existen **dos órdenes posibles**.

Llamemos a las posiciones 1, 2, 3 y 4 de izquierda a derecha.

### 1. Posibles posiciones de la casa azul

La azul no puede estar en los extremos, así que solo puede estar en la posición **2 o 3**.

### Caso 1: azul en la posición 2

La roja debe estar a la izquierda de la azul, por lo que necesariamente:

- Posición 1: roja
- Posición 2: azul

Quedan las posiciones 3 y 4 para la verde y la blanca. Como deben estar juntas, ambas posibilidades funcionan:

1. **Roja – Azul – Verde – Blanca**
2. **Roja – Azul – Blanca – Verde**

En ambos casos, la verde no está al lado de la roja.

### Caso 2: azul en la posición 3

La roja puede estar en la posición 1 o 2.

#### 2a. Roja en la posición 1

Quedan libres las posiciones 2 y 4 para la verde y la blanca. No están juntas, así que es imposible.

#### 2b. Roja en la posición 2

Quedan libres las posiciones 1 y 4 para la verde y la blanca. Tampoco están juntas, así que es imposible.

### Conclusión

Las condiciones no permiten determinar un único orden. Los dos órdenes posibles son:

- **Roja – Azul – Verde – Blanca**
- **Roja – Azul – Blanca – Verde**