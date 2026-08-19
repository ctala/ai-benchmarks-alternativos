# Claude Haiku 4.5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-haiku-4.5`
- success: True  | final: 8.77 | quality: 10.0
- latency_total: 5.721s | tokens_per_second: 82.3
- input_tokens: 123 | output_tokens: 471
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia experta, abordando el tema con ejemplos prácticos y soluciones.

## Respuesta completa

# Cuando "Success" No Significa Éxito

Esa notificación verde de "Workflow completed successfully" que ves en n8n puede ser engañosa. Un workflow puede terminar sin errores y no haber ejecutado ni una sola acción útil. Aquí está el problema y cómo detectarlo.

## El Culpable: Las Condiciones Silenciosas

Generalmente ocurre cuando usas nodos **Switch** o **IF** que filtran el flujo. Si ninguna rama se cumple, el workflow continúa hasta el final sin hacer nada. Sin errores. Sin alertas. Solo silencio.

Ejemplo típico: Un webhook que dispara un workflow con condiciones estrictas. Si los datos no coinciden exactamente, la rama se descarta y el workflow termina "exitosamente".

## Cómo Detectarlo

**1. Revisa los logs de ejecución**
Abre el histórico y expande cada nodo. Busca nodos que muestren `0 items` o ramas no ejecutadas. Eso es tu culpable.

**2. Usa nodos de debug estratégicos**
Coloca un **Debug** después de cada punto de filtrado. No es paranoia, es precisión.

**3. Monitorea las salidas reales**
En el panel de ejecución, verifica que los nodos críticos (API calls, database writes, webhooks salientes) realmente procesaron datos.

**4. Configura alertas apropiadas**
No confíes solo en "workflow completed". Usa **Error Workflow** para capturar lógica fallida o crea un nodo final que valide que algo sucedió.

## La Lección

"Success" en n8n significa "sin errores de sintaxis". No significa "hizo lo que esperabas". Esa diferencia te ahorrará horas de debugging.

Revisa tus workflows críticos hoy.