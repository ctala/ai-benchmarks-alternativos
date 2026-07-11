# GPT-5.6 Sol — startup_content/workshop_outline

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.88 | quality: 10.0
- latency_total: 72.991s | tokens_per_second: 75.2
- input_tokens: 186 | output_tokens: 5491
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada y materiales necesarios para un workshop práctico.

## Respuesta completa

# Workshop presencial: **Construye tu Asistente de IA para tu Startup**
### Workshop práctico para emprendedores early-stage no técnicos

**Duración:** 3 horas  
**Audiencia:** 20–30 emprendedores  
**Modalidad:** Presencial, práctica y participativa  
**Nivel técnico:** Principiante; no requiere programación  
**Resultado concreto:** Cada participante sale con un asistente de IA funcional, probado y listo para usar en una tarea real de su startup.

> **Enfoque:** Menos teoría, más construcción. El asistente se creará con un **prompt maestro reutilizable**, por lo que puede funcionar en ChatGPT, Claude, Gemini u otra herramienta conversacional, sin APIs ni código.

---

## Objetivos del workshop

Al terminar, los participantes podrán:

1. Detectar tareas de su startup que vale la pena delegar a IA.
2. Diseñar instrucciones claras para un asistente.
3. Construir una primera versión sin programar.
4. Probarla con casos reales y mejorarla.
5. Identificar riesgos, límites y buenas prácticas.
6. Definir cómo incorporar el asistente a su flujo de trabajo semanal.

---

# 1. Agenda detallada — 3 horas

| Tiempo | Bloque | Actividad | Slides |
|---|---|---|---:|
| 00:00–00:10 | 1. Bienvenida y activación | Encuadre + dinámica inicial | 3 |
| 00:10–00:25 | 2. Qué es un asistente de IA | Charla breve + ejemplos | 5 |
| 00:25–00:40 | 3. Elegir el caso de uso correcto | Mapeo individual + conversación en parejas | 4 |
| 00:40–00:55 | 4. Anatomía de un buen asistente | Framework práctico + demo | 6 |
| 00:55–01:20 | 5. Diseña tu asistente | Ejercicio guiado: canvas + prompt maestro | 5 |
| 01:20–01:30 | **Break** | Pausa y soporte técnico | 1 |
| 01:30–01:50 | 6. Construye la versión 1 | Implementación individual | 4 |
| 01:50–02:15 | 7. Prueba y mejora | Testing por parejas + iteración | 5 |
| 02:15–02:35 | 8. Del experimento al flujo de trabajo | Demo + plan de adopción | 4 |
| 02:35–02:50 | 9. Seguridad, límites y criterio humano | Casos prácticos + checklist | 4 |
| 02:50–03:00 | 10. Show & tell y cierre | Presentaciones rápidas + compromiso | 2 |

**Total:** 180 minutos  
**Slide count estimado:** 43 slides

---

# 2. Materiales necesarios

## Para preparar antes del workshop

### Espacio

- Salón con mesas para trabajar en grupos de 2–4 personas.
- Proyector o pantalla grande.
- Audio, si el espacio lo requiere.
- Wi-Fi estable para 20–30 dispositivos.
- Extensiones eléctricas y multicontactos.
- 1 rotafolio o pizarra.
- Marcadores.
- Notas adhesivas en dos colores.
- Cronómetro visible.

### Para los participantes

Enviar 2–3 días antes:

- Solicitud de llevar laptop con cargador.
- Instrucción de crear una cuenta en al menos una plataforma:
  - ChatGPT
  - Claude
  - Gemini
  - Otra herramienta aprobada por la organización
- Solicitud de traer:
  - Una descripción breve de su startup.
  - Una tarea repetitiva que realicen cada semana.
  - Dos o tres ejemplos reales de inputs o solicitudes relacionadas con esa tarea.
  - Información no confidencial que puedan usar durante el ejercicio.
- Recordatorio: **no subir datos sensibles, contraseñas, información financiera privada o datos personales de clientes.**

