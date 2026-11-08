# Qwen 3.8 Max 0902 — startup_content/workshop_outline

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.87 | quality: 10.0
- latency_total: 312.513s | tokens_per_second: 41.4
- input_tokens: 240 | output_tokens: 12950
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores no técnicos, proporcionando una agenda detallada y práctica para construir un asistente de IA.

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

**Promesa del workshop:**  
En 3 horas, emprendedores early-stage no técnicos salen con un **asistente de IA MVP funcionando**, entrenado con información real de su startup y listo para probar con usuarios, clientes o su propio equipo.

**Audiencia:** 20–30 emprendedores early-stage, no técnicos.  
**Formato:** presencial, práctico, manos a la obra.  
**Recomendación:** mesas de 4–5 personas, 1 facilitador principal + 1 apoyo técnico/logístico.

---

## 1. Agenda detallada con tiempos — 3 horas / 180 minutos

| Hora | Bloque | Duración | Objetivo | Dinámica | Key takeaway |
|---|---|---:|---|---|---|
| 0:00–0:10 | **1. Bienvenida: “Hoy construyes, no solo escuchas”** | 10 min | Activar energía, alinear expectativas y explicar el reto del día. | Charla breve + encuesta rápida a mano alzada. | No necesitas ser programador para construir un asistente útil. |
| 0:10–0:25 | **2. Demo en vivo: un asistente trabajando para una startup** | 15 min | Mostrar un asistente real resolviendo casos de negocio. | Demo en vivo + preguntas rápidas. | Un asistente útil = buenas instrucciones + buenos datos + límites claros. |
| 0:25–0:45 | **3. Diseña tu caso: Asistente Canvas** | 20 min | Definir el problema, usuario, objetivo y datos del asistente. | Ejercicio individual/en parejas con plantilla. | El mejor asistente no hace todo: resuelve un dolor concreto. |
| 0:45–1:10 | **4. Manos al prompt: crea el cerebro de tu asistente** | 25 min | Redactar el prompt maestro con rol, contexto, reglas y tono. | Ejercicio guiado + mini demo del facilitador. | Un buen prompt da claridad, límites y ejemplos. |
| 1:10–1:20 | **5. Break activo: recarga y networking** | 10 min | Descansar, resolver dudas rápidas y compartir con otros. | Descanso + conversación informal. | Compartir tu caso con otro emprendedor mejora tu claridad. |
| 1:20–1:55 | **6. Entrénalo con tu conocimiento real** | 35 min | Cargar datos, FAQs o documentos y hacer pruebas reales. | Ejercicio práctico + test entre pares. | La calidad de los datos importa más que la “magia” de la IA. |
| 1:55–2:15 | **7. Conviértelo en un MVP compartible** | 20 min | Dejar el asistente listo para mostrar, usar o validar. | Ejercicio práctico + demostración rápida. | Un MVP simple ya sirve para aprender con usuarios reales. |
| 2:15–2:35 | **8. Prueba de fuego: calidad, riesgos y mejoras** | 20 min | Detectar errores, huecos, riesgos y oportunidades de mejora. | Red team en parejas + checklist de calidad. | Lanza rápido, pero con límites, revisión humana y responsabilidad. |
| 2:35–3:00 | **9. Demo express, compromisos y cierre** | 25 min | Socializar resultados y definir próximos pasos. | Demos voluntarias + compromiso final + cierre. | El workshop termina cuando empieza tu experimento real. |

**Total: 180 minutos / 3 horas.**

---

## 2. Materiales necesarios: qué preparar antes

### A. Antes del workshop — para participantes

Enviar un correo o mensaje 3–5 días antes con este checklist:

**Cada participante debe llevar:**

- Laptop cargada.
- Cuenta gratuita creada en al menos una herramienta de IA:
  - ChatGPT, Claude, Gemini o la que el facilitador recomiende.
- Un documento corto de su startup:
  - Qué hace.
  - A quién sirve.
  - Problema que resuelve.
  - Producto o servicio principal.
- 10 preguntas frecuentes reales o probables de clientes.
- Si tienen, ejemplos de:
  - Mensajes de clientes por WhatsApp.
  - Objeciones de venta.
  - Dudas de onboarding.
  - Respuestas que hoy responden manualmente.

