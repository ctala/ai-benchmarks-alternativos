# KAT Coder Pro v2.5 — deep_reasoning/logic_puzzle_constraint

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 5.17 | quality: 5.0
- latency_total: 18.769s | tokens_per_second: 109.1
- input_tokens: 104 | output_tokens: 2048

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



# 🏠 Solución del acertijo de las 4 casas

## Datos del problema

| Posición | 1 | 2 | 3 | 4 |
|----------|---|---|---|---|
| Color | ? | ? | ? | ? |

**Colores:** Roja, Azul, Verde, Blanca

**Restricciones:**
1. Roja está a la izquierda de Azul (Roja < Azul)
2. Verde está al lado de Blanca (adyacentes)
3. Azul NO está en los extremos (Azul ≠ 1, Azul ≠ 4)
4. Verde NO está al lado de Roja

---

## Paso 1: Analizar dónde puede estar la casa Azul

Por la restricción 3, Azul solo puede estar en la **posición 2 o 3**.

---

## Paso 2: Probar Azul en posición 3

Si **Azul = 3**, entonces por restricción 1 (Roja < Azul), Roja puede estar en posición 1 o 2.

| Subcaso | 1 | 2 | 3 | 4 | ¿Válido? |
|---------|---|---|---|---|----------|
| B1: Roja=1 | Roja | ? | Azul | ? | ❌ Las posiciones libres (2 y 4) **no son adyacentes**, no se puede cumplir restricción 2 |
| B2: Roja=2 | ? | Roja | Azul | ? | ❌ Las posiciones libres (1 y 4) **no son adyacentes**, no se puede cumplir restricción 2 |

**Conclusión:** Azul NO puede estar en posición 3.

---

## Paso 3: Probar Azul en posición 2

Si **Azul = 2**, entonces por restricción 1 (Roja < Azul), Roja debe estar en **posición 1**.

| Posición | 1 | 2 | 3 | 4 |
|----------|-----|-----|-----|-----|
| Color | Roja | Azul | ? | ? |

Quedan **Verde** y **Blanca** para las posiciones 3 y 4, que son adyacentes ✓

Hay dos formas de ubicarlas:

### Opción A: Verde en 3, Blanca en 4

| Posición | 1 | 2 | 3 | 4 |
|----------|-----|-----|-----|-----|
| Color | Roja | Azul | Verde | Blanca |

Verificamos:
- ✅ Roja(1) < Azul(2)
- ✅ Verde(3) al lado de Blanca(4)
- ✅ Azul(2) no está en extremos
- ✅ Verde(3) NO está al lado de Roja(1) → distancia = 2

### Opción B: Blanca en 3, Verde en 4

| Posición | 1 | 2 | 3 | 4 |
|----------|-----|-----|-----|-----|
| Color | Roja | Azul | Blanca | Verde |

Verificamos:
- ✅ Roja(1) < Azul(2)
- ✅ Verde(4) al lado de Blanca(3)
- ✅ Azul(2) no está en extremos
- ✅ Verde(4) NO está al lado de Roja(1) → distancia = 3

---

## ✅ Resultado

El acertijo tiene **dos soluciones válidas**:

| | 1ª | 2ª | 3ª | 