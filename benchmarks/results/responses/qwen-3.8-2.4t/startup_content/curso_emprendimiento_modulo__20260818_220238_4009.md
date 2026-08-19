# Qwen 3.8 2.4T (A95B) — startup_content/curso_emprendimiento_modulo

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 106.271s | tokens_per_second: 105.8
- input_tokens: 270 | output_tokens: 11240

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



# Módulo 3  
## **Automatización con IA: De la idea al flujo de trabajo**

---

## 1. Objetivo del módulo

Al finalizar este módulo, el emprendedor será capaz de identificar oportunidades de automatización dentro de su negocio, comprender cómo funcionan los flujos de trabajo con inteligencia artificial y diseñar una automatización práctica usando herramientas visuales como **N8N**, con el fin de ahorrar tiempo, reducir tareas repetitivas y mejorar la respuesta de su startup frente a clientes, leads y contenido.

---

## 2. Contenido teórico: automatización con IA para emprendedores

### 2.1 ¿Qué es automatización con IA?

La **automatización tradicional** ejecuta tareas cuando ocurre algo específico.  
Por ejemplo: “Si llega un correo, guárdalo como tarea”.

La **automatización con IA** va más allá: no solo ejecuta tareas, sino que también puede **interpretar, clasificar, redactar, resumir o tomar decisiones simples** a partir de información no estructurada.

En palabras simples:

> automatización = “hacer tareas sin repetirlas manualmente”  
> IA = “darle criterio inteligente a esas tareas”

Ejemplos cotidianos:

- Recibir mensajes de clientes y que una IA responda preguntas frecuentes.
- Publicar un formulario de contacto y que la IA clasifique si el lead es frío, tibio o caliente.
- Tener una hoja de cálculo con ideas y que la IA genere textos para redes sociales.
- Recibir solicitudes de soporte y que la IA detecte la urgencia antes de pasarlas al equipo humano.

Para una startup, automatizar con IA no significa reemplazar personas. Significa **liberar tiempo humano para tareas de mayor valor**, como cerrar ventas, atender casos complejos o mejorar el producto.

---

### 2.2 ¿Qué es un flujo de trabajo automatizado?

Un flujo de trabajo automatizado, también llamado **workflow**, es una secuencia de pasos conectados entre sí.

Normalmente tiene estos componentes:

| Componente | Significado sencillo | Ejemplo |
|---|---|---|
| **Disparador o trigger** | El evento que inicia el proceso | Llega un nuevo mensaje, un formulario o una fila nueva en Google Sheets |
| **Nodo o paso** | Cada acción dentro del flujo | Clasificar, escribir, enviar, guardar |
| **Condición** | Una regla para decidir el siguiente paso | Si el lead es caliente, notificar al equipo de ventas |
| **Acción final** | El resultado útil | Enviar respuesta, actualizar CRM, crear tarea |
| **Datos** | La información que viaja por el flujo | Nombre, correo, mensaje, categoría |

Ejemplo visual simplificado:

```text
Nuevo lead en formulario
        ↓
La IA analiza el mensaje
        ↓
Clasifica como frío, tibio o caliente
        ↓
Guarda el resultado en Google Sheets
        ↓
Si es caliente, envía alerta a ventas
```

Este tipo de flujo puede construirse sin saber programar usando herramientas visuales.

---

### 2.3 Herramientas de automatización: enfoque en N8N

Una de las herramientas más útiles para crear automatizaciones es **N8N**.

¿Qué es N8N?

> **N8N** es una plataforma visual que permite conectar aplicaciones y crear flujos de trabajo automatizados usando nodos.

Con N8N puedes conectar, por ejemplo:

- Google Sheets
- WhatsApp
- Gmail
- CRM
- Formularios
- Bases de datos
- Inteligencia artificial
- Slack
- Telegram
- Plataformas de pago
- Redes sociales

#### Ventajas de N8N para startups

- Permite crear flujos visuales sin escribir código complejo.
- Tiene nodos para muchas aplicaciones populares.
- Puede integrar modelos de IA para clasificar, escribir o analizar.
- Es flexible: sirve para marketing, ventas, soporte y operaciones.
- Puede usarse en la nube o en un servidor propio.
- Es útil para startups que quieren automatizar procesos sin contratar un equipo técnico grande.

#### Alternativas similares

