# Claude Haiku 5.5 — startup_content/workshop_outline

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.73 | quality: 9.8
- latency_total: 21.466s | tokens_per_second: 208.8
- input_tokens: 315 | output_tokens: 4482
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que aborda todos los aspectos solicitados, ofreciendo insights útiles para emprendedores no técnicos.

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

# Workshop: "Construye tu Asistente de IA para tu Startup"
### Workshop Práctico · 3 horas · 20–30 personas · Nivel: no técnico

---

## 1. Agenda detallada (180 min)

| Hora | Min | Bloque | Formato |
|---|---|---|---|
| 0:00 | 15 | Bienvenida y "por qué ahora" | Charla energética + pregunta de apertura |
| 0:15 | 25 | Anatomía de un asistente de IA | Charla + demo en vivo |
| 0:40 | 10 | Pausa activa | Ronda de networking rápido |
| 0:50 | 25 | Diseña tu asistente (framework) | Ejercicio guiado en grupos |
| 1:15 | 30 | Construcción práctica, paso 1 y 2 | Hands-on con herramientas no-code |
| 1:45 | 15 | Pausa + café | Networking |
| 2:00 | 35 | Construcción práctica, paso 3 y 4 + pruebas | Hands-on en parejas |
| 2:35 | 15 | Demo lightning de los participantes | Presentaciones de 90 segundos |
| 2:50 | 10 | Cierre, plan de 7 días y recursos | Charla + compromiso personal |

**Total: 180 min**

---

## 2. Materiales

### Antes del workshop (2 semanas antes)
- [ ] Cuenta de prueba preparada en 2 herramientas no-code (ej. Custom GPTs de ChatGPT, Claude Projects o Gemini Gems; elegir 1 principal y 1 alternativa)
- [ ] Plantilla de "Ficha de Asistente" en Google Docs o Notion (ver Anexo A)
- [ ] Base de conocimiento de ejemplo: un PDF de 5–10 páginas de un caso ficticio (ej. "Cafetería SaaS" o "Tienda de ropa sostenible")
- [ ] Formulario de inscripción que pida: nombre de startup, sector, principal dolor de cliente
- [ ] Verificar conectividad del venue y tener plan B offline (capturas de pantalla y video grabado del demo)
- [ ] Confirmar que cada participante tenga laptop y cuenta gratuita creada antes de llegar (enviar guía de 1 página 3 días antes)

### El día del evento
- Laptops o tablets para quienes no tengan (2–3 disponibles)
- Cargadores y extensiones eléctricas
- Proyector/pantalla, micrófono inalámbrico
- Post-its de colores (3 colores), marcadores gruesos, cinta adhesiva
- Mesas en grupos de 4–5
- Tarjetas de "pregunta del pozo" (para las preguntas anónimas)
- Stickers o insignias con nombre
- Impresiones: Ficha de Asistente (1 por persona), Cheat sheet de prompts (1 por persona), QR a recursos
- Wifi con contraseña escrita en pizarra

---

## 3. Desglose por bloque

### Bloque 1 · Bienvenida y "por qué ahora" (15 min)
- **Dinámica:** Charla energética con pregunta de apertura. Pedir levantar la mano: "¿Quién ya usó ChatGPT para algo de su negocio esta semana?" Luego: "¿Quién lo usó para algo que le ahorró más de 1 hora?"
- **Objetivo:** Romper el hielo y conectar el tema con la realidad de cada uno.
- **Contenido clave:** Por qué un asistente de IA es hoy accesible sin programar; ejemplos de startups latinoamericanas que lo usan para atención al cliente, ventas o contenido.
- **Key takeaway:** *"Ya no necesitas un equipo técnico para tener un asistente de IA; necesitas claridad sobre tu cliente."*