**Importante para LatAm:**  
Si algunos participantes tienen problemas para crear cuentas, pedir que vengan con al menos una cuenta lista o que traigan un correo alternativo. También se puede trabajar en parejas.

---

### B. Materiales del espacio físico

Preparar antes del evento:

- Salón con mesas tipo taller, no estilo conferencia.
- Sillas móviles para trabajo en grupos.
- Pantalla o proyector visible desde todos los ángulos.
- Buen sonido o micrófono si el grupo es mayor a 20 personas.
- WiFi probado antes del evento.
- Alargadores o zapatillas eléctricas por mesa.
- Enchufes accesibles.
- Agua, café o snacks simples.
- Post-its.
- Marcadores.
- Hojas impresas del “Asistente Canvas”.
- Tarjetas o stickers con nombre.
- Timer visible.
- Música suave para los momentos de ejercicio.

---

### C. Materiales digitales del facilitador

Preparar:

- Slide deck del workshop.
- Demo de un asistente ya funcionando.
- Plantilla de “Asistente Canvas” en PDF o link.
- Plantilla de “Prompt Maestro”.
- Documento de conocimiento de ejemplo:
  - FAQs ficticias.
  - Descripción de producto.
  - Políticas simples.
- Checklist de pruebas.
- Link corto o QR con todos los recursos.
- Cuenta de respaldo del facilitador.
- Video o screenshots de la demo por si falla internet.
- Hotspot móvil de backup.
- Carpeta compartida o Drive con materiales.

---

### D. Kit de emergencia / Plan B

Para que el workshop no dependa 100% de internet o cuentas:

- Plantillas impresas.
- Ejemplos de prompts impresos.
- Capturas del flujo de creación del asistente.
- Video corto de la demo.
- Trabajo en parejas si alguien no tiene cuenta.
- Cuenta demo del facilitador para mostrar en vivo.
- Versión “sin código” del ejercicio: diseñar el asistente en papel y simular respuestas.

---

## 3. Detalle por bloque

---

### Bloque 1: “Hoy construyes, no solo escuchas”  
**Duración:** 10 minutos  
**Hora sugerida:** 0:00–0:10  

**Objetivo:**  
Subir la energía, dejar claras las reglas y activar mentalidad práctica.

**Dinámica:**  
- Bienvenida rápida.
- Explicación del reto: “Hoy se llevan un asistente MVP”.
- Encuesta rápida:
  - ¿Quién ya usa IA?
  - ¿Quién tiene un proceso repetitivo que odia hacer?
  - ¿Quién quiere automatizar atención, ventas o operaciones?

**Key takeaway:**  
La IA no viene a reemplazar al fundador; viene a quitarle trabajo repetitivo para que se enfoque en vender, validar y construir.

---

### Bloque 2: Demo en vivo — “Un asistente trabajando para una startup”  
**Duración:** 15 minutos  
**Hora sugerida:** 0:10–0:25  

**Objetivo:**  
Mostrar qué es un asistente de IA aplicado a una startup real.

**Dinámica:**  
Demo en vivo de un asistente que puede:

- Responder preguntas frecuentes.
- Explicar un producto.
- Calificar un lead.
- Pedir datos faltantes.
- Derivar a una persona humana cuando no sabe.
- Mantener un tono de marca.

El facilitador muestra el “detrás de escena”:

- Prompt.
- Base de conocimiento.
- Límites.
- Pruebas.

**Key takeaway:**  
Un asistente no es “magia”: es un sistema con instrucciones claras, datos confiables y pruebas constantes.

---

### Bloque 3: Diseña tu caso — “Asistente Canvas”  
**Duración:** 20 minutos  
**Hora sugerida:** 0:25–0:45  

**Objetivo:**  
Que cada emprendedor defina un caso de uso concreto.

**Dinámica:**  
Cada participante completa una plantilla simple:

1. ¿Qué problema resuelve mi asistente?
2. ¿Para quién es?
3. ¿Qué tarea principal hará?
4. ¿Qué información necesita saber?
5. ¿Qué no debe hacer?
6. ¿Cuándo debe derivar a un humano?
7. ¿Cómo sabré que funciona?

**Ejemplos de casos recomendados para no técnicos:**

- Asistente de preguntas frecuentes.
- Asistente de atención al cliente.
- Asistente de calificación de leads.
- Asistente de onboarding básico.
- Asistente para explicar precios o planes.
- Asistente interno para responder dudas del equipo.

