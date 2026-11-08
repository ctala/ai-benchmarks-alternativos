# DeepSeek V4 Pro (0813) — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 25.756s | tokens_per_second: 49.9
- input_tokens: 179 | output_tokens: 1285

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Workflow en verde no significa que haya hecho algo. En n8n, `success` solo indica que la ejecución terminó sin excepciones no controladas. Los culpables clásicos: `Continue On Fail` activado, `Always Output Data` emitiendo items vacíos, un HTTP Request con status 404 que no validas, o un IF que ramifica al vacío. Resultado: crees que se creó el registro y no pasó nada.

**Cómo detectarlo:**

1. **No mires el color, mira los datos.** En Executions, abre la ejecución "exitosa" y revisa los nodos críticos. Si en los detalles el nodo no aparece en `runData` o su array de `items` está vacío, no ejecutó trabajo real.

2. **Valida output explícitamente.** Después de un nodo HTTP Request o de base de datos, agrega un Code node que verifique campos requeridos y haga `throw new Error("Sin datos")` si falla. Así el flujo falla de verdad y activa tu Error Workflow.

3. **Automatiza la revisión vía API.** Consulta `/executions?status=success&includeData=true` (o el nuevo filtro por `finished`) y busca en `data.resultData.runData` las claves de tus nodos clave: si faltan o traen `data.main[0]` con length 0, marca alerta.

4. **Usa Stop And Error como guardián.** Si un nodo condicional no cumple el mínimo esperado, detén el flujo con error intencional. Un fracaso silencioso es peor que un error ruidoso.

5. **Métricas propias.** Suma un nodo al final que incremente un contador o envíe un evento solo si los nodos críticos produjeron items. Compáralo con lo esperado en tu monitoreo.

Regla simple: valida siempre el output, no el estado. El verde solo confirma que no explotó, no que haya hecho algo útil.