### Bloque 2 · Anatomía de un asistente de IA (25 min)
- **Dinámica:** Charla de 10 min + demo en vivo de 15 min. En la demo, mostrar un asistente sin instrucciones vs. uno con instrucciones claras, lado a lado.
- **Objetivo:** Que entiendan las 4 piezas de un asistente: **rol, contexto, conocimiento y tono**.
- **Contenido clave:**
  - Rol: quién es el asistente ("Eres la asistente de servicio al cliente de…")
  - Contexto: qué sabe de tu negocio
  - Conocimiento: documentos que consulta (precios, políticas, FAQ)
  - Tono y límites: qué puede y no puede responder
- **Key takeaway:** *"Un buen asistente es 80% instrucciones claras y 20% tecnología."*

### Bloque 3 · Pausa activa (10 min)
- **Dinámica:** Ronda de networking rápido: cada persona se presenta en 20 segundos con su startup y "qué pregunta le daría a su asistente".
- **Objetivo:** Activar energía y generar conexiones entre participantes.
- **Key takeaway:** Las mejores ideas surgen al escuchar casos de otros.

### Bloque 4 · Diseña tu asistente con el framework (25 min)
- **Dinámica:** Ejercicio guiado en grupos de 4–5. Cada persona llena su Ficha de Asistente mientras el grupo le hace preguntas de "fuego cruzado" para afinar la idea.
- **Objetivo:** Definir el caso de uso concreto del asistente.
- **Preguntas guía de la Ficha:**
  1. ¿Qué pregunta repetida recibes cada semana de tus clientes?
  2. ¿Quién es tu cliente y qué idioma/tono usa?
  3. ¿Qué información necesita tener el asistente? (precios, horarios, políticas)
  4. ¿Qué NO debe hacer nunca? (prometer descuentos, dar asesoría legal, etc.)
  5. ¿Cómo sabrás que funciona? (métrica simple: tiempo de respuesta, % resuelto)
- **Key takeaway:** *"Un asistente que resuelve UNA cosa bien vale más que uno que hace diez a medias."*

### Bloque 5 · Construcción práctica, pasos 1 y 2 (30 min)
- **Dinámica:** Hands-on guiado. El facilitador va paso a paso en pantalla, los participantes replican. Paso 1: crear el asistente y escribir sus instrucciones (rol + tono). Paso 2: subir la base de conocimiento (el PDF de ejemplo o el propio).
- **Objetivo:** Tener un asistente funcional con instrucciones básicas.
- **Apoyo:** Facilitador circula; los asistentes técnicos (si hay) ayudan en mesas.
- **Key takeaway:** *"Crear el asistente toma minutos; lo que toma tiempo es escribir bien lo que debe saber."*

### Bloque 6 · Pausa y café (15 min)
- Networking libre. Sugerencia: dejar el asistente de demo corriendo para que la gente pruebe preguntas.

### Bloque 7 · Construcción práctica, pasos 3 y 4 + pruebas (35 min)
- **Dinámica:** Trabajo en parejas. Paso 3: añadir reglas de límites y escalamiento ("si no sabes, dilo y ofrece contactar a un humano"). Paso 4: pruebas. Cada pareja hace 10 preguntas reales de clientes y registra qué tan bien responde el asistente.
- **Objetivo:** Un asistente con límites claros y probado.
- **Ejercicio de prueba:** Tabla simple con 3 columnas: pregunta / respuesta / ¿correcta? (sí / parcial / no). Luego ajustan instrucciones y repiten 3 preguntas.
- **Key takeaway:** *"Probar con preguntas reales es el paso que separa un juguete de una herramienta de negocio."*

### Bloque 8 · Demo lightning (15 min)
- **Dinámica:** Cada participante (o pareja, si son muchos) muestra su asistente en 90 segundos: qué hace, una pregunta en vivo y qué aprendió. Cronómetro visible.
- **Objetivo:** Visibilizar avances y celebrar el progreso.
- **Key takeaway:** *"Ver cómo otros resolvieron el mismo problema de forma distinta multiplica tus ideas."*

