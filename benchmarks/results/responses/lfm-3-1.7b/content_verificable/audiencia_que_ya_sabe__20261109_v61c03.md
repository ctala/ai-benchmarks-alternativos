# LFM-3 1.7B — content_verificable/audiencia_que_ya_sabe

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 9.08 | quality: 10.0
- latency_total: 12.969s | tokens_per_second: 288.1
- input_tokens: 110 | output_tokens: 3736

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Tema:** ¿Por qué un workflow de n8n puede devolver **“success”** sin hacer nada?

La respuesta está en el estado global del flujo. N8n marca la ejecución completa como *success* siempre que los nodos anteriores hayan terminado sin error y el último nodo tenga un resultado válido, aun si ese resultado es simplemente un “salto” o un campo vacío.

**Ejemplos comunes**  
- Un nodo **If** que pasa verdadero pero no llama al siguiente paso.  
- Una **Cron** que dispara una vez y solo envía un log sin invocar APIs externas.  
- Un **Set** que pone campos a nulo, haciendo que el flujo considere completado.  

Estas situaciones crean un flujo con éxito total aunque no ocurrió ni un solo llamada externa.

**Cómo detectarlo**  
1. Revisa la *Historial de ejecuciones* (Run History) buscando filas sin registros de salida (0 row).  
2. Activa la vista *Depuración/Nivel de logs* sobre cada nodo durante la ejecución.  
3. Observa el valor real de los *outputs* de los nodos intermedios; si están vacíos o iguales al tipo de dato entrante, el flujo no realizó acción.  
4. Verifica que el último nodo haya realizado realmente una petición HTTP o escrito en base… Si falla o no responde, el éxito fue falso.

Un truco rápido: inserta un nodo **Check** que siempre debe dispararse. Si aparece, sabes que algo más funcionó; si no, hay un paso omitido o una lógica de cortocircuito que evitó la acción.

¡Revisa tus nodos y antes de subirlo al scheduler, confirma que cada etapa ha producido algún dato real!