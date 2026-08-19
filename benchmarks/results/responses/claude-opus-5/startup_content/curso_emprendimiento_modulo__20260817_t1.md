# Claude Opus 5 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.67 | quality: 9.76
- latency_total: 115.206s | tokens_per_second: 71.1
- input_tokens: 388 | output_tokens: 8192
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil para emprendedores, cubriendo todos los aspectos solicitados con ejemplos prácticos y explicaciones detalladas.

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

> **Duración estimada:** 4 horas (1.5h de teoría + 2.5h de práctica)
> **Nivel:** Emprendedor no técnico
> **Requisitos previos:** Módulos 1 y 2 (Fundamentos de IA generativa y Prompting efectivo)

---

## 1. Objetivo del módulo

Al finalizar este módulo serás capaz de identificar tareas repetitivas dentro de tu negocio, traducirlas a un **flujo de trabajo automatizado** y construir tu primera automatización funcional conectando herramientas de IA con las aplicaciones que ya usas (WhatsApp, Gmail, Google Sheets, Notion, tu CRM). No necesitas saber programar: aprenderás a "pensar en flujos" —disparador, procesamiento, acción— y a usar plataformas visuales como **n8n** y **Make** para que la IA trabaje mientras tú duermes. El resultado tangible del módulo es una automatización propia, en producción, que le ahorre al menos 5 horas semanales a tu equipo.

---

## 2. Contenido teórico

### 2.1 Qué es (y qué no es) automatizar con IA

Automatizar es delegar una secuencia de pasos a un sistema. Lo hacemos desde hace décadas: una factura que se genera sola, un correo de bienvenida programado. Lo nuevo es que la IA agrega **capacidad de juicio** a esa secuencia.

| Automatización clásica | Automatización con IA |
|---|---|
| Sigue reglas rígidas: "si el asunto dice *factura*, mover a carpeta X" | Interpreta significado: "si este correo expresa una queja urgente, escalar" |
| Falla ante lo inesperado | Tolera variaciones, errores de ortografía, lenguaje informal |
| Solo mueve datos | Genera datos nuevos: resúmenes, respuestas, clasificaciones |
| Barata y determinista | Cuesta por uso (tokens) y es probabilística |

**Regla de oro:** usa automatización clásica para lo estructurado y reserva la IA para el paso donde se necesita *entender* o *crear*. Un flujo bien diseñado suele tener 1 o 2 nodos de IA, no diez.

### 2.2 La anatomía de todo flujo de trabajo

Cualquier automatización, sin importar la herramienta, tiene tres partes:

```
[ DISPARADOR ]  →  [ PROCESAMIENTO ]  →  [ ACCIÓN ]
   Trigger            Lógica + IA           Output

Ej: llega un      Ej: la IA clasifica    Ej: se crea fila
mensaje de        el mensaje y redacta   en Sheets + se envía
WhatsApp          una respuesta          respuesta al cliente
```

**Tipos de disparador:**
- **Webhook:** algo externo avisa a tu flujo (un formulario enviado, un pago recibido). Es el más común y potente.
- **Programado (cron):** se ejecuta cada día a las 8:00 am, cada lunes, cada hora.
- **Polling:** el flujo revisa cada X minutos si hay algo nuevo (nuevo correo, nueva fila).
- **Manual:** tú aprietas el botón.

### 2.3 El panorama de herramientas

| Herramienta | Curva de aprendizaje | Costo | Cuándo elegirla |
|---|---|---|---|
| **Zapier** | Muy baja | Alto por volumen (~USD 20-70/mes) | Flujos simples, poco volumen, cero tolerancia a lo técnico |
| **Make** | Media | Medio (~USD 10-30/mes) | Buen balance; interfaz visual muy clara para lógica ramificada |
| **n8n** | Media-alta | **Gratis autohospedado** o ~USD 24/mes en cloud | Volumen alto, lógica compleja, control de datos, presupuesto ajustado |
| **Agentes en ChatGPT / Claude Projects** | Baja | Incluido en el plan | Tareas asistidas donde tú estás en el loop |
| **Chatwoot / ManyChat** | Baja | Freemium | Específicamente atención al cliente en canales de mensajería |

