# GPT-5.6 Terra — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 50.592s | tokens_per_second: 124.1
- input_tokens: 186 | output_tokens: 6281
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y un ejercicio práctico.

## Respuesta completa

# Workshop presencial (3 horas)
# **“Construye tu Asistente de IA para tu Startup – Workshop Práctico”**

**Audiencia:** Emprendedores early-stage no técnicos  
**Participantes:** 20–30 personas  
**Formato:** Presencial, práctico, con laptop y trabajo individual o en parejas  
**Resultado esperado:** Cada participante sale con una primera versión funcional de un asistente de IA para una tarea real de su startup, más un plan para probarlo durante la semana.

> **Principio del workshop:** No vamos a “hablar sobre IA” durante tres horas. Vamos a construir, probar y mejorar un asistente que pueda ahorrar tiempo en una tarea concreta del negocio.

---

## 1. Agenda detallada con tiempos (180 minutos)

| Hora | Duración | Bloque | Resultado |
|---|---:|---|---|
| 0:00–0:10 | 10 min | Bienvenida, contexto y reglas del juego | Participantes alineados y conectados a la herramienta |
| 0:10–0:25 | 15 min | ¿Qué puede hacer un asistente de IA en una startup? | Identifican casos de uso realistas |
| 0:25–0:40 | 15 min | Elige una tarea que valga la pena automatizar | Cada persona define su caso de uso |
| 0:40–0:55 | 15 min | Anatomía de un buen asistente: el framework | Aprenden una estructura simple para dar instrucciones |
| 0:55–1:05 | 10 min | Demo en vivo: de cero a asistente útil | Ven el proceso completo en acción |
| 1:05–1:15 | 10 min | Pausa / networking | Descanso y resolución de bloqueos técnicos |
| 1:15–1:35 | 20 min | Ejercicio 1: Diseña el “cerebro” de tu asistente | Completan el canvas del asistente |
| 1:35–2:05 | 30 min | Ejercicio 2: Construye tu asistente | Crean una primera versión funcional |
| 2:05–2:30 | 25 min | Ejercicio 3: Prueba, rompe y mejora | Iteran su asistente con casos reales |
| 2:30–2:50 | 20 min | Galería de asistentes y feedback entre pares | Reciben feedback y nuevas ideas |
| 2:50–3:00 | 10 min | Cierre: plan de acción de 7 días | Se comprometen con una prueba concreta post-workshop |

---

# 2. Materiales necesarios y preparación previa

## Para participantes

### Obligatorio
- Laptop con batería cargada y cargador.
- Acceso a Wi-Fi estable.
- Cuenta activa en una herramienta de IA generativa:
  - ChatGPT, Claude, Gemini, Copilot u otra equivalente.
- Información básica de su startup:
  - Qué problema resuelve.
  - Para quién.
  - Producto o servicio.
  - Tono de comunicación.
  - Ejemplos de contenido, mensajes, FAQs o documentos existentes.

### Recomendado
- 2–3 ejemplos reales de tareas repetitivas que hacen semanalmente.
- Un documento corto para usar como contexto:
  - Descripción de producto.
  - Pitch deck.
  - Preguntas frecuentes.
  - Guion de ventas.
  - Mensajes de clientes.
  - Manual de onboarding.
- Audífonos, si habrá recursos en video o demos individuales.

---

## Para el facilitador: preparar antes

### Espacio y logística
- Sala con mesas para trabajar en parejas o grupos de 3.
- Proyector, pantalla y adaptadores.
- Wi-Fi probado con anticipación.
- Extensiones eléctricas suficientes.
- Pizarra o rotafolio.
- Post-its, marcadores y hojas A4.
- Un QR visible con todos los recursos del workshop.

### Recursos digitales
Preparar una carpeta compartida en Google Drive, Notion o similar con:

1. **Asistente Canvas** imprimible y digital.
2. **Plantilla de prompt maestro**.
3. **Biblioteca de casos de uso para startups**.
4. **Checklist de prueba y mejora**.
5. **Ejemplos de asistentes listos para copiar y adaptar**.
6. **Guía de privacidad y uso responsable de IA**.
7. Links de acceso a las herramientas sugeridas.

### Preparar demos
Tener listos al menos 3 asistentes de ejemplo:

1. **Asistente de investigación de clientes**
   - Convierte entrevistas en insights, pain points y oportunidades.

2. **Asistente de ventas**
   - Crea mensajes de outreach, follow-ups y respuestas a objeciones.

