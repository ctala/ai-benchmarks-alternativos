# MiniMax M3 (directo / sub) — ocr_extraction/business_card_extraction

- model_id: `MiniMax-M3`
- success: True  | final: 8.07 | quality: 9.28
- latency_total: 8.102s | tokens_per_second: 38.5
- input_tokens: 391 | output_tokens: 312
- judge_score: 5 | justificación: La respuesta es precisa y relevante, con datos exactos y claros, aunque incluye información adicional no solicitada, lo que no afecta la utilidad práctica.

## Respuesta completa

<think>
The user wants me to extract information from a business card and return it in a specific JSON format. Let me analyze the card:

Front:
- Name: MARIA JOSE RODRIGUEZ SOTO
- Position: Chief Technology Officer
- Company: NexaFlow Intelligence
- Slogan: "Transforming Data into Decisions"
- Phone: +56 9 8765 4321
- Email: mj.rodriguez@nexaflow.ai
- LinkedIn: linkedin.com/in/mjrodriguez

Back:
- Address: Av. Apoquindo 4500, Piso 12
- City: Las Condes, Santiago
- Country: Chile
- Website: www.nexaflow.ai

Let me format this into the requested JSON.
</think>
{
  "nombre_completo": "Maria Jose Rodriguez Soto",
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