# DeepSeek V4 Flash (OpenRouter) — startup_content/workshop_outline

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.19 | quality: 9.72
- latency_total: 85.807s | tokens_per_second: 57.8
- input_tokens: 198 | output_tokens: 4957
- judge_score: 4.8 | justificación: 

## Respuesta completa

# Outline del Workshop: "Construye tu Asistente de IA para tu Startup"

**Duración total:** 3 horas  
**Audiencia:** Emprendedores early-stage no técnicos (20-30 personas)  
**Formato:** Presencial, práctico, enérgico  
**Herramienta principal:** [Voiceflow](https://www.voiceflow.com/) (gratuita, sin código, arrastrar y soltar) – los participantes crearán un chatbot con IA generativa.

---

## Materiales necesarios (preparar antes)

### Para el facilitador
- Proyector + pantalla
- Pizarrón blanco o rotafolio con marcadores
- Conexión a internet estable (con respaldo 4G)
- Micrófono inalámbrico (opcional, para energía)
- Plantilla de proyecto en Voiceflow (enlace compartido)
- Demo de un asistente ya funcionando (ej: chatbot de soporte)
- Lista de reproducción de música upbeat para breaks

### Para los participantes (pedir con 1 semana de antelación)
- **Laptop propia** con cargador
- **Cuenta gratuita en Voiceflow** (registro previo: voiceflow.com/signup)
- **Cuenta gratuita en OpenAI** (opcional, para API key – se puede usar la integración nativa de Voiceflow)
- Navegador Chrome o Edge actualizado
- 1 hoja de papel y bolígrafo (para diseño rápido)

### Material impreso (entregar al inicio)
- **Guía rápida** de 2 caras: pasos clave + capturas de pantalla
- **Tarjeta de recursos** (QR a plantilla, tutoriales, comunidad)
- **Post-it** de colores para dinámica de ideas

---

## Agenda detallada (3 horas)

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 – 0:30 | **1. Bienvenida y el "¿Por qué?"** | 30 min |
| 0:30 – 1:00 | **2. Diseña tu asistente en 3 pasos** | 30 min |
| 1:00 – 1:05 | Break rápido (estiramiento) | 5 min |
| 1:05 – 2:05 | **3. Construcción práctica (ejercicio principal)** | 60 min |
| 2:05 – 2:35 | **4. Publica y conecta tu asistente** | 30 min |
| 2:35 – 3:00 | **5. Demo, feedback y cierre** | 25 min |

---

## Desarrollo de cada bloque

### Bloque 1: Bienvenida y el "¿Por qué?" (30 min)

**Título:** De la idea al asistente en 90 minutos  
**Objetivo:** Que los participantes entiendan el valor de un asistente de IA para su startup y se sientan capaces de construirlo, incluso sin saber programar.  
**Dinámica:** Charla interactiva + demo en vivo  
**Key takeaway:** "Un asistente de IA no es magia, es un flujo de conversación que tú diseñas. Hoy vas a crear el tuyo."

**Slide count estimado:** 7 slides  
- Slide 1: Título + energía (1)  
- Slide 2: ¿Qué problema resuelve un asistente de IA? (2)  
- Slide 3: Casos reales en startups latinas (3)  
- Slide 4: Demo rápida – asistente de ventas funcionando (4-5)  
- Slide 5: Mapa del workshop (6)  
- Slide 6: Reglas del juego: "Sin miedo, sin código" (7)

**Actividad breve (5 min):**  
"Cada uno escribe en un post-it un dolor de su startup que un asistente podría resolver (atención al cliente, leads, FAQs). Lo pegamos en la pared y vemos patrones."

---

### Bloque 2: Diseña tu asistente en 3 pasos (30 min)

**Título:** El plano antes de construir  
**Objetivo:** Que los participantes definan el alcance, personalidad y flujo de su asistente en papel, antes de tocar la herramienta.  
**Dinámica:** Taller guiado con papel y lápiz + ejemplos en pizarrón  
**Key takeaway:** "Un buen asistente empieza con un prompt claro y un flujo lógico, no con código."

**Slide count estimado:** 10 slides  
- Slide 1: Los 3 pasos: Propósito → Personalidad → Flujo (1)  
- Slide 2: Paso 1 – Define el propósito (2)  
- Slide 3: Ejemplos de propósitos para startups (3)  
- Slide 4: Paso 2 – Dale personalidad (tono, reglas, límites) (4-5)  
- Slide 5: Ejemplo de prompt de sistema (6)  
- Slide 6: Paso 3 – Dibuja el flujo (bienvenida, preguntas, despedida) (7-8)  
- Slide 7: Plantilla de flujo en papel (9)  
- Slide 8: Ejercicio: cada uno dibuja su flujo en 10 min (10)

**Ejercicio en papel (10 min):**  
Cada participante dibuja un diagrama de flujo simple:  
- Inicio → Saludo → Capturar nombre/email → Responder FAQ → Despedida  
Usan el post-it de su dolor como inspiración.

---

### Bloque 3: Construcción práctica – ejercicio principal (60 min)

**Título:** Manos a la obra: tu asistente en Voiceflow  
**Objetivo:** Que cada participante construya un asistente funcional con al menos 3 interacciones, usando la plantilla compartida.  
**Dinámica:** Tutorial guiado paso a paso (facilitador proyecta + participantes siguen) con ayudantes circulando.  
**Key takeaway:** "En 60 minutos tienes un prototipo que puedes mostrar a tu equipo o inversor."

**Slide count estimado:** 5 slides (mínimo, la mayor parte es demo en vivo)  
- Slide 1: Pantalla de inicio de Voiceflow (1)  
- Slide 2: Cargar plantilla (enlace) (2)  
- Slide 3: Los 4 bloques mágicos: Texto, Pregunta, GPT, Fin (3)  
- Slide 4: Conectar GPT con tu prompt (captura) (4)  
- Slide 5: Probar en el simulador (5)

**Estructura del ejercicio (60 min):**  
| Tiempo | Actividad |
|--------|-----------|
| 0-5 | Abrir Voiceflow, cargar plantilla "Asistente base" |
| 5-15 | Personalizar saludo y mensaje de bienvenida |
| 15-30 | Agregar bloque GPT con el prompt de sistema que definieron |
| 30-40 | Configurar una pregunta de captura de datos (nombre, email) |
| 40-50 | Probar en el simulador, ajustar prompt |
| 50-60 | Compartir enlace de previsualización con el vecino |

**Rol del facilitador:**  
- Proyecta cada paso en vivo  
- Cada 10 minutos pide "levanten la mano si están atorados"  
- Dos ayudantes (si hay) resuelven dudas uno a uno  

---

### Bloque 4: Publica y conecta tu asistente (30 min)

**Título:** De prototipo a herramienta real  
**Objetivo:** Que los participantes sepan cómo publicar su asistente en web, WhatsApp o embed en su sitio, y cómo medirlo.  
**Dinámica:** Demo + discusión rápida  
**Key takeaway:** "Un asistente sin publicación es un juguete. Hoy lo conviertes en herramienta."

**Slide count estimado:** 7 slides  
- Slide 1: Opciones de publicación (1)  
- Slide 2: Embed en web (código HTML) (2)  
- Slide 3: Integración con WhatsApp (usando Twilio o WATI) (3-4)  
- Slide 4: Publicar en Slack, Telegram (5)  
- Slide 5: Analítica básica: qué mejorar (6)  
- Slide 6: Demo rápida: publicar en web y probar en celular (7)

**Actividad (10 min):**  
Cada participante publica su asistente como enlace público (Voiceflow lo permite gratis) y lo abre en su celular. Lo prueba con su vecino.

---

### Bloque 5: Demo, feedback y cierre (25 min)

**Título:** Tu asistente en acción  
**Objetivo:** Celebrar los logros, compartir aprendizajes y dar recursos para seguir.  
**Dinámica:** Demos voluntarias (3-4 personas) + ronda rápida de feedback  
**Key takeaway:** "Hoy diste el primer paso. Mañana puedes escalarlo."

**Slide count estimado:** 4 slides  
- Slide 1: "Comparte tu creación" (1)  
- Slide 2: Preguntas para mejorar: ¿qué le falta? ¿qué sorprendió? (2)  
- Slide 3: Recursos para llevar a casa (3)  
- Slide 4: Cierre + contacto + encuesta de satisfacción (4)

**Actividad final (10 min):**  
- 3 voluntarios muestran su asistente (2 min c/u)  
- Facilitador da un consejo personalizado  
- Todos escanean QR con recursos  

---

## Ejercicio principal del workshop (detalle)

**Nombre:** "De la idea al prototipo en 60 minutos"  
**Herramienta:** Voiceflow (gratuita, sin código)  
**Resultado esperado:** Un asistente de IA funcional que:  
- Saluda al usuario  
- Captura nombre y email (o dato relevante)  
- Responde 2-3 preguntas frecuentes usando GPT (con prompt personalizado)  
- Se despide y ofrece contacto humano  

**Pasos guiados (los participantes siguen al facilitador):**  
1. **Abrir plantilla** – enlace pre-generado con flujo básico  
2. **Personalizar bloque de inicio** – cambiar texto de bienvenida  
3. **Agregar bloque "Preguntar nombre"** – tipo "Text" con variable  
4. **Insertar bloque GPT** – pegar el prompt de sistema que diseñaron en papel  
5. **Conectar bloques** – condicional simple (si respuesta contiene "ayuda", derivar a humano)  
6. **Probar en simulador** – escribir preguntas, ver respuestas  
7. **Ajustar prompt** – si la IA responde mal, mejorar instrucciones  
8. **Compartir enlace** – copiar URL de previsualización  

**Material de apoyo:**  
- Plantilla de Voiceflow (enlace acortado)  
- Hoja con prompts de ejemplo:  
  > *"Eres un asistente de ventas para [nombre startup]. Tu tono es amigable y profesional. Responde preguntas sobre precios, horarios y servicios. Si no sabes algo, di que un humano te contactará."*  
- Tarjeta con variables comunes: `{name}`, `{email}`, `{question}`  

---

## Recursos para llevar a casa

**1. Enlaces directos**  
- Plantilla de Voiceflow usada en el workshop  
- Tutorial en video (grabación del taller, si aplica)  
- Guía PDF "De 0 a asistente IA en 5 pasos"  

**2. Herramientas gratuitas recomendadas**  
- **Voiceflow** – creación de chatbots visuales  
- **ChatGPT** – para afinar prompts  
- **Zapier** – conectar asistente con CRM/email  
- **Botpress** – alternativa open source  
- **Tidio** – chat en vivo + IA para web  

**3. Comunidad y aprendizaje**  
- Grupo de WhatsApp del workshop (para dudas post-evento)  
- Canal de YouTube con mini tutoriales  
- Próximo webinar: "Cómo medir el ROI de tu asistente"  

**4. Desafío de 7 días**  
- Día 1: Agregar 3 preguntas más a tu asistente  
- Día 2: Conectar con formulario de Google Sheets  
- Día 3: Publicar en tu web  
- Día 4: Probar con 5 usuarios reales  
- Día 5: Ajustar prompt basado en feedback  
- Día 6: Agregar un bloque de "hablar con humano"  
- Día 7: Compartir resultados en el grupo  

---

## Notas para el facilitador

- **Energía:** Usa música al inicio y durante los breaks. Camina entre los participantes.  
- **Tiempo:** Si el bloque 3 se alarga, recorta el bloque 4 (pueden publicar después).  
- **Inclusión:** Algunos pueden tener laptops lentas o sin internet – forma parejas.  
- **Cierre:** Termina con una frase motivadora tipo: *"Hoy construiste algo que ayer parecía imposible. Ahora ve y haz crecer tu startup con IA."*