3. **Asistente de contenido**
   - Genera posts de LinkedIn, emails, guiones de video o calendario de contenido.

### Plan B técnico
No todos tendrán cuentas pagas ni las mismas funciones. Por eso, preparar dos rutas:

- **Ruta A:** Crear un asistente personalizado si la plataforma lo permite.
- **Ruta B:** Crear un “prompt maestro” reutilizable en un chat normal.

> El objetivo no depende de pagar una suscripción: todos deben salir con un asistente que puedan usar desde el día siguiente.

---

# 3. Desarrollo por bloques

---

## Bloque 1. Bienvenida, contexto y reglas del juego
**Duración:** 10 minutos  
**Tipo de dinámica:** Charla breve + interacción rápida  
**Slides estimados:** 2–3

### Objetivo
Instalar energía, alinear expectativas y asegurar que todos estén listos técnicamente para construir.

### Dinámica
1. Bienvenida energética.
2. Pregunta a mano alzada:
   - “¿Quién ya usa IA al menos una vez por semana?”
   - “¿Quién siente que usa IA, pero aún no logra resultados consistentes?”
3. Explicar el resultado esperado:
   - “Hoy no vienen a aprender prompts bonitos. Vienen a construir un colaborador digital para una tarea concreta de su startup.”
4. Compartir reglas del juego:
   - Trabajar sobre un problema real.
   - Hacer, no solo escuchar.
   - Probar antes de juzgar.
   - No subir información confidencial, datos personales de clientes, contraseñas ni información financiera sensible.

### Key takeaway
**La IA no reemplaza la estrategia de una startup; acelera la ejecución de tareas repetibles cuando le damos buen contexto e instrucciones claras.**

---

## Bloque 2. ¿Qué puede hacer un asistente de IA en una startup?
**Duración:** 15 minutos  
**Tipo de dinámica:** Charla breve + discusión  
**Slides estimados:** 4–5

### Objetivo
Ayudar a los participantes a distinguir entre usos “interesantes” y usos realmente útiles para una startup early-stage.

### Dinámica
Presentar una definición simple:

> **Un asistente de IA es una herramienta configurada para cumplir una función específica, con un contexto, instrucciones y formato de respuesta definidos.**

Mostrar casos de uso por área:

| Área | Ejemplos de asistentes |
|---|---|
| Clientes | Sintetizador de entrevistas, analista de feedback, creador de encuestas |
| Ventas | Generador de prospectos, redactor de outreach, asistente de follow-up |
| Marketing | Creador de contenido, editor de tono, generador de campañas |
| Producto | Generador de user stories, organizador de feedback, creador de FAQs |
| Operaciones | Documentador de procesos, resumen de reuniones, asistente de onboarding |
| Fundraising | Revisor de pitch, preparador de preguntas de inversionistas, redactor de updates |

### Pregunta de discusión
“¿Qué tarea te quita tiempo cada semana, pero no necesariamente requiere que tú la hagas desde cero?”

### Key takeaway
**El mejor primer asistente no es el más sofisticado: es el que resuelve una tarea frecuente, tediosa y de alto valor para el equipo.**

---

## Bloque 3. Elige una tarea que valga la pena automatizar
**Duración:** 15 minutos  
**Tipo de dinámica:** Ejercicio individual + conversación en parejas  
**Slides estimados:** 3–4

### Objetivo
Que cada participante seleccione un problema concreto y acotado para construir durante el workshop.

### Dinámica
Entregar o proyectar una matriz simple para elegir el caso de uso:

| Pregunta | Sí / No |
|---|---|
| ¿Hago esta tarea al menos una vez por semana? | |
| ¿Me toma más de 20 minutos? | |
| ¿Sigue pasos relativamente repetibles? | |
| ¿Tengo ejemplos o información para enseñarle a la IA? | |
| ¿Puedo revisar el resultado antes de usarlo? | |

Si una tarea tiene 4 o 5 respuestas “sí”, es una buena candidata.

### Ejemplos de tareas adecuadas
- Convertir notas de entrevistas en aprendizajes accionables.
- Redactar emails de seguimiento comercial.
- Crear contenido a partir de una idea o una conversación.
- Responder preguntas frecuentes de clientes.
- Preparar resúmenes de reuniones.
- Revisar un pitch o propuesta comercial.
- Generar descripciones de producto.

### Ejemplos de tareas no recomendadas para el primer asistente
- “Que maneje todo mi marketing.”
- “Que consiga inversión.”
- “Que decida mi estrategia.”
- “Que responda automáticamente a todos mis clientes sin supervisión.”
- “Que construya mi producto completo.”

