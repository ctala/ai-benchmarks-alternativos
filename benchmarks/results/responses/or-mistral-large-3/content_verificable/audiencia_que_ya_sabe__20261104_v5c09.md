# Mistral Large 3 675B — content_verificable/audiencia_que_ya_sabe

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 10.878s | tokens_per_second: 64.2
- input_tokens: 105 | output_tokens: 698

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

**Cuando tu workflow dice "éxito" pero no mueve un dedo (y cómo pillarlo)**

Sabes de sobra que un workflow en n8n puede terminar con un ✅ verde y, sin embargo, no haber ejecutado ni una sola acción útil. No es magia negra: es diseño. Y hay tres razones principales por las que pasa esto, más un par de trucos para detectarlo antes de que te explote en la cara.

### **1. Filtros que se lo tragan todo**
Un nodo `IF` con una condición mal escrita (o un `Switch` con ramas vacías) puede hacer que el flujo termine "con éxito" porque técnicamente *sí* se ejecutó... pero no entró por ninguna rama útil. **Solución:** Añade un nodo `Set` justo después del filtro con un valor fijo (ej: `{{ "FILTRO_PASÓ" }}`) y revisa el output en la ejecución. Si no aparece, el filtro está fallando en silencio.

### **2. Webhooks que no devuelven datos**
Un nodo `Webhook` puede recibir una petición vacía o con un payload que no coincide con lo que esperas. n8n lo marca como éxito porque *técnicamente* el webhook respondió (aunque sea con un 200 y un `{}`). **Solución:** Usa un `Function` o `Code` justo después para loguear el input crudo:
```javascript
console.log($input.all());
return $input.all();
```
Si el log está vacío o es `undefined`, el problema está en el cliente que llama al webhook.

### **3. Nodos que fallan "por dentro"**
Algunos nodos (como `HTTP Request`, `AWS`, o `Google Sheets`) pueden devolver un 200 pero con un error en el body (ej: `{"error": "Not found"}`). n8n no lo interpreta como fallo porque la petición HTTP fue exitosa. **Solución:** Añade un `IF` después de estos nodos para chequear el contenido de la respuesta:
```plaintext
{{ $node["HTTP Request"].json["error"] }}
```
Si existe, lanza un error manual con un `Function` o redirige a un nodo de notificación.

---

### **Cómo cazar estos fantasmas**
1. **Logs en cada paso crítico:** No confíes en el output final. Añade nodos `Set` o `Function` para loguear datos clave en puntos intermedios.
2. **Pruebas con datos reales:** Usa el modo "Test" con payloads idénticos a los de producción. Si solo pruebas con datos limpios, no verás los casos borde.
3. **Alertas en ejecuciones vacías:** Configura un webhook o un nodo `Email` que se active si el output de un nodo clave está vacío. Ejemplo:
   ```javascript
   if (!$input.all().length) {
     $node["Send Email"].run();
   }
   ```

El verde no siempre es sinónimo de "todo bien". Si tu workflow procesa datos críticos, asume que en algún punto *algo* se romperá en silencio y prepárate para detectarlo.