### Materiales impresos o digitales

1. **Canvas del Asistente de IA**, una página por participante.
2. Plantilla del prompt maestro.
3. Checklist de testing.
4. Matriz para elegir casos de uso.
5. Checklist de privacidad y seguridad.
6. Plan de implementación de siete días.
7. Código QR con todos los recursos.
8. Encuesta rápida de salida.

### Preparación del facilitador

- Crear un asistente de ejemplo relacionado con una startup.
- Preparar dos demos:
  - Un prompt débil.
  - Una versión mejorada usando el framework.
- Tener capturas o video corto de respaldo si falla internet.
- Preparar ejemplos de casos de uso por área:
  - Ventas.
  - Marketing.
  - Atención al cliente.
  - Investigación.
  - Operaciones.
  - Fundraising.
  - Product discovery.
- Tener una alternativa de trabajo en parejas para participantes sin laptop o sin acceso a una herramienta.
- Designar, idealmente, un cofacilitador para soporte técnico.

---

# 3. Desarrollo de cada bloque

## Bloque 1. Bienvenida y activación

**Duración:** 10 minutos  
**Slides:** 3

### Objetivo

Alinear expectativas, generar energía y dejar claro que todos construirán algo funcional durante la sesión.

### Dinámica

**Encuadre + activación rápida**

1. Pregunta al grupo:  
   **“¿Qué tarea de tu startup te encantaría no volver a hacer desde cero?”**
2. Los participantes escriben una tarea en una nota adhesiva.
3. Comparten con la persona de al lado.
4. El facilitador recoge tres o cuatro ejemplos y los conecta con el objetivo del workshop.

### Contenidos

- Qué construiremos.
- Qué no haremos: código, APIs o automatizaciones complejas.
- Regla del workshop: **construir, probar, mejorar**.
- Resultado esperado al final de las tres horas.

### Key takeaway

> No necesitamos “saber de IA”; necesitamos identificar una tarea clara y enseñar a la IA cómo ayudarnos.

---

## Bloque 2. Qué es —y qué no es— un asistente de IA

**Duración:** 15 minutos  
**Slides:** 5

### Objetivo

Dar un modelo mental simple para entender cómo funciona un asistente y evitar expectativas irreales.

### Dinámica

**Charla breve + ejemplos en vivo**

Comparar:

- Chat genérico: responde a una solicitud aislada.
- Asistente: tiene un rol, un objetivo, contexto, proceso, reglas y formato de salida.

### Contenidos

- Diferencia entre:
  - Prompt.
  - Asistente.
  - Automatización.
  - Agente.
- Capacidades útiles:
  - Redactar.
  - Resumir.
  - Clasificar.
  - Analizar información.
  - Generar opciones.
  - Hacer preguntas.
  - Aplicar criterios.
- Límites:
  - Puede inventar información.
  - No conoce todo el contexto del negocio.
  - No reemplaza decisiones críticas.
  - Necesita revisión humana.

### Ejemplos rápidos

- Asistente para preparar entrevistas con clientes.
- Asistente para responder leads.
- Asistente para convertir notas en contenido.
- Asistente para analizar feedback.
- Asistente para preparar reuniones con inversionistas.

### Key takeaway

> Un asistente útil no es “una IA que hace de todo”; es una herramienta diseñada para una tarea específica y repetible.

---

## Bloque 3. Elegir el caso de uso correcto

**Duración:** 15 minutos  
**Slides:** 4

### Objetivo

Seleccionar una tarea con suficiente valor, frecuencia y claridad para construir durante el workshop.

### Dinámica

**Mapeo individual + conversación en parejas**

Cada participante anota entre tres y cinco tareas que realiza en su startup y las evalúa con cuatro criterios:

| Criterio | Pregunta |
|---|---|
| Frecuencia | ¿La hago semanalmente o varias veces al mes? |
| Tiempo | ¿Consume al menos 30 minutos cada vez? |
| Repetibilidad | ¿Sigue pasos o criterios similares? |
| Riesgo | ¿Un error sería fácil de detectar y corregir? |

