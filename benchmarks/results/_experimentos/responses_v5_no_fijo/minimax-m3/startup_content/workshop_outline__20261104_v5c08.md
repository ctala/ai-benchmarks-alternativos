# MiniMax M3 — startup_content/workshop_outline

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.46 | quality: 9.72
- latency_total: 50.776s | tokens_per_second: 107.0
- input_tokens: 341 | output_tokens: 5433
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

# Outline completo  
## “Construye tu Asistente de IA para tu Startup — Workshop Práctico”

**Formato:** presencial  
**Duración:** 3 horas  
**Audiencia:** 20–30 emprendedores early-stage no técnicos  
**Enfoque:** práctico, participativo y orientado a resultados  
**Producto del taller:** cada participante diseñará y prototipará un asistente de IA útil para su startup.

---

# 1. Agenda detallada

| Bloque | Duración | Acumulado | Contenido |
|---|---:|---:|---|
| Abertura y encuadre | 15 min | 15 min | Bienvenida, reglas de trabajo y promesa del taller |
| Bloque 1: ¿Qué puede resolver un asistente de IA? | 25 min | 40 min | Casos de uso, oportunidad y criterios de valor |
| Bloque 2: Anatomía de un asistente de IA | 30 min | 1 h 10 min | Prompt, contexto, herramientas, knowledge base y límites |
| Pausa activa | 10 min | 1 h 20 min | Stretch, café ykj networking informal |
| Bloque 3: Demo en vivo | 25 min | 1 h 45 min | Construcción guiada de un asistente funcional |
| Ejercicio principal: diseña tu asistente | 40 min | 2 h 25 min | Diseño individual y construcción del prototipo |
| Bloque 4: Prueba, feedback y mejora | 20 min | 2 h 45 min | Testing entre pares e iteración rápida |
| Cierre y plan de activación | 15 min | 3 h | Presentaciones, próximos pasos y cierre |
| **Total** | **3 horas** |  |  |

> **Nota logística:** si el venue exige un corte de café de 10–15 minutos fuera de las 3 horas, reducir el ejercicio principal a 35 minutos y el bloque de mejora a 15 minutos.

---

# 2. Objetivos del workshop

Al finalizar, cada participante será capaz de:

1. Identificar un proceso repetitivo o una necesidad concreta de clientes o del negocio.
2. Determinar si un asistente de IA es la solución adecuada.
3. Escribir un prompt estructurado con contexto, rol, instrucciones, límites y formato de respuesta.
4. Definir qué información debe conocer el asistente y cómo entregársela.
5. Identificar herramientas que podría usar y riesgos que debe considerar.
6. Construir un prototipo funcional de asistente de IA.
7. Probarlo, recibir feedback y aplicar una mejora.
8. Definir un siguiente paso para validar si su asistente genera valor real.

---

# 3. Materiales necesarios

## Antes del workshop

### MaterialesSPIKE para participantes
- 1 computador o tablet por participante.
- Acceso a una herramienta de IA generativa:
  - ChatGPT, Claude, Gemini u otra equivalente.
- Acceso a una segunda herramienta para comparación, opcional.
- Navegador actualizado.
- Bloc de notas digital o físico.
- Plantilla de diseño del asistente en Google Docs/Notion.
- Documento de instrucciones de acceso y enlaces.
- Formulario de feedback.
- Cronómetro visible para el facilitador.

### MaterialesSPIKE para facilitador
- Presentación principal.
- Computador, proyector y adaptador HDMI/USB-C.
- Audio si el venue lo requiere.
- Diapositivas de apoyo para los ejercicios.
- Formulario de feedback.
- Cronómetro visible para el facilitador.

### MaterialesSPIKE de apoyo
- Casos de uso "");
- One-page template.
- Quiz breve.
- Chat bootcamp guide.
- Refrigerios: café, agua, snacks.
- Etiquetas o nombres de mesa.
- Pizarra, marcadores o post-its.
- Hojas grandes para mapear flujos de trabajo.
- Música suave durante el trabajo individual.

### Salas
- Sala principal con mesas en grupos de 4–6 personas.
- Espacio abierto para compartir.
- Pizarra o pantalla secundaria, si es posible.
- Área de café.
-Mesas con tomacorrientes y Wi-Fi.
- Zona de trabajo individual.

