# GPT-OSS 20B — agent_capabilities/model_as_router

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 3.93 | quality: 2.5
- latency_total: 10.87s | tokens_per_second: 60.3
- input_tokens: 307 | output_tokens: 656

## Respuesta completa

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "devstral",
    "razon": "Devstral ofrece un buen balance entre comprensión de lenguaje natural y generación de resúmenes, lo que facilita la extracción de temas recurrentes en un gran conjunto de textos."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Claude Sonnet sobresale en la creación de contenido empático y honesto, cualidades esenciales para una disculpa profesional y eficaz."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "Deepseek-v3 es la opción más rentable y poderosa para tareas de codificación, garantizando precisión y eficiencia al generar scripts complejos."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "devstral",
    "razon": "Devstral combina rapidez y creatividad en la generación de contenido, ideal para producir múltiples publicaciones atractivas y coherentes."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Minimax-m2.7 está optimizado para llamadas a herramientas y manejo de datos estructurados, lo que lo hace perfecto para la validación de JSON."
  }
]
```