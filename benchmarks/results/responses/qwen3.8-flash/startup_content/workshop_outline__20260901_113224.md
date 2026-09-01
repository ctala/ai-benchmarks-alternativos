# Qwen 3.8 Flash — startup_content/workshop_outline

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 159.341s | tokens_per_second: 87.7
- input_tokens: 240 | output_tokens: 13976
- judge_score: 5.0 | justificación: 

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

# Outline completo del workshop presencial  
## **“Construye tu Asistente de IA para tu Startup – Workshop Práctico”**

**Duración:** 3 horas  
**Audiencia:** 20–30 emprendedores early-stage, no técnicos  
**Formato:** presencial, práctico, con laptop o papel  
**Resultado tangible:** cada participante sale con un **MVP de asistente de IA** para su startup: tarea definida, prompt maestro, casos de prueba y plan de implementación.

**Filosofía del taller:**  
Nada de teoría larga. Nada de “IA mágica”.  
Objetivo: que salgan con algo **funcional, testeado y listo para mejorar**.

---

# 1. Agenda detallada con tiempos – 3 horas / 180 minutos

| Hora | Bloque | Duración | Dinámica | Objetivo | Key takeaway | Slides |
|---|---:|---:|---|---|---|---:|
| 0:00–0:10 | Bienvenida y activación | 10 min | Charla corta + dinámica “tarea que te come la semana” | Generar energía, contexto y diagnóstico rápido | “Tu asistente empieza por una tarea real, no por una idea vaga” | 2 |
| 0:10–0:30 | Por qué un asistente de IA para una startup | 20 min | Charla + casos + mitos vs realidades | Mostrar valor, límites y oportunidades | “La IA no reemplaza tu estrategia; amplifica tu operación” | 6 |
| 0:30–0:50 | Anatomía de un asistente que funciona | 20 min | Charla + mini ejercicio de definición | Enseñar la estructura básica de un asistente | “Rol + contexto + tarea + reglas + formato = mejor respuesta” | 6 |
| 0:50–1:10 | Demo en vivo: de problema a asistente | 20 min | Demo práctica | Mostrar cómo se construye sin código | “No se hace perfecto de entrada; se itera” | 4 |
| 1:10–1:25 | Break | 15 min | Pausa | Reset mental y networking | “Pausa para volver con foco” | 1 |
| 1:25–2:05 | Ejercicio principal: construye tu asistente MVP | 40 min | Hands-on individual + soporte del facilitador | Que cada emprendedor cree su primer asistente | “Un asistente útil nace de una tarea específica” | 6 |
| 2:05–2:25 | Testeo y iteración en parejas | 20 min | Peer testing | Mejorar prompts con casos reales | “Test cases > opiniones” | 3 |
| 2:25–2:45 | Show & tell + feedback grupal | 20 min | Presentaciones cortas + feedback | Aprender de otros asistentes | “Mejoras concretas en 2 minutos” | 2 |
| 2:45–3:00 | Cierre: plan de 7 días | 15 min | Charla + compromiso + recursos | Definir siguiente paso | “Automatiza una tarea esta semana” | 4 |
| **Total** |  | **180 min** |  |  |  | **34 slides** |

---

# 2. Materiales necesarios – qué preparar antes

## A. Previo al workshop – 1 a 2 semanas antes

1. **Encuesta rápida a participantes**
   - Etapa de la startup.
   - Sector o modelo de negocio.
   - Tarea que más tiempo les consume.
   - Canales usados: WhatsApp, email, redes, web, CRM, etc.
   - Nivel de comodidad con IA.
   - Preocupaciones: privacidad, costo, equipo, tiempo.

2. **Preparar plantillas impresas o digitales**
   - **Assistant Canvas** para cada participante.
   - **Prompt maestro** con espacios para llenar.
   - **Ficha de test cases** con 3 escenarios mínimos.
   - **Checklist de calidad** para evaluar el asistente.

3. **Preparar tarjetas de escenarios**
   Ejemplos:
   - Soporte al cliente.
   - Calificación de leads.
   - Respuestas por WhatsApp.
   - Onboarding de clientes.
   - Generación de contenido.
   - Resúmenes de reuniones.
   - Operaciones internas.
   - FAQ de producto.
   - Seguimiento de pagos.
   - Atención postventa.

