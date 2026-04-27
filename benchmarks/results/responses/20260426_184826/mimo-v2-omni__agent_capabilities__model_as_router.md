# MiMo-V2-Omni (multimodal) — agent_capabilities/model_as_router

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 7.18 | quality: 8.8
- latency_total: 35.363s | tokens_per_second: 27.1
- input_tokens: 290 | output_tokens: 957
- judge_score: 4.4 | justificación: 

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "deepseek-v3",
    "razon": "Requiere análisis profundo de texto no estructurado, razonamiento para identificar patrones y resúmenes precisos. Deepseek-v3 destaca en razonamiento y es económico para procesar grandes volúmenes de datos."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Necesita empatía, honestidad y tono apropiado para comunicación sensible con clientes. Claude-sonnet es especialista en contenido que requiere calidez humana y autenticidad."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Tarea de coding específica que requiere precisión técnica y lógica de programación. Deepseek-v3 es excelente para desarrollo de software y razonamiento algorítmico."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "gemini-flash-lite",
    "razon": "Generación de contenido variado y rápido para marketing. Gemini-flash-lite es ultra rápido y eficiente para crear múltiples versiones de contenido promocional."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Tarea de validación técnica que se beneficia de tool calling preciso. Minimax-m2.7 está optimizado para interacciones con herramientas y verificación sistemática de datos estructurados."
  }
]
```