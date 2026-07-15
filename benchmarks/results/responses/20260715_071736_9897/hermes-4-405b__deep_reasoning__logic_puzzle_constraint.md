# Hermes 4 405B — deep_reasoning/logic_puzzle_constraint

- model_id: `nousresearch/hermes-4-405b`
- success: True  | final: 5.02 | quality: 5.0
- latency_total: 13.75s | tokens_per_second: 29.2
- input_tokens: 130 | output_tokens: 402
- judge_score: 4.4 | justificación: 

## Respuesta completa

Para resolver este problema, analicemos las condiciones una por una y probemos diferentes posibilidades:

1. La casa roja está a la izquierda de la azul, pero no necesariamente adyacente.
2. La casa verde está al lado de la blanca.
3. La casa azul no está en los extremos.
4. La casa verde no está al lado de la roja.

Empecemos con la casa azul. Como no está en los extremos, solo puede estar en la segunda o tercera posición.

Caso 1: Casa azul en la segunda posición
- Si la casa azul está en la segunda posición, la roja debe estar en la primera (por la condición 1).
- Entonces, las casas verde y blanca deben estar en las posiciones tercera y cuarta (por la condición 2).
- Sin embargo, esto violaría la condición 4, ya que la casa verde estaría al lado de la roja.

Caso 2: Casa azul en la tercera posición
- Si la casa azul está en la tercera posición, la roja debe estar en la primera o segunda posición (por la condición 1).
- Si la casa roja está en la primera posición, la casa verde y blanca deben estar en la segunda y cuarta posición (por la condición 2).
- Sin embargo, esto violaría la condición 4, ya que la casa verde estaría al lado de la roja.
- Por lo tanto, la casa roja debe estar en la segunda posición, la casa verde en la cuarta y la blanca en la primera (por la condición 2).
- Este arreglo satisface todas las condiciones.

Por lo tanto, el orden de las casas de izquierda a derecha es: blanca, roja, azul, verde.