# Tencent Hy4 preview — deep_reasoning/logic_puzzle_constraint

- model_id: `tencent/hy4-preview`
- success: True  | final: 4.95 | quality: 5.0
- latency_total: 55.777s | tokens_per_second: 62.2
- input_tokens: 130 | output_tokens: 3472

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

Entendiendo **“al lado”** como **contigua**, el problema **no tiene una única solución**: hay **2 órdenes posibles**.

Numeremos las posiciones de izquierda a derecha como 1, 2, 3, 4.

Colores:  
- **R** = roja  
- **AZ** = azul  
- **V** = verde  
- **B** = blanca  

Sabemos que la azul no está en los extremos, así que solo puede estar en la posición **2** o **3**.

---

## Caso 1: la azul está en la posición 2

Como la roja está a la izquierda de la azul, la roja debe estar en la posición 1.

Esqueleto:

**R - AZ - _ - _**

Quedan las posiciones 3 y 4 para verde y blanca. Probemos:

1. **R - AZ - V - B**  
   - Verde está al lado de blanca: sí, posiciones 3 y 4.  
   - Verde no está al lado de roja: sí, posiciones 3 y 1 no son contiguas.  
   ✅ Válido.

2. **R - AZ - B - V**  
   - Verde está al lado de blanca: sí, posiciones 4 y 3.  
   - Verde no está al lado de roja: sí, posiciones 4 y 1 no son contiguas.  
   ✅ Válido.

---

## Caso 2: la azul está en la posición 3

La roja debe estar a la izquierda, así que puede estar en la posición 1 o 2.

### 2A: roja en posición 1

Esqueleto:

**R - _ - AZ - _**

Quedan las posiciones 2 y 4 para verde y blanca. Probemos:

1. **R - V - AZ - B**  
   - Verde y blanca no están al lado: posiciones 2 y 4.  
   ❌ Inválido.

2. **R - B - AZ - V**  
   - Verde y blanca no están al lado: posiciones 4 y 2.  
   ❌ Inválido.

### 2B: roja en posición 2

Esqueleto:

**_ - R - AZ - _**

Quedan las posiciones 1 y 4 para verde y blanca. Probemos:

1. **V - R - AZ - B**  
   - Verde y blanca no están al lado: posiciones 1 y 4.  
   ❌ Inválido.

2. **B - R - AZ - V**  
   - Verde y blanca no están al lado: posiciones 4 y 1.  
   ❌ Inválido.

---

## Soluciones posibles

Por tanto, los únicos órdenes válidos son:

1. **Roja - Azul - Verde - Blanca**  
2. **Roja - Azul - Blanca - Verde**

Con los datos dados, **no se puede decidir entre esas dos**: faltaría una condición adicional para obtener una única solución.