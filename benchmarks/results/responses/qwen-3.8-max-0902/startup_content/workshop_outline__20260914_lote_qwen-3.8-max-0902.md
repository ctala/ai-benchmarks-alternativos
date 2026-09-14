# Qwen 3.8 Max 0902 — startup_content/workshop_outline

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.88 | quality: 10.0
- latency_total: 294.448s | tokens_per_second: 42.5
- input_tokens: 240 | output_tokens: 12526
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores no técnicos, proporcionando un plan detallado y práctico para el taller.

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

# 🚀 Outline completo: “Construye tu Asistente de IA para tu Startup - Workshop Práctico”

**Duración total:** 3 horas / 180 minutos  
**Audiencia:** 20-30 emprendedores early-stage, no técnicos  
**Promesa del workshop:** Cada participante sale con un asistente de IA básico, probado y listo para seguir mejorando, usando herramientas no-code.  
**Enfoque:** 100% práctico, rápido, aplicable a startups latinoamericanas, con recursos limitados y foco en casos de uso reales: atención al cliente, ventas, soporte, calificación de leads o onboarding.

---

## 1. Agenda detallada de 3 horas

| Tiempo | Bloque | Duración | Formato principal | Output del participante |
|---|---|---:|---|---|
| 0:00 - 0:10 | Bienvenida + pacto de acción | 10 min | Charla dinámica | Mentalidad de “hoy construyo” |
| 0:10 - 0:25 | IA útil para startups: menos hype, más resultados | 15 min | Charla + ejemplos | 2-3 casos de uso identificados |
| 0:25 - 0:40 | Demo exprés: de 0 a asistente en minutos | 15 min | Demo en vivo | Referencia clara de qué construir |
| 0:40 - 1:10 | Diseña tu asistente: Canvas rápido | 30 min | Ejercicio individual o en parejas | Caso de uso y prompt base definidos |
| 1:10 - 1:20 | Break activo / networking | 10 min | Descanso corto | Energía renovada |
| 1:20 - 2:15 | Manos a la obra: construye tu asistente | 55 min | Taller guiado + soporte | Asistente creado y configurado |
| 2:15 - 2:40 | Prueba, mejora y límites responsables | 25 min | Pruebas en parejas + ajustes | Asistente mejorado y más seguro |
| 2:40 - 3:00 | Demos voluntarias + cierre con próximos pasos | 20 min | Presentaciones cortas | Plan de acción de 7 días |

**Total: 180 minutos**

---

## 2. Materiales necesarios: qué preparar antes

### A. Preparación del facilitador / equipo

#### Espacio físico
- [ ] Sala con mesas móviles o formato “islas” de 4-5 personas.
- [ ] Sillas suficientes para 20-30 participantes + equipo facilitador.
- [ ] Proyector o pantalla grande.
- [ ] Adaptador HDMI / USB-C.
- [ ] Audio básico si el espacio es grande.
- [ ] Micrófono si hay más de 25 personas.
- [ ] Buena iluminación.
- [ ] Pizarra o papelógrafo para anotar ideas.
- [ ] Enchufes y zapatillas eléctricas distribuidas por mesas.

#### Conectividad
- [ ] Wi-Fi estable, idealmente probado con 20-30 dispositivos conectados.
- [ ] Contraseña visible en pantalla o impresa.
- [ ] Plan B: hotspot móvil o datos compartidos.
- [ ] Descargar o tener offline:
  - Slides en PDF.
  - Plantillas del ejercicio.
  - Ejemplos de prompts.
  - Demo grabada por si falla internet.

#### Cuentas y herramientas
- [ ] Cuenta del facilitador lista para demo.
- [ ] Herramienta principal probada:
  - ChatGPT Custom GPT / GPTs.
  - Gemini Gems.
  - Poe.
  - Chatbase.
  - Dante AI.
  - Landbot, si se quiere llevar luego a WhatsApp.
- [ ] Cuentas de respaldo para mostrar, sin datos reales de participantes.
- [ ] Enlace corto o QR para recursos del workshop.
- [ ] Carpeta compartida con plantillas:
  - Canvas del asistente.
  - Prompt maestro.
  - Checklist de pruebas.
  - Recursos para llevar a casa.

