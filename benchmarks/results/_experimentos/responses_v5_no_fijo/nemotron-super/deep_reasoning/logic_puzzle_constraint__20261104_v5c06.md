# Nemotron 3 Super — deep_reasoning/logic_puzzle_constraint

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 3.53 | quality: 2.25
- latency_total: 16.752s | tokens_per_second: 96.0
- input_tokens: 108 | output_tokens: 1608

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

**Respuesta:**  
Las casas pueden estar en cualquiera de los dos órdenes siguientes (de izquierda a derecha):

1. **Rojo – Azul – Verde – Blanco**  
2. **Rojo – Azul – Blanco – Verde**

---

### Razonamiento paso a paso

Denotemos las posiciones de la calle como 1, 2, 3 y 4 (1 = extremo izquierdo, 4 = extremo derecho).  
Los colores son: **R** (rojo), **B** (azul), **G** (verde), **W** (blanco).

Las condiciones son:

1. **R está a la izquierda de B** → posición(R) < posición(B).  
2. **G está al lado de W** → |posición(G) – posición(W)| = 1.  
3. **B NO está en los extremos** → posición(B) ∈ {2, 3}.  
4. **G NO está al lado de R** → |posición(G) – posición(R)| ≠ 1.

---

#### 1. Probar la posición de B

**Caso A: B en la posición 2**  
- Por (1) R debe estar a la izquierda de B → la única posición disponible es 1.  
  → R = 1, B = 2.  
- Quedan las posiciones 3 y 4 para G y W.  
- Por (2) G y W deben ser adyacentes; las posiciones 3 y 4 sí lo son, así que pueden estar en cualquiera de los dos órdenes:  
  - G = 3, W = 4  
  - G = 4, W = 3  
- Verificamos (4): G no puede estar al lado de R (posición 1).  
  - Si G = 3 → distancia a R = 2 (no adyacente).  
  - Si G = 4 → distancia a R = 3 (no adyacente).  
  → Ambas opciones cumplen (4).

Así obtenemos dos soluciones válidas:

- 1 R, 2 B, 3 G, 4 W → **Rojo‑Azul‑Verde‑Blanco**  
- 1 R, 2 B, 3 W, 4 G → **Rojo‑Azul‑Blanco‑Verde**

**Caso B: B en la posición 3**  
- Por (1) R debe estar a la izquierda de B → R puede estar en 1 o en 2.  
  - *Subcaso B1:* R = 1, B = 3 → quedan posiciones 2 y 4 para G y W.  
    - Pero 2 y 4 no son adyacentes → viola (2).  
  - *Subcaso B2:* R = 2, B = 3 → quedan posiciones 1 y 4 para G y W.  
    - También 1 y 4 no son adyacentes → viola (2).  
- Ninguna subcasa funciona, portanto B **no** puede estar en la posición 3.

---

#### 2. Conclusión

La única posición posible para la casa azul es la 2, lo que obliga a la roja a estar en la 1.  
Las casas verde y blanco deben ocupar las posiciones 3 y 4, y pueden estar en cualquiera de los dos órdenes porque ambas cumplen con la condición de no estar al lado de la roja.

Por lo tanto, el orden de las casas de izquierda a derecha es **Rojo‑Azul‑Verde‑Blanco** o **Rojo‑Azul‑Blanco‑Verde**.  

Ambas disposiciones satisfacen todas las restricciones dadas.