### 2.4 Por qué n8n para emprendedores latinoamericanos

n8n será nuestra herramienta principal en este módulo por cuatro razones concretas:

1. **Costo por ejecución = 0.** En Zapier, cada paso de cada flujo consume una "tarea" facturable. Si procesas 3.000 mensajes al mes con un flujo de 6 pasos, son 18.000 tareas → plan de USD 100+. En n8n autohospedado pagas solo el servidor (~USD 5-10/mes en Hetzner o DigitalOcean) y las llamadas a la API de IA.
2. **Soberanía de datos.** Los datos de tus clientes se quedan en tu servidor. Relevante si operas bajo la Ley 1581 de Colombia, la LGPD de Brasil o la LFPDPPP de México.
3. **Nodo de código opcional.** Si algún día necesitas algo raro, hay una salida. No te quedas atrapado.
4. **Nodos de IA nativos.** Trae integraciones listas con OpenAI, Anthropic, Google Gemini, bases de datos vectoriales y un constructor de agentes.

**Conceptos clave de n8n que usaremos:**

- **Nodo:** cada caja del flujo. Hace una cosa.
- **Ejecución:** una corrida completa del flujo. Puedes ver el historial y depurar.
- **Expresiones:** la forma de referenciar datos de pasos anteriores. Sintaxis: `{{ $json.nombreDelCampo }}`
- **Nodo IF / Switch:** bifurca el flujo según una condición.
- **Nodo Set / Edit Fields:** limpia y reorganiza datos.
- **Credenciales:** guardas tus API keys una vez y las reutilizas.

### 2.5 Cómo decidir qué automatizar primero: la matriz ICE-A

No automatices lo que te parezca "cool". Puntúa cada candidato de 1 a 5:

| Criterio | Pregunta |
|---|---|
| **F**recuencia | ¿Cuántas veces por semana ocurre? |
| **T**iempo | ¿Cuántos minutos consume cada vez? |
| **E**structura | ¿El proceso es siempre parecido o es un caos distinto cada vez? |
| **R**iesgo | Si la IA se equivoca, ¿cuál es el daño? (aquí puntaje alto = riesgo bajo) |

**Prioridad = Frecuencia × Tiempo × Estructura × Riesgo**

Ejemplo real (agencia de marketing en Medellín, 4 personas):

| Tarea | F | T | E | R | Prioridad |
|---|---|---|---|---|---|
| Responder "¿cuánto cuesta?" en Instagram | 5 | 2 | 5 | 5 | **250** |
| Redactar reportes mensuales de clientes | 2 | 5 | 4 | 3 | 120 |
| Negociar contratos | 1 | 5 | 1 | 1 | 5 |

Ganó lo obvio: responder consultas de precio. Empieza por lo aburrido y frecuente, no por lo estratégico.

### 2.6 Cuatro reglas de seguridad antes de tocar nada

1. **Human-in-the-loop al inicio.** Tu primera versión NO envía nada al cliente automáticamente: te manda el borrador a ti por Telegram o Slack para que apruebes. Después de 2 semanas sin errores, sueltas el control.
2. **Nunca pongas la API key en el texto del flujo.** Usa siempre el gestor de credenciales.
3. **Define el "no sé".** Instruye a la IA para que, si no está segura, escale a un humano en lugar de inventar. La alucinación en atención al cliente cuesta dinero y reputación.
4. **Log de todo.** Cada ejecución debe dejar un registro (una fila en Google Sheets basta) para que puedas auditar qué respondió la IA y por qué.

---

## 3. Tres ejemplos prácticos de automatización

### Ejemplo A — Atención al cliente automatizada

**Contexto:** *Tiendita*, e-commerce de café de especialidad en Bogotá. Recibe ~120 mensajes diarios por WhatsApp; el 70% son las mismas 5 preguntas (envíos, precios, formas de pago, origen del café, estado del pedido). Dos personas dedican 4 horas diarias a esto.

**Flujo:**

