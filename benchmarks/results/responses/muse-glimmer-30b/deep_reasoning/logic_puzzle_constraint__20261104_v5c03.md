# Muse Glimmer 30B — deep_reasoning/logic_puzzle_constraint

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 5.25 | quality: 5.0
- latency_total: 16.424s | tokens_per_second: 164.2
- input_tokens: 146 | output_tokens: 2697

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

Con 4 puestos 1-2-3-4 de izquierda a derecha sean

R = pos. roja,  A = pos. azul,  V = pos. verde,  B = pos. blanca

* R < A
* |V-B| = 1
* A ∈ {2,3}
* |V-R| ≠ 1

El azul no puede estar en un extremo.

**A = 2**
Entonces R < 2 ⇒ R = 1. Es la única posibilidad para el azul en 2.
Ahora |V-R| ≠ 1 ⇒ |V-1| ≠ 1 ⇒ V ≠ 2. Quedan para V y B los
puestos 3 y 4.

|V-B| = 1 obliga a que V y B ocupen 3 y 4 en algún orden.

* V = 3, B = 4
  1 R  2 A  3 V  4 B
  R<A, A no es extremo, V junto a B y V no está junto a R.

* V = 4, B = 3
  1 R  2 A  3 B  4 V
  R<A, A no es extremo, V junto a B y V no está junto a R.

Las dos son compatibles con las cuatro condiciones. En particular
los dos primeros puestos quedan forzados

1. Roja  2. Azul

y los dos últimos son el par verde-blanca en cualquier orden.

**A = 3**
Entonces R < 3 ⇒ R = 1 ó 2.

*R = 1.* |V-R|≠1 ⇒ V≠2 y V≠3 por el azul. Queda V=4. La
adyacencia |V-B|=1 obliga a B=3 que ya está ocupado por el azul.
Imposible.

*R = 2.* |V-R|≠1 ⇒ V≠1,2,3. Queda V=4. La adyacencia obliga a
B=3 que ya está ocupado por el azul. Imposible.

Por tanto el azul no puede estar en el puesto 3. El único bloque
forzado es R A en las dos primeras casas y el par V-B ocupa las dos
últimas casas.

Si se quiere fijar un orden canónico para el par verde-blanca se
toma habitualmente V antes que B, es decir

Izquierda → Derecha : Roja – Azul – Verde – Blanca

que es la solución 1 R 2 A 3 V 4 B. La solución simétrica
1 R 2 A 3 B 4 V verifica exactamente las mismas cuatro condiciones.