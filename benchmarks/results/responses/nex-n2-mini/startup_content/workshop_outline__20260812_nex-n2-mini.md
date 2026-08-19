# Nex-N2-Mini — startup_content/workshop_outline

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 8.67 | quality: 9.44
- latency_total: 42.738s | tokens_per_second: 191.7
- input_tokens: 201 | output_tokens: 8192
- judge_score: 4.6 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un facilitador de workshops de emprendimiento y tecnologia con experiencia en Latinoamerica.

**user:**

Crea el outline completo para un workshop presencial de 3 horas titulado:
"Construye tu Asistente de IA para tu Startup - Workshop Practico"

La audiencia son emprendedores early-stage no-tecnicos (20-30 personas).

Incluye:
1. Agenda detallada con tiempos (3 horas)
2. Materiales necesarios (que preparar antes)
3. Para cada bloque:
   - Titulo y duracion
   - Objetivo
   - Dinamica (charla, ejercicio, demo, discusion)
   - Key takeaway
4. Ejercicio principal del workshop (que todos puedan hacer)
5. Recursos para llevar a casa
6. Slide count estimado por seccion

El tono debe ser energico y practico, no academico.


## Respuesta completa

# Outline completo: Workshop presencial de 3 horas  
## “Construye tu Asistente de IA para tu Startup - Workshop Práctico”

**Audiencia:** emprendedores early-stage, no técnicos, 20-30 personas.  
**Formato:** presencial, trabajo en equipos de 2-3 personas.  
**Resultado final:** cada equipo sale con un MVP funcional de asistente de IA para su startup, una base de conocimiento inicial, un prompt maestro y un plan simple de lanzamiento.

---

# 1. Agenda detallada con tiempos

| Tiempo | Bloque | Actividad central | Objetivo |
|---|---|---|---|
| 0:00 - 0:10 | Bienvenida + mapa del día | Presentación rápida, reglas del workshop y formación de equipos | Crear energía inicial y dejar claro qué se va a construir |
| 0:10 - 0:30 | ¿Dónde puede ayudar IA a tu startup? | Identificación de casos de uso reales | Elegir un problema concreto donde IA pueda ahorrar tiempo, vender más o mejorar atención |
| 0:30 - 0:50 | Anatomía de un asistente de IA | Mini-charla práctica + ejemplos de buenos y malos asistentes | Entender qué necesita un asistente para funcionar: conocimiento, reglas, tono, límites y mano humana |
| 0:50 - 1:15 | Demo en vivo | Construcción rápida de un asistente desde cero | Ver que un MVP puede crearse en menos de 30 minutos, sin programar |
| 1:15 - 1:25 | Break + setup de herramientas | Descanso y revisión de acceso a plataformas | Preparar a todos para construir |
| 1:25 - 2:10 | Sprint principal | Construcción del MVP del asistente de IA | Crear una primera versión funcional del asistente |
| 2:10 - 2:35 | Prueba, mejora y ajuste | Test con preguntas difíciles + iteración | Aprender a detectar errores, ambigüedades y respuestas inseguras |
| 2:35 - 2:50 | Lanzamiento seguro | Checklist de privacidad, límites, escalado y métricas | Definir cómo lanzar sin generar problemas |
| 2:50 - 3:00 | Pitch rápido + compromiso final | Cada equipo comparte su asistente en 60 segundos | Cerrar con aprendizaje, próximos pasos y motivación |

**Total:** 180 minutos / 3 horas.

---

# 2. Materiales necesarios

## A. Preparar antes - facilitador

### Sala y logística

- Proyector o pantalla grande.
- Wi-Fi estable.
- Extensión eléctrica o regletas para cada mesa.
- Pizarra o rotafolio.
- Marcadores.
- Post-its.
- Tarjetas de colores.
- Cinta adhesiva o masilla.
- Impresiones del **Canvas del Asistente de IA**.
- Impresiones de la **plantilla de prompt maestro**.
- Impresiones del **checklist de pruebas**.
- Impresiones del **checklist de lanzamiento**.
- Código QR para:
  - Formulario de registro.
  - Descarga de materiales.
  - Herramientas recomendadas.
  - Grupo de seguimiento post-workshop.

### Herramientas recomendadas

Usar una herramienta principal para que todos avancen rápido:

- **Opción recomendada:** Chatbase, Botpress Cloud, Casetta o similar para crear un chatbot con documentos.
- **Alternativa gratuita o simple:** ChatGPT + Google Sheets + Tally/Typeform.
- **Para conexión posterior:** Zapier, Make o Google Apps Script, solo como bonus.

Importante: preparar una cuenta demo y una cuenta alternativa por si falla internet o una plataforma.

### Material demo

