# GPT-OSS 120B — startup_content/workshop_outline

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.93 | quality: 9.8
- latency_total: 32.466s | tokens_per_second: 63.1
- input_tokens: 247 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y dinámicas de bloques bien estructuradas.

## Respuesta completa

## **Workshop Presencial (3 h) – “Construye tu Asistente de IA para tu Startup”**  
**Público:** Emprendedores early‑stage sin conocimientos técnicos (20‑30 personas)  
**Formato:** Presencial, con laptops/ tablets de los participantes y una pantalla gigante para demo en vivo.

---

## 1️⃣ Agenda Detallada (3 h)

| Horario | Bloque | Duración |
|---------|--------|----------|
| **00:00 – 00:10** | Welcome & Warm‑up | 10 min |
| **00:10 – 00:35** | ¿Qué es un asistente de IA y por qué lo necesita tu startup? | 25 min |
| **00:35 – 01:15** | Arquitectura “low‑code” – Herramientas sin código (No‑Code AI) | 40 min |
| **01:15 – 01:25** | **Coffee‑break rápido** | 10 min |
| **01:25 – 02:45** | **Ejercicio práctico – Crea tu propio asistente** (hands‑on) | 80 min |
| **02:45 – 02:55** | Pitch‑light de los prototipos y feedback grupal | 10 min |
| **02:55 – 03:00** | Cierre, próximos pasos y entrega de recursos | 5 min |

> **Total:** 180 min = 3 h  

---

## 2️⃣ Materiales Necesarios (pre‑work)

| Tipo | Detalle | ¿Quién lo prepara? |
|------|---------|--------------------|
| **Sala** | Sillas en “U” o mesas grupales, proyector + pantalla, sonido, pizarra o flipchart, post‑its, marcadores de colores | Organizador del venue |
| **Tecnología** | 1 punto Wi‑Fi sólido (mín. 50 Mbps), enchufes / regletas, 2 laptops del facilitador (para demo) | Facilitador + IT |
| **Cuentas** | **Cuenta gratuita** en al menos una de estas plataformas (se escogerá una para la demo): <br>• **ChatGPT (OpenAI) + Playground** <br>• **Microsoft Power Virtual Agents** <br>• **Google Dialogflow CX (plan trial)** <br>• **Bubble + API Connector** <br>Se pide a los participantes crear la cuenta **antes** del workshop y traer el acceso (email). | Facilitador envía email de invitación 48 h antes |
| **Plantilla** | PDF “Canvas de Asistente IA” (objetivo, usuarios, flujos, tono, métricas) | Facilitador (distribución al iniciar) |
| **Handout** | Resumen de “10 comandos rápidos” para entrenar prompts, checklist de seguridad de datos | Facilitador (imprimir) |
| **Material visual** | Slides (PowerPoint / Google Slides) – 55‑65 diapositivas | Facilitador (preparar) |
| **Premios simbólicos** | Stickers, libreta de ideas, “certificado de creador IA” | Organización |

---

## 3️⃣ Bloques Detallados

### **Bloque 0 – Welcome & Warm‑up (10 min)**
| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Romper el hielo, crear comunidad y alinear expectativas. |
| **Dinámica** | 1️⃣ Breve presentación del facilitador (2 min). <br>2️⃣ Cada participante dice su nombre, sector y **un reto** que le gustaría solucionar con IA (30 seg). <br>3️⃣ Muro de post‑its: “Mi idea de asistente” (colocamos en la pared). |
| **Key takeaway** | Todos comparten una necesidad real y vemos la diversidad de oportunidades. |
| **Slides** | 3 (bienvenida, agenda visual, dinámica rápida). |

---

### **Bloque 1 – ¿Qué es un asistente de IA y por qué lo necesita tu startup? (25 min)**
| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Entender, en 5 min, el valor de un asistente (ventas, soporte, interno) y desmontar mitos de “es para gigantes tech”. |
| **Dinámica** | Charla + 2 casos relámpago (30‑seg cada uno) de startups latam que usan IA (ej.: “Rappi Bot”, “Kavak FAQ IA”). <br>Mini‑encuesta con Mentimeter: “¿Cuál sería tu caso de uso ideal?” |
| **Key takeaway** | **Un asistente = ahorro de tiempo + mayor conversión**; cualquier startup puede crear uno sin programar. |
| **Slides** | 8‑10 (definición, beneficios, ejemplos, encuesta). |

