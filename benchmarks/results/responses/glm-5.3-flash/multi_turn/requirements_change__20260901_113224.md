# GLM 5.3 Flash — multi_turn/requirements_change

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 7.24 | quality: 8.0
- latency_total: 186.91s | tokens_per_second: 32.8
- input_tokens: 235 | output_tokens: 6124

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente tecnico para emprendedores que trabajan con N8N.

**user:**

Necesito un workflow en N8N que lea emails de Gmail, extraiga los datos del remitente, y los guarde en un Google Sheet.

**assistant:**

Perfecto, ese workflow es bastante directo. Te explico los pasos:

1. **Trigger**: Gmail Trigger (se activa con cada email nuevo)
2. **Extraer datos**: Function node para parsear remitente, asunto, fecha
3. **Guardar**: Google Sheets node para agregar una fila

Los campos a extraer serian: nombre del remitente, email, asunto, fecha. Quieres que te detalle la configuracion de cada nodo?

**user:**

En realidad, cambio de idea. No quiero Google Sheets, quiero que los datos vayan a Notion. Ademas, quiero que el workflow filtre solo los emails que tengan la palabra 'propuesta' o 'cotizacion' en el asunto. Y que me mande una notificacion a Slack cuando llegue uno.


## Respuesta completa

Perfecto, con esos cambios el flujo queda asi:

**Gmail Trigger → Filter → Edit Fields → Notion → Slack**

**1. Gmail Trigger**
- Evento: mensaje nuevo recibido, con polling cada 1-5 min segun la frecuencia que necesites.
- Necesitas las credenciales de Gmail OAuth2 conectadas en N8N.

**2. Filter** (para no procesar emails irrelevantes)
- Condicion tipo Boolean → "is true", con este valor:
```
{{ /propuesta|cotiza/i.test($json.subject) }}
```
- Truco: uso "cotiza" como raiz, asi cubre cotizacion, cotización y cotizaciones. La `i` ignora mayusculas.

**3. Edit Fields (Set)** — separa nombre y email del remitente:
- Nombre: `{{ $json.from.includes('<') ? $json.from.split('<')[0].trim().replace(/"/g, '') : '' }}`
- Email: `{{ $json.from.includes('<') ? $json.from.split('<')[1].replace('>', '') : $json.from }}`
- Asunto: `{{ $json.subject }}`
- Fecha: `{{ $now.toFormat('yyyy-MM-dd') }}` (fecha de llegada; si prefieres la del email, revisa si tu trigger trae `$json.date`)
- Resumen: `{{ $json.snippet }}`

**4. Notion**
- Antes crea la base de datos en Notion con estas propiedades: Nombre (Title), Email (Email), Asunto (Rich Text), Fecha (Date), Resumen (Rich Text).
- En el nodo: Resource "Database Page" → Operation "Create", y mapea cada propiedad con las variables del paso anterior.
- Si usas token de integracion interna, recuerda compartir la base con N8N.

**5. Slack**
- Operation: Message → Post, elige el canal.
- Texto sugerido:
```
🎯 Nueva propuesta: "{{ $('Edit Fields').item.json.asunto }}" de {{ $('Edit Fields').item.json.nombre }} ({{ $('Edit Fields').item.json.email }})
Ver en Notion: {{ $json.url }}
```
- `$json.url` es el link de la pagina recien creada en Notion.

Tips finales:
- Pon el Filter justo despues del trigger para no gastar llamadas a la API con emails que no aplican.
- Haz una ejecucion de prueba y revisa el output del trigger: segun la version, algunos campos pueden venir anidados y ajustas las expresiones.

Si quieres, te armo el JSON del workflow para importarlo directo a N8N.