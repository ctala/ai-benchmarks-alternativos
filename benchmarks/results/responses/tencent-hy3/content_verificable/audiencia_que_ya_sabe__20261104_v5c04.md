# Tencent Hy3 — content_verificable/audiencia_que_ya_sabe

- model_id: `tencent/hy3`
- success: True  | final: 5.94 | quality: 6.0
- latency_total: 57.338s | tokens_per_second: 64.8
- input_tokens: 113 | output_tokens: 3713

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

¿Tu workflow dice 'success' pero tienes la sensación de que no pasó nada? Bienvenido al infierno silencioso de n8n.

En n8n, un estado 'success' solo significa que el motor no lanzó una excepción. No garantiza que tus nodos hicieron su trabajo, solo que no se rompieron intentándolo.

El caso más clásico: tu DB o API devuelve un array vacío (`[]`). El nodo lo traga y pasa al siguiente. Si tu IF tiene una rama 'false' que termina en un nodo vacío, n8n cierra la ejecución con un bonito check verde. Otro escenario frecuente: un webhook que recibe un payload con estructura inesperada. Tus expresiones devuelven `undefined`, pero como no operas matemáticamente con ese valor, n8n ni parpadea y da por buena la ejecución.

¿Cómo le metemos mano a este problema de los no-ops?

1. **Valida la longitud:** Si esperas datos, pon un IF justo después de la fuente. Si `{{ $items().length }} === 0` (o tu array anidado específico), rutea a un nodo Error o a una alerta en Slack. No dejes que el flujo siga si no hay nada que procesar.
2. **Assertions en Code:** Si un campo es crítico para la lógica de negocio, tira un `throw new Error('Missing field X')` manualmente. Fuerza el fallo si la realidad no cumple tus supuestos.
3. **Usa Filter a muerte:** Descarta items vacíos o inválidos antes de llegar a los nodos de acción (HTTP Request, DB Insert) para evitar escrituras fantasma.
4. **Monitoreo proactivo:** Activa un Error Workflow o consulta la API de n8n para cruzar ejecuciones 'success' contra el volumen esperado de items procesados por corrida.

Un 'success' en n8n es una presunción de inocencia, no una garantía de eficiencia. Audita tus rutas muertas.