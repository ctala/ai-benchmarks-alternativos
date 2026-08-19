# Qwen 3.8 27B — startup_content/curso_emprendimiento_modulo

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 82.562s | tokens_per_second: 142.4
- input_tokens: 270 | output_tokens: 11755
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores, con ejemplos prácticos y explicaciones detalladas sobre la automatización con IA.

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



# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

> **Curso:** IA Práctica para Emprendedores  
> **Nivel:** Emprendedor no técnico  
> **Enfoque:** Hands-on, con ejercicios aplicables y ejemplos reales

---

## 1. Objetivo del módulo

En este módulo aprenderás a convertir tareas repetitivas de tu emprendimiento en flujos de trabajo automatizados con ayuda de IA. No necesitas saber programar: aprenderás a identificar procesos que valen la pena automatizar, entender cómo funcionan herramientas como **N8N**, y construir flujos simples para atención al cliente, generación de contenido y calificación de leads. Al finalizar, podrás diseñar tu primer flujo automatizado, probarlo de forma segura y medir su impacto en tiempo, costo y resultados.

---

## 2. Contenido teórico

### 2.1 ¿Qué es automatización con IA?

La **automatización con IA** consiste en usar software para que tareas repetitivas se realicen solas o con poca intervención humana, y usar inteligencia artificial para que el sistema pueda:

- Leer mensajes, formularios, correos o documentos.
- Clasificar información.
- Responder preguntas frecuentes.
- Generar textos.
- Calificar leads.
- Tomar decisiones simples con reglas + IA.

Ejemplo práctico:

> Cuando un cliente escribe por WhatsApp: “¿Cuánto cuesta el plan anual?”, el sistema puede responder automáticamente con la información correcta y, si la pregunta es compleja, avisar a una persona.

### 2.2 Diferencia entre automatización tradicional y automatización con IA

| Tipo de automatización | Ejemplo | Limitación |
|---|---|---|
| Tradicional / por reglas | Si llega un correo con “factura”, moverlo a carpeta “Facturas” | Solo funciona con reglas exactas |
| Con IA | Clasificar un mensaje como “consulta de precio”, “queja” o “soporte técnico” aunque esté redactado de muchas formas | Requiere supervisión y buenas instrucciones |

La IA no “reemplaza” la automatización; la hace más flexible.

---

### 2.3 Anatomía de un flujo de trabajo automatizado

Un flujo de trabajo con IA normalmente tiene 5 partes:

| Parte | Pregunta clave | Ejemplo |
|---|---|---|
| **Trigger / disparador** | ¿Qué inicia el flujo? | Alguien envía un formulario, llega un correo, se publica una publicación |
| **Datos de entrada** | ¿Qué información recibe el sistema? | Nombre, email, mensaje, producto, precio |
| **Procesamiento con IA** | ¿Qué decide o genera la IA? | Clasificar lead, responder pregunta, generar texto |
| **Acción** | ¿Qué hace el sistema después? | Enviar email, guardar en hoja, actualizar CRM, publicar contenido |
| **Revisión humana** | ¿Dónde interviene una persona? | Aprobación final, casos complejos, quejas |

---

### 2.4 Herramientas para automatizar: N8N

**N8N** es una plataforma visual para crear flujos de trabajo automatizados. Puedes conectar aplicaciones como:

- Google Sheets
- Gmail
- WhatsApp Business API
- Instagram / Facebook
- HubSpot
- Pipedrive
- Typeform
- Slack
- OpenAI
- Groq
- Otras herramientas de IA

#### ¿Por qué N8N es útil para startups?

- **Visual:** arrastras nodos y conectas aplicaciones.
- **Flexible:** puedes automatizar procesos internos y externos.
- **Económico:** comparado con contratar desarrollo a medida.
- **Escalable:** empieza con un flujo simple y luego crece.
- **Permite IA:** puedes integrar modelos de lenguaje para clasificar, resumir o responder.

#### Formas de usar N8N

1. **N8N Cloud**  
   Recomendado para emprendedores no técnicos. La empresa se encarga del servidor.

2. **N8N self-hosted**  
   Tú lo instalas en tu propio servidor. Da más control, pero requiere conocimientos técnicos.

