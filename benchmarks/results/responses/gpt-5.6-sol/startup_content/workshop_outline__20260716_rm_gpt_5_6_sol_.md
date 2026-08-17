# GPT-5.6 Sol — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.85 | quality: 10.0
- latency_total: 105.148s | tokens_per_second: 58.5
- input_tokens: 186 | output_tokens: 6155
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan detallado y práctico para un workshop de emprendimiento.

## Respuesta completa

# Workshop presencial  
## **Construye tu Asistente de IA para tu Startup — Workshop Práctico**

**Duración:** 3 horas  
**Audiencia:** 20–30 emprendedores early-stage no técnicos  
**Modalidad:** Presencial, práctica y sin código  
**Formato recomendado:** Mesas de 4–5 personas, con trabajo individual y pruebas en parejas

## Resultado esperado

Al terminar, cada participante tendrá:

- Un asistente de IA funcional para una tarea concreta de su startup.
- Instrucciones reutilizables y documentadas.
- Al menos tres pruebas realizadas con casos reales o simulados.
- Una versión mejorada a partir del feedback de otra persona.
- Un plan simple para implementarlo durante los próximos siete días.

> **Principio del workshop:** no buscamos crear “el asistente perfecto”. Buscamos construir en tres horas una primera versión útil, segura y fácil de mejorar.

---

# 1. Agenda detallada — 180 minutos

| Hora | Bloque | Duración | Formato | Slides estimados |
|---|---|---:|---|---:|
| 0:00–0:10 | 1. Bienvenida y activación | 10 min | Charla + dinámica | 3 |
| 0:10–0:25 | 2. ¿Qué es realmente un asistente de IA? | 15 min | Charla interactiva | 4 |
| 0:25–0:40 | 3. Elige el problema correcto | 15 min | Ejercicio individual + parejas | 3 |
| 0:40–1:00 | 4. Anatomía de un buen asistente + demo | 20 min | Explicación + demo en vivo | 6 |
| 1:00–1:20 | 5. Diseña las instrucciones de tu asistente | 20 min | Ejercicio guiado | 5 |
| 1:20–1:30 | **Break** | 10 min | Pausa | 1 |
| 1:30–2:05 | 6. Build Sprint: construye tu asistente | 35 min | Trabajo práctico | 4 |
| 2:05–2:30 | 7. Test Lab: prueba, rompe y mejora | 25 min | Pruebas en parejas | 4 |
| 2:30–2:45 | 8. Show & Tell | 15 min | Presentaciones + discusión | 2 |
| 2:45–2:55 | 9. Privacidad, límites y plan de implementación | 10 min | Charla + compromiso individual | 3 |
| 2:55–3:00 | 10. Cierre y próximos pasos | 5 min | Recap + foto final | 2 |
|  | **Total** | **180 min** |  | **37 slides aprox.** |

---

# 2. Materiales necesarios

## Preparación del facilitador

### Tecnología

- Proyector o pantalla grande.
- Adaptadores HDMI/USB-C.
- Computadora del facilitador.
- Conexión Wi-Fi estable para 30 dispositivos.
- Hotspot o plan de respaldo.
- Extensiones eléctricas y multicontactos.
- Cronómetro visible.
- Parlante opcional para música durante los ejercicios.

### Herramientas de IA

Seleccionar una herramienta principal y tener una alternativa:

- ChatGPT
- Claude
- Gemini
- Copilot
- Otra plataforma de IA conversacional disponible en el país

El workshop debe poder realizarse usando una conversación normal con IA, sin depender de funciones pagadas como creación de agentes, GPTs personalizados o integraciones.

### Configuración previa

- Enviar un correo 48–72 horas antes solicitando:
  - Llevar laptop y cargador.
  - Crear o verificar una cuenta en la herramienta elegida.
  - Traer una tarea repetitiva de su startup.
  - Traer uno o dos ejemplos reales, sin información sensible.
- Crear un QR con:
  - Workbook digital.
  - Plantilla de instrucciones.
  - Casos de prueba.
  - Recursos posteriores.
- Tener capturas de pantalla para una demo de respaldo si falla internet.
- Preparar un asistente de ejemplo previamente construido.
- Preparar datos ficticios para quienes todavía no tienen clientes o información real.

### Materiales impresos

Idealmente, una copia por participante:

1. Canvas “Mi Asistente de IA”.
2. Plantilla de instrucciones.
3. Checklist de pruebas.
4. Tarjeta de guardrails y privacidad.
5. Plan de implementación de siete días.
6. Hoja de feedback para parejas.

### Materiales físicos

- Post-its de dos colores.
- Marcadores.
- Hojas A4.
- Cinta adhesiva.
- Puntos adhesivos para votación.
- Nombre o tent cards para participantes.

## Configuración del salón

- Mesas en grupos de 4–5 personas.
- Una persona facilitadora principal.
- Recomendado: un cofacilitador para apoyar durante el Build Sprint.
- Pared o tablero para colocar casos de uso.
- Mesa de “soporte técnico” para resolver accesos y contraseñas sin frenar al grupo.

---

# 3. Desarrollo de cada bloque

## Bloque 1. Bienvenida y activación

**Duración:** 10 minutos  
**Slides:** 3

### Objetivo

Crear energía, alinear expectativas y conectar el workshop con problemas reales de los participantes.

### Dinámica

**Charla breve + participación rápida**

1. Bienvenida y presentación del facilitador.
2. Mostrar el resultado esperado: “Hoy sales con un asistente funcionando”.
3. Pregunta al grupo:
   - “¿Qué tarea repetitiva te quita más tiempo cada semana?”
4. Cada participante escribe una tarea en un post-it.
5. Dos o tres personas comparten su respuesta.

### Contenido clave

- No se requiere programar.
- No se necesita entender cómo funciona un modelo de IA internamente.
- El foco será resolver una tarea concreta, no “usar IA por usar IA”.
- La primera versión será un prototipo, no un producto final.

### Key takeaway

> Un buen asistente de IA comienza con un problema claro, no con una herramienta.

---

## Bloque 2. ¿Qué es realmente un asistente de IA?

**Duración:** 15 minutos  
**Slides:** 4

### Objetivo

Diferenciar entre una consulta aislada a la IA y un asistente diseñado para ejecutar una tarea de forma consistente.

### Dinámica

**Charla interactiva con ejemplos**

Comparar tres niveles:

1. **Pregunta aislada:**  
   “Dame ideas para Instagram”.

2. **Prompt con contexto:**  
   “Dame cinco ideas para Instagram para una fintech dirigida a freelancers”.

3. **Asistente:**  
   Tiene un rol, contexto, proceso, formato, reglas y criterios de calidad reutilizables.

### Ejemplos relevantes para startups

- Sintetizar entrevistas de clientes.
- Preparar reuniones comerciales.
- Crear borradores de contenido.
- Responder preguntas frecuentes.
- Convertir feedback en insights accionables.
- Redactar seguimiento de ventas.
- Comparar competidores.
- Organizar experimentos de validación.

### Miniinteracción

Mostrar tres posibles casos y preguntar:

- ¿Cuál genera más valor?
- ¿Cuál necesita supervisión humana?
- ¿Cuál sería riesgoso automatizar completamente?

### Key takeaway

> Un asistente no es “un prompt mágico”; es un proceso repetible con instrucciones, límites y criterios de calidad.

---

## Bloque 3. Elige el problema correcto

**Duración:** 15 minutos  
**Slides:** 3

### Objetivo

Seleccionar una tarea pequeña, frecuente y medible que pueda prototiparse dentro del workshop.

### Dinámica

**Ejercicio individual + conversación en parejas**

Cada participante lista tres tareas que:

- Repite con frecuencia.
- Consumen tiempo.
- Utilizan texto, información o documentos.
- Tienen un resultado relativamente claro.

Luego puntúa cada tarea del 1 al 5 en:

| Criterio | Pregunta |
|---|---|
| Frecuencia | ¿Ocurre semanalmente o más? |
| Tiempo | ¿Consume al menos 30–60 minutos? |
| Claridad | ¿Sé cómo debería verse un buen resultado? |
| Riesgo | ¿Puedo probarla sin datos sensibles ni decisiones críticas? |
| Impacto | ¿Liberaría tiempo o mejoraría una métrica relevante? |

### Regla para elegir

Priorizar una tarea:

- Frecuente.
- Específica.
- Fácil de verificar.
- De bajo o medio riesgo.
- Que requiera supervisión humana al final.

### Ejemplos recomendados para el workshop

