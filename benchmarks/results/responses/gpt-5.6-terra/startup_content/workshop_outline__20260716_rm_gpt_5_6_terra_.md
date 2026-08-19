# GPT-5.6 Terra — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 52.691s | tokens_per_second: 117.0
- input_tokens: 186 | output_tokens: 6165
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y extremadamente útil para emprendedores no técnicos, proporcionando una agenda detallada y materiales necesarios, aunque podría profundizar un poco más en ejemplos específicos.

## Respuesta completa

# Workshop presencial (3 horas)
# **“Construye tu Asistente de IA para tu Startup – Workshop Práctico”**

**Audiencia:** 20–30 emprendedores early-stage no técnicos  
**Modalidad:** Presencial, práctico, individual con momentos de trabajo en parejas  
**Resultado esperado:** Cada participante sale con un asistente de IA funcional para una tarea concreta de su startup, un prompt reutilizable y un plan de mejora de 7 días.

> **Principio del workshop:** No vamos a “hablar sobre IA”. Vamos a construir algo útil antes de salir de la sala.

---

## 1. Agenda detallada con tiempos (180 minutos)

| Hora | Bloque | Duración | Formato |
|---|---:|---:|---|
| 00:00–00:10 | Bienvenida: de la idea al asistente | 10 min | Charla + activación |
| 00:10–00:25 | Qué puede (y qué no puede) hacer un asistente de IA | 15 min | Charla + ejemplos |
| 00:25–00:40 | Elige un problema real de tu startup | 15 min | Ejercicio individual |
| 00:40–01:00 | La receta de un buen asistente: rol, contexto, tarea y formato | 20 min | Charla + mini ejercicio |
| 01:00–01:15 | Demo en vivo: construir un asistente desde cero | 15 min | Demo |
| 01:15–01:25 | Pausa | 10 min | Break |
| 01:25–01:50 | Diseña tu asistente con el Canvas | 25 min | Ejercicio individual + apoyo |
| 01:50–02:20 | Construcción: crea la primera versión funcional | 30 min | Trabajo práctico |
| 02:20–02:40 | Prueba, corrige e itera | 20 min | Ejercicio práctico |
| 02:40–02:55 | Feedback entre pares: “Prueba mi asistente” | 15 min | Trabajo en parejas |
| 02:55–03:00 | Cierre, compromisos y próximos pasos | 5 min | Cierre grupal |

---

# 2. Materiales necesarios y preparación previa

## Para el facilitador

### Tecnología
- Proyector o pantalla grande.
- Computadora con acceso a internet.
- Micrófono de solapa o mano si la sala es grande.
- Wi-Fi estable para 30 personas.
- **Plan B de conectividad:** hotspot móvil o red alternativa.
- Cable HDMI, adaptadores USB-C/HDMI y alargadores eléctricos.
- Cronómetro visible o timer proyectado.

### Plataformas recomendadas
Elegir **una plataforma principal** para evitar confusión durante el workshop:

- ChatGPT (gratuito o Plus)
- Claude
- Gemini
- Microsoft Copilot

**Recomendación práctica:** usar ChatGPT o Claude como plataforma principal, pero enseñar una estructura de prompt que funcione en cualquier herramienta.

> No es indispensable que todos creen un GPT personalizado. El objetivo es que todos puedan crear un “asistente” mediante un prompt maestro reutilizable, incluso con una cuenta gratuita.

### Material impreso o digital
- 30 copias del **Canvas de Asistente de IA** (1–2 páginas).
- 30 copias de la hoja de **pruebas y mejora**.
- Post-its de 2 colores.
- Marcadores gruesos.
- Lapiceros.
- Tarjetas con ejemplos de casos de uso.
- Código QR a una carpeta con recursos, plantillas y prompts.
- Lista visible con la red Wi-Fi y contraseña.

### Preparación de contenido
Tener listos:
- Una demo funcional de un asistente de IA.
- 2–3 ejemplos latinoamericanos y cercanos a startups early-stage.
- Un prompt “malo” y uno “bueno” para comparar.
- Un documento de contexto de ejemplo: descripción de startup, perfil de cliente, FAQs o pitch.
- Un backup de la demo en screenshots o video corto por si falla internet.

---

## Para participantes

Solicitar antes del workshop que traigan:

- Laptop cargada y cargador.
- Cuenta creada en al menos una herramienta de IA generativa:
  - ChatGPT, Claude, Gemini o Copilot.