### Archivo de acceso a herramientas
- Enlace a la plantilla.
- Link directo a la herramienta de IA.
- Documento con instrucciones resumidas.
- Lista de herramientas sugeridas.
- Contacto de soporte técnico.

---

# 4. Outline por bloques

## Apertura y encuadre — 15 minutos

### Objetivo
Crear un ambiente de trabajo collaborativo, energetico y sin tecnicismos innecesarios. Explicar claramente qué se hará y qué producto se llevará cada participante.

### Dinámica
- **Bienvenida:** 2 minutos.
- **Declaración de energía:** pedir a los participantes que compartan en una palabra cómo se sienten al llegar.
- **Promesa del taller:** 3 minutos.
  - “Hoy no diseñaremos tecnología compleja”.
  - “Diseñaremos una herramienta que resuelva un problema real”.
- **Reglas del taller:** 3 minutos.
  - Centrarse en el problema, no en la herramienta.
  - Compartir en voz alta.
  - Prototipar antes de perfeccionar.
  - Dar feedback constructivo.
  - Respetar la confidencialidad de los negocios de otros participantes.
- **Encuesta de entrada:** 4 minutos.
  - ¿Cuál es tu startup?
  - ¿Qué tarea te gustaría automatizar?
  - ¿Qué herramientas utilizas hoy con IA?
- **Roadmap visual:** 3 minutos.

### Key takeaway
> “No necesitas saber programar. Necesitas definir bien un problema y diseñar una solución que se pueda probar.”

---

## Bloque 1: ¿Qué puede resolver un asistente de IA? — 25 minutos

### Objetivo
Ayudar a los participantes a distinguir un buen caso de uso de IA de una idea vaga o innecesariamente compleja.

### Dinámica

### 1.1 Charla energica — 8 minutos
- Qué es un asistente de IA en términos simples.
- En qué se diferencia de:
  - un chatbot básico;
  - una automatización rígida;
  - un buscador;
  - una herramienta copiloto.
- Tipos de asistentes útiles:
  - atención al cliente;
  - precalificación de leads;
  - generación de contenido;
  - investigación de mercado;
  - soporte interno;
  - ventas y propuestas;
  - operación y back office;
  - análisis de feedback.
- La ecuación mental:
  - **Problema + contexto + tarea + resultado esperado = asistente útil.**

### 1.2 Demo comparativa — 7 minutos
Mostrar dos ejemplos con la misma herramienta:

- Un prompt débil:
  > “Escribe sobre marketing digital.”

- Un prompt orientado a tarea:
  > “Actúa como analista de una startup SaaS B2B. Analiza los resultados de esta campaña y recomienda tres acciones para mejorar la conversión. Usa una tabla con métrica, hallazgo y acción.”

Preguntar:
- ¿Cuál de los dos resultados sería más útil para tomar una decisión?
- ¿Qué cambió?

### 1.3 Microejercicio: breathtaking de problemas — 7 minutos
Cada participante escribe seis problemas o tareas repetitivas:

1. ¿Qué haces cada semana?
2. ¿Qué pregunta te hacen siempre tus clientes?
3. ¿Qué información copias y pegas?
4. ¿Qué tarea te consume más tiempo?
5. ¿Dónde pierdes oportunidades por responder tarde?
6. ¿Qué contenido necesitas producir constantemente?

Luego selecciona el candidato con mayor combinación de:

- frecuencia;
- consumo de tiempo;
- impacto económico;
- tolerancia razonable al error.

### 1.4 Discusión en mesa — 3 minutos
Dos o tres participantes comparten su candidato. El facilitador orienta con preguntas:
- ¿Quién se beneficia?
- ¿Qué tan frecuente es?
- ¿Cómo sabremos que funciona?
- ¿Qué debería hacer el asistente, y qué no?

### Key takeaway
> “La mejor herramienta de IA empieza con una tarea concreta, repetitiva y medible, no con una tecnología de moda.”

---

## Bloque 2: Anatomía de un asistente de IA — 30 minutos

### Objetivo
Enseñar a los participantes a diseñar un asistente con componentes claros, sin entrar en complejidad técnica.

### Dinámica

### 2.1 Charla: los seis componentes — 12 minutos

