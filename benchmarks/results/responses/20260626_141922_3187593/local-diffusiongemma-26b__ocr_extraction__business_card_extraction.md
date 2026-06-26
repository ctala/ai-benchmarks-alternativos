# DiffusionGemma 26B-A4B (DGX Spark Q8_0) — ocr_extraction/business_card_extraction

- model_id: `hf.co/unsloth/diffusiongemma-26B-A4B-it-GGUF:Q8_0`
- success: True  | final: 7.07 | quality: 7.04
- latency_total: 14.357s | tokens_per_second: 53.5
- input_tokens: 0 | output_tokens: 768
- judge_score: 3.4 | justificación: 

## Respuesta completa

thought
*   Role: OCR system extracting contact info from business cards.
    *   Input: Text representing front and back of a business card.
    *   Output format: A specific JSON structure.
    *   Constraint: "Only the JSON, nothing else."

    *   *Front:*
        *   Name: MARIA JOSE RODRIGUEZ SOTO
        *   Title: Chief Technology Officer
        *   Company: NexaFlow Intelligence
        *   Slogan: "Transforming Data into Decisions"
        *   Phone: +56 9 8765 4321
        *   Email: mj.rodriguez@nexaflow.ai
        *   LinkedIn: linkedin.com/in/mjrodriguez
    *   *Back:*
        *   Address: Av. Apoquindo 4500, Piso 12
        *   City: Las Condes, Santiago
        *   Country: Chile
        *   Website: www.nexaflow.ai

    *   `nombre_completo`: MARIA JOSE RODRIGUEZ SOTO
    *   `cargo`: Chief Technology Officer
    *   `empresa`: NexaFlow Intelligence
    *   `slogan`: Transforming Data into Decisions
    *   `telefono`: +56 9 8765 4321
    *   `email`: mj.rodriguez@nexaflow.ai
    *   `linkedin`: linkedin.com/in/mjrodriguez
    *   `direccion`: Av. Apoquindo 4500, Piso 12
    *   `ciudad`: Las Condes, Santiago
    *   `pais`: Chile
    *   `website`: www.nexaflow.ai

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

Ensure no extra text is included.```json
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