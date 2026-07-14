# GPT-OSS 20B — deep_reasoning/logic_puzzle_constraint

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 5.62 | quality: 5.0
- latency_total: 22.16s | tokens_per_second: 92.4
- input_tokens: 144 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

## Respuesta completa

**Paso 1 – Analiza las restricciones básicas**

| Restricción | Qué implica |
|-------------|-------------|
| 1. “La casa roja está a la izquierda de la azul” | El rojo debe estar en una posición menor que la azul. |
| 2. “La casa verde está al lado de la blanca” | Verde y blanca ocupan dos puestos contiguos. |
| 3. “La casa azul NO está en los extremos” | El azul no puede estar en la posición 1 ni en la 4. |
| 4. “La casa verde NO está al lado de la roja” | Verde no puede estar inmediatamente a la izquierda ni a la derecha del rojo. |

Denotemos las posiciones de izquierda a derecha como **1 – 2 – 3 – 4**.

---

**Paso 2 – Coloca la casa azul**

Como la azul no está en los extremos, solo puede estar en la posición 2 o en la 3.

---

### Caso A – Azul en la posición 2  
| Posición | 1 | 2 | 3 | 4 |
|----------|---|---|---|---|
| Color    | ? | azul | ? | ? |

*Red debe estar a la izquierda de la azul*, por lo que el rojo tiene que ocupar la posición 1.

| Posición | 1 | 2 | 3 | 4 |
|----------|---|---|---|---|
| Color    | rojo | azul | ? | ? |

Quedan los colores verde y blanca.  
Para cumplir la regla 2 (verde contiguo a blanca) deben ocupar las posiciones 3 y 4 en algún orden.  
Ninguna de esas posiciones está adyacente al rojo (que está en la 1), por lo que la regla 4 (verde no al lado de rojo) también se satisface.

Por tanto, en este caso hay **dos** disposiciones válidas:

1. **rojo – azul – verde – blanca**  
2. **rojo – azul – blanca – verde**

---

### Caso B – Azul en la posición 3  
| Posición | 1 | 2 | 3 | 4 |
|----------|---|---|---|---|
| Color    | ? | ? | azul | ? |

*Red debe estar a la izquierda de la azul*, por lo que el rojo puede estar en la posición 1 o en la 2.

#### Sub‑caso B1 – Rojo en la posición 1  
| Posición | 1 | 2 | 3 | 4