- Analizador de entrevistas de clientes.
- Asistente de follow-up comercial.
- Generador de briefs de contenido.
- Preparador de reuniones.
- Organizador de feedback.
- Creador de FAQs.
- Revisor de propuestas de valor.
- Asistente de experimentos de validación.

### Casos que conviene evitar

- “Haz todo mi marketing”.
- “Maneja mi startup”.
- Decisiones legales, médicas o financieras.
- Evaluar o contratar personas automáticamente.
- Tareas que requieran múltiples integraciones técnicas.
- Procesar información confidencial sin autorización.

### Key takeaway

> Si el caso de uso no cabe en una frase, probablemente todavía es demasiado amplio.

---

## Bloque 4. Anatomía de un buen asistente + demo

**Duración:** 20 minutos  
**Slides:** 6

### Objetivo

Dar a los participantes una estructura simple para convertir una tarea en instrucciones que la IA pueda seguir.

### Dinámica

**Explicación visual + demo en vivo**

Presentar la estructura **R-C-P-F-R**:

1. **Rol:** ¿Quién debe ser el asistente?
2. **Contexto:** ¿Qué necesita saber sobre la startup, cliente o situación?
3. **Proceso:** ¿Qué pasos debe seguir?
4. **Formato:** ¿Cómo debe entregar el resultado?
5. **Reglas:** ¿Qué debe hacer, evitar o preguntar?

Agregar dos componentes para mejorar la consistencia:

6. **Criterios de calidad:** ¿Cómo sabemos si la respuesta es buena?
7. **Ejemplos:** ¿Qué ejemplo puede imitar?

### Demo recomendada

Construir en vivo un:

**“Asistente para analizar entrevistas de clientes”**

#### Antes

Prompt débil:

> “Analiza esta entrevista y dime qué piensas”.

#### Después

Instrucciones estructuradas:

> Eres un analista de customer discovery para una startup early-stage. Tu misión es analizar transcripciones de entrevistas sin inventar información.  
>  
> Identifica: problemas mencionados, intensidad del problema, soluciones actuales, objeciones, frases textuales y señales de intención de compra.  
>  
> Separa observaciones de interpretaciones. Si falta información, indícalo.  
>  
> Entrega el resultado en una tabla y termina con tres preguntas que deberíamos validar en la siguiente entrevista.

Probarlo con una transcripción ficticia breve.

### Puntos a destacar durante la demo

- La primera respuesta no tiene que ser perfecta.
- Se puede pedir a la IA que haga preguntas antes de ejecutar.
- El formato de salida reduce trabajo posterior.
- Las reglas previenen alucinaciones y respuestas genéricas.
- Los ejemplos ayudan más que los adjetivos vagos como “hazlo increíble”.

### Key takeaway

> Cuanto más claro sea el proceso y el formato de salida, más útil y consistente será el asistente.

---

## Bloque 5. Diseña las instrucciones de tu asistente

**Duración:** 20 minutos  
**Slides:** 5

### Objetivo

Crear el primer borrador de instrucciones antes de abrir o configurar la herramienta.

### Dinámica

**Ejercicio guiado individual**

Cada participante completa el canvas:

### Canvas “Mi Asistente de IA”

1. **Nombre del asistente**
2. **Usuario principal**
3. **Tarea que realiza**
4. **Momento en el que se utilizará**
5. **Información que recibirá**
6. **Resultado esperado**
7. **Pasos que debe seguir**
8. **Formato de respuesta**
9. **Qué no debe hacer**
10. **Qué debe preguntar si falta información**
11. **Cómo revisaré la calidad**

### Fórmula para definir la tarea

> Ayudar a **[usuario]** a convertir **[input]** en **[output]**, siguiendo **[criterios]**, para lograr **[resultado]**.

Ejemplo:

> Ayudar al fundador a convertir notas de una llamada comercial en un correo de seguimiento personalizado, breve y accionable, para aumentar la probabilidad de una siguiente reunión.

### Cierre del bloque

En parejas, cada participante explica su asistente en 45 segundos. La otra persona responde:

- ¿Entiendo exactamente qué hace?
- ¿El resultado se puede evaluar?
- ¿Es suficientemente pequeño para construir hoy?

### Key takeaway

> Diseñar primero evita perder tiempo probando prompts al azar.

---

## Break

**Duración:** 10 minutos  
**Slides:** 1

Dejar visible:

- QR de materiales.
- Hora exacta de regreso.
- Instrucción: “Vuelve con tu canvas completo y la herramienta abierta”.