Aunque en este módulo usamos N8N como referencia, también existen otras herramientas:

| Herramienta | Ideal para |
|---|---|
| **N8N** | Automatizaciones flexibles, potentes y escalables |
| **Make** | Emprendedores que quieren una interfaz visual amigable |
| **Zapier** | Automatizaciones simples con muchas apps conocidas |
| **Pipedream** | Perfiles un poco más técnicos |
| **Google Apps Script** | Automatizaciones dentro de Google Workspace |

Para un emprendedor no técnico, la recomendación es empezar con una plataforma visual, usar plantillas y automatizar procesos pequeños antes de crear sistemas complejos.

---

### 2.4 Conceptos clave explicados sin tecnicismos

Aunque no seas programador, te ayudará entender algunos términos frecuentes.

#### API

Una **API** es como un puente que permite que dos aplicaciones se comuniquen.

Ejemplo:  
Tu flujo en N8N puede “hablar” con Google Sheets a través de su API para leer o escribir datos.

#### Webhook

Un **webhook** es una dirección especial que recibe información cuando ocurre algo.

Ejemplo:  
Cuando alguien completa un formulario, ese formulario puede enviar los datos a un webhook, y ese webhook activa tu flujo automatizado.

#### Nodo

Un **nodo** es cada paso dentro del flujo.

Ejemplo:  
Un nodo recibe el lead, otro nodo llama a la IA, otro nodo guarda el resultado y otro nodo envía una notificación.

#### Prompt

Un **prompt** es la instrucción que le das a la IA.

Ejemplo:  
“Clasifica este lead según su mensaje, presupuesto e interés. Devuelve una categoría: frío, tibio o caliente”.

#### CRM

Un **CRM** es un sistema para gestionar clientes y oportunidades.

Ejemplos:  
HubSpot, Pipedrive, Zoho CRM, Notion, Airtable o incluso una hoja de Google Sheets bien organizada.

---

### 2.5 ¿Qué se puede automatizar con IA en una startup?

Algunas áreas comunes:

#### Marketing

- Generar ideas de contenido.
- Crear borradores para redes sociales.
- Resumir artículos para boletines.
- Personalizar mensajes según tipo de cliente.

#### Ventas

- Clasificar leads.
- Responder solicitudes iniciales.
- Crear seguimientos automáticos.
- Preparar resúmenes de reuniones.

#### Atención al cliente

- Responder preguntas frecuentes.
- Detectar urgencia o molestia.
- Escalar casos complejos a una persona.
- Registrar conversaciones en una base de datos.

#### Operaciones

- Organizar información de formularios.
- Generar reportes simples.
- Enviar recordatorios.
- Actualizar bases de datos.

---

### 2.6 Regla de oro antes de automatizar

Antes de automatizar, primero debes entender el proceso manual.

No automatices algo que no entiendes.  
Primero responde estas preguntas:

1. ¿Qué tarea se repite mucho?
2. ¿Quién la hace actualmente?
3. ¿Cuánto tiempo toma?
4. ¿Qué información se necesita?
5. ¿Qué decisión debe tomar la IA y cuál debe seguir siendo humana?
6. ¿Qué pasa si la IA se equivoca?
7. ¿Cómo vamos a medir si la automatización funciona?

Una automatización útil no empieza con tecnología. Empieza con un proceso claro.

---

### 2.7 Cuándo sí y cuándo no automatizar

#### Sí conviene automatizar cuando:

- La tarea se repite muchas veces.
- Hay reglas claras.
- El volumen es alto.
- Hay datos digitales.
- El error no es crítico si se supervisa.
- Puede mejorar la velocidad de respuesta.

#### No conviene automatizar cuando:

- La decisión es muy delicada.
- Falta información confiable.
- El proceso todavía es confuso.
- Se necesita mucha sensibilidad humana.
- Puede afectar gravemente la experiencia del cliente.
- No hay nadie que revise errores importantes.

Ejemplo:  
Una IA puede responder preguntas frecuentes de clientes, pero no debería manejar sola una queja legal, una crisis de reputación o una negociación delicada sin supervisión.

---

## 3. Ejemplos prácticos de automatización para startups

A continuación, tres casos prácticos pensados para startups latinoamericanas. Cada caso incluye el problema, el flujo, las herramientas y el beneficio esperado.

---

## Ejemplo 1: Atención al cliente automatizada

