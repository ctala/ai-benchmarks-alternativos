# Qwen 3.8 Omni Flash — startup_content/curso_emprendimiento_modulo

- model_id: `qwen/qwen3.8-omni-flash`
- success: True  | final: 8.29 | quality: 9.72
- latency_total: 217.273s | tokens_per_second: 71.4
- input_tokens: 270 | output_tokens: 15513
- judge_score: 4.8 | justificación: 

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

# Módulo 3 — Automatización con IA: De la idea al flujo de trabajo

**Curso:** IA Práctica para Emprendedores  
**Nivel:** Emprendedor no técnico  
**Enfoque:** Hands-on, aplicable, con ejemplos reales para Latinoamérica  
**Duración sugerida:** 2 a 3 horas de estudio + práctica  

---

## 1. Objetivo del módulo

Al finalizar este módulo, podrás reconocer qué tareas repetitivas de tu startup son candidatas a automatizarse con inteligencia artificial, diseñar un flujo de trabajo simple usando herramientas visuales como n8n y poner en marcha una primera automatización con supervisión humana que te permita ahorrar tiempo, responder más rápido a clientes o leads, mejorar el seguimiento comercial y tomar mejores decisiones sin necesidad de programar.

---

## 2. Contenido teórico

### 2.1 ¿Qué es automatizar con IA?

Automatizar con IA significa conectar una secuencia de tareas para que un sistema haga parte del trabajo por ti, usando inteligencia artificial cuando se requiere entender lenguaje, clasificar información, generar textos, resumir datos o apoyar una decisión.

Piensa en una cafetería:

- **Automatización simple:** cuando alguien pide un café, la máquina lo prepara siguiendo instrucciones fijas.
- **Automatización con IA:** un asistente lee el pedido, entiende si el cliente quiere algo personalizado, sugiere una opción adicional y avisa al barista solo cuando hace falta criterio humano.

En una startup, la automatización con IA puede servir para:

- Leer mensajes de clientes y clasificarlos por tipo de solicitud.
- Responder preguntas frecuentes con base en tu información oficial.
- Calificar leads según presupuesto, urgencia ofit con tu cliente ideal.
- Generar borradores de contenido para redes sociales.
- Resumir correos, reuniones o formularios largos.
- Enviar avisos automáticos a tu equipo cuando algo importante sucede.

La clave no es “reemplazar personas”, sino **quitar trabajo repetitivo** para que tú y tu equipo se enfoquen en decisiones, venta, producto y relación con clientes.

---

### 2.2 ¿Qué puede hacer la IA dentro de un flujo de trabajo?

Dentro de una automatización, la IA normalmente cumple una de estas funciones:

| Función de la IA | Ejemplo práctico |
|---|---|
| Clasificar | Determinar si un mensaje es “venta”, “soporte”, “reclamo” o “spam”. |
| Extraer información | Sacar nombre, empresa, correo, presupuesto o urgencia desde un texto libre. |
| Resumir | Convertir una conversación larga en 3 puntos clave para el equipo comercial. |
| Generar texto | Redactar respuesta inicial, post para redes sociales o seguimiento por WhatsApp. |
| Apoyar decisión | Asignar una puntuación a un lead según criterios definidos por ti. |
| Traducir o adaptar tono | Convertir un mensaje técnico a lenguaje sencillo para clientes no técnicos. |

Importante: la IA no “sabe” tu negocio por sí sola. Necesita contexto, reglas y ejemplos. Por eso, tu rol como emprendedor es definir bien el problema, los criterios y los límites.

---

### 2.3 ¿Cuándo conviene automatizar y cuándo no?

No todo debe automatizarse. Para emprendimientos en etapa temprana, conviene empezar por procesos que cumplan varias de estas condiciones:

| Señal de que puedes automatizar | Ejemplo |
|---|---|
| Ocurre muchas veces por semana | Responder “¿cuánto cuesta?” o “¿hacen envíos?”. |
| Tiene pasos repetitivos | Copiar datos de un formulario a una hoja de cálculo. |
| La decisión es relativamente clara | Clasificar lead como caliente, tibio o frío. |
| El error tiene bajo costo | Un borrador de contenido que igual revisa un humano. |
| Ya está documentado | Sabes exactamente qué respuesta dar en cada caso. |

Evita automatizar primero:

- Procesos caóticos o mal definidos.
- Conversaciones sensibles con clientes enojados.
- Decisiones legales, médicas, financieras críticas sin supervisión humana.
- Temas donde la IA pueda inventar información y causar daño reputacional.

Regla práctica:

> Primero estandariza, luego semi-automatiza, después automatiza más.