### Bloque 9 · Cierre, plan de 7 días y recursos (10 min)
- **Dinámica:** Charla breve + compromiso personal. Cada persona escribe en un post-it: "Esta semana voy a…" y lo pega en la pared de salida.
- **Objetivo:** Asegurar que el aprendizaje continúe fuera del evento.
- **Key takeaway:** *"El asistente que construiste hoy es un borrador. Mejóralo con datos reales de esta semana."*

---

## 4. Ejercicio principal del workshop: "Asistente en 4 pasos"

Todos completan este ejercicio. Es el corazón del workshop.

**Paso 1 · Rol (5 min):** Escribe una frase: *"Eres [nombre] , el asistente de [tu startup] que ayuda a [tipo de cliente] a [resultado que busca]."*

**Paso 2 · Conocimiento (10 min):** Sube o pega 5–10 datos clave de tu negocio: precios, horarios, políticas de devolución, preguntas frecuentes. Formato: lista simple.

**Paso 3 · Límites (8 min):** Escribe 3 cosas que el asistente NUNCA debe hacer y 1 regla de escalamiento: *"Si el cliente pide X o está molesto, responde: 'Te conecto con nuestro equipo' y deriva."*

**Paso 4 · Pruebas (12 min):** Haz 10 preguntas reales que te han hecho clientes. Califica cada respuesta (correcta / parcial / incorrecta). Ajusta una instrucción y vuelve a probar 3 preguntas.

**Entregable:** Un asistente funcional + tabla de 10 pruebas calificadas.

---

## 5. Recursos para llevar a casa

- **Guía de 1 página:** "Plantilla de instrucciones para tu asistente" (con los 4 componentes)
- **Cheat sheet de 20 prompts** para mejorar instrucciones según el sector (retail, servicios, B2B, educación)
- **Checklist de privacidad:** qué datos NO subir a herramientas de IA (datos personales de clientes, contraseñas, información financiera sensible)
- **Plan de 7 días:** un reto diario simple (día 1: probar con 3 clientes reales; día 3: ajustar; día 7: medir tiempo ahorrado)
- **Comparativa de herramientas no-code** actualizada (costos, idiomas, integraciones con WhatsApp/web)
- **Comunidad:** grupo de WhatsApp o Discord del workshop para compartir avances durante 30 días
- **QR** a video grabado del demo y a la plantilla editable

---

## 6. Slide count estimado

| Sección | Slides |
|---|---|
| Bienvenida y "por qué ahora" | 4 |
| Anatomía de un asistente | 7 |
| Pausa activa | 1 |
| Framework de diseño | 4 |
| Construcción pasos 1–2 | 5 |
| Pausa | 1 |
| Construcción pasos 3–4 y pruebas | 5 |
| Demo lightning | 2 |
| Cierre y plan de 7 días | 3 |
| Portada, agenda y créditos | 3 |
| **Total estimado** | **~35 slides** |

*Nota: Los bloques prácticos (construcción) deben tener slides mínimos, con el foco en la pantalla del facilitador y capturas de pasos. Menos slides, más demo.*

---

### Anexo A · Ficha de Asistente (plantilla)

```
NOMBRE DEL ASISTENTE:
STARTUP Y SECTOR:
CLIENTE TIPO (quién es, qué idioma/tono usa):
PREGUNTA #1 QUE RECIBO SIEMPRE:
INFORMACIÓN QUE DEBE SABER (lista):
LO QUE NUNCA DEBE HACER (3 cosas):
CUÁNDO DEBE DERIVAR A UN HUMANO:
MÉTRICA DE ÉXITO (ej. % resuelto sin humano):
```

---

¿Quieres que desarrolle alguna de estas partes en más detalle, por ejemplo los prompts específicos del cheat sheet, el guion del demo en vivo o la guía de preparación para los participantes?