4. **Preparar demo en vivo**
   - Elegir una startup ficticia o real anonimizada.
   - Ejemplo: tienda online de café, app de reservas, SaaS para pymes, agencia de marketing.
   - Tener listo un chat con IA: ChatGPT, Claude o Gemini.
   - Tener un “prompt malo” y uno “prompt mejorado”.
   - Mostrar 3 casos de prueba.

5. **Preparar recursos para llevar a casa**
   - PDF con plantillas.
   - QR con carpeta de recursos.
   - Lista de herramientas no-code.
   - Plan de 7 días.
   - Biblioteca de prompts.

6. **Coordinar logística técnica**
   - Wi-Fi estable.
   - Extensión eléctrica o regletas.
   - Proyector o pantalla.
   - Micrófono si la sala es grande.
   - Timer visible.
   - Música para entrada, break y cierre.

---

## B. Sala y layout para 20–30 personas

**Recomendado:** mesas en islas de 4–5 personas.

Elementos:
- Pantalla principal.
- Computadora del facilitador.
- Conexión a internet.
- Temporizador visible.
- Pizarra, flipchart o papelógrafo.
- Post-its.
- Marcadores.
- Tarjetas impresas.
- Hojas de trabajo por participante.
- Botellas de agua o café.
- Música ambiental.
- QR para recursos digitales.

**Ideal:** 1 facilitador + 1 co-facilitador o “supporter” para resolver dudas durante el ejercicio.

---

## C. Kit por participante

Cada persona debe tener:

- Laptop, tablet o celular.
- Cuenta gratuita en una herramienta de IA:
  - ChatGPT, Claude, Gemini, Perplexity u otra disponible.
- Plantilla impresa o digital: **Assistant Canvas**.
- Prompt maestro.
- Ficha de 3 test cases.
- Checklist de calidad.
- Tarjeta de escenario, si no traen su caso propio.
- Acceso al QR de recursos.

**Opción sin laptop:**  
Papel y lápiz. El objetivo es diseñar el asistente, no obligar a usar una herramienta específica.

---

## D. Kit del facilitador

- Slides finales.
- Demo probada.
- Cuenta demo de IA.
- Plantillas en PDF.
- Cronómetro.
- Tarjetas de feedback.
- Ejemplos de asistentes:
  - Soporte.
  - Ventas.
  - Contenido.
  - Operaciones.
  - Onboarding.
- Checklist de privacidad.
- Guía de contingencia.

---

## E. Contingencias recomendadas

| Problema | Solución |
|---|---|
| No hay Wi-Fi | Usar demo descargada y ejercicio en papel |
| Algunos no tienen laptop | Usar celular o trabajo en parejas |
| Herramienta de IA falla | Tener backup con otra plataforma |
| Participantes avanzados | Reto extra: conectar a WhatsApp, email o Forms |
| Participantes muy novatos | Tarjetas prellenadas y prompts de ejemplo |
| Grupo grande sin co-facilitador | Ejercicios en parejas y feedback cruzado |

---

# 3. Bloques detallados

---

## Bloque 1: Bienvenida y activación  
**Duración:** 10 minutos  
**Slides:** 2

### Objetivo
Generar energía, alinear expectativas y descubrir rápidamente qué tareas quiere automatizar cada emprendedor.

### Dinámica
- Charla corta: 2 min.
- Pregunta rápida: 5 min.
- Mapeo en pizarra: 3 min.

**Pregunta de activación:**  
“¿Qué tarea repetitiva te come la semana y te gustaría delegar hoy?”

Los participantes responden en parejas durante 1 minuto y luego comparten una palabra clave con el facilitador.

El facilitador anota en la pizarra categorías:
- Soporte.
- Ventas.
- Contenido.
- Operaciones.
- Resúmenes.
- Seguimiento.
- Pagos.
- Onboarding.

### Key takeaway
“Tu asistente empieza por una tarea real, no por una idea vaga.”

### Notas de facilitación
- Tono rápido, cercano, práctico.
- No dejar que se vuelva sesión de networking.
- Usar frases como:  
  “Aquí no venimos a entender IA; venimos a usarla.”

---