#### Equipo facilitador
Para 20-30 personas:
- [ ] 1 facilitador principal.
- [ ] 2-3 co-facilitadores o “helpers” flotantes.
- [ ] Ideal: 1 helper por cada 8-10 participantes.
- [ ] Roles definidos:
  - Facilitador principal: ritmo, explicaciones, demos.
  - Helpers: resolver dudas técnicas, cuentas, prompts.
  - Productor/logística: tiempo, materiales, QR, incidencias.

---

### B. Materiales físicos para el día del workshop

- [ ] Impresión del “Canvas del Asistente” para cada participante o pareja.
- [ ] Hojas de “Prompt Maestro” impresas.
- [ ] Checklist de pruebas impreso o en PDF.
- [ ] Post-its de colores.
- [ ] Marcadores.
- [ ] Tarjetas o stickers para identificar “caso de uso elegido”.
- [ ] Señalética del QR de recursos.
- [ ] Lista de asistencia.
- [ ] Encuesta rápida de entrada/salida, si se quiere medir impacto.

---

### C. Preparación de los participantes

Enviar antes del workshop un mensaje corto tipo:

> “Para aprovechar el workshop, trae tu laptop, cargador y una idea de negocio o startup. Si aún no tienes una, no te preocupes: podrás usar un caso de ejemplo. Crea una cuenta gratuita en al menos una herramienta de IA: ChatGPT, Gemini, Claude o Poe. Trae 5 preguntas frecuentes que tus clientes suelen hacerte, si ya tienes clientes o usuarios.”

#### Pre-work recomendado para participantes
- [ ] Traer laptop o trabajar en pareja.
- [ ] Cargador.
- [ ] Cuenta gratuita creada en al menos una herramienta de IA.
- [ ] Descripción breve de su startup:
  - Qué hace.
  - A quién sirve.
  - Qué problema resuelve.
- [ ] 3-5 preguntas frecuentes de clientes o usuarios.
- [ ] Información básica del producto/servicio:
  - Precio.
  - Horario de atención.
  - Canales de contacto.
  - Políticas de devolución, garantía o soporte, si aplica.
- [ ] No traer datos sensibles, contraseñas, información médica, financiera o confidencial.

---

## 3. Detalle por bloque

---

### Bloque 1: Bienvenida + pacto de acción  
**Duración:** 10 minutos  
**Objetivo:** Activar energía, bajar la ansiedad tecnológica y dejar claro que el workshop es práctico.

**Dinámica:**  
- Charla rápida del facilitador.
- Pregunta al público:  
  “¿Quién ya usa IA en su startup?”  
  “¿Quién siente que la IA es mucho ruido y poca claridad?”
- Reglas del juego:
  - Hoy se construye.
  - No se necesita saber programar.
  - Hecho es mejor que perfecto.
  - No usar datos sensibles.
  - Si te trabas, levanta la mano y pedimos ayuda.

**Key takeaway:**  
> “No vine a escuchar sobre IA: vine a construir mi primer asistente.”

**Slides sugeridas:** 2

---

### Bloque 2: IA útil para startups: menos hype, más resultados  
**Duración:** 15 minutos  
**Objetivo:** Mostrar casos de uso concretos y ayudar a los participantes a elegir un problema real.

**Dinámica:**  
- Mini charla con ejemplos latinoamericanos y cercanos.
- Casos de uso:
  - Responder preguntas frecuentes de clientes.
  - Calificar leads antes de una reunión.
  - Ayudar con onboarding de usuarios.
  - Redactar respuestas para soporte.
  - Asistente interno para el equipo.
  - Primer filtro para WhatsApp o formulario web.
- Pregunta rápida en mesas:
  “¿Qué tarea repetitiva te roba más tiempo hoy?”

**Key takeaway:**  
> “El mejor asistente de IA no es el más inteligente, sino el que resuelve un dolor concreto de tu startup.”

**Slides sugeridas:** 4

---

### Bloque 3: Demo exprés: de 0 a asistente en minutos  
**Duración:** 15 minutos  
**Objetivo:** Mostrar el camino completo para que nadie sienta que es demasiado técnico.

