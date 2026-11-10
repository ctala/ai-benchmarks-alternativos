# GPT-OSS 120B — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 16.703s | tokens_per_second: 44.0
- input_tokens: 165 | output_tokens: 735

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**¿Tu workflow devuelve “success” sin haber hecho nada?**  

Si trabajas con n8n día a día, ya sabes que un “success” es solo la señal de que la cadena de nodos se ejecutó sin errores. Pero a veces esa señal es engañosa: el flujo completa su recorrido, pero la lógica real nunca se disparó. Aquí tienes los motivos más comunes y cómo detectarlos antes de que el “éxito” se convierta en una falsa alarma.

---

### 1️⃣ Entrada vacía o filtrada sin notarlo  
Los nodos *Trigger* (webhook, cron, poll) pueden recibir payload vacío o filtros que descartan todo. Si la salida del trigger es `{}` o un array sin elementos, los nodos siguientes pueden seguir ejecutándose sin datos útiles.  
**Detección:** añade un nodo **IF** justo después del trigger que compruebe `{{ $json.length > 0 }}` o que el campo clave exista. Si la condición falla, lanza un *error* o envía una alerta a Slack.

### 2️⃣ “Continue On Fail” silencioso  
Activar *Continue On Fail* en un nodo que falla (por ejemplo, una llamada a API que devuelve 404) permite que el flujo siga y termine “success”. El resultado final será un objeto vacío o el mensaje de error encapsulado.  
**Detección:** revisa la propiedad `status` en `$node["NombreNodo"].json` y usa un **Set** para lanzar un error explícito cuando `status !== "ok"`.

### 3️⃣ Operaciones idempotentes sin cambios reales  
Al actualizar un registro con los mismos valores, la API responde “200 OK” pero no hay modificación. El workflow marca éxito, aunque nada cambió.  
**Detección:** compara los datos antes y después con un **Code** node (`if (old.value === new.value) throw new Error("No change")`).  

### 4️⃣ Salidas “null” que pasan desapercibidas  
Al usar nodos como *Merge* o *SplitInBatches*, un batch vacío sigue generando una ejecución “success”.  
**Detección:** inserta un **IF** que valide `{{ $json !== null }}` antes de cualquier acción de escritura.

---

### Checklist rápido

1. **Trigger → IF (payload check)**  
2. **Cada nodo crítico → Set → Throw si `status` != “ok”**  
3. **Comparar antes/después** para operaciones idempotentes.  
4. **Logs estructurados**: incluye `{workflowId, step, result}` en un webhook de auditoría.

Implementa estas guardas y transforma el “success” en una garantía real de que algo se hizo, no solo de que el flujo no se rompió. ¡A seguir automatizando sin sorpresas!