- Descripción breve de su startup, aunque sea preliminar:
  - Qué hacen.
  - Para quién.
  - Problema que resuelven.
  - Producto o servicio.
- Si tienen: pitch deck, landing page, FAQs, notas de entrevistas a clientes o documentos de ventas.

> **Importante:** no necesitan saber programar, usar APIs ni tener experiencia previa con IA.

---

# 3. Desarrollo por bloque

---

## Bloque 1. Bienvenida: de la idea al asistente
**Duración:** 10 minutos  
**Formato:** Charla breve + activación grupal  
**Slides estimadas:** 3

### Objetivo
Crear energía, alinear expectativas y dejar claro que el resultado será práctico: un asistente funcional al final de las 3 horas.

### Dinámica
1. Bienvenida rápida.
2. Pregunta de activación a mano alzada:
   - “¿Quién ya usó ChatGPT, Claude o Gemini esta semana?”
   - “¿Quién siente que usa IA, pero todavía sin un sistema claro?”
3. Mostrar el objetivo final del día:
   - “Hoy saldrás con un asistente que te ahorre tiempo en una tarea repetitiva de tu startup.”
4. Presentar la regla del workshop:
   - **Menos perfección, más prototipo.**
   - **No construirás ‘el asistente definitivo’; construirás una primera versión útil.**

### Key takeaway
> Un asistente de IA no es magia ni una app compleja: es una forma estructurada de delegar una tarea repetitiva con contexto, criterios y un formato de salida claro.

---

## Bloque 2. Qué puede (y qué no puede) hacer un asistente de IA
**Duración:** 15 minutos  
**Formato:** Charla dinámica + ejemplos  
**Slides estimadas:** 5

### Objetivo
Bajar la IA a casos de uso reales para emprendedores y establecer límites responsables.

### Dinámica
Presentar la idea de que un asistente de IA funciona mejor cuando se usa para tareas como:

- Crear borradores de contenido para LinkedIn, Instagram o newsletters.
- Convertir notas de entrevistas en insights de clientes.
- Preparar respuestas para leads y clientes.
- Crear un primer borrador de pitch, propuesta comercial o email.
- Organizar ideas de producto.
- Generar guiones para ventas, demos o videos.
- Diseñar FAQs y mensajes de onboarding.
- Analizar feedback cualitativo de usuarios.

Luego contrastar con tareas donde **no debe actuar sin supervisión**:

- Tomar decisiones legales, contables o médicas.
- Inventar datos de mercado o métricas.
- Enviar mensajes automáticamente sin revisión.
- Compartir información confidencial en herramientas no aprobadas.
- Reemplazar la validación con clientes reales.

### Ejemplos de asistentes
1. **Asistente de entrevistas de clientes:** convierte notas en dolores, deseos, objeciones y oportunidades.
2. **Asistente de contenido para founders:** crea posts en el tono del fundador, dirigidos a un ICP específico.
3. **Asistente de ventas:** transforma una descripción de prospecto en un email de outreach personalizado.
4. **Asistente de pitch:** ayuda a simplificar la propuesta de valor para clientes e inversionistas.

### Key takeaway
> La IA es especialmente valiosa para acelerar borradores, organizar información y reducir trabajo repetitivo. Pero el fundador sigue siendo responsable del criterio, la validación y la decisión final.

---

## Bloque 3. Elige un problema real de tu startup
**Duración:** 15 minutos  
**Formato:** Ejercicio individual + discusión breve  
**Slides estimadas:** 3

### Objetivo
Evitar que los participantes intenten construir un asistente “para todo” y enfocarlos en un problema concreto, frecuente y de alto valor.

### Dinámica
Cada participante completa una hoja o formulario con estas preguntas:

1. ¿Qué tarea repites cada semana?
2. ¿Qué tarea te quita tiempo, pero no requiere que la hagas desde cero cada vez?
3. ¿Qué tarea puede empezar con un borrador en vez de una respuesta perfecta?
4. ¿Qué información ya tienes disponible para ayudar a la IA?
5. ¿Qué resultado concreto te gustaría obtener en menos de 10 minutos?

### Filtro de priorización: “Fácil + frecuente + útil”
Pedir que evalúen cada idea del 1 al 5:

| Criterio | Pregunta |
|---|---|
| Frecuencia | ¿La haces al menos una vez por semana? |
| Tiempo | ¿Te toma más de 20 minutos? |
| Repetición | ¿Sigue una estructura similar cada vez? |
| Contexto disponible | ¿Tienes información para enseñarle a la IA? |
| Riesgo bajo | ¿Puedes revisar el resultado antes de usarlo? |