**Key takeaway:**  
No construyas “un asistente para todo”. Construye un asistente para un dolor específico.

---

### Bloque 4: Manos al prompt — “Crea el cerebro de tu asistente”  
**Duración:** 25 minutos  
**Hora sugerida:** 0:45–1:10  

**Objetivo:**  
Redactar el prompt maestro del asistente.

**Dinámica:**  
Ejercicio guiado. El facilitador muestra una estructura y todos la completan.

**Estructura recomendada del prompt:**

1. **Rol:** quién es el asistente.
2. **Contexto:** qué startup representa.
3. **Objetivo:** qué debe lograr.
4. **Audiencia:** con quién habla.
5. **Fuentes:** qué información puede usar.
6. **Formato:** cómo responde.
7. **Tono:** cercano, profesional, simple, etc.
8. **Límites:** qué no puede inventar.
9. **Derivación:** cuándo pasar a humano.
10. **Ejemplos:** una buena respuesta y una mala respuesta.

**Key takeaway:**  
Si el prompt es claro, el asistente responde mejor. Si el prompt es vago, el asistente inventa.

---

### Bloque 5: Break activo  
**Duración:** 10 minutos  
**Hora sugerida:** 1:10–1:20  

**Objetivo:**  
Recargar energía y generar networking.

**Dinámica:**  
- Pausa corta.
- El facilitador invita a que cada persona le cuente a alguien:
  - “Mi asistente va a resolver…”
  - “Mi mayor duda ahora es…”

**Key takeaway:**  
Explicar tu caso en una frase te ayuda a construirlo mejor.

---

### Bloque 6: Entrénalo con tu conocimiento real  
**Duración:** 35 minutos  
**Hora sugerida:** 1:20–1:55  

**Objetivo:**  
Que el asistente use información real o realista de la startup.

**Dinámica:**  
Cada participante:

1. Crea o sube un documento de conocimiento:
   - FAQs.
   - Descripción del producto.
   - Precios.
   - Políticas.
   - Casos comunes.
2. Lo carga en la herramienta de IA o lo pega como contexto.
3. Prueba con preguntas reales.
4. Ajusta el prompt según las respuestas.

**Pruebas mínimas:**

- 5 preguntas fáciles.
- 3 preguntas difíciles.
- 2 preguntas trampa o fuera de alcance.

**Ejemplos de preguntas trampa:**

- “¿Me puedes dar un descuento que no está en la información?”
- “¿Qué pasa si mi caso no está cubierto?”
- “Inventa una política de reembolso.”
- “Actúa como abogado y dame consejo legal.”

**Key takeaway:**  
El asistente mejora cuando lo entrenas con información real, concreta y bien organizada.

---

### Bloque 7: Conviértelo en un MVP compartible  
**Duración:** 20 minutos  
**Hora sugerida:** 1:55–2:15  

**Objetivo:**  
Que el asistente quede en un formato mínimo para usar o mostrar.

**Dinámica:**  
Dependiendo de la herramienta elegida, cada participante puede:

**Opción A — MVP simple:**  
Dejar listo un chat con:
- Prompt maestro.
- Documento de conocimiento cargado.
- Instrucciones para reutilizarlo.

**Opción B — MVP personalizado:**  
Crear un asistente personalizado si la herramienta lo permite:
- Custom GPT.
- Claude Project.
- Gemini Gem.
- Bot en Poe.
- Chatbase, Dante, Landbot u otra opción no-code.

**Opción C — MVP para WhatsApp o redes:**  
Si la startup atiende por WhatsApp, Instagram o Messenger:
- Adaptar las respuestas a mensajes cortos.
- Crear un flujo de conversación.
- Simular el bot en un documento.
- Dejarlo listo para implementar después con una herramienta de mensajería.

**Key takeaway:**  
No necesitas lanzar perfecto. Necesitas lanzar algo que puedas probar mañana.

---

### Bloque 8: Prueba de fuego — calidad, riesgos y mejoras  
**Duración:** 20 minutos  
**Hora sugerida:** 2:15–2:35  

**Objetivo:**  
Detectar errores, alucinaciones, riesgos y mejoras.

**Dinámica:**  
En parejas, cada persona prueba el asistente del otro.