1. **Rol:** quién es el asistente y para quién trabaja.
2. **Objetivo:** qué resultado debe producir.
3. **Contexto:** qué sabe sobre la startup, clientes y situación.
4. **Instrucciones:** qué debe hacer, en qué orden y con qué límites.
5. **Fuentes o herramientas:** dónde puede buscar, enviar, consultar o ejecutar.
6. **Formato de salida:** cómo debe entregar el resultado.

Incluir una explicación visual de:

- **Prompt:** instrucciones principales.
- **Contexto:** información específica del caso.
- **Knowledge base:** documentos que puede consultar.
- **Herramientas:** acciones que puede ejecutar.
- **Memoria:** información que retiene entre sesiones, con precaución.
- **Guardrails:** límites, escalamiento y criterios de confianza.

### 2.2 Demo de arquitectura — 6 minutos
Construir visualmente un asistente de soporte o precalificación:

- Entrada: mensaje de un lead.
- Contexto: startup, producto, ICP, objeciones frecuentes.
- Instrucciones: clasificar, responder y escalar.
- Salida: recomendación, respuesta y siguiente acción.
- Límite: no prometer ni inventar información.

### 2.3 Ejercicio guiado:填写 el canvas — 8 minutos
Los participantes completan las primeras secciones de la plantilla:

- Nombre del asistente.
- Usuario principal.
- Problema que resuelve.
- Tarea principal.
- Resultado esperado.
- Qué NO debe hacer.
- Ejemplo de una buena interacción.

### 2.4 Discusión y clearing misconceptions — 4 minutos
Aclarar:
- “Más instrucciones” no siempre significa “mejores instrucciones”.
- El asistente no conoce automáticamente todo.
- No todo debe automatizarse.
- La IA puede equivocarse.
- El prototipo no necesita ser perfecto.

### Key takeaway
> “Un buen asistente no es una caja negra: es una combinación explícita de contexto, instrucciones, límites y una salida clara.”

---

## Pausa activa — 10 minutos

### Objetivo
Permitir descanso, networking y resolver problemas de acceso sin interrumpir el ritmo principal.

### Dinámica
- Música o sonido ambiental.
- Café, agua y snacks.
- Networking opcional con una pregunta:
  - “¿Qué tarea de tu startup te gustaría convertir en un asistente?”
- Un facilitador o soporte técnico disponible.

### Key takeaway
> “Después del descanso vamos a pasar de diseñar a construir.”

---

## Bloque 3: Demo en vivo — 25 minutos

### Objetivo
Demostrar el proceso completo de construcción de un asistente, desde la definición del problema hasta una interacción funcional.

### Dinámica

### 3.1 Presentación del caso — 3 minutos
Usar un ejemplo reconocible para una startup early-stage:

- **Asistente de precalificación y respuesta de leads para una startup SaaS.**
- Mostrar:
  - problema de negocio;
  - usuario;
  - resultado esperado;
  - criterios de una buena respuesta.

### 3.2 Construcción en vivo — 17 minutos

Construir el prototipo paso a paso:

1. Definir el rol y el objetivo.
2. Escribir el prompt base.
3. Agregar contexto del negocio.
4. Definir reglas de respuesta.
5. Incorporar información de referencia.
6. Establecer límites.
7. Probar con un caso realista.
8. Corregir un fallo observado en vivo.
9. Añadir un formato de salida estructurado.

Mostrar deliberadamente un error y cómo corregirlo. Esto normaliza la iteración y reduce la expectativa de perfección.

### 3.3 Microdemostración de herramientas — 5 minutos
Opciones, sin_LOCK83 Locked all platforms. 

**Más Color:** es la herramienta que se puede usar hoy en el taller.

**Más contexto:** pegar políticas, FAQ, tono de marca o información del producto.

**Plantilla:** reutilizar una estructura parafaq, emails, análisis, etc.

**Integración:** conectar documentos, web, CRM, correo o calendario, según disponibilidad y cuenta.

Aclarar que no todas las herramientas requieren programación, pero sí configuración y criterio.

### Key takeaway
> “Construir un asistente es un ciclo: definir, instructing, probar, corregir y mejorar.”

---

# 5. Ejercicio principal: diseña y construye tu asistente — 40 minutos

