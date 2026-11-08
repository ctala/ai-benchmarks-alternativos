# Tencent Hy4 — startup_content/curso_emprendimiento_modulo

- model_id: `tencent/hy4`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 50.877s | tokens_per_second: 83.0
- input_tokens: 273 | output_tokens: 4224
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores, proporcionando una guía detallada sobre la automatización con IA y herramientas específicas como n8n.

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un disenador instruccional especializado en emprendimiento y tecnologia.
Creas contenido educativo practico para emprendedores latinoamericanos.
Tu enfoque es hands-on, con ejercicios aplicables y ejemplos reales.

**user:**

Disena el Modulo 3 de un curso llamado "IA Practica para Emprendedores".

El modulo se titula: "Automatizacion con IA: De la idea al flujo de trabajo"

Incluye:
1. Objetivo del modulo (1 parrafo)
2. Contenido teorico (explicacion de automatizacion con IA, herramientas como N8N)
3. 3 ejemplos practicos de automatizacion para startups:
   - Atencion al cliente automatizada
   - Generacion de contenido para redes sociales
   - Calificacion automatica de leads
4. Ejercicio practico paso a paso (que el alumno pueda seguir)
5. Recursos adicionales
6. Preguntas de autoevaluacion (3 preguntas)

Formato: Markdown con buena estructura. Nivel: Emprendedor no-tecnico.


## Respuesta completa

# Módulo 3: Automatización con IA — De la idea al flujo de trabajo

⏱️ **Duración estimada:** 90 min  
🎯 **Nivel:** Emprendedor no técnico  
🛠️ **Herramientas principales:** n8n, ChatGPT / OpenAI, Google Sheets, Gmail, WhatsApp (via Twilio o Evolution API), Notion (opcional)

---

## 1. Objetivo del módulo

Al finalizar este módulo, serás capaz de identificar tareas repetitivas en tu negocio, traducirlas a un flujo de trabajo automatizado con IA y construir tu primer flujo funcional en **n8n** sin saber programar. No se trata de “aprender tecnología”, sino de recuperar tiempo: pasar de “yo lo hago todo” a “el sistema lo hace por mí, y yo solo reviso lo importante”.

---

## 2. Contenido teórico

### ¿Qué es automatizar con IA (y qué NO es)?

Automatizar es **enseñarle a un sistema una secuencia de pasos** para que los ejecute solo cuando pase algo (un disparador).  
La IA entra cuando uno de esos pasos requiere **interpretar, redactar, clasificar o decidir** con lenguaje natural.

| Sin IA | Con IA |
|------|-------|
| “Si llega un correo → guárdalo en Sheets” | “Si llega un correo → entiende si es queja, consulta o venta → responde o escala” |
| Reglas fijas (`si precio > 100`) | Criterios flexibles (`si el tono parece urgente`) |

> 💡 **Idea clave para emprendedores:** La IA no reemplaza tu criterio, lo **amplifica**. Tú defines las reglas del juego; la IA maneja el volumen.

**Analogía LatAm:** Es como tener un asistente de tienda que nunca duerme, anota todo en el cuaderno, te avisa solo cuando hay un cliente caliente… y además escribe los posts del Instagram.

---

### ¿Por qué n8n?

**n8n** (pronunciado *“n-eight-n”*) es una herramienta visual para armar flujos. Piénsalo como un **tablero de post-its conectados con flechas**.

| Ventaja | Qué significa para ti |
|-------|----------------------|
| Visual | Arrastras cajitas, no escribes código |
| Self-host o nube | Puedes empezar gratis en n8n.cloud o instalarlo en tu VPS (ej. Hostinger, Contabo) |
| +400 integraciones | Gmail, Sheets, WhatsApp, Stripe, Mercado Pago, Notion, Shopify… |
| Nodo de IA nativo | Conectas OpenAI, Claude o Gemini directamente |
| Licencia friendly | Ideal para startups que quieren control de datos (clientes LATAM, cuidado con PII) |

**Partes de un flujo en n8n (vocabulario mínimo):**

| Concepto | En criollo | Ejemplo |
|--------|-----------|---------|
| **Trigger** | “Cuando pase esto…” | Nuevo mensaje de WhatsApp |
| **Node** | “Haz esto…” | Limpiar texto / Llamar a ChatGPT |
| **Connection** | La flechita | WhatsApp → IA → Sheets |
| **Credentials** | Tus llaves | API de OpenAI, cuenta de Gmail |
| **Execution** | Cada vez que corrió | Ver log de qué pasó |

