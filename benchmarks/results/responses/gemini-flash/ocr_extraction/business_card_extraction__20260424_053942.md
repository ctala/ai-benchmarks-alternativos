# Gemini 2.5 Flash — ocr_extraction/business_card_extraction

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 7.7 | quality: 8.44
- latency_total: 3.362s | tokens_per_second: 50.6
- input_tokens: 241 | output_tokens: 170
- judge_score: 4.4 | justificación: 

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
  "direccion": "Av. Apoquindo 4500, Piso 12",
  "ciudad": "Las Condes, Santiago",
  "pais": "Chile",
  "website": "www.nexaflow.ai"
}
```