### Casos de uso sugeridos para quienes se bloqueen
- Crear posts de LinkedIn a partir de aprendizajes semanales.
- Resumir entrevistas a clientes.
- Redactar emails de seguimiento comercial.
- Crear respuestas a preguntas frecuentes.
- Generar propuestas comerciales iniciales.
- Preparar briefs para freelancers o agencias.
- Crear guiones de demos de producto.
- Convertir feedback de usuarios en hipótesis de producto.

### Key takeaway
> El mejor primer asistente no resuelve toda tu empresa: resuelve una tarea repetitiva, específica y valiosa.

---

## Bloque 4. La receta de un buen asistente: rol, contexto, tarea y formato
**Duración:** 20 minutos  
**Formato:** Charla + mini ejercicio guiado  
**Slides estimadas:** 6

### Objetivo
Enseñar una estructura simple y reutilizable para diseñar instrucciones claras.

### Dinámica
Presentar el framework **RCTA**:

### R — Rol
¿Quién debe ser el asistente?

Ejemplos:
- “Eres un estratega de contenido B2B para startups SaaS.”
- “Eres un asistente de investigación de clientes.”
- “Eres un copywriter especializado en ventas consultivas para pymes.”

### C — Contexto
¿Qué necesita saber sobre la startup, el cliente y el objetivo?

Ejemplos:
- Producto o servicio.
- Cliente ideal.
- Propuesta de valor.
- Tono de comunicación.
- País o mercado.
- Restricciones del negocio.
- Ejemplos de mensajes previos.

### T — Tarea
¿Qué debe hacer exactamente?

Ejemplos:
- “Convierte estas notas de entrevista en insights accionables.”
- “Crea tres versiones de un email de seguimiento.”
- “Genera cinco ideas de contenido basadas en esta conversación.”

### A — Aceptación / Formato de salida
¿Cómo debe verse una buena respuesta?

Ejemplos:
- Tabla con columnas específicas.
- Máximo 150 palabras.
- Incluir tres alternativas.
- Usar lenguaje simple.
- Terminar con preguntas pendientes.
- Indicar supuestos cuando falte información.

### Mini ejercicio
Mostrar dos prompts:

**Prompt débil:**  
> “Hazme un post para LinkedIn sobre mi startup.”

**Prompt mejorado:**  
> “Actúa como un estratega de contenido para founders B2B en Latinoamérica. Mi startup ayuda a restaurantes pequeños a reducir desperdicio de alimentos mediante predicción de demanda. Crea un post de LinkedIn de máximo 180 palabras dirigido a dueños de restaurantes. Usa un tono directo, práctico y no corporativo. El post debe comenzar con una observación provocadora, explicar un dolor concreto y cerrar con una pregunta para generar conversación. No inventes métricas.”

### Key takeaway
> Una buena instrucción no depende de “pedirle bonito” a la IA: depende de darle contexto, una tarea específica y criterios claros de éxito.

---

## Bloque 5. Demo en vivo: construir un asistente desde cero
**Duración:** 15 minutos  
**Formato:** Demo en vivo  
**Slides estimadas:** 3

### Objetivo
Mostrar que construir un asistente básico es accesible y que la primera versión puede hacerse en pocos minutos.

### Dinámica
El facilitador crea en vivo un asistente ejemplo.

### Ejemplo sugerido
**“Asistente de Insights de Clientes”**

Input:
- Notas de una entrevista con cliente.
- Transcripción corta o comentarios de usuarios.

Output:
- Problemas mencionados.
- Frases textuales relevantes.
- Objeciones.
- Motivaciones de compra.
- Hipótesis de producto.
- Preguntas para la próxima entrevista.

### Pasos de la demo
1. Abrir la herramienta de IA.
2. Pegar el prompt maestro.
3. Añadir contexto de una startup ficticia.
4. Ingresar una entrevista de ejemplo.
5. Revisar la primera respuesta.
6. Detectar un problema:
   - Muy genérico.
   - No separa hechos de suposiciones.
   - Falta una tabla.
7. Ajustar instrucciones.
8. Mostrar una segunda respuesta mejorada.

### Frase clave para reforzar
> “El primer resultado no es el producto final. Es una conversación de diseño con la IA.”

### Key takeaway
> Crear un asistente es un ciclo: instrucción → prueba → revisión → ajuste. La calidad aparece en la iteración, no en el primer prompt.

---

## Pausa
**Duración:** 10 minutos  
**Formato:** Break  
**Slides estimadas:** 1

