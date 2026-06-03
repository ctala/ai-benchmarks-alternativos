# Claude Opus 4.7 (suscripción) — startup_content/curso_emprendimiento_modulo

- model_id: `claude-opus-4-7`
- success: True  | final: 6.99 | quality: 10.0
- latency_total: 107.241s | tokens_per_second: 62.3
- input_tokens: 6 | output_tokens: 6683
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores, cubriendo todos los aspectos solicitados con ejemplos prácticos y recomendaciones específicas.

## Respuesta completa

# Módulo 3: Automatización con IA — De la idea al flujo de trabajo

> **Curso:** IA Práctica para Emprendedores
> **Duración estimada:** 4-6 horas (lectura + ejercicio + autoevaluación)
> **Pre-requisitos:** Módulos 1 y 2 (Fundamentos de IA + Prompting efectivo)

---

## 1. Objetivo del módulo

Al finalizar este módulo, serás capaz de **identificar tareas repetitivas en tu negocio que consumen tu tiempo y diseñar flujos automatizados con IA que las resuelvan sin que tengas que escribir código**. Vas a entender qué es la automatización con IA, conocer las herramientas no-code más usadas en LATAM (N8N, Make, Zapier), y construir tu primer flujo funcional de principio a fin. La meta no es que te conviertas en programador, sino que aprendas a **delegar trabajo a la IA** como si fuera un asistente que trabaja 24/7 por menos de USD 20 al mes.

---

## 2. Contenido teórico

### 2.1 ¿Qué es la automatización con IA?

La automatización tradicional consiste en encadenar acciones predecibles: "cuando llega un email → guardarlo en Drive". Funciona, pero es **rígida**: si el email tiene un formato distinto, el flujo se rompe.

La **automatización con IA** agrega un cerebro al medio de ese flujo. Ahora podés decir:

> "Cuando llegue un email → que la IA lo lea, decida si es un cliente potencial, urgencia o spam → y haga algo distinto según el caso."

Esa decisión inteligente en medio del proceso es lo que cambia todo. Permite automatizar tareas que antes requerían **criterio humano**: leer texto en lenguaje natural, clasificar, resumir, responder con tono adecuado, extraer datos de documentos desordenados, etc.

### 2.2 Los 3 componentes de cualquier flujo automatizado

Todo flujo de automatización tiene 3 partes:

| Componente | Qué hace | Ejemplo |
|---|---|---|
| **Trigger (disparador)** | El evento que inicia el flujo | "Llegó un mensaje de WhatsApp" |
| **Procesamiento (IA)** | Donde la IA piensa y decide | "Clasificá el mensaje: venta, soporte o queja" |
| **Acción** | Lo que se ejecuta como resultado | "Mandalo al canal de Slack correspondiente" |

### 2.3 Herramientas para automatizar sin código

| Herramienta | Para quién | Costo aproximado | Ventaja |
|---|---|---|---|
| **N8N** | Emprendedor técnico-curioso | Gratis self-hosted / USD 20/mes cloud | Open source, controlás tus datos, integra cualquier API |
| **Make (ex-Integromat)** | Visual learner | Desde USD 9/mes | Interfaz muy visual, fácil de empezar |
| **Zapier** | Cero conocimiento técnico | Desde USD 20/mes | Más popular, miles de integraciones |
| **n8n.io self-hosted** | Quien quiere costo cero | Solo el VPS (USD 5/mes) | Privacidad total, ilimitado |

**Recomendación para LATAM:** Empezá con **N8N cloud** o **Make**. Zapier escala caro rápido. N8N self-hosted es el final boss cuando ya tengas volumen.

### 2.4 ¿Qué modelo de IA usar?

Según el benchmark de modelos alternativos:
- **Para tareas simples** (clasificar, resumir corto): **Gemini 2.5 Flash Lite** o **GPT-5.4 Mini** — rápidos y baratos
- **Para tareas que requieren razonamiento** (calificar leads complejos): **Devstral Small** o **GPT-4.1**
- **Para volumen alto y privacidad**: **Qwen3.5 en Ollama Cloud** (lo que usa Cristian en producción)

> 💡 Regla práctica: empezá con el modelo más barato. Solo subí de tier si la calidad no alcanza.

---

## 3. Tres ejemplos prácticos de automatización para startups

### 3.1 Ejemplo A: Atención al cliente automatizada por WhatsApp