Preparar una demo con una startup ficticia, por ejemplo:

**“AulaExpress”**  
Startup que vende cursos online para pymes.

Materiales para la demo:

- 8-10 preguntas frecuentes.
- 1 documento con información de precios.
- 1 documento con proceso de onboarding.
- 1 documento con política de cancelación.
- 3 respuestas que el asistente debe dar correctamente.
- 3 preguntas difíciles donde debe decir “no lo sé” o escalar.
- 1 ejemplo de mensaje de escalado a humano.

### Plantillas para repartir

Preparar carpetas compartidas con:

- Canvas del asistente de IA.
- Prompt maestro.
- Lista de preguntas frecuentes.
- Plantilla de prueba de respuestas.
- Checklist de lanzamiento.
- Dashboard simple de métricas.
- Guía de seguridad y privacidad.
- Plan de acción de 30 días.

---

## B. Pedir que traigan los participantes

Antes del workshop, enviar un mensaje a los emprendedores:

**Trae:**

1. Laptop.
2. Cuenta de Google, Notion, Chatbase, Botpress o similar.
3. Una descripción de tu startup en una frase.
4. Tus preguntas frecuentes de clientes.
5. Un documento útil:
   - FAQ.
   - Manual de producto.
   - Precio.
   - Política de cancelación.
   - Guía de onboarding.
   - Preguntas de ventas.
6. 3 ejemplos de clientes que suelen preguntar algo repetitivo.

---

# 3. Bloques del workshop

## Bloque 1: Bienvenida + mapa del día

**Duración:** 10 minutos

### Objetivo

Crear energía, explicar el resultado práctico del workshop y formar equipos.

### Dinámica

- Presentación rápida del facilitador.
- Regla del día: “No venimos a entender toda la IA, venimos a construir algo útil”.
- Cada participante responde en voz alta:
  - “Soy ___”
  - “Mi startup hace ___”
  - “Quiero que mi asistente de IA me ayude con ___”
- Formación de equipos de 2-3 personas.

### Key takeaway

La IA será más útil si se aplica a un problema concreto de la startup, no como experimento abstracto.

### Slide count estimado

3 slides.

---

## Bloque 2: ¿Dónde puede ayudar IA a tu startup?

**Duración:** 20 minutos

### Objetivo

Identificar oportunidades reales dentro del negocio.

### Dinámica

1. El facilitador muestra ejemplos rápidos de uso de IA:
   - Atención al cliente.
   - Soporte interno.
   - Generación de respuestas de ventas.
   - Onboarding de clientes.
   - Clasificación de leads.
   - Resumen de reuniones.
   - Respuestas frecuentes en WhatsApp, web o email.

2. Ejercicio individual:
   - Escribir en post-its 3 tareas repetitivas que consumen tiempo.
   - Escribir 3 preguntas que los clientes hacen todos los días.
   - Marcar cuál podría responder un asistente de IA.

3. Puesta en común:
   - Cada equipo elige un caso de uso.
   - Lo escribe así:  
     **“Queremos un asistente de IA que ayude a ___ a resolver ___ usando ___.”**

Ejemplo:

> “Queremos un asistente de IA que ayude a nuevos usuarios a resolver dudas de onboarding usando nuestro manual de producto y FAQ.”

### Key takeaway

Un buen asistente de IA empieza con una tarea repetitiva, frecuente y medible.

### Slide count estimado

5 slides.

---

## Bloque 3: Anatomía de un asistente de IA

**Duración:** 20 minutos

### Objetivo

Explicar de forma simple cómo funciona un asistente de IA y qué lo hace útil o peligroso.

### Dinámica

Mini-charla práctica con ejemplos.

Explicar los 5 componentes:

1. **Propósito**  
   ¿Para qué existe? Atención, ventas, soporte, onboarding, etc.

2. **Usuario objetivo**  
   ¿A quién ayuda? Cliente nuevo, cliente existente, vendedor, equipo interno.

3. **Base de conocimiento**  
   Qué información puede usar: FAQ, documentos, precios, políticas, guías.

4. **Prompt o personalidad**  
   Cómo habla, qué tono usa, qué límites tiene.

5. **Escalamiento a humano**  
   Qué hace cuando no sabe, cuando hay riesgo o cuando el caso es complejo.

### Ejemplo de mala respuesta

Cliente pregunta:  
“¿Cuánto cuesta?”  

Asistente inventa:  
“Cuesta 99 dólares al mes.”

Problema: puede estar equivocado.

### Ejemplo de buena respuesta

“Asistente dice:  
‘Nuestros planes comienzan desde $49 al mes. Te dejo las opciones disponibles y si quieres puedo ayudarte a elegir el más adecuado.’”

