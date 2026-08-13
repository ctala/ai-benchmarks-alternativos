# Claude Opus 5 (suscripción) — multi_turn/requirements_change

- model_id: `claude-opus-5`
- success: True  | final: 5.2 | quality: 6.0
- latency_total: 60.781s | tokens_per_second: 56.5
- input_tokens: 2 | output_tokens: 3432

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

Cambio anotado. La arquitectura ahora es esta:

```
Gmail Trigger → IF (filtro seguridad) → Set (normalizar) → Notion (create page) → Slack (notificar)
```

## 1. Gmail Trigger — filtra en el origen, no después

No uses un IF para filtrar si Gmail lo puede hacer por ti. En **Filters → Search (q)**:

```
subject:(propuesta OR cotizacion OR cotización)
```

Así el trigger solo dispara con lo que te importa y no gastas ejecuciones en ruido.

Config recomendada:
- **Poll Times**: cada 5 minutos (cada minuto si necesitas la notificación casi en tiempo real — ojo que el Gmail Trigger *hace polling*, no push, así que "instantáneo" no existe acá).
- **Simplify**: `true`. Te devuelve `From`, `Subject`, `date`, `snippet` planos en vez de tener que bucear en `payload.headers`.

## 2. IF — red de seguridad (opcional pero barato)

La búsqueda de Gmail hace stemming y a veces matchea de más. Un IF con condición String → contains, case insensitive:

```
{{ $json.Subject.toLowerCase() }}
```
contiene `propuesta` **OR** contiene `cotiza`

Uso `cotiza` como raíz para cubrir cotización / cotizacion / cotizaciones de una.

## 3. Set — parsear el remitente

El header `From` viene como `Cristian Tala <cristian@dominio.com>`. Necesitas separarlo:

| Campo | Expresión |
|---|---|
| `nombre` | `{{ ($json.From.match(/^(.*?)\s*</)?.[1] \|\| '').replace(/"/g,'').trim() }}` |
| `email` | `{{ $json.From.match(/<(.+?)>/)?.[1] \|\| $json.From }}` |
| `dominio` | `{{ ($json.From.match(/<(.+?)>/)?.[1] \|\| $json.From).split('@')[1] }}` |
| `asunto` | `{{ $json.Subject }}` |
| `fecha` | `{{ new Date($json.date).toISOString() }}` |
| `link` | `https://mail.google.com/mail/u/0/#inbox/{{ $json.threadId }}` |

El `dominio` no lo pediste, pero te sirve después para agrupar por empresa. Y el `link` es lo que más vas a usar: te lleva al email desde Notion con un clic.

## 4. Notion — Create Database Page

- **Resource**: Database Page → **Operation**: Create
- **Database ID**: lo sacas de la URL de la base (`notion.so/workspace/`**`ID_32_CHARS`**`?v=...`)

Las propiedades tienen que existir **con el tipo correcto** en tu base antes de correr esto:

| Propiedad Notion | Tipo | Valor |
|---|---|---|
| Nombre | Title | `{{ $json.nombre }}` |
| Email | Email | `{{ $json.email }}` |
| Asunto | Rich text | `{{ $json.asunto }}` |
| Fecha | Date | `{{ $json.fecha }}` |
| Link | URL | `{{ $json.link }}` |
| Estado | Select | `Nuevo` |

**El gotcha #1 de Notion**: crear la integración en `notion.so/my-integrations` no basta. Tienes que abrir la base de datos → menú `...` → **Connections → Connect to → tu integración**. Si te sale `object_not_found` o un 404, es esto el 90% de las veces. No es el token.

**Gotcha #2**: el campo Date exige ISO 8601. Si mandas el string crudo de Gmail (`Mon, 12 Aug 2026 09:14:22 -0400`) te tira 400. De ahí el `.toISOString()`.

## 5. Slack

- **Resource**: Message → **Operation**: Send
- **Send To**: Channel (ej. `#ventas`)
- **Text**:

```
🔔 *{{ $('Set').item.json.asunto }}*
De: {{ $('Set').item.json.nombre }} ({{ $('Set').item.json.email }})
<{{ $('Set').item.json.link }}|Ver email> · <{{ $json.url }}|Ver en Notion>
```

Fíjate en `$('Set').item.json` — como Slack va después de Notion, el `$json` del nodo actual ya es el output de Notion (que trae el `url` de la página creada, muy útil). Para los datos del email tienes que referenciar el nodo Set por nombre.

**El bot tiene que estar invitado al canal.** `/invite @tu-bot` en Slack. Si no, `channel_not_found` aunque el canal exista.

---

## Dos cosas que te van a morder después

**Duplicados.** Si el workflow falla en Notion y lo reintentas, o si tocas el trigger, puedes reprocesar emails. Dos opciones:
- Agregar un nodo Gmail → Add Label ("Procesado") al final, y sumar `-label:Procesado` a la query del trigger. Es la más limpia y además te da visibilidad en la bandeja.
- O guardar el `messageId` en una propiedad de Notion y consultar antes de crear.

**Si Notion cae, pierdes la notificación.** Como Slack está encadenado después, un fallo en Notion mata todo el flujo. Si prefieres que Slack avise igual, saca la rama de Slack del Set en paralelo (dos conexiones desde Set) en vez de encadenarla.

---

¿Te armo el JSON completo del workflow para que lo importes directo, o prefieres montarlo nodo por nodo? Si va el JSON, dime el nombre del canal de Slack y si quieres el esquema de propiedades de Notion tal cual lo puse arriba o con otros campos.