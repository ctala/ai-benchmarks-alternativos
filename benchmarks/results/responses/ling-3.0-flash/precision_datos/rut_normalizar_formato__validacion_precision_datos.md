# Ling 3.0 Flash — precision_datos/rut_normalizar_formato

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 3.677s | tokens_per_second: 170.5
- input_tokens: 260 | output_tokens: 627

## Entrada exacta (lo que recibió el modelo)

**system:**

Trabajas en el área de operaciones de una pyme. Tu respuesta se pega directo en una planilla, así que respondes SOLO con los datos pedidos, uno por línea y en el orden pedido. Sin numeración, sin viñetas, sin comillas, sin encabezados y sin explicación.

**user:**

Estos RUT vienen de un formulario donde cada cliente los escribió a su manera. Déjalos todos en el formato 12.345.678-5 (puntos de miles, guion antes del dígito verificador y K en mayúscula). No cambies ningún dígito.

5126663-3
18765432 7
9.876.543-3
11111112-k
20.111.222-2
6000009-3
9000033-0
21.093.845 - 1


## Respuesta completa

5.126.663-3
18.765.432-7
9.876.543-3
11.111.112-K
20.111.222-2
6.000.009-3
9.000.033-0
21.093.845-1