## Bloque 2: Por qué un asistente de IA para una startup  
**Duración:** 20 minutos  
**Slides:** 6

### Objetivo
Mostrar el valor concreto de un asistente de IA para una startup early-stage, especialmente para equipos pequeños, sin programar.

### Dinámica
Charla + casos + mito/realidad.

### Contenido sugerido

#### 1. El problema del emprendedor early-stage
- Pocas manos.
- Muchas tareas.
- Soporte, ventas, contenido, operaciones y estrategia al mismo tiempo.

#### 2. Qué puede hacer un asistente de IA
Ejemplos prácticos:
- Responder preguntas frecuentes.
- Redactar respuestas por WhatsApp o email.
- Calificar leads.
- Generar contenido para redes.
- Resumir reuniones.
- Crear propuestas.
- Ayudar con onboarding.
- Reducir carga operativa.

#### 3. Qué no debe hacer sin supervisión
- Prometer precios sin validar.
- Tomar decisiones legales o financieras sensibles.
- Acceder a datos personales sin control.
- Reemplazar criterio humano en temas críticos.

#### 4. Mitos vs realidades
- Mito: “La IA lo automatiza todo.”  
  Realidad: “Automatiza tareas claras.”
- Mito: “Necesito programar.”  
  Realidad: “Puedes empezar con prompts y herramientas no-code.”
- Mito: “El prompt perfecto existe.”  
  Realidad: “El mejor prompt es el que testas y mejoras.”

### Key takeaway
“La IA no reemplaza tu estrategia; amplifica tu operación.”

### Notas de facilitación
- Usar ejemplos latinoamericanos:
  - WhatsApp.
  - Mercado Pago.
  - OXXO.
  - Stripe.
  - Google Forms.
  - Notion.
  - Airtable.
- Evitar lenguaje técnico.
- Mantener energía: “Esto no es futuro, es para esta semana.”

---

## Bloque 3: Anatomía de un asistente que funciona  
**Duración:** 20 minutos  
**Slides:** 6

### Objetivo
Dar un framework simple para diseñar un asistente de IA útil, seguro y práctico.

### Dinámica
Charla + mini ejercicio.

### Framework: “R.C.T.R.F.”

1. **Rol**  
   ¿Quién es el asistente?  
   Ejemplo: “agente de soporte”, “asistente comercial”, “editor de contenido”.

2. **Contexto**  
   ¿Para qué startup trabaja?  
   Incluye producto, cliente ideal, etapa, tono, canal.

3. **Tarea**  
   ¿Qué debe hacer?  
   Mejor una tarea clara que muchas tareas vagas.

4. **Reglas**  
   ¿Qué no debe hacer?  
   Ejemplo: no inventar, no dar consejo legal, escalar si falta información.

5. **Formato**  
   ¿Cómo debe responder?  
   Ejemplo: respuesta breve, siguiente acción, si escalar.

### Mini ejercicio
Cada participante escribe en 60 segundos:
- Una tarea.
- Un usuario.
- Un límite.

Ejemplo:  
“Responder dudas sobre envíos a clientes de e-commerce. Límite: no inventar tiempos.”

### Key takeaway
“Rol + contexto + tarea + reglas + formato = mejor respuesta.”

### Notas de facilitación
- Insistir en que un asistente no es “chatbot genérico”.
- La calidad viene del contexto y las reglas.
- Usar ejemplos de startup early-stage.

---

## Bloque 4: Demo en vivo – de problema a asistente  
**Duración:** 20 minutos  
**Slides:** 4

### Objetivo
Mostrar en vivo cómo se construye un MVP de asistente de IA sin código.

### Dinámica
Demo práctica con una startup ficticia.

### Ejemplo de demo

**Startup:** Café Andino, e-commerce de café de especialidad.  
**Problema:** el fundador responde todo por WhatsApp y no da abasto.  
**Tarea del asistente:** responder preguntas frecuentes sobre envíos, molienda y pagos.

#### Paso 1: Prompt inicial débil
“Eres un asistente de soporte.”

Resultado: respuestas genéricas, sin contexto, sin límites.

#### Paso 2: Agregar contexto
“Eres agente de soporte de Café Andino, tienda de café de especialidad en Latinoamérica.”

