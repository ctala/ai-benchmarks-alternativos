# GPT-5.5 — startup_content/workshop_outline

- model_id: `gpt-5.5`
- success: True  | final: 6.7 | quality: 9.44
- latency_total: 72.901s | tokens_per_second: 76.2
- input_tokens: 186 | output_tokens: 5554
- judge_score: 4.6 | justificación: 

## Respuesta completa

# Workshop presencial de 3 horas  
## “Construye tu Asistente de IA para tu Startup - Workshop Práctico”

**Audiencia:** emprendedores early-stage no técnicos, 20-30 personas.  
**Formato:** presencial, práctico, con laptop.  
**Resultado esperado:** cada participante sale con un primer asistente de IA funcional para una tarea real de su startup.

---

# 1. Agenda detallada — 3 horas

| Tiempo | Bloque | Duración |
|---|---:|---:|
| 00:00 - 00:10 | Bienvenida, contexto y setup | 10 min |
| 00:10 - 00:25 | Qué puede hacer un asistente de IA por tu startup | 15 min |
| 00:25 - 00:45 | Elige el caso de uso correcto | 20 min |
| 00:45 - 01:05 | Anatomía de un buen asistente de IA | 20 min |
| 01:05 - 01:15 | Break corto | 10 min |
| 01:15 - 01:35 | Demo: de idea a asistente en vivo | 20 min |
| 01:35 - 02:15 | Ejercicio principal: construye tu asistente | 40 min |
| 02:15 - 02:40 | Testeo, mejora y “red teaming” | 25 min |
| 02:40 - 02:55 | Mini demos + aprendizajes del grupo | 15 min |
| 02:55 - 03:00 | Cierre y próximos pasos | 5 min |

---

# 2. Materiales necesarios

## Para preparar antes del workshop

### Tecnología

- Proyector o pantalla grande.
- Audio / micrófono si el espacio es grande.
- WiFi estable para 30 personas.
- Extensiones eléctricas o regletas.
- Laptop del facilitador.
- Timer visible o cronómetro.

### Herramientas digitales sugeridas

Pedir a los participantes que lleguen con cuenta creada en al menos una de estas:

- ChatGPT.
- Claude.
- Gemini.
- Perplexity.
- Microsoft Copilot.

Idealmente, que traigan laptop. También pueden usar celular, pero laptop es mucho mejor.

### Material impreso o digital

- Worksheet del workshop en Google Docs, Notion, PDF o impreso.
- Plantilla de “Diseño de Asistente de IA”.
- Plantilla de “Prompt Maestro”.
- Checklist de testeo.
- Lista de recursos y herramientas para llevarse.
- QR con acceso a todos los materiales.

### Información que deben traer los participantes

Pedirles antes del evento que lleguen con:

- Descripción breve de su startup.
- Cliente objetivo.
- Un problema repetitivo que tengan hoy.
- 3 a 5 preguntas frecuentes de clientes, usuarios, inversionistas o leads.
- Algún material propio si lo tienen:
  - Pitch deck.
  - Landing page.
  - Brochure.
  - FAQs.
  - Guiones de venta.
  - Descripción del producto.
  - Casos de uso.
  - Mensajes de WhatsApp o emails frecuentes, anonimizados.

---

# 3. Bloques del workshop

---

## Bloque 1: Bienvenida, contexto y setup

**Duración:** 10 minutos  
**Slide count estimado:** 3 slides

### Objetivo

Romper el hielo, alinear expectativas y dejar claro que el workshop será práctico: no venimos a hablar de IA, venimos a construir algo útil.

### Dinámica

- Bienvenida energética.
- Pregunta rápida al grupo:

  > “¿Qué tarea de tu startup te gustaría que alguien hiciera por ti desde mañana?”

- Explicar el resultado final:

  > “Hoy cada persona va a salir con un asistente de IA versión 1.0 para su startup.”

- Verificar setup:
  - Laptop abierta.
  - Cuenta de IA lista.
  - Acceso al worksheet.

### Key takeaway

La IA no reemplaza al founder, pero sí puede quitarle trabajo repetitivo para que se enfoque en vender, hablar con clientes y construir.

---

## Bloque 2: Qué puede hacer un asistente de IA por tu startup

**Duración:** 15 minutos  
**Slide count estimado:** 5 slides

### Objetivo

Mostrar posibilidades concretas y aterrizadas para startups early-stage, sin tecnicismos.

### Dinámica

Charla corta con ejemplos prácticos.

Ejemplos de asistentes que pueden construir:

1. **Asistente de ventas**
   - Responde objeciones.
   - Prepara mensajes de seguimiento.
   - Personaliza emails para leads.