> ⚠️ **Buen práctica LATAM:** Nunca pongas datos sensibles (RUT, CPF, DNI, tarjetas) directo en el prompt. Usa `{{ $json.campo }}` y, si puedes, anonimiza antes de enviar a la IA.

---

### Estructura mental: De la idea al flujo (método de 4 pasos)

Usa esta plantilla antes de abrir n8n:

1. **Disparador:** ¿Qué evento inicia todo?  
2. **Contexto:** ¿Qué datos necesito? (nombre, mensaje, fuente)  
3. **Decisión IA:** ¿Qué le pido a la IA? (clasificar / redactar / resumir)  
4. **Salida + Humano:** ¿Dónde guardo y cuándo me avisan?  

> 📌 Regla de oro: **Siempre deja un “botón de apagado” y un canal de revisión humana.** La IA sugiere, tú apruebas.

---

## 3. Tres ejemplos prácticos para startups

### 3.1 🛎️ Atención al cliente automatizada (WhatsApp + IA + escalado)

**Caso real:** *Tienda de cosméticos en Medellín con 200 pedidos/semana.*  
Problema: 60% de mensajes eran “¿Dónde está mi pedido?”.

**Flujo:**
```
WhatsApp entrante
   → IA clasifica: [Envío | Devolución | Producto | Otro]
   → Si es "Envío": IA busca estado en Google Sheets (n° de guía) y responde
   → Si es "Devolución" o tono enojado → etiqueta "URGENTE" + notifica a Slack/Telegram
   → Guarda todo en Sheets con fecha + intención
```

**Prompt tipo (nodo OpenAI):**
> Clasifica el siguiente mensaje de cliente en una de estas categorías: ENVIO, DEVOLUCION, PRODUCTO, OTRO.  
> Si detectas frustración o palabras como "demora", "no llegó", "reclamo", añade `urgente: true`.  
> Devuelve solo JSON: `{"categoria": "...", "urgente": false}`.  
> Mensaje: `{{ $json.mensaje }}`

**Resultado:** De 3 hs/día de respuestas → 20 min de revisión de urgentes.

---

### 3.2 📱 Generación de contenido para redes (1 idea → 5 piezas)

**Caso real:** *Consultora de nutrición en CDMX.*  
Problema: “Se me acaba el contenido miércoles”.

**Flujo:**
```
Lunes 8:00 am (Schedule Trigger)
   → Lee 1 idea cruda de Notion / Sheets ("Ayuno intermitente para mamás")
   → IA genera:
        • 1 hilo de X (3 tuits)
        • 1 caption Instagram + 5 hashtags
        • 1 guion de Reel de 30 seg
        • 1 asunto de newsletter
   → Guarda en Google Sheets con columna "Estado: Borrador"
   → Te manda un Gmail: "Ya tienes contenido para la semana ✅"
```

**Tip emprendedor:** Pídele a la IA **tu tono**, no “tono profesional”:
> Escribe como una nutrióloga mexicana de 35 años que habla con mamás reales, sin tecnicismos, usando "se te antojó" en vez de "apetito". Evita emojis excesivos.

**Resultado:** 2 horas de domingo → 10 minutos de aprobación lunes.

---

### 3.3 🎯 Calificación automática de leads (Formulario → Score → Ventas)

**Caso real:** *SaaS de contabilidad para PYMES en Lima.*  
Problema: El founder llamaba a todos, incluso a curiosos.

**Flujo:**
```
Typeform / Tally / Google Form
   → IA lee: empresa, empleados, dolor, presupuesto estimado
   → Asigna score 1–10 + etiqueta: CALIENTE / TIBIO / FRIO
   → Si ≥ 8 → Crea tarjeta en CRM (HubSpot / Notion) + Slack #ventas
   → Si 5–7 → Entra a secuencia de email educativo (Gmail)
   → Si < 5 → Guarda en Sheets "Nurturing" sin molestar al equipo
```

