# GPT-6 Luna Pro — startup_content/workshop_outline

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.59 | quality: 9.72
- latency_total: 25.141s | tokens_per_second: 209.9
- input_tokens: 7197 | output_tokens: 5277
- judge_score: 4.8 | justificación: 

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

# Outline del workshop  
## **Construye tu Asistente de IA para tu Startup — Workshop Práctico**

**Duración:** 3 horas  
**Audiencia:** 20–30 emprendedores early-stage no técnicos  
**Formato:** Presencial, participativo y orientado a construir  
**Resultado esperado:** Cada participante termina con un primer prototipo de asistente de IA definido, probado y con próximos pasos claros.

> **Supuesto de diseño:** El ejercicio se hace con herramientas de IA accesibles mediante navegador y sin programar. Conviene tener una herramienta de respaldo por si falla el acceso a internet o alguna plataforma.

---

## 1. Agenda detallada

| Tiempo | Bloque | Formato |
|---|---|---|
| 00:00–00:10 | Bienvenida y encuadre | Apertura breve |
| 00:10–00:25 | ¿Qué puede hacer un asistente de IA por tu startup? | Charla + conversación |
| 00:25–00:45 | Elegir un buen problema: del dolor al caso de uso | Ejercicio individual + parejas |
| 00:45–01:05 | Diseña tu asistente: usuario, tarea y límites | Mini charla + canvas |
| 01:05–01:15 | Pausa | Descanso |
| 01:15–01:35 | Demo: de una instrucción vaga a un asistente útil | Demostración en vivo |
| 01:35–02:20 | Ejercicio principal: construye y prueba tu asistente | Trabajo individual o en parejas |
| 02:20–02:40 | Clínica de pruebas: ¿funciona en casos reales? | Prueba cruzada + feedback |
| 02:40–02:55 | De prototipo a piloto: riesgos, medición y próximos pasos | Discusión guiada |
| 02:55–03:00 | Cierre y compromiso de acción | Ronda rápida |

**Total: 180 minutos**

---

## 2. Bloques en detalle

### Bloque 1 — Bienvenida y encuadre
**Duración:** 10 min  
**Objetivo:** Crear energía, presentar el resultado del workshop y entender quiénes están en la sala.  
**Dinámica:** Apertura del facilitador y ronda rápida: nombre, startup y “una tarea repetitiva que me gustaría dejar de hacer”.  
**Key takeaway:** No venimos a hablar de IA en abstracto: vamos a trabajar sobre una tarea real de cada negocio.  
**Slides estimadas:** 2

---

### Bloque 2 — ¿Qué puede hacer un asistente de IA por tu startup?
**Duración:** 15 min  
**Objetivo:** Dar una idea concreta de qué es —y qué no es— un asistente de IA.  
**Dinámica:** Charla breve con ejemplos cercanos a startups: responder preguntas frecuentes, resumir entrevistas, preparar borradores comerciales, clasificar feedback o transformar notas en tareas. Conversación rápida sobre qué tareas conviene automatizar y cuáles requieren criterio humano.  
**Key takeaway:** Un buen asistente ayuda con una tarea acotada; no reemplaza la estrategia ni valida automáticamente sus propias respuestas.  
**Slides estimadas:** 4

---

### Bloque 3 — Elegir un buen problema: del dolor al caso de uso
**Duración:** 20 min  
**Objetivo:** Identificar una tarea frecuente, concreta y de bajo riesgo para convertirla en el primer caso de uso.  
**Dinámica:**  
1. Cada persona anota tres tareas repetitivas o lentas.  
2. Las puntúa según frecuencia, tiempo que consumen y facilidad de revisar el resultado.  
3. En parejas, elige una para trabajar durante el workshop.  
**Key takeaway:** Para el primer prototipo, conviene elegir una tarea pequeña, frecuente y fácil de verificar.  
**Slides estimadas:** 3

---

### Bloque 4 — Diseña tu asistente: usuario, tarea y límites
**Duración:** 20 min  
**Objetivo:** Convertir la tarea elegida en una definición clara del asistente.  
**Dinámica:** Mini charla y trabajo con un canvas de una página. Cada participante define:
- Quién usará el asistente.
- Qué tarea debe hacer.
- Qué información recibirá.
- Cómo debe entregar el resultado.
- Qué no debe hacer y cuándo debe pedir ayuda humana.  
**Key takeaway:** La calidad de un asistente empieza por una tarea y unas instrucciones claras, no por escribir un prompt largo.  
**Slides estimadas:** 4

