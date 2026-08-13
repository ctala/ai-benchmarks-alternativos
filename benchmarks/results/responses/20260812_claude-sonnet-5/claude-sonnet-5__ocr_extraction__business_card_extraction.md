# Claude Sonnet 5 — ocr_extraction/business_card_extraction

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.87 | quality: 10.0
- latency_total: 3.566s | tokens_per_second: 68.7
- input_tokens: 373 | output_tokens: 245

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