# Mistral Large — content_verificable/audiencia_que_ya_sabe

- model_id: `mistralai/mistral-large`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 12.274s | tokens_per_second: 52.3
- input_tokens: 105 | output_tokens: 642
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, abordando problemas comunes con soluciones prácticas.

## Respuesta completa

**¿Tu workflow dice "success" pero no hizo nada? Aquí está el porqué (y cómo pillarlo)**

Todos hemos estado ahí: un workflow corre sin errores, n8n te devuelve un bonito ✅ *success*, pero los datos siguen igual. ¿Magia? No. **Falsos positivos**. Aquí las causas más comunes y cómo cazarlas:

### 1. **Nodos que no fallan (pero deberían)**
Algunos nodos (ej: *HTTP Request*, *Execute Command*) devuelven *success* aunque la acción falle. Por ejemplo:
- Un *HTTP Request* recibe un `200 OK` pero el cuerpo de la respuesta es `{"error": "Nope"}`.
- Un *Execute Command* corre un script que falla silenciosamente (ej: `exit 0` aunque el proceso muera).

**Solución:** Usa el nodo *IF* para validar respuestas. Ejemplo:
```json
{{ $json.body.error }} // Si existe, lanza un error manual con "Throw Error"
```

### 2. **Webhooks que no disparan lo que esperas**
Un webhook recibe datos, pero:
- El payload no coincide con lo que tu workflow espera (ej: `{{ $json.data }}` en lugar de `{{ $json.payload.data }}`).
- El webhook se dispara con un *test request* vacío.

**Solución:** Añade un nodo *Set* al inicio para loguear el payload completo:
```json
{{ JSON.stringify($input.all()) }}
```
Luego revisa los *executions* para ver qué llegó realmente.

### 3. **Cron jobs que corren... en el vacío**
Un workflow con trigger *Cron* se ejecuta, pero:
- Las variables globales o credenciales que usa están vacías o caducadas.
- El nodo *Date & Time* usa una zona horaria distinta a la tuya (ej: UTC vs. local).

**Solución:** Añade un nodo *Set* al inicio para validar dependencias:
```json
{
  "hasCredentials": {{ $credentials?.apiKey ? true : false }},
  "currentTime": {{ DateTime.now().toFormat("yyyy-MM-dd HH:mm") }}
}
```

### 4. **Nodos que "saltan" sin avisar**
Nodos como *Merge* o *Switch* pueden ignorar ramas enteras si no cumplen condiciones, pero el workflow sigue como si nada.

**Solución:** Usa el nodo *No Operation* (o un *Set* vacío) en ramas críticas y loguea su ejecución:
```json
"Rama X ejecutada": true
```

---
**Pro tip:** Activa el modo *Debug* en n8n (`N8N_LOG_LEVEL=debug`) y revisa los logs de cada nodo. Los falsos *success* suelen dejar huellas en los detalles de ejecución.

¿Te ha pasado algo similar? Comparte tu caso en los comentarios. 🚀