# Qwen 3-Next 80B Thinking (NIM) — ocr_extraction/invoice_extraction

- model_id: `qwen/qwen3-next-80b-a3b-thinking`
- success: True  | final: 6.89 | quality: 7.96
- latency_total: 18.324s | tokens_per_second: 111.8
- input_tokens: 476 | output_tokens: 2048
- judge_score: 3.8 | justificación: 

## Respuesta completa

Okay, let's tackle this. I need to extract all the data from the scanned invoice and structure it into the exact JSON format specified. Let me read through the user's query again to make sure I understand.

The invoice content is provided with various fields: factura number, fecha, emisor details, cliente details, detalle table with items, neto, iva, total, condicion_pago, banco, and cuenta. The JSON structure has specific keys, so I need to map each part correctly.

First, the factura number is "00234-2026". In the JSON, it's "numero_factura", so that's straightforward. The date is "15 de Marzo de 2026". Need to check if the date format should be in a specific way, but the example shows "fecha": "" as a string, so probably keep it as is.

Emisor: nombre is "TechFlow SpA", RUT is "77.432.198-3", direccion is "Av. Providencia 1234, Of. 501, Santiago". So the emisor object should have those three fields.

Cliente: nombre "Startup Labs Ltda.", RUT "76.891.234-K", direccion "Calle Moneda 920, Santiago".

Now the items. The table has three entries. Let's parse each row.

First item: Descripcion "Licencia API Enterprise", Cant 1, Precio Unit "$890.000", Total "$890.000". Wait, but in the JSON structure, the items array has "descripcion", "cantidad" (as number), "precio_unitario" (number), "total" (number). So need to convert the price and total to numbers without the dollar sign and commas. For example, "$890.000" would be 890000. But in some regions, the comma is a thousands separator, but here it's written as $890.000 which might be 890,000. However, in the JSON, the numbers should be numeric, so 890000. Wait, but the example shows "precio_unitario": 0, so as a number, not string. So need to remove the dollar sign and the dots (since in Chile, they use . as thousand separator and , as decimal, but in this case, maybe the numbers are written with . as thousand separators). Let's see: $890.000 is 890,000. So in numeric terms, that's 890000. Similarly, $150.000 is 150000. So when extracting, convert those to numbers by removing the $ and the dots. Wait, but sometimes in Chile, the decimal separator is a comma, but for thousands they use dots. So 890.000 would be 890000. So yes, remove the $ and the dots. So for example, $890.000 becomes 890000. So in JSON, it's a number.

So for the first item:

descripcion: "Licencia API Enterprise"

cantidad: 1 (as number)

precio_unitario: 890000

total: 890000

Second item: "Soporte Premium (3 meses)", Cant 3, Precio Unit $150.000, Total $450.000. So precio_unitario 150000, total 450000.

Third item: "Integracion N8N custom", Cant 12, Precio Unit $45.000, Total $540.000. So precio_unitario 45000, total 540000.

Wait, $45.000 would be 45000. So yes.

Then neto: $1.880.000. So neto should be 1880000.

IVA: $357.200 → 357200

Total: $2.237.200 → 2237200

Condicion de pago: "30 dias"

Banco: "Banco de Chile"

Cuenta: "00-123-45678-90"

Now, check the JSON structure again. The "items" array must have objects with those keys. Also, all the numbers are numeric types, not strings.

Let me verify each part.

Numero_factura: "00234-2026" as a string.

Fecha: "15 de Marzo de 2026" as string.

Emisor: name, rut, direccion.

Cliente: same.

Items: each with descripcion (string), cantidad (number), precio_unitario (number), total (number).

Neto: number, iva: number, total: number.

Condicion_pago: string, banco: string, cuenta: string.

So for the RUTs, they have a hyphen, like "77.432.198-3" and "76.891.234-K". So those should be kept as strings.

Now, let's process each field.

Check the invoice data again:

FACTURA N° 00234-2026 → numero_factura: "00234-2026"

Fecha: 15 de Marzo de 2026 → "15 de Marzo de 2026"

Emisor: TechFlow SpA, RUT 77.432.198-3, direccion Av. Providencia 1234, Of. 501, Santiago

Cliente: Startup Labs Ltda., RUT 76.891.234-K, direccion Calle Moneda 920, Santiago

Detalle:

- Licencia API Enterprise | 1 | $890.000 | $890.000

So descripcion: "Licencia API Enterprise", cantidad 1, precio_unitario 890000, total 890000.

So in JSON, the price and total should be numbers, not strings. So 890000, not "890000".

Similarly, Soporte Premium: 3 units, $150.000 each → 150000, total 450000.

Integracion: 12 units, $45.000 each → 45000 per unit, total 540000 (12*45000=540000).

Neto: $1.880.000 → 1880000

IVA: 357200

Total: 2237200

Condicion_pago: "30 dias"

Banco: "Banco de Chile"

Cuenta: "00-123-45678-90"

Now, the JSON structure must match exactly. Let's make sure all keys are present.

Check the required structure:

{

"numero_factura": "",

"fecha": "",

"emisor": {"nombre": "", "rut": "", "direccion": ""},

"cliente": {"nombre": "", "rut": "", "direccion": ""},

"items": [{"descripcion": "", "cantidad": 0, "precio_unitario": 0, "total": 0}],

"neto": 0,

"iva": 0,

"total": 0,

"condicion_pago": "",

"banco": "",

"cuenta": ""

}

Yes, so all the fields are there.

Now, for the items array, each item must have those four fields. Let's structure them.

For the first item:

"descripcion": "Licencia API Enterprise",

"cantidad": 1,

"precio_unitario": 890000,

"total": 890000

Second item:

"descripcion": "Soporte Premium (3 meses)",

"cantidad": 3,

"precio_unitario": 150000,

"total": 450000

Third item:

"descripcion": "Integracion N8N custom",

"cantidad": 12,

"precio_unitario": 45000,

"total": 540000

Neto is 1880000, which is sum of all items' totals? Let's check: 890000 + 450000 + 540000 = 1,880,000. Yes, correct.

IVA: 19% of neto. 1,880,000 * 0.19 = 357,200. Correct.

Total: 1,880,000 + 357,200 = 2,237,200. Correct.

Now, the numbers in JSON should be without quotes. So neto: 1880000, not "188000