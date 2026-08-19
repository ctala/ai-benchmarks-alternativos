# Gemini 3.7 Flash — deep_reasoning/logic_puzzle_constraint

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 5.26 | quality: 5.0
- latency_total: 15.679s | tokens_per_second: 130.4
- input_tokens: 94 | output_tokens: 2044

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

Para resolver este acertijo lógico, representemos las cuatro casas numeradas del **1 al 4 de izquierda a derecha**: `[ 1, 2, 3, 4 ]`.

Nuestras casas son: **Roja (R)**, **Azul (A)**, **Verde (V)** y **Blanca (B)**.

---

### **P