```
[Webhook WhatsApp Business API]
        ↓
[Nodo Set: extraer teléfono, nombre, texto]
        ↓
[Nodo IA - Clasificador]  →  categoría + urgencia
        ↓
[Switch]
   ├─ "estado_pedido" → [HTTP Request a API de la tienda] → [IA redacta respuesta con el dato] → [Enviar WhatsApp]
   ├─ "faq"           → [Vector Store: buscar en base de conocimiento] → [IA redacta] → [Enviar WhatsApp]
   ├─ "queja"         → [Notificar a Slack #urgente] → [Respuesta: "un asesor te contacta en 10 min"]
   └─ "otro"          → [Crear ticket] → [Notificar a agente humano]
        ↓
[Google Sheets: registrar interacción]
```

**Prompt del clasificador:**

```
Eres el clasificador de mensajes de Tiendita, e-commerce de café colombiano.

Clasifica el siguiente mensaje de cliente en UNA categoría:
- estado_pedido: pregunta por un pedido ya realizado
- faq: duda sobre productos, envíos, pagos, tiempos
- queja: insatisfacción, producto dañado, reclamo
- otro: cualquier cosa que no encaje claramente

Devuelve SOLO un JSON válido:
{"categoria": "...", "urgencia": "alta|media|baja", "resumen": "máx 15 palabras", "confianza": 0.0-1.0}

Si confianza < 0.7, usa categoria "otro".

Mensaje del cliente: {{ $json.body }}
```

**Prompt del redactor de respuestas (nodo FAQ):**

```
Eres Sofi, asesora de Tiendita. Respondes por WhatsApp.

REGLAS:
- Tono: cálido, colombiano neutro, tuteo. Máximo 60 palabras.
- Usa ÚNICAMENTE la información del CONTEXTO. 
- Si el contexto no contiene la respuesta, responde exactamente: 
  "Déjame confirmarlo con el equipo y te escribo en unos minutos 🙌"
- NUNCA inventes precios, plazos ni promociones.
- Un emoji máximo.

CONTEXTO:
{{ $json.documentosRecuperados }}

PREGUNTA DEL CLIENTE:
{{ $json.mensaje }}
```

**Resultados a 60 días:**
- 68% de mensajes resueltos sin intervención humana
- Tiempo de primera respuesta: de 47 min a 8 segundos
- Costo: USD 8/mes de servidor + USD 19/mes de API de IA
- El equipo pasó de atender chats a hacer venta consultiva → +14% en ticket promedio

**Errores que cometieron y cómo los corrigieron:**
- *Semana 1:* la IA inventó una promoción de "2x1" que no existía → agregaron la regla "NUNCA inventes precios ni promociones" y bajaron la temperatura a 0.2.
- *Semana 2:* respondía en inglés a clientes que escribían "hi" → agregaron "responde siempre en español" al prompt de sistema.

---

### Ejemplo B — Generación de contenido para redes sociales

**Contexto:** *LegalGo*, startup B2B de gestión de contratos en Ciudad de México. El fundador necesita presencia en LinkedIn pero no tiene tiempo ni community manager.

**Flujo:**

```
[Cron: lunes 7:00 am]
        ↓
[Google Sheets: leer "Banco de Ideas" → filtrar estado = "pendiente"]
        ↓
[Loop sobre 3 ideas]
        ↓
[Nodo IA - Generador de posts]  (con brand voice en el prompt de sistema)
        ↓
[Nodo IA - Generador de prompt visual]
        ↓
[HTTP Request → API de imágenes]
        ↓
[Notion: crear página con post + imagen + estado "por aprobar"]
        ↓
[Telegram al fundador: "3 posts listos para revisar 👉 [link]"]

--- flujo separado ---
[Webhook desde Notion: estado cambia a "aprobado"]
        ↓
[Buffer / LinkedIn API: programar publicación]
        ↓
[Sheets: marcar idea como "publicada"]
```

**Prompt de sistema (esto es lo que hace la diferencia):**

