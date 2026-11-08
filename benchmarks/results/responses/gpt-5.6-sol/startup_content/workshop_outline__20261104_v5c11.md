# GPT-5.6 Sol — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.05 | quality: 9.72
- latency_total: 49.383s | tokens_per_second: 107.2
- input_tokens: 186 | output_tokens: 5294
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

# Workshop presencial: **Construye tu Asistente de IA para tu Startup**
### Workshop práctico para emprendedores early-stage no técnicos

**Duración:** 3 horas  
**Audiencia:** 20–30 emprendedores  
**Modalidad:** Presencial, práctica y colaborativa  
**Resultado esperado:** Cada participante termina con un asistente de IA básico, probado y listo para usar en una tarea real de su startup.

> **Promesa del workshop:** No necesitas programar. Solo necesitas una tarea repetitiva, contexto de tu negocio y disposición para experimentar.

---

## 1. Agenda general — 180 minutos

| Tiempo | Bloque | Duración | Slides estimados |
|---|---|---:|---:|
| 00:00–00:10 | Bienvenida y activación | 10 min | 3 |
| 00:10–00:25 | Qué es —y qué no es— un asistente de IA | 15 min | 5 |
| 00:25–00:45 | Elegir el problema correcto | 20 min | 5 |
| 00:45–01:05 | Anatomía de un buen asistente | 20 min | 7 |
| 01:05–01:20 | Demo en vivo: de cero a asistente | 15 min | 3 |
| 01:20–01:30 | Pausa | 10 min | 1 |
| 01:30–02:15 | Ejercicio principal: construye tu asistente | 45 min | 6 |
| 02:15–02:40 | Pruebas, mejoras y trabajo en parejas | 25 min | 5 |
| 02:40–02:55 | Show & Tell + aprendizajes | 15 min | 2 |
| 02:55–03:00 | Cierre y próximos pasos | 5 min | 2 |
|  | **Total** | **180 min** | **39 slides aprox.** |

---

# 2. Agenda detallada por bloques

## Bloque 1: Bienvenida y activación

**Duración:** 10 minutos  
**Slides:** 3

### Objetivo
Generar energía, alinear expectativas y conectar el workshop con problemas reales de las startups participantes.

### Dinámica
**Activación + conversación breve.**

1. Bienvenida y presentación del facilitador.
2. Presentar la promesa del workshop.
3. Pregunta al grupo:
   - “¿Qué tarea repetitiva te gustaría dejar de hacer esta semana?”
4. Los participantes comparten respuestas en voz alta o mediante notas adhesivas.
5. Agrupar rápidamente las respuestas:
   - Marketing y contenido
   - Ventas
   - Atención al cliente
   - Investigación
   - Operaciones
   - Administración

### Key takeaway
**Un asistente de IA debe comenzar con un problema concreto, no con una herramienta de moda.**

### Slides sugeridos
1. Título y promesa.
2. Qué construiremos hoy.
3. Pregunta de activación.

---

## Bloque 2: Qué es —y qué no es— un asistente de IA

**Duración:** 15 minutos  
**Slides:** 5

### Objetivo
Dar a participantes no técnicos un modelo mental simple sobre los asistentes de IA y sus posibilidades.

### Dinámica
**Charla breve + ejemplos participativos.**

Explicar que un asistente es una combinación de:

- Un rol claro
- Una tarea específica
- Contexto del negocio
- Instrucciones
- Formato de salida
- Criterios de calidad
- Iteración humana

### Ejemplos relevantes

- Asistente para responder consultas frecuentes.
- Asistente para preparar reuniones comerciales.
- Asistente para transformar entrevistas en insights.
- Asistente para crear borradores de contenido.
- Asistente para analizar feedback de clientes.
- Asistente para redactar seguimientos de ventas.

### Qué no es

- Un empleado autónomo que “sabe todo”.
- Una fuente infalible.
- Un reemplazo del criterio del fundador.
- Una herramienta a la que se le deben entregar datos sensibles sin revisión.
- Una solución para un proceso que aún no se entiende.

