# Hermes 4 405B — deep_reasoning/logic_puzzle_constraint

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 7.06 | quality: 8.18
- latency_total: 17.119s | tokens_per_second: 36.5
- input_tokens: 130 | output_tokens: 624
- judge_score: 4.4 | justificación: 

## Respuesta completa

Para resolver este problema, analizamos paso a step las restricciones y comprobamos cada posibilidad:

1. **Casas y colores**: Hay 4 casas, cada una de un color diferente: rojo, azul, verde, blanco.
2. **Restricciones**:
   - La casa roja está a la izquierda de la azul.
   - La casa verde está al lado de la blanca.
   - La casa azul no está en los extremos.
   - La casa verde no está al lado de la roja.

**Paso 1: Posición de la casa azul**  
La casa azul no puede estar en los extremos (posición 1 o 4). Por lo tanto, debe estar en la posición 2 o 3.

**Paso 2: Posición de la casa roja**  
La casa roja debe estar a la izquierda de la azul. Si la azul está en la posición 2, la roja debe estar en la posición 1. Si la azul está en la posición 3, la roja debe estar en la posición 1 o 2.

**Caso 1: Azul en posición 2**  
- Azul en 2 → Roja en 1.  
- Verde no puede estar al lado de roja → Verde no puede estar en 2 (ya está azul).  
- Verde debe estar al lado de blanca → Si verde está en 3, blanca en 4.  
- Asignación: 1: roja, 2: azul, 3: verde, 4: blanca.  
- Comprobación:  
  - Roja (1) a la izquierda de azul (2) ✔️  
  - Verde (3) al lado de blanca (4) ✔️  
  - Azul (2) no en extremo ✔️  
  - Verde (3) no al lado de roja (1) ✔️  

**Caso 2: Azul en posición 3**  
- Azul en 3 → Roja en 1 o 2.  
- Si roja en 1:  
  - Verde no puede estar al lado de roja → No puede estar en 2.  
  - Verde debe estar al lado de blanca → Si verde en 4, blanca en 3 (pero azul está en 3) ✖️  
- Si roja en 2:  
  - Verde no puede estar al lado de roja → No puede estar en 1 o 3.  
  - Verde debe estar al lado de blanca → Si verde en 4, blanca en 3 (pero azul está en 3) ✖️  

**Conclusión**  
El único orden válido es: **Roja, Azul, Verde, Blanca** (de izquierda a derecha).