Puntuar cada criterio del 1 al 5.

### Regla para elegir

Priorizar una tarea:

- Frecuente.
- Repetitiva.
- Basada principalmente en texto o información.
- Fácil de revisar.
- De riesgo bajo o medio.
- Con ejemplos reales disponibles.

### Casos que conviene evitar en el workshop

- Decisiones legales, médicas o financieras.
- Selección final de candidatos sin revisión.
- Uso de datos confidenciales.
- Tareas demasiado amplias como “manejar todo mi marketing”.
- Automatizaciones que necesiten múltiples sistemas.

### Key takeaway

> El mejor primer caso de uso no es el más ambicioso: es el que se puede probar esta semana.

---

## Bloque 4. Anatomía de un buen asistente

**Duración:** 15 minutos  
**Slides:** 6

### Objetivo

Aprender una estructura simple para crear instrucciones consistentes y reutilizables.

### Dinámica

**Framework práctico + demo antes/después**

El facilitador muestra primero un prompt vago:

> “Ayúdame a responder clientes.”

Luego construye una versión sólida usando el framework.

## Framework: **RUTA**

### R — Rol y resultado

- ¿Quién debe ser el asistente?
- ¿Qué resultado concreto debe producir?

### U — Usuario y contexto

- ¿Qué hace la startup?
- ¿Quién recibirá el resultado?
- ¿Qué información necesita conocer?

### T — Tarea y proceso

- ¿Qué pasos debe seguir?
- ¿Qué preguntas debe hacer antes de responder?
- ¿Qué criterios debe aplicar?

### A — Acuerdos de calidad

- Tono.
- Formato de salida.
- Límites.
- Información que no debe inventar.
- Qué debe hacer si falta contexto.

### Key takeaway

> La calidad del asistente depende menos de “palabras mágicas” y más de contexto, proceso y criterios claros.

---

## Bloque 5. Diseña tu asistente

**Duración:** 25 minutos  
**Slides:** 5

### Objetivo

Convertir el caso de uso seleccionado en un diseño claro antes de abrir la herramienta de IA.

### Dinámica

**Ejercicio guiado con el Canvas del Asistente**

Cada participante completa:

1. **Nombre del asistente.**
2. **Usuario principal.**
3. **Problema que resuelve.**
4. **Resultado esperado.**
5. **Inputs que recibirá.**
6. **Pasos que debe seguir.**
7. **Preguntas que debe hacer.**
8. **Criterios de calidad.**
9. **Formato de salida.**
10. **Límites y alertas.**
11. **Ejemplo de un buen resultado.**

### Trabajo en parejas

Cada participante explica su asistente en 60 segundos. La pareja debe responder:

- ¿Entiendo exactamente qué hará?
- ¿Qué información le falta?
- ¿Cómo sabremos si el resultado es bueno?
- ¿El alcance es demasiado amplio?

### Rol del facilitador

Circular por el salón y ayudar a reducir alcance:

- De “asistente de marketing” a “asistente para convertir una entrevista con un cliente en tres publicaciones de LinkedIn”.
- De “asistente de ventas” a “asistente para preparar el seguimiento de un lead después de una llamada”.
- De “asistente de producto” a “asistente para clasificar feedback de usuarios por problema y urgencia”.

### Key takeaway

> Si no puedes explicar la tarea en una frase, todavía es demasiado amplia.

---

## Break

**Duración:** 10 minutos  
**Slides:** 1

Durante la pausa:

- Verificar que todos tengan acceso a una herramienta.
- Resolver problemas de cuentas o conectividad.
- Formar parejas para quienes necesiten apoyo.
- Mostrar en pantalla el QR de recursos.

---

## Bloque 6. Construye la versión 1

**Duración:** 20 minutos  
**Slides:** 4

### Objetivo

Transformar el canvas en un prompt maestro e implementar la primera versión del asistente.

### Dinámica