### Miniinteracción
Mostrar tres casos y pedir al grupo votar:

- ¿Buen caso para IA?
- ¿Requiere revisión humana?
- ¿No debería automatizarse?

### Key takeaway
**La IA acelera tareas bien definidas; no reemplaza el juicio, la estrategia ni la responsabilidad.**

### Slides sugeridos
1. Definición simple.
2. Anatomía general.
3. Casos de uso.
4. Qué no esperar.
5. Riesgos y supervisión humana.

---

## Bloque 3: Elegir el problema correcto

**Duración:** 20 minutos  
**Slides:** 5

### Objetivo
Ayudar a cada participante a seleccionar una tarea realista y valiosa para el ejercicio principal.

### Dinámica
**Charla breve + ejercicio individual + conversación en tríos.**

### Criterios de selección

Una buena primera tarea debe ser:

- **Frecuente:** ocurre varias veces al mes.
- **Repetitiva:** sigue patrones similares.
- **Basada en texto o información:** documentos, mensajes, notas o datos simples.
- **Fácil de revisar:** una persona puede detectar si el resultado es bueno.
- **De bajo riesgo:** un error no genera un problema grave.
- **Con ejemplos disponibles:** ya existen respuestas o entregables anteriores.

### Matriz rápida: impacto vs. facilidad

Cada participante lista tres tareas y les asigna una puntuación del 1 al 5 en:

1. Tiempo que consume.
2. Frecuencia.
3. Facilidad para explicar el proceso.
4. Disponibilidad de ejemplos.
5. Riesgo de equivocación.

Selecciona una tarea de **alto valor y bajo riesgo**.

### Preguntas de enfoque

- ¿Quién usará el asistente?
- ¿Qué información recibirá?
- ¿Qué debe producir?
- ¿Cómo sabrás si hizo un buen trabajo?
- ¿Qué parte debe revisar una persona?

### Key takeaway
**Empieza pequeño: una tarea, un usuario, un resultado claro.**

### Slides sugeridos
1. Qué hace buen caso de uso.
2. Casos recomendados.
3. Casos que conviene evitar.
4. Matriz impacto/facilidad.
5. Instrucciones del ejercicio.

---

## Bloque 4: Anatomía de un buen asistente

**Duración:** 20 minutos  
**Slides:** 7

### Objetivo
Entregar una estructura práctica que permita diseñar instrucciones robustas sin conocimientos técnicos.

### Dinámica
**Charla aplicada + construcción colectiva.**

## Framework: **RUTA + C**

### R — Rol
¿Quién debe ser el asistente?

> “Eres un asistente comercial para una startup SaaS B2B…”

### U — Usuario y objetivo
¿A quién ayuda y qué resultado busca?

> “Ayudas al fundador a preparar reuniones con potenciales clientes…”

### T — Tarea y proceso
¿Qué debe hacer, paso a paso?

> “Analiza la información, identifica necesidades, genera preguntas y propone el siguiente paso…”

### A — Acuerdos de salida
¿Cómo debe entregar la respuesta?

> “Responde en una tabla con oportunidad, evidencia, pregunta y prioridad…”

### C — Contexto, criterios y límites
¿Qué debe saber? ¿Qué significa calidad? ¿Qué no debe hacer?

> “No inventes información. Marca como ‘dato faltante’ cualquier información no disponible. Usa un tono directo y profesional.”

### Plantilla base

```text
ROL
Eres [rol específico] para [tipo de startup o negocio].

OBJETIVO
Tu objetivo es ayudar a [usuario] a conseguir [resultado].

CONTEXTO
Esta es la información relevante sobre el negocio:
[producto, cliente, propuesta de valor, tono, proceso]

ENTRADA
Recibirás:
[tipo de información]

PROCESO
Cada vez que recibas una solicitud:
1. [...]
2. [...]
3. [...]

SALIDA
Entrega el resultado en este formato:
[tabla, lista, correo, resumen, checklist]

CRITERIOS DE CALIDAD
Una buena respuesta debe:
- [...]
- [...]
- [...]

LÍMITES
- No inventes información.
- Indica cuando falten datos.
- No uses ni expongas información sensible.
- Solicita aclaraciones cuando sea necesario.
```