**Problema real:** Tenés una tienda online y recibís 50+ mensajes diarios preguntando "¿hacen envíos a Concepción?", "¿cuánto demora?", "¿tienen talla M?". Te roban 2 horas al día.

**Flujo automatizado:**

```
[WhatsApp Business API]
        ↓
[N8N recibe el mensaje]
        ↓
[IA lee el mensaje + consulta tu FAQ y catálogo]
        ↓
   ¿Puede responder con >85% confianza?
        ↓                    ↓
       SÍ                    NO
        ↓                    ↓
[Responde solo]    [Avisa a humano + sugiere respuesta]
```

**Stack sugerido:**
- WhatsApp Business API (vía Twilio o 360dialog)
- N8N como orquestador
- Gemini 2.5 Flash Lite como cerebro
- Google Sheets como base de FAQs y catálogo

**Ahorro estimado:** 60-70% de los mensajes se auto-responden. Recuperás ~1.5 horas/día.

---

### 3.2 Ejemplo B: Generación de contenido para redes sociales

**Problema real:** Sos founder y "deberías" estar publicando en LinkedIn 3 veces por semana, pero entre operación y ventas nunca te da el tiempo.

**Flujo automatizado:**

```
[Cron: cada lunes 8am]
        ↓
[N8N lee tu blog o un RSS de noticias del sector]
        ↓
[IA genera 3 posts adaptados a LinkedIn, IG y X]
        ↓
[Los guarda en un Google Sheet "borrador"]
        ↓
[Te manda un email para que revises y apruebes]
        ↓
[Al aprobar: se programan en Buffer/Metricool]
```

**Stack sugerido:**
- RSS de tu blog o ecosistemastartup.com
- N8N + GPT-5.4 Mini para redacción
- Google Sheets como cola de aprobación
- Buffer o Metricool para publicar

**Clave del prompt:** la IA debe tener un "system prompt" con tu **tono de voz, audiencia y temas tabú**. Sin eso, sale contenido genérico de LinkedIn-influencer.

**Ahorro estimado:** de 4 horas/semana a 20 minutos de revisión.

---

### 3.3 Ejemplo C: Calificación automática de leads (Lead Scoring)

**Problema real:** Tu equipo de ventas recibe 30 leads por día desde el formulario web, pero solo 5 son realmente buenos. Pierden tiempo llamando a todos.

**Flujo automatizado:**

```
[Formulario web (Typeform/Tally)]
        ↓
[N8N recibe los datos: nombre, empresa, cargo, problema, presupuesto]
        ↓
[IA enriquece: busca la empresa en LinkedIn/web]
        ↓
[IA puntúa el lead 0-100 según criterios tuyos]
        ↓
   ¿Score > 70?
        ↓                ↓
       SÍ               NO
        ↓                ↓
[CRM "Hot" +     [CRM "Nurturing" +
 notifica a       email automático
 vendedor en      con caso de uso]
 Slack]
```

**Criterios típicos que la IA evalúa:**
- ¿El cargo es decisor? (CEO, Founder, Director +20pts)
- ¿La empresa tiene el tamaño esperado? (+15pts)
- ¿El problema descrito coincide con lo que vos resolvés? (+25pts)
- ¿Mencionó presupuesto o urgencia? (+20pts)
- ¿Es de un país que atendés? (+20pts)

**Stack sugerido:**
- Typeform / Tally como entrada
- N8N + Devstral Small (mejor razonamiento) como evaluador
- HubSpot / Pipedrive como CRM destino
- Slack para notificar al vendedor

**Ahorro estimado:** el equipo solo llama a leads >70 puntos = 3x más conversión por hora de venta.

---

## 4. Ejercicio práctico paso a paso

### Objetivo del ejercicio
Vas a construir tu **primer flujo funcional**: un clasificador automático de emails que separe consultas de venta, soporte y spam, y las mande a Slack en canales distintos.

**Tiempo estimado:** 90 minutos
**Costo:** USD 0 (todo en plan free)

---

### Paso 1: Crear cuenta en N8N Cloud (5 min)

1. Andá a **n8n.io** → "Get started for free"
2. Confirmá tu email
3. En el dashboard, hacé clic en **"+ Add workflow"**
4. Nombrá tu workflow: `Clasificador de emails`

---