#### Paso 3: Agregar tarea clara
“Responde dudas sobre envíos, molienda, pagos con Mercado Pago y suscripciones.”

#### Paso 4: Agregar reglas
“No inventes tiempos de envío.  
No des consejo nutricional.  
Si el cliente pide reembolso, escalar a humano.”

#### Paso 5: Agregar formato
“Responde en máximo 3 líneas:  
1. Respuesta clara.  
2. Siguiente acción.  
3. Si escalar.”

#### Paso 6: Testear 3 casos
- “¿Cuándo llega a Bogotá?”
- “¿Puedo pagar con OXXO?”
- “Mi pedido llegó dañado.”

### Key takeaway
“No se hace perfecto de entrada; se itera.”

### Notas de facilitación
- Mostrar errores en vivo. Eso humaniza.
- Explicar que el asistente se mejora con pruebas.
- No usar jerga técnica.

---

## Bloque 5: Break  
**Duración:** 15 minutos  
**Slides:** 1

### Objetivo
Descanso, reset mental y networking.

### Dinámica
- Música.
- Café.
- Pizarra con reto suave: “En el break, piensa una tarea que tu asistente podría resolver esta semana.”

### Key takeaway
“Pausa para volver con foco.”

---

## Bloque 6: Ejercicio principal – construye tu asistente MVP  
**Duración:** 40 minutos  
**Slides:** 6

### Objetivo
Que cada participante construya un MVP de asistente de IA para una tarea concreta de su startup.

### Dinámica
Hands-on individual o en parejas.  
El facilitador y co-facilitador acompañan.

### Resultado esperado
Cada participante debe salir con:

1. **Tarea del asistente**
2. **Assistant Canvas**
3. **Prompt maestro**
4. **3 casos de prueba**
5. **1 mejora sugerida**
6. **Siguiente paso**

### Estructura del ejercicio

#### 0–5 min: Elegir escenario
Puede ser propio o una tarjeta:
- Soporte.
- Ventas.
- Contenido.
- Operaciones.
- Onboarding.
- Seguimiento.
- FAQ.
- Resúmenes.

#### 5–12 min: Llenar Assistant Canvas
- ¿Qué hace el asistente?
- ¿Para quién?
- ¿Qué canal?
- ¿Qué datos usa?
- ¿Qué no debe hacer?
- ¿Cuándo escalar?
- ¿Cómo debe responder?

#### 12–25 min: Escribir el prompt maestro
Usar la plantilla entregada.

#### 25–35 min: Testear 3 casos
- Caso fácil.
- Caso raro.
- Caso sin información.

#### 35–40 min: Iterar
Corregir el prompt con base en los tests.

### Key takeaway
“Un asistente útil nace de una tarea específica.”

### Notas de facilitación
- Insistir: una sola tarea.
- Evitar asistentes tipo “haz todo por mí”.
- Recordar privacidad: no pegar datos sensibles de clientes.

---

## Bloque 7: Testeo y iteración en parejas  
**Duración:** 20 minutos  
**Slides:** 3

### Objetivo
Mejorar los asistentes con feedback real entre participantes.

### Dinámica
Trabajo en parejas.

### Proceso
Cada pareja recibe una ficha con 3 preguntas:

1. ¿El asistente entiende el contexto?
2. ¿La respuesta tiene formato útil?
3. ¿Hay riesgo de inventar o confundir?

Cada persona testea el prompt de su compañero con 3 inputs:

- Pregunta normal.
- Pregunta ambigua.
- Pregunta que requiere escalar.

Luego dan feedback con esta fórmula:

**“1 fortaleza + 1 ajuste + 1 pregunta”**

Ejemplo:  
“Fortaleza: buen tono.  
Ajuste: falta límite de precio.  
Pregunta: ¿qué pasa si el cliente quiere cancelar?”

### Key takeaway
“Test cases > opiniones.”

### Notas de facilitación
- No dejar que se vuelva conversación libre.
- Usar timer por ronda.
- Recoger ejemplos buenos para el show & tell.

---

## Bloque 8: Show & tell + feedback grupal  
**Duración:** 20 minutos  
**Slides:** 2

### Objetivo
Compartir aprendizajes y mejorar con ejemplos reales del grupo.

### Dinámica
Seleccionar 3 asistentes al azar o por votación rápida.