### Key takeaway

Un buen asistente no es el que responde todo; es el que responde bien, sabe cuándo no sabe y sabe escalar.

### Slide count estimado

6 slides.

---

## Bloque 4: Demo en vivo - Construyendo un asistente desde cero

**Duración:** 25 minutos

### Objetivo

Mostrar que se puede construir un MVP sin programar.

### Dinámica

Demo en vivo con herramienta no-code.

Pasos:

1. Crear nuevo asistente.
2. Nombrarlo.
3. Definir propósito.
4. Subir documentos o pegar FAQ.
5. Escribir prompt de comportamiento.
6. Configurar tono.
7. Configurar límites:
   - No inventar precios.
   - No prometer descuentos.
   - Escalar casos sensibles.
8. Probar 5 preguntas.
9. Mostrar cómo compartir el enlace.

### Ejemplo de prompt para demo

> Actúa como el asistente de soporte de AulaExpress.  
> Tu trabajo es ayudar a usuarios nuevos a entender el producto, los precios, el onboarding y las políticas básicas.  
> Responde con tono cercano, claro y breve.  
> Usa solo la información disponible en la base de conocimiento.  
> Si no sabes algo, di que no tienes esa información y ofrece contactar al equipo humano.  
> No inventes precios, fechas ni promociones.

### Key takeaway

Un asistente útil no requiere ser perfecto: se lanza como MVP, se prueba y se mejora.

### Slide count estimado

7 slides + demo en vivo.

---

## Bloque 5: Break + setup de herramientas

**Duración:** 10 minutos

### Objetivo

Descansar y preparar a los equipos para construir.

### Dinámica

- Break.
- Revisión de acceso a herramientas.
- El facilitador y ayudantes resuelven problemas técnicos.
- Los equipos revisan su caso de uso y base de conocimiento.

### Key takeaway

La velocidad depende de tener claro qué vas a construir antes de tocar la herramienta.

### Slide count estimado

0-1 slide.

---

## Bloque 6: Sprint principal - Construcción del MVP

**Duración:** 45 minutos

### Objetivo

Que cada equipo cree su primer asistente de IA funcional.

### Dinámica

Trabajo en equipos.

El facilitador acompaña con preguntas:

- ¿Qué problema resuelve?
- ¿A quién ayuda?
- ¿Qué información necesita?
- ¿Qué no debe responder?
- ¿Cómo escalará a un humano?
- ¿Cómo sabrán si funciona?

### Estructura del sprint

| Tiempo | Paso | Acción |
|---|---|---|
| 5 min | Definir caso de uso | Escribir en una frase qué hará el asistente |
| 10 min | Preparar base de conocimiento | Reunir FAQ, precios, políticas, onboarding o guías |
| 10 min | Configurar herramienta | Crear asistente y cargar información |
| 10 min | Escribir prompt | Definir rol, tono, límites y escalado |
| 5 min | Probar primeras preguntas | Hacer 5 tests básicos |
| 5 min | Ajustar | Corregir respuesta confusa, ambigua o incorrecta |

### Entregable del sprint

Cada equipo debe salir con:

- Nombre del asistente.
- Propósito.
- Base de conocimiento cargada.
- Prompt inicial.
- Link o enlace de prueba.
- 5 preguntas iniciales de test.

### Key takeaway

La primera versión no tiene que ser perfecta; tiene que ser testeable.

### Slide count estimado

3 slides.

---

# 4. Ejercicio principal del workshop

## “Construye tu asistente de IA MVP”

### Descripción

Cada equipo creará un asistente de IA no-code que responda preguntas frecuentes de su startup usando una base de conocimiento simple.

El asistente puede estar pensado para:

- Atención al cliente.
- Soporte interno.
- Onboarding.
- Ventas.
- Preguntas frecuentes.
- Captura de leads.
- Seguimiento post-venta.

### Objetivo del ejercicio

Construir un MVP que pueda probarse con usuarios reales en menos de 24 horas.

---

## Paso 1: Elegir el caso de uso

Cada equipo completa esta frase:

> “Mi asistente de IA ayudará a ______ a ______, usando ______.”

Ejemplos:

> “Mi asistente de IA ayudará a nuevos clientes a entender cómo configurar su cuenta, usando nuestra guía de onboarding.”

> “Mi asistente de IA ayudará al equipo comercial a responder dudas frecuentes antes de una demo, usando nuestra FAQ de ventas.”

> “Mi asistente de IA ayudará a clientes existentes a resolver problemas comunes, usando nuestro manual de soporte.”

---

## Paso 2: Crear la base de conocimiento mínima

Cada equipo debe preparar 5-10 respuestas claras.

Debe incluir:

- 3 preguntas frecuentes.
- 2 datos importantes: precio, política, proceso o condición.
- 2 preguntas difíciles donde el asistente debe decir que no sabe.
- 1 canal de escalado a humano.

Ejemplo:

| Pregunta | Respuesta esperada |
|---|---|
| ¿Cómo inicio sesión? | Explicar paso a paso |
| ¿Cuánto cuesta el plan básico? | Dar precio correcto |
| ¿Qué pasa si quiero cancelar? | Explicar política |
| ¿Tienen descuento para gobierno? | Escalar a ventas |
| ¿Pueden hacer una integración específica? | Escalar a producto |

---

## Paso 3: Escribir el prompt maestro

Plantilla para usar:

```text
Actúa como el asistente de IA de [NOMBRE STARTUP].

Tu rol es ayudar a [USUARIO OBJETIVO] con [PROBLEMA O NECESIDAD].

Responde con tono [TONO: cercano, profesional, claro, breve].

Usa únicamente la información de la base de conocimiento.

Si no sabes la respuesta, di:
“Ahora mismo no tengo esa información, pero puedo ayudarte a contactar al equipo humano.”

No inventes precios, fechas, promociones, disponibilidad o garantías.

Si el usuario pregunta sobre [CASOS SENSIBLES], escala a un humano.

Antes de responder, identifica si la pregunta requiere:
1. Respuesta directa.
2. Más información del usuario.
3. Escalamiento a humano.

Termina cada respuesta con una siguiente acción útil.
```

---

## Paso 4: Probar con preguntas difíciles

Cada equipo prueba al menos 10 preguntas:

- 5 preguntas normales.
- 3 preguntas fuera de alcance.
- 2 preguntas ambiguas o difíciles.

Ejemplo de preguntas difíciles:

- “¿Me puedes devolver mi dinero hoy?”
- “¿Qué pasa si no uso el producto?”
- “¿Tienen una política especial para mi país?”
- “¿Puedes garantizar estos resultados?”
- “¿Puedes revisar mi caso personalmente?”

---

## Paso 5: Mejorar el asistente

Después de probar, cada equipo ajusta:

- Prompt.
- Redacción de respuestas.
- Base de conocimiento.
- Límites.
- Mensaje de escalado.
- Tono.

### Key takeaway del ejercicio principal

Un asistente de IA de calidad se construye con información clara, límites bien definidos y pruebas constantes.

---

# 5. Bloque 7: Prueba, mejora y ajuste

**Duración:** 25 minutos

### Objetivo

Aprender a evaluar si el asistente realmente funciona.

### Dinámica

Cada equipo hace una simulación rápida:

1. Una persona actúa como cliente.
2. Otra persona interactúa con el asistente.
3. La tercera registra respuestas en una tabla.

### Plantilla de prueba

| Pregunta | Respuesta correcta | Error o mejora | Calificación 0-3 |
|---|---|---|---|
| Pregunta 1 | Sí/No | Comentario | 0, 1, 2 o 3 |
| Pregunta 2 | Sí/No | Comentario | 0, 1, 2 o 3 |

### Escala de evaluación

- **3:** Respuesta correcta, clara y útil.
- **2:** Respuesta útil, pero mejorable.
- **1:** Respuesta incompleta o confusa.
- **0:** Respuesta incorrecta o peligrosa.

### Regla clave

Si el asistente falla en respuestas sensibles, no se lanza todavía.

### Key takeaway

No se trata de que el asistente responda mucho; se trata de que responda bien.

### Slide count estimado

5 slides.

---

# 6. Bloque 8: Lanzamiento seguro

**Duración:** 15 minutos

### Objetivo

Preparar a los equipos para lanzar una primera versión de forma responsable.

### Dinámica

Mini-charla + checklist.

Explicar los riesgos principales:

- Responder con información incorrecta.
- Usar datos sensibles sin permiso.
- Prometer algo que la startup no puede cumplir.
- Atender preguntas legales, médicas o financieras sin criterio.
- Reemplazar completamente al equipo humano demasiado pronto.

### Checklist de lanzamiento

Antes de compartir el asistente con clientes, responder:

- ¿Sé qué preguntas debe responder?
- ¿Sé qué preguntas debe negarse a responder?
- ¿Tiene datos actualizados?
- ¿Tiene mensaje de escalado a humano?
- ¿Tiene tono adecuado?
- ¿Está probado con al menos 10 preguntas?
- ¿Hay una persona responsable de revisar errores?
- ¿Tengo métricas para medirlo?
- ¿Estoy usando solo información permitida?
- ¿Mi equipo está preparado para recibir casos escalados?

### Métricas simples

Cada equipo elige 2-3 métricas:

- Tiempo promedio