3. **N8N local / Docker**  
   Opción avanzada para equipos técnicos.

Para este curso, la opción más práctica es **N8N Cloud** o una cuenta de prueba.

---

### 2.5 Otras herramientas similares

| Herramienta | Ideal para | Nota |
|---|---|---|
| **N8N** | Flujos complejos, IA, control avanzado | Muy flexible |
| **Make** | Automatizaciones visuales sencillas | Buena para no técnicos |
| **Zapier** | Conectar apps populares rápidamente | Fácil, pero puede ser más caro |
| **Flowise** | Crear agentes de IA con interfaz visual | Más enfocado en IA |
| **LangChain** | Desarrollo de agentes con código | Para equipos técnicos |

---

### 2.6 Principios clave para automatizar con IA

1. **Empieza con un proceso doloroso y repetitivo.**  
   No automatices todo. Elige una tarea que consuma tiempo y tenga reglas claras.

2. **Define bien el criterio.**  
   Si quieres calificar leads, define qué es “caliente”, “tibio” y “frío”.

3. **Usa IA para decisiones, no para todo.**  
   La IA puede clasificar o responder, pero las decisiones críticas deben tener revisión humana.

4. **Prueba antes de activar.**  
   Usa datos de prueba, no clientes reales, hasta que el flujo funcione bien.

5. **Mide resultados.**  
   Tiempo ahorrado, respuestas más rápidas, más leads calificados, menos tareas manuales.

6. **Cuida los datos.**  
   No envíes información sensible a servicios de IA sin entender las políticas de privacidad.

---

## 3. Ejemplos prácticos de automatización para startups

### 3.1 Atención al cliente automatizada

#### Caso real

Una startup de cursos online recibe muchos mensajes por WhatsApp e Instagram con preguntas como:

- ¿Cómo pago?
- ¿Cuándo inicia el curso?
- ¿Qué incluye el plan?
- ¿Tienen descuento?
- ¿Puedo ver una demo?

#### Flujo recomendado

1. **Disparador:** llega un mensaje por WhatsApp, Instagram o email.
2. **IA lee el mensaje** y lo clasifica:
   - Consulta de precio
   - Soporte técnico
   - Queja
   - Venta
   - Spam
3. **IA responde** con información de la base de conocimiento.
4. **Si la pregunta es compleja**, el flujo envía una alerta a un humano.
5. **Registro:** el mensaje y la respuesta se guardan en Google Sheets o CRM.

#### Ejemplo de instrucción para la IA

```text
Eres un asistente de atención al cliente de una startup de cursos online.
Responde de forma clara, breve y amable.
Solo usa la información proporcionada.
Si no sabes la respuesta, di: “Un asesor te contactará en breve”.
No inventes precios, fechas ni políticas.
```

#### KPIs para medir

- Tiempo de primera respuesta.
- % de mensajes resueltos sin humano.
- Satisfacción del cliente.
- Escalamientos a humano.
- Volumen de consultas por categoría.

#### Recomendación

No dejes la IA respondiendo sin supervisión. Revisa una muestra diaria durante las primeras 2 semanas.

---

### 3.2 Generación de contenido para redes sociales

#### Caso real

Una startup de productos naturales necesita publicar en Instagram, TikTok y LinkedIn, pero no tiene tiempo de redactar todos los posts.

#### Flujo recomendado

1. **Disparador:** se agrega un producto o tema en Google Sheets.
2. **IA genera 3 versiones de contenido:**
   - Post para Instagram
   - Guion corto para TikTok
   - Post profesional para LinkedIn
3. **El contenido se guarda** en una hoja o se envía por email para aprobación.
4. **Una persona aprueba** y publica manualmente o conecta el flujo a Buffer, Meta Business o Later.

#### Entrada de ejemplo

```text
Producto: snack de arándano bajo en azúcar
Beneficio: energía para gimnasio
Público: adultos 25-40 años
Tono: cercano, motivador
```

#### Salida de ejemplo

**Instagram:**

> ¿Entrenas y buscas algo que no te quite energía?  
> Nuestro snack de arándano bajo en azúcar te acompaña antes y después del gimnasio.  
> 🍇 Energía natural  
> 💪 Sin exceso de azúcar  
> 👉 Pide el tuyo en el link del perfil.