Sugerencia: mantener proyectado un slide con:
- Wi-Fi.
- Código QR de recursos.
- Checklist para la siguiente parte.
- “Al volver, vas a construir tu asistente.”

---

## Bloque 6. Diseña tu asistente con el Canvas
**Duración:** 25 minutos  
**Formato:** Ejercicio individual + acompañamiento del facilitador  
**Slides estimadas:** 4

### Objetivo
Que cada participante diseñe las instrucciones de su asistente antes de abrir la herramienta.

### Dinámica
Entregar el **Canvas de Asistente de IA**.

## Canvas de Asistente de IA

### 1. Nombre del asistente
Ejemplos:
- Asistente de Contenido Founder-led.
- Analista de Entrevistas de Clientes.
- Copiloto de Ventas B2B.
- Asistente de Propuestas Comerciales.

### 2. Problema que resuelve
> “Me ayuda a convertir notas desordenadas de entrevistas en aprendizajes accionables.”

### 3. Usuario final
¿Quién lo usará?
- Founder.
- Equipo comercial.
- Marketing.
- Customer success.
- Operaciones.

### 4. Rol del asistente
> “Eres un investigador cualitativo de clientes para startups.”

### 5. Contexto de mi startup
- Qué hacemos.
- Para quién.
- Qué problema resolvemos.
- En qué mercado operamos.
- Diferenciadores.
- Tono de marca.

### 6. Input que recibirá
- Notas.
- Transcripción.
- Brief.
- Perfil de prospecto.
- Ideas sueltas.
- Datos de una reunión.

### 7. Output esperado
- Tabla.
- Email.
- Guion.
- Calendario de contenido.
- Resumen.
- Lista priorizada.
- Plan de acción.

### 8. Reglas y restricciones
- No inventar datos.
- Señalar cuando falte contexto.
- Usar lenguaje claro.
- Evitar jerga.
- Máximo 300 palabras.
- Hacer preguntas aclaratorias si falta información crítica.

### 9. Cómo sabré si funciona
> “Si me entrega un borrador que puedo revisar y usar en menos de 10 minutos.”

### Rol del facilitador
- Circular por la sala.
- Identificar participantes atascados.
- Ayudar a reducir asistentes demasiado amplios.
- Reforzar el principio: **una tarea, un resultado, una primera versión.**

### Key takeaway
> Antes de escribir un prompt, define el trabajo que quieres delegar y cómo se ve un buen resultado.

---

## Bloque 7. Construcción: crea la primera versión funcional
**Duración:** 30 minutos  
**Formato:** Trabajo práctico individual + soporte en sala  
**Slides estimadas:** 3

### Objetivo
Transformar el Canvas en un prompt maestro y probarlo con información real de la startup.

### Dinámica
Los participantes abren su herramienta de IA elegida y siguen estos pasos:

1. Copiar la plantilla de prompt maestro.
2. Completar el rol, contexto, tarea y formato.
3. Ingresar información real de su startup.
4. Probar con un caso real.
5. Guardar el prompt en un documento o en la funcionalidad de proyecto/GPT/instrucciones de la herramienta que utilicen.

## Plantilla de prompt maestro

```text
Actúa como [ROL DEL ASISTENTE].

Contexto de mi startup:
- Startup: [NOMBRE]
- Qué hacemos: [DESCRIPCIÓN]
- Cliente ideal: [CLIENTE]
- Problema que resolvemos: [PROBLEMA]
- Mercado o país: [MERCADO]
- Tono de comunicación: [TONO]
- Información adicional relevante: [CONTEXTO]

Tu tarea es:
[DESCRIBIR TAREA ESPECÍFICA]

Cuando recibas [TIPO DE INPUT], debes:
1. [PASO 1]
2. [PASO 2]
3. [PASO 3]

Entrega la respuesta en este formato:
[FORMATO ESPERADO]

Reglas:
- No inventes datos, métricas ni testimonios.
- Si falta información relevante, indica qué información falta.
- Diferencia entre hechos, hipótesis y recomendaciones.
- Usa lenguaje claro y accionable.
- [OTRA REGLA ESPECÍFICA]
```

### Apoyo para distintos niveles
Para quienes terminan rápido:
- Añadir ejemplos de “buenas respuestas”.
- Cargar documentos de contexto, si la plataforma lo permite.
- Crear un segundo modo de trabajo:
  - “Modo rápido”
  - “Modo estratégico”
- Pedirle al asistente que haga preguntas antes de responder.