### Entregable
Cada participante completa esta frase:

> “Voy a construir un asistente que ayude a **[tipo de usuario]** a **[tarea específica]**, para lograr **[resultado medible o deseado]**.”

### Key takeaway
**Un asistente útil empieza con una tarea específica, no con una ambición gigante.**

---

## Bloque 4. Anatomía de un buen asistente: el framework
**Duración:** 15 minutos  
**Tipo de dinámica:** Charla práctica + mini-ejemplo  
**Slides estimados:** 5–6

### Objetivo
Enseñar una estructura simple para diseñar instrucciones consistentes sin necesidad de saber programar.

### Dinámica
Presentar el framework **ROL-OBJETIVO-CONTEXTO-PROCESO-FORMATO-LÍMITES**.

### Framework para crear el asistente

1. **Rol:** ¿Quién es el asistente?
   - “Eres un asistente de investigación de clientes para una startup B2B SaaS.”

2. **Objetivo:** ¿Qué resultado debe producir?
   - “Tu objetivo es analizar entrevistas y detectar patrones, pains y oportunidades.”

3. **Contexto:** ¿Qué necesita saber sobre la startup?
   - Cliente ideal, producto, etapa, industria, tono, propuesta de valor.

4. **Proceso:** ¿Qué pasos debe seguir?
   - Leer información.
   - Hacer preguntas si falta contexto.
   - Analizar.
   - Priorizar.
   - Entregar recomendaciones.

5. **Formato:** ¿Cómo debe responder?
   - Tabla, checklist, email, bullets, plan semanal, guion, etc.

6. **Límites:** ¿Qué no debe hacer?
   - No inventar información.
   - No asumir datos no confirmados.
   - No dar asesoría legal, médica o financiera como si fuera profesional.
   - Señalar explícitamente cuando no tenga suficiente información.

### Mini ejemplo
> “Eres un asistente de ventas para una startup que vende software de gestión para pequeñas empresas en México. Tu trabajo es redactar mensajes de LinkedIn y emails breves, cercanos y personalizados para prospectos. Antes de escribir, pide el perfil del prospecto, el problema que podría tener y la oferta relevante. Entrega tres versiones: directa, consultiva y casual. No inventes datos sobre la empresa del prospecto.”

### Key takeaway
**La calidad de un asistente depende menos de una frase mágica y más de darle contexto, proceso, formato y límites claros.**

---

## Bloque 5. Demo en vivo: de cero a asistente útil
**Duración:** 10 minutos  
**Tipo de dinámica:** Demo en vivo  
**Slides estimados:** 2–3

### Objetivo
Mostrar que el proceso es accesible para personas no técnicas y que la primera versión no tiene que ser perfecta.

### Dinámica
Construir frente al grupo un asistente sencillo, por ejemplo:

**“Asistente de Follow-up Comercial”**

Mostrar el proceso:
1. Definir su función.
2. Agregar contexto de la startup.
3. Establecer el tono.
4. Indicar el formato de salida.
5. Probarlo con una situación real.
6. Detectar una respuesta mediocre.
7. Mejorar la instrucción.

### Mensaje clave durante la demo
“No esperamos que funcione perfecto en el primer intento. Construir con IA es un ciclo: instruir → probar → detectar fallas → ajustar.”

### Key takeaway
**Un asistente no se “termina” de una vez: se entrena mediante iteración y pruebas reales.**

---

## Bloque 6. Pausa / networking
**Duración:** 10 minutos  
**Tipo de dinámica:** Descanso + soporte técnico  
**Slides estimados:** 1

### Objetivo
Dar espacio para recargar energía y resolver barreras de acceso antes del bloque de construcción.

### Dinámica
- Pausa activa.
- El facilitador y apoyos técnicos verifican:
  - Accesos a plataformas.
  - Conexión a Wi-Fi.
  - Participantes que aún no eligieron caso de uso.
- Invitar a conversar con alguien que esté construyendo un asistente en otra área.

### Key takeaway
**La mejor inspiración suele venir de ver cómo otros fundadores están resolviendo problemas similares de manera distinta.**

---

## Bloque 7. Ejercicio 1: Diseña el “cerebro” de tu asistente
**Duración:** 20 minutos  
**Tipo de dinámica:** Ejercicio individual o en parejas  
**Slides estimados:** 2–3

### Objetivo
Convertir la idea seleccionada en una especificación clara antes de abrir la herramienta de IA.