**TikTok:**

> “Si entrenas y comes mal, no es de extrañar que te sientas cansado.”  
> Muestra el snack.  
> “Este snack de arándano bajo en azúcar te da energía sin el bajón de azúcar.”  
> CTA: “Pídelo hoy”.

**LinkedIn:**

> Muchos equipos productivos subestiman el impacto de los snacks en su rendimiento.  
> Elegir opciones con menos azúcar y más ingredientes naturales puede ayudar a mantener energía estable durante el día.

#### KPIs para medir

- Número de publicaciones por semana.
- Tiempo invertido en creación de contenido.
- Engagement por tipo de red.
- Tasa de aprobación del contenido generado.

#### Recomendación

La IA puede generar borradores, pero la voz de marca debe ser revisada por una persona.

---

### 3.3 Calificación automática de leads

#### Caso real

Una startup B2B recibe leads desde formularios, WhatsApp y eventos. El equipo comercial pierde tiempo revisando mensajes que no están listos para comprar.

#### Flujo recomendado

1. **Disparador:** llega un lead por formulario, WhatsApp o CRM.
2. **IA analiza el mensaje** y asigna una categoría:
   - Caliente
   - Tibio
   - Frío
3. **IA genera una puntuación** de 0 a 100.
4. **El lead se guarda** en Google Sheets o CRM.
5. **Acción automática:**
   - Si es caliente: enviar email de ventas o notificar al equipo.
   - Si es tibio: enviar secuencia de nutrición.
   - Si es frío: archivar o enviar contenido educativo.

#### Criterios de calificación

| Categoría | Señales |
|---|---|
| **Caliente** | Pregunta por precio, compra, implementación, presupuesto, urgencia, tamaño de empresa, fecha de inicio |
| **Tibio** | Pregunta información general, quiere conocer más, no tiene urgencia |
| **Frío** | No hay interés claro, spam, fuera de segmento, solo pide descuento sin contexto |

#### Ejemplo de instrucción para la IA

```text
Eres un clasificador de leads para una startup B2B.
Analiza el mensaje y devuelve una puntuación de 0 a 100.
También indica la categoría: CALIENTE, TIBIO o FRI.
Devuelve solo JSON:
{
  "score": 80,
  "categoria": "CALIENTE",
  "motivo": "El lead pregunta por precio y quiere implementar este mes."
}
```

#### KPIs para medir

- % de leads calificados correctamente.
- Tiempo para contactar leads calientes.
- Tasa de conversión de leads calientes a reunión.
- Número de leads fríos eliminados automáticamente.

#### Recomendación

Al inicio, usa la IA como asistente: ella clasifica, pero un humano revisa los leads calientes.

---

## 4. Ejercicio práctico paso a paso

# Ejercicio: Califica leads entrantes con IA y guárdalos en Google Sheets

En este ejercicio construirás un flujo simple en **N8N** que:

1. Recibe un formulario con:
   - Nombre
   - Email
   - Mensaje
2. Usa IA para clasificar el lead como:
   - CALIENTE
   - TIBIO
   - FRI
3. Guarda la información en Google Sheets.
4. Opcionalmente, envía un aviso por email si el lead es caliente.

---

## 4.1 Resultado esperado

Al finalizar tendrás:

- Un formulario web.
- Un flujo en N8N.
- Una hoja de Google Sheets con leads clasificados.
- Un proceso automatizado que puedes mejorar después.

**Duración estimada:** 60 a 90 minutos.

---

## 4.2 Herramientas necesarias

| Herramienta | Para qué |
|---|---|
| **N8N** | Crear el flujo automatizado |
| **Google Sheets** | Guardar leads |
| **OpenAI, Groq u otro proveedor de IA** | Clasificar el lead |
| **Gmail o Resend** | Opcional: enviar aviso por email |

> **Recomendación para no técnicos:** usa N8N Cloud o una cuenta de prueba para no preocuparte por servidores.

---

## 4.3 Antes de empezar

Completa esta lista:

- [ ] Tengo una cuenta en N8N.
- [ ] Tengo una cuenta de Google.
- [ ] Tengo una API key de un proveedor de IA, por ejemplo OpenAI o Groq.
- [ ] Sé cuál es el objetivo del lead: vender curso, servicio, software, producto, etc.
- [ ] Tengo claro qué significa lead caliente, tibio y frío.

