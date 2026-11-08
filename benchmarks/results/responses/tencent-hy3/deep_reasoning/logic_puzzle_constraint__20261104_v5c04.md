# Tencent Hy3 — deep_reasoning/logic_puzzle_constraint

- model_id: `tencent/hy3`
- success: True  | final: 5.12 | quality: 5.0
- latency_total: 114.616s | tokens_per_second: 59.3
- input_tokens: 128 | output_tokens: 6799

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

Numeremos las casas de izquierda a derecha como **1, 2, 3 y 4**.

### 1. La casa azul no está en los extremos
Como hay 4 casas, los extremos son las posiciones 1 y 4.  
Por lo tanto, la casa **azul solo puede estar en la posición 2 o en la 3**.

---

### 2. Probamos cada posibilidad para la azul

#### Caso A: La azul está en la posición 3
- La roja debe estar a la izquierda de la azul, así que la roja tendría que estar en la 1 o en la 2.
- La verde y la blanca deben estar **al lado** (juntas).

Veamos las subcasos:

- Si la roja está en la 1: quedan libres las posiciones 2 y 4 para verde y blanca. Pero 2 y 4 **no son contiguas**, así que no pueden estar al lado. ❌
- Si la roja está en la 2: quedan libres las posiciones 1 y 4 para verde y blanca. Tampoco son contiguas. ❌

Además, la única pareja contigua libre sería (1,2), pero ahí tendría que ir la roja, no verde y blanca.  
**Conclusión: la azul no puede estar en la posición 3.**

---

#### Caso B: La azul está en la posición 2
- La roja debe estar a la izquierda de la azul. La única posición posible es la **1**.
- Quedan las posiciones 3 y 4 para la verde y la blanca.
- Como 3 y 4 son posiciones contiguas, se cumple que la verde está al lado de la blanca. ✅
- La roja está en 1, y la verde quedaría en 3 o en 4, así que **no está al lado de la roja**. ✅

Aquí sí hay solución. Como verde y blanca pueden invertirse, tenemos dos órdenes válidas:

1. **Roja – Azul – Verde – Blanca**
2. **Roja – Azul – Blanca – Verde**

---

### Respuesta final
Con los datos dados, el orden de izquierda a derecha es:

> **Roja, Azul, y luego Verde y Blanca en cualquier orden.**

Es decir, hay dos soluciones posibles:
- **Roja, Azul, Verde, Blanca**
- **Roja, Azul, Blanca, Verde**

No hay información suficiente para saber cuál de las dos últimas está antes.