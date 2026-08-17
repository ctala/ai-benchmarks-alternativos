# DeepSeek R1 (reasoning) — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 8.37 | quality: 10.0
- latency_total: 53.883s | tokens_per_second: 20.2
- input_tokens: 101 | output_tokens: 1088
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia técnica, proporcionando soluciones prácticas y detalladas.

## Respuesta completa

### ¿Workflow "success" pero sin resultados? Así lo detectas.  

Tu workflow luce verde en el historial, pero no ejecutó acciones reales (no envió emails, no actualizó tu CRM, ni activó procesos). ¿Por qué? Aquí las causas y soluciones para técnicos:  

#### Causas comunes:  
1. **Trigger "silencioso"**:  
   - Un webhook recibió un payload vacío o inválido (ej: `{}` en lugar de datos esperados).  
   - Un cron se ejecutó, pero no hubo datos nuevos en el sistema origen (ej: API con respuesta `200 OK` y `[]`).  

2. **Flujo "descartado" por condiciones**:  
   - Nodos *If* o *Filter* bloquearon el flujo por reglas demasiado restrictivas (ej: comparar `last_updated` sin convertir timezones).  
   - Nodos con `Continue on Fail` activado: errores *dentro* de un nodo (ej: clave API inválida) pasaron desapercibidos.  

3. **Lógica de error incompleta**:  
   - Un *Error Trigger* manejó la excepción, pero no escaló la alerta (Slack/Email) o registró el incidente.  

#### Soluciones rápidas:  
✅ **Inspecciona los *input/output* en cada nodo**:  
   - Usa el **Execution List** (icono ⚡) y verifica:  
     - ¿El trigger recibió datos? (ej: en webhooks, revisa *Request > Body*).  
     - ¿Los nodos posteriores procesaron *items*? (nodos grises = no se ejecutaron).  

✅ **Agrega "sentinels"**:  
   - Inserta un nodo **Code** (o **Function**) con `console.log(items.length)` antes de acciones críticas.  
   - Usa un nodo **Telegram/Slack** para recibir "ping" en cada paso clave.  

✅ **Valida con datos "muertos"**:  
   - Prueba con payloads de error (ej: respuesta vacía de API) para forzar caminos alternativos.  

⚠️ **Mejora preventiva**:  
   - En nodos de API, añade un *If* que verifique `items.length === 0` y envíe alertas.  
   - Usa **n8n Error Workflow** para capturar fallos *globales* y reportar incluso en éxitos "falsos".  

**Conclusión**: Un "success" sin acción es casi siempre un fallo *de datos o condiciones*. Tus herramientas: Execution List + logging estratégico.  

¿Tienes un patrón de detección? ¡Compártelo en Twitter (#n8nEdgeCases)!  

---  
*¿Útil? Responde con un 👍. ¿Tema para el próximo boletín? Cuéntamelo.*