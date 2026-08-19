# Poolside Laguna XS 2.1 — content_verificable/audiencia_que_ya_sabe

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 4.695s | tokens_per_second: 179.6
- input_tokens: 140 | output_tokens: 843

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

¿Alguna vez has tenido un workflow en n8n que termina con "success", pero al revisar no has hecho nada? Es un error común y frustrante, especialmente cuando el sistema no te avisa. Aquí te explico por qué pasa y cómo detectarlo.  

**¿Por qué ocurre?**  
1. **Condiciones no cumplidas**: Un nodo "If" o "Switch" que filtra datos puede bloquear la ejecución sin mostrar error. Si la lógica no se cumple, el workflow se detiene, pero n8n lo marca como exitoso.  
2. **Datos vacíos**: Un webhook recibe un payload vacío o un cron se dispara sin parámetros. Si un nodo espera un valor (ej: un ID) y no lo recibe, el workflow se "cierra" sin acción.  
3. **Nodos desconectados**: Si un nodo está conectado a otro que no se ejecuta (ej: un "Set" que no tiene valor), el flujo se rompe silenciosamente.  

**Cómo detectarlo**  
- **Revisa las ejecuciones**: En la pestaña "Execution", observa la secuencia de nodos. Si un nodo está en gris o no muestra datos, es señal.  
- **Usa el modo Debug**: Activa "Debug" en el nodo que sospechas y verifica si recibe o envía datos.  
- **Valida entradas**: Agrega un nodo "Function" al inicio para imprimir `items` y asegurarte de que los datos llegan.  
- **Añade logs**: Usa nodos "Set" con mensajes clave (ej: "Datos recibidos: {payload}") para seguir el flujo.  

**Solución rápida**  
Si el workflow no hace nada, revisa:  
1. ¿El trigger (webhook/cron) está recibiendo datos?  
2. ¿Hay condiciones que bloqueen la ejecución?  
3. ¿Los nodos posteriores dependen de valores que no existen?  

Pequeños ajustes en validaciones o logs evitan dolores de cabeza. ¿Ya te ha pasado? Comparte cómo lo resolviste.