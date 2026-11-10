# Tencent Hy4 — precision_datos/sku_confundibles_stock_cero

- model_id: `tencent/hy4`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 16.154s | tokens_per_second: 110.3
- input_tokens: 381 | output_tokens: 1781

## Entrada exacta (lo que recibió el modelo)

**system:**

Trabajas en el área de operaciones de una pyme. Tu respuesta se pega directo en una planilla, así que respondes SOLO con los datos pedidos, uno por línea y en el orden pedido. Sin numeración, sin viñetas, sin comillas, sin encabezados y sin explicación.

**user:**

Del siguiente reporte de inventario, copia solo los SKU de los productos con stock 0, en el orden del reporte. Los SKU distinguen entre cero y la letra O, entre uno, ele minúscula e i mayúscula, y entre «rn» y «m»: cópialos carácter por carácter.

BOL-0O1l-T02 — Bolso negro — stock: 4
MOC-rn0l-T10 — Mochila arena — stock: 0
MOC-m0l-T10 — Mochila arena — stock: 7
BIL-I1l0-T02 — Billetera gris humo — stock: 0
BIL-1lI0-T02 — Billetera gris humo — stock: 12
CRT-OI01-T01 — Cartera camel — stock: 2
CRT-0IO1-T01 — Cartera camel — stock: 0
CIN-Ol0I-TO1 — Cinturón negro — stock: 0
CIN-Ol0I-T01 — Cinturón negro — stock: 9
BOL-lm1O-T01 — Bolso burdeos — stock: 0
BOL-Im1O-T01 — Bolso burdeos — stock: 3


## Respuesta completa

MOC-rn0l-T10
BIL-I1l0-T02
CRT-0IO1-T01
CIN-Ol0I-TO1
BOL-lm1O-T01