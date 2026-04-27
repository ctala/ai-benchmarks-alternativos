# DeepSeek V4 Pro — deep_reasoning/logic_puzzle_constraint

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 6.26 | quality: 8.18
- latency_total: 451.468s | tokens_per_second: 11.3
- input_tokens: 110 | output_tokens: 5102
- judge_score: 4.4 | justificación: 

## Respuesta completa

Tenemos 4 casas en una calle, cada una de un color diferente: roja (R), azul (A), verde (V) y blanca (B). Las posiciones de izquierda a derecha son 1, 2, 3 y 4.

**Condiciones:**
1. La casa roja está a la izquierda de la azul: posición de R < posición de A.
2. La casa verde está al lado de la blanca: |V - B| = 1.
3. La casa azul NO está en los extremos: A ≠ 1 y A ≠ 4.
4. La casa verde NO está al lado de la roja: |V - R| ≠ 1.

**Paso 1: Ubicación de la casa azul**
Por la condición 3, A solo puede estar en la posición 2 o 3.

**Paso 2: Probar A = 2**
Si A = 2, la condición 1 obliga a que R esté a su izquierda. La única posición disponible es la 1. Entonces R = 1.
Quedan las posiciones 3 y 4 para V y B.
- ¿Cumplen la condición 2? Sí, las posiciones 3 y 4 son adyacentes (|3-4|=1), por lo que V y B están juntas en cualquier orden.
- ¿Cumplen la condición 4? V estará en 3 o 4. R está en 1. En ningún caso son adyacentes (|3-1|=2, |4-1|=3 ≠ 1).

Por lo tanto, con A = 2 hay **dos órdenes válidos**:
- Posibilidad 1: R = 1, A = 2, B = 3, V = 4 → Roja, Azul, Blanca, Verde.
- Posibilidad 2: R = 1, A = 2, V = 3, B = 4 → Roja, Azul, Verde, Blanca.

**Paso 3: Probar A = 3**
Si A = 3, la condición 1 permite R = 1 o R = 2.
- Si R = 1, quedan las posiciones 2 y 4 para V y B. No son adyacentes (|2-4| = 2). **Inválido** (falla condición 2).
- Si R = 2, quedan las posiciones 1 y 4 para V y B. No son adyacentes (|1-4| = 3). **Inválido**.

Para A = 3 no hay ninguna solución posible.

**Conclusión**
Existen dos órdenes posibles que satisfacen todas las condiciones:
1. **Roja, Azul, Blanca, Verde**
2. **Roja, Azul, Verde, Blanca**