### Dinámica
Cada participante completa el **Asistente Canvas**.

### Asistente Canvas

**1. Nombre del asistente**  
Ejemplo: “Sofía, mi asistente de entrevistas de clientes”.

**2. Tarea principal que resuelve**  
¿Qué debe hacer exactamente?

**3. Usuario final**  
¿Quién lo usará: founder, ventas, marketing, customer success, equipo completo?

**4. Contexto de mi startup**
- Qué vendemos.
- A quién.
- Problema que resolvemos.
- País/mercado.
- Etapa.
- Tono de marca.

**5. Inputs que recibirá**
- Notas de reuniones.
- Brief de contenido.
- Perfil de prospecto.
- Datos de entrevista.
- Información de producto.

**6. Output esperado**
- Tabla.
- Email.
- Resumen.
- Priorización.
- Guion.
- Checklist.
- Plan de acción.

**7. Reglas y límites**
- Qué debe preguntar antes de responder.
- Qué nunca debe inventar.
- Qué datos no debe usar.
- Cuándo debe decir “necesito más información”.

**8. Cómo sabré que funciona**
- Ahorra 30 minutos por tarea.
- Mantiene el tono de marca.
- Produce resultados editables.
- Reduce el tiempo de respuesta.
- Genera ideas accionables.

### Rol del facilitador
Circular por las mesas y hacer preguntas de precisión:
- “¿Qué input exacto le vas a dar?”
- “¿Qué salida quieres recibir?”
- “¿Cómo sabrás si la respuesta es buena?”
- “¿Qué debería hacer cuando no tenga información suficiente?”

### Key takeaway
**Si no puedes explicar claramente qué entra y qué sale de tu asistente, todavía no estás listo para construirlo.**

---

## Bloque 8. Ejercicio 2: Construye tu asistente
**Duración:** 30 minutos  
**Tipo de dinámica:** Construcción práctica guiada  
**Slides estimados:** 3–4

### Objetivo
Crear una primera versión funcional del asistente en la herramienta elegida.

### Dinámica
Los participantes usan su Canvas para redactar y cargar su prompt maestro.

### Plantilla de prompt maestro

```text
Eres [NOMBRE DEL ASISTENTE], un asistente especializado en [FUNCIÓN].

Tu objetivo es ayudar a [USUARIO] a [RESULTADO ESPECÍFICO].

Contexto de la startup:
- Startup: [NOMBRE]
- Producto/servicio: [DESCRIPCIÓN]
- Cliente ideal: [ICP]
- Mercado/país: [MERCADO]
- Tono de comunicación: [TONO]
- Información relevante: [DATOS / DOCUMENTOS / EJEMPLOS]

Cuando recibas una solicitud:
1. Primero identifica si tienes suficiente información.
2. Si falta información crítica, haz máximo [3] preguntas concretas.
3. Sigue este proceso: [PASOS QUE DEBE SEGUIR].
4. Entrega el resultado en este formato: [FORMATO].
5. Prioriza respuestas claras, accionables y adaptadas al contexto de la startup.

Reglas:
- No inventes datos, citas, métricas ni información sobre clientes.
- Si no estás seguro, dilo explícitamente.
- No incluyas información confidencial no proporcionada.
- Mantén el tono [TONO].
- Antes de finalizar, verifica que el resultado sea útil para [OBJETIVO].
```

### Recomendación de construcción
Los participantes pueden crear:

- Un asistente personalizado, si su herramienta lo permite.
- Un chat con el prompt maestro fijado o guardado.
- Un documento plantilla donde copian el prompt cada vez que lo necesiten.

### Hito mínimo del bloque
Al finalizar, cada persona debe tener:
- Un prompt maestro listo.
- Un nombre para su asistente.
- Al menos una interacción realizada.
- Un primer output generado.

### Key takeaway
**No necesitas programar para crear valor: una buena configuración y un flujo de trabajo claro ya pueden ahorrar horas a una startup.**

---

## Bloque 9. Ejercicio 3: Prueba, rompe y mejora
**Duración:** 25 minutos  
**Tipo de dinámica:** Prueba guiada + iteración  
**Slides estimados:** 3–4

### Objetivo
Evitar que los participantes se queden con una primera versión “bonita” pero poco útil. Deben evaluar su asistente con criterio.

### Dinámica
Cada participante prueba su asistente con tres escenarios:

### Prueba 1: Caso ideal
Dar al asistente información completa y verificar si entrega lo esperado.