### Construcción colectiva
El grupo ayuda a construir un asistente simple, por ejemplo:

> “Asistente para convertir notas de una entrevista con clientes en necesidades, dolores, citas relevantes y próximos experimentos.”

### Key takeaway
**Los mejores resultados vienen de instrucciones claras, contexto útil y un formato verificable.**

### Slides sugeridos
1. Framework RUTA + C.
2. Rol.
3. Usuario y objetivo.
4. Tarea y proceso.
5. Formato de salida.
6. Contexto, criterios y límites.
7. Plantilla completa.

---

## Bloque 5: Demo en vivo — De cero a asistente

**Duración:** 15 minutos  
**Slides:** 3

### Objetivo
Mostrar el proceso completo antes de que los participantes construyan su propia versión.

### Dinámica
**Demo en vivo.**

### Caso sugerido
Construir un **asistente de seguimiento comercial** que:

- Recibe notas de una llamada.
- Resume necesidades y objeciones.
- Identifica información faltante.
- Redacta un correo de seguimiento.
- Sugiere el próximo paso.

### Secuencia de la demo

1. Mostrar una instrucción demasiado genérica:
   > “Escribe un correo para este cliente.”
2. Revisar por qué el resultado es mediocre.
3. Aplicar RUTA + C.
4. Agregar contexto de la startup.
5. Definir formato y criterios.
6. Probar con un caso.
7. Detectar un error.
8. Mejorar las instrucciones.
9. Volver a probar.

### Mensajes clave durante la demo

- La primera versión no tiene que ser perfecta.
- El prompt es un prototipo.
- Los ejemplos mejoran la consistencia.
- Si la salida falla, hay que mejorar las instrucciones o el contexto.
- Siempre debe existir revisión humana en decisiones sensibles.

### Key takeaway
**Construir un asistente es un ciclo: diseñar, probar, observar, ajustar y volver a probar.**

### Slides sugeridos
1. Caso y resultado esperado.
2. Antes vs. después.
3. Ciclo de mejora.

---

## Pausa

**Duración:** 10 minutos  
**Slides:** 1

Dejar en pantalla:

- Hora de regreso.
- Código QR a la plantilla de trabajo.
- Recordatorio: “Al volver, construiremos.”

---

# 3. Ejercicio principal: Construye tu asistente

## Bloque 6: Construcción individual guiada

**Duración:** 45 minutos  
**Slides:** 6

### Objetivo
Que cada participante cree y pruebe un asistente funcional para una tarea real de su startup.

### Dinámica
**Ejercicio individual con apoyo del facilitador y trabajo opcional en parejas.**

### Herramienta
Puede realizarse en cualquier asistente conversacional de IA disponible. No requiere código ni creación de integraciones.

## Entregable mínimo

Al terminar, cada participante debe tener:

1. Nombre del asistente.
2. Usuario y problema que resuelve.
3. Instrucciones completas.
4. Al menos un ejemplo de entrada.
5. Un resultado generado.
6. Una segunda versión mejorada.
7. Un checklist de revisión humana.

---

## Desarrollo del ejercicio

### Paso 1: Define la misión — 5 minutos

Completar:

> Mi asistente ayuda a __________ a realizar __________ para conseguir __________.

Ejemplo:

> Mi asistente ayuda al fundador a convertir notas de llamadas comerciales en seguimientos personalizados para aumentar la velocidad de cierre.

---

### Paso 2: Escribe el contexto mínimo — 8 minutos

Completar una ficha:

- Nombre de la startup.
- Qué ofrece.
- Cliente objetivo.
- Propuesta de valor.
- Tono de comunicación.
- Términos que debe usar o evitar.
- Información que nunca debe inventar.

**Regla práctica:** compartir solo el contexto necesario y evitar datos personales, financieros, estratégicos o confidenciales.

---

### Paso 3: Define entradas y salidas — 7 minutos

#### Entrada
¿Qué recibirá el asistente?