### Contexto

Una startup vende productos por Instagram y WhatsApp en México, Colombia o Perú. Recibe muchos mensajes como:

- “¿Cuál es el precio?”
- “¿Hacen envíos?”
- “¿Cuánto tarda la entrega?”
- “¿Tienen pagos con tarjeta?”
- “¿Dónde están ubicados?”

El equipo tarda horas en responder lo mismo.

### Objetivo

Crear un asistente que responda automáticamente las preguntas frecuentes y pase a una persona humana los casos complejos.

### Flujo automatizado

```text
Cliente escribe por WhatsApp o Instagram
        ↓
La IA analiza el mensaje
        ↓
Identifica la intención: precio, envío, pago, queja, otro
        ↓
Responde con información aprobada
        ↓
Si es una queja o caso complejo, alerta a soporte humano
        ↓
Guarda la conversación en una hoja o CRM
```

### Herramientas sugeridas

- WhatsApp Business API o Instagram Messaging
- N8N como orquestador
- OpenAI, Gemini u otro modelo de IA
- Google Sheets, Airtable o HubSpot CRM
- Slack, Telegram o correo para alertas internas

### Ejemplo de prompt para la IA

```text
Eres el asistente virtual de una tienda online. Responde de forma clara, amable y breve. Usa únicamente la información proporcionada. Si no sabes la respuesta o el cliente muestra molestia, indica que una persona del equipo lo contactará pronto. No inventes precios, plazos ni políticas.
```

### Base de conocimiento simple

La IA debería responder usando una base como esta:

| Pregunta frecuente | Respuesta aprobada |
|---|---|
| Precio del producto | Los precios actualizados están en este catálogo |
| Envíos | Enviamos en 2 a 5 días hábiles |
| Métodos de pago | Aceptamos transferencia, tarjeta y pago contra entrega |
| Devoluciones | Se aceptan devoluciones dentro de 5 días |
| Horario | Atención de lunes a viernes de 9:00 a 18:00 |

### Beneficio esperado

- Respuesta inmediata 24/7.
- Menos tiempo invertido en preguntas repetitivas.
- Mejor experiencia para el cliente.
- Equipo humano enfocado en casos importantes.

### Indicador recomendado

- Tiempo promedio de respuesta.
- Porcentaje de mensajes resueltos por IA.
- Porcentaje de conversaciones escaladas a humano.
- Nivel de satisfacción del cliente.

---

## Ejemplo 2: Generación de contenido para redes sociales

### Contexto

Una startup de servicios o una marca local necesita publicar contenido, pero no tiene tiempo para escribir textos todos los días.

Por ejemplo:

- Una cafetería.
- Una agencia pequeña.
- Un emprendimiento de bienestar.
- Una academia online.
- Una tienda de ropa.

El problema no es quedarse sin ideas, sino convertir esas ideas en textos publicables de forma constante.

### Objetivo

Automatizar la creación de borradores de contenido a partir de una lista de temas.

### Flujo automatizado

```text
El equipo registra temas en Google Sheets o Airtable
        ↓
N8N detecta una nueva fila o tema pendiente
        ↓
La IA genera una propuesta de publicación
        ↓
Crea texto, hashtags y llamado a la acción
        ↓
El humano revisa y aprueba
        ↓
Se agenda en una herramienta de publicación
```

### Herramientas sugeridas

- Google Sheets o Airtable
- N8N
- OpenAI, Gemini u otro modelo de lenguaje
- Notion para aprobación
- Metricool, Buffer, Later o Meta Business Suite
- Slack o Gmail para avisar al equipo

### Ejemplo de estructura en Google Sheets

| Fecha | Pilar de contenido | Tema | Audiencia | Estado |
|---|---|---|---|---|
| 10/03 | Producto | Beneficios del café frío | Personas que trabajan | Pendiente |
| 12/03 | Educación | Cómo conservar el café | Clientes actuales | Pendiente |

### Ejemplo de prompt para la IA

```text
Actúa como community manager de una marca latinoamericana. Crea una publicación para redes sociales basada en el tema entregado. Incluye: gancho inicial, texto breve, llamado a la acción y 5 hashtags relevantes. Tono: cercano, profesional y práctico. No uses frases exageradas ni promesas irreales.
```

### Beneficio esperado