### Paso 2: Configurar el trigger de Gmail (10 min)

1. En el canvas, clic en el **"+"** para agregar un nodo
2. Buscá **"Gmail Trigger"**
3. Configurá:
   - **Event:** `Message received`
   - **Polling:** cada 5 minutos
   - **Filter:** `is:unread` (solo emails sin leer)
4. Conectá tu cuenta de Gmail (OAuth)
5. Hacé clic en **"Execute node"** para verificar que trae datos

---

### Paso 3: Agregar el cerebro IA (20 min)

1. Agregá un nodo **"OpenAI"** o **"HTTP Request"** (para OpenRouter)
2. Configurá las credenciales con tu API key
3. En el campo **System prompt**, pegá:

```
Sos un asistente que clasifica emails de una startup. Leé el email
y respondé SOLO con una de estas 3 palabras:

- VENTA: si el email muestra interés en comprar, pide cotización
  o pregunta por precios.
- SOPORTE: si es un cliente existente con un problema, queja o duda
  técnica.
- SPAM: si es publicidad no solicitada, newsletter o no aporta valor.

No expliques. Solo respondé una palabra.
```

4. En el campo **User prompt**, mapeá:
```
Asunto: {{ $json.subject }}
Cuerpo: {{ $json.body }}
```

5. Modelo recomendado: `google/gemini-2.5-flash-lite` (barato y rápido)
6. Temperature: `0.2` (queremos respuestas consistentes)

---

### Paso 4: Agregar la lógica de ruteo (15 min)

1. Agregá un nodo **"Switch"** o **"IF"**
2. Creá 3 rutas según el output de la IA:
   - Si contiene "VENTA" → ruta 1
   - Si contiene "SOPORTE" → ruta 2
   - Si contiene "SPAM" → ruta 3 (no hace nada, descarta)

---

### Paso 5: Conectar Slack (15 min)

1. Agregá un nodo **"Slack"** en cada ruta de Switch
2. Configurá cada uno para postear en un canal distinto:
   - VENTA → `#ventas-leads`
   - SOPORTE → `#soporte-clientes`
3. Mensaje recomendado:
```
🔔 Nuevo email clasificado como {{ $json.classification }}

De: {{ $json.from }}
Asunto: {{ $json.subject }}

Preview: {{ $json.body.substring(0, 200) }}...

Ver completo: {{ $json.gmailLink }}
```

---

### Paso 6: Activar y probar (15 min)

1. Activá el workflow con el toggle superior derecho
2. Mandate a vos mismo 3 emails de prueba:
   - Uno preguntando "cuánto cuesta su servicio"
   - Uno diciendo "tengo un problema con mi cuenta"
   - Uno tipo newsletter de cualquier cosa
3. Esperá 5 minutos y verificá que cada uno cayó en el canal correcto

---

### Paso 7: Iterar (10 min)

- Si la IA clasificó mal alguno → ajustá el system prompt con más ejemplos
- Si tarda mucho → probá un modelo más rápido
- Si querés agregar una 4ta categoría (ej: PRENSA) → editá el prompt y agregá una ruta

✅ **¡Listo!** Tenés tu primer flujo de IA productivo.

---

## 5. Recursos adicionales