---

## Bloque 6. Build Sprint: construye tu asistente

**Duración:** 35 minutos  
**Slides:** 4

### Objetivo

Convertir el canvas en un asistente funcional dentro de una herramienta de IA.

### Dinámica

**Trabajo práctico individual con apoyo del facilitador**

Los participantes pueden:

- Utilizar las instrucciones al inicio de una conversación.
- Guardarlas en un proyecto, configuración o agente personalizado si su herramienta lo permite.
- Mantenerlas en un documento reutilizable si utilizan una cuenta gratuita.

### Secuencia del sprint

#### Minutos 0–5: configurar

- Abrir la herramienta.
- Crear una nueva conversación o proyecto.
- Pegar la plantilla base.

#### Minutos 5–15: completar instrucciones

Agregar:

- Rol.
- Contexto.
- Proceso.
- Formato.
- Reglas.
- Criterios de calidad.

#### Minutos 15–25: ejecutar primer caso

Proporcionar un input real anonimizado o uno ficticio.

Observar:

- ¿Entendió la tarea?
- ¿Siguió los pasos?
- ¿El formato es útil?
- ¿Inventó algo?
- ¿El resultado ahorra tiempo?

#### Minutos 25–35: realizar primera mejora

Cambiar una o dos partes de las instrucciones. Evitar reescribir todo.

### Rol del facilitador

Circular por las mesas y hacer preguntas, no construir por la persona:

- “¿Qué input recibirá?”
- “¿Cómo se ve un buen resultado?”
- “¿Qué decisión seguirá siendo humana?”
- “¿Qué información podría faltar?”
- “¿Qué hizo la IA que no querías que hiciera?”

### Key takeaway

> La primera versión sirve para aprender qué instrucciones faltan; no para demostrar que la idea ya está terminada.

---

## Bloque 7. Test Lab: prueba, rompe y mejora

**Duración:** 25 minutos  
**Slides:** 4

### Objetivo

Validar el asistente con distintos escenarios y mejorar su confiabilidad.

### Dinámica

**Pruebas individuales + red teaming en parejas**

Cada participante prueba tres escenarios:

1. **Caso normal:** input claro y completo.
2. **Caso incompleto:** falta información relevante.
3. **Caso difícil:** input ambiguo, contradictorio o fuera de alcance.

### Checklist de evaluación

Puntuar del 1 al 5:

- Relevancia.
- Precisión.
- Claridad.
- Utilidad.
- Cumplimiento del formato.
- Manejo de información faltante.
- Respeto de límites.
- Cantidad de edición humana requerida.

### Prueba en parejas

Intercambiar asistentes o instrucciones.

La otra persona intenta “romperlo” con preguntas como:

- ¿Qué pasa si el input está incompleto?
- ¿Qué pasa si le pido algo fuera de su función?
- ¿Qué pasa si hay información contradictoria?
- ¿Inventa datos para completar la respuesta?
- ¿Entrega recomendaciones como hechos?
- ¿Explica sus supuestos?

### Ciclo de mejora

Aplicar la fórmula:

> **Observé que…**  
> **Esto ocurre porque falta…**  
> **Agregaré o cambiaré esta instrucción…**  
> **Volveré a probar con…**

### Key takeaway

> No evalúes un asistente por una respuesta impresionante. Evalúalo por su comportamiento en varios casos.

---

## Bloque 8. Show & Tell

**Duración:** 15 minutos  
**Slides:** 2

### Objetivo

Compartir aprendizajes, inspirar nuevos casos de uso y practicar cómo explicar el valor del asistente.

### Dinámica

**Presentaciones relámpago**

Seleccionar entre tres y cinco voluntarios. Cada uno tiene dos minutos:

1. ¿Qué problema resuelve?
2. ¿Qué input recibe?
3. ¿Qué output entrega?
4. ¿Qué cambió después de probarlo?
5. ¿Cuánto tiempo podría ahorrar?

Después de cada presentación, el grupo da feedback usando:

- **Me gusta:** algo útil o claro.
- **Me pregunto:** una duda o riesgo.
- **Probaría:** un test adicional.

Opcional: votación con puntos adhesivos en tres categorías:

- Mayor ahorro de tiempo.
- Uso más creativo.
- Mejor diseño de instrucciones.

### Key takeaway

> El valor del asistente no está en lo sofisticado que parece, sino en la tarea que mejora.

