# Gemini 2.5 Pro — ocr_extraction/business_card_extraction

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 7.31 | quality: 8.16
- latency_total: 9.662s | tokens_per_second: 103.5
- input_tokens: 241 | output_tokens: 1000
- judge_score: 4.2 | justificación: 

## Respuesta completa

```json
{
  "nombre_completo": "MARIA JOSE RODRIGUEZ SOTO",
  "cargo": "Chief Technology Officer",
  "empresa": "NexaFlow Intelligence",
  "slogan": "Transforming Data into Decisions",
  "telefono": "+56 9 8765 4321",
  "email": "mj.rodriguez@nexaflow.ai",
  "linkedin": "linkedin.com/in/mjrodriguez",
  "direccion": "Av. Apoquindo 4500, Piso 12, Las Condes",
  "ciudad": "Santiago",
  "pais": "Chile",
  "website": "www.nexaflow.ai"
}
```