# Mistral Large 3 675B — content_verificable/audiencia_que_ya_sabe

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 5.97 | quality: 6.0
- latency_total: 10.251s | tokens_per_second: 47.4
- input_tokens: 105 | output_tokens: 486
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

**Cuando tu workflow dice "éxito" pero te miente (y cómo pillarlo)**

Todos lo hemos visto: un workflow en n8n marca ✅ *Execution successful*, pero revisas los datos y… nada. Ni un registro actualizado, ni un email enviado, ni un webhook disparado. ¿Qué está pasando?

### **Los sospechosos habituales**
1. **Filtros silenciosos**: Un *If* o *Filter* que evalúa mal los datos y descarta todo sin errores. Revisa las condiciones con un *Set* previo que muestre los valores en el log.
2. **Nodos "fantasma"**: Un *HTTP Request* o *Webhook* que devuelve 200 pero el endpoint no procesa la petición (ej: API con rate limiting o payload inválido). Usa un *Set* después para verificar la respuesta.
3. **Cron/webhook sin triggers reales**: Un workflow programado que no se dispara porque el cron está mal configurado o el webhook no recibe datos. Prueba con un *Manual Trigger* para descartar.
4. **Errores en nodos "no críticos"**: Algunos nodos (como *Spreadsheet File*) pueden fallar internamente pero no romper el flujo. Activa el modo *Debug* y revisa los logs detallados.

### **Cómo cazar el problema**
- **Añade nodos de verificación**: Un *Set* con `{{ $json }}` después de cada paso crítico para ver qué datos fluyen (o no).
- **Usa el modo *Debug***: Ejecuta el workflow manualmente con *Debug* activado para ver los logs en tiempo real.
- **Prueba con datos mínimos**: Simplifica el input (ej: un solo registro) para aislar el fallo.
- **Revisa los *execution IDs***: Compara ejecuciones exitosas vs. las que "no hacen nada" para detectar patrones.

Si tu workflow miente, es porque algo se le escapó a n8n. Pero con estos trucos, lo pillarás. 🕵️‍♂️

¿Tienes algún caso concreto que te haya vuelto loco? Responde a este email y lo analizamos.