---

## Bloque 9. Privacidad, límites y plan de implementación

**Duración:** 10 minutos  
**Slides:** 3

### Objetivo

Evitar usos riesgosos y convertir el prototipo en un pequeño experimento de negocio.

### Dinámica

**Charla breve + compromiso individual**

### Reglas prácticas de seguridad

No ingresar sin autorización:

- Datos personales de clientes.
- Información financiera sensible.
- Contratos confidenciales.
- Contraseñas o credenciales.
- Información médica.
- Datos internos de empleados.
- Propiedad intelectual crítica.

Buenas prácticas:

- Anonimizar nombres y datos.
- Utilizar información ficticia durante las pruebas.
- Revisar las políticas de la herramienta.
- Mantener revisión humana.
- Verificar hechos, cifras y fuentes.
- No presentar contenido generado como verdad automática.
- Definir cuándo el asistente debe responder: “No tengo suficiente información”.

### Plan de implementación de siete días

Cada participante completa:

- Lo usaré para:
- La persona responsable será:
- Lo probaré en:
- Lo usaré al menos ___ veces:
- Mediré:
- Revisaré manualmente:
- Decidiré continuar, ajustar o detener según:

### Métricas simples

- Minutos ahorrados.
- Porcentaje de respuestas utilizables.
- Cantidad de edición requerida.
- Tiempo de respuesta.
- Calidad percibida por el usuario.
- Errores encontrados.
- Conversión o siguiente acción lograda.

### Key takeaway

> Empieza con supervisión humana, mide el resultado y automatiza solo después de demostrar valor.

---

## Bloque 10. Cierre y próximos pasos

**Duración:** 5 minutos  
**Slides:** 2

### Objetivo

Consolidar el aprendizaje y asegurar una acción posterior.

### Dinámica

**Recap + compromiso público**

Completar verbalmente o en una tarjeta:

> “En las próximas 48 horas usaré mi asistente para ________”.

Cierre con tres ideas:

1. Problema pequeño y claro.
2. Instrucciones estructuradas.
3. Pruebas y mejora continua.

Foto grupal opcional mostrando el nombre de los asistentes creados.

### Key takeaway

> Construir fue el primer paso; el verdadero aprendizaje comienza al usarlo con situaciones reales.

---

# 4. Ejercicio principal del workshop

## Reto: “Construye un asistente útil en 60 minutos”

El ejercicio principal comienza en el bloque de diseño y culmina con el Test Lab. Todos pueden realizarlo en una herramienta conversacional, sin código y sin necesidad de una cuenta pagada.

## Entregable mínimo

Al finalizar, cada persona debe tener:

1. Un caso de uso definido en una frase.
2. Un bloque de instrucciones reutilizables.
3. Un formato de entrada.
4. Un formato de salida.
5. Tres casos de prueba.
6. Una versión mejorada después del feedback.
7. Una métrica para probarlo durante siete días.

## Plantilla universal de instrucciones

```text
NOMBRE DEL ASISTENTE:
[Nombre breve y descriptivo]

ROL:
Eres un/a [rol o especialidad relevante].

USUARIO:
Tu usuario principal es [tipo de persona].

OBJETIVO:
Tu misión es ayudar a [usuario] a convertir [input] en [output]
para lograr [resultado].

CONTEXTO:
Esta startup:
- Ofrece:
- Atiende a:
- Está en la etapa:
- Su tono o estilo es:
- La información relevante es:

PROCESO:
Cuando recibas un input:

1. Revisa si tienes la información necesaria.
2. Si falta información crítica, haz un máximo de [número] preguntas.
3. Analiza el input siguiendo estos criterios:
   - [criterio 1]
   - [criterio 2]
   - [criterio 3]
4. Genera el resultado.
5. Revisa que cumpla las reglas antes de responder.

FORMATO DE SALIDA:
Entrega la respuesta en este formato:

1. [Sección]
2. [Sección]
3. [Tabla, bullets, email, checklist, etc.]
4. Próxima acción recomendada

REGLAS:
- No inventes datos.
- Separa hechos, supuestos y recomendaciones.
- Si no tienes suficiente información, dilo claramente.
- No ejecutes tareas fuera del alcance definido.
- Utiliza un lenguaje [simple/directo/profesional/etc.].
- No incluyas información confidencial.
- Todo resultado debe ser revisado por una persona.

CRITERIOS DE CALIDAD:
Una buena respuesta debe ser:
- Específica.
- Accionable.
- Fácil de revisar.
- Consistente con el contexto.
- Clara sobre sus supuestos.

PRIMERA INTERACCIÓN:
Antes de comenzar, pregunta al usuario por:
- [input necesario 1]
- [input necesario 2]
- [input necesario 3]
```

