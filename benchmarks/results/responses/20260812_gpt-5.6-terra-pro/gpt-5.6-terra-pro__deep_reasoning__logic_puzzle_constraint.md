# GPT-5.6 Terra Pro — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 4.99 | quality: 5.0
- latency_total: 12.217s | tokens_per_second: 164.9
- input_tokens: 3668 | output_tokens: 2014

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

No hay una única solución: hay **dos órdenes posibles**.

Denotemos:

- R = roja  
- A = azul  
- V = verde  
- B = blanca  

La azul no puede estar en los extremos, así que solo puede estar en la posición 2 o 3.

## Caso 1: la azul está en la posición 2

Posiciones:

1. _  
2. Azul  
3. _  
4. _  

Como la roja está a la izquierda de la azul, necesariamente debe estar en la posición 1:

1. Roja  
2. Azul  
3. _  
4. _  

Quedan verde y blanca en las posiciones 3 y 4. Deben estar juntas, y lo están en ambos órdenes posibles:

- **Roja – Azul – Verde – Blanca**
- **Roja – Azul – Blanca – Verde**

En ambos casos la verde no está al lado de la roja: la roja está en la posición 1 y la verde en la 3 o la 4.

---

## Caso 2: la azul está en la posición 3

La roja debe estar a su izquierda, así que podría estar en la posición 1 o 2.

### 2a. Roja en la posición 1

Quedarían verde y blanca en las posiciones 2 y 4:

- Roja – Verde/Blanca – Azul – Verde/Blanca

Pero verde y blanca no estarían juntas, así que es imposible.

### 2b. Roja en la posición 2

Quedarían verde y blanca en las posiciones 1 y 4:

- Verde/Blanca – Roja – Azul – Verde/Blanca

Tampoco estarían juntas, así que es imposible.

---

Por tanto, las únicas posibilidades son:

1. **Roja – Azul – Verde – Blanca**  
2. **Roja – Azul – Blanca – Verde**  

La información dada no permite decidir cuál de esas dos es la correcta.