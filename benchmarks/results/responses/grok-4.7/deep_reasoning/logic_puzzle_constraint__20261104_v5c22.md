# Grok 4.7 — deep_reasoning/logic_puzzle_constraint

- model_id: `x-ai/grok-4.7`
- success: True  | final: 4.83 | quality: 5.0
- latency_total: 39.372s | tokens_per_second: 57.5
- input_tokens: 1334 | output_tokens: 2263

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

Hay dos órdenes posibles que cumplen todas las condiciones.

Colores: roja (R), azul (A), verde (V), blanca (B). Posiciones de izquierda a derecha: 1-2-3-4.

La azul no está en un extremo, así que solo puede ir en 2 o en 3.

**Caso azul en 3**  
La roja tiene que quedar a su izquierda (posición 1 o 2). Entonces verde y blanca ocupan las dos casillas que sobran, que nunca son contiguas:
- roja en 1 → quedan 2 y 4  
- roja en 2 → quedan 1 y 4  

En ambos subcasos verde y blanca no están al lado. Imposible.

**Caso azul en 2**  
La roja solo puede ir en 1 (único lugar a la izquierda de la azul). Quedan las posiciones 3 y 4 para verde y blanca, que sí son contiguas. La roja (posición 1) solo linda con la azul, así que la verde —esté en 3 o en 4— no está a su lado. Las dos disposiciones valen:
- R A V B  
- R A B V  

No hay más casos. Ambas satisfacen las cuatro condiciones; el orden no queda único.