- Notas
- Preguntas de clientes
- Descripción de una campaña
- Feedback
- Perfil de un prospecto
- Documento o texto

#### Salida
¿Qué debe producir?

- Tabla
- Checklist
- Correo
- Resumen ejecutivo
- Guion
- Lista priorizada
- Plan de acción

---

### Paso 4: Construye las instrucciones con RUTA + C — 10 minutos

Los participantes adaptan la plantilla.

El facilitador y un asistente de sala circulan para resolver dudas y ayudar a reducir casos demasiado amplios.

---

### Paso 5: Haz la primera prueba — 7 minutos

Usar un caso real anonimizado o un ejemplo ficticio realista.

Evaluar:

- ¿La respuesta es útil?
- ¿Es específica?
- ¿Sigue el formato?
- ¿Inventa datos?
- ¿El tono es adecuado?
- ¿Se puede usar con pocas modificaciones?

---

### Paso 6: Mejora y vuelve a probar — 8 minutos

Agregar una o más mejoras:

- Instrucciones más claras.
- Un ejemplo de buena respuesta.
- Criterios de calidad.
- Preguntas de aclaración.
- Restricciones.
- Una mejor estructura de salida.

Guardar las versiones **V1** y **V2** para comparar.

### Key takeaway
**No necesitas construir el asistente perfecto; necesitas una primera versión útil, comprobable y mejorable.**

### Slides sugeridos
1. Objetivo y entregable.
2. Paso 1: misión.
3. Paso 2: contexto.
4. Paso 3: entrada y salida.
5. Paso 4: instrucciones.
6. Pasos 5–6: prueba y mejora.

---

# 4. Bloque 7: Pruebas, mejoras y trabajo en parejas

**Duración:** 25 minutos  
**Slides:** 5

### Objetivo
Fortalecer los asistentes mediante pruebas adversas y feedback entre pares.

### Dinámica
**Trabajo en parejas + test estructurado.**

Cada participante presenta en dos minutos:

- Qué hace su asistente.
- Quién lo usa.
- Qué entrada recibe.
- Qué resultado debería entregar.

La pareja actúa como “usuario de prueba”.

## Pruebas recomendadas

### Test 1: Caso normal
Una entrada clara y completa.

### Test 2: Información incompleta
Faltan datos importantes.

### Test 3: Solicitud ambigua
La intención no está clara.

### Test 4: Caso fuera de alcance
Se solicita algo que el asistente no debería hacer.

### Test 5: Riesgo de invención
La respuesta requeriría información que no está disponible.

## Rúbrica rápida de feedback

Puntuar del 1 al 5:

| Criterio | Pregunta |
|---|---|
| Claridad | ¿Entendí para qué sirve? |
| Utilidad | ¿El resultado ahorra tiempo o mejora una tarea? |
| Especificidad | ¿La respuesta está adaptada al negocio? |
| Confiabilidad | ¿Evita inventar y reconoce límites? |
| Usabilidad | ¿El formato se puede usar fácilmente? |

### Formato de feedback

- **Funciona bien:** …
- **Me confundió:** …
- **Agregaría:** …
- **Eliminaría:** …
- **Riesgo a revisar:** …

Luego cada participante realiza una última mejora.

### Key takeaway
**Un asistente confiable no solo funciona con el caso ideal; también sabe qué hacer cuando falta información.**

### Slides sugeridos
1. Instrucciones para las parejas.
2. Cinco pruebas.
3. Rúbrica.
4. Formato de feedback.
5. Última iteración.

---

## Bloque 8: Show & Tell + aprendizajes

**Duración:** 15 minutos  
**Slides:** 2

### Objetivo
Celebrar resultados, compartir ideas replicables y reforzar aprendizajes.

### Dinámica
**Presentaciones relámpago + discusión.**

Invitar a 3 o 4 participantes a presentar durante dos minutos:

1. Problema elegido.
2. Qué hace el asistente.
3. Resultado antes y después de iterar.
4. Mayor aprendizaje.
5. Siguiente paso.

### Preguntas para el grupo

