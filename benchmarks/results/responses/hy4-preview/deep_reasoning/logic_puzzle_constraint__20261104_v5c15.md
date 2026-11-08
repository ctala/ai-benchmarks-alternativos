# Tencent Hy4 preview — deep_reasoning/logic_puzzle_constraint

- model_id: `tencent/hy4-preview`
- success: True  | final: 4.95 | quality: 5.0
- latency_total: 57.699s | tokens_per_second: 60.9
- input_tokens: 130 | output_tokens: 3511

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

Numeremos las posiciones de izquierda a derecha como **1, 2, 3, 4**.

Condiciones:

1. **Roja** está a la izquierda de **Azul**.
2. **Verde** está al lado de **Blanca**.
3. **Azul** no está en los extremos, así que solo puede estar en la posición **2** o **3**.
4. **Verde** no está al lado de **Roja**.

---

## Caso 1: la casa azul está en la posición 2

Si la azul está en 2, la roja debe estar a su izquierda, así que:

- Posición 1: **Roja**
- Posición 2: **Azul**

Quedan las posiciones 3 y 4 para **Verde** y **Blanca**. Como deben estar juntas, hay dos opciones:

### Opción A

**Roja - Azul - Verde - Blanca**

Comprobación:

- Roja está a la izquierda de azul: sí.
- Verde está al lado de blanca: sí, posiciones 3 y 4.
- Azul no está en un extremo: sí, está en la posición 2.
- Verde no está al lado de roja: sí, porque entre ellas está la azul.

✅ Válida.

### Opción B

**Roja - Azul - Blanca - Verde**

Comprobación:

- Roja está a la izquierda de azul: sí.
- Verde está al lado de blanca: sí, posiciones 4 y 3.
- Azul no está en un extremo: sí, está en la posición 2.
- Verde no está al lado de roja: sí, están separadas.

✅ Válida.

---

## Caso 2: la casa azul está en la posición 3

Si la azul está en 3, la roja debe estar en la posición 1 o 2.

### Subcaso 2.1: roja en la posición 1

Quedarían las posiciones 2 y 4 para verde y blanca.  
Pero la posición 2 y la 4 **no son adyacentes**, así que verde y blanca no pueden estar al lado.

❌ No válida.

### Subcaso 2.2: roja en la posición 2

Quedarían las posiciones 1 y 4 para verde y blanca.  
Pero la posición 1 y la 4 **no son adyacentes**, así que verde y blanca no pueden estar al lado.

❌ No válida.

---

## Conclusión

Con las condiciones dadas, **no hay una única solución**, sino dos órdenes posibles:

1. **Roja - Azul - Verde - Blanca**
2. **Roja - Azul - Blanca - Verde**

Si el problema espera una sola respuesta, falta alguna condición adicional.