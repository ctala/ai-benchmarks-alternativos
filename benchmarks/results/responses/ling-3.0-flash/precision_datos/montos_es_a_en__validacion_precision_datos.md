# Ling 3.0 Flash — precision_datos/montos_es_a_en

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 1.964s | tokens_per_second: 81.5
- input_tokens: 248 | output_tokens: 160

## Entrada exacta (lo que recibió el modelo)

**system:**

Trabajas en el área de operaciones de una pyme. Tu respuesta se pega directo en una planilla, así que respondes SOLO con los datos pedidos, uno por línea y en el orden pedido. Sin numeración, sin viñetas, sin comillas, sin encabezados y sin explicación.

**user:**

Estos montos vienen de una planilla en formato chileno (punto para miles, coma para decimales). El sistema de facturación de EE.UU. los necesita con coma para miles, punto decimal y SIEMPRE dos decimales (ejemplo: 1,234.50). Sin símbolo de moneda. El valor no puede cambiar.

1.234.567,89
12.000.000
999,9
1.000,05
7.450.003,10
0,5
1.234
45.678,00


## Respuesta completa

1,234,567.89
12,000,000.00
999.90
1,000.05
7,450,003.10
0.50
1,234.00
45,678.00