## Nombre del ejercicio
## “Tu Asistente MVP en 90 minutos de Pensamiento”

Aunque el bloque dure 40 minutos, puede introducirse con una meta visible de prototipado.

### Objetivo
Que cada participante diseñe y pruebe un prototipo funcional de asistente de IA para un proceso real de su startup.

### Producto final
Una primera versión que incluya:

- usuario definido;
- problema concreto;
- prompt estructurado;
- contexto del negocio;
- ejemplos de entradas y salidas;
- límites y reglas de escalamiento;
- una prueba real;
- una mejora prioritaria.

### Dinámica

### Fase 1: selección del caso de uso — 5 minutos
Cada participante elige uno de estos escenarios o crea uno propio:

- Asistente de precalificación de leads.
- Agente de soporte de primer nivel.
- Generador de propuestas comerciales.
- Analizador de feedback de clientes.
- Asistente de onboarding de usuarios.
- Investigador de competencia.
- Creador de contenido para redes y campañas.
- Asistente interno de preguntas frecuentes.
- Evaluador de ideas o-features.
- Asistente de preparación de reuniones.

Debe cumplir tres criterios:

1. Tarea repetitiva.
2. Resultado observable.
3. Posibilidad de probarla con un input real.

### Fase 2:填写 el canvas — 8 minutos
Completar la plantilla:

**Bloque A — Problema**
- ¿Qué problema resuelve?
- ¿Quién lo usa?
- ¿Con qué frecuencia?
- ¿Cómo se resuelve hoy?

**Bloque B — Comportamiento**
- ¿Qué debe hacer?
- ¿Qué no debe hacer?
- ¿Qué necesita saber?
- ¿Qué formato debe devolver?

**Bloque C — Ejemplo**
- Ejemplo de input.
- Respuesta ideal.
- Errores que debe evitar.

### Fase 3: construcción del prototipo — 12 minutos
- Escribir el prompt.
- Añadir contexto.
- Definir reglas y límites.
- Pegar la información de referencia disponible.
- Probar con dos o tres casos.
- Guardar una versión que funcione.

### Fase 4: swap y feedback — 10 minutos
Participants work in pairs or groups of three:

1. Presentar el problema en 60 segundos.
2. El compañero prueba el asistente con un input.
3. Dar feedback usando tres preguntas:
   - ¿La respuesta resuelve la tarea?
   - ¿Falta información importante?
   - ¿Qué cambiarías primero?
4. Intercambiar roles.

### Fase 5: iteración — 5 minutos
Incorporar al menos un cambio:

- agregar contexto;
- mejorar instrucciones;
- definir un formato de salida;
- reducir ambigüedad;
- añadir una regla;
- cambiar la tarea;
- limitar el alcance.

### Material de apoyo: prompt base

```text
Actúa como [ROL] para [USUARIO/STARTUP].

Tu objetivo es [OBJETIVO PRINCIPAL].

Contexto:
- Startup/producto: [DESCRIPCIÓN]
- Cliente ideal: [CLIENTE IDEAL]
- Tono: [TONO]
- Información disponible: [CONTEXTO Y FUENTES]

Cuando recibas una solicitud:
1. [PASO 1]
2. [PASO 2]
3. [PASO 3]

Reglas:
- Usa únicamente la información proporcionada.
- Si falta información, haz preguntas antes de continuar.
- No inventes datos, precios, políticas o compromisos.
- [LÍMITE RELEVANTE].
- Si la solicitud está fuera de alcance, explica por qué y sugiere el siguiente paso.
- Si existe una urgencia o riesgo, escala a una persona.

Formato de salida:
[FORMATO: tabla, checklist, bullets, correo, JSON, etc.]

Ejemplo:
Entrada: [EJEMPLO]
Salida esperada: [EJEMPLO]
```

### Key takeaway
> “No se busca el asistente perfecto. Se busca una versión útil que puedas probar con una persona real mañana.”

---

## Bloque 4: Prueba, feedback y mejora — 20 minutos

### Objetivo
Ayudar a los participantes a evaluar la utilidad del prototipo y convertir observations en mejoras concretas.

### Dinámica

### 4.1 Charla: cómo evaluar un asistente — 5 minutos
Diferenciar entre:

