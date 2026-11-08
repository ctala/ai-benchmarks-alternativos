# Nemotron 3 Nano 30B — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 9.25 | quality: 10.0
- latency_total: 9.603s | tokens_per_second: 82.3
- input_tokens: 116 | output_tokens: 790

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa


**🚦 ¿Por qué un workflow devuelve “success” sin haber hecho nada?**  

En n8n el estado *success* se dispara tan pronto como la ejecución termina sin lanzar una excepción. Si todos los nodos están configurados con *continueOnFailure* = true (o están vacíos) y no hay salida que rompa el flujo, la plataforma interpreta que todo salió bien, aunque el “trabajo” real sea nulo. Es el caso típico de:

- Un **Webhook** que recibe una petición y simplemente pasa al siguiente nodo (o a ninguno).  
- Un **Cron** que se ejecuta, pero la primera condición de filtro descarta todas las entradas.  
- Un **IF** que siempre evalúa *false* y, por tanto, nunca entra en la rama de acción.  

**🔍 Cómo detectarlo**  

1. **Revisa el payload de la ejecución**: abre la pestaña *Execution* → *Details* y observa el campo `json`. Si el cuerpo está vacío (`{}`) o contiene solo los campos de metadatos (`workflowId`, `runId`, …), es señal de que no se procesó nada útil.  
2. **Utiliza el endpoint `/v1/executions`**: filtra por `workflowId` y revisa el atributo `workflowStatus`. Cuando sea *success* pero el `runStatus` sea *idle* o *skipped*, sabes que el flujo quedó en “modo vacío”.  
3. **Añade un “Debug” o “Set” al inicio**: escribe deliberadamente un valor en `items[0].json` y comprueba si aparece en la salida. Si no, el problema está antes de esa rama.  
4. **Monitorea los logs de error**: aunque el estado sea *success*, los logs pueden contener “No items to process” o “Skipped node”.  

**💡 Tips de prevención**  

- Desactiva *continueOnFailure* en los nodos críticos y controla explícitamente los flujos alternativos.  
- Usa un nodo **No‑Op** (por ejemplo, “Set” con `json.foo = json.foo`) como “marcador” de entrada; si esa variable no cambia, sabes que nada se ejecutó.  
- Programa una **verificación de salud** al final del workflow (un simple “If” que compare un timestamp) y envía una alerta cuando el resultado sea idéntico al de la ejecución anterior.  

Con estas pistas podrás identificar rápidamente los workflows que “engañan” con un *success* aparente y corregir la lógica antes de que se conviertan en procesos fantasma. 🚀