---

### Bloque 5 — Pausa
**Duración:** 10 min  
**Objetivo:** Descansar y volver con energía para la parte práctica.  
**Dinámica:** Pausa libre.  
**Key takeaway:** —  
**Slides estimadas:** 0

---

### Bloque 6 — Demo: de una instrucción vaga a un asistente útil
**Duración:** 20 min  
**Objetivo:** Mostrar cómo configurar y mejorar un asistente sin programar.  
**Dinámica:** Demo en vivo con un caso sencillo, por ejemplo, un asistente que convierte notas de una reunión comercial en un resumen, próximos pasos y un borrador de correo. El facilitador muestra:
1. Una instrucción vaga y sus problemas.
2. Una versión mejorada con contexto, formato y límites.
3. Una prueba con un ejemplo.
4. Una corrección basada en el resultado.  
**Key takeaway:** No se espera acertar al primer intento: se mejora probando con ejemplos reales.  
**Slides estimadas:** 4

---

### Bloque 7 — Ejercicio principal: construye y prueba tu asistente
**Duración:** 45 min  
**Objetivo:** Crear un primer prototipo funcional para una tarea real de la startup.  
**Dinámica:** Trabajo individual o en parejas, con el canvas y la plantilla de instrucciones. El facilitador y los ayudantes circulan para dar soporte.  
**Key takeaway:** Al final, cada participante debe tener una versión inicial del asistente y al menos una prueba documentada.  
**Slides estimadas:** 3

#### Pasos del ejercicio principal

**1. Define el trabajo — 5 min**  
Completa esta frase:  
> “Mi asistente ayuda a **[tipo de usuario]** a **[tarea concreta]** usando **[información de entrada]** y entrega **[resultado esperado]**.”

**2. Prepara un ejemplo — 5 min**  
Usa información ficticia, pública o anonimizada. No incluyas datos personales, información confidencial de clientes ni secretos comerciales.

**3. Configura el asistente — 10 min**  
En la herramienta disponible, escribe instrucciones que incluyan:
- Rol y contexto del negocio.
- Tarea específica.
- Pasos que debe seguir.
- Formato deseado para la respuesta.
- Límites y casos en los que debe pedir aclaración o derivar a una persona.

**4. Prueba y mejora — 15 min**  
Pruébalo con un ejemplo. Identifica qué faltó, qué inventó o qué entregó en un formato poco útil. Ajusta las instrucciones y vuelve a probar.

**5. Guarda el prototipo — 10 min**  
Anota:
- Nombre y propósito del asistente.
- Instrucciones utilizadas.
- Ejemplo de entrada y salida.
- Una limitación conocida.
- El siguiente cambio que probarías.

**Alternativas de caso de uso para quienes no sepan por dónde empezar:**
- Convertir notas de reuniones en acuerdos y tareas.
- Crear borradores de respuestas a preguntas frecuentes.
- Resumir feedback de usuarios y agrupar temas.
- Preparar un primer borrador de una propuesta comercial.
- Transformar una descripción de producto en ideas para publicaciones.

---

### Bloque 8 — Clínica de pruebas: ¿funciona en casos reales?
**Duración:** 20 min  
**Objetivo:** Detectar errores y mejorar el prototipo con feedback de otra persona.  
**Dinámica:** En parejas, cada participante muestra una prueba. La otra persona revisa:
- ¿El resultado sirve para la tarea?
- ¿Qué información falta?
- ¿Hay algo inventado o arriesgado?
- ¿Se entiende cuándo debe intervenir una persona?  
Cada creador registra una mejora concreta.  
**Key takeaway:** Un asistente útil debe probarse con casos variados, no solo con el ejemplo que mejor le sale.  
**Slides estimadas:** 2

---

### Bloque 9 — De prototipo a piloto: riesgos, medición y próximos pasos
**Duración:** 15 min  
**Objetivo:** Ayudar a decidir si el asistente merece una prueba pequeña dentro del negocio.  
**Dinámica:** Discusión guiada y selección de una métrica. Ejemplos: minutos ahorrados, tiempo de respuesta, correcciones necesarias o porcentaje de resultados utilizables. Revisar también qué datos no deberían compartirse y qué decisiones requieren revisión humana.  
**Key takeaway:** Antes de escalar, prueba el asistente con pocos casos y mide si realmente mejora el trabajo.  
**Slides estimadas:** 3

