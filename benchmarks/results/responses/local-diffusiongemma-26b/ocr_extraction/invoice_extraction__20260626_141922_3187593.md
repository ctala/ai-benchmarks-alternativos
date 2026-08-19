# DiffusionGemma 26B-A4B (DGX Spark Q8_0) — ocr_extraction/invoice_extraction

- model_id: `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0`
- success: True  | final: 6.99 | quality: 7.12
- latency_total: 29.012s | tokens_per_second: 52.9
- input_tokens: 0 | output_tokens: 1536
- judge_score: 3.2 | justificación: 

## Respuesta completa

thought
*   Role: Intelligent OCR system extracting structured data.
    *   Input: Text representation of a scanned invoice.
    *   Output: A specific JSON structure following a predefined schema.
    *   Constraint: Respond ONLY with the JSON, no extra text.

    *   `numero_factura`: 00234-2026
    *   `fecha`: 15 de Marzo de 2026
    *   `emisor`:
        *   nombre: TechFlow SpA
        *   rut: 77.432.198-3
        *   direccion: Av. Providencia 1234, Of. 501, Santiago
    *   `cliente`:
        *   nombre: Startup Labs Ltda.
        *   rut: 76.891.234-K
        *   direccion: Calle Moneda 920, Santiago
    *   `items`:
        1.  desc: Licencia API Enterprise, cant: 1, price: 890000, total: 890000
        2.  desc: Soporte Premium (3 meses), cant: 3, price: 150000, total: 450000
        3.  desc: Integracion N8N custom, cant: 12, price: 45000, total: 540000
    *   `neto`: 1880000
    *   `iva`: 357200
    *   `total`: 2237200
    *   `condicion_pago`: 30 dias
    *   `banco`: Banco de Chile
    *   `cuenta`: 00-123-45678-90

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

    *   Check schema match? Yes.
    *   Check numbers are integers? Yes.
    *   Check no extra text? Yes.{
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