- **Corrección:** la respuesta cumple la tarea.
- **Utilidad:** la respuesta ahorra tiempo o mejora una decisión.
- **Experiencia:** resulta clara y fácil de usar.
- **Riesgo:** el costo de equivocarse es aceptable o no.

Escala rápida de 1 a 5:

- Claridad.
- Utilidad.
- Confianza.
- Viabilidad de implementación.
- Nivel de riesgo.

### 4.2 Prueba rápida — 5 minutos
Cada participante ejecuta tres pruebas:

1. Un caso obvio.
2. Un caso ambiguo.
3. Un caso fuera de alcance.

Debe observar:
- ¿Alucinó?
- ¿Seguyó el formato?
- ¿Hizo buenas preguntas?
- ¿Escaló correctamente?
- ¿La respuesta es accionable?

### 4.3 Feedback en grupos pequeños — 6 minutos
En grupos de cuatro a seis:

- Un participante presenta su asistente en dos minutos.
- Los demás responden:
  - “Lo que más me sirvió fue…”
  - “Lo que no está claro es…”
  - “Probaría esto…”
- El participante elige solo un cambio prioritario.

### 4.4 Iteración final — 4 minutos
Aplicar el cambio y repetir una prueba.

### Key takeaway
> “Probar un asistente es tan importante como construirlo. Cada error es información para la siguiente iteración.”

---

## Cierre y plan de activación — 15 minutos

### Objetivo
Cerrar con resultados visibles, próximos pasos concretos y compromiso de activación.

### Dinámica

### 5.1 Mini showcase — 6 minutos
- Seleccionar tres o cuatro participantes.
- Cada uno presenta:
  - nombre del asistente;
  - problema;
  - qué puede hacer hoy;
  - siguiente prueba.
- Preferir variedad de casos, no solo los mejores prototipos.

### 5.2 Plan de 7 días — 5 minutos
Cada participante define:

1. ¿Con quién voy a probar el asistente?
2. ¿Qué tres tareas reales usaré?
3. ¿Qué mediré?
4. ¿Qué feedback pediré?
5. ¿Qué improving haré al final de la semana?

### 5.3 Cierre y feedback — 4 minutos
- Recordar los tres aprendizajes:
  1. Empezar por el problema.
  2. Dar contexto y límites.
  3. Probar y mejorar.
- Realizar encuesta corta:
  - ¿Qué te resultó más útil?
  - ¿Qué quedó poco claro?
  - ¿Qué crearías a continuación?
- Anunciar recursos y community.

### Key takeaway
> “El asistente no termina cuando terminas el workshop. Empieza con la primera conversación real.”

---

# 6. Recursos para llevar a casa

## Carpeta “Kit del asistente de IA”

### 1. One-page de diseño
- Problema y usuario.
- Objetivo.
- Tareas principales.
- Entradas.
- Salidas.
- Contexto.
- Reglas.
- Límites.
- Métrica de éxito.

### 2. Biblioteca de prompts
- Resumen de clientes.
- Clasificación de leads.
- Respuesta a FAQs.
- Análisis de feedback.
- Propuesta comercial.
- Síntesis de reuniones.
- Investigación de competencia.
- Email de seguimiento.
- Content repurposing.
- Checklist de calidad.

### 3. Checklist de calidad
Antes de poner un asistente en producción:

- [ ] El objetivo está definido en una frase.
- [ ] El usuario es claro.
- [ ] Las fuentes están actualizadas.
- [ ] El prompt no depende de contexto oculto.
- [ ] Existe un ejemplo de entrada y salida.
- [ ] Se define qué hacer ante información faltante.
- [ ] Se define cuándo escalar.
- [ ] Se probaron casos ambiguos y fuera de alcance.
- [ ] Hay un responsable humano.
- [ ] Existe una métrica de éxito.

### 4. Tarjeta de experimentation
Para cada prueba, registrar:

- fecha;
- usuario;
- tarea;
- resultado;
- error;
- feedback;
- siguiente cambio.

### 5. Matriz de priorización
Evaluar casos de uso según:

| Criterio | Pregunta |
|---|---|
| Frecuencia | ¿Cuántas veces ocurre? |
| Tiempo | ¿Cuánto tiempo consume hoy? |
| Impacto | ¿Afecta ingresos, retención o eficiencia? |
| Viabilidad | ¿Disponemos de datos e inputs? |
| Riesgo | ¿Qué sucede si se equivoca? |
| Escalabilidad | ¿Puede crecer con la startup? |

