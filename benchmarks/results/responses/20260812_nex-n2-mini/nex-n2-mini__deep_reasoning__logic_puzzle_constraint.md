# Nex-N2-Mini — deep_reasoning/logic_puzzle_constraint

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 5.9 | quality: 5.0
- latency_total: 7.361s | tokens_per_second: 177.7
- input_tokens: 103 | output_tokens: 1308

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

Con las pistas dadas **no hay un único orden posible**. Hay **dos soluciones**.

Sea el orden de izquierda a derecha:

1 — 2 — 3 — 4

### Paso 1: La casa azul no está en los extremos

Entonces la azul puede estar en la posición 2 o en la posición 3.

---

## Caso 1: La casa azul está en la posición 2

Entonces:

1 — Azul — 3 — 4

La casa roja está a la izquierda de la azul. Como la azul está en 2, la roja debe estar en 1.

1 — Roja — Azul — 3 — 4

Las casas verde y blanca quedan en las posiciones 3 y 4. Además, la verde debe estar al lado de la blanca, lo cual se cumple.

Además, la verde no puede estar al lado de la roja. Como la roja está en 1, la verde puede estar en 3 o en 4.

Esto da dos posibilidades:

1. **Roja, Azul, Verde, Blanca**
2. **Roja, Azul, Blanca, Verde**

---

## Caso 2: La casa azul está en la posición 3

Entonces:

1 — 2 — Azul — 4

La casa roja debe estar a la izquierda de la azul, así que la roja puede estar en 1 o en 2.

### Si la roja está en 1:

1 — Roja — Azul — 3 — 4

Las casas verde y blanca tendrían que estar en 3 y 4, pero 3 y 4 sí son adyacentes. Entonces esto también parece posible al principio.

Pero revisando bien: si la verde está en 3, está al lado de la roja en 1? No, no está al lado. Entonces esta opción también sería posible.

Corrección: en realidad sí se cumple.

Entonces también sería:

3. **Roja, Blanca, Azul, Verde**

Pero hay que comprobar la pista de que la verde no está al lado de la roja. En este caso la verde está en 4 y la roja en 1, no están al lado.

### Si la roja está en 2:

1 — 2 — Roja — Azul — 4

Las casas verde y blanca tendrían que estar en 1 y 4, pero no están al lado, así que no sirve.

---

Por lo tanto, las soluciones son:

1. **Roja, Azul, Verde, Blanca**
2. **Roja, Azul, Blanca, Verde**
3. **Roja, Blanca, Azul, Verde**

Todas cumplen las pistas. Por eso, con la información dada, **el orden no queda determinado de forma única**.