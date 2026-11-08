# GPT-6.1 Terra — startup_content/workshop_outline

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 37.47s | tokens_per_second: 81.3
- input_tokens: 186 | output_tokens: 3045
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y dinámicas bien estructuradas.

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

# Construye tu Asistente de IA para tu Startup  
### Workshop práctico presencial · 3 horas · 20–30 emprendedores

**Promesa del workshop:** cada participante saldrá con un asistente de IA configurado para una tarea concreta de su startup, probado con un caso real y con un plan para mejorarlo.

No se necesita saber programar. Trabajaremos con una herramienta de chat con IA accesible desde navegador o celular; si permite crear asistentes personalizados, usaremos esa función. Si no, el asistente quedará listo como un prompt reutilizable.

---

## 1. Agenda detallada — 180 minutos

| Hora | Duración | Bloque | Dinámica | Slides |
|---|---:|---|---|---:|
| 0:00–0:15 | 15 min | Bienvenida: ¡tu primer copiloto! | Activación y conversación en parejas | 3 |
| 0:15–0:30 | 15 min | IA sin vueltas: qué puede y qué no puede hacer | Charla con ejemplos | 4 |
| 0:30–0:45 | 15 min | Encuentra tu tarea ganadora | Ejercicio individual y discusión | 3 |
| 0:45–1:05 | 20 min | Demo: de tarea a asistente | Demostración en vivo | 4 |
| 1:05–1:15 | 10 min | Pausa | Descanso | 1 |
| 1:15–1:55 | 40 min | ¡Manos a la obra! Construye tu asistente | Ejercicio guiado individual | 5 |
| 1:55–2:20 | 25 min | Prueba, falla y mejora | Pruebas en parejas | 3 |
| 2:20–2:40 | 20 min | Muestra y aprende | Demos y retroalimentación | 2 |
| 2:40–3:00 | 20 min | Plan de acción y cierre | Compromiso individual y discusión | 3 |
| **Total** | **180 min** | | | **28 slides** |

---

## 2. Materiales y preparación previa

### Para las y los participantes

Enviar 3–5 días antes:

- Invitación a traer laptop o celular con cargador. **Ideal: una laptop por persona**; si no es posible, se puede trabajar en parejas.
- Instrucciones para crear y probar una cuenta en la herramienta de IA elegida, preferentemente con una opción gratuita disponible en su país. Aclarar que los límites y funciones pueden variar.
- Solicitud de llevar una tarea repetitiva de su startup y un ejemplo **sin datos sensibles**. Por ejemplo: redactar mensajes de seguimiento, preparar preguntas para entrevistas o convertir notas ficticias en un resumen.
- Aviso de que no deben compartir contraseñas, información personal de clientes ni datos confidenciales del negocio.

### Para el equipo facilitador

- Elegir y probar previamente una herramienta principal que funcione desde navegador y en la región. Comprobar registro, acceso, idioma y límites del plan disponible.
- Preparar una alternativa: un documento editable con la plantilla del asistente y capturas de la demo, para quienes no puedan acceder a la herramienta.
- Configurar y probar un ejemplo completo: un asistente que redacte mensajes de seguimiento para prospectos ficticios.
- Preparar la presentación, una plantilla digital e impresa por participante y un enlace corto o QR a los recursos.
- Tener tres casos de ejemplo para quienes aún no tengan una startup definida.
- Idealmente, contar con **una persona de apoyo** para resolver problemas de acceso durante la práctica.

### En el espacio

- Wi-Fi probado para al menos 30 dispositivos, con red y contraseña visibles.
- Proyector, pantalla, audio si se usará video y extensiones eléctricas.
- Mesas que permitan trabajar en parejas; papel, bolígrafos y notas adhesivas.
- Opcional: conexión de respaldo desde un teléfono. Si falla internet de forma general, realizar la construcción en papel o documento local y dejar la prueba online como tarea de seguimiento.

---

## 3. Bloques del workshop

### Bloque 1. Bienvenida: ¡tu primer copiloto!  
**Duración:** 15 minutos · **Slides:** 3

**Objetivo:** generar energía, conectar a las personas y dejar claro qué van a construir.

**Dinámica:**

- **0–5 min | Bienvenida:** presentar la promesa y el resultado esperado.
- **5–10 min | En parejas:** cada persona responde: “¿Qué tarea de tu startup te gustaría hacer más rápido?”
- **10–15 min | Plenario:** recoger 3–4 respuestas y mostrar cómo se conectan con el workshop.

**Key takeaway:** no venimos a aprender programación; venimos a resolver una tarea concreta con IA.

---

