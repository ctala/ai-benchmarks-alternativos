# Muse Wonder — deep_reasoning/logic_puzzle_constraint

- model_id: `meta/muse-wonder`
- success: True  | final: 4.79 | quality: 5.0
- latency_total: 17.656s | tokens_per_second: 122.1
- input_tokens: 98 | output_tokens: 2156

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

Numeremos las posiciones de izquierda a derecha:

$$1 \quad 2 \quad 3 \quad 4$$

Los colores son: **Roja (R), Azul (A), Verde (V) y Blanca (B)**.

Vamos probando las posibilidades que deja cada pista.

### 1. La casa azul no está en los extremos

Por tanto, la azul no puede estar en la posición 1 ni en la 4.

Solo quedan dos posibilidades:

- Azul en la posición **2**
- Azul en la posición **3**

### 2. Probamos Azul en la posición 3

La roja está a la izquierda de la azul, así que la roja puede estar en la 1 o en la 2.

**Caso 3a: Roja en 1, Azul en 3**
```
1:R  2:?  3:A  4:?
```
Quedan las posiciones 2 y 4 para la verde y la blanca. Pero la 2 y la 4 **no están al lado**, y una pista dice que la verde está al lado de la blanca.

Este caso es imposible.

**Caso 3b: Roja en 2, Azul en 3**
```
1:?  2:R  3:A  4:?
```
Quedan las posiciones 1 y 4 para la verde y la blanca. Tampoco están al lado.

Este caso también es imposible.

Por tanto, **la azul no puede estar en la posición 3**.

### 3. Probamos Azul en la posición 2

La roja está a la izquierda de la azul. A la izquierda de la posición 2 solo está la posición 1, así que la roja está obligatoriamente en la 1:

```
1:R  2:A  3:?  4:?
```

Quedan las posiciones 3 y 4 para la verde y la blanca. Esas dos posiciones sí están al lado, así que se cumple la pista de que la verde está al lado de la blanca.

Ahora comprobamos la última pista: la verde no está al lado de la roja.

- Si la verde está en la 3, sus vecinas son la azul (2) y la blanca (4). No es la roja. **Válido**.
- Si la verde está en la 4, su única vecina es la blanca (3). No es la roja. **Válido**.

Por tanto, hay **dos** ordenaciones que cumplen todas las pistas:

**Posibilidad 1:**
```
Roja - Azul - Verde - Blanca
```
- Roja a la izquierda de Azul ✔
- Verde al lado de Blanca ✔
- Azul no está en un extremo ✔
- Verde no está al lado de Roja ✔

**Posibilidad 2:**
```
Roja - Azul - Blanca - Verde
```
- Roja a la izquierda de Azul ✔
- Verde al lado de Blanca ✔
- Azul no está en un extremo ✔
- Verde no está al lado de Roja ✔

### Conclusión

Las pistas determinan con seguridad las dos primeras casas:

**1ª: Roja, 2ª: Azul**

Pero no permiten distinguir el orden de las dos últimas: pueden ser **Verde-Blanca** o **Blanca-Verde**. Haría falta una pista adicional para obtener una única solución completa.