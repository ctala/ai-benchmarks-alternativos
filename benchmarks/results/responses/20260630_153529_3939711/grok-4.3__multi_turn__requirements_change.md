# Grok 4.3 — multi_turn/requirements_change

- model_id: `x-ai/grok-4.3`
- success: True  | final: 6.4 | quality: 6.4
- latency_total: 6.851s | tokens_per_second: 121.4
- input_tokens: 345 | output_tokens: 832

## Respuesta completa

✅ Entendido. Aquí tienes la estructura actualizada del workflow en **n8n**:

### Workflow recomendado

**Nodos necesarios:**

1. **Gmail Trigger**  
   - Event: `Message Received`
   - Marca la opción **"Only with attachments"** si quieres (opcional).

2. **IF** (para filtrar)  
   Este nodo es clave. Configúralo así:

   - **Condition 1:**
     - Value: `{{ $json.subject }}`
     - Operation: `Contains`
     - Value: `propuesta`
   - Agrega otra condición con **OR**:
     - Value: `{{ $json.subject }}`
     - Operation: `Contains`
     - Value: `cotizacion`

   > Consejo: Puedes poner ambas condiciones en el mismo nodo IF usando **OR**.

3. **Set** (opcional pero recomendado)  
   Para limpiar y organizar los datos antes de enviarlos a Notion:

   - `remitente_nombre`: `{{ $json.from.name }}`
   - `remitente_email`: `{{ $json.from.email }}`
   - `asunto`: `{{ $json.subject }}`
   - `fecha`: `{{ $json.date }}`
   - `snippet`: `{{ $json.snippet }}` (opcional)

4. **Notion**  
   - Operation: `Create Database Item`
   - Selecciona tu base de datos de Notion.
   - Mapea los campos (recomiendo tener estos en Notion):
     - Remitente
     - Email
     - Asunto
     - Fecha
     - Snippet / Contenido

5. **Slack**  
   - Operation: `Send a message`
   - Elige el canal donde quieres recibir las notificaciones.
   - Mensaje sugerido:
     ```
     📩 Nuevo email recibido:
     *De:* {{ $json.from.name }} ({{ $json.from.email }})
     *Asunto:* {{ $json.subject }}
     ```

---

### Orden de los nodos:

```
Gmail Trigger → IF → Set → Notion → Slack
```

---

### Preguntas para ajustar mejor el workflow:

1. ¿Quieres que el filtro sea **exacto** (`propuesta` o `cotizacion`) o también acepte variaciones como "Propuesta comercial" o "Cotización"?
2. ¿En Notion quieres crear un **Database Item** o una **Page** normal?
3. ¿Quieres que el mensaje de Slack incluya algún enlace o más información?

Dime cómo quieres ajustarlo y te doy la configuración más precisa de cada nodo.