- ¿Qué instrucción produjo la mayor mejora?
- ¿Qué error apareció con más frecuencia?
- ¿Qué asistente podrías comenzar a usar mañana?
- ¿Qué tarea todavía necesita intervención humana?

### Key takeaway
**El valor no está en “tener IA”, sino en mejorar una tarea real de forma medible.**

### Slides sugeridos
1. Formato de presentación.
2. Aprendizajes comunes.

---

## Bloque 9: Cierre y próximos pasos

**Duración:** 5 minutos  
**Slides:** 2

### Objetivo
Convertir el prototipo en un experimento real de negocio.

### Dinámica
**Compromiso individual + cierre energético.**

Cada participante completa:

> Durante los próximos siete días usaré mi asistente en ______ casos y mediré ______.

### Métricas posibles

- Minutos ahorrados.
- Tiempo de respuesta.
- Número de borradores aprovechables.
- Porcentaje de la salida que requiere edición.
- Cantidad de errores o alucinaciones.
- Calidad percibida por el usuario.
- Consistencia del formato.

### Cierre sugerido

> “Hoy no construiste un robot perfecto. Construiste una primera versión de una nueva forma de trabajar.”

### Key takeaway
**El siguiente paso no es agregar más funciones: es usarlo en cinco casos reales, medir y aprender.**

### Slides sugeridos
1. Reto de siete días.
2. QR de recursos y cierre.

---

# 5. Materiales necesarios

## Para preparar antes del workshop

### Tecnología

- Proyector y pantalla.
- Computador del facilitador.
- Adaptadores HDMI/USB-C.
- Internet estable.
- Red Wi-Fi y contraseña visibles.
- Hotspot o conexión de respaldo.
- Extensiones eléctricas y multitomas.
- Cronómetro visible.
- Micrófono si el espacio lo requiere.
- Parlante opcional para música de entrada y pausa.

### Para participantes

Solicitar previamente:

- Laptop cargada.
- Cargador.
- Cuenta activa en una herramienta de IA conversacional.
- Acceso verificado antes del evento.
- Una tarea repetitiva de su startup.
- Uno o dos ejemplos anonimizados de esa tarea.

### Materiales impresos

Una hoja de trabajo por participante con:

1. Inventario de tareas.
2. Matriz impacto/facilidad.
3. Canvas del asistente.
4. Plantilla RUTA + C.
5. Rúbrica de pruebas.
6. Plan de siete días.

También:

- Notas adhesivas.
- Marcadores.
- Bolígrafos.
- Puntos adhesivos para votación.
- Hojas adicionales.
- Carteles para agrupar casos de uso.

### Material digital

- Presentación.
- Plantilla editable.
- Documento con ejemplos.
- Casos ficticios de respaldo.
- Rúbrica de evaluación.
- Carpeta compartida.
- Encuesta de salida.
- Código QR y enlace corto a todos los recursos.

---

## Preparación del facilitador

### Una semana antes

- Enviar correo con requerimientos técnicos.
- Pedir a los asistentes que elijan tres tareas repetitivas.
- Confirmar acceso a herramientas.
- Preparar ejemplos relevantes para startups latinoamericanas.
- Evitar casos que dependan de software costoso o integraciones.

### El día anterior

- Probar la demo completa.
- Guardar capturas por si falla internet.
- Preparar un ejemplo de mala instrucción y su versión mejorada.
- Crear cinco casos ficticios para quienes no lleven uno.
- Verificar enlaces y permisos.
- Imprimir 10% de materiales adicionales.

### Una hora antes

- Probar proyector, audio e internet.
- Distribuir mesas en grupos de 4–5 personas.
- Colocar extensiones.
- Mostrar Wi-Fi y QR en pantalla.
- Abrir todas las pestañas necesarias.
- Tener un plan B offline.

---

# 6. Casos de uso sugeridos

Para participantes que no sepan qué construir:

## Ventas

- Preparador de reuniones comerciales.
- Generador de correos de seguimiento.
- Clasificador de prospectos.
- Analizador de objeciones.
- Generador de preguntas de discovery.

