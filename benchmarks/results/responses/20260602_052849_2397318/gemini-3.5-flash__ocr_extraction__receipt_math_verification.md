# Gemini 3.5 Flash — ocr_extraction/receipt_math_verification

- model_id: `google/gemini-3.5-flash`
- success: True  | final: 5.75 | quality: 6.08
- latency_total: 10.685s | tokens_per_second: 191.3
- input_tokens: 364 | output_tokens: 2044
- judge_score: 4.0 | justificación: La respuesta extrae correctamente los datos de los ítems del recibo, pero no completa el cálculo para todos los ítems ni verifica el subtotal y la propina sugerida, lo que limita la profundidad y utilidad práctica.

## Respuesta completa

```json
{
  "items": [
    {
      "nombre": "Lomo vetado",
      "cantidad": 2,
      "precio_unitario": 18900,
      "precio_total": 37800
    },
    {
      "nombre": "Ensalada cesar",
      "