**Construcción individual, con soporte del facilitador**

Los participantes copian la plantilla, completan los espacios y la ejecutan en la herramienta elegida.

## Plantilla de prompt maestro

```text
Actúa como [ROL DEL ASISTENTE].

Tu objetivo es ayudarme a [RESULTADO CONCRETO].

Contexto de mi startup:
- Qué hacemos: [DESCRIPCIÓN]
- Cliente principal: [CLIENTE]
- Etapa o situación actual: [CONTEXTO RELEVANTE]

Cada vez que te comparta [TIPO DE INPUT], sigue este proceso:

1. [PASO 1]
2. [PASO 2]
3. [PASO 3]
4. Revisa el resultado usando estos criterios:
   - [CRITERIO 1]
   - [CRITERIO 2]
   - [CRITERIO 3]

Antes de generar el resultado:
- Hazme las preguntas necesarias si falta información.
- No inventes datos, testimonios, cifras o fuentes.
- Indica claramente cualquier supuesto.
- Si no puedes completar la tarea con confianza, explícame qué falta.

Entrega el resultado en este formato:
[FORMATO DE SALIDA]

Usa un tono:
[TONO]

Evita:
[LÍMITES, PALABRAS, COMPORTAMIENTOS O RIESGOS]

Ejemplo de un buen resultado:
[EJEMPLO]

Confirma que entendiste tu función y dime qué información necesitas
para comenzar.
```

### Meta de este bloque

Cada persona debe lograr que su asistente:

- Entienda su rol.
- Solicite un input.
- Entregue un primer resultado.
- Use el formato pedido.

### Key takeaway

> La versión 1 no tiene que ser perfecta; tiene que ser suficientemente clara para poder probarla.

---

## Bloque 7. Prueba y mejora

**Duración:** 25 minutos  
**Slides:** 5

### Objetivo

Pasar de “se ve bien” a “funciona con casos reales”.

### Dinámica

**Testing individual + revisión por parejas**

Cada participante ejecuta tres pruebas:

### Prueba 1: Caso normal

Un ejemplo típico y completo.

### Prueba 2: Caso difícil

Información incompleta, ambigua o desordenada.

### Prueba 3: Caso límite

Una solicitud fuera de alcance, sensible o que pueda provocar una respuesta inventada.

## Checklist de evaluación

Puntuar del 1 al 5:

- ¿Entendió la tarea?
- ¿Pidió contexto cuando faltaba?
- ¿Siguió el proceso?
- ¿Entregó el formato correcto?
- ¿El resultado es accionable?
- ¿Evitó inventar información?
- ¿Suena coherente con la startup?
- ¿Cuánto tiempo ahorraría realmente?

### Testing por parejas

La pareja prueba el asistente sin recibir explicaciones adicionales.

Esto permite comprobar si las instrucciones son suficientemente claras para otra persona.

### Fórmula de iteración

Después de cada prueba:

1. Identificar el error.
2. Decidir si falta contexto, proceso, criterio o límite.
3. Modificar una parte del prompt.
4. Repetir la prueba.
5. Guardar la versión mejorada.

### Key takeaway

> No mejores el asistente “por intuición”. Usa casos reales, encuentra el fallo y corrige la instrucción específica.

---

## Bloque 8. Del experimento al flujo de trabajo

**Duración:** 20 minutos  
**Slides:** 4

### Objetivo

Evitar que el asistente quede como una demo interesante que nadie vuelve a usar.

### Dinámica

**Mini charla + diseño de un flujo semanal**

Cada participante completa:

- **Disparador:** ¿Cuándo usaré el asistente?
- **Input:** ¿Qué información le entregaré?
- **Proceso:** ¿Qué hará?
- **Revisión humana:** ¿Qué debo verificar?
- **Output:** ¿Dónde guardaré o usaré el resultado?
- **Métrica:** ¿Cómo sabré si aporta valor?

### Ejemplo

**Asistente de seguimiento comercial**

