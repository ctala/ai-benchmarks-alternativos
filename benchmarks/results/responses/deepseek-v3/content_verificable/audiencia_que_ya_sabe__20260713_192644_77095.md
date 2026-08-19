# DeepSeek V3.2 — content_verificable/audiencia_que_ya_sabe

- model_id: `deepseek/deepseek-chat`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 13.04s | tokens_per_second: 31.7
- input_tokens: 99 | output_tokens: 414
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, ofreciendo consejos prácticos para detectar falsos positivos en workflows de n8n.

## Respuesta completa

**¿Tu workflow dice "success" pero no hizo nada? Cómo detectar falsos positivos**  

Si construyes workflows en n8n todos los días, sabes que el *status "success" no siempre es sinónimo de éxito real*. A veces, el workflow ejecuta todas las tareas sin errores… pero no hizo lo que esperabas.  

**¿Por qué pasa esto?**  

1. **Respuestas vacías o mal formateadas**: Una API devuelve `200 OK` con un array vacío, y tu workflow sigue adelante sin validar si había datos.  
2. **Condicionales demasiado permisivas**: Un `IF` mal configurado puede hacer que una rama crítica nunca se ejecute, pero el flujo sigue marcándose como exitoso.  
3. **Webhooks silenciosos**: Un endpoint acepta el payload (HTTP 200), pero luego falla internamente y no hay retroalimentación.  

**Cómo cazarlo antes de que te cace a ti**:  

- **Logea TODO**: Usa nodos de *Function* o *Webhook* para imprimir datos clave (ej: `console.log(JSON.stringify(input))`).  
- **Chequea outputs manualmente**: Si un nodo devuelve `{}` o `[]`, añade una validación explícita.  
- **Métricas de negocio**: Si tu workflow debe crear 5 registros, verifica que realmente se crearon (ej: con un *HTTP Request* posterior a la DB).  

Peor que un error visible es uno que pasa desapercibido. **Tu arma secreta**: asume que "success" solo significa "no falló", no "funcionó".  

*¿Tienes otros trucos para evitar falsos éxitos? ¡Responde a este correo y comparte!* 🚀  

— [Tu nombre]