Cada participante presenta:
- Tarea del asistente.
- Prompt o fragmento del prompt.
- Un test case.
- Una mejora necesaria.

Tiempo: 2 minutos por presentación.

Feedback grupal:
- 1 fortaleza.
- 1 ajuste.
- 1 idea de implementación.

### Key takeaway
“Mejoras concretas en 2 minutos.”

### Notas de facilitación
- Elegir casos diversos.
- Evitar que alguien monopolice.
- Celebrar progreso, no perfección.

---

## Bloque 9: Cierre – plan de 7 días  
**Duración:** 15 minutos  
**Slides:** 4

### Objetivo
Que cada participante salga con un siguiente paso claro.

### Dinámica
Charla + compromiso individual.

### Plan sugerido de 7 días

**Día 1:** Elegir una sola tarea.  
**Día 2:** Escribir contexto y reglas.  
**Día 3:** Crear prompt maestro.  
**Día 4:** Testear 10 preguntas reales.  
**Día 5:** Corregir errores y añadir escalación.  
**Día 6:** Usarlo con supervisión humana.  
**Día 7:** Medir: tiempo ahorrado, errores, satisfacción.

### Frase de cierre
“No construyas un asistente para ‘todo tu negocio’. Construye uno para una tarea. Luego escala.”

### Key takeaway
“Automatiza una tarea esta semana.”

---

# 4. Ejercicio principal del workshop  
## **“Reto: Asistente IA MVP para tu startup”**

**Duración total:** 40 minutos  
**Público:** no técnicos  
**Requisito:** laptop, celular o papel  
**Entregable por participante:**  
1. Assistant Canvas.  
2. Prompt maestro.  
3. 3 casos de prueba.  
4. 1 iteración.  
5. Plan de implementación.

---

## Paso a paso detallado

### Paso 1 – Elegir una tarea  
**Tiempo:** 5 minutos

El participante elige una tarea concreta.

Ejemplos:
- Responder dudas frecuentes por WhatsApp.
- Calificar leads por formulario.
- Generar ideas de contenido.
- Resumir notas de reuniones.
- Crear respuestas para objeciones de venta.
- Ayudar con onboarding de clientes.
- Redactar emails de seguimiento.

**Regla:**  
Si la tarea puede explicarse en una frase, sirve.

Mal ejemplo:  
“Quiero un asistente que me ayude con todo el negocio.”

Buen ejemplo:  
“Quiero un asistente que responda preguntas de envío y pago para mi tienda.”

---

### Paso 2 – Llenar el Assistant Canvas  
**Tiempo:** 7 minutos

Plantilla:

| Campo | Pregunta guía |
|---|---|
| Tarea | ¿Qué debe hacer exactamente? |
| Usuario | ¿Quién lo usará? |
| Canal | ¿Dónde responderá? |
| Contexto | ¿Qué información necesita? |
| Tono | ¿Cómo debe sonar? |
| Reglas | ¿Qué no debe hacer? |
| Escalación | ¿Cuándo pasar a humano? |
| Formato | ¿Cómo debe responder? |
| Métrica | ¿Cómo sabrás que funciona? |

Ejemplo:

- Tarea: responder preguntas sobre envíos, molienda y pagos.
- Usuario: clientes de e-commerce.
- Canal: WhatsApp.
- Contexto: tienda de café en Latinoamérica.
- Tono: cercano, claro, profesional.
- Reglas: no inventar precios, no dar consejo nutricional.
- Escalación: reembolsos, reclamos, datos personales.
- Formato: respuesta breve + siguiente acción.
- Métrica: reducir 30% de preguntas repetitivas.

---

### Paso 3 – Escribir el prompt maestro  
**Tiempo:** 13 minutos

Usar esta plantilla:

```text
Actúa como [rol del asistente] de [nombre/tipo de startup].

Contexto:
- Somos una startup de [sector].
- Nuestro cliente ideal es [tipo de cliente].
- Nuestro objetivo es [objetivo].
- Los canales principales son [WhatsApp/email/web/etc.].

Tu tarea:
Responde [tarea específica] usando solo la siguiente información:
[pegar FAQ, descripción de producto, políticas, precios, etc.]

Reglas:
1. No inventes información.
2. Si no sabes, responde: “Necesito confirmar con el equipo.”
3. No des consejo legal, financiero, médico ni nutricional.
4. Escala a un humano si el usuario pide reembolso, cancelación, reclamo o datos sensibles.
5. Mantén un tono [tono].

Formato de respuesta:
1. Respuesta breve.
2. Siguiente acción.
3. Si escalar: “Te paso con una persona del equipo.”

Ejemplo de tono:
Cliente: “¿Cuándo llega mi pedido?”
Respuesta: “Los envíos a [ciudad] toman entre [rango]. Si quieres, puedo ayudarte a revisar tu pedido.”
```

**Importante:**  
No pegar datos personales reales de clientes. Usar información anonimizada.

---

### Paso 4 – Testear 3 casos  
**Tiempo:** 10 minutos

Cada participante prueba su prompt con 3 inputs:

1. **Caso feliz**  
   Pregunta normal.  
   Ejemplo: “¿Cuánto tarda el envío?”

2. **Caso límite**  
   Pregunta ambigua o fuera de alcance.  
   Ejemplo: “¿Me recomiendan café para la gastritis?”

3. **Caso de escalación**  
   Pregunta que debe pasar a humano.  
   Ejemplo: “Quiero reembolso porque llegó roto.”

### Criterios de éxito

El asistente debe:
- Responder de forma útil.
- No inventar.
- Mantener el tono.
- Escalar cuando corresponde.
- Dar una siguiente acción.

---

### Paso 5 – Iterar  
**Tiempo:** 5 minutos

Preguntas de mejora:

- ¿Qué respuesta fue demasiado larga?
- ¿Qué regla faltó?
- ¿Qué contexto adicional ayudaría?
- ¿Qué tipo de pregunta debería escalar?
- ¿El formato es fácil de usar?

Actualizar el prompt con una mejora concreta.

---

## Ejemplo completo de asistente MVP

### Startup
Tienda online de café de especialidad.

### Tarea
Responder preguntas frecuentes por WhatsApp.

### Prompt maestro

```text
Actúa como agente de soporte de Café Andino, una tienda online de café de especialidad en Latinoamérica.

Contexto:
- Vendemos café de especialidad, moliendas personalizadas y suscripciones mensuales.
- Usamos WhatsApp, Mercado Pago y Stripe.
- El cliente ideal es una persona que compra café para casa o pequeños negocios.

Tu tarea:
Responde dudas sobre envíos, molienda, pagos, suscripciones y estado de pedidos usando solo la siguiente información:
- Envíos nacionales: 2 a 4 días hábiles.
- Envíos internacionales: 7 a 15 días hábiles.
- Moliendas disponibles: espresso, filtrado, prensa, francesa.
- Pagos aceptados: tarjeta, Mercado Pago, OXXO.
- Suscripciones: pueden pausarse o cancelarse desde la cuenta.

Reglas:
1. No inventes tiempos de envío ni precios.
2. No des consejo nutricional ni médico.
3. Si el cliente pide reembolso, reclamo o cancelación, escala a un humano.
4. Si no sabes la respuesta, di: “Necesito confirmar con el equipo.”
5. Mantén un tono cercano, claro y profesional.

Formato de respuesta:
1. Respuesta breve.
2. Siguiente acción.
3. Si escalar: “Te paso con una persona del equipo.”
```

### Test cases

1. “¿Cuándo llega mi pedido a Bogotá?”
2. “¿Puedo pagar con OXXO?”
3. “Quiero reembolso porque llegó dañado.”

### Mejora posible
Agregar:  
“No pidas datos personales completos en chat. Para revisar pedido, pide número de orden.”

---

# 5. Recursos para llevar a casa

Entregar en formato digital y/o impreso.

## A. Plantillas

1. **Assistant Canvas**
   - Tarea.
   - Usuario.
   - Canal.
   - Contexto.
   - Reglas.
   - Escalación.
   - Formato.
   - Métrica.

2. **Prompt maestro**
   - Plantilla editable.
   - Ejemplos por caso de uso.

3. **Ficha de test cases**
   - Caso feliz.
   - Caso límite.
   - Caso de escalación.
   - Resultado esperado.