**Checklist de calidad:**

- ¿Responde con claridad?
- ¿Usa la información correcta?
- ¿Inventa datos?
- ¿Pide aclaración si falta información?
- ¿Reconoce cuando no sabe?
- ¿Deriva a humano cuando corresponde?
- ¿Mantiene el tono correcto?
- ¿Evita promesas legales, médicas o financieras?
- ¿Respeta la privacidad?
- ¿Se entiende en español local?

**Key takeaway:**  
Un asistente de IA se puede lanzar rápido, pero se debe revisar con responsabilidad.

---

### Bloque 9: Demo express, compromisos y cierre  
**Duración:** 25 minutos  
**Hora sugerida:** 2:35–3:00  

**Objetivo:**  
Mostrar resultados, celebrar avances y definir próximos pasos.

**Dinámica:**  
- 3–5 demos voluntarias de 2 minutos.
- Feedback rápido del facilitador.
- Cada participante escribe su compromiso:
  - “Mañana voy a probar mi asistente con…”
  - “Esta semana voy a mejorar…”
  - “Voy a medir…”

**Cierre:**  
El facilitador recuerda que el objetivo no fue crear un producto final, sino un experimento serio.

**Key takeaway:**  
El verdadero trabajo empieza mañana: probar, medir, ajustar y volver a probar.

---

## 4. Ejercicio principal del workshop

### 🛠️ Reto central: “Construye tu Asistente MVP en 90 minutos”

**Objetivo del ejercicio:**  
Que cada emprendedor termine con un asistente funcional que pueda responder preguntas, guiar usuarios o apoyar un proceso simple de su startup.

**Requisito:**  
Debe ser tan simple que todos puedan hacerlo, incluso sin conocimientos técnicos.

---

### Caso recomendado para la mayoría

**Asistente de respuestas para clientes o usuarios.**

Ejemplos:

- Responder preguntas frecuentes.
- Explicar cómo funciona el producto.
- Dar información de precios.
- Ayudar con dudas de compra.
- Hacer triage básico de soporte.
- Calificar leads con preguntas simples.

---

### Entregable final del participante

Cada emprendedor debe terminar con:

1. **Asistente Canvas completado.**
2. **Prompt maestro del asistente.**
3. **Base de conocimiento mínima.**
4. **Prueba con al menos 10 preguntas.**
5. **Lista de 3 mejoras prioritarias.**
6. **MVP compartible**, que puede ser:
   - Un chat configurado.
   - Un asistente personalizado.
   - Un documento listo para copiar y pegar.
   - Un flujo simulado para WhatsApp.

---

### Paso a paso del ejercicio

#### Paso 1: Elige un dolor concreto — 20 minutos

El participante responde:

- ¿Qué tarea repetitiva quiero reducir?
- ¿Quién usará el asistente?
- ¿Qué pregunta o problema resolverá?
- ¿Qué resultado sería exitoso?

**Ejemplo:**

> “Quiero un asistente que responda las dudas más frecuentes de clientes sobre mi servicio de suscripción, para reducir mensajes repetitivos por WhatsApp.”

---

#### Paso 2: Crea la base de conocimiento — 15 minutos dentro del bloque de entrenamiento

El participante prepara un documento simple con:

- Nombre de la startup.
- Descripción del producto o servicio.
- Público objetivo.
- 10 preguntas frecuentes.
- Respuestas correctas.
- Precios, si aplica.
- Políticas básicas.
- Casos donde se necesita ayuda humana.
- Frases de tono o marca.

**Ejemplo de base de conocimiento mínima:**

```text
Startup: EcoEnvíos
Qué hace: Servicio de entregas locales en bicicleta.
Clientes: Tiendas online y restaurantes pequeños.
Horario: Lunes a viernes, 9:00 a 18:00.
Cobertura: Zona centro y norte de la ciudad.
Precio base: $3 por entrega en zona centro.
Entregas urgentes: +$1.50.
Política: Si el cliente no está disponible, se espera 10 minutos.
Derivar a humano si: hay reclamos, paquetes perdidos o solicitudes especiales.
Tono: cercano, responsable, simple.
```

---

#### Paso 3: Redacta el prompt maestro — 25 minutos

Plantilla recomendada:

```text
Eres el asistente virtual de [nombre de tu startup].

Tu objetivo principal es [objetivo del asistente].

Tu audiencia son [tipo de usuario/cliente].

Debes usar únicamente la información proporcionada en la base de conocimiento. Si no encuentras la respuesta, di claramente que no tienes esa información y ofrece derivar a una persona humana.

No inventes datos.
No des consejos legales, médicos, financieros o técnicos complejos.
No prometas descuentos, reembolsos o condiciones que no estén explícitamente indicadas.
No pidas datos sensibles como contraseñas, tarjetas completas, documentos de identidad o información confidencial.

Tu tono debe ser [cercano/profesional/simple/amable/directo].

Cuando respondas:
1. Sé breve y claro.
2. Usa lenguaje simple.
3. Si falta información, haz una pregunta para aclarar.
4. Si el problema requiere intervención humana, indícalo.
5. Si el usuario quiere comprar o contratar, guía hacia [acción deseada].

Ejemplo de buena respuesta:
Usuario: ¿Hacen entregas los domingos?
Asistente: Por ahora operamos de lunes a viernes de 9:00 a 18:00. Si necesitas una entrega especial, puedo ayudarte a dejar tu solicitud para que el equipo la revise.

Ejemplo de mala respuesta:
Usuario: ¿Hacen entregas los domingos?
Asistente: Sí, claro, podemos coordinar cuando quieras.
```

---

#### Paso 4: Prueba con 10 preguntas — 35 minutos

Cada participante debe probar su asistente con:

**5 preguntas normales:**

- ¿Qué hace tu startup?
- ¿Cuánto cuesta?
- ¿Cómo funciona?
- ¿Dónde atienden?
- ¿Cómo puedo empezar?

**3 preguntas difíciles:**

- ¿Qué pasa si el producto llega tarde?
- ¿Puedo cancelar?
- ¿Tienen descuentos?

**2 preguntas trampa:**

- Inventa algo que no está en la información.
- Pide algo fuera de alcance.
- Haz una pregunta legal, médica o financiera.

**Criterio de éxito:**

El asistente debe:

- Responder correctamente al menos 7 de 10 preguntas.
- No inventar información crítica.
- Pedir aclaración cuando falten datos.
- Reconocer cuando no sabe.
- Derivar a humano si corresponde.

---

#### Paso 5: Conviértelo en MVP — 20 minutos

El participante deja el asistente listo de alguna de estas formas:

**Nivel 1 — MVP básico:**  
Tiene un chat con prompt y documento cargado.

**Nivel 2 — MVP reutilizable:**  
Guarda el prompt, el documento y las instrucciones para volver a usarlo.

**Nivel 3 — MVP compartible:**  
Crea un bot personalizado o un link si la herramienta lo permite.

**Nivel 4 — MVP para WhatsApp:**  
Adapta las respuestas a mensajes cortos y deja un flujo listo para implementar.

---

### Cómo asegurar que todos puedan hacerlo

Para que sea inclusivo y práctico:

- Si alguien no tiene cuenta, trabaja en pareja.
- Si alguien no tiene laptop, puede trabajar con compañero y completar canvas impreso.
- Si internet falla, usar versión papel + simulación.
- Si una herramienta no está disponible, usar otra equivalente.
- Si alguien se bloquea, el facilitador le da un caso de ejemplo listo para adaptar.

**Regla de oro:**  
Nadie debe quedarse sin construir algo útil.

---

## 5. Recursos para llevar a casa

Al final del workshop, cada participante debería recibir un “Kit del Builder” mediante QR o link corto.

### Recursos recomendados

1. **Asistente Canvas PDF**
   - Plantilla de una página para definir el asistente.

2. **Plantilla de Prompt Maestro**
   - Versión editable para copiar y pegar.

3. **Banco de 20 prompts para startups**
   - Atención al cliente.
   - Ventas.
   - Marketing.
   - Operaciones.
   - Investigación de mercado.
   - Soporte interno.

4. **Checklist de pruebas**
   - 10 preguntas normales.
   - 5 preguntas difíciles.
   - 5 preguntas trampa.

5. **Base de conocimiento de ejemplo**
   - Documento ficticio para practicar.

6. **Guía rápida de herramientas no-code**
   - Opciones gratuitas.
   - Opciones freemium.
   - Opciones para WhatsApp.
   - Opciones para web.
   - Opciones para uso interno.

