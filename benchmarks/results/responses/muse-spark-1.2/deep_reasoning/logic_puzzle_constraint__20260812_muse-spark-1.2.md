# Muse Spark 1.2 — deep_reasoning/logic_puzzle_constraint

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 5.06 | quality: 5.0
- latency_total: 16.475s | tokens_per_second: 156.2
- input_tokens: 97 | output_tokens: 2574

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

Hay 2 soluciones válidas. Te explico por qué:

Tenemos 4 posiciones: `1 - 2 - 3 - 4` de izquierda a derecha.

Condiciones:
1.  `R < B` -> Roja a la izquierda de Azul
2.  `|G - W| = 1` -> Verde y Blanca juntas
3.  `B != 1 y B != 4` -> Azul solo puede estar en 2 o 3
4.  `|G - R| != 1` -> Verde y Roja NO juntas

### Paso 1: ¿Dónde puede estar la AZUL?
Por la condición 3, solo hay 2 casos: `B=2` o `B=3`. Probamos ambos.

### Paso 2: Caso B = 2
Si la Azul está en la posición 2, la Roja tiene que estar a su izquierda. Solo queda la posición 1.

> Tenemos: `1:R - 2:B - 3:? - 4:?`

Nos quedan Verde y Blanca para las posiciones 3 y 4. Como 3 y 4 son adyacentes, cumplen la condición 2 sin problema.

Falta la condición 4: Verde NO al lado de Roja.
Roja está en 1, solo la posición 2 está al lado de 1. Como en la 2 está la Azul, da igual donde pongamos la Verde:

*   Opción A: `1:R - 2:B - 3:G - 4:W` -> G en 3 no está al lado de R en 1. **VÁLIDA**
*   Opción B: `1:R - 2:B - 3:W - 4:G` -> G en 4 no está al lado de R en 1. **VÁLIDA**

Las dos cumplen las 4 condiciones.

### Paso 3: Caso B = 3
Si la Azul está en la posición 3, la Roja puede estar en 1 o en 2. Probamos:

**a) B=3 y R=1:**
> `1:R - 2:? - 3:B - 4:?`
Quedan las posiciones 2 y 4 para Verde y Blanca. Pero 2 y 4 NO están al lado, violan la condición 2. **DESCARTADO.**

**b) B=3 y R=2:**
> `1:? - 2:R - 3:B - 4:?`
Quedan las posiciones 1 y 4 para Verde y Blanca. Pero 1 y 4 NO están al lado, violan la condición 2. **DESCARTADO.**

Por lo tanto **es imposible que la Azul esté en la posición 3.**

### Conclusión

La única configuración posible es con la Azul en la posición 2 y la Roja en la 1.

> **Orden de izquierda a derecha: ROJA - AZUL - VERDE - BLANCA**

Y también es válida su variante intercambiando las dos últimas:

> **ROJA - AZUL - BLANCA - VERDE**

Ambas cumplen todas las condiciones. Si quieres la que aleja MÁS la Verde de la Roja, la segunda `R - B - W - G` es la ideal.

> **Nota:** Si interpretas "Verde al lado de Blanca" como bloque en orden `G-W` de izquierda a derecha, la única solución es `ROJA - AZUL - VERDE - BLANCA`.