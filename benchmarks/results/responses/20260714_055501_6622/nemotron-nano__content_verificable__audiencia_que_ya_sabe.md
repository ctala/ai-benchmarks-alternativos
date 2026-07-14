# Nemotron 3 Nano 30B — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 5.586s | tokens_per_second: 104.2
- input_tokens: 116 | output_tokens: 582
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para detectar workflows que devuelven 'success' sin realizar acciones.

## Respuesta completa

**¿Workflow “Success” vacío? Cómo detectar el engaño**

En n8n un nodo *Execution* puede marcar el estado **Success** incluso cuando la ejecución real quedó sin impacto. Esto ocurre cuando:

1. **Falla silenciosa** – El nodo lanza una excepción pero el motor la captura y la interpreta como “finado sin errores”, devolviendo Success.  
2. **Ejecución condicional que nunca se cumple** – Un *IF* o *Switch* que nunca entra en la rama verdadera hace que el flujo se considere completado sin tocar los nodos críticos.  
3. **Webhook o Trigger que nunca dispara** – Un *Webhook* recibe la petición, pero la respuesta se responde antes de que el nodo interno procese datos, dejando el registro de éxito sin trabajo real.  
4. **Cron con “no‑run”** – Un disparador programado se ejecuta, pero el *IF* previo descarta la ejecución y el nodo final se marca como exitoso sin tocar nada.

### Detectarlo

- **Revisa el log de eventos** (`Execution List`) y busca entradas con **“no data processed”** o con **“skipped”**.  
- **Añade nodos de auditoría** (por ejemplo, *Function* que registre `items.length` o `msg.json`) antes y después del punto crítico; si el recuento permanece en 0 y el log indica Success, hay una pista.  
- **Utiliza el nodo *Run Once* o *Manual Execution* con `debug` activado**; el panel de salida mostrará si se procesó alguna fila.  
- **Configura alertas con *Error Trigger***: aunque el flujo termine con Success, un *Error Trigger* seguirá disparado cuando la salida sea un array vacío o cuando se produzca una excepción capturada.  
- **Revisa los *Workflow Executions* en la UI** y habilita la columna **“Items processed”**; un valor constante en 0 mientras el estado sea Success es la señal definitiva.

En resumen, el éxito de un workflow en n8n no garantiza acción concreta; la combinación de logs, métricas de procesamiento y triggers de error es la única forma fiable de detectar ejecuciones fantasma.