---

### 2.4 Anatomía de un flujo de automatización

Un flujo de trabajo, también llamado workflow, se puede entender como una cadena de bloques. Cada bloque hace algo.

Ejemplo simple:

```text
Nuevo mensaje de cliente
        ↓
La IA clasifica la intención
        ↓
Si es pregunta frecuente → responder automáticamente
Si es reclamo → avisar a humano
        ↓
Guardar conversación en Google Sheets
```

Componentes comunes:

| Componente | Qué es | Ejemplo |
|---|---|---|
| Disparador o trigger | Evento que inicia el flujo | Nuevo formulario, nuevo correo, nuevo mensaje, pago recibido. |
| Entrada de datos | Información que entra al sistema | Nombre, correo, mensaje, presupuesto, empresa. |
| Nodo de IA | Bloque que procesa lenguaje o toma decisiones | Clasificar, resumir, generar respuesta. |
| Condición | Regla para dividir el camino | Si score > 70, avisar al vendedor. |
| Acción | Lo que hace el sistema | Enviar correo, guardar en hoja, crear tarea, mandar mensaje por Telegram. |
| Registro | Dónde queda la evidencia | Google Sheets, CRM, Notion, Airtable. |
| Supervisión humana | Revisión final cuando hace falta | Aprobar respuesta, llamar al cliente, corregir datos. |

En herramientas como n8n, estos componentes se llaman **nodos**. Tú los conectas visualmente, como piezas de Lego.

---

### 2.5 Herramientas: n8n y alternativas

#### n8n

n8n, también escrito N8N, es una plataforma de automatización de flujos de trabajo que permite conectar aplicaciones, bases de datos, APIs y modelos de IA mediante nodos visuales.

Es útil para emprendedores porque:

- Permite crear automatizaciones sin escribir código desde cero.
- Tiene integración con muchas herramientas comunes: Google Sheets, Gmail, Telegram, WhatsApp a través de proveedores, CRM, webhooks, IA, etc.
- Puede funcionar en la nube o autoalojado, aunque para empezar lo más simple es la versión cloud.
- Ofrece flexibilidad para crecer: empiezas con un flujo pequeño y luego agregas condiciones, bases de conocimiento, CRMs y notificaciones.

En n8n puedes hacer cosas como:

```text
Formulario de contacto → IA califica lead → guarda en Google Sheets → avisa por Telegram
```

o:

```text
Mensaje entrante → IA detecta intención → responde si es frecuente → escala a humano si es complejo
```

#### Alternativas según tu contexto

| Herramienta | Ideal para | Nivel técnico | Comentario |
|---|---|---|---|
| n8n | Emprendedores que quieren flexibilidad y control | Bajo/medio | Muy útil si planeas escalar automatizaciones. |
| Make | Flujos visuales rápidos | Bajo | Fácil de entender, bueno para principiantes. |
| Zapier | Conectar apps populares rápidamente | Bajo | Muy simple, pero puede volverse costoso a escala. |
| Power Automate | Empresas que usan Microsoft 365 | Medio | Bueno si ya usas Outlook, Teams, Excel, SharePoint. |
| Bardeen | Automatizaciones desde el navegador | Bajo | Útil para tareas web personales o pequeñas. |

Para este módulo usaremos n8n como referencia principal, porque combina automatización, IA y posibilidad de crecer sin depender solo de plantillas cerradas.

---

### 2.6 Principios para automatizar sin fallar

1. **Empieza pequeño**  
   No intentes automatizar toda tu operación de golpe. Elige una tarea de 10 a 30 minutos semanales.

2. **Mantén un humano en el loop**  
   Sobre todo al inicio. La IA puede proponer, pero una persona aprueba acciones sensibles.

3. **Define criterios claros**  
   Si pides calificar leads, debes saber qué es un lead caliente para tu negocio.

4. **Mide antes y después**  
   Tiempo de respuesta, leads atendidos, conversión, horas ahorradas, errores detectados.

5. **Cuida datos personales**  
   En Latinoamérica hay normas de protección de datos. No envíes información sensible innecesaria a la IA y pide consentimiento cuando aplique.

6. **Documenta el flujo**  
   Aunque sea simple, anota: disparador, entradas, reglas, salidas, responsable humano y métricas.

---

## 3. Tres ejemplos prácticos de automatización para startups

---

### 3.1 Ejemplo 1: Atención al cliente automatizada

**Contexto típico en LatAm:**  
Una startup de comercio electrónico, servicios locales o productos físicos recibe muchos mensajes por WhatsApp, Instagram o formulario web. La mayoría son preguntas repetidas: precios, envíos, tiempos de entrega, métodos de pago, devoluciones.

