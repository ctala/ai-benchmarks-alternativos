# GPT-6 Astra — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-6-astra`
- success: True  | final: 4.71 | quality: 5.0
- latency_total: 10.231s | tokens_per_second: 56.1
- input_tokens: 96 | output_tokens: 574

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

**Hay dos órdenes posibles; las pistas no determinan una solución única.**

Numeramos las posiciones del **1 al 4**, de izquierda a derecha.

### 1. ¿Dónde puede estar la casa azul?
Como no está en los extremos, solo puede ocupar la posición **2 o 3**.

### 2. Probamos con la azul en la posición 2
La roja debe estar a su izquierda, así que necesariamente ocupa la posición 1. Quedan las posiciones 3 y 4 para la verde y la blanca:

- **Roja – Azul – Verde – Blanca**: ✅ La verde está junto a la blanca y no está junto a la roja.
- **Roja – Azul – Blanca – Verde**: ✅ La verde está junto a la blanca y no está junto a la roja.

Ambos órdenes cumplen todas las pistas.

### 3. Probamos con la azul en la posición 3
La roja puede ocupar la posición 1 o la 2.

**Si la roja está en la posición 1**, quedan las posiciones 2 y 4:
- **Roja – Verde – Azul – Blanca**: ❌ La verde no está junto a la blanca y, además, está junto a la roja.
- **Roja – Blanca – Azul – Verde**: ❌ La verde no está junto a la blanca.

**Si la roja está en la posición 2**, quedan las posiciones 1 y 4:
- **Verde – Roja – Azul – Blanca**: ❌ La verde no está junto a la blanca y, además, está junto a la roja.
- **Blanca – Roja – Azul – Verde**: ❌ La verde no está junto a la blanca.

### Conclusión
Las únicas soluciones son:

1. **Roja – Azul – Verde – Blanca**
2. **Roja – Azul – Blanca – Verde**

Hace falta una pista adicional para elegir entre ellas.