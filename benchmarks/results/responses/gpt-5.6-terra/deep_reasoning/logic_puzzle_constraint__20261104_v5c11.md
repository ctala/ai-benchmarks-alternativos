# GPT-5.6 Terra — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 5.06 | quality: 5.0
- latency_total: 6.464s | tokens_per_second: 93.0
- input_tokens: 96 | output_tokens: 601

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

No hay una única solución: con las condiciones dadas hay **2 órdenes posibles**.

Denotemos:

- R = roja  
- A = azul  
- V = verde  
- B = blanca  

La casa azul no puede estar en los extremos, así que solo puede ocupar la posición 2 o la 3.

---

## Caso 1: La azul está en la posición 2

Orden parcial:

1. _  
2. Azul  
3. _  
4. _  

La roja debe estar a la izquierda de la azul. Como a la izquierda de la posición 2 solo está la posición 1:

1. Roja  
2. Azul  
3. _  
4. _  

Quedan verde y blanca para las posiciones 3 y 4. Como deben estar juntas, pueden colocarse de dos formas:

- Roja – Azul – Verde – Blanca  
- Roja – Azul – Blanca – Verde  

Comprobación: la verde no está al lado de la roja, porque hay una casa azul entre ellas. Ambas opciones sirven.

---

## Caso 2: La azul está en la posición 3

Orden parcial:

1. _  
2. _  
3. Azul  
4. _  

La roja debe estar a la izquierda de la azul, así que podría estar en la posición 1 o 2.

### 2a. Roja en la posición 1

Quedarían las posiciones 2 y 4 para verde y blanca:

- Posición 2 y posición 4 no están juntas.

Esto contradice que verde y blanca deben estar una al lado de la otra.

### 2b. Roja en la posición 2

Quedarían las posiciones 1 y 4 para verde y blanca:

- Tampoco están juntas.

También es imposible.

Por tanto, la azul no puede estar en la posición 3.

---

# Soluciones finales, de izquierda a derecha

1. **Roja – Azul – Verde – Blanca**  
2. **Roja – Azul – Blanca – Verde**  

Se necesitaría una pista adicional para decidir cuál de las dos es la única correcta.