**Problema:**  
El fundador o el equipo responde manualmente durante horas, se retrasa en ventas importantes y pierde consistencia en las respuestas.

**Flujo propuesto:**

```text
Cliente envía mensaje
        ↓
n8n recibe el mensaje
        ↓
IA clasifica intención: precio, envío, pago, reclamo, otro
        ↓
Si es pregunta frecuente → responde con base en catálogo/FAQ
Si es caso complejo → crea tarea y avisa a humano
        ↓
Guarda conversación en Google Sheets o CRM
```

**Herramientas posibles:**

- n8n como motor del flujo.
- WhatsApp Business API, Twilio, Meta WhatsApp Cloud API o incluso un formulario web para empezar.
- OpenAI u otro modelo de IA para clasificar y redactar.
- Google Sheets, Notion o CRM para registro.
- Telegram, Slack o correo para avisos internos.

**Ejemplo real simplificado:**

Una tienda de productos sostenibles en Bogotá recibe 60 mensajes diarios. El 70% son preguntas sobre envíos y precios. Automatizan:

- Si el mensaje dice “cuánto cuesta” o “precio”, la IA responde con lista de productos.
- Si dice “dónde están” o “envío”, responde con zonas y tiempos.
- Si dice “quiero reclamar” o “llegó mal”, avisa inmediatamente al encargado.

**Resultado esperado:**

- Respuesta más rápida.
- Menos carga operativa.
- Mejor registro de consultas frecuentes.
- Posibilidad de detectar productos o dudas que necesitan mejora en la página web.

**Cuidados:**

- Siempre ofrecer opción de “hablar con una persona”.
- No prometer stock, precios o tiempos de envío si la base de datos no está actualizada.
- Revisar diariamente las conversaciones escaladas a humano.

---

### 3.2 Ejemplo 2: Generación de contenido para redes sociales

**Contexto típico:**  
Una startup necesita publicar constantemente en Instagram, LinkedIn, TikTok o Facebook, pero no tiene equipo grande de marketing. El fundador pierde horas pensando qué publicar.

**Problema:**  
Falta de consistencia, mensajes desordenados, poco tiempo para crear contenido y dificultad para mantener tono de marca.

**Flujo propuesto:**

```text
Todos los lunes a las 8:00 a.m.
        ↓
n8n lee promociones, productos o temas desde Google Sheets
        ↓
IA genera 5 ideas de contenido con copy, hashtags y llamada a la acción
        ↓
Envía borradores por Telegram o correo para aprobación
        ↓
Si el humano aprueba, programa publicación o guarda en carpeta de contenido
```

**Herramientas posibles:**

- n8n con trigger programado.
- Google Sheets como calendario editorial simple.
- OpenAI para generar copys.
- Telegram o Gmail para aprobación humana.
- Metricool, Buffer, Later o similar para programar publicaciones.
- Canva o IA de imagen si deseas acompañar con diseño.

**Ejemplo real simplificado:**

Una startup de software contable para pymes en Ciudad de México quiere publicar en LinkedIn. Cada semana alimenta una hoja con:

- Tema: facturación electrónica.
- Beneficio: ahorrar tiempo.
- Prueba social: cliente que redujo errores.
- Oferta: demo gratuita.

La IA genera:

- Un post educativo.
- Un post con historia de cliente.
- Un post con error común.
- Un carrusel con 5 consejos.
- Un mensaje corto para Stories.

El fundador revisa, corrige tono y aprueba.

**Resultado esperado:**

- Ahorro de 3 a 6 horas semanales.
- Mayor consistencia editorial.
- Mejores pruebas de mensajes comerciales.
- Banco de contenido reutilizable.

**Cuidados:**

- La IA puede inventar datos. Nunca publicar cifras, promesas o casos sin verificar.
- Mantener voz de marca: define ejemplos de cómo sí y cómo no habla tu startup.
- Humanizar el contenido: agregar experiencia real, opinión y contexto local.

---

### 3.3 Ejemplo 3: Calificación automática de leads

**Contexto típico:**  
Una startup B2B o de servicios recibe leads desde formularios, anuncios, ferias, WhatsApp o página web. No todos los leads están listos para comprar.

**Problema:**  
El equipo comercial pierde tiempo llamando a curiosos, mientras leads calientes esperan demasiado.

**Flujo propuesto:**