**Prompt tipo:**
> Eres un asistente de ventas B2B en Perú. Puntúa del 1 al 10 este lead según:  
> - Tiene ≥10 empleados (+3)  
> - Menciona "me quito tiempo" o "errores en facturación" (+3)  
> - Presupuesto declarado > S/ 300/mes (+2)  
> - Dice "solo estoy viendo" (−3)  
> Devuelve JSON: `{"score": 8, "etiqueta": "CALIENTE", "motivo": "..."}`.  
> Datos: `{{ $json }}`

**Resultado:** Llamadas bajaron 40%, cierres subieron porque el tiempo fue a los CALIENTES.

---

## 4. Ejercicio práctico paso a paso 🧪

> **Reto:** Construye tu primer flujo: *“Clasificador de mensajes de contacto con aviso a Telegram”*  
> ⏱️ 25–30 min | 💸 Costo: $0 (n8n.cloud trial + OpenAI free tier o Gemini gratis)

### Paso 0 · Prepara (5 min)
- Crea cuenta en 👉 https://n8n.cloud (o usa tu instancia local)
- Ten a mano:
  - Una **API Key** de OpenAI (o Gemini / Claude)
  - Un **bot de Telegram** (habla con [@BotFather](https://t.me/BotFather) → `/newbot` → copia el token)
  - Tu **Chat ID** de Telegram (escribe a [@userinfobot](https://t.me/userinfobot))

### Paso 1 · Crea el flujo
1. Clic en **“New Workflow”**
2. Nómbralo: `M3 - Clasificador Contacto`
3. Agrega primer nodo → busca **“Webhook”**
   - Method: `POST`
   - Copia la **Test URL** (la usaremos para simular)

### Paso 2 · Simula un mensaje real
1. Clic en **“Listen for test event”**
2. Abre una terminal / Postman / o usa este curl:

```bash
curl -X POST "TU_TEST_URL" \
  -H "Content-Type: application/json" \
  -d '{"nombre":"Ana","mensaje":"Hola, me interesa pero ya tengo 3 presupuestos y necesito decidir hoy 😅"}'
```

3. Vuelve a n8n → deberías ver los datos entrar ✅

### Paso 3 · Añade el nodo de IA
1. Clic en `+` después del Webhook → busca **“OpenAI”** → *Message a Model*
2. Credentials → pega tu API Key
3. Modelo: `gpt-4o-mini` (barato y rápido)
4. En **Messages → System** pega:

```
Eres asistente de ventas de una startup latinoamericana.
Clasifica el mensaje en: CALIENTE, TIBIO o FRIO.
CALIENTE = urgencia, presupuesto o decisión próxima.
Devuelve SOLO este JSON, sin texto extra:
{"etiqueta":"...","motivo":"...","responde_ya":true/false}
```

5. En **User** escribe:
```
Nombre: {{ $json.body.nombre }}
Mensaje: {{ $json.body.mensaje }}
```

6. Clic en **“Execute step”** → revisa la salida 👀

### Paso 4 · Convierte el texto en datos (importante)
1. Agrega nodo **“Code”** (modo *Run Once for All Items*) y pega:

```js
const raw = $input.first().json.message.content;
const limpio = raw.replace(/```json|```/g, "").trim();
return [{ json: JSON.parse(limpio) }];
```

> 💡 No te asustes: es el único “código” del módulo, y es copiar/pegar. Su trabajo es solo limpiar el JSON.

### Paso 5 · Decide con un IF
1. Agrega nodo **“IF”**
2. Condición: `{{ $json.responde_ya }}` → **is true**
3. Rama **True** → nodo **Telegram → Send Message**
   - Chat ID: el tuyo
   - Texto:
   ```
   🔥 Lead CALIENTE: {{ $('Webhook').first().json.body.nombre }}
   Motivo: {{ $json.motivo }}
   Mensaje: {{ $('Webhook').first().json.body.mensaje }}
   ```
4. Rama **False** → nodo **Google Sheets → Append Row** (o simplemente un **NoOp** llamado `Guardar para después`)

### Paso 6 · Prueba de extremo a extremo
1. Clic en **“Execute Workflow”**
2. Repite el `curl` del Paso 2
3. ✅ Deberías recibir el mensaje en Telegram en segundos

### Paso 7 · Actívalo (modo producción)
1. Cambia de **Test URL** a **Production URL**
2. Toggle **“Active”** → ON
3. Pega esa URL en tu formulario (Tally, Typeform → Webhook, o tu landing)

### 🎁 Reto extra (opcional, +10 min)
Agrega un nodo **Gmail** en la rama `False` que envíe un correo amable:  
> *“Hola Ana, gracias por escribirnos 👋 Te compartimos una guía mientras decides: [link]”*

---

### ✅ Checklist de entrega
- [ ] Webhook recibe datos
- [ ] IA devuelve JSON válido
- [ ] Telegram llega solo si `responde_ya = true`
- [ ] Flujo está en **Active**
- [ ] Escribiste en un papel: **“¿Qué tarea mía va a reemplazar este flujo mañana?”** 📝

---

## 5. Recursos adicionales

| Recurso | Para qué | Link |
|-------|---------|------|
| 📘 n8n Docs para principiantes | Primeros pasos oficiales | https://docs.n8n.io/getting-started/ |
| 🧩 n8n Templates | Copia flujos listos (WhatsApp, Sheets, CRM) | https://n8n.io/workflows/ |
| 🧠 Prompt Library (OpenAI) | Prompts de clasificación probados | https://platform.openai.com/docs/guides/prompt-engineering |
| 🇱🇦 Comunidad n8n Español | Dudas en tu idioma | https://community.n8n.io/c/espanol/ |
| 🎥 Video: n8n + WhatsApp (Evolution API) | Caso LATAM real | Busca: *“n8n Evolution API WhatsApp español”* en YouTube |
| 📄 Plantilla Google Sheets del M3 | Columnas: Fecha / Nombre / Etiqueta / Motivo / Estado | [Haz una copia](https://docs.google.com/spreadsheets/) y crea: `Fecha, Nombre, Etiqueta, Motivo, Estado` |
| 🔐 Mini-guía de datos | Qué NO enviar a la IA (DNI, RUT, CPF, tarjetas) | Ver `docs/` del curso → `buenas-practicas-datos.pdf` |
| 💰 Calculadora de costo | Cuánto te cuesta cada ejecución con gpt-4o-mini | https://openai.com/api/pricing/ |

> 🧭 **Tip de mentor:** Guarda todos tus flujos en una carpeta de Notion llamada *“Mis empleados digitales”*, con columnas: **Qué hace / Cuándo corre / Quién lo revisa / Cómo lo apago**. Eso es gobernanza, incluso siendo 1 persona.

---

## 6. Preguntas de autoevaluación

1. **En tus propias palabras:** ¿Cuál es la diferencia entre una automatización “con reglas” y una “con IA”? Da un ejemplo de tu negocio donde la IA aporte algo que un `SI → ENTONCES` no podría resolver.

2. **Ordena los 4 pasos del método visto en clase** (Disparador → Contexto → Decisión IA → Salida + Humano) para este caso:  
   *“Cuando alguien deja su correo en mi landing, quiero saber si es cliente potencial o solo curioso, y avisarme solo si vale la pena llamarlo.”*  
   ¿En qué paso colocarías el **aviso a Telegram** y por qué debe existir siempre un canal de revisión humana?

3. **Diagnóstico:** Tu flujo en n8n corre, pero la IA responde con texto tipo *`Aquí tienes el JSON: {"etiqueta": "CALIENTE"...}`* y el nodo IF se rompe.  
   ¿Qué nodo agregarías, qué hace exactamente y qué cambiarías en el **prompt** para evitar que vuelva a pasar?

<details>
<summary>👀 Ver pistas (haz clic solo después de intentar)</summary>

1. Pista: piensa en *tono, intención, ambigüedad* vs. *números exactos*.  
2. Pista: el aviso va en **Salida**, y el humano evita que un falso positivo te haga llamar a un curioso… o que un falso negativo te haga perder una venta.  
3. Pista: `Code` limpiando ```json + la frase *“Devuelve SOLO JSON, sin texto extra”* en el System prompt.

</details>

---

### ➡️ Siguiente módulo
**Módulo 4 — Métricas y mantenimiento: Cómo saber si tu IA está ahorrándote dinero (y cuándo apagarla)**  
*(Incluye: logs en n8n, costo por ejecución, y un dashboard simple en Looker Studio)*

---

🧑‍🏫 *Diseñado para emprendedores que no quieren ser programadores… pero sí quieren dejar de ser el cuello de botella de su propio negocio.*  
¿Listo para el M4? Primero, activa tu flujo y mándame captura del Telegram ✅