- Producción de contenido más rápida.
- Menos bloqueo creativo.
- Mayor consistencia en redes sociales.
- Equipo de marketing enfocado en estrategia y revisión final.

### Importante

La IA genera borradores.  
El humano revisa, ajusta y aprueba.

Esto es clave porque la marca necesita mantener voz, contexto y precisión.

### Indicador recomendado

- Número de publicaciones producidas por semana.
- Tiempo ahorrado por publicación.
- Interacción generada.
- Cantidad de publicaciones aprobadas sin cambios mayores.

---

## Ejemplo 3: Calificación automática de leads

### Contexto

Una startup recibe contactos desde un formulario web, una campaña publicitaria o una referencia.

El problema es que no todos los leads están listos para comprar. Algunos solo quieren información. Otros tienen urgencia, presupuesto y necesidad clara.

Si el equipo intenta atender todos por igual, pierde tiempo o responde tarde a los mejores prospectos.

### Objetivo

Clasificar automáticamente cada lead según su potencial de compra.

### Flujo automatizado

```text
Nuevo lead completa un formulario
        ↓
La información llega a N8N
        ↓
La IA analiza mensaje, necesidad, país y presupuesto
        ↓
Asigna una categoría: frío, tibio o caliente
        ↓
Guarda el resultado en Google Sheets o CRM
        ↓
Si es caliente, envía alerta inmediata al equipo de ventas
```

### Herramientas sugeridas

- Google Forms, Typeform, Fillout o formulario web
- N8N
- Google Sheets, Airtable o CRM
- OpenAI u otro modelo de IA
- Slack, WhatsApp o Gmail para alertas

### Criterios de calificación

La IA puede usar reglas como estas:

| Señal | Interpretación |
|---|---|
| Pregunta solo precio sin contexto | Probablemente lead frío o tibio |
| Tiene problema claro y presupuesto | Lead más caliente |
| Quiere contratar esta semana | Lead caliente |
| No responde datos clave | Lead tibio o por calificar |
| Proyecto incompatible con el servicio | Lead descartado o de baja prioridad |

### Ejemplo de prompt para la IA

```text
Eres un clasificador de leads para una startup. Analiza los datos del prospecto y devuelve una clasificación. Usa únicamente esta información: nombre, país, mensaje, presupuesto y urgencia. Devuelve solo un JSON válido con los campos: puntaje de 0 a 100, categoría entre frío, tibio o caliente, razón breve y próxima acción recomendada. No inventes información.
```

### Ejemplo de respuesta esperada de la IA

```json
{
  "puntaje": 82,
  "categoria": "caliente",
  "razon": "El lead tiene una necesidad específica, muestra urgencia y menciona presupuesto disponible.",
  "proxima_accion": "Contactar hoy mismo por WhatsApp o llamada."
}
```

### Beneficio esperado

- Respuesta más rápida a leads importantes.
- Menos tiempo perdido en prospectos poco calificados.
- Mejor organización del embudo de ventas.
- Mayor probabilidad de conversión.

### Indicador recomendado

- Tiempo entre llegada del lead y primera respuesta.
- Porcentaje de leads clasificados como calientes.
- Tasa de conversión por categoría.
- Exactitud de la clasificación comparada con revisión humana.

---

## 4. Ejercicio práctico paso a paso

## **Construye tu primer flujo: calificador automático de leads**

En este ejercicio crearás una automatización simple para recibir leads, analizarlos con IA y guardar la clasificación en una hoja de cálculo.

> Este ejercicio está pensado para emprendedores no técnicos.  
> Si no tienes experiencia con N8N, puedes hacer primero la versión manual y luego pasar a la automatización visual.

---

### Objetivo del ejercicio

Crear un flujo que haga lo siguiente:

1. Recibir un nuevo lead en Google Sheets.
2. Analizar el mensaje del lead con IA.
3. Clasificarlo como frío, tibio o caliente.
4. Guardar la clasificación en otra hoja.
5. Opcional: alertar si el lead es caliente.

---

### Duración estimada

- Versión manual: 25 minutos.
- Versión con N8N: 60 a 90 minutos.
- Versión mejorada con notificación: 2 horas.

---

### Requisito previo

Necesitas:

- Una cuenta de Google.
- Google Sheets abierto.
- Una cuenta en N8N Cloud o acceso a una instancia de N8N.
- Opcional: una API key de OpenAI, Gemini u otro proveedor de IA.
- Opcional: cuenta en Make o Zapier si no quieres usar N8N.

