# MiniMax M2.7 — multi_turn/requirements_change

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 4.57 | quality: 4.0
- latency_total: 14.335s | tokens_per_second: 42.1
- input_tokens: 228 | output_tokens: 604
- judge_score: 2.0 | justificación: La respuesta no cumple con los requisitos originales de leer emails de Gmail, extraer datos del remitente y guardarlos en un Google Sheet, en su lugar introduce Notion y Slack, lo que la hace irrelevante y poco precisa.

## Respuesta completa

Aqui tienes el workflow actualizado:

## Estructura del Workflow

```
Gmail Trigger → IF (filtro) → Notion (guardar) → Slack (notificar)
```

---

### 1. Gmail Trigger

Configuracion estandar, conectas tu cuenta de Gmail y listo.

---

### 2. Nodo IF (Filtro)

Aqui filtras por asunto. Usa dos nodos IF encadenados para el OR:

**Primer IF:**
- Condition: `Subject` contains `propuesta`

**Segundo IF (conectado al TRUE del primero):**
- Condition: `Subject` contains `cotizacion`

Solo si el email pasa ambos filtros, continua el flujo.

---

### 3. Notion - Create Database Item

Configura tu base de datos de Notion con estos campos:
- **Nombre** (o titulo): Nombre del remitente
- **Email**: Email del remitente
- **Asunto**: El asunto del email
- **Fecha**: Fecha de recepcion

Mapea los datos del email a los campos de Notion.

---

### 4. Slack - Send Message

Configura el canal donde quieres recibir alertas.

Mensaje ejemplo:
```
📧 Nuevo email relevante
De: {{ $json.from.name }} ({{ $json.from.email }})
Asunto: {{ $json.subject }}
```

---

Quieres que te detalle la configuracion de alguno de estos nodos?