- Disparador: al terminar una llamada.
- Input: notas de la conversación.
- Proceso: detectar necesidades, objeciones y próximos pasos.
- Output: email de seguimiento + actualización resumida.
- Revisión humana: validar compromisos y datos.
- Métrica: tiempo de preparación y tasa de respuesta.

### Plan de adopción

Cada participante define:

- Una persona responsable.
- Una frecuencia de uso.
- Una métrica.
- Una fecha para revisar resultados.
- Un cambio que implementará esta semana.

### Key takeaway

> El valor no aparece cuando creas el asistente; aparece cuando lo incorporas a una rutina.

---

## Bloque 9. Seguridad, límites y criterio humano

**Duración:** 15 minutos  
**Slides:** 4

### Objetivo

Usar IA con responsabilidad sin frenar la experimentación.

### Dinámica

**Casos rápidos + checklist semáforo**

El facilitador presenta situaciones y el grupo vota:

- Verde: uso de bajo riesgo.
- Amarillo: requiere cuidado y revisión.
- Rojo: no usar o escalar a un especialista.

### Checklist práctico

#### No compartir

- Contraseñas.
- Datos bancarios.
- Información médica.
- Datos personales innecesarios.
- Contratos o información confidencial sin autorización.
- Propiedad intelectual sensible.
- Listas completas de clientes.

#### Siempre revisar

- Cifras.
- Fechas.
- Nombres.
- Fuentes.
- Promesas comerciales.
- Interpretaciones legales.
- Mensajes que se enviarán en nombre de la empresa.

#### Regla de oro

> Si un error puede causar daño financiero, legal, reputacional o personal, debe existir revisión humana antes de actuar.

### Key takeaway

> La IA puede proponer; el equipo sigue siendo responsable de verificar y decidir.

---

## Bloque 10. Show & tell y cierre

**Duración:** 10 minutos  
**Slides:** 2

### Objetivo

Celebrar avances, compartir aprendizajes y generar compromiso de uso.

### Dinámica

**Presentaciones relámpago + compromiso final**

Seleccionar tres participantes. Cada uno tiene 60–90 segundos para compartir:

1. Qué problema eligió.
2. Qué hace su asistente.
3. Qué mejoró después de probarlo.
4. Qué hará con él esta semana.

### Cierre individual

Cada participante completa la frase:

> “En los próximos siete días usaré mi asistente para ______ y mediré ______.”

Encuesta rápida mediante QR:

- Nivel de confianza antes y después.
- Utilidad del asistente creado.
- Próximo caso de uso que quieren explorar.
- Feedback sobre el workshop.

### Key takeaway

> Empieza pequeño, úsalo con frecuencia y mejora con evidencia.

---

# 4. Ejercicio principal del workshop

## Reto: Construye un asistente para una tarea real de tu startup

El ejercicio ocupa los bloques 3, 5, 6 y 7. Está diseñado para que todos puedan completarlo sin conocimientos técnicos.

### Resultado mínimo esperado

Al final, cada participante tendrá:

- Un caso de uso definido.
- Un Canvas del Asistente completo.
- Un prompt maestro reutilizable.
- Tres pruebas documentadas.
- Una versión mejorada.
- Un plan para usarlo durante los próximos siete días.

## Etapas del ejercicio

### Etapa 1: Elegir

Seleccionar una tarea frecuente, repetitiva, revisable y de bajo riesgo.

### Etapa 2: Diseñar

Definir:

- Rol.
- Resultado.
- Contexto.
- Proceso.
- Criterios.
- Formato.
- Límites.

### Etapa 3: Construir

Llevar el diseño a ChatGPT, Claude, Gemini u otra herramienta mediante el prompt maestro.

### Etapa 4: Probar

Usar tres casos:

1. Normal.
2. Difícil.
3. Límite.

### Etapa 5: Mejorar

Actualizar las instrucciones con base en los errores observados.

### Etapa 6: Implementar

Definir cuándo, cómo y con qué métrica se utilizará.

## Casos de uso recomendados