Si no tienes acceso a una API de IA, puedes hacer la versión manual usando ChatGPT o Gemini directamente.

---

# Versión A: Ejercicio rápido sin N8N  
## “Calificación de leads con IA manual”

Esta versión es ideal si todavía no quieres configurar herramientas.

### Paso 1: Crea tu hoja de leads

Abre Google Sheets y crea una pestaña llamada:

```text
Leads_Entrada
```

Con estas columnas:

| ID | Fecha | Nombre | Email | País | Mensaje | Presupuesto | Categoría | Próxima acción |
|---|---|---|---|---|---|---|---|---|

Ejemplo de fila:

| ID | Fecha | Nombre | Email | País | Mensaje | Presupuesto | Categoría | Próxima acción |
|---|---|---|---|---|---|---|---|---|
| 001 | 12/03 | Laura | laura@mail.com | Colombia | Necesito automatizar reservas para mi clínica | USD 300 | | |

---

### Paso 2: Copia este prompt

```text
Eres un clasificador de leads para una startup. Analiza el siguiente lead y devuelve solo un JSON válido con los campos:
- puntaje: número de 0 a 100
- categoria: frío, tibio o caliente
- razon: explicación breve
- proxima_accion: acción recomendada

Datos del lead:
Nombre: [NOMBRE]
País: [PAÍS]
Mensaje: [MENSAJE]
Presupuesto: [PRESUPUESTO]

Reglas:
- Si tiene necesidad clara, urgencia y presupuesto, tiende a caliente.
- Si solo pide información general, tiende a tibio.
- Si no hay datos suficientes o no parece objetivo de compra, tiende a frío.
- No inventes información.
```

---

### Paso 3: Reemplaza los campos

Ejemplo:

```text
Nombre: Laura
País: Colombia
Mensaje: Necesito automatizar reservas para mi clínica
Presupuesto: USD 300
```

---

### Paso 4: Pega el prompt en ChatGPT, Gemini o tu IA preferida

La IA debería devolver algo como:

```json
{
  "puntaje": 85,
  "categoria": "caliente",
  "razon": "Existe una necesidad clara de automatización, contexto específico y presupuesto mencionado.",
  "proxima_accion": "Contactar hoy para agendar llamada de diagnóstico."
}
```

---

### Paso 5: Registra el resultado en la hoja

Completa las columnas:

| Categoría | Próxima acción |
|---|---|
| Caliente | Contactar hoy para agendar llamada |

---

### Paso 6: Repite con 5 leads reales o ficticios

Tu tarea es clasificar al menos cinco leads y responder:

- ¿Cuántos fueron fríos?
- ¿Cuántos tibios?
- ¿Cuántos calientes?
- ¿La IA necesitó reglas más claras?
- ¿Qué dato adicional mejoraría la clasificación?

---

# Versión B: Ejercicio con N8N  
## “Flujo automático con Google Sheets + IA”

Esta es la versión recomendada del módulo.

---

## Paso 1: Define el proceso que vas a automatizar

Antes de abrir N8N, escribe en una nota:

```text
Cuando llegue un nuevo lead en Google Sheets, quiero que la IA lo clasifique como frío, tibio o caliente, y luego guarde la clasificación en otra hoja.
```

Este será tu flujo mínimo viable.

---

## Paso 2: Prepara tu hoja de entrada

Crea un archivo en Google Sheets llamado:

```text
CRM Leads Startup
```

Dentro, crea una pestaña llamada:

```text
Leads_Entrada
```

Columnas sugeridas:

| ID | Fecha | Nombre | Email | País | Mensaje | Presupuesto | Estado |
|---|---|---|---|---|---|---|---|

Ejemplo:

| ID | Fecha | Nombre | Email | País | Mensaje | Presupuesto | Estado |
|---|---|---|---|---|---|---|---|
| 001 | 12/03 | Laura | laura@mail.com | Colombia | Necesito automatizar reservas para mi clínica | USD 300 | Nuevo |

Importante: la columna **ID** te ayudará a identificar cada lead.

---

## Paso 3: Prepara tu hoja de salida

En el mismo archivo, crea otra pestaña llamada:

```text
Leads_Clasificados
```

Columnas:

| ID | Nombre | País | Presupuesto | Puntaje_IA | Categoría_IA | Razón_IA | Próxima_Acción_IA |
|---|---|---|---|---|---|---|---|

Aquí guardarás el resultado de la automatización.

---

## Paso 4: Entra a N8N

Opciones:

- Usar N8N Cloud si tienes cuenta o período de prueba.
- Usar una instalación de N8N proporcionada por tu equipo técnico.
- Usar una alternativa como Make o Zapier si no tienes acceso a N8N.

Una vez dentro, crea un nuevo flujo de trabajo.

En N8N normalmente se llama:

```text
Create Workflow
```

o

```text
Nuevo flujo de trabajo
```

---

## Paso 5: Agrega el disparador de Google Sheets

Busca el nodo de Google Sheets.

Elige una opción similar a:

```text
When a row is added
```

o

```text
On row added
```

Es decir: “cuando se agrega una nueva fila”。

Conecta tu cuenta de Google si N8N te lo pide.

Luego selecciona:

- Archivo de Google Sheets.
- Pestaña: `Leads_Entrada`.

Prueba el nodo para verificar que pueda leer las filas.

---

## Paso 6: Agrega un nodo de IA

Busca el nodo de IA disponible en tu N8N.

Puede llamarse:

- OpenAI
- AI Agent
- Language Model
- Text Classifier
- HTTP Request, si usas la API manualmente

La idea es que este nodo reciba los datos del lead y los analice.

Usa un prompt como este:

```text
Eres un clasificador de leads para una startup. Analiza el siguiente lead y devuelve solo un JSON válido con los campos:
- puntaje: número de 0 a 100
- categoria: frío, tibio o caliente
- razon: explicación breve
- proxima_accion: acción recomendada

Datos del lead:
Nombre: {{ $json.Nombre }}
País: {{ $json.País }}
Mensaje: {{ $json.Mensaje }}
Presupuesto: {{ $json.Presupuesto }}

Reglas:
- Si tiene necesidad clara, urgencia y presupuesto, tiende a caliente.
- Si solo pide información general, tiende a tibio.
- Si no hay datos suficientes o no parece objetivo de compra, tiende a frío.
- No inventes información.
```

En N8N, las expresiones como `{{ $json.Nombre }}` permiten usar datos del paso anterior. Si tu versión muestra los campos de otra forma, selecciona cada campo desde el menú desplegable.

---

## Paso 7: Configura la respuesta de la IA

Pídele a la IA que devuelva algo estructurado.理想mente, JSON.

Ejemplo esperado:

```json
{
  "puntaje": 85,
  "categoria": "caliente",
  "razon": "Necesidad clara y presupuesto mencionado.",
  "proxima_accion": "Contactar hoy."
}
```

Si la IA devuelve texto normal, puedes usar un paso adicional para extraer campos, pero para tu primer flujo intenta que la respuesta sea simple y corta.

---

## Paso 8: Agrega el nodo de Google Sheets para guardar el resultado

Agrega otro nodo de Google Sheets.

Escoge una opción similar a:

```text
Append Row
```

o

```text
Add Row
```

Selecciona:

- Archivo: `CRM Leads Startup`
- Pestaña: `Leads_Clasificados`

Luego mapea los campos:

| Columna en Google Sheets | Dato que debes insertar |
|---|---|
| ID | ID del lead original |
| Nombre | Nombre |
| País | País |
| Presupuesto | Presupuesto |
| Puntaje_IA | Puntaje devuelto por la IA |
| Categoría_IA | Categoría devuelta por la IA |
| Razón_IA | Razón devuelta por la IA |
| Próxima_Acción_IA | Próxima acción recomendada |

---

## Paso 9: Prueba el flujo

Agrega una fila nueva manualmente en `Leads_Entrada`.

Ejemplo:

| ID | Fecha | Nombre | Email | País | Mensaje | Presupuesto | Estado |
|---|---|---|---|---|---|---|---|
| 002 | 12/03 | Carlos | carlos@mail.com | México | Quiero información sobre sus servicios, aún no tengo presupuesto | No indicado | Nuevo |

Luego ejecuta el flujo en N8N.

Deberías ver algo como:

```text
ID: 002
Nombre: Carlos
País: México
Presupuesto: No indicado
Puntaje_IA: 40
Categoría_IA: frío
Razón_IA: No indica presupuesto ni urgencia clara.
Próxima_Acción_IA: Enviar correo educativo y volver a contactar en 7 días.
```

