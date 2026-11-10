# GPT-6.1 Terra — precision_datos/identificadores_fiscales_latam

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 9.12 | quality: 10.0
- latency_total: 2.479s | tokens_per_second: 54.9
- input_tokens: 226 | output_tokens: 136

## Entrada exacta (lo que recibió el modelo)

**system:**

Trabajas en el área de operaciones de una pyme. Tu respuesta se pega directo en una planilla, así que respondes SOLO con los datos pedidos, uno por línea y en el orden pedido. Sin numeración, sin viñetas, sin comillas, sin encabezados y sin explicación.

**user:**

Formatea estos identificadores fiscales de clientes según la convención de cada país. No cambies ningún carácter, solo el formato:
- CUIT (Argentina): XX-XXXXXXXX-X
- NIT (Colombia): XXX.XXX.XXX-D
- RFC (México): los 13 caracteres seguidos, en mayúsculas, sin espacios

CUIT de Textiles del Plata: 30712345671
CUIT de Martina Ríos: 20312456789
NIT de Andes Logística: 9001234568
NIT de Café Origen: 8300547895
RFC de Ana Peña Gómez: peña 900228 5t9
RFC de Luis Molina Lozano: molo 790101 o19


## Respuesta completa

30-71234567-1
20-31245678-9
900.123.456-8
830.054.789-5
PEÑA9002285T9
MOLO790101O19