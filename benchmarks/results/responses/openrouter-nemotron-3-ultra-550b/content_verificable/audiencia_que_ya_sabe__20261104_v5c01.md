# Nemotron 3 Ultra 550B — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 13.312s | tokens_per_second: 49.4
- input_tokens: 116 | output_tokens: 658

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El "Success" verde es una mentira (y cómo pillarla)**

Tu workflow acaba en verde. El log dice *Execution finished*. El webhook respondió 200. Tú te vas a por café.

Media hora después: Slack explota. "El informe no ha llegado", "El lead no se ha creado en HubSpot", "La factura no se ha generado".

**¿Qué ha pasado?**
Que n8n define "éxito" como **"el grafo se ha recorrido sin lanzar excepción no capturada"**. No significa "la lógica de negocio se ha cumplido".

Los culpables habituales en produ:
1.  **`IF` / `Switch` cayendo en `false`/`fallback` sin nodo terminal:** El flujo sigue, n8n sonríe, tú pierdes datos.
2.  **Expresiones que evalúan `undefined` / `null` y el nodo destino lo traga:** Un `Set` que mapea `{{ $json.email }}` (vacío) → la API externa acepta `null` y crea el registro "fantasma", o un `HTTP Request` que manda `body: {}` y devuelve 200 OK.
3.  **`SplitInBatches` / `LoopOverItems` con array vacío:** Cero iteraciones = éxito instantáneo.
4.  **Error handling activado ("Continue On Fail")** tragándose el fallo real y devolviendo el item original intacto.

**Tu kit de detección (implementa esto *ya*):**

*   **Nodo "Assert" casero (Function/Code):** Al final de cada rama crítica, valida *contrato de salida*. `if (!items[0].json.dealId) throw new Error('Deal no creado')`. Fuerza el rojo.
*   **`Execute Workflow` + `Wait` + Webhook de confirmación:** Para async externo. No confíes en el 202 Accepted; espera el callback o pollea el estado real.
*   **Metric node (o Function final) → Push a Prometheus/Grafana/Loki:** Cuenta `items_processed`, `items_failed`, `branches_taken`. Alerta si `processed === 0` en horario laboral.
*   **Test unitario real en CI:** Usa `n8n-cli` o la API REST para lanzar el workflow con *fixtures* de edge cases (arrays vacíos, schemas rotos, 404/500 mockados). Verifica output JSON, no solo exit code.

**Regla de oro:** Si no has validado *output shape* y *side effects* (DB, API, FS), el verde es solo decoración.