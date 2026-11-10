# Gemma 4 31B — precision_datos/iban_clabe_formato

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.568s | tokens_per_second: 76.6
- input_tokens: 282 | output_tokens: 120

## Entrada exacta (lo que recibió el modelo)

**system:**

Trabajas en el área de operaciones de una pyme. Tu respuesta se pega directo en una planilla, así que respondes SOLO con los datos pedidos, uno por línea y en el orden pedido. Sin numeración, sin viñetas, sin comillas, sin encabezados y sin explicación.

**user:**

Necesito estos datos bancarios de proveedores en el formato que pide cada sistema:
- Las tres primeras: IBAN en formato electrónico (sin espacios).
- La cuarta: IBAN en formato impreso (grupos de 4 separados por un espacio).
- La quinta: CLABE de 18 dígitos seguidos, sin espacios.

ES91 2100 0418 4502 0005 1332
ES17 0049 1500 0512 3456 7890
ES44 2085 7300 4103 0017 2201
ES9121000418450200051332
002 180 70010012345 8


## Respuesta completa

ES9121000418450200051332
ES1700491500051234567890
ES4420857300410300172201
ES91 2100 0418 4502 0005 1332
002180700100123458