### Bloque 2. IA sin vueltas: qué puede y qué no puede hacer  
**Duración:** 15 minutos · **Slides:** 4

**Objetivo:** dar el contexto mínimo para usar la herramienta con criterio.

**Dinámica:**

- **Charla breve:** explicar la IA generativa como una herramienta que produce respuestas a partir de instrucciones y contexto.
- **Ejemplos:** comparar una petición vaga —“haz marketing”— con una concreta —“propón tres mensajes de seguimiento para un prospecto ficticio”.
- **Discusión rápida:** ¿qué tareas podrían acelerar sin delegar la decisión final?

Cubrir tres reglas: la IA puede equivocarse o inventar datos; hay que revisar sus respuestas; y no se deben ingresar datos sensibles sin autorización.

**Key takeaway:** la IA es un copiloto, no una fuente infalible ni un reemplazo de tu criterio.

---

### Bloque 3. Encuentra tu tarea ganadora  
**Duración:** 15 minutos · **Slides:** 3

**Objetivo:** elegir un caso de uso simple y valioso para construir durante el workshop.

**Dinámica:**

- **5 min | Individual:** anotar tres tareas repetitivas.
- **5 min | Selección:** elegir una que ocurra con frecuencia, pueda describirse claramente y no requiera información confidencial.
- **5 min | En parejas:** completar y compartir:  
  **“Quiero que mi asistente me ayude a ______ para lograr ______.”**

Sugerencias: redactar respuestas frecuentes con información ficticia, preparar una entrevista de descubrimiento o crear un primer borrador de publicación.

**Key takeaway:** empieza pequeño: una tarea clara vale más que intentar construir un asistente que haga todo.

---

### Bloque 4. Demo: de tarea a asistente  
**Duración:** 20 minutos · **Slides:** 4

**Objetivo:** mostrar el proceso completo antes de que cada persona lo replique.

**Dinámica — demostración en vivo:**

1. Presentar el caso: seguimiento a un prospecto ficticio.
2. Definir rol, tarea, contexto, formato y límites.
3. Ingresar las instrucciones en la herramienta.
4. Probar con una solicitud concreta.
5. Detectar una debilidad y ajustar las instrucciones.

Mostrar tanto la opción de guardar un asistente personalizado como la alternativa de guardar el prompt en un documento, si la herramienta no tiene esa función.

**Key takeaway:** un asistente útil se construye dando buenas instrucciones, probando y ajustando.

---

### Bloque 5. Pausa  
**Duración:** 10 minutos · **Slides:** 1

**Objetivo:** recargar energía y resolver dudas rápidas de acceso.

**Dinámica:** descanso. El equipo de apoyo ayuda a quienes todavía no pueden ingresar a la herramienta.

**Key takeaway:** vuelve con tu tarea elegida y listo para construir.

---

### Bloque 6. ¡Manos a la obra! Construye tu asistente  
**Duración:** 40 minutos · **Slides:** 5

**Objetivo:** que cada participante configure una primera versión funcional o deje listo su prompt reutilizable.

**Dinámica:**

| Tiempo | Acción |
|---|---|
| 0–5 min | Abrir la herramienta y la plantilla. |
| 5–15 min | Completar rol, tarea, contexto y resultado esperado. |
| 15–25 min | Añadir límites, tono y criterios de calidad. |
| 25–35 min | Configurar el asistente o pegar el prompt en el chat; hacer una primera prueba. |
| 35–40 min | Guardar la versión inicial y anotar qué mejorar. |

El facilitador recorre la sala, ayuda a reducir tareas demasiado amplias y recuerda usar información ficticia o autorizada.

**Key takeaway:** no necesitas una versión perfecta para empezar; necesitas una primera versión que puedas probar.

---

### Bloque 7. Prueba, falla y mejora  
**Duración:** 25 minutos · **Slides:** 3

**Objetivo:** mejorar la calidad y confiabilidad del asistente mediante pruebas sencillas.

**Dinámica en parejas:**

- **5 min:** cada persona explica qué debería hacer su asistente.
- **10 min:** cada persona ejecuta dos pruebas: un caso normal y uno ambiguo o con información faltante.
- **5 min:** la pareja revisa los resultados con la lista de evaluación.
- **5 min:** cada quien ajusta sus instrucciones y guarda la nueva versión.

**Lista rápida de evaluación:**

- ¿Respondió a la tarea correcta?
- ¿Usó el formato y tono pedidos?
- ¿Pidió aclaraciones cuando faltaba información?
- ¿Inventó datos o hizo afirmaciones que requieren verificación?
- ¿Qué instrucción concreta mejoraría el resultado?