### Prueba 2: Caso incompleto
Dar información insuficiente y comprobar si hace buenas preguntas antes de responder.

### Prueba 3: Caso difícil o ambiguo
Probar una situación real donde podría confundirse, inventar datos o responder de forma genérica.

### Checklist de evaluación

| Criterio | Pregunta |
|---|---|
| Utilidad | ¿Me ahorra tiempo o mejora mi resultado? |
| Contexto | ¿Entiende mi negocio y mi cliente? |
| Precisión | ¿Evita inventar información? |
| Formato | ¿Entrega una respuesta fácil de usar? |
| Tono | ¿Suena como mi startup? |
| Autonomía | ¿Sabe qué preguntar cuando le falta información? |
| Acción | ¿La respuesta me permite hacer algo concreto? |

### Iteración
Cada participante debe mejorar al menos uno de estos elementos:
- Agregar contexto.
- Cambiar el formato de salida.
- Especificar el proceso.
- Añadir un ejemplo de respuesta ideal.
- Establecer mejores límites.
- Mejorar las preguntas iniciales del asistente.

### Key takeaway
**La prueba no busca demostrar que tu asistente es perfecto; busca encontrar rápidamente dónde falla para hacerlo más útil.**

---

## Bloque 10. Galería de asistentes y feedback entre pares
**Duración:** 20 minutos  
**Tipo de dinámica:** Show & tell + feedback en parejas o grupos de 3  
**Slides estimados:** 2–3

### Objetivo
Generar aprendizaje colectivo, visibilizar casos de uso y recibir feedback de alguien que representa a un “usuario fresco”.

### Dinámica
Formar grupos de 3 personas.

Cada persona tiene:
- **3 minutos** para mostrar su asistente.
- **2 minutos** para recibir feedback.

### Guía para mostrar el asistente
1. ¿Qué problema resuelve?
2. ¿Para quién?
3. ¿Qué input recibe?
4. ¿Qué output entrega?
5. ¿Qué fue lo más difícil de diseñar?
6. ¿Qué mejorarás después del workshop?

### Guía de feedback entre pares
- “Lo más valioso de tu asistente es…”
- “Me gustaría que hiciera también…”
- “No entendí cómo manejaría…”
- “Una prueba que te recomiendo hacer es…”

### Cierre grupal
Pedir 3–4 voluntarios para mostrar su asistente al grupo completo en 60 segundos.

### Key takeaway
**El feedback más útil no es “qué buena idea”, sino una prueba concreta que revela cómo hacer el asistente más usable.**

---

## Bloque 11. Cierre: plan de acción de 7 días
**Duración:** 10 minutos  
**Tipo de dinámica:** Reflexión individual + compromiso público  
**Slides estimados:** 2–3

### Objetivo
Convertir el workshop en adopción real, no en una herramienta abandonada en una pestaña del navegador.

### Dinámica
Cada participante completa una tarjeta de compromiso:

> Durante los próximos 7 días, usaré mi asistente para: **[tarea]**  
> Lo probaré al menos: **[X] veces**  
> Mediré: **[tiempo ahorrado / calidad / velocidad / resultados]**  
> Mi siguiente mejora será: **[acción concreta]**

Pedir que compartan su compromiso con la persona sentada a su lado.

### Cierre del facilitador
Mensaje final:

> “Tu primer asistente no necesita ser impresionante. Necesita ser útil. Si te ahorra 30 minutos a la semana, te ayuda a responder mejor a un cliente o te permite aprender más rápido, ya está generando valor.”

### Key takeaway
**La ventaja no la tendrá quien pruebe más herramientas de IA, sino quien convierta una tarea repetitiva en un sistema útil y repetible.**

---

# 4. Ejercicio principal del workshop

## Nombre
# **Construye tu Primer Asistente Operativo de IA**

### Objetivo del ejercicio
Que cada participante cree un asistente que ejecute una tarea específica de su startup usando información, instrucciones y formatos definidos por ellos mismos.

### Duración total
**75 minutos**
- 20 min: Diseño con Canvas.
- 30 min: Construcción.
- 25 min: Prueba e iteración.

### Entregable final
Cada participante sale con:

1. Un caso de uso claro.
2. Un prompt maestro reutilizable.
3. Un asistente configurado o chat estructurado.
4. Al menos tres pruebas realizadas.
5. Una mejora aplicada.
6. Un plan de uso para los siguientes 7 días.

---

## Ejemplos de asistentes que pueden construir