Revisa la pestaña `Leads_Clasificados`.  
Si aparece la fila con los datos, tu automatización funciona.

---

## Paso 10: Activa el flujo

Cuando la prueba funcione, activa el flujo para que se ejecute automáticamente.

En N8N suele haber una opción como:

```text
Inactive / Active
```

o

```text
Activate Workflow
```

A partir de ahí, cada nueva fila puede disparar la clasificación automática.

---

## Paso 11: Agrega una condición opcional

Ahora puedes mejorar el flujo con una regla simple:

```text
Si la categoría es caliente, enviar alerta.
Si no es caliente, no hacer nada extra.
```

Agrega un nodo de condición, a veces llamado:

```text
IF
```

Configura la condición:

```text
Categoría_IA = caliente
```

Si se cumple, puedes conectar un nodo que envíe:

- Correo electrónico.
- Mensaje a Slack.
- Mensaje a Telegram.
- Notificación a WhatsApp.

Ejemplo de alerta:

```text
Nuevo lead caliente:
Nombre: {{ Nombre }}
País: {{ País }}
Presupuesto: {{ Presupuesto }}
Acción recomendada: {{ Próxima_Acción_IA }}
```

---

## Paso 12: Mejora el flujo con revisión humana

Para evitar errores, agrega una columna llamada:

```text
Revisado_Humano
```

Con opciones:

- Sí
- No

El flujo de trabajo recomendado para tu startup sería:

```text
IA clasifica
Humano revisa
Ventas actúa
```

La IA recomienda.  
El equipo decide.

---

## Paso 13: Documenta tu automatización

Crea una nota simple en Notion, Google Docs o tu gestor de tareas:

```text
Nombre del flujo:
Clasificador de leads con IA

Disparador:
Nueva fila en Leads_Entrada

Pasos:
1. N8N detecta nueva fila.
2. IA clasifica el lead.
3. Resultado se guarda en Leads_Clasificados.
4. Si es caliente, se envía alerta.

Responsable humano:
Fundador/a o líder de ventas

Frecuencia de revisión:
Diaria durante la primera semana

Métricas:
Número de leads clasificados, leads calientes, tiempo de respuesta.
```

---

## Paso 14: Tarea final del módulo

Construye una versión funcional de tu flujo y completa esta tabla:

| Pregunta | Respuesta del emprendedor |
|---|---|
| ¿Qué proceso automaticé? | |
| ¿Qué herramienta usé? | |
| ¿Qué disparador inicia el flujo? | |
| ¿Qué acción realiza la IA? | |
| ¿Qué acción sigue siendo humana? | |
| ¿Cuánto tiempo estimo que ahorraré por semana? | |
| ¿Qué mejora le haría después? | |

---

## Alternativa si no usas N8N

Si el ejercicio con N8N te parece avanzado, puedes usar esta versión simple en Make o Zapier:

```text
Nuevo lead en Google Sheets
        ↓
OpenAI o ChatGPT clasifica
        ↓
Se guarda resultado en otra hoja de Google Sheets
```

En Make:

1. Crea una cuenta gratuita.
2. Agrega el módulo de Google Sheets: “Watch Rows”.
3. Agrega un módulo de OpenAI o herramienta de IA disponible.
4. Agrega otro módulo de Google Sheets: “Add Row”.
5. Prueba y activa.

En Zapier:

1. Crea un Zap.
2. Trigger: Google Sheets, “New Spreadsheet Row”.
3. Acción: OpenAI o ChatGPT, “Send Prompt” o similar.
4. Acción: Google Sheets, “Create Spreadsheet Row”.
5. Prueba y publica.

La lógica es la misma: disparador, IA, acción final.

---

## 5. Recursos adicionales

### Herramientas principales

| Recurso | Para qué sirve |
|---|---|
| N8N | Crear automatizaciones visuales con nodos |
| Make | Automatizar procesos sin código |
| Zapier | Conectar apps populares con automatizaciones simples |
| Google Sheets | Base de datos simple para empezar |
| Airtable | Base de datos visual más flexible |
| Notion | Documentar procesos y aprobar contenido |
| HubSpot CRM | Gestionar leads y oportunidades |
| Brevo | Enviar correos automáticos |
| Mailchimp | Email marketing simple |
| Metricool | Programar publicaciones en redes sociales |
| Buffer | Programar contenido |
| WhatsApp Business | Comunicación con clientes en Latinoamérica |