---

### **Bloque 2 – Arquitectura “low‑code” – Herramientas sin código (40 min)**
| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Conocer el stack sin código y decidir la herramienta más cómoda para el día de hoy. |
| **Dinámica** | Demo en vivo (10 min) + tabla comparativa (5 min) + **Speed‑Round** de 3‑min por herramienta (participantes prueban “saludar” al bot y ven respuesta). |
| **Herramientas mostradas** | 1️⃣ **ChatGPT Playground** (prompt‑engineering básico) <br>2️⃣ **Microsoft Power Virtual Agents** (drag‑and‑drop) <br>3️⃣ **Google Dialogflow CX** (flujos visuales) |
| **Key takeaway** | Cada herramienta tiene **3 pilares**: facilidad de uso, integración con canales y costos. Elige la que mejor encaje con tu presupuesto y público. |
| **Slides** | 12‑15 (roadmap, tabla comparativa, pasos de configuración). |

---

### **Bloque 3 – Ejercicio práctico – Crea tu propio asistente (80 min)**
> **Este es el corazón del workshop. Todos salen con un prototipo funcional (aunque sea “hello‑world”).**

| Sub‑bloque | Duración | Dinámica | Detalle |
|------------|----------|----------|--------|
| **3.1** Preparación del canvas | 10 min | Individual + grupo | Cada participante rellena el **Canvas de Asistente IA** (objetivo, usuario, tono, 3 intents). |
| **3.2** Creación del “prompt base” (ChatGPT) | 15 min | Parejas | Con el prompt de ejemplo, añaden variables de su caso. Testean en Playground; ajustan hasta que el bot responde coherentemente. |
| **3.3** Definir flujos simples (Power Virtual Agents) | 20 min | Grupos de 4 | Arrastran bloques: “Saludo → Pregunta de cliente → Respuesta → Escalada a humano”. |
| **3.4** Conectar a un canal (Web widget o WhatsApp sandbox) | 15 min | Individual + asistente del facilitador | Copian el código embed y lo pegan en una página HTML simple (se les entrega una plantilla). |
| **3.5** Test rápido y mejora | 10 min | Solo | Intercambian dispositivos con el vecino y prueban el asistente del otro, anotan 2 mejoras. |
| **3.6** Documentar & guardar | 10 min | Individual | Exportan el proyecto (link o archivo) a la carpeta de Google Drive del workshop. |

| **Objetivo global** | Tener un asistente “mínimo viable” (MVP) listo para probar con clientes reales. |
| **Key takeaway** | **MVP en 30 min** es posible: define objetivo → escribe prompt → crea 2‑3 intents → publica. |
| **Slides** | 20‑25 (instrucciones paso‑a‑paso, screenshots, checklist de errores comunes). |

---

### **Bloque 4 – Pitch‑light y feedback (10 min)**
| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Mostrar rápidamente lo creado, generar confianza y obtener ideas de mejora. |
| **Dinámica** | Cada equipo (máx. 3 personas) tiene **1 min** para presentar: nombre del asistente, caso de uso y demo rápida (30 seg). After‑round, el público vota con stickers el “Más prometedor”. |
| **Key takeaway** | El feedback rápido ayuda a focalizar el siguiente sprint de desarrollo. |
| **Slides** | 4 (instrucciones de pitch, tabla de votos). |

---

### **Bloque 5 – Cierre & Próximos Pasos (5 min)**
| Elemento | Detalle |
|----------|---------|
| **Objetivo** | Consolidar aprendizajes y motivar a seguir iterando. |
| **Dinámica** | 1️⃣ Recapitulación de 3 puntos en 1 min. <br>2️⃣ Entrega física/digital