## Opciones de ejercicio para quienes no tengan un caso de uso

### Opción A: Analizador de entrevistas

**Input:** notas o transcripción.  
**Output:** problemas, frases textuales, intensidad, soluciones actuales y preguntas siguientes.

### Opción B: Asistente de follow-up comercial

**Input:** notas de una reunión.  
**Output:** correo personalizado, acuerdos, próximos pasos y recordatorio.

### Opción C: Asistente de contenido

**Input:** una idea, entrevista o artículo.  
**Output:** tres publicaciones adaptadas al canal y audiencia.

### Opción D: Asistente para feedback

**Input:** comentarios de clientes.  
**Output:** temas, frecuencia, urgencia, evidencia y acciones sugeridas.

### Opción E: Preparador de reuniones

**Input:** tipo de reunión, objetivo y participantes.  
**Output:** agenda, preguntas, riesgos y resultado esperado.

## Criterio de éxito

El ejercicio está completo si otra persona puede usar el asistente sin que su creador tenga que explicarle verbalmente cómo funciona.

---

# 5. Recursos para llevar a casa

Entregar mediante QR y, cuando sea posible, en formato editable.

## Kit de recursos

1. **Canvas “Mi Asistente de IA”**
2. **Plantilla universal de instrucciones**
3. **Biblioteca de casos de uso para startups**
4. **Checklist de calidad**
5. **Checklist de privacidad y seguridad**
6. **Matriz para priorizar oportunidades de IA**
7. **Plan de prueba de siete días**
8. **Plantilla para registrar versiones y aprendizajes**
9. **Glosario simple de IA para no técnicos**
10. **Lista comparativa de herramientas no-code**

## Plantilla de registro de pruebas

| Fecha | Caso probado | Resultado | Error observado | Cambio realizado | Nueva puntuación |
|---|---|---|---|---|---|

## Checklist antes de usar un resultado

- ¿La información es correcta?
- ¿Hay datos inventados?
- ¿Los supuestos están claros?
- ¿El tono es apropiado?
- ¿Se expuso información sensible?
- ¿El resultado necesita revisión experta?
- ¿La próxima acción es clara?
- ¿Yo asumiría responsabilidad por enviar o usar esta respuesta?

## Reto posterior de siete días

- Usar el asistente al menos cinco veces.
- Registrar cuánto tiempo ahorra.
- Identificar los tres errores más frecuentes.
- Mejorar una sola sección de las instrucciones.
- Compartir la versión final con una persona del equipo.
- Decidir: continuar, ajustar o descartar.

---

# 6. Resumen de slides estimados

| Sección | Slides |
|---|---:|
| Bienvenida y resultados | 3 |
| Qué es un asistente de IA | 4 |
| Selección del problema | 3 |
| Anatomía + demo | 6 |
| Diseño de instrucciones | 5 |
| Break | 1 |
| Build Sprint | 4 |
| Test Lab | 4 |
| Show & Tell | 2 |
| Privacidad + implementación | 3 |
| Cierre | 2 |
| **Total estimado** | **37 slides** |

La presentación debe ser principalmente visual: ejemplos, plantillas, cronómetros e instrucciones de ejercicios. Evitar slides llenas de texto; el workbook debe contener el detalle.

---

# Recomendaciones de facilitación

- Mantener la teoría en menos del 30% del tiempo.
- Usar ejemplos de startups latinoamericanas: ventas por WhatsApp, equipos pequeños, operaciones manuales y presupuestos limitados.
- No detener el workshop por problemas de acceso; formar parejas si alguien no puede entrar a una herramienta.
- Celebrar asistentes simples que resuelven bien una tarea.
- Repetir constantemente: **“No subas información que no compartirías públicamente”**.
- Dar avisos de tiempo durante los sprints: quedan 15, 5 y 2 minutos.
- Priorizar que todos terminen una versión funcional sobre profundizar en funciones avanzadas.
- Tener un caso ficticio de respaldo para participantes que aún están explorando una idea de startup.