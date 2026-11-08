# GPT-OSS 120B — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 19.409s | tokens_per_second: 35.3
- input_tokens: 152 | output_tokens: 686

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**¿Por qué tu workflow muestra “success” y, sin embargo, no ha hecho nada?**  

En la práctica, el mensaje de éxito es simplemente la señal de que el motor de n8n ha llegado al final del grafo sin lanzar una excepción. Eso no garantiza que haya procesado datos útiles. Los escenarios más comunes son:

1. **Trigger sin payload** – Un webhook o cron se dispara, pero la petición entrante está vacía o el cron no tiene parámetros. Los nodos posteriores reciben `null` y, al no haber lógica que dependa de esos valores, terminan sin generar acciones.  

2. **Condiciones que nunca se cumplen** – Un nodo *IF* con una expresión que siempre evalúa a `false` corta el flujo. Si la rama “true” contiene la única operación real, el workflow “sobrevive” pero no ejecuta nada.  

3. **Salida implícita de nodos “pasivos”** – Nodos como *Set* o *Merge* pueden devolver un objeto vacío cuando sus campos están desactivados. Si el siguiente nodo espera una propiedad que nunca llega, simplemente se salta la operación.  

4. **Errores silenciados** – Cuando se usan bloques *Try/Catch* o la opción “Continue On Fail”, una excepción queda atrapada y el workflow sigue a buen puerto, aunque la tarea principal haya fallado.  

**Cómo detectarlo antes de que sea un problema**  

- **Añade un nodo *Function* al final** que inspeccione `items` y lance un error si `items.length === 0` o si alguna clave esperada falta.  
- **Marca con un *Set* una bandera** (`workflowExecuted = true`) en la rama que realmente realiza trabajo y verifica su presencia al final.  
- **Utiliza la opción “Execution Mode → Manual”** para inspeccionar la vista de “Execution Data” y confirmar que los nodos críticos recibieron datos.  
- **Configura alertas en tu panel de monitorización** (por ejemplo, con el webhook de Slack) que se activen cuando la métrica “executed nodes” sea menor que un umbral.  

Implementar cualquiera de estos chequeos convierte el “success” ilusorio en una garantía real de que tu workflow ha cumplido su propósito. ¡A seguir automatizando sin sorpresas!