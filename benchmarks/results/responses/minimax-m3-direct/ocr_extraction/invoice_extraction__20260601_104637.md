# MiniMax M3 (directo / sub) — ocr_extraction/invoice_extraction

- model_id: `MiniMax-M3`
- success: True  | final: 7.34 | quality: 8.24
- latency_total: 13.756s | tokens_per_second: 41.1
- input_tokens: 597 | output_tokens: 565
- judge_score: 4.0 | justificación: La respuesta es precisa y relevante, con una estructura clara y datos útiles, aunque la profundidad es solo aceptable ya que no ofrece insights adicionales más allá de la información básica de la factura.

## Respuesta completa

<think>
The user wants me to extract data from the invoice and return it in a specific JSON structure. Let me parse the invoice carefully:

- numero_factura: 00234-2026
- fecha: 15 de Marzo de 2026
- emisor: TechFlow SpA, 77.432.198-3, Av. Providencia 1234, Of. 501, Santiago
- cliente: Startup Labs Ltda., 76.891.234-K, Calle Moneda 920, Santiago
- items: 
  - Licencia API Enterprise, 1, 890000, 890000
  - Soporte Premium (3 meses), 3, 150000, 450000
  - Integracion N8N custom, 12, 45000, 540000
- neto: 1880000
- iva: 357200
- total: 2237200
- condicion_pago: 30 dias
- banco: Banco de Chile
- cuenta: 00-123-45678-90

I should respond only with the JSON, no additional text.
</think>
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