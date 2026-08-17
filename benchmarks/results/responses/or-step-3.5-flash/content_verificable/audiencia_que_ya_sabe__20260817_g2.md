# Step 3.5 Flash — content_verificable/audiencia_que_ya_sabe

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 16.316s | tokens_per_second: 62.2
- input_tokens: 113 | output_tokens: 1015

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**¿Tu workflow de n8n marca "success" pero no hizo nada? No estás solo.**

Ese "success" solo confirma que el flujo se ejecutó hasta el final sin errores *técnicos* de la plataforma. No garantiza que tus nodos hayan procesado datos reales o tomado las acciones esperadas. Es el clásico "todo OK, pero no pasó nada".

**¿Por qué ocurre?**
Los casos más comunes:
1. **Condiciones falsas:** Un nodo `IF` o `Switch` evaluó una expresión que nunca fue verdadera, descartando todos los items.
2. **Datasets vacíos:** Un nodo anterior (ej. una API, una base de datos) devolvió un array vacío `[]`. Los nodos siguientes se ejecutan, pero sin datos que procesar.
3. **Errores "suaves":** Un `HTTP Request` devolvió un `200 OK` pero con un cuerpo vacío o un mensaje de error en el JSON. n8n lo ve como exitoso.
4. **Filtros demasiado restrictivos:** Un nodo `Filter` eliminó todos los elementos por una condición mal escrita.

**Cómo detectarlo (sin adivinar):**
- **Revisa siempre el panel de ejecución:** Haz clic en cada nodo. Mira la pestaña **"Output"**. ¿Hay datos? ¿Es un array vacío `[]`? ¿Viene un campo que esperabas?
- **Nodo de debug estratégico:** Inserta un nodo `Set` justo después de puntos críticos (ej. después de una API, antes de un `IF`). Así forzas una inspección visible de los datos en ese momento.
- **Prueba con datos reales:** Usa el botón **"Test workflow"** con el payload de un evento real, no solo con datos de ejemplo genéricos.
- **Confía en los logs, no solo en el estado:** Un workflow puede terminar en verde pero con advertencias en los logs de un nodo específico (ej. "No items to process").

**Regla de oro:** El "success" de n8n es la ausencia de fallos de ejecución, no la confirmación de resultados. Tu validación debe ir un nivel más abajo: **¿los datos en el output de cada nodo son los que esperabas?**

¿Has cazado ya algún "falso positivo" en tus flujos? ¡Comparte el caso!