## Marketing

- Reutilizador de contenido.
- Generador de briefs.
- Adaptador de mensajes por canal.
- Analizador de comentarios.
- Calendario de contenido basado en objetivos.

## Clientes

- Borrador de respuestas frecuentes.
- Clasificador de tickets.
- Resumen de conversaciones.
- Identificador de problemas recurrentes.
- Generador de mensajes de onboarding.

## Investigación

- Analizador de entrevistas.
- Sintetizador de feedback.
- Comparador de competidores basado en información proporcionada.
- Generador de hipótesis.
- Organizador de hallazgos.

## Operaciones

- Creador de procedimientos.
- Generador de checklists.
- Resumen de reuniones.
- Asistente para documentación interna.
- Preparador de reportes semanales.

---

# 7. Recursos para llevar a casa

Entregar una carpeta o página con:

1. **Canvas del asistente de IA**
   - Problema
   - Usuario
   - Entrada
   - Proceso
   - Salida
   - Criterios
   - Límites

2. **Plantilla editable RUTA + C**

3. **Checklist de calidad**
   - ¿Tiene un propósito específico?
   - ¿Incluye suficiente contexto?
   - ¿Define el formato?
   - ¿Evita inventar?
   - ¿Pide aclaraciones?
   - ¿Define cuándo interviene una persona?

4. **Banco de casos de uso para startups**

5. **Rúbrica para probar asistentes**

6. **Plan de experimento de siete días**

7. **Guía de privacidad y uso responsable**
   - No compartir contraseñas.
   - No incluir datos personales sin autorización.
   - Anonimizar información de clientes.
   - No cargar información financiera, legal o confidencial sin entender las políticas de la herramienta.
   - Revisar siempre decisiones sensibles.

8. **Ejemplos antes/después**
   - Prompt genérico.
   - Prompt estructurado.
   - Resultado inicial.
   - Resultado mejorado.

9. **Registro de iteraciones**
   - Versión.
   - Cambio realizado.
   - Resultado.
   - Problema detectado.
   - Próximo ajuste.

10. **Grabación o PDF de las slides**, si aplica.

---

# 8. Plan B para evitar fricciones

## Si falla internet

- Trabajar el diseño completo en papel.
- Usar capturas preparadas de la demo.
- Hacer pruebas cruzadas: una persona simula ser el asistente siguiendo las instrucciones de otra.
- Compartir un enlace para ejecutar las pruebas después.

## Si alguien no tiene cuenta

- Trabajar en parejas.
- Usar casos impresos.
- Compartir un dispositivo solo durante la prueba.

## Si alguien no tiene un caso de uso

Asignarle uno de cinco casos preparados:

1. Seguimiento comercial.
2. Análisis de entrevista.
3. Respuesta a preguntas frecuentes.
4. Resumen de reunión.
5. Brief de contenido.

## Si el grupo avanza a ritmos distintos

Preparar retos extra para quienes terminan antes:

- Agregar dos ejemplos.
- Crear una prueba adversa.
- Definir una rúbrica automática.
- Adaptar la salida a dos canales.
- Crear una versión para otro usuario.

---

# 9. Resumen de slides

| Sección | Slides |
|---|---:|
| Bienvenida | 3 |
| Qué es un asistente | 5 |
| Elegir el problema | 5 |
| Anatomía del asistente | 7 |
| Demo | 3 |
| Pausa | 1 |
| Construcción | 6 |
| Pruebas en parejas | 5 |
| Show & Tell | 2 |
| Cierre | 2 |
| **Total estimado** | **39** |

**Recomendación:** Mantener las slides visuales, con poco texto. Las instrucciones detalladas deben estar en la hoja de trabajo, no en la presentación.

---

# Resultado final del workshop

Cada participante se va con:

- Un problema priorizado.
- Un asistente de IA diseñado para su startup.
- Instrucciones reutilizables.
- Dos versiones probadas.
- Feedback de otro emprendedor.
- Límites y revisión humana definidos.
- Un experimento concreto para los próximos siete días.