### Documentación oficial
- **N8N Academy:** [docs.n8n.io/courses](https://docs.n8n.io/courses) — curso gratis oficial
- **Make Academy:** [make.com/en/academy](https://www.make.com/en/academy)
- **OpenRouter Models:** [openrouter.ai/models](https://openrouter.ai/models) — comparar precios

### Plantillas listas para copiar
- **N8N Workflow Templates:** [n8n.io/workflows](https://n8n.io/workflows) — 1500+ flujos gratis
- **Awesome n8n (GitHub):** repositorios con casos reales de la comunidad

### Para profundizar en LATAM
- **ecosistemastartup.com** — casos de startups latinas usando IA
- **Comunidad Skool de Cristian Tala** — flujos reales compartidos por emprendedores
- **Benchmark de modelos:** [benchmarks.cristiantala.com](https://benchmarks.cristiantala.com) — calculadora para elegir modelo según costo/calidad

### Canales YouTube recomendados
- **Leon van Zyl** (inglés) — tutoriales N8N paso a paso
- **The AI Automators** (inglés) — flujos de negocio avanzados

### Libros
- *"Working Backwards"* (Bryar & Carr) — para diseñar procesos automatizables con criterio Amazon
- *"The 4-Hour Workweek"* (Tim Ferriss) — mindset de delegación y automatización

---

## 6. Preguntas de autoevaluación

Respondé estas preguntas **antes** de revisar las respuestas sugeridas al final. Si fallás 2 o más, te recomiendo releer la sección correspondiente.

### Pregunta 1
**Tu startup recibe 200 mensajes diarios por Instagram DM. El 80% son preguntas repetidas sobre stock, precios y envíos. El 20% requiere criterio humano (reclamos, pedidos especiales). ¿Cómo diseñarías el flujo de automatización con IA? Mencioná trigger, procesamiento y acción.**

<details>
<summary>Ver respuesta sugerida</summary>

- **Trigger:** Nuevo DM recibido en Instagram (vía Meta Business API o Manychat)
- **Procesamiento IA:** Clasificá el mensaje en 4 categorías: STOCK, PRECIO, ENVIO, OTRO. Si está en las 3 primeras, generá respuesta usando un Google Sheet con info actualizada. Si es OTRO, marcalo para humano.
- **Acción:** Las 3 categorías auto-respondidas se envían directamente. La categoría OTRO se reenvía a un canal de Slack del equipo de atención con un resumen + link al DM original.

**Bonus:** agregar un "fallback de confianza" — si la IA no está >85% segura, mandar a humano aunque la categoría sea conocida.
</details>

---

### Pregunta 2
**¿Cuál es la diferencia clave entre automatización tradicional y automatización con IA? Dá un ejemplo donde una falla y la otra funciona.**

<details>
<summary>Ver respuesta sugerida</summary>

La automatización tradicional sigue reglas **rígidas y predecibles**. La automatización con IA agrega capacidad de **interpretar lenguaje natural y tomar decisiones con criterio**.

**Ejemplo donde falla la tradicional y gana la IA:**
Un flujo tradicional que diga "si el email tiene la palabra 'factura' → mandalo a contabilidad" va a fallar cuando un cliente escriba "necesito el comprobante de pago de mi última compra" (sin usar "factura"). La IA entiende el contexto y lo clasifica correctamente como tema contable.
</details>

---

### Pregunta 3
**Estás eligiendo entre N8N Cloud (USD 20/mes), Zapier (USD 20/mes) y N8N self-hosted (USD 5/mes en un VPS). Sos founder técnico-curioso con 500 ejecuciones mensuales y datos sensibles de clientes. ¿Cuál elegirías y por qué? Mencioná al menos 2 criterios.**

<details>
<summary>Ver respuesta sugerida</summary>

**Elección:** N8N self-hosted.

**Criterios:**
1. **Privacidad de datos:** al ser self-hosted, los datos de tus clientes nunca pasan por servidores de terceros. Crítico si manejás info sensible (salud, finanzas, datos personales bajo Ley 19.628 en Chile o LGPD en Brasil).
2. **Costo a escala:** Zapier cobra por tarea ejecutada. Con 500 ejecuciones podés estar bien, pero si el flujo crece a 5.000/mes Zapier te cobra USD 70+ y N8N self-hosted sigue costando USD 5.
3. **Aprendizaje:** sos "técnico-curioso" — montar un VPS te enseña infra básica que después usás para mil cosas más (deploy de apps, scraping, hosting de modelos locales).

**Trade-off honesto:** vas a invertir ~4-6 horas iniciales en setup (Docker, dominio, SSL). Si valorás más tu tiempo que esos USD 15/mes de diferencia, N8N Cloud es razonable.
</details>

---

## Cierre del módulo

Si llegaste hasta acá y completaste el ejercicio, ya tenés algo que el 95% de los emprendedores LATAM no tienen: **un flujo productivo de IA corriendo en tu negocio**. En el **Módulo 4** vamos a aprender a **conectar múltiples flujos entre sí** y diseñar tu primer "agente" autónomo que tome decisiones más complejas.

> 📌 **Tarea para la próxima clase:** identificá **3 tareas repetitivas** que hagas vos o tu equipo esta semana. Anotálas con: cuánto tiempo te toman, cuántas veces por semana, y qué pasa si se hacen mal. En el próximo módulo las vamos a priorizar y automatizar.

---

*Módulo 3 — Curso "IA Práctica para Emprendedores" · Cristian Tala*