2. **Asistente de customer discovery**
   - Sugiere preguntas para entrevistas.
   - Resume aprendizajes.
   - Detecta patrones de dolor.

3. **Asistente de soporte**
   - Responde preguntas frecuentes.
   - Explica cómo usar el producto.
   - Clasifica tickets o mensajes.

4. **Asistente de contenido**
   - Genera ideas para LinkedIn, Instagram o blog.
   - Adapta tono de marca.
   - Convierte aprendizajes en posts.

5. **Asistente para pitch**
   - Mejora el one-liner.
   - Simula preguntas de inversionistas.
   - Ayuda a preparar respuestas.

6. **Asistente interno del founder**
   - Prioriza tareas.
   - Resume reuniones.
   - Ayuda a tomar decisiones.

### Key takeaway

Un buen asistente de IA no empieza con la herramienta. Empieza con una tarea repetitiva, costosa o crítica para el negocio.

---

## Bloque 3: Elige el caso de uso correcto

**Duración:** 20 minutos  
**Slide count estimado:** 4 slides

### Objetivo

Ayudar a cada participante a elegir un caso de uso realista y valioso para construir durante el workshop.

### Dinámica

Ejercicio individual + conversación en parejas.

Los participantes completan una matriz simple:

| Tarea | Frecuencia | Dolor | Impacto en negocio | ¿Ideal para IA? |
|---|---:|---:|---:|---:|
| Responder leads | Alta | Alto | Alto | Sí |
| Hacer logo | Baja | Medio | Bajo | No prioritario |
| Preparar entrevistas | Media | Alto | Alto | Sí |

### Criterios para elegir buen caso de uso

El caso ideal debe ser:

- Repetitivo.
- Basado en texto o información.
- Fácil de revisar por una persona.
- Relacionado con ventas, clientes, soporte, contenido o aprendizaje.
- Posible de probar hoy mismo.

### Mini actividad

Cada persona responde:

1. ¿Qué tarea quiero delegar parcialmente a un asistente?
2. ¿Quién usará el asistente?
3. ¿Qué resultado debe entregar?
4. ¿Qué información necesita para hacerlo bien?

Luego lo comparte con una persona al lado en 2 minutos.

### Key takeaway

No construyas un asistente “inteligente para todo”. Construye un asistente específico para una tarea concreta.

---

## Bloque 4: Anatomía de un buen asistente de IA

**Duración:** 20 minutos  
**Slide count estimado:** 6 slides

### Objetivo

Entender los componentes básicos de un asistente útil, sin entrar en programación.

### Dinámica

Charla práctica + ejemplos.

### Componentes de un asistente

1. **Rol**
   - Quién es el asistente.
   - Ejemplo: “Eres un asistente de ventas B2B para una startup SaaS”.

2. **Objetivo**
   - Qué debe lograr.
   - Ejemplo: “Ayudar a convertir leads interesados en demos agendadas”.

3. **Contexto**
   - Información sobre la startup, cliente, producto, mercado, tono.

4. **Entradas**
   - Qué le dará el usuario.
   - Ejemplo: perfil del lead, mensaje recibido, objeción, país, industria.

5. **Proceso**
   - Cómo debe pensar o trabajar.
   - Ejemplo: analizar lead, identificar dolor, elegir ángulo, redactar respuesta.

6. **Formato de salida**
   - Cómo debe entregar la respuesta.
   - Ejemplo: email corto, mensaje de WhatsApp, tabla, checklist, guion.

7. **Reglas**
   - Qué debe y no debe hacer.
   - Ejemplo: no inventar precios, no prometer integraciones inexistentes, pedir aclaraciones si falta información.

8. **Ejemplos**
   - Muestras de buenas respuestas.
   - Esto mejora muchísimo la calidad.

### Fórmula simple

> Buen asistente = rol claro + contexto útil + tarea específica + formato de salida + límites.

### Key takeaway

La calidad del asistente depende más de cómo lo defines que de la herramienta que uses.

---

## Bloque 5: Break corto

**Duración:** 10 minutos  
**Slide count estimado:** 1 slide

### Objetivo

Pausa rápida antes de la parte práctica.

### Dinámica

- Café / agua.
- Revisar que todos tengan acceso a la herramienta de IA.
- El facilitador y asistentes ayudan a quien tenga problemas técnicos.

### Key takeaway

Volvemos listos para construir.

---

## Bloque 6: Demo: de idea a asistente en vivo

**Duración:** 20 minutos  
**Slide count estimado:** 5 slides

### Objetivo