---

### Bloque 10 — Cierre y compromiso de acción
**Duración:** 5 min  
**Objetivo:** Convertir el prototipo en una acción posterior al workshop.  
**Dinámica:** Ronda rápida: cada persona completa “En los próximos siete días voy a probar mi asistente con…”.  
**Key takeaway:** El valor aparece cuando el prototipo se prueba en el flujo real de trabajo, con supervisión.  
**Slides estimadas:** 1

---

## 3. Materiales necesarios

### Para preparar antes
- **Espacio:** Sala con mesas para grupos de 2–4 personas; idealmente, sillas móviles.
- **Internet:** Wi-Fi estable y datos de acceso compartidos con anticipación.
- **Proyector y audio:** Para mostrar la demo.
- **Herramientas:** Elegir una herramienta de IA disponible para el grupo y preparar una alternativa por si hay problemas de acceso.
- **Demo ensayada:** Caso simple con datos ficticios; tener capturas o un video breve como respaldo.
- **Material impreso o digital:**
  - Canvas “Diseña tu asistente”.
  - Plantilla de instrucciones.
  - Hoja de pruebas y checklist de revisión.
  - Hoja de próximos pasos.
- **Seguridad y privacidad:** Avisar que no se deben introducir datos confidenciales, personales o de clientes.
- **Facilitación:** Para 20–30 personas, idealmente un facilitador principal y 1–2 personas de apoyo durante el ejercicio.

### Para participantes
- Laptop o tablet con navegador y cargador.
- Acceso a la herramienta de IA seleccionada, si es posible.
- Una tarea repetitiva de su startup en mente.
- Un ejemplo ficticio, público o anonimizado para probar el asistente.
- Papel y lápiz, si el canvas no se usa digitalmente.

### Kit de respaldo
- Hojas impresas con el canvas y la plantilla.
- Capturas de la demo.
- Ejemplos de casos de uso y datos ficticios.
- Opción de trabajar en parejas si alguien no tiene dispositivo o cuenta.

---

## 4. Recursos para llevar a casa

1. **Canvas de diseño del asistente:** usuario, tarea, entradas, salida, límites y revisión humana.
2. **Plantilla de instrucciones para copiar y adaptar:**

   > Actúa como **[rol]** para **[contexto del negocio]**.  
   > Tu tarea es **[tarea concreta]**.  
   > Recibirás **[tipo de información]**.  
   > Sigue estos pasos: **[pasos]**.  
   > Devuelve el resultado en este formato: **[formato]**.  
   > No inventes información. Si falta un dato, **[pregunta o acción]**.  
   > No debes **[límites]**.  
   > Si la solicitud requiere criterio humano o tiene un riesgo importante, indícalo claramente.

3. **Checklist de pruebas:** utilidad, precisión, claridad, límites y necesidad de revisión humana.
4. **Guía para escoger el primer caso de uso:** frecuencia, tiempo ahorrado, facilidad de comprobación y nivel de riesgo.
5. **Plan de piloto de siete días:** qué probar, con quién, cuántas veces y qué medir.
6. **Lista de prácticas responsables:** usar datos ficticios o anonimizados, revisar resultados y no delegar decisiones sensibles sin supervisión.
7. **Prototipo creado durante el workshop:** instrucciones, ejemplo de prueba, resultado y siguiente mejora.

---

## 5. Slide count estimado

| Sección | Slides |
|---|---:|
| Bienvenida y encuadre | 2 |
| Qué puede hacer un asistente de IA | 4 |
| Elegir un caso de uso | 3 |
| Diseño del asistente | 4 |
| Pausa | 0 |
| Demo | 4 |
| Ejercicio principal | 3 |
| Clínica de pruebas | 2 |
| De prototipo a piloto | 3 |
| Cierre | 1 |
| **Total estimado** | **26 slides** |

**Sugerencia de facilitación:** mantener las diapositivas ligeras y visuales. El centro del workshop es construir y probar, no cubrir contenido a toda velocidad.