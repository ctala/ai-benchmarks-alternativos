# MiniMax M2.7 (directo) — deep_reasoning/logic_puzzle_constraint

- model_id: `MiniMax-M2.7`
- success: True  | final: 5.05 | quality: 5.0
- latency_total: 55.605s | tokens_per_second: 36.8
- input_tokens: 131 | output_tokens: 2048

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

**Solución paso a paso**

Supongamos que las casas se numeran de izquierda a derecha  

\[
\text{posición 1},\; \text{posición 2},\; \text{posición 3},\; \text{posición 4}
\]

Cada posición puede estar ocupada por una de las cuatro casas de colores  

\[
R\;(roja),\; A\;(azul),\; V\;(verde),\; B\;(blanca)
\]

Las condiciones del problema son:

1. **R está a la izquierda de A**  → \( \text{pos}(R) < \text{pos}(A) \)
2. **V está al lado de B**     → \( \text{pos}(V) \) y \( \text{pos}(B) \) son consecutivos
3. **A no está en los extremos**  → \( \text{