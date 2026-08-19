# Gemini 3.6 Flash — deep_reasoning/logic_puzzle_constraint

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 2.15 | quality: 0.75
- latency_total: 11.572s | tokens_per_second: 176.6
- input_tokens: 95 | output_tokens: 2044

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

Para encontrar el orden correcto de las casas de izquierda a derecha (posiciones 1, 2, 3 y 4), analizaremos cada pista y probaremos todas las posibilidades paso a paso.

---

### **Paso 1: Analizar la posición de la casa Azul**
* **Pista:** *"La casa azul NO está en los extremos"*
* **