### Para founders
- Asistente para preparar updates semanales de startup.
- Asistente para convertir notas de reuniones en tareas y decisiones.
- Asistente para revisar pitches y detectar preguntas difíciles de inversionistas.

### Para marketing
- Asistente de creación de contenido para LinkedIn o Instagram.
- Asistente que convierte una entrevista o webinar en piezas de contenido.
- Asistente de tono de marca para revisar copies.

### Para ventas
- Asistente de mensajes de prospección.
- Asistente de follow-up post-demo.
- Asistente para responder objeciones comerciales.

### Para producto y clientes
- Asistente que resume entrevistas de usuarios.
- Asistente que clasifica feedback de clientes.
- Asistente para transformar problemas de clientes en hipótesis de producto.

### Para operaciones
- Asistente de documentación de procesos.
- Asistente de onboarding para nuevos miembros del equipo.
- Asistente para redactar SOPs o checklists operativos.

---

# 5. Recursos para llevar a casa

Entregar mediante QR y carpeta digital.

## Plantillas
1. **Asistente Canvas** en Google Docs, Notion y PDF.
2. **Prompt maestro editable**.
3. **Checklist para probar asistentes de IA**.
4. **Guía de mejora en 15 minutos**.
5. **Plantilla de biblioteca de prompts del equipo**.
6. **Plantilla de documentación de procesos para IA**.

## Biblioteca de prompts
Incluir prompts iniciales para:
- Análisis de entrevistas.
- Seguimiento de ventas.
- Creación de contenido.
- Preparación de pitch.
- Síntesis de reuniones.
- Investigación de competencia.
- Generación de FAQs.
- Documentación de procesos.

## Guía de uso responsable
Una hoja de una página con reglas simples:

- No subir contraseñas, datos bancarios o información personal sensible.
- No compartir bases de datos de clientes sin revisar políticas y permisos.
- Verificar siempre datos, citas, métricas y afirmaciones.
- Mantener revisión humana antes de enviar contenido a clientes.
- No usar IA como sustituto de asesoría legal, financiera o médica profesional.
- Definir qué información de la startup sí y no puede utilizarse en herramientas externas.

## Reto post-workshop: “7 días con tu asistente”
Proponer un reto sencillo:

- Día 1: úsalo en una tarea real.
- Día 2: registra qué falló.
- Día 3: agrega mejor contexto.
- Día 4: prueba otro formato de respuesta.
- Día 5: comparte el asistente con un compañero.
- Día 6: mide tiempo ahorrado.
- Día 7: decide si lo mantienes, mejoras o descartas.

---

# 6. Slide count estimado por sección

| Sección | Slides estimados |
|---|---:|
| Portada, objetivo y reglas del workshop | 2–3 |
| Casos de uso de IA para startups | 4–5 |
| Selección de tarea / matriz de priorización | 3–4 |
| Framework de diseño de asistentes | 5–6 |
| Demo en vivo | 2–3 |
| Pausa | 1 |
| Ejercicio: Asistente Canvas | 2–3 |
| Construcción del asistente / prompt maestro | 3–4 |
| Pruebas, evaluación e iteración | 3–4 |
| Galería de asistentes y feedback | 2–3 |
| Cierre y reto de 7 días | 2–3 |
| **Total estimado** | **29–39 slides** |

> Recomendación: Mantener las slides visuales y ligeras. El protagonismo debe estar en la construcción en vivo, los templates y el trabajo de los participantes, no en una presentación larga.

---

# Estructura sugerida del deck

1. Portada.
2. Qué construirán hoy.
3. Reglas del juego.
4. Qué es un asistente de IA.
5. Casos de uso por área.
6. Qué tareas sí conviene automatizar.
7. Matriz de selección de caso de uso.
8. Instrucción del primer ejercicio.
9. Framework ROL-OBJETIVO-CONTEXTO-PROCESO-FORMATO-LÍMITES.
10. Ejemplo de prompt malo vs. prompt útil.
11. Demo paso a paso.
12. Instrucciones del Canvas.
13. Timer de ejercicio.
14. Plantilla de prompt maestro.
15. Instrucciones de construcción.
16. Ejemplos de formatos de salida.
17. Checklist de prueba.
18. Ejemplos de pruebas difíciles.
19. Guía de feedback entre pares.
20. Reto de 7 días.
21. Recursos, QR y cierre.

---

## Frase de cierre sugerida

> “No necesitas convertirte en experto técnico para aprovechar IA. Necesitas identificar dónde tu startup pierde tiempo, darle a la IA un trabajo claro y construir el hábito de probar, medir y mejorar.”