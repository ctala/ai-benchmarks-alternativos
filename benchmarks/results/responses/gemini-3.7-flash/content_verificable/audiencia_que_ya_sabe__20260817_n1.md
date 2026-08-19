# Gemini 3.7 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 14.515s | tokens_per_second: 89.1
- input_tokens: 93 | output_tokens: 1294

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**El falso verde: cuando n8n dice «Success» pero no hizo absolutamente nada**

Pocas cosas son más frustrantes que ver un check verde en el historial de ejecuciones, ir a la base de datos o al CRM y descubrir que no se movió un solo registro. Ya lo sabes: en n8n, `Status: Success` solo significa que ningún nodo lanzó una excepción no controlada. No garantiza impacto en el mundo real.

Los culpables habituales de este «éxito fantasma» suelen ser:

1. **Arrays vacíos (`[]`):** Tu nodo HTTP o consulta SQL devuelve cero registros. El nodo siguiente simplemente no tiene ítems sobre los que iterar y la ejecución termina con elegancia… y sin cambios.
2. **Ramas huérfanas en nodos IF/Switch:** La condición evalúa a `false`, el flujo toma la salida secundaria (que dejaste sin conectar) y el workflow concluye sin alertar.
3. **Filtros excesivamente restrictivos:** Nodos *Filter* que descartan el 100% del payload entrante.

### Cómo detectarlo y blindar tus flujos

* **Forzar fallos deliberados:** Si recibir 0 ítems es una anomalía de negocio, evalúa `{{ $input.all().length === 0 }}` y enrútalo a un nodo **Stop and Error**. Haz que el flujo falle de verdad para que salte tu trigger de error global.
* **Alertas en ramas muertas:** Nunca dejes la salida *false* en el aire si esperabas procesar datos. Conéctala a un webhook de observabilidad o loguea la condición descartada.
* **Métricas de salida vs. entrada:** En workflows críticos, añade un Code Node al final que compare `items_in` contra `items_out`. Si el ratio es 0, envía una advertencia a tu canal de alertas.

Que no se haya roto no significa que haya funcionado. Monitorea los datos procesados, no solo el código de salida.