Para quienes necesitan apoyo:
- Usar uno de los prompts base entregados.
- Completar solo los campos esenciales.
- Trabajar con un caso de uso sugerido.

### Key takeaway
> Ya tienes un asistente cuando puedes darle un input real y obtener un resultado que reduce tu tiempo de trabajo.

---

## Bloque 8. Prueba, corrige e itera
**Duración:** 20 minutos  
**Formato:** Ejercicio práctico guiado  
**Slides estimadas:** 4

### Objetivo
Enseñar a mejorar el asistente con pruebas simples, en lugar de asumir que una mala respuesta significa que “la IA no sirve”.

### Dinámica
Cada participante prueba su asistente con al menos dos inputs distintos.

### Checklist de evaluación
Pedir que califiquen cada respuesta del 1 al 5:

| Criterio | Pregunta |
|---|---|
| Relevancia | ¿Entendió el contexto de mi startup? |
| Utilidad | ¿Me ahorra trabajo real? |
| Precisión | ¿Evita inventar información? |
| Formato | ¿Entregó el resultado como lo pedí? |
| Tono | ¿Suena como mi marca o mi estilo? |
| Acción | ¿Puedo usar esto como base hoy? |

### Preguntas de mejora
- ¿Qué información le faltó?
- ¿Qué parte de la respuesta fue demasiado genérica?
- ¿Qué formato habría sido más útil?
- ¿Qué regla necesito agregar?
- ¿Qué ejemplo podría darle para mejorar el tono?
- ¿Qué debería preguntarme antes de responder?

### Fórmula de iteración
> “La respuesta fue útil, pero necesito que ahora: [cambio específico].”

Ejemplos:
- “Separa los hallazgos entre dolores, deseos, objeciones y citas textuales.”
- “No uses lenguaje de marketing genérico.”
- “Dame una versión para WhatsApp y otra para email.”
- “Prioriza las recomendaciones por impacto y facilidad de implementación.”

### Key takeaway
> No mejores tu asistente agregando más texto sin criterio. Mejora una variable a la vez: contexto, tarea, formato, reglas o ejemplos.

---

## Bloque 9. Feedback entre pares: “Prueba mi asistente”
**Duración:** 15 minutos  
**Formato:** Trabajo en parejas  
**Slides estimadas:** 2

### Objetivo
Validar si el asistente es comprensible y útil para alguien que no conoce a fondo la startup.

### Dinámica
Formar parejas. Cada persona tiene aproximadamente 7 minutos:

1. Explica en 60 segundos:
   - Qué tarea resuelve su asistente.
   - Para quién.
   - Qué resultado entrega.
2. La otra persona revisa el prompt o instrucciones.
3. Hace una prueba con un input diferente o formula una pregunta crítica.
4. Da feedback usando esta estructura:

### Feedback “2 + 1”
- **2 cosas claras o útiles**
- **1 mejora prioritaria**

### Preguntas para pares
- ¿Entiendo qué hace este asistente?
- ¿La tarea está suficientemente acotada?
- ¿El formato de salida es útil?
- ¿Hay contexto suficiente?
- ¿Qué riesgo o supuesto detecto?
- ¿Qué le agregaría para que sea más útil mañana?

### Key takeaway
> Si otra persona entiende qué hace tu asistente y puede probarlo, ya tienes una herramienta mucho más clara y replicable.

---

## Bloque 10. Cierre, compromisos y próximos pasos
**Duración:** 5 minutos  
**Formato:** Cierre grupal  
**Slides estimadas:** 2

### Objetivo
Convertir el prototipo en una práctica semanal y cerrar con una sensación de avance concreto.

### Dinámica
Pedir que cada participante complete esta frase:

> “Esta semana voy a usar mi asistente para ________ al menos ________ veces.”

Solicitar 3–5 voluntarios para compartir:
- Qué construyeron.
- Qué tarea van a delegar.
- Qué fue lo más útil que descubrieron.

Cerrar con tres ideas:

1. Empieza con una tarea pequeña y frecuente.
2. Usa información real de tu startup.
3. Itera después de usarlo, no antes.

### Key takeaway
> Tu asistente mejora cuando se usa en el trabajo real. La meta no es tener un prompt perfecto; es recuperar tiempo y aprender más rápido.

---

# 4. Ejercicio principal del workshop

# **Construye tu “Asistente Operativo #1”**

Cada participante construirá un asistente de IA para una tarea repetitiva y concreta de su startup.

