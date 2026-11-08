# MiniMax M2.5 — multi_turn/requirements_change

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 5.14 | quality: 4.0
- latency_total: 4.938s | tokens_per_second: 103.7
- input_tokens: 230 | output_tokens: 512

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

Perfecto, mucho mejor. Te explico la estructura completa:

## Estructura del Workflow

```
Gmail Trigger → IF (filtro) → Notion → Slack
                ↓
            Continue (false)
```

---

## 1. Gmail Trigger

- Configura tu cuenta de Gmail
- Elige la bandeja de entrada
- Marca "Mark as read" si quieres

---

## 2. Nodo IF (Filtro)

Usa esta expresión en **Condition 1**:

```javascript
{{ $json.subject.toLowerCase().includes('propuesta') }}
```

Y agrega una segunda condición (OR) para "cotizacion":

```javascript
{{ $json.subject.toLowerCase().includes('cotizacion') }}
```

---

## 3. Notion (Create Page)

- Conecta tu cuenta de Notion
- Selecciona la **Database** donde quieres guardar
- Mapea los campos:
  - **Name**: `{{ $json.from.name }}`
  - **Email**: `{{ $json.from.address }}`
  - **Subject**: `{{ $json.subject }}`
  - **Date**: `{{ $json.date }}`

---

## 4. Slack (Send Message)

- Conecta tu cuenta de Slack
- Channel: donde quieras recibir la alerta
- Message texto:
```Hola! Nuevo lead detectado:
De: {{ $json.from.name }}
Email: {{ $json.from.address }}
Asunto: {{ $json.subject }}
```

---

¿Quieres que te pase el JSON del workflow para que puedas importarlo directo?