# Nemotron 3 Nano Omni 30B-A3B Reasoning — content_verificable/audiencia_que_ya_sabe

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 9.29 | quality: 10.0
- latency_total: 6.35s | tokens_per_second: 147.4
- input_tokens: 116 | output_tokens: 936
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, abordando el tema con ejemplos específicos y soluciones prácticas.

## Respuesta completa

En n8n un workflow se considera **éxitoso** cuando llega al último nodo que finaliza la ejecución sin lanzar una excepción. Eso implica que, aunque la lógica interna haya sido mínima o incluso nula, el motor marca la ejecución como “completed” en cuanto el flujo alcanza un nodo de salida ( *Respond on Webhook*, *Stopper*, *End of Workflow* ) o finaliza de forma natural.  

### ¿Por qué ocurre?

1. **Respuesta anticipada** – Si el primer nodo es un *Respond on Webhook* y la respuesta se envía antes de que cualquier otro nodo se ejecute, n8n registra la ejecución como exitosa aunque nada más haya sido procesado.  
2. **Condiciones que nunca se cumplen** – Un *If* que siempre evalúa a *false* o un *Cron* que dispara pero el *Run* interno está desactivado (p.ej. nodo *Execute* con “Continue on Fail” desmarcado) hacen que el flujo llegue al final sin tocar datos.  
3. **Nodos “vacíos”** – *No-Op* como *Set* con valores idénticos o *No Operation* (solo un *No‑Op* node) no generan actividad pero siguen formando parte del camino, por lo que la ejecución termina sin error.  
4. **Terminación forzada** – El nodo *Terminate* o *Stopper* pueden detener el flujo inmediatamente después del disparador, devolviendo 200 OK al webhook sin ejecutar pasos posteriores.  

### ¿Cómo detectarlo?

- **Log detallado**: inserta un nodo *Log* (o *Debug*) justo después del disparador y antes de cualquier transformación. Revisa el *Execution Log* para confirmar que cada nodo se ejecutó.  
- **Webhook de confirmación**: usa un *Respond on Webhook* con un token único y verifica en tu endpoint externo que la petición se envía después de los pasos esperados.  
- **Statísticas de ejecución**: en la barra lateral de *Workflow* revisa “Nodes executed” y “Average execution time”. Un valor 0 / cero indica que no hubo procesamiento.  
- **Pruebas de carga**: ejecuta el workflow con *Run Once* y observa la respuesta del webhook; si recibes 200 OK antes de que el log muestre actividad, el éxito es “falso”.  

Al combinar logs, tokens de verificación y el panel de estadísticas, podrás identificar rápidamente esos casos en los que n8n indica “success” sin haber hecho nada real. ¡A revisar esos flujos fantasma!