**Dinámica:**  
- Demo en vivo del facilitador.
- Crear un asistente simple para una startup ficticia.
- Ejemplo:
  - Startup ficticia: “CaféAndo”, una tienda online de café de especialidad.
  - Asistente: responde dudas sobre envíos, precios, métodos de pago y recomendaciones de producto.
- Mostrar:
  1. Nombre del asistente.
  2. Descripción.
  3. Instrucciones / prompt.
  4. Base de conocimiento simple.
  5. Prueba con 2 preguntas.
  6. Ajuste rápido.

**Key takeaway:**  
> “Si puedo describirlo, puedo convertirlo en instrucciones para un asistente.”

**Slides sugeridas:** 2  
**Nota:** La demo debe ser simple, visible y sin pasos técnicos complejos.

---

### Bloque 4: Diseña tu asistente: Canvas rápido  
**Duración:** 30 minutos  
**Objetivo:** Que cada participante defina qué asistente va a construir antes de abrir la herramienta.

**Dinámica:**  
- Ejercicio individual o en parejas.
- Completar el “Canvas del Asistente”:
  1. ¿Qué problema resuelve?
  2. ¿Quién lo usa?
  3. ¿Qué tarea principal hace?
  4. ¿Qué información necesita?
  5. ¿Qué tono debe tener?
  6. ¿Qué no debe hacer?
  7. ¿Cuándo debe derivar a una persona?
  8. ¿Cómo se ve una buena respuesta?

**Ejemplo rápido:**

| Campo | Ejemplo |
|---|---|
| Problema | Los clientes preguntan siempre por precios y envíos |
| Usuario | Clientes de tienda online |
| Tarea | Responder dudas de compra |
| Información | Catálogo, precios, envíos, pagos |
| Tono | Cercano, claro, rápido |
| Límites | No prometer fechas exactas si no están confirmadas |
| Escalamiento | Si hay reclamo, pasar a humano |
| Éxito | Cliente recibe respuesta útil en menos de 30 segundos |

**Key takeaway:**  
> “Un buen asistente nace de un buen problema, no de una herramienta.”

**Slides sugeridas:** 5

---

### Bloque 5: Break activo / networking  
**Duración:** 10 minutos  
**Objetivo:** Bajar la carga mental, resolver pequeños bloqueos y generar energía.

**Dinámica:**  
- Descanso corto.
- Opción de “pregunta rápida” en parejas:
  “¿Qué asistente estás construyendo y para quién?”
- El facilitador puede aprovechar para:
  - Revisar que todos tengan cuentas listas.
  - Detectar participantes que necesiten ayuda.
  - Asignar helpers a mesas más trabadas.

**Key takeaway:**  
> “Recargo energía y vuelvo a construir.”

**Slides sugeridas:** 1

---

### Bloque 6: Manos a la obra: construye tu asistente  
**Duración:** 55 minutos  
**Objetivo:** Que cada participante cree un asistente funcional usando una herramienta no-code.

**Dinámica:**  
- Taller guiado paso a paso.
- Helpers flotando por la sala.
- Cada participante o pareja construye su asistente.

**Ruta recomendada:**

#### Minutos 0-10: Elegir herramienta
Opciones:
- ChatGPT Custom GPT / GPTs.
- Gemini Gems.
- Poe.
- Chatbase.
- Dante AI.
- Si ninguna funciona, usar “Prompt Maestro” en cualquier chat de IA.

#### Minutos 10-25: Configurar identidad
Crear:
- Nombre del asistente.
- Descripción.
- Audiencia.
- Tono.
- Objetivo principal.

#### Minutos 25-40: Cargar conocimiento mínimo
Pegar o subir:
- 5 preguntas frecuentes.
- Información del producto/servicio.
- Precios, horarios, canales, políticas básicas.
- Enlaces útiles, si aplica.

#### Minutos 40-55: Primera prueba
Probar con:
- Una pregunta normal.
- Una pregunta confusa.
- Una pregunta fuera de alcance.

**Key takeaway:**  
> “Mi asistente no necesita ser perfecto; necesita existir y poder mejorar.”