Mostrar el proceso completo en vivo antes de que los participantes lo hagan.

### Dinámica

Demo práctica en pantalla.

### Ejemplo de demo

Construir un:

> “Asistente de ventas para una startup que vende software de gestión para restaurantes pequeños en Latinoamérica.”

### Paso a paso de la demo

1. Definir tarea:
   - Responder leads que preguntan por precio y beneficios.

2. Dar contexto:
   - Producto.
   - Cliente ideal.
   - Beneficios.
   - Tono.
   - Objeciones frecuentes.

3. Crear prompt maestro.

4. Probar con 2 escenarios:
   - Lead interesado pero preocupado por precio.
   - Lead que compara con Excel o WhatsApp.

5. Mejorar el asistente:
   - Hacer respuestas más cortas.
   - Adaptar a tono latinoamericano.
   - Agregar CTA para agendar demo.
   - Evitar promesas falsas.

### Key takeaway

La primera versión nunca es perfecta. El valor aparece cuando pruebas, corriges y ajustas.

---

# 4. Ejercicio principal del workshop

## Bloque 7: Construye tu asistente de IA para tu startup

**Duración:** 40 minutos  
**Slide count estimado:** 5 slides

### Objetivo

Que cada participante construya un asistente funcional usando una plantilla guiada.

### Dinámica

Ejercicio individual, con apoyo del facilitador.  
Puede hacerse en ChatGPT, Claude, Gemini o cualquier herramienta similar.

---

## Ejercicio: “Mi Asistente IA v1.0”

Cada participante elegirá uno de estos tipos de asistente:

### Opción A: Asistente de ventas

Ideal si necesitas:

- Responder leads.
- Preparar mensajes de seguimiento.
- Manejar objeciones.
- Agendar demos.

### Opción B: Asistente de soporte / FAQ

Ideal si necesitas:

- Responder preguntas frecuentes.
- Explicar cómo funciona tu producto.
- Ayudar a usuarios nuevos.

### Opción C: Asistente de customer discovery

Ideal si necesitas:

- Preparar entrevistas.
- Analizar respuestas.
- Detectar patrones de dolor.
- Mejorar tu propuesta de valor.

### Opción D: Asistente de contenido

Ideal si necesitas:

- Crear posts.
- Reutilizar ideas.
- Adaptar tono de marca.
- Generar contenido desde aprendizajes reales.

### Opción E: Asistente de pitch

Ideal si necesitas:

- Mejorar tu pitch.
- Preparar respuestas para inversionistas.
- Practicar preguntas difíciles.

---

## Plantilla de Prompt Maestro

Los participantes copian y completan esta plantilla:

```text
Eres [tipo de asistente] para mi startup.

Contexto de la startup:
- Nombre:
- Qué hacemos:
- Cliente ideal:
- Problema que resolvemos:
- Producto/solución:
- Beneficios principales:
- Diferenciadores:
- País/mercado:
- Etapa actual:

Tu objetivo principal es:
[Describe la tarea específica que debe hacer el asistente]

Debes ayudarme a:
1. [Tarea 1]
2. [Tarea 2]
3. [Tarea 3]

Información importante:
- Tono de comunicación:
- Palabras que usamos:
- Palabras que evitamos:
- Objeciones frecuentes:
- Preguntas frecuentes:
- Precios o condiciones, si aplica:
- Cosas que NO debes prometer:
- Cosas que debes preguntar si falta información:

Cuando te dé una solicitud, sigue este proceso:
1. Analiza el contexto.
2. Identifica qué necesita el usuario o cliente.
3. Si falta información importante, haz preguntas.
4. Propón una respuesta clara, útil y accionable.
5. Entrega la respuesta en el formato solicitado.

Formato de respuesta:
[Ejemplo: mensaje de WhatsApp corto, email, tabla, guion, lista de acciones, etc.]

Reglas:
- No inventes información.
- Si no sabes algo, dilo y pregunta.
- Mantén las respuestas simples y prácticas.
- Adapta el lenguaje a Latinoamérica.
- Prioriza claridad sobre sofisticación.

Primera tarea:
[Escribe aquí el primer caso real que quieres probar]
```

---

## Pasos del ejercicio

### Paso 1: Elegir el asistente — 5 min

Cada participante decide:

> “Voy a construir un asistente para ________.”

Ejemplos:

- “Responder leads de Instagram.”
- “Preparar preguntas para entrevistas con clientes.”
- “Crear posts de LinkedIn a partir de aprendizajes.”
- “Responder preguntas frecuentes de usuarios.”
- “Practicar preguntas de inversionistas.”

---

### Paso 2: Completar contexto — 10 min

Cada participante llena los datos de su startup.

El facilitador recomienda:

> “No seas genérico. Mientras más contexto real le des, mejor funciona.”

Mal ejemplo:

```text
Vendemos software para empresas.
```

Buen ejemplo:

```text
Vendemos un software simple para que restaurantes pequeños en Colombia controlen pedidos, inventario básico y ventas diarias sin depender de Excel.
```

---

### Paso 3: Crear el prompt maestro — 10 min

Copian la plantilla en su herramienta de IA y la completan.

Luego le piden a la IA:

```text
Antes de empezar, hazme 5 preguntas para mejorar este asistente.
```

Esto ayuda a enriquecer el contexto.

---

### Paso 4: Probar con un caso real — 10 min

Cada participante prueba el asistente con una situación concreta.

Ejemplos:

```text
Un lead me escribió: "¿Cuánto cuesta y por qué debería usar esto si ya manejo todo por WhatsApp?"
Redacta una respuesta breve para WhatsApp con tono cercano y un CTA para agendar demo.
```

O:

```text
Voy a entrevistar a una dueña de restaurante que usa Excel para controlar inventario.
Dame 10 preguntas de customer discovery, evitando venderle mi solución.
```

O:

```text
Con base en esta idea, dame 5 posts para LinkedIn orientados a founders B2B early-stage.
```

---

### Paso 5: Mejorar la respuesta — 5 min

Los participantes iteran usando comandos como:

```text
Hazlo más corto.
```

```text
Hazlo más directo y menos corporativo.
```

```text
Agrega una pregunta final para avanzar la conversación.
```

```text
Dame 3 versiones: conservadora, atrevida y muy breve.
```

```text
No inventes funcionalidades que no mencioné.
```

### Resultado final del ejercicio

Cada persona debe terminar con:

1. Un prompt maestro de su asistente.
2. Una primera respuesta útil generada por el asistente.
3. Una lista de mejoras para seguir iterando.
4. Un caso de uso claro para probar durante la semana.

### Key takeaway

No necesitas programar para tener un primer asistente útil. Necesitas claridad sobre el problema, contexto real y buenos ciclos de prueba.

---

# 5. Bloque 8: Testeo, mejora y “red teaming”

**Duración:** 25 minutos  
**Slide count estimado:** 4 slides

### Objetivo

Mejorar los asistentes a través de pruebas reales y feedback de otros participantes.

### Dinámica

Trabajo en parejas.

Cada persona intercambia laptop o explica su asistente a otra persona.

La pareja debe probar el asistente con 3 escenarios:

### Test 1: Caso normal

Ejemplo:

> “Un cliente interesado pregunta por beneficios.”

### Test 2: Caso difícil

Ejemplo:

> “Un cliente dice que es muy caro.”

### Test 3: Caso riesgoso

Ejemplo:

> “El usuario pide algo que la startup no ofrece o información que no existe.”

---

## Checklist de evaluación

Cada participante revisa:

| Criterio | Sí / No | Comentario |
|---|---|---|
| ¿El asistente entiende bien el contexto? |  |  |
| ¿La respuesta es útil? |  |  |
| ¿El tono se siente como mi marca? |  |  |
| ¿Evita inventar información? |  |  |
| ¿Hace preguntas cuando falta contexto? |  |  |
| ¿El resultado se puede usar casi tal cual? |  |  |
| ¿Tiene un siguiente paso claro? |  |  |

---

## Prompts para mejorar

```text
Evalúa tu propia respuesta. Dime qué puede mejorar en claridad, precisión y utilidad.
```

```text
Reescribe la respuesta para que sea más accionable y menos genérica.
```

```text
¿Qué información falta para dar una mejor respuesta?
```

```text
Detecta posibles riesgos, promesas exageradas o información inventada.
```

```text
Convierte esta respuesta en un mensaje de WhatsApp de máximo 500 caracteres.
```

### Key takeaway

Un asistente bueno no es el que responde bonito. Es el que responde útil, con contexto, sin inventar y orientado a una acción.

---

# 6. Bloque 9: Mini demos + aprendizajes del grupo

**Duración:** 15 minutos  
**Slide count estimado:** 2 slides

### Objetivo

Compartir ejemplos, inspirar al grupo y reforzar aprendizajes prácticos.

### Dinámica

3 a 5 voluntarios muestran en 2 minutos:

1. Qué asistente construyeron.
2. Para qué tarea sirve.
3. Qué respuesta generó.
4. Qué mejorarían en la siguiente versión.

El facilitador comenta rápidamente:

- Qué estuvo bien.
- Qué se puede ajustar.
- Cómo llevarlo al día a día.

### Key takeaway

Ver asistentes de otros abre ideas. Muchas veces el mejor caso de uso no es el más sofisticado, sino el más repetitivo.

---

# 7. Bloque 10: Cierre y próximos pasos

**Duración:** 5 minutos  
**Slide count estimado:** 2 slides

### Objetivo

Cerrar con acción concreta para que no se quede solo en el workshop.

### Dinámica

Cada participante escribe su compromiso:

> “Durante los próximos 7 días voy a usar mi asistente para ________.”

Ejemplos:

- Responder 10 leads.
- Preparar 5 entrevistas.
- Crear 7 posts.
- Mejorar mi pitch.
- Documentar mis FAQs.

### Recomendación final

Usar esta regla:

> Si una tarea se repite 3 veces, conviértela en proceso.  
> Si es un proceso basado en información, prueba convertirlo en asistente.

### Key takeaway

El asistente no se termina hoy. Hoy nace la versión 1.0. La mejora real viene al usarlo con casos reales durante la semana.

---

# 8. Slide count estimado por sección

| Sección | Slides estimadas |
|---|---:|
| Bienvenida, contexto y setup | 3 |
| Qué puede hacer un asistente de IA por tu startup | 5 |
| Elige el caso de uso correcto | 4 |
| Anatomía de un buen asistente de IA | 6 |
| Break | 1 |
| Demo en vivo | 5 |
| Ejercicio principal | 5 |
| Testeo y mejora | 4 |
| Mini demos | 2 |
| Cierre | 2 |
| **Total estimado** | **37 slides** |

Recomendación: mantener las slides visuales y simples. La energía del workshop debe estar en los ejercicios, no en la presentación.

---

# 9. Recursos para llevar a casa

## Plantillas

1. Plantilla de Prompt Maestro.
2. Plantilla para diseñar asistentes.
3. Checklist de testeo.
4. Matriz para elegir casos de uso.
5. Banco de prompts de mejora.
6. Plantilla de documentación de procesos.

---

## Prompts útiles para seguir mejorando

### Para definir mejor el asistente

```text
Hazme 10 preguntas para entender mejor mi startup y mejorar este asistente.
```

### Para evitar respuestas genéricas

```text
Haz la respuesta más específica usando solo la información que te di. Si falta algo, pregúntame.
```

### Para mejorar tono

```text
Reescribe esto con un tono más cercano, directo y latinoamericano. Evita sonar corporativo.
```

### Para ventas

```text
Dame 3 versiones de respuesta para este lead: una breve, una consultiva y una más persuasiva.
```

### Para soporte

```text
Convierte esta explicación en una respuesta simple para un usuario que no es técnico.
```

### Para customer discovery

```text
Dame preguntas para entender el problema sin mencionar mi solución.
```

### Para pitch

```text
Actúa como inversionista escéptico. Hazme 10 preguntas difíciles sobre mi startup.
```

### Para análisis

```text
Resume estos comentarios de clientes en patrones de dolor, objeciones y oportunidades.
```

---

## Herramientas recomendadas

### IA conversacional

- ChatGPT.
- Claude.
- Gemini.
- Microsoft Copilot.

### Investigación

- Perplexity.
- Google.
- You.com.

### Organización

- Notion.
- Google Docs.
- Airtable.
- Trello.

### Automatización, para una siguiente etapa

- Zapier.
- Make.
- n8n.
- Google Forms + Sheets.
- Typeform.

### Creación de asistentes más estructurados

- Custom GPTs de ChatGPT.
- Claude Projects.
- Gemini Gems.
- Poe Bots.
- Botpress, para quienes quieran explorar más adelante.

---

# 10. Recomendaciones para el facilitador

## Mantener el ritmo

Este público no necesita una clase técnica. Necesita claridad, ejemplos y acción.

Frases útiles:

- “No busquemos perfección, busquemos una versión útil.”
- “Si tu asistente suena genérico, le falta contexto.”
- “Si inventa, ponle límites.”
- “Si responde largo, pídele formato.”
- “Si no sirve, no cambies de herramienta todavía: mejora la instrucción.”

## Evitar errores comunes

1. Dedicar demasiado tiempo a teoría.
2. Hablar de modelos, tokens, APIs o arquitectura.
3. Permitir casos de uso demasiado amplios.
4. No dejar tiempo para probar.
5. No conectar el asistente con una tarea real de negocio.

## Indicador de éxito del workshop

Al final, cada participante debería poder decir:

> “Ya tengo un asistente que me ayuda con una tarea concreta de mi startup y sé cómo mejorarlo.”