```text
Nuevo lead llega por formulario o anuncio
        ↓
n8n captura datos
        ↓
IA analiza: empresa, necesidad, presupuesto, urgencia, cargo
        ↓
Asigna score de 0 a 100 y segmento: caliente, tibio, frío, revisar
        ↓
Si es caliente → avisa al vendedor y sugiere mensaje de seguimiento
Si es tibio → entra a secuencia de nutrición
Si es frío → archiva o envía contenido educativo
        ↓
Guarda todo en CRM o Google Sheets
```

**Herramientas posibles:**

- n8n.
- Typeform, Google Forms, webhooks de Meta Ads, WhatsApp o formulario propio.
- OpenAI para análisis y scoring.
- Google Sheets, HubSpot, Pipedrive, Zoho CRM o Airtable.
- Gmail, WhatsApp, Telegram o Slack para alertas.

**Criterios ejemplo de scoring:**

| Criterio | Puntos |
|---|---:|
| Coincidencia con cliente ideal | 0–30 |
| Urgencia declarada | 0–25 |
| Presupuesto estimado | 0–20 |
| Datos de contacto completos | 0–15 |
| Cargo decisor o influenciador | 0–10 |
| **Total** | **0–100** |

Interpretación:

| Score | Segmento | Acción |
|---:|---|---|
| 80–100 | Caliente | Llamar o escribir en menos de 15 minutos. |
| 60–79 | Tibio | Enviar propuesta o agendar llamada de descubrimiento. |
| 40–59 | Frío/educativo | Entrar a secuencia de contenido. |
| 0–39 o datos incompletos | Revisar | Pedir información adicional con mensaje suave. |

**Ejemplo real simplificado:**

Una fintech peruana que ofrece facturación electrónica recibe leads desde Facebook Ads. Automatizan:

- Si el lead dice “necesito emitir facturas este mes” y tiene RUC/company data, score alto.
- Si dice “solo estoy investigando”, score medio-bajo.
- Si no deja teléfono, va a “revisar”.

Los leads calientes reciben WhatsApp automático con agendamiento de demo. Los tibios entran a email nurturing.

**Resultado esperado:**

- Priorización comercial más objetiva.
- Menos tiempo perdido en leads fríos.
- Mayor velocidad de contacto.
- Mejor tasa de conversión.

**Cuidados:**

- No usar variables discriminatorias como género, edad, ubicación sensible, nacionalidad, etc.
- Validar que la IA no infiera datos que no fueron proporcionados.
- Mantener revisión humana en casos límite.

---

## 4. Ejercicio práctico paso a paso

# Tu primer flujo: calificador de leads con IA en n8n

En este ejercicio crearás un automatización sencilla que:

1. Recibe datos de un lead desde un formulario.
2. Usa IA para analizarlo y asignarle una calificación.
3. Guarda la información en Google Sheets.
4. Te envía una alerta por Telegram para actuar rápido.

Este flujo es semi-automático: la IA trabaja, pero tú revisas y decides. Es ideal para empezar sin riesgos.

---

### Antes de empezar

Necesitarás:

- Una cuenta en n8n Cloud o una instancia de n8n disponible.
- Una cuenta de Google para usar Google Sheets.
- Acceso a un nodo de IA, por ejemplo OpenAI.
- Una cuenta de Telegram, opcional pero recomendada para alertas.
- 30 a 45 minutos.

Si no tienes Telegram, puedes sustituir la alerta por Gmail o simplemente revisar Google Sheets.

---

## Paso 1: Define tu cliente ideal y tus criterios

Antes de abrir n8n, responde en una libreta o documento:

| Pregunta | Tu respuesta |
|---|---|
| ¿Quién es mi cliente ideal? |  |
| ¿Qué problema resuelvo? |  |
| ¿Qué presupuesto mínimo suele tener? |  |
| ¿Qué nivel de urgencia es valioso? |  |
| ¿Qué datos necesito para calificar? | nombre, empresa, correo, teléfono, necesidad, presupuesto, urgencia |
| ¿Qué haría yo con un lead caliente? | llamar, enviar WhatsApp, agendar demo, mandar propuesta |

Ejemplo para una startup de automatización para pymes:

- Cliente ideal: dueños o gerentes de empresas con 5 a 50 empleados.
- Problema: pierden tiempo en tareas manuales.
- Presupuesto interesante: desde USD 300/mes o equivalente local.
- Urgencia alta: quieren implementar en menos de 30 días.
- Lead caliente: tiene empresa, presupuesto, urgencia y contacto completo.

---

## Paso 2: Crea un nuevo workflow en n8n

1. Entra a tu cuenta de n8n.
2. Haz clic en **Create Workflow** o **Crear flujo de trabajo**.
3. Ponle un nombre claro, por ejemplo:

```text
Calificador de leads con IA
```

4. Vas a construir este flujo:

```text
Formulario → IA Calificadora → Guardar en Google Sheets → Aviso Telegram
```

---

## Paso 3: Agrega el disparador: Form Trigger

El trigger será un formulario simple para capturar leads.

1. Haz clic en **Add First Step** o **Agregar primer paso**.
2. Busca el nodo **Form**.
3. Selecciona **On form submission**.
4. Renombra el nodo como:

```text
Formulario
```

5. Configura los campos del formulario. Puedes usar estos:

| Campo | Tipo |
|---|---|
| nombre | Short Text |
| empresa | Short Text |
| correo | Email |
| telefono | Phone |
| necesidad | Textarea |
| presupuesto | Dropdown |
| urgencia | Dropdown |

Para presupuesto, usa opciones como:

```text
No definido
Menos de 500
500 a 2000
Más de 2000
```

Para urgencia:

```text
Este mes
De 1 a 3 meses
Solo investigando
```

Importante: adapta montos a tu moneda local, por ejemplo MXN, COP, PEN, ARS, CLP, etc.

6. Guarda el formulario.
7. Copia la URL del formulario.
8. Ábrela en otra pestaña y haz una prueba con un lead ficticio.

Ejemplo de prueba:

```text
Nombre: Laura Méndez
Empresa: Dulces Andinos
Correo: laura@dulcesandinos.com
Teléfono: +51 987 654 321
Necesidad: Quiero automatizar pedidos por WhatsApp
Presupuesto: 500 a 2000
Urgencia: Este mes
```

---

## Paso 4: Agrega el nodo de IA

Ahora harás que la IA analice el lead.

1. Después del nodo **Formulario**, haz clic en **Plus** para agregar un nuevo nodo.
2. Busca el nodo de IA que tengas disponible, por ejemplo **OpenAI**.
3. Renómbralo como:

```text
IA Calificadora
```

4. Configura un modelo económico y suficiente, por ejemplo:

```text
gpt-4o-mini
```

o el equivalente disponible en tu cuenta.

5. En el mensaje o prompt, pega la siguiente instrucción. Luego ajusta los campos usando el selector de datos de n8n si es necesario.

```text
Eres un calificador comercial para una startup latinoamericana. Analiza el siguiente lead y responde SOLO con este formato:

SCORE: [número entre 0 y 100]
SEGMENTO: [caliente | tibio | frío | revisar]
RAZÓN: [máximo 2 frases]
MENSAJE_SUGERIDO: [mensaje cálido para WhatsApp o email, máximo 280 caracteres]
SIGUIENTE_ACCIÓN: [llamar | enviar propuesta | agendar demo | nutrir por email | pedir datos]

Datos del lead:
Nombre: {{ $('Formulario').item.json.nombre }}
Empresa: {{ $('Formulario').item.json.empresa }}
Correo: {{ $('Formulario').item.json.correo }}
Teléfono: {{ $('Formulario').item.json.telefono }}
Necesidad: {{ $('Formulario').item.json.necesidad }}
Presupuesto: {{ $('Formulario').item.json.presupuesto }}
Urgencia: {{ $('Formulario').item.json.urgencia }}

Criterios de calificación:
- 30 puntos: coincide con cliente ideal si tiene empresa clara y necesidad relacionada con automatización, eficiencia, ventas u operaciones.
- 25 puntos: urgencia. Este mes = 25, de 1 a 3 meses = 15, solo investigando = 5.
- 20 puntos: presupuesto. Más de 2000 = 20, 500 a 2000 = 12, menos de 500 = 5, no definido = 0.
- 15 puntos: datos de contacto completos: correo y teléfono válidos.
- 10 puntos: necesidad específica y accionable.

Reglas:
- No inventes información.
- Si faltan datos clave, usa segmento "revisar".
- Sé directo, ético y comercial, pero no exageres.
- El mensaje sugerido debe sonar humano, cercano y adequado a Latinoamérica.
- No uses promesas falsas ni garantías imposibles.
```

6. Si tu nodo de IA permite temperatura, ponla baja, por ejemplo:

```text
0.2
```

Esto hace la respuesta más consistente.

7. Haz clic en **Execute Workflow** o **Ejecutar flujo** para probar.

Deberías ver una respuesta parecida a:

```text
SCORE: 82
SEGMENTO: caliente
RAZÓN: La empresa tiene necesidad clara, urgencia alta y presupuesto intermedio. Cuenta con datos de contacto completos.
MENSAJE_SUGERIDO: Hola Laura, vi que buscan automatizar pedidos por WhatsApp en Dulces Andinos. Puedo mostrarles un ejemplo similar en 15 minutos. ¿Te va bien hoy o mañana?
SIGUIENTE_ACCIÓN: agendar demo
```

