# DeepSeek V4 Flash (OpenRouter) — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 5.84s | tokens_per_second: 103.6
- input_tokens: 100 | output_tokens: 605
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y prácticamente útil, proporcionando soluciones detalladas y aplicables para detectar y manejar workflows que devuelven 'success' sin realizar acciones.

## Respuesta completa

**Asunto:** ¿Workflow exitoso o falso positivo?  

Sabes que un workflow en n8n devuelve “success” aunque no haya hecho nada útil. Sí, ese momento en que el nodo final se pinta de verde, pero los datos prometidos nunca llegaron a destino. ¿Por qué pasa?  

Causas comunes:  
- **Webhook sin validación**: recibe un payload vacío o mal formado, lo pasa como “éxito” y el resto del workflow opera sobre `null`.  
- **Cron mal configurado**: ejecuta pero el trigger no encuentra registros nuevos (ej: base de datos sin cambios). El workflow corre, pero no procesa nada.  
- **Nodos condicionales silenciosos**: un filtro descarta todos los items, pero el flujo sigue y el último nodo reporta éxito sin haber transformado ni enviado nada.  
- **Errores atrapados por error handler**: configuraste “Continue on error” y el workflow termina sin que te enteres de que un paso intermedio falló.  

**Cómo detectarlo:**  
1. **Logging estructurado**: agrega un nodo `Set` que registre la cantidad de items antes y después de cada paso crítico. Envíalo a un webhook de logging o a una hoja de cálculo.  
2. **Nodo “Stop and Error” condicional**: si tras un filtro el array está vacío, lanza un error intencional con `throw new Error('Sin datos para procesar')`. Así el workflow falla de verdad y puedes alertarte.  
3. **Monitorea el output del nodo final**: revisa el JSON de salida. Si contiene `[]` o `null` cuando esperabas datos, algo huele mal.  

**Mi recomendación:** no confíes en el color verde. Cada workflow debería terminar con un nodo que verifique que se cumplió el objetivo (ej: “si no hay registros actualizados, notifica por Slack”).  

¿Tienes algún caso real de falso éxito? Responde este correo, me interesa saber cómo lo resolviste.  

— Tu nombre