## Objetivo del ejercicio
Crear una primera versión funcional que pueda ser utilizada desde el día siguiente.

## Duración total del ejercicio
**90 minutos distribuidos en tres etapas:**
- Diseño con Canvas: 25 min.
- Construcción: 30 min.
- Prueba e iteración: 20 min.
- Feedback de pares: 15 min.

## Entregable mínimo
Al finalizar, cada participante debe tener:

1. Un nombre para su asistente.
2. Un problema específico que resuelve.
3. Un prompt maestro guardado.
4. Un input real probado.
5. Un output generado.
6. Al menos una mejora realizada después de la primera prueba.
7. Un compromiso de uso para la próxima semana.

## Ejemplos de entregables finales
- Un asistente que transforma entrevistas de clientes en insights accionables.
- Un asistente que crea borradores de posts para LinkedIn con el tono del founder.
- Un asistente que redacta emails de follow-up para leads.
- Un asistente que organiza feedback de usuarios en oportunidades de producto.
- Un asistente que convierte un brief comercial en una propuesta inicial.
- Un asistente que genera guiones para demos de ventas.

---

# 5. Recursos para llevar a casa

Entregar vía código QR o correo posterior al workshop.

## Plantillas
1. **Canvas de Asistente de IA** en PDF y Google Docs.
2. **Prompt maestro RCTA** editable.
3. **Checklist de calidad para respuestas de IA.**
4. **Guía de iteración:** cómo mejorar prompts sin empezar desde cero.
5. **Plantilla de contexto de startup:**
   - Qué hacemos.
   - Cliente ideal.
   - Problema.
   - Propuesta de valor.
   - Competidores.
   - Tono de voz.
   - Preguntas frecuentes.

## Biblioteca de prompts iniciales
Incluir al menos 8 prompts listos para adaptar:

1. Asistente de entrevistas de clientes.
2. Asistente de contenido para founders.
3. Asistente de emails de ventas.
4. Asistente de propuesta comercial.
5. Asistente de validación de ideas.
6. Asistente de síntesis de feedback de usuarios.
7. Asistente de pitch y storytelling.
8. Asistente de onboarding y FAQs.

## Guía práctica: “7 días para mejorar tu asistente”
Proponer un reto simple:

| Día | Acción |
|---|---|
| Día 1 | Usarlo en una tarea real |
| Día 2 | Identificar qué respuesta fue débil |
| Día 3 | Mejorar contexto o reglas |
| Día 4 | Probarlo con otro input |
| Día 5 | Agregar un ejemplo de buena respuesta |
| Día 6 | Pedir feedback a un compañero |
| Día 7 | Decidir si mantener, ajustar o descartar el asistente |

## Recomendaciones de uso responsable
- No subir información sensible de clientes sin autorización.
- No compartir contraseñas, datos financieros privados o información legal confidencial.
- Revisar siempre los resultados antes de enviarlos o publicarlos.
- Verificar datos, cifras, citas y afirmaciones.
- No delegar decisiones críticas sin revisión humana.

---

# 6. Slide count estimado por sección

| Sección | Slides estimadas |
|---|---:|
| Bienvenida y objetivo del workshop | 3 |
| Qué puede y no puede hacer un asistente | 5 |
| Selección del problema | 3 |
| Framework RCTA: rol, contexto, tarea y formato | 6 |
| Demo en vivo | 3 |
| Pausa | 1 |
| Canvas de Asistente de IA | 4 |
| Construcción práctica | 3 |
| Prueba e iteración | 4 |
| Feedback entre pares | 2 |
| Cierre y próximos pasos | 2 |
| **Total estimado** | **36 slides** |

> Para mantener el ritmo, la mayoría de las slides deben ser visuales, con ejemplos, preguntas y plantillas; evitar bloques largos de texto.

---

# Recomendación de facilitación para 20–30 personas

- Trabajar con música suave durante los momentos de construcción.
- Usar un cronómetro visible para mantener energía y foco.
- Pedir a quienes avancen más rápido que apoyen a una persona cercana.
- Tener un “rincón de ayuda” para participantes con problemas de cuenta, Wi-Fi o acceso.
- Evitar explicar demasiadas funcionalidades de cada plataforma.
- Repetir durante el workshop:  
  **“No necesitas saber programar. Necesitas saber qué trabajo quieres delegar.”**

## Resultado final ideal

Al terminar las 3 horas, cada emprendedor podrá decir:

> “Construí un asistente de IA para una tarea real de mi startup, lo probé con información real y sé cómo mejorarlo mientras lo uso.”