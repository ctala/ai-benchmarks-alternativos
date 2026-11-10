# Gemini 3.8 Flash — precision_datos/fechas_a_iso

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 6.695s | tokens_per_second: 114.3
- input_tokens: 263 | output_tokens: 765

## Entrada exacta (lo que recibió el modelo)

**system:**

Trabajas en el área de operaciones de una pyme. Tu respuesta se pega directo en una planilla, así que respondes SOLO con los datos pedidos, uno por línea y en el orden pedido. Sin numeración, sin viñetas, sin comillas, sin encabezados y sin explicación.

**user:**

Pasa estas fechas a formato ISO (AAAA-MM-DD). Ojo con el origen: las fechas numéricas de la planilla chilena vienen como día/mes/año y las del sistema de EE.UU. vienen como mes/día/año.

Planilla CL: 03/04/2026
Sistema EE.UU.: 03/04/2026
Planilla CL: 31/12/2025
Sistema EE.UU.: 11/09/2026
Correo: 4 de marzo de 2026
Correo: 1.º de julio de 2025
Factura: 7 ene. 2027
Contrato: 29-feb-2028
Planilla CL: 05-06-26
Sistema EE.UU.: Dec 1, 2025


## Respuesta completa

2026-04-03
2026-03-04
2025-12-31
2026-11-09
2026-03-04
2025-07-01
2027-01-07
2028-02-29
2026-06-05
2025-12-01