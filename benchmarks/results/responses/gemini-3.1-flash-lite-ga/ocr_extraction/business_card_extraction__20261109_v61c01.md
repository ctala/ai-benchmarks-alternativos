# Gemini 3.1 Flash Lite (GA) — ocr_extraction/business_card_extraction

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 9.63 | quality: 10.0
- latency_total: 1.359s | tokens_per_second: 123.6
- input_tokens: 239 | output_tokens: 168

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un sistema de OCR. Extraes informacion de contacto de tarjetas de presentacion.

**user:**

Tengo una tarjeta de presentacion que dice:

Lado frontal:
  MARIA JOSE RODRIGUEZ SOTO
  Chief Technology Officer

  NexaFlow Intelligence
  "Transforming Data into Decisions"

  +56 9 8765 4321
  mj.rodriguez@nexaflow.ai
  linkedin.com/in/mjrodriguez

Lado trasero:
  Av. Apoquindo 4500, Piso 12
  Las Condes, Santiago, Chile
  www.nexaflow.ai

Extrae la informacion en este formato JSON exacto:
{
  "nombre_completo": "",
  "cargo": "",
  "empresa": "",
  "slogan": "",
  "telefono": "",
  "email": "",
  "linkedin": "",
  "direccion": "",
  "ciudad": "",
  "pais": "",
  "website": ""
}

Solo el JSON, nada mas.


## Respuesta completa

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