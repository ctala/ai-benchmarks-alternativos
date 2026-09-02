# Gemma 4 31B — deep_reasoning/logic_puzzle_constraint

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 5.4 | quality: 5.0
- latency_total: 19.537s | tokens_per_second: 284.5
- input_tokens: 113 | output_tokens: 5559

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

Para resolver este acertijo, vamos a analizar las posiciones de las 4 casas (1, 2, 3 y 4) de izquierda a derecha, probando las posibilidades basadas en las restricciones dadas.

### 1. Análisis de la Casa Azul (B)
La pista dice: **"La casa azul NO está en los extremos"**.
Esto significa que la casa azul solo puede estar en la **posición 2** o en la **posición 3**.

---

### 2. Probando la Posibilidad A: Casa Azul en la posición 3
Si la casa azul está en la posición 3: `_ , _ , Azul , _`

*   **Restricción de la Casa Roja (R):** "La casa roja está a la izquierda de la azul". Entonces la roja podría estar en la posición 1 o 2.
    *   **Caso A1 (Roja en 1):** `Roja , _ , Azul , _` $\rightarrow$ Quedan libres las posiciones 2 y 4.
    *   **Caso A2 (Roja en 2):** `_ , Roja , Azul , _` $\rightarrow$ Quedan libres las posiciones 1 y 4.
*   **Restricción de la Casa Verde (G) y Blanca (W):** "La casa verde está al lado de la blanca". Esto significa que deben estar en posiciones consecutivas (adyacentes).
    *   En el **Caso A1**, las posiciones{2, 4} no están juntas. **(Imposible)**.
    *   En el **Caso A2**, las posiciones{1, 4} no están juntas. **(Imposible)**.

**Conclusión:** La casa azul **no puede** estar en la posición 3.

---

### 3. Probando la Posibilidad B: Casa Azul en la posición 2
Si la casa azul está en la posición 2: `_ , Azul , _ , _`

*   **Restricción de la Casa Roja (R):** "La casa roja está a la izquierda de la azul". Como la azul está en la posición 2, la roja **obligatoriamente** debe estar en la posición 1.
    *   Estado actual: `Roja , Azul , _ , _`
*   **Restricción de la Casa Verde (G) y Blanca (W):** "La casa verde está al lado de la blanca". Solo quedan las posiciones 3 y 4, que son adyacentes. Por lo tanto, la verde y la blanca deben ocupar esos lugares.
    *   Esto nos deja dos órdenes posibles:
        1.  `Roja , Azul , Verde , Blanca`
        2.  `Roja , Azul , Blanca , Verde`
*   **Restricción final: "La casa verde NO está al lado de la roja"**.
    *   En la opción 1 (`Roja, Azul, Verde, Blanca`), la Roja está en la posición 1 y la Verde en la {3}. **No están al lado**. (Válido).
    *   En la opción 2 (`Roja, Azul, Blanca, Verde`), la Roja está en la posición 1 y la Verde en la {4}. **No están al lado**. (Válido).

---

### Resultado Final

Ambas configuraciones cumplen estrictamente con todas las reglas proporcionadas. El orden de las casas de izquierda a derecha es:

**Posibilidad 1:**
1. **Roja**
2. **Azul**
3. **Verde**
4. **Blanca**

**Posibilidad 2:**
1. **Roja**
2. **Azul**
3. **Blanca**
4. **Verde**