# Gemini 3.8 Flash — precision_datos/direcciones_despacho

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.9 | quality: 10.0
- latency_total: 5.85s | tokens_per_second: 116.6
- input_tokens: 289 | output_tokens: 682

## Entrada exacta (lo que recibió el modelo)

**system:**

Trabajas en el área de operaciones de una pyme. Tu respuesta se pega directo en una planilla, así que respondes SOLO con los datos pedidos, uno por línea y en el orden pedido. Sin numeración, sin viñetas, sin comillas, sin encabezados y sin explicación.

**user:**

Del siguiente mensaje de logística, copia la dirección de despacho de cada cliente, una por línea, en el orden en que aparecen los clientes y tal cual están escritas (solo la dirección, sin el nombre del cliente).

«Hola, te paso los despachos de mañana. A Distribuidora Los Aromos (fono +56 2 2345 1208) le va a Av. Providencia 1280, of. 1102, Providencia. Comercial Ñuble pidió que esta vez sea en Arturo Prat 1208, local 3, Chillán, no en la de siempre (Arturo Prat 1280). Ferretería Andina: Carrera 7 # 71-21, torre B, piso 4, Bogotá. Papelería Sur: Av. Insurgentes Sur 1602, piso 4, Col. Crédito Constructor, CDMX. Y Café Quillota: Pasaje Los Quillayes 455, depto. 32B, Viña del Mar.»


## Respuesta completa

Av. Providencia 1280, of. 1102, Providencia
Arturo Prat 1208, local 3, Chillán
Carrera 7 # 71-21, torre B, piso 4, Bogotá
Av. Insurgentes Sur 1602, piso 4, Col. Crédito Constructor, CDMX
Pasaje Los Quillayes 455, depto. 32B, Viña del Mar