# Qwen 3.6 27B base (OpenRouter FP8) — ocr_extraction/invoice_extraction

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 6.47 | quality: 7.28
- latency_total: 30.98s | tokens_per_second: 66.1
- input_tokens: 526 | output_tokens: 2048
- judge_score: 3.2 | justificación: 

## Respuesta completa

Here's a thinking process:

1.  **Analyze User Input:**
   - **Input Document:** A scanned invoice with specific fields: Invoice Number, Date, Issuer (Name, RUT, Address), Client (Name, RUT, Address), Line Items (Description, Quantity, Unit Price, Total), Net, VAT (19%), Total, Payment Condition, Bank, Account.
   - **Required Output Format:** JSON with a specific schema.
   - **Constraint:** Respond SOLO with the JSON, no additional text.

2.  **Extract Data from Input:**
   - `numero_factura`: "00234-2026"
   - `fecha`: "15 de Marzo de 2026" (I'll keep it as is, or format it if needed, but the prompt says exact structure, so I'll stick to the string)
   - `emisor`:
     - `nombre`: "TechFlow SpA"
     - `rut`: "77.432.198-3"
     - `direccion`: "Av. Providencia 1234, Of. 501, Santiago"
   - `cliente`:
     - `nombre`: "Startup Labs Ltda."
     - `rut`: "76.891.234-K"
     - `direccion`: "Calle Moneda 920, Santiago"
   - `items`:
     - Item 1:
       - `descripcion`: "Licencia API Enterprise"
       - `cantidad`: 1
       - `precio_unitario`: 890000 (remove $ and .)
       - `total`: 890000
     - Item 2:
       - `descripcion`: "Soporte Premium (3 meses)"
       - `cantidad`: 3
       - `precio_unitario`: 150000
       - `total`: 450000
     - Item 3:
       - `descripcion`: "Integracion N8N custom"
       - `cantidad`: 12
       - `precio_unitario`: 45000
       - `total`: 540000
   - `neto`: 1880000
   - `iva`: 357200
   - `total`: 2237200
   - `condicion_pago`: "30 dias"
   - `banco`: "Banco de Chile"
   - `cuenta`: "00-123-45678-90"

3.  **Format Data into JSON:**
   I need to ensure all numeric values are numbers (not strings), and strings are properly quoted. I'll strip currency symbols and thousand separators for numbers.

   ```json
   {
     "numero_factura": "00234-2026",
     "fecha": "15 de Marzo de 2026",
     "emisor": {
       "nombre": "TechFlow SpA",
       "rut": "77.432.198-3",
       "direccion": "Av. Providencia 1234, Of. 501, Santiago"
     },
     "cliente": {
       "nombre": "Startup Labs Ltda.",
       "rut": "76.891.234-K",
       "direccion": "Calle Moneda 920, Santiago"
     },
     "items": [
       {
         "descripcion": "Licencia API Enterprise",
         "cantidad": 1,
         "precio_unitario": 890000,
         "total": 890000
       },
       {
         "descripcion": "Soporte Premium (3 meses)",
         "cantidad": 3,
         "precio_unitario": 150000,
         "total": 450000
       },
       {
         "descripcion": "Integracion N8N custom",
         "cantidad": 12,
         "precio_unitario": 45000,
         "total": 540000
       }
     ],
     "neto": 1880000,
     "iva": 357200,
     "total": 2237200,
     "condicion_pago": "30 dias",
     "banco": "Banco de Chile",
     "cuenta": "00-123-45678-90"
   }
   ```

4.  **Validate against Constraints:**
   - Structure matches exactly? Yes.
   - All data extracted? Yes.
   - Numbers are numeric? Yes.
   - Only JSON output? Yes.
   - Check for any formatting issues: The prompt asks for exact structure. I'll make sure keys match exactly. `precio_unitario` vs `precio_unitario` (prompt says `precio_unitario`). Wait, prompt says `precio_unitario`. I'll use that.
   - Check `cantidad`: prompt says `cantidad`. I'll use that.
   - Check `iva`: prompt says `iva`. I'll use that.
   - Check `condicion_pago`: prompt says `condicion_pago`. I'll use that.
   - All good.

   One minor thing: The prompt says `precio_unitario` in the schema. I'll use exactly that.
   The prompt says `cantidad` in the schema. I'll use exactly that.
   The prompt says `iva` in the schema. I'll use exactly that.
   The prompt says `condicion_pago` in the schema. I'll use exactly that.

   Let's double-check the values:
   Neto: 1.880.000 -> 1880000
   IVA: 357.200 -> 357200
   Total: 2.237.200 -> 2237200
   Prices: 890.000 -> 890000, 150.000 -> 150000, 45.000 -> 45000
   Totals: 890000, 450000, 540000
   All correct.

   I will generate the JSON exactly as requested. No extra text. Ensure proper JSON syntax.
   Ready.✅
   Output matches the required format. I will produce it now. 
   Self-Correction/Verification during thought: 
   Should I keep the date as string? Yes.
   Should I keep RUT as string? Yes.
   Should I keep account as string? Yes.
   Numbers should be numbers.
   All matches schema.
   Proceed. 
   Output generation. 
   ```json
   {
     "numero_factura": "00234-2026",
     "fecha": "15 de Marzo de 2026",
     "emisor": {
       "nombre": "TechFlow SpA",
       "rut": "77.432.198-3",
       "direccion": "Av. Providencia 1234, Of. 501, Santiago"
     },
     "cliente": {
       "nombre": "Startup Labs Ltda.",
       "rut": "76.891.234-K",
       "direccion": "Calle Moneda 920, Santiago"
     },
     "items": [
       {
         "descripcion": "Licencia API Enterprise",
         "cantidad": 1,
         "precio_unitario": 890000,
         "total": 890000
       },
       {
         "descripcion": "Soporte Premium (3 meses)",
         "cantidad": 3,
         "precio_unitario": 150000,
         "total": 450000
       },
       {
         "descripcion": "Integracion N8N custom",
         "cantidad": 12,
         "precio_unitario": 45000,
         "total": 540000
       }
     ],
     "neto": 1880000,
     "iva": 357200,
     "total": 2237200,
     "condicion_pago": "30 dias",
     "banco": "Banco de Chile",
     "cuenta": "00-123-45678-90"
   }
   ```
   Matches perfectly. Output matches constraint. Done. 
   One detail: The prompt schema uses `precio_unitario`, `cantidad`, `iva`, `condicion_pago`. I will strictly follow that.
   All good.✅
   Output matches. 
   Proceeds. 
