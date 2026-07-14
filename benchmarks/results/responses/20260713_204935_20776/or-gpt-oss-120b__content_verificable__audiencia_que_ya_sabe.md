# GPT-OSS 120B — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 29.9s | tokens_per_second: 27.6
- input_tokens: 169 | output_tokens: 824
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, abordando el problema específico con soluciones prácticas y detalladas.

## Respuesta completa

**¿Por qué mi workflow devuelve “success” sin haber hecho nada?**  

En n8n no es raro ver una ejecución marcada como *success* mientras que, en la práctica, nada se procesó. Esto ocurre cuando el flujo **cumple su camino de salida sin generar datos**: filtros que descartan todo, ramas `IF` que nunca se activan, o nodos que simplemente pasan a la siguiente etapa sin salida (`Set` vacío, `NoOp`, etc.). La plataforma interpreta “ejecutado sin errores” como éxito, aunque el resultado sea nulo.

### Señales de que algo “no pasó”
1. **Execution Summary → No data** – En el panel de historial, la barra “Data” está vacía.  
2. **Node execution logs** – Cada nodo muestra “0 items processed”.  
3. **Output de webhook/cron** – El endpoint responde 200 pero no devuelve payload.  
4. **Metrics de tiempo** – Duraciones extremadamente bajas (milisegundos) pueden indicar que el flujo nunca entró en una rama real.

### Cómo detectarlo de forma automática
- **Añade un nodo “Function” al final** que lance un error si `items.length === 0`.  
  ```js
  if (items.length === 0) {
    throw new Error('Workflow executed but produced no items');
  }
  return items;
  ```
- **Utiliza un “IF” basado en `{{$json["$execution"]["data"]["$node"]?.length}}`** para crear una rama de alerta cuando la cuenta de ítems es 0.  
- **Activa “Save Execution Data”** en Settings → Execution; luego crea una regla de monitorización (por ejemplo, con Grafana o el propio “Workflow Trigger” de n8n) que avise cuando el número de ejecuciones exitosas sin datos supere un umbral.  
- **Implementa un “Error Workflow”** que capture la excepción del nodo anterior y envíe un mensaje (Slack, email) con la ID de ejecución y el motivo.

### Buenas prácticas
- **Valida siempre la entrada**: antes de cualquier filtro, verifica que haya al menos un ítem.  
- **Documenta los “dead‑ends”** en el diagrama del workflow; así podrás identificar rápidamente ramas que podrían quedar sin salida.  
- **Revisa periódicamente el historial**: un pico de “success” sin datos suele indicar un cambio en la fuente (API, webhook) que necesita ajuste.

Detectar y actuar sobre estos “success vacíos” evita que tus integraciones se vuelvan silenciosas y garantiza que cada ejecución entregue valor real. ¡A afinar esos flujos!