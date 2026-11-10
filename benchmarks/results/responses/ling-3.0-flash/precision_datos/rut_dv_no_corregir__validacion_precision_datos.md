# Ling 3.0 Flash — precision_datos/rut_dv_no_corregir

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 2.768s | tokens_per_second: 142.7
- input_tokens: 304 | output_tokens: 395

## Entrada exacta (lo que recibió el modelo)

**system:**

Trabajas en el área de operaciones de una pyme. Tu respuesta se pega directo en una planilla, así que respondes SOLO con los datos pedidos, uno por línea y en el orden pedido. Sin numeración, sin viñetas, sin comillas, sin encabezados y sin explicación.

**user:**

Pasa estos RUT al formato que pide el sistema de cobranza: sin puntos, con guion antes del dígito verificador y K en mayúscula (ejemplo: 12345678-5).
Importante: se transcriben tal como vienen de la planilla de origen. Si algún dígito verificador no cuadra, NO lo recalcules ni lo corrijas: el equipo de cobranza revisa esos casos con el cliente.

12.345.678-5
7.654.321-6
15.234.567-4
9.000.008-k
18.765.432-8
22.468.013-9
16.437.290-1
13.579.246-0


## Respuesta completa

12345678-5
7654321-6
15234567-4
9000008-K
18765432-8
22468013-9
16437290-1
13579246-0