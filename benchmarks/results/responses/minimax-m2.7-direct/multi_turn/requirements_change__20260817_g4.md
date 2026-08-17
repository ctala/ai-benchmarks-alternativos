# MiniMax M2.7 (directo) — multi_turn/requirements_change

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.5 | quality: 8.0
- latency_total: 8.768s | tokens_per_second: 49.8
- input_tokens: 228 | output_tokens: 437

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

Perfecto, mucho mejor. Aqui tienes la estructura actualizada:

```
┌─────────────┐    ┌──────────┐    ┌───────────┐    ┌────────┐    ┌────────┐
│Gmail Trigger│───▶│   IF     │───▶│  Notion   │───▶│ Slack  │───▶│  End   │
└─────────────┘    └──────────┘    └───────────┘    └────────┘    └────────┘
                   filtro asunto        crear          notificar
                   'propuesta'         entrada         canal
                   'cotizacion'
```

**Nodos:**

1. **Gmail Trigger** - igual que antes
2. **IF** - filtro con condicion:
   ```
   {{ $json.subject.includes('propuesta') || $json.subject.includes('cotizacion') }}
   ```
3. **Notion** - Create Database Item (configuras la base de datos destino con los campos que necesites)
4. **Slack** - Message (envias al canal que prefieras)

Quieres que te detalle la configuracion de cada nodo o prefieres que te exporte el JSON completo del workflow para que lo importes directo?