Si la respuesta no respeta el formato, repite el prompt y enfatiza:

```text
Responde exactamente con esas cinco líneas. No agregues introducciones ni explicaciones adicionales.
```

---

## Paso 5: Crea la hoja de Google Sheets

Antes de conectar n8n, prepara una hoja donde guardarás los leads.

1. Abre Google Sheets.
2. Crea una hoja nueva llamada:

```text
Leads IA
```

3. En la primera fila, escribe estos encabezados:

| Columna | Encabezado |
|---|---|
| A | fecha |
| B | nombre |
| C | empresa |
| D | correo |
| E | telefono |
| F | necesidad |
| G | presupuesto |
| H | urgencia |
| I | score |
| J | segmento |
| K | razon |
| L | mensaje_sugerido |
| M | siguiente_accion |
| N | respuesta_ia_completa |

Puedes simplificar si quieres, pero esta estructura te servirá para medir resultados.

---

## Paso 6: Agrega el nodo Google Sheets

1. Después de **IA Calificadora**, agrega un nuevo nodo.
2. Busca **Google Sheets**.
3. Renómbralo como:

```text
Guardar en Hoja
```

4. Conecta tu cuenta de Google cuando te lo pida.
5. Selecciona la operación:

```text
Append Row
```

o **Añadir fila**.

6. Elige el documento y la hoja:

```text
Leads IA
```

7. Mapea los campos.

Para datos originales del formulario, usa expresiones desde el nodo **Formulario**, por ejemplo:

```text
{{ $('Formulario').item.json.nombre }}
{{ $('Formulario').item.json.empresa }}
{{ $('Formulario').item.json.correo }}
{{ $('Formulario').item.json.telefono }}
{{ $('Formulario').item.json.necesidad }}
{{ $('Formulario').item.json.presupuesto }}
{{ $('Formulario').item.json.urgencia }}
```

Para la respuesta de la IA, depende de cómo tu nodo devuelva el dato. Normalmente verás un campo como:

```text
message
```

o

```text
text
```

Selecciona desde el panel derecho de n8n el campo que contiene la respuesta completa de la IA y ponlo en:

```text
respuesta_ia_completa
```

Si quieres extraer score, segmento, razón, mensaje y siguiente acción automáticamente, puedes hacerlo después con un nodo Code o con herramientas más avanzadas. Para este primer ejercicio, basta con guardar la respuesta completa y leerla manualmente.

8. Ejecuta el nodo para verificar que se agregue una fila en Google Sheets.

---

## Paso 7: Agrega la alerta por Telegram

Telegram es útil porque muchos equipos en Latinoamérica lo usan para operaciones rápidas.

### 7.1 Crea un bot en Telegram

1. Abre Telegram y busca:

```text
@BotFather
```

2. Envía el comando:

```text
/newbot
```

3. Elige un nombre, por ejemplo:

```text
Alertas Leads Startup
```

4. Elige un username terminado en bot, por ejemplo:

```text
mi_startup_leads_bot
```

5. Copia el token que te da BotFather. Se ve parecido a:

```text
123456789:AAExemploDeTokenSecreto
```

### 7.2 Obtén tu chat ID

1. Abre Telegram y busca:

```text
@userinfobot
```

2. Inicia conversación.
3. Copia tu ID numérico.

Ese ID será tu chat ID para recibir mensajes de tu bot, siempre que le hayas enviado un mensaje antes.

Importante: envíale cualquier mensaje a tu bot recién creado, por ejemplo “hola”, para que pueda escribirte.

### 7.3 Configura el nodo Telegram en n8n

1. Después de **Guardar en Hoja**, agrega un nodo **Telegram**.
2. Renómbralo como:

```text
Aviso Telegram
```

3. Crea una credencial con el token de tu bot.
4. Selecciona la operación:

```text
Send Message
```

5. En **Chat ID**, pega tu ID numérico.
6. En el mensaje, usa algo como:

```text
🔥 Nuevo lead calificado

Nombre: {{ $('Formulario').item.json.nombre }}
Empresa: {{ $('Formulario').item.json.empresa }}
Teléfono: {{ $('Formulario').item.json.telefono }}

Análisis IA:
{{ $('IA Calificadora').item.json.message }}
```

Si el campo no se llama `message`, selecciónalo desde el panel de datos de n8n.

7. Ejecuta el flujo completo.