**Slides sugeridas:** 4

---

### Bloque 7: Prueba, mejora y límites responsables  
**Duración:** 25 minutos  
**Objetivo:** Mejorar el asistente con pruebas reales y definir reglas de seguridad.

**Dinámica:**  
- Pruebas en parejas: un participante prueba el asistente del otro.
- Se usa el “Checklist de pruebas”.
- Mini charla sobre límites:
  - No inventar información.
  - No dar consejos médicos, legales o financieros delicados.
  - Derivar a humano cuando corresponda.
  - Cuidar datos personales.
  - Ser transparente: decir que es un asistente de IA.

**Pruebas recomendadas:**

| Tipo de prueba | Ejemplo |
|---|---|
| Pregunta típica | “¿Cuánto cuesta el plan básico?” |
| Pregunta ambigua | “No sé cuál elegir” |
| Cliente molesto | “Estoy harto, no me llega el pedido” |
| Fuera de alcance | “¿Puedes hacerme una devolución ahora mismo?” |
| Escalamiento | “Quiero hablar con una persona” |

**Ajustes comunes:**
- Respuestas más cortas.
- Tono más cercano.
- No inventar datos.
- Pedir aclaración si la pregunta es confusa.
- Ofrecer siempre un siguiente paso.
- Derivar a humano si hay reclamos o temas sensibles.

**Key takeaway:**  
> “La IA acelera, pero la responsabilidad y la confianza son de la startup.”

**Slides sugeridas:** 4

---

### Bloque 8: Demos voluntarias + cierre con próximos pasos  
**Duración:** 20 minutos  
**Objetivo:** Mostrar avances, celebrar aprendizajes y dejar un plan de acción.

**Dinámica:**  
- 3-5 demos voluntarias de 2 minutos cada una.
- Formato de demo:
  1. Qué problema resuelve.
  2. Para quién es.
  3. Demo rápida de una pregunta.
  4. Qué mejorarían esta semana.
- Feedback rápido del facilitador.
- Cierre con compromiso personal:
  - “En los próximos 7 días voy a…”

**Ejemplos de compromisos:**
- Probar el asistente con 5 clientes reales.
- Agregar 10 preguntas frecuentes.
- Conectarlo a un formulario.
- Usarlo como borrador de respuestas de soporte.
- Medir cuántas consultas resuelve sin ayuda humana.

**Key takeaway:**  
> “Me voy con un asistente funcionando y con un plan claro para mejorarlo.”

**Slides sugeridas:** 3

---

## 4. Ejercicio principal del workshop

### Nombre del ejercicio  
**“Mi asistente de atención y ventas en 55 minutos”**

### Objetivo  
Que cada emprendedor construya un asistente de IA básico que pueda:
- Responder preguntas frecuentes.
- Explicar un producto o servicio.
- Recomendar un siguiente paso.
- Derivar a una persona cuando sea necesario.

### Modalidad  
- Individual si cada participante tiene laptop.
- En parejas si hay menos equipos o niveles distintos.
- Si alguien no tiene startup, puede usar un caso ficticio entregado por el facilitador.

---

### Caso de uso recomendado

Elegir **uno solo** de estos casos:

1. **Asistente de preguntas frecuentes**
   - Responde dudas sobre producto, precio, horarios, envíos, garantías.

2. **Asistente de ventas**
   - Ayuda a elegir un plan, producto o servicio.

3. **Asistente de calificación de leads**
   - Hace preguntas básicas antes de agendar una reunión.

4. **Asistente de onboarding**
   - Explica primeros pasos para usar el producto.

5. **Asistente interno**
   - Ayuda al equipo con respuestas comerciales o procesos simples.

**Regla de oro:**  
> Mejor un asistente pequeño y útil que uno gigante y confuso.

---

### Paso a paso del ejercicio

#### Paso 1: Elige el problema  
**Tiempo:** 5 minutos  
Completa:

> “Mi asistente ayudará a [tipo de usuario] a [resolver tarea] para [beneficio principal].”

Ejemplo:

> “Mi asistente ayudará a clientes de mi tienda online a resolver dudas sobre precios, envíos y pagos para aumentar la confianza y reducir consultas repetitivas.”

