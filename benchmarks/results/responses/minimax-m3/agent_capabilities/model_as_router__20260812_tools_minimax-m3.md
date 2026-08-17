# MiniMax M3 — agent_capabilities/model_as_router

- model_id: `minimax/minimax-m3`
- success: True  | final: 5.24 | quality: 5.0
- latency_total: 16.273s | tokens_per_second: 97.6
- input_tokens: 420 | output_tokens: 1589

## Respuesta completa

# Asignación de Modelos para tu Startup

```json
[
  {
    "subtarea": "Analizar 500 reviews de usuarios y extraer los 5 problemas principales",
    "modelo": "claude-sonnet",
    "razon": "Claude sobresale en comprensión de sentimiento, matices y contexto humano. Las reviews requieren empatia para distinguir entre quejas reales, sugerencias y simple frustración."
  },
  {
    "subtarea": "Escribir un email de disculpas a clientes afectados por un bug",
    "modelo": "claude-sonnet",
    "razon": "Tono empático, honesto y profesional. Claude es el mejor para contenido delicado que requiere equilibrio entre disculparse, asumir responsabilidad y recuperar confianza."
  },
  {
    "subtarea": "Generar un script Python que procese los datos de ventas de Q1",
    "modelo": "deepseek-v3",
    "razon": "DeepSeek es el mejor en razonamiento + coding. El procesamiento de datos requiere lógica robusta, manejo de edge cases y código limpio. Además es muy barato (ideal para startup)."
  },
  {
    "subtarea": "Crear 20 posts para redes sociales sobre nuestro nuevo feature",
    "modelo": "claude-sonnet",
    "razon": "Necesitas consistencia de marca, creatividad y copy que enganche. Claude mantiene mejor el tono en volumen. Alternativa: gemini-flash-lite si priorizas velocidad sobre calidad."
  },
  {
    "subtarea": "Validar que 100 respuestas JSON de nuestra API sean correctas",
    "modelo": "minimax-m2.7",
    "razon": "Tarea sistemática tipo agente que puede usar herramientas. minimax-m2.7 está optimizado para tool calling, ideal para validar schemas, detectar anomalias y reportar errores estructuradamente."
  }
]
```

## 💰 Resumen de costos aproximados (para 500 reviews ~75k tokens, etc.):

| Tarea | Modelo | Costo estimado |
|-------|--------|----------------|
| Reviews | claude-sonnet | ~$0.30 |
| Email disculpa | claude-sonnet | ~$0.01 |
| Script Python | deepseek-v3 | ~$0.005 |
| 20 posts redes | claude-sonnet | ~$0.05 |
| Validación JSON | minimax-m2.7 | ~$0.02 |

**Total estimado: ~$0.40** para las 5 tareas 🎉

## 💡 Tips extra:
- Para el script Python, pide a deepseek-v3 que incluya **tests unitarios** y manejo de errores.
- Para los posts de redes, podrías usar un **prompt con ejemplos de posts anteriores** para mantener voz de marca.
- Para validación JSON, considera hacerlo **híbrido**: validación de schema con código + revisión semántica con IA.