Deberías recibir un mensaje en Telegram con el lead y el análisis de la IA.

---

## Paso 8: Activa el workflow

1. Revisa que los nodos estén conectados en este orden:

```text
Formulario → IA Calificadora → Guardar en Hoja → Aviso Telegram
```

2. Haz clic en **Activate** o **Activar**.
3. Comparte la URL del formulario con un colega o úsala tú mismo con datos de prueba.
4. Verifica tres cosas:

- ¿Llegó el lead a Google Sheets?
- ¿La IA dio una calificación útil?
- ¿Recibiste la alerta en Telegram?

---

## Paso 9: Haz una prueba con 3 leads distintos

Usa estos perfiles para ver cómo responde la IA:

### Lead 1: caliente

```text
Nombre: Carlos Rojas
Empresa: Taller Mecánico Rojas
Correo: carlos@tallerrojas.com
Teléfono: +52 55 1234 5678
Necesidad: Necesito agendar citas por WhatsApp y reducir ausencias
Presupuesto: 500 a 2000
Urgencia: Este mes
```

### Lead 2: tibio

```text
Nombre: Ana Torres
Empresa: Boutique Alma
Correo: ana@boutiquealma.com
Teléfono: +57 300 111 2233
Necesidad: Quiero organizar pedidos de Instagram
Presupuesto: Menos de 500
Urgencia: De 1 a 3 meses
```

### Lead 3: revisar

```text
Nombre: Luis
Empresa: 
Correo: 
Teléfono: 
Necesidad: Info
Presupuesto: No definido
Urgencia: Solo investigando
```

Observa si la IA distingue correctamente. Si no lo hace, ajusta los criterios del prompt.

---

## Paso 10: Itera y mejora tu flujo

Cuando ya funcione, puedes evolucionarlo:

| Mejora | Cómo ayuda |
|---|---|
| Agregar nodo IF | Separar leads calientes de tibios. |
| Enviar solo alertas de leads calientes | Evitar ruido. |
| Conectar CRM | Dar seguimiento comercial formal. |
| Agregar base de conocimiento | Mejorar respuestas de atención al cliente. |
| Programar resumen diario | Recibir cada noche los leads del día. |
| Medir conversión | Saber si el scoring realmente funciona. |

Ejemplo de condición simple:

```text
Si la respuesta de IA contiene "SEGMENTO: caliente" → enviar alerta prioritaria
Si contiene "tibio" → enviar alerta normal
Si contiene "revisar" → no alertar inmediatamente, solo guardar
```

---

## Solución de problemas comunes

| Problema | Posible causa | Solución |
|---|---|---|
| El formulario no envía datos | Workflow inactivo o URL incorrecta | Usa la URL de prueba dentro del editor o activa el workflow. |
| La IA da respuestas desordenadas | Prompt muy abierto | Exige formato exacto y baja temperatura. |
| Error de credencial en OpenAI | API key inválida o sin créditos | Revisa clave, facturación y modelo disponible. |
| Google Sheets no guarda | permisos insuficientes o hoja equivocada | Reconecta credencial y verifica documento/hoja. |
| Telegram no envía mensaje | Bot no recibió mensaje previo o chat ID incorrecto | Escríbele al bot y confirma tu ID. |
| Campos vacíos en Sheets | Expresiones mal referenciadas | Usa el selector de datos de n8n en vez de escribir a mano. |
| La IA inventa datos | Prompt sin restricciones | Agrega: “No inventes información. Si falta dato, marca revisar.” |

---

## 5. Recursos adicionales

### Documentación y aprendizaje de n8n

- Documentación oficial de n8n: `docs.n8n.io`
- Plantillas de workflows: sección Templates de n8n.
- Comunidad y foro: útil para buscar errores específicos.
- Búsquedas recomendadas:
  - “n8n form trigger tutorial”
  - “n8n OpenAI workflow”
  - “n8n Google Sheets append row”
  - “n8n Telegram send message”
  - “n8n lead scoring automation”

### Herramientas complementarias

| Necesidad | Herramientas sugeridas |
|---|---|
| Formularios | n8n Form, Google Forms, Typeform, Tally. |
| Base de datos simple | Google Sheets, Airtable, Notion. |
| CRM ligero | HubSpot Free, Pipedrive, Zoho CRM, Notion CRM. |
| Mensajería interna | Telegram, Slack, WhatsApp Business, Gmail. |
| Programación de contenido | Metricool, Buffer, Later, Publer. |
| IA para texto | OpenAI, Anthropic, Google Gemini, Mistral, según disponibilidad y costo. |

### Plantilla rápida para mapear un proceso automatizable

