# Claude Fable 5 (suscripción) — agent_capabilities/model_as_router

- model_id: `claude-fable-5`
- success: True  | final: 7.17 | quality: 9.2
- latency_total: 13.933s | tokens_per_second: 55.4
- input_tokens: 2 | output_tokens: 772

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere razonamiento sobre volumen grande de texto para sintetizar patrones. DeepSeek es fuerte en razonamiento y su precio ($0.14/M) hace viable procesar 500 reviews sin que el costo escale."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Comunicación sensible que requiere empatía, tono honesto y manejo cuidadoso de la relación con el cliente. Es exactamente la fortaleza de Sonnet. Volumen bajo (1 email), el costo no importa."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "devstral",
    "razon": "Tarea de coding pura. Devstral es el mejor general y especialmente bueno en código, con buena velocidad. Alternativa válida: deepseek-v3 si el presupuesto es crítico."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación creativa simple y repetitiva en volumen. La velocidad ultra alta (200+ tok/s) permite iterar rápido sobre 20 variantes. Si los posts requieren tono muy cuidado, escalar los finales a claude-sonnet para pulido."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "gemini-flash-lite",
    "razon": "Validación estructural simple y de alto volumen: 100 llamadas cortas donde la velocidad y el bajo costo dominan. No requiere razonamiento profundo. Si la validación implica lógica de negocio compleja, usar minimax-m2.7 por su fortaleza en tool calling/formatos estructurados."
  }
]
```