---

### Recursos de aprendizaje recomendados

1. **Documentación oficial de N8N**  
   Busca guías sobre:
   - Google Sheets node
   - Trigger nodes
   - AI nodes
   - Workflow templates

2. **Plantillas de automatización**  
   Busca plantillas con términos como:
   - “AI lead qualification”
   - “ChatGPT Google Sheets”
   - “Customer support automation”
   - “Social media content workflow”

3. **Guía práctica de prompts para startups**  
   Crea tu propio documento con prompts útiles para:
   - Calificar leads.
   - Responder clientes.
   - Crear contenido.
   - Redactar correos de seguimiento.
   - Resumir conversaciones.

4. **Base de conocimiento para atención al cliente**  
   Prepara un documento con:
   - Preguntas frecuentes.
   - Respuestas oficiales.
   - Precios.
   - Políticas.
   - Horarios.
   - Casos que deben pasarse a humano.

5. **Mini CRM en Google Sheets**  
   Columnas recomendadas:
   - ID
   - Nombre
   - Email
   - WhatsApp
   - País
   - Fuente
   - Mensaje
   - Categoría
   - Próxima acción
   - Responsable
   - Fecha de seguimiento
   - Estado

---

## Plantilla bonus: prompt para calificar leads

Puedes guardar este prompt y adaptarlo a tu negocio:

```text
Eres un asistente de ventas para una startup latinoamericana. Tu objetivo es clasificar leads según su potencial de compra. Analiza los datos entregados y no inventes información.

Devuelve únicamente un JSON válido con estos campos:
- puntaje: número de 0 a 100
- categoria: frío, tibio o caliente
- razon: explicación breve
- proxima_accion: recomendación concreta

Criterios:
- Lead caliente: necesidad específica, urgencia clara, presupuesto disponible o intención explícita de contratar.
- Lead tibio: interés real pero faltan datos clave, presupuesto o urgencia.
- Lead frío: consulta genérica, sin intención clara de compra o incompatible con el servicio.

Datos del lead:
Nombre: [NOMBRE]
País: [PAÍS]
Mensaje: [MENSAJE]
Presupuesto: [PRESUPUESTO]
Urgencia: [URGENCIA]
```

---

## Plantilla bonus: prompt para atención al cliente

```text
Eres el asistente virtual de una startup. Responde con tono amable, breve y profesional. Usa solo la información oficial proporcionada. Si la pregunta no está en la base de conocimiento, indica que una persona del equipo responderá pronto. Si el cliente está molesto, muestra empatía y escala el caso a soporte humano. No inventes precios, plazos, promociones ni políticas.
```

---

## Plantilla bonus: prompt para contenido de redes

```text
Actúa como community manager de una marca latinoamericana. Crea una publicación para redes sociales a partir del tema indicado. Debe incluir: gancho inicial, texto corto, llamado a la acción y 5 hashtags. El tono debe ser cercano, útil y profesional. No uses promesas exageradas ni clichés muy genéricos.
```

---

## 6. Preguntas de autoevaluación

### Pregunta 1

¿Cuál es la diferencia principal entre una automatización tradicional y una automatización con IA?

**Respuesta esperada:**  
La automatización tradicional ejecuta tareas repetitivas cuando ocurre un evento, mientras que la automatización con IA además puede analizar, interpretar, clasificar o generar contenido a partir de información como mensajes, textos o datos.

---

### Pregunta 2

En un flujo de trabajo automatizado, ¿qué función cumple el disparador o trigger?

**Respuesta esperada:**  
El disparador es el evento que inicia el flujo de trabajo. Por ejemplo, una nueva fila en Google Sheets, un mensaje entrante de WhatsApp o un formulario recién completado.

---

### Pregunta 3

¿Por qué es importante mantener revisión humana en una automatización de atención al cliente o calificación de leads?

**Respuesta esperada:**  
Porque la IA puede equivocarse, malinterpretar contexto, no tener información suficiente o tomar decisiones inadecuadas en casos sensibles. La revisión humana ayuda a proteger la experiencia del cliente, corregir errores y mantener el criterio del negocio.