Copia esta tabla y llénala con una tarea real de tu startup:

| Campo | Ejemplo |
|---|---|
| Proceso | Responder preguntas de clientes |
| Frecuencia | 40 mensajes/semana |
| Tiempo actual | 5 horas/semana |
| Entradas | mensaje, nombre, producto consultado |
| Salidas deseadas | respuesta, registro, alerta si es complejo |
| Reglas claras | Sí/No |
| Riesgo si falla | Bajo/Medio/Alto |
| ¿Se puede automatizar? | Sí, con supervisión humana |
| Primera versión | Clasificar y responder FAQ simples |
| Métrica | Tiempo de respuesta y % resuelto sin humano |

### Buenas prácticas de prompt para emprendedores

Usa esta estructura:

```text
Rol: Eres un experto en...
Tarea: Analiza/genera/clasifica...
Contexto: Mi negocio es...
Entrada: Aquí están los datos...
Formato de salida: Responde así...
Restricciones: No inventes, sé breve, evita...
Ejemplo: Así es una buena respuesta...
```

Ejemplo corto:

```text
Eres un asesor comercial de una startup que vende software de facturación a pymes. Analiza el lead y asigna un score de 0 a 100. Responde solo con: SCORE, SEGMENTO, RAZÓN, SIGUIENTE_ACCIÓN. No inventes datos. Si falta información clave, usa segmento "revisar".
```

### Protección de datos y ética

- Pide consentimiento cuando recolectes datos personales.
- No envíes contraseñas, datos bancarios, documentos de identidad sensibles ni información médica a la IA.
- Informa cuando un cliente interactúa con un bot, especialmente en atención al cliente.
- Guarda registros para poder auditar decisiones automatizadas.
- Adapta montos, language y ejemplos a tu país y moneda.

---

## 6. Preguntas de autoevaluación

Responde estas preguntas con tus propias palabras. Si puedes responderlas claramente, significa que comprendiste el módulo.

### Pregunta 1

Elige un proceso repetitivo de tu startup y describe cómo lo automatizarías con IA. Incluye: disparador, datos de entrada, tarea de la IA, acción final y dónde interviene un humano.

**Qué debe contener tu respuesta:**

- Un proceso concreto, por ejemplo: responder correos, calificar leads, generar contenido.
- Un trigger claro: nuevo formulario, nuevo mensaje, pago recibido, cita agendada.
- Una tarea de IA realista: clasificar, resumir, generar, extraer.
- Una salida útil: respuesta, alerta, registro, tarea.
- Un punto de control humano.

---

### Pregunta 2

¿Por qué no conviene automatizar completamente la atención al cliente desde el primer día? Menciona dos riesgos y dos medidas para mitigarlos.

**Qué debe contener tu respuesta:**

Riesgos posibles:

- La IA puede responder mal o inventar información.
- Clientes frustrados pueden sentirse ignorados si no hay opción humana.
- Pueden revelarse datos sensibles sin control.
- La marca puede perder tono humano.

Medidas posibles:

- Mantener opción de hablar con persona.
- Empezar respondiendo solo preguntas frecuentes verificadas.
- Revisar conversaciones diariamente.
- Usar base de conocimiento actualizada.
- Escalar casos complejos automáticamente.

---

### Pregunta 3

Diseña tres criterios simples para calificar leads en tu negocio. Explica cómo medirías si tu automatización está funcionando mejor que el proceso manual.

**Qué debe contener tu respuesta:**

Tres criterios ejemplo:

- Urgencia: este mes, 1–3 meses, solo investigando.
- Presupuesto: rango bajo, medio, alto.
- Fit: coincide con cliente ideal o no.
- Contacto: teléfono/correo válido.
- Cargo: decisor o influenciador.

Métricas posibles:

- Tiempo promedio de primer contacto.
- Porcentaje de leads atendidos el mismo día.
- Tasa de respuesta.
- Tasa de conversión a reunión o venta.
- Horas ahorradas por semana.
- Número de errores o reclamos por automatización.

---

## Cierre del módulo

La automatización con IA no es un lujo técnico ni una meta lejana. Es una forma práctica de hacer más con el equipo que ya tienes. Para un emprendedor latinoamericano, el valor está en responder más rápido, ordenar el seguimiento comercial, crear contenido constante y liberar horas valiosas del fundador.

Tu próximo paso no es automatizar todo. Es elegir una tarea pequeña, diseñar el flujo, probarlo con datos reales y medir el impacto. Cuando ese primer flujo funcione, tendrás confianza para escalar hacia atención al cliente, contenido, ventas y operaciones.