7. **Plantilla de flujo para WhatsApp**
   - Mensaje de bienvenida.
   - Menú simple.
   - Respuestas frecuentes.
   - Derivación a humano.

8. **Plan de 7 días para mejorar tu asistente**
   - Día 1: probar con 3 usuarios.
   - Día 2: corregir respuestas.
   - Día 3: agregar 10 FAQs nuevas.
   - Día 4: ajustar tono.
   - Día 5: definir límites.
   - Día 6: medir tiempo ahorrado.
   - Día 7: decidir si escalar o simplificar.

9. **Checklist de responsabilidad y privacidad**
   - No subir datos sensibles.
   - No compartir información confidencial.
   - Revisar respuestas antes de publicar.
   - Informar cuando se usa IA, si aplica.
   - Tener siempre opción humana.

10. **Comunidad opcional**
   - Grupo de WhatsApp, Slack o Discord para seguir compartiendo avances.

---

## 6. Slide count estimado por sección

La presentación debe ser ligera, visual y práctica. Nada de slides eternos.

| Sección | Slides estimados | Recomendación |
|---|---:|---|
| 1. Bienvenida y reto | 3 | Energía, promesa y reglas. |
| 2. Demo en vivo | 4 | Apoyo visual mínimo; prioridad a la demo. |
| 3. Asistente Canvas | 4 | Explicar plantilla con ejemplo. |
| 4. Prompt maestro | 5 | Mostrar estructura y ejemplo completo. |
| 5. Break | 1 | Timer, música o instrucción simple. |
| 6. Entrenamiento y pruebas | 5 | Paso a paso y checklist de pruebas. |
| 7. MVP compartible | 4 | Opciones de publicación o uso inmediato. |
| 8. Calidad, riesgos y mejoras | 4 | Checklist, ética y límites. |
| 9. Demos y cierre | 4 | Instrucciones para demos y compromiso final. |

**Total estimado: 34 slides.**

**Regla práctica:**  
Máximo 1 idea por slide. Si una slide tiene más de 20 palabras, probablemente debería ser una plantilla o un ejercicio, no texto.

---

## Recomendaciones especiales para contexto LatAm

### 1. WhatsApp primero
Muchas startups en Latinoamérica atienden por WhatsApp. Aunque el workshop no termine con un bot de WhatsApp publicado, sí debe incluir:

- Respuestas cortas.
- Lenguaje natural.
- Flujo simple.
- Derivación a humano.
- Plantillas listas para copiar.

### 2. Herramientas accesibles
Prioriza herramientas gratuitas o freemium. Antes del workshop, valida:

- Disponibilidad en los países de los participantes.
- Necesidad de tarjeta de crédito.
- Límites de uso gratuito.
- Facilidad para crear cuentas.

### 3. Conexión inestable
Siempre ten:

- Hotspot móvil.
- Demo grabada.
- Materiales descargables.
- Versión impresa.
- Ejercicios que puedan hacerse sin internet por unos minutos.

### 4. Lenguaje local
El asistente debe sonar natural para el país o región:

- “Vos”, “tú” o “usted” según mercado.
- Moneda local.
- Horarios reales.
- Canales habituales.
- Expresiones comunes sin exagerar.

### 5. Privacidad y confianza
Recuerda a los participantes:

- No subir datos sensibles de clientes reales sin consentimiento.
- Usar datos ficticios si hay dudas.
- Evitar información bancaria, médica o legal sensible.
- Revisar respuestas antes de publicarlas públicamente.

---

## Criterios de éxito del workshop

Un buen resultado sería:

- 90% de participantes completó el Asistente Canvas.
- 80% o más terminó con un asistente probado.
- Cada participante identificó al menos 3 mejoras.
- Los participantes entienden que el asistente necesita datos, límites y pruebas.
- Nadie se queda bloqueado por falta de acceso, cuenta o conocimiento técnico.
- Los emprendedores salen con una acción concreta para los próximos 7 días.

---

## Cierre sugerido del facilitador

> “Hoy no vinimos a hablar de IA. Vinimos a construir algo útil.  
> Su asistente no tiene que ser perfecto hoy. Tiene que ser probado mañana.  
> El emprendedor que prueba rápido, aprende rápido.  
> Y el que aprende rápido, construye mejor.”