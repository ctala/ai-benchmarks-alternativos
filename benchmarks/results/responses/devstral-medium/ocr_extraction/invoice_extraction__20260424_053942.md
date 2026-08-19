# Devstral Medium — ocr_extraction/invoice_extraction

- model_id: `mistralai/devstral-medium`
- success: True  | final: 7.05 | quality: 6.28
- latency_total: 2.791s | tokens_per_second: 131.5
- input_tokens: 519 | output_tokens: 367
- judge_score: 2.6 | justificación: 

## Respuesta completa

{
  "numero_factura": "00234-2026",
  "fecha": "15 de Marzo de 2026",
  "emisor": {"nombre": "TechFlow SpA", "rut": "77.432.198-3", "direccion": "Av. Providencia 1234, Of. 501, Santiago"},
  "cliente": {"nombre": "Startup Labs Ltda.", "rut": "76.891.234-K", "direccion": "Calle Moneda 920, Santiago"},
  "items": [
    {"descripcion": "Licencia API Enterprise", "cantidad": 1, "precio_unitario": 890000, "total": 890000},
    {"descripcion": "Soporte Premium (3 meses)", "cantidad": 3, "precio_unitario": 150000, "total": 450000},
    {"descripcion": "Integracion N8N custom", "cantidad": 12, "precio_unitario": 45000, "total": 540000}
  ],
  "neto": 1880000,
  "iva": 357200,
  "total": 2237200,
  "condicion_pago": "30 dias",
  "banco": "Banco de Chile",
  "cuenta": "00-123-45678-90"
}