```
Eres el ghostwriter de Andrés, fundador de LegalGo (SaaS de gestión 
de contratos para PyMEs mexicanas).

AUDIENCIA: directores de operaciones y gerentes legales de empresas 
de 20-200 empleados en México. Escépticos del hype tecnológico. 
Les importa el riesgo y el tiempo, no la innovación por la innovación.

VOZ DE ANDRÉS:
- Directo. Frases cortas. Cero corporativismo.
- Comparte números y fracasos propios, no teoría.
- PROHIBIDO: "en el mundo actual", "revolucionario", "sinergia",
  "desbloquear el potencial", "no es solo X, es Y", emojis en el cuerpo,
  preguntas retóricas al inicio.
- Usa "nosotros" para hablar de LegalGo, "yo" para opiniones.

ESTRUCTURA DEL POST:
1. Primera línea: una afirmación concreta y contraintuitiva (máx 12 palabras)
2. Salto de línea
3. Contexto en 2-3 líneas cortas
4. El insight, con un dato o anécdota real
5. Cierre: una implicación práctica. Sin CTA de venta.

LONGITUD: 120-180 palabras. Párrafos de máximo 2 líneas.

Genera 2 variantes distintas del post sobre la idea que te daré.
Devuelve JSON: {"variante_a": "...", "variante_b": "...", "gancho_visual": "..."}
```

**Idea de entrada (fila del Sheet):**
> `Tema: 40% de las PyMEs mexicanas no sabe cuántos contratos vigentes tiene | Ángulo: no es negligencia, es que nadie es dueño del proceso | Dato: encuesta propia a 87 clientes`

**Salida (variante A):**

> El 40% de las PyMEs que auditamos no sabía cuántos contratos vigentes tenía.
>
> No es descuido.
>
> Preguntamos a 87 clientes quién era el responsable de los contratos. Las respuestas: legal, finanzas, el asistente de dirección, "depende del contrato".
>
> Cuatro respuestas distintas en la misma empresa significa cero responsables.
>
> El contrato se firma, se escanea, se guarda en el correo de alguien y desaparece hasta que hay un problema. Entonces alguien pasa tres días buscándolo.
>
> Antes de comprar software, defina una persona. Una sola. Aunque el archivo siga siendo una carpeta de Drive.
>
> La herramienta no arregla un proceso sin dueño. Lo hace más rápido y más caro.

**Por qué funciona:** el prompt no pide "un post sobre contratos". Define audiencia, prohibiciones explícitas, estructura y longitud. El 80% de la calidad está en el prompt de sistema, no en el modelo.

**Resultados a 90 días:** de 0 a 12 posts/mes, ~25 min semanales de revisión del fundador, 3 leads calificados atribuidos directamente a LinkedIn.

---

### Ejemplo C — Calificación automática de leads

**Contexto:** *Fábrica de Datos*, consultora de analítica en Santiago. Recibe ~60 leads/mes por formulario web. El 60% no tiene presupuesto ni tamaño para su servicio, pero el equipo comercial descubre eso después de agendar y hacer la llamada. Costo: ~20 horas mensuales desperdiciadas.

**Flujo:**

```
[Webhook: formulario web enviado]
        ↓
[Nodo Set: normalizar campos, extraer dominio del email]
        ↓
[IF: ¿email corporativo?]  ← descarta gmail/hotmail si el servicio es B2B enterprise
        ↓
[HTTP Request: enriquecimiento] → tamaño de empresa, industria, sitio web
        ↓
[Nodo IA - Scoring]  → puntaje 0-100 + razonamiento + señales
        ↓
[Switch por puntaje]
   ├─ 80-100 (Caliente) → [Notificar Slack #ventas + @head_of_sales]
   │                     → [Email personalizado con link a agenda directa]
   │                     → [HubSpot: crear deal en etapa "Contacto"]
   ├─ 50-79  (Tibio)    → [Secuencia de nurturing: 3 emails educativos]
   │                     → [HubSpot: contacto en lista "Nurturing"]
   └─ 0-49   (Frío)     → [Email con recursos gratuitos + calculadora]
                        → [HubSpot: lista "Educación"]
        ↓
[Google Sheets: log completo con puntaje y razonamiento]
```

**Prompt de scoring:**