Para participantes que no sepan qué construir, ofrecer estas opciones:

1. **Asistente de entrevistas con clientes**  
   Prepara preguntas y organiza hallazgos.

2. **Asistente de seguimiento comercial**  
   Convierte notas de reuniones en un email y próximos pasos.

3. **Asistente de contenido**  
   Transforma una idea o conversación en publicaciones.

4. **Asistente de feedback de producto**  
   Clasifica comentarios por tema, impacto y urgencia.

5. **Asistente de reuniones**  
   Convierte notas en decisiones, responsables y fechas.

6. **Asistente de investigación**  
   Crea un plan de análisis y organiza información aportada por el usuario.

7. **Asistente de pitch**  
   Revisa claridad, estructura y posibles preguntas de inversionistas.

## Criterio de éxito

El asistente se considera funcional si:

- Produce un resultado útil en menos de cinco minutos.
- Sigue el formato solicitado.
- Pide contexto si lo necesita.
- No inventa información esencial.
- Una segunda persona puede utilizarlo.
- Ahorra tiempo o mejora la consistencia de la tarea.

---

# 5. Recursos para llevar a casa

Entregar mediante una carpeta o página accesible por QR.

## Kit del participante

1. **Canvas editable del Asistente de IA.**
2. **Plantilla del prompt maestro RUTA.**
3. **Matriz de priorización de casos de uso.**
4. **Checklist de testing con tres tipos de prueba.**
5. **Checklist de privacidad y revisión humana.**
6. **Biblioteca de casos de uso para startups.**
7. **Ejemplos de prompts antes/después.**
8. **Plan de adopción de siete días.**
9. **Hoja para registrar versiones y mejoras.**
10. **Glosario simple de IA para no técnicos.**

## Reto de siete días

- **Día 1:** Usar el asistente con un caso real.
- **Día 2:** Detectar el principal error.
- **Día 3:** Mejorar instrucciones o criterios.
- **Día 4:** Probar con un caso difícil.
- **Día 5:** Pedir a otra persona que lo use.
- **Día 6:** Medir tiempo ahorrado y calidad.
- **Día 7:** Decidir si mantener, rediseñar o descartar.

## Métricas sugeridas

- Minutos ahorrados por tarea.
- Frecuencia de uso.
- Porcentaje del resultado que requiere edición.
- Consistencia del formato.
- Número de errores detectados.
- Calidad percibida del 1 al 5.
- Velocidad de respuesta a clientes o leads.

---

# 6. Resumen de slides por sección

| Sección | Slides estimados |
|---|---:|
| Bienvenida y activación | 3 |
| Qué es un asistente de IA | 5 |
| Elegir el caso de uso | 4 |
| Anatomía de un buen asistente | 6 |
| Diseña tu asistente | 5 |
| Break / instrucciones | 1 |
| Construye la versión 1 | 4 |
| Prueba y mejora | 5 |
| Del experimento al flujo de trabajo | 4 |
| Seguridad y límites | 4 |
| Show & tell y cierre | 2 |
| **Total estimado** | **43** |

---

## Recomendaciones de facilitación

- Mantener las explicaciones teóricas en bloques de máximo 10 minutos.
- Usar ejemplos latinoamericanos y lenguaje cotidiano.
- Evitar jerga como “tokens”, “embeddings” o “arquitecturas de agentes”.
- Mostrar resultados imperfectos: normaliza la iteración.
- Recordar cada 30–40 minutos: **“No buscamos perfección; buscamos utilidad comprobable.”**
- Tener participantes trabajando en parejas, aunque cada uno construya su asistente.
- Usar un cronómetro visible para mantener ritmo.
- Celebrar pequeños logros: primera respuesta, primera prueba y primera mejora.
- No depender de funciones premium; el ejercicio debe funcionar en un chat estándar.

> **Mensaje final del workshop:**  
> “No necesitas construir una plataforma de IA. Empieza construyendo un compañero útil para una tarea que hoy te quita tiempo.”