---

#### Paso 2: Define la identidad del asistente  
**Tiempo:** 5 minutos  

Completa:

- Nombre del asistente:
- Startup:
- Audiencia:
- Tono:
- Objetivo:
- Límites:
- Cuándo derivar a humano:

Ejemplo:

- Nombre: “Lúa”
- Startup: Tienda de ropa sostenible
- Audiencia: Clientes que compran online
- Tono: Cercano, claro, amable
- Objetivo: Resolver dudas de compra
- Límites: No inventar stock ni fechas de entrega
- Derivar a humano: reclamos, devoluciones complejas o clientes molestos

---

#### Paso 3: Prepara tu base de conocimiento mínima  
**Tiempo:** 10 minutos  

Reúne o escribe rápidamente:

1. ¿Qué vendes?
2. ¿Cuánto cuesta?
3. ¿Cómo se compra?
4. ¿Cómo se paga?
5. ¿Cómo se entrega o se usa?
6. ¿Qué pasa si hay un problema?
7. ¿Cuál es el canal humano de contacto?
8. 5 preguntas frecuentes reales.

Si no tienes clientes aún, escribe preguntas que crees que te harían.

---

#### Paso 4: Crea el asistente  
**Tiempo:** 20 minutos  

Usa una herramienta no-code.  
Si usas ChatGPT, Gemini, Poe o similar, completa:

- Nombre.
- Descripción.
- Instrucciones.
- Conocimiento o contexto.
- Tono.
- Restricciones.

---

#### Paso 5: Usa el Prompt Maestro

Copia, pega y adapta:

```text
Eres [nombre del asistente], el asistente virtual de [nombre de la startup].

Tu objetivo principal es [objetivo del asistente].

Tu audiencia principal es [tipo de usuario o cliente].

Debes responder en español claro, simple y útil.

Tono: [cercano / profesional / amable / directo / breve].

Reglas obligatorias:
1. Responde solo con base en la información proporcionada.
2. Si no sabes algo, di: “No tengo esa información ahora, pero puedo ayudarte a contactar a una persona del equipo”.
3. No inventes precios, stock, fechas, políticas ni promesas.
4. No des consejos médicos, legales, financieros o delicados.
5. Si el usuario está molesto o pide ayuda humana, ofrece derivar a una persona.
6. Mantén respuestas cortas, claras y accionables.
7. Si la pregunta es confusa, haz una pregunta de aclaración.
8. Siempre que sea posible, termina con un siguiente paso simple.

Información del negocio:
[Pega aquí descripción del producto/servicio]

Preguntas frecuentes:
[Pega aquí tus 5 preguntas y respuestas]

Políticas básicas:
[Precios, horarios, envíos, pagos, contacto humano, etc.]

Formato de respuesta:
- Respuesta breve.
- Usa bullets si ayuda.
- No uses más de 120 palabras salvo que sea necesario.
- Ofrece una acción siguiente.
```

---

#### Paso 6: Prueba tu asistente  
**Tiempo:** 10 minutos  

Haz estas 5 pruebas:

1. **Pregunta feliz:**  
   “¿Cuánto cuesta?”  
   “¿Cómo funciona?”  
   “¿Hacen envíos?”

2. **Pregunta ambigua:**  
   “No sé cuál me sirve.”  
   “Quiero algo barato.”

3. **Pregunta fuera de alcance:**  
   “¿Me puedes hacer un descuento especial?”  
   “¿Puedo pagar en cuotas?” si no tienes esa información.

4. **Cliente molesto:**  
   “Estoy harto, nadie me responde.”  
   “Mi pedido no llegó.”

5. **Escalamiento humano:**  
   “Quiero hablar con una persona.”  
   “Necesito soporte real.”

---

#### Paso 7: Ajusta y mejora  
**Tiempo:** 5 minutos  

Si el asistente:
- Responde muy largo → pide respuestas más cortas.
- Inventa datos → agrega: “No inventes información”.
- Suena frío → ajusta el tono.
- No ofrece acción → agrega: “Siempre propone un siguiente paso”.
- No deriva a humano → agrega regla de escalamiento.