**Key takeaway:** probar es parte de construir. Si la respuesta falla, mejora la instrucción y vuelve a intentar.

---

### Bloque 8. Muestra y aprende  
**Duración:** 20 minutos · **Slides:** 2

**Objetivo:** celebrar avances y aprender de otros casos de uso.

**Dinámica:**

- **10 min | Demos:** invitar a tres personas a mostrar su tarea, un resultado y una mejora realizada. Aproximadamente tres minutos por persona.
- **7 min | Retroalimentación:** después de cada demo, recoger una idea útil o pregunta breve del grupo.
- **3 min | Síntesis:** destacar patrones: instrucciones claras, límites y revisión humana.

Si hay más voluntarios, pueden compartir sus asistentes al finalizar o en el canal posterior al workshop.

**Key takeaway:** un asistente sencillo, probado y relevante puede convertirse en una herramienta de uso diario.

---

### Bloque 9. Plan de acción y cierre  
**Duración:** 20 minutos · **Slides:** 3

**Objetivo:** convertir la práctica en un siguiente paso real.

**Dinámica:**

- **5 min | Individual:** completar el plan de siete días.
- **5 min | En parejas:** compartir el compromiso.
- **5 min | Plenario:** escuchar 2–3 compromisos.
- **5 min | Cierre:** entregar recursos, recoger feedback y celebrar.

**Plan de siete días:**

1. Usaré mi asistente para: ______.
2. Lo probaré en estas situaciones: ______.
3. Revisaré la calidad fijándome en: ______.
4. La próxima mejora será: ______.
5. Lo haré antes del día: ______.

**Key takeaway:** el valor aparece cuando incorporas el asistente a una tarea real y lo mejoras con el uso.

---

## 4. Ejercicio principal: construye tu asistente

### Resultado esperado

Un asistente configurado en la herramienta o un prompt guardado que la persona pueda copiar y reutilizar.

### Plantilla para completar

```text
ROL
Actúa como un asistente de [rol útil para mi startup].

OBJETIVO
Ayúdame a [una tarea concreta] para [resultado que quiero lograr].

CONTEXTO
Mi startup/proyecto se dedica a [descripción breve].
La audiencia o usuario es [descripción general, sin datos sensibles].

CÓMO QUIERO QUE TRABAJES
1. Antes de responder, pide aclaraciones si falta información importante.
2. Usa un tono [cercano/profesional/directo/etc.].
3. Entrega el resultado en este formato: [lista, tabla, mensaje, etc.].
4. Incluye [elementos que no deben faltar].

LÍMITES
- No inventes datos. Si no sabes algo, indícalo.
- No uses información confidencial o personal que no sea necesaria.
- Señala qué partes debo verificar antes de usar el resultado.
- No tomes decisiones finales por mí.

PRIMERA PRUEBA
Ayúdame con este caso ficticio o autorizado: [describir el caso].
```

### Ejemplo listo para adaptar

> Actúa como asistente de comunicación para una startup que vende software a pequeños negocios. Ayúdame a redactar mensajes breves de seguimiento para prospectos, con un tono cercano y profesional. Dame dos versiones de máximo 80 palabras. Si falta información importante, pregúntame. No inventes precios, características ni resultados.  
>
> **Prueba:** prepara un seguimiento para un prospecto ficticio que pidió una demostración, pero no respondió durante una semana.

### Plan B para cualquier participante

Si alguien no tiene cuenta, dispositivo o idea de startup, puede trabajar en pareja usando el ejemplo anterior. También puede completar la plantilla en papel y llevarse el prompt para probarlo después.

---

## 5. Recursos para llevar a casa

Entregar en un documento compartido y, de ser posible, mediante QR:

1. **Plantilla del asistente** editable y lista para copiar.
2. **Lista de pruebas:** caso normal, caso ambiguo y revisión de datos, tono y formato.
3. **Plan de acción de siete días** completado durante el cierre.
4. **Ejemplos de casos de uso:** seguimiento comercial, preparación de entrevistas y contenido para redes.
5. **Guía de uso responsable:** no ingresar datos sensibles; verificar afirmaciones, cifras y fuentes; revisar siempre antes de publicar o enviar.
6. **Enlace a la herramienta utilizada** y a su centro oficial de ayuda, junto con la aclaración de que sus funciones y límites pueden cambiar.
7. **Canal opcional de seguimiento** para compartir avances y pedir feedback entre participantes.

**Mensaje final para el grupo:** no necesitas el asistente perfecto. Necesitas uno que te ayude con una tarea real, que puedas revisar y que mejore contigo.