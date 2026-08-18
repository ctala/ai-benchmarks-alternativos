# Claude Opus 5 Fast — deep_reasoning/logic_puzzle_constraint

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 2.27 | quality: 1.5
- latency_total: 8.553s | tokens_per_second: 207.6
- input_tokens: 157 | output_tokens: 1776

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

## Planteamiento

Posiciones: **1 – 2 – 3 – 4** (de izquierda a derecha).
Colores: rojo, azul, verde, blanco.

Pistas:
1. Rojo está en una posición menor que azul.
2. Verde y blanco son adyacentes.
3. Azul no está en 1 ni en 4 → azul ∈ {2, 3}.
4. Verde no es adyacente a rojo.

## Prueba de casos según la posición del azul

**Caso A: azul en 3**

Rojo debe estar a su izquierda: rojo en 1 o en 2.

- *A1: rojo en 1.* Quedan las posiciones 2 y 4 para verde y blanco. Pero 2 y 4 **no son adyacentes** (los separa la 3). ❌ viola la pista 2.
- *A2: rojo en 2.* Quedan las posiciones 1 y 4 para verde y blanco. Tampoco son adyacentes. ❌ viola la pista 2.

→ El azul **no puede estar en 3**.

**Caso B: azul en 2**

Rojo debe estar a su izquierda, y la única posición libre a la izquierda es la 1 → **rojo en 1, azul en 2**.

Quedan las posiciones 3 y 4 para verde y blanco: son adyacentes ✔ (pista 2).
Además, el vecino de rojo (posición 1) es solo la casa 2, que es azul, así que verde nunca queda al lado de rojo ✔ (pista 4).

## Resultado

Las dos primeras casas están fijas:

**Rojo – Azul – {verde/blanco} – {blanco/verde}**

Es decir, hay **dos soluciones que cumplen todas las pistas**:

- Rojo – Azul – **Verde** – **Blanco**
- Rojo – Azul – **Blanco** – **Verde**

Las pistas, tal como están, no distinguen entre ambas: la condición "verde no está al lado de rojo" ya se satisface automáticamente al estar el azul en la posición 2, así que no aporta información para ordenar verde y blanco.

Para que la solución fuera única haría falta una pista extra, por ejemplo "el verde está a la derecha del blanco", lo que daría:

**Rojo – Azul – Blanco – Verde**