---

### Entregable del ejercicio

Cada participante debe terminar con al menos uno de estos entregables:

- [ ] Asistente creado en una herramienta no-code.
- [ ] Link del asistente, si la herramienta lo permite.
- [ ] Prompt Maestro completo y probado.
- [ ] 3 pruebas realizadas.
- [ ] 1 mejora aplicada.
- [ ] Plan de próximos 7 días.

**Mínimo viable:**  
Si alguien no logra crear el bot completo, debe salir con el Prompt Maestro listo para usar en cualquier herramienta.

---

## 5. Recursos para llevar a casa

Entregar una carpeta digital, idealmente vía QR, con lo siguiente:

### 1. PDF: Canvas del Asistente
Una hoja simple para definir:
- Problema.
- Usuario.
- Tarea.
- Información.
- Tono.
- Límites.
- Escalamiento.
- Métrica de éxito.

---

### 2. Plantilla: Prompt Maestro
Versión editable para copiar y pegar.

---

### 3. Checklist de pruebas
Para probar el asistente antes de usarlo con clientes reales.

Ejemplo:

| Prueba | Pasó | Ajuste necesario |
|---|---|---|
| Responde preguntas frecuentes |  |  |
| No inventa información |  |  |
| Tiene tono adecuado |  |  |
| Sabe derivar a humano |  |  |
| Ofrece siguiente paso |  |  |
| Maneja cliente molesto |  |  |

---

### 4. Banco de prompts para startups
Prompts listos para:
- Atención al cliente.
- Ventas.
- Calificación de leads.
- Onboarding.
- Soporte interno.
- Redacción de respuestas para WhatsApp.
- Resumen de feedback de usuarios.

---

### 5. Guía rápida: herramientas no-code
Tabla comparativa simple:

| Herramienta | Ideal para | Nivel | Costo inicial |
|---|---|---|---|
| ChatGPT GPTs | Asistentes conversacionales | Fácil | Gratis / Plus según acceso |
| Gemini Gems | Asistentes en ecosistema Google | Fácil | Gratis según cuenta |
| Poe | Crear bots rápidos | Fácil | Gratis / opciones pagas |
| Chatbase | Asistente con base de conocimiento | Medio | Freemium |
| Dante AI | Asistentes con documentos | Medio | Freemium |
| Landbot | Flujos + WhatsApp | Medio-alto | Freemium / pago |

**Nota importante para LatAm:**  
Si el objetivo final es WhatsApp, no empezar con integración compleja en el workshop. Primero construir el cerebro del asistente. La integración a WhatsApp puede ser una fase 2.

---

### 6. Plan de 7 días
Una hoja simple:

| Día | Acción |
|---|---|
| Día 1 | Probar asistente con 5 preguntas reales |
| Día 2 | Agregar 5 preguntas frecuentes más |
| Día 3 | Ajustar tono y límites |
| Día 4 | Probar con un compañero o cliente de confianza |
| Día 5 | Medir cuántas respuestas fueron útiles |
| Día 6 | Definir si se usa en web, formulario o borrador de WhatsApp |
| Día 7 | Decidir siguiente mejora o integración |

---

### 7. Guía ética y práctica
Reglas rápidas:
- No usar datos sensibles.
- No prometer lo que no se puede cumplir.
- Avisar si el usuario habla con IA, si corresponde.
- Derivar a humano en reclamos, salud, legal, financiero o temas delicados.
- Revisar respuestas antes de automatizar completamente.

---

### 8. Slides del workshop
Versión PDF o link para repasar después.

---

### 9. Comunidad opcional
- Grupo de WhatsApp o Telegram.
- Canal para compartir avances.
- Reto de 7 días.
- Sesión de seguimiento opcional.

---

## 6. Slide count estimado por sección