```
Eres el analista de calificación de leads de Fábrica de Datos, 
consultora de analítica de datos en Chile.

CLIENTE IDEAL (ICP):
- Empresas de 50-500 empleados
- Industrias: retail, banca, seguros, salud privada, logística
- Ya tienen datos pero no los usan (ERP/CRM implementado, sin BI)
- Presupuesto mínimo proyecto: USD 15.000
- Decisor: gerente/director de operaciones, TI, o comercial

ANTI-ICP (descartar):
- Startups pre-revenue, freelancers, agencias que revenden
- Buscan solo un dashboard puntual o un curso
- Estudiantes o investigación académica

RÚBRICA (suma 100):
- Ajuste de tamaño de empresa: 0-25
- Ajuste de industria: 0-20
- Urgencia y especificidad del problema descrito: 0-25
- Señales de presupuesto (menciona presupuesto, plazo, proyecto formal): 0-20
- Autoridad del contacto (cargo): 0-10

Penaliza -30 si detectas cualquier señal de ANTI-ICP.

DATOS DEL LEAD:
Nombre: {{ $json.nombre }}
Cargo: {{ $json.cargo }}
Empresa: {{ $json.empresa }}
Email: {{ $json.email }}
Empleados (enriquecido): {{ $json.empleados }}
Industria (enriquecida): {{ $json.industria }}
Mensaje: {{ $json.mensaje }}

Devuelve SOLO JSON:
{
  "puntaje": 0-100,
  "temperatura": "caliente|tibio|frio",
  "razonamiento": "2 frases explicando el puntaje",
  "senal_mas_fuerte": "...",
  "bandera_roja": "... o null",
  "pregunta_clave_para_la_llamada": "la pregunta que el vendedor debe hacer primero"
}
```

**Ejemplo de entrada y salida:**

*Entrada:* `Cargo: Subgerente de Operaciones | Empresa: Distribuidora Los Andes (180 empleados, logística) | Mensaje: "Tenemos SAP hace 6 años y seguimos armando reportes en Excel. El gerente general pidió un tablero de indicadores para el directorio de marzo. ¿Cuánto demora un proyecto así?"`

*Salida:*
```json
{
  "puntaje": 88,
  "temperatura": "caliente",
  "razonamiento": "Tamaño e industria en el centro del ICP, con ERP implementado y datos sin explotar. Hay un plazo externo (directorio de marzo) y patrocinio del gerente general.",
  "senal_mas_fuerte": "Plazo definido impuesto por la gerencia general",
  "bandera_roja": null,
  "pregunta_clave_para_la_llamada": "¿Qué decisiones específicas necesita tomar el directorio con ese tablero?"
}
```

**Detalle crítico:** el campo `pregunta_clave_para_la_llamada` fue lo que más valoró el equipo comercial. La IA no solo filtra, prepara al vendedor.

**Resultados a 4 meses:**
- Tasa de leads que llegan a llamada agendada: 41% → 78%
- Tiempo de respuesta a leads calientes: 6 horas → 4 minutos
- Concordancia IA vs. calificación humana: 84% (midieron 100 leads en paralelo durante el primer mes antes de confiar en el sistema)

---

## 4. Ejercicio práctico: tu primer flujo con IA

> **Qué vas a construir:** un asistente que revisa tu bandeja de entrada cada mañana, clasifica los correos nuevos por urgencia e intención, redacta un borrador de respuesta para los importantes, y te envía un resumen a Telegram.
>
> **Tiempo:** 90-120 minutos.
> **Costo:** USD 0 (plan gratuito de n8n Cloud + ~USD 0.30 de API de IA).

### Paso 0 — Preparación (15 min)

1. Crea cuenta en [n8n.io](https://n8n.io) → plan de prueba cloud. *(Alternativa gratuita permanente: instalar con Docker, pero para este ejercicio usa la nube.)*
2. Consigue una API key de un proveedor de IA:
   - OpenAI: platform.openai.com → API keys → carga USD 5 de crédito
   - o Google AI Studio (Gemini): tiene capa gratuita generosa, ideal para practicar
3. Crea un bot de Telegram:
   - Abre Telegram, busca **@BotFather**
   - Envía `/newbot`, elige nombre y usuario
   - Guarda el **token** que te devuelve
   - Envíale un mensaje a tu bot, luego visita `https://api.telegram.org/bot<TU_TOKEN>/getUpdates` y copia tu **chat_id**

**Checkpoint:** tienes 3 cosas guardadas en un archivo de texto: URL de n8n, API key de IA, token + chat_id de Telegram.

---

### Paso 1 — Crear el workflow y el disparador (10 min)

1. En n8n: **Workflows → Add