---

## 4.4 Paso 1: Define el criterio de calificación

Antes de tocar N8N, escribe en un documento:

```text
Mi startup vende: ________________________

Lead CALIENTE:
- Pregunta por precio
- Quiere comprar pronto
- Tiene presupuesto
- Pregunta por implementación
- Tiene urgencia

Lead TIBIO:
- Pregunta información general
- Quiere conocer más
- No tiene fecha clara
- No menciona presupuesto

Lead FRI:
- No hay interés claro
- Es spam
- Está fuera de segmento
- Solo pide descuento sin contexto
```

Ejemplo:

```text
Mi startup vende: software de gestión para clínicas dentales.

Lead CALIENTE:
- Pregunta por precio
- Quiere implementar en 1 mes
- Tiene 2 o más sedes
- Pregunta por demo

Lead TIBIO:
- Pregunta qué hace el software
- Quiere más información
- No tiene fecha

Lead FRI:
- Pregunta por trabajo
- No es clínica dental
- Spam
```

---

## 4.5 Paso 2: Crea la hoja de Google Sheets

1. Entra a [Google Sheets](https://sheets.google.com).
2. Crea una hoja nueva.
3. Ponle nombre: **Leads IA**.
4. Crea las siguientes columnas:

| A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|
| Fecha | Nombre | Email | Mensaje | Categoría | Score | Motivo | Estado |

Deja la primera fila como encabezados.

Ejemplo:

| Fecha | Nombre | Email | Mensaje | Categoría | Score | Motivo | Estado |
|---|---|---|---|---|---|---|---|
| 2026-01-01 | María | maria@ejemplo.com | Quiero comprar para 10 personas y pagar hoy | CALIENTE | 90 | Urgencia y compra clara | Pendiente |

---

## 4.6 Paso 3: Crea el flujo en N8N

1. Entra a tu cuenta de N8N.
2. Crea un nuevo flujo.
3. Ponle nombre: **Calificación de leads con IA**.

Vamos a usar estos nodos:

| Nodo | Función |
|---|---|
| **Form / Webhook** | Recibe el formulario |
| **IA / LLM** | Clasifica el lead |
| **Google Sheets** | Guarda el lead |
| **Email** | Opcional: avisa si el lead es caliente |

> Si tu versión de N8N no tiene nodo **Form**, usa un **Webhook** conectado a un formulario externo como Google Forms, Typeform o Jotform.

---

## 4.7 Paso 4: Configura el formulario

### Opción A: Usar Form Trigger

1. Busca el nodo **Form** o **Form Trigger**.
2. Agrégalo al flujo.
3. Configura los campos:

| Campo | Tipo |
|---|---|
| nombre | Texto |
| email | Email |
| mensaje | Texto largo |

4. Guarda el nodo.

Al activar el flujo, N8N te dará un enlace del formulario.

### Opción B: Usar Webhook + formulario externo

1. Crea un formulario en Google Forms, Typeform o Jotform.
2. Configura el formulario para que envíe datos por webhook.
3. En N8N, agrega un nodo **Webhook**.
4. Copia la URL del webhook de N8N y pégala en tu formulario.

---

## 4.8 Paso 5: Agrega el nodo de IA

1. Conecta el nodo de formulario a un nodo de IA.
2. Busca un nodo como:
   - **OpenAI**
   - **AI Agent**
   - **LLM**
   - **Groq**
   - Otro proveedor de IA compatible.

3. Configura las credenciales del proveedor de IA.
4. Escribe la instrucción del sistema.

### Prompt recomendado para clasificación simple

```text
Eres un asistente de calificación de leads para una startup.
Analiza el mensaje y responde SOLO con UNA palabra:

CALIENTE
TIBIO
FRI

Reglas:
- CALIENTE: el lead muestra interés claro, pregunta por precio, compra, implementación, presupuesto o tiene urgencia.
- TIBIO: el lead muestra interés general, pregunta información, pero no hay urgencia clara.
- FRI: no hay interés claro, es spam, está fuera de segmento o solo pide descuento sin contexto.

No agregues explicaciones.
No agregues punto final.
Solo escribe una de estas palabras: CALIENTE, TIBIO o FRI.

Mensaje del lead: {{ $json.mensaje }}
```

> Si el nodo de IA permite “structured output” o “JSON”, puedes usar una versión más avanzada.

### Prompt avanzado con JSON

```text
Eres un clasificador de leads para una startup.
Analiza el mensaje del lead y devuelve únicamente JSON válido.

Formato:
{
  "score": 0,
  "categoria": "CALIENTE",
  "motivo": "explicación breve"
}

Reglas:
- score: número de 0 a 100
- categoria: CALIENTE, TIBIO o FRI
- motivo: máximo 20 palabras

Mensaje del lead: {{ $json.mensaje }}
```

---

## 4.9 Paso 6: Conecta Google Sheets

1. Agrega un nodo **Google Sheets**.
2. Conéctalo al nodo de IA.
3. Selecciona la hoja **Leads IA**.
4. Elige la operación: **Append** o **Añadir fila**.
5. Mapea los campos.

Ejemplo de mapeo:

| Columna de Google Sheets | Valor en N8N |
|---|---|
| Fecha | `{{ $now }}` o fecha actual |
| Nombre | `{{ $json.nombre }}` |
| Email | `{{ $json.email }}` |
| Mensaje | `{{ $json.mensaje }}` |
| Categoría | `{{ $json.message }}` o `{{ $json.output }}` |
| Score | vacío en versión simple |
| Motivo | vacío en versión simple |
| Estado | `Pendiente` |

> El nombre del campo de salida puede variar según el nodo de IA. Busca el campo que contenga la respuesta de texto.

---

## 4.10 Paso 7: Opcional — Envía email si el lead es caliente

Si quieres automatizar el aviso:

1. Agrega un nodo **IF**.
2. Conéctalo después del nodo de IA.
3. Configura la condición:

```text
Si el texto de la IA contiene: CALIENTE
```

4. En la rama **true**, agrega un nodo de email.
5. Configura el email:

**Asunto:**

```text
Nuevo lead caliente: {{ $json.nombre }}
```

**Cuerpo:**

```text
Nombre: {{ $json.nombre }}
Email: {{ $json.email }}
Mensaje: {{ $json.mensaje }}
Categoría: {{ $json.message }}

Revisa este lead pronto.
```

6. En la rama **false**, puedes conectar directamente a Google Sheets si prefieres no enviar email.

> **Importante:** si usas el nodo IF, asegúrate de que la IA responda exactamente “CALIENTE”, “TIBIO” o “FRI”.

---

## 4.11 Paso 8: Prueba el flujo

Antes de compartir el formulario con clientes reales:

1. Activa el flujo en modo prueba.
2. Abre el enlace del formulario.
3. Envía un mensaje de prueba:

```text
Hola, quiero comprar para 10 personas y pagar hoy.
```

4. Revisa Google Sheets.
5. Verifica que la categoría sea **CALIENTE**.

Envía otro mensaje:

```text
Solo quería saber qué incluye el plan.
```

Debería ser **TIBIO**.

Envía un mensaje frío:

```text
¿Tienen trabajo disponible?
```

Debería ser **FRI**.

---

## 4.12 Paso 9: Activa el flujo

1. Cuando las pruebas funcionen bien, activa el flujo.
2. Copia el enlace del formulario.
3. Compártelo en tu web, redes sociales o correo.
4. Revisa diariamente la hoja durante la primera semana.
5. Corrige el prompt si la IA clasifica mal.

---

## 4.13 Problemas comunes y soluciones

| Problema | Posible causa | Solución |
|---|---|---|
| La IA responde con explicaciones | Prompt no es estricto | Pide “solo una palabra” y da ejemplos |
| El lead no llega a Google Sheets | Credenciales incorrectas | Verifica conexión con Google |
| El formulario no dispara el flujo | Flujo desactivado o webhook incorrecto | Activa el flujo y prueba el webhook |
| La categoría sale vacía | Mapeo incorrecto en Google Sheets | Revisa el campo de salida del nodo IA |
| El lead caliente no envía email | Condición IF incorrecta | Verifica que la IA escriba exactamente “CALIENTE” |
| El costo de IA sube | Demasiadas llamadas o mensajes largos | Limita longitud del mensaje y usa modelo más económico |

---

## 4.14 Checklist final del ejercicio

- [ ] Creé el formulario.
- [ ] Configuré el nodo de IA.
- [ ] Conecté Google Sheets.
- [ ] Probé con 3 tipos de leads.
- [ ] Activé el flujo.
- [ ] Compartí el enlace del formulario.
- [ ] Definí quién revisa los leads calientes.
- [ ] Mediré resultados cada semana.

---

## 5. Recursos adicionales

### 5.1 Documentación oficial

- **N8N Docs:** https://docs.n8n.io  
  Documentación de nodos, credenciales y automatizaciones.

- **N8N Templates:** https://n8n.io/workflows  
  Plantillas listas para importar y modificar.

- **OpenAI API:** https://platform.openai.com  
  Para crear API keys y entender costos.

- **Groq Console:** https://console.groq.com  
  Alternativa para modelos de lenguaje con planes gratuitos o económicos.

- **Google Sheets:** https://sheets.google.com  
  Para guardar leads y contenido.

---

### 5.2 Plantillas útiles para buscar en N8N

Busca términos como:

- `AI lead qualification`
- `Form to Google Sheets`
- `AI agent customer support`
- `Social media content generator`
- `CRM lead scoring`
- `WhatsApp AI assistant`

> Al importar una plantilla, revisa siempre qué datos envía y qué permisos requiere.

---

### 5.3 Guía rápida para escribir prompts efectivos

Usa esta estructura:

```text
ROL:
Eres un asistente de ventas / soporte / contenido.

TAREA:
Clasifica / responde / genera.

FORMATO:
Responde en JSON / solo una palabra / 3 bullets.

RESTRICCIONES:
No inventes información.
Si no sabes, di X.
Máximo X palabras.

EJEMPLO:
Entrada: ...
Salida: ...
```

Ejemplo:

```text
ROL:
Eres un asistente de atención al cliente.

TAREA:
Responde la pregunta del cliente usando solo la información proporcionada.

FORMATO:
Máximo 3 frases.

RESTRICCIONES:
No inventes precios.
No prometas fechas.
Si no sabes, di: “Un asesor te contactará en breve”.
```

---

### 5.4 Seguridad y privacidad

Antes de automatizar con datos de clientes:

- Revisa la política de privacidad del proveedor de IA.
- No envíes datos sensibles innecesarios.
- Pide consentimiento si es necesario.
- Limita el acceso a hojas y credenciales.
- Usa revisión humana para decisiones importantes.
- Guarda solo la información que realmente necesitas.

---

### 5.5 Métricas recomendadas

| Proceso | Métrica |
|---|---|
| Atención al cliente | Tiempo de primera respuesta |
| Atención al cliente | % de tickets resueltos sin humano |
| Contenido | Publicaciones por semana |
| Contenido | Tiempo ahorrado en redacción |
| Leads | % de leads clasificados correctamente |
| Leads | Tiempo para contactar lead caliente |
| Leads | Conversión de lead a reunión |

---

## 6. Preguntas de autoevaluación

### Pregunta 1

En un flujo de trabajo automatizado, ¿qué elemento define cuándo inicia el proceso?

a) La hoja de Google Sheets  
b) El nodo de IA  
c) El disparador o trigger  
d) El email de respuesta  

**Respuesta correcta:** c) El disparador o trigger.

---

### Pregunta 2

¿Qué práctica es más importante antes de activar un flujo de atención al cliente con IA?

a) Usar el modelo de IA más caro  
b) Publicar el flujo en redes sociales  
c) Probar con mensajes de ejemplo y revisar las respuestas  
d) Eliminar la revisión humana para ahorrar tiempo  

**Respuesta correcta:** c) Probar con mensajes de ejemplo y revisar las respuestas.

---

### Pregunta 3

Un lead escribe:

> “Necesito implementar el sistema en mi clínica antes de fin de mes. ¿Cuánto cuesta y tienen demo?”

¿Cómo debería clasificar la IA?

a) FRI  
b) TIBIO  
c) CALIENTE  
d) No se puede clasificar  

**Respuesta correcta:** c) CALIENTE.