4. **Checklist de calidad**
   - ¿Entiende el contexto?
   - ¿Responde con formato útil?
   - ¿Evita inventar?
   - ¿Escala correctamente?
   - ¿Respeta datos personales?

---

## B. Biblioteca de prompts

Incluir prompts para:

1. Soporte al cliente.
2. Ventas y objeciones.
3. Leads y calificación.
4. Contenido para redes.
5. Emails de seguimiento.
6. Onboarding de clientes.
7. Resúmenes de reuniones.
8. Operaciones internas.
9. FAQ de producto.
10. Reembolsos y escalación.

---

## C. Herramientas recomendadas

### Modelos / chatbots
- ChatGPT.
- Claude.
- Gemini.
- Perplexity.
- Copilot.

### Automatización no-code
- Zapier.
- Make.
- n8n.
- Airtable Automations.
- Google Forms + Sheets + Apps Script.
- Notion Automations.

### Interfaces de chat / asistentes
- Botpress.
- Voiceflow.
- Chatbase.
- Tidio.
- Intercom.
- WhatsApp Business API con plataformas como WATI o Treble, según presupuesto.

### Base de conocimiento
- Notion.
- Google Docs.
- Airtable.
- Zendesk.
- Help Scout.

### Métricas simples
- Tiempo de respuesta.
- Número de preguntas resueltas sin humano.
- Tasa de escalación.
- Errores detectados.
- Satisfacción del cliente.

---

## D. Checklist de privacidad y seguridad

1. No subir datos personales sensibles.
2. Anonimizar ejemplos.
3. No compartir contraseñas.
4. No usar IA para decisiones legales o financieras finales.
5. Tener revisión humana.
6. Definir cuándo escalar.
7. Guardar prompts y versiones.
8. Revisar políticas de la herramienta.
9. Limitar acceso interno.
10. Auditar respuestas antes de lanzar.

---

## E. Plan de 7 días

| Día | Acción |
|---|---|
| 1 | Elegir una tarea concreta |
| 2 | Escribir contexto, reglas y tono |
| 3 | Crear prompt maestro |
| 4 | Testear 10 preguntas reales |
| 5 | Corregir errores y añadir escalación |
| 6 | Usarlo con supervisión humana |
| 7 | Medir resultados y decidir siguiente iteración |

---

## F. Recursos extra

- Slides del workshop.
- Video corto de la demo, si se grabó.
- Carpeta compartida.
- QR con todos los recursos.
- Lista de lecturas cortas:
  - Guía de prompts.
  - Ejemplos de automatización.
  - Checklist de IA responsable.
- Comunidad o canal de seguimiento, si aplica.

---

# 6. Slide count estimado por sección

| Sección | Slides |
|---|---:|
| Portada y agenda | 2 |
| Bienvenida y activación | 2 |
| Por qué un asistente de IA | 6 |
| Anatomía del asistente | 6 |
| Demo en vivo | 4 |
| Break | 1 |
| Ejercicio principal | 6 |
| Testeo y iteración | 3 |
| Show & tell | 2 |
| Cierre y plan de 7 días | 4 |
| **Total** | **36** |

**Recomendación:**  
Mantener máximo 34–36 slides para 3 horas.  
Si se quiere aún más energía, reducir a 28–30 slides y dejar más tiempo a práctica.

---

# 7. Resumen operativo para el facilitador

## Antes
- Preparar encuesta.
- Imprimir Assistant Canvas.
- Preparar demo.
- Probar Wi-Fi y herramientas.
- Definir co-facilitador si hay más de 20 personas.
- Preparar QR de recursos.

## Durante
- Controlar tiempos.
- Insistir en una sola tarea.
- No dejar que el ejercicio se vuelva conversación libre.
- Mostrar errores como parte del aprendizaje.
- Recoger 3 casos para show & tell.
- Cerrar con compromiso de 7 días.

## Después
- Enviar recursos.
- Compartir fotos o ejemplos anonimizados.
- Invitar a sesión de seguimiento.
- Recoger feedback:
  - ¿Qué fue útil?
  - ¿Qué faltó?
  - ¿Qué construirán esta semana?

---

# 8. Mensaje central del workshop

**“No necesitas ser técnico para construir un asistente de IA. Necesitas una tarea clara, un buen prompt, reglas de seguridad y pruebas reales.”**