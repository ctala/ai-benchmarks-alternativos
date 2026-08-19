# GPT-OSS 20B — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 36.161s | tokens_per_second: 22.6
- input_tokens: 165 | output_tokens: 819
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

En n8n, la palabra “success” no siempre significa que algo “haya pasado”. La propia máquina de ejecución solo garantiza que la cadena de nodos se haya procesado sin lanzar un error; no comprueba si el efecto deseado ocurrió.  
Algunos escenarios comunes que generan un “success” vacío son:

| Escenario | Por qué parece vació | Cómo se detecta |
|-----------|----------------------|-----------------|
| **Webhook sin salida** | El nodo Webhook devuelve 200 OK inmediatamente, aunque no haya ningún nodo posterior. | Añade un nodo **Set** al final que escriba un valor “ok:true” en la salida. |
| **Función sin `return`** | Un nodo Function que sólo modifica `items[i].json` y no devuelve nada. | Usa `return items;` explícitamente o agrega un nodo **Debug** para ver `items`. |
| **Condición `If` que falla** | Un nodo If con `false` no pasa datos al siguiente nodo, pero no lanza error. | Inserta un nodo **NoOp** con salida “no data” y revisa el log. |
| **Error ignorado** | `Ignore Error` captura un fallo y permite continuar. | Activa la vista “Execution Log” y busca “Error ignored”. |
| **Cron sin acción** | Un trigger Cron que no tiene nodos de acción, solo un Webhook que responde. | Añade un nodo **Wait** o **Trigger** a tu cron para validar que algo realmente suceda. |

**Detección práctica**  
1. **Logs**: habilita “Debug” y revisa la salida de cada nodo.  
2. **Flags**: en cada nodo que deba hacer algo, escribe un campo booleano en `items[i].json` y verifica que llegue al final.  
3. **Monitoreo**: crea un workflow de alerta que se active cuando un flujo regrese `success` pero el flag esté en `false`.  

En resumen, “success” en n8n es solo la ausencia de error, no la garantía de acción. Añade siempre un nodo de verificación o un flag y vigila el log. Así evitarás que tu flujo se comporte como un fantasma.