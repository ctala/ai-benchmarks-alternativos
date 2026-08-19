# Kimi K2.5 — ocr_extraction/business_card_extraction

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 2.4 | quality: 1.25
- latency_total: 35.227s | tokens_per_second: 58.1
- input_tokens: 245 | output_tokens: 2048

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
  "nombre_completo": "Maria Jose Rodriguez Soto",
  "cargo": "Chief Technology Officer",
  "empresa":