### 6. Plan de 7 días
- Día 1: elegir el caso y definir la MVP.
- Día 2: preparar contexto y prompt.
- Día 3: internally testear.
- Día 4: probarlo con un cliente o compañero.
- Día 5: analizar feedback.
- Día 6: implementar mejoras.
- Día 7: definir la siguiente iteración.

### 7. Grabación de la sesión
- Video de la demo.
- Enlace a la presentación.
- Enlace a la plantilla.
- Formulario de feedback.
- Canal de comunidad o seguimiento.
- Grabación opcional de preguntas frecuentes.

---

# 7. Slide count estimado por sección

| Sección | Slides estimados | Duración |
|---|---:|---:|
| Portada y apertura | 3–4 | 5 min |
| Reglas y objetivo del taller | 2–3 | 10 min |
| Bloque 1: casos de uso | 5–7 | 25 min |
| Pausa activa | 1–2 | 10 min |
| Bloque 2: anatomía del asistente | 7–9 | 30 min |
| Demo en vivo | 3–5 | 25 min |
| Ejercicio principal | 3–5 | 40 min |
| Feedback e iteración | 3–4 | 20 min |
| Cierre y plan de activación | 4–5 | 15 min |
| Recursos y anexos | 3–5 | Backup |
| **Total visible** | **31–42** | **3 horas** |
| **Total con respaldo** | **38–50** |  |

## Recomendación de diseño

- **1 idea principal por slide.**
- Pocas palabras y mucho apoyo visual.
- Slides distintos para demo, especialmente antes de construir en vivo.
- No leer el contenido en voz alta: usarlo como guía de conversación.
- Incluir la plantilla del ejercicio como slide o como handout digital.
- Mantener visibles durante todo el taller:
  - problema;
  - usuario;
  - resultado;
  - siguiente acción.

---

# 8. Facilitación y dinámica para 20–30 personas

## Organization del espacio

- **Mesas de 5–6 personas** durante coached blocks.
- **Parejas** para peer testing.
- **Grupos de 4–6** para feedback final.
- Rotar turnos para evitar que solo los más participativos hablen.

## Ritmo recomendado

- Nunca más de **12–15 minutos consecutivos de exposición**.
- Alternar:
  - input breve;
  - práctica;
  - sharing;
  - demo;
  - feedback.
- Usar una señal visual:
  - “Think” para reflexión individual.
  - “Pair” para trabajo en pareja.
  - “Build” para construcción.
  - “Share” para puesta en común.

## Preguntas guía del facilitador

- ¿Qué problema concreto estás resolviendo?
- ¿Quién sería el usuario principal?
- ¿Cómo hace esto hoy la persona?
- ¿Qué resultado observable esperas?
- ¿Qué información necesita saber el asistente?
- ¿Qué debería hacer cuando no sabe?
- ¿Cómo lo probarías mañana?
- ¿Cuál es el error más costoso que podría cometer?

---

# 9. Evaluación del workshop

## Métricas cuantitativas
- Porcentaje de participantes que construyeron un prototipo.
- Porcentaje que lo probó con un input real.
- Número promedio de iteraciones.
- Satisfacción con la facilidad del ejercicio.
- Utilidad percibida de la plantilla.
- Intención de usar el asistente con un cliente en los próximos siete días.

## Preguntas de feedback

1. ¿QuéAprendiste hoy que puedas aplicar mañana?
2. ¿Qué parte fue más útil?
3. ¿Qué parte fue confusa o demasiado técnica?
4. ¿Qué mejorarías del facilitador?
5. ¿Qué asistente te gustaría construir después?
6. ¿Tu prototipo ya tiene un usuario o caso de prueba definido?

---

# 10. Cierre operativo sugerido

La última instrucción debe ser simple:

> **Antes de salir: escribe en un post-it tu asistente, la persona que lo probará y la fecha de esa prueba.**

El facilitador puede cerrar con:

> “No van a salir con un producto terminado. Salen con un prototipo, un caso claro y un compromiso: hablar con un usuario real esta semana.”