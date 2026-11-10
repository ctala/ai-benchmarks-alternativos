# GPT-OSS 20B — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 5.72 | quality: 5.0
- latency_total: 19.488s | tokens_per_second: 136.3
- input_tokens: 157 | output_tokens: 2656

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

**Solución paso a paso**

Denotemos las posiciones de las cuatro casas por \(1,2,3,4\) (de izquierda a derecha) y las letras  

- \(R\) = roja  
- \(B\) = azul  
- \(G\) = verde  
- \(W\) = blanca  

Las reglas del enunciado son:

1. **\(R\) está a la izquierda de \(B\)** (no necesariamente adyacente).  
2. **\(G\) está al lado de \(W\)** (son casas contiguas).  
3. **\(B\) no está en los extremos** → \(B\neq 1,4\).  
4. **\(G\) no está al lado de \(R\)**.

---

### 1. Posición de la casa azul

Como \(B\) no puede estar en los extremos, solo puede ocupar la posición 2 o la 3.

---

### 2. Analizamos cada posibilidad

#### a) \(B = 2\)

*Red debe estar a la izquierda de azul*, por lo que la única opción es \(R = 1\).

Quedan las posiciones 3 y 4 para \(G\) y \(W\).  
Para cumplir la regla 2, \(G\) y \(W\) deben estar contiguos; las posiciones 3‑4 sí lo son.  
La regla 4 también se cumple porque \(G\) está en la posición 3 o 4 y la roja está en la 1, no son contiguas.

**Dos arreglos posibles**:

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| R | B | G | W |

| 1 | 2 | 3 | 4 |
|---|---|---|---|
| R | B | W | G |

#### b) \(B = 3\)

Ahora \(R\) debe estar a la izquierda de \(B\), es decir \(R = 1\) o \(R = 2\).

- Si \(R = 1\): las posiciones restantes son 2 y 4 para \(G\) y \(W\).  
  Pero 2 y 4 **no son contiguas**, por lo que la regla 2 no se puede cumplir.  

- Si \(R = 2\): las posiciones restantes son 1 y 4 para \(G\) y \(W\).  
  Nuevamente 1 y 4 no son contiguas, por lo que tampoco se puede cumplir la regla 2.

En ninguna de las dos sub‑casas con \(B = 3\) se satisfacen las restricciones.

---

### 3. Conclusión

La única posición viable para la casa azul es \(B = 2\), y la roja debe estar en la posición 1.  
Las casas verdes y blancas pueden ocupar las posiciones 3 y 4 en cualquiera de los dos órdenes.

---

## Orden(es) de izquierda a derecha

| Posición | 1 | 2 | 3 | 4 |
|----------|---|---|---|---|
| Color 1  | R | B | G | W |
| Color 2  | R | B | W | G |

Por lo tanto, **hay dos soluciones posibles**:

1. **Roja – Azul – Verde – Blanca**  
2. **Roja – Azul – Blanca – Verde**

Ambas cumplen con todas las condiciones dadas.