| Sección | Slides estimadas | Contenido sugerido |
|---|---:|---|
| Bienvenida + pacto de acción | 2 | Título, reglas del juego, promesa del workshop |
| IA útil para startups | 4 | Casos de uso, errores comunes, ejemplos LatAm |
| Demo exprés | 2 | Paso a paso visual, captura del flujo |
| Diseña tu asistente | 5 | Canvas explicado, ejemplo, errores comunes |
| Break activo | 1 | Tiempo, QR de recursos, pregunta de networking |
| Manos a la obra | 4 | Instrucciones paso a paso, herramientas, prompt |
| Prueba, mejora y límites | 4 | Checklist, pruebas, ética, escalamiento |
| Demos + cierre | 3 | Formato de demo, compromisos, próximos pasos |
| **Total recomendado** | **25** | Sin contar anexos |

### Slides de respaldo opcionales
Tener 4-6 slides extra para contingencias:
- Cómo crear cuenta en herramientas.
- Qué hacer si falla internet.
- Ejemplos de prompts por industria.
- Ruta para llevar el asistente a WhatsApp.
- Errores comunes y cómo corregirlos.
- Recursos adicionales.

**Total sugerido incluyendo respaldo:** 29-31 slides.

---

## Recomendaciones de facilitación para mantener energía y ritmo

### 1. Usa lenguaje simple
Evita:
- APIs.
- Tokens.
- Fine-tuning.
- Embeddings.
- Arquitectura de agentes.

Usa:
- Instrucciones.
- Conocimiento.
- Pruebas.
- Ajustes.
- Asistente.

---

### 2. Regla 80/20
- 20% explicación.
- 80% acción.

Cada concepto debe llevar a una acción inmediata.

---

### 3. Mantén el taller no técnico
Si alguien pregunta algo muy técnico:
- Reconoce la pregunta.
- Dile que es una fase avanzada.
- Ofrece un recurso o conversación posterior.
- Vuelve al MVP.

---

### 4. Usa ejemplos locales
Ejemplos que funcionan en LatAm:
- Tienda online.
- Emprendimiento de comida.
- Servicios profesionales.
- Educación online.
- Salud y bienestar.
- Logística ligera.
- SaaS B2B simple.
- Comunidad o membresía.
- Consultoría.
- Marketplace.

---

### 5. Cuidado con la frustración tecnológica
Los puntos donde la gente se traba:
- Crear cuenta.
- Confirmar correo.
- Elegir herramienta.
- No saber qué escribir en el prompt.
- No tener preguntas frecuentes.
- Internet lento.

Solución:
- Tener guía visual.
- Tener cuentas demo.
- Tener casos ficticios.
- Tener helpers asignados.
- Tener versión offline del ejercicio.

---

### 6. Plan B si falla internet

Si el Wi-Fi colapsa:

1. Pasar a trabajo en parejas.
2. Usar el Canvas impreso.
3. Redactar el Prompt Maestro a mano o en documento local.
4. Hacer pruebas simuladas entre participantes.
5. Mostrar demo grabada.
6. Dejar el asistente listo para configurar cuando vuelva la conexión.

---

## Guion rápido para el facilitador

### Apertura, 1 minuto
> “Bienvenidos. Hoy no vamos a hablar de IA como si fuera magia. Vamos a construir algo real, simple y útil para su startup. En tres horas, cada uno se va con un asistente básico funcionando o con el prompt listo para lanzarlo. La regla es simple: hecho es mejor que perfecto.”

### Transición al ejercicio
> “Antes de abrir la herramienta, vamos a pensar. Un asistente malo responde rápido. Un asistente útil resuelve un problema concreto.”

### Cierre
> “La IA no va a reemplazar a tu startup, pero sí puede ahorrarte horas si la configuras bien. Su tarea esta semana es probarlo con usuarios reales, medir y mejorar. El asistente perfecto no existe; el asistente mejorado, sí.”

---

## Resultado esperado del workshop

Al finalizar, los participantes deberían tener:

- [ ] Un caso de uso claro.
- [ ] Un asistente creado o un Prompt Maestro listo.
- [ ] Al menos 3 pruebas realizadas.
- [ ] Una mejora aplicada.
- [ ] Límites definidos.
- [ ] Plan de acción de 7 días.
- [ ] Recursos para seguir sin depender del facilitador.

**Frase final sugerida:**  
> “Hoy no aprendimos teoría de IA. Hoy construimos una herramienta real para trabajar mejor, atender mejor y vender mejor.”