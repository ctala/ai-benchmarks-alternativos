# Nemotron 3 Nano Omni 30B-A3B Reasoning — startup_content/workshop_outline

- model_id: `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 41.592s | tokens_per_second: 90.5
- input_tokens: 206 | output_tokens: 3764
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y extremadamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y una estructura de bloques bien pensada, aunque podría profundizar un poco más en algunos conceptos.

## Respuesta completa

## 🚀 Workshop “Construye tu Asistente de IA para tu Startup”  
**Duración total:** 3 horas (180 min)  
**Participantes:** 20‑30 emprendedores early‑stage, sin conocimientos técnicos profundos  

---

## 1️⃣ Agenda detallada (tiempos)

| Horario | Bloque | Duración |
|---------|--------|----------|
| 09:00‑09:10 | **Bienvenida + Ice‑breaker** | 10 min |
| 09:10‑09:20 | **¿Por qué un asistente de IA?** (Problem‑Fit) | 10 min |
| 09:20‑09:35 | **Conceptos básicos: qué es y qué no es** | 15 min |
| 09:35‑09:55 | **Plataforma low‑code elegida** (Demo rápida) | 20 min |
| 09:55‑10:15 | **Manos‑a‑la‑obra: crear la “caja” del asistente** | 20 min |
| 10:15‑10:35 | **Ejercicio principal – Diseña tu bot** (trabajo en parejas) | 20 min |
| 10:35‑10:50 | **Testing & ajustes en vivo** | 15 min |
| 10:50‑11:10 | **Show‑and‑Tell: cada equipo comparte su bot** | 20 min |
| 11:10‑11:25 | **Próximos pasos + recursos** | 15 min |
| 11:25‑11:30 | **Cierre + feedback rápido** | 5 min |
| **TOTAL** |  | **180 min** |

> **Tip:** Usa un cronómetro visible y anuncia “¡5 min para cambiar de fase!” para mantener la energía alta.

---

## 2️⃣ Materiales que debes preparar antes

| Ítem | Cantidad / Detalle |
|------|--------------------|
| **Laptops** | 1 por participante (con acceso a internet). Si no hay, reserva una sala con PC y usa “trae tu propio dispositivo” (BYO). |
| **Conexión a internet** | Wi‑Fi estable (mínimo 10 Mbps). |
| **Cuentas pre‑creadas** | - **OpenAI (ChatGPT) – cuenta gratuita** (para la API). <br>- **Dialogflow CX / Google Assistant** (cuenta demo). <br>- **Bubble / Softr** (prueba gratuita). <br>*(Entrega credenciales impresas o QR para que todos entren rápidamente).*
| **Cheat‑sheet “IA sin código”** | 1 hoja A4 por participante (resumen de pasos, palabras clave, links). |
| **Pegatinas / post‑its** | 2 colores (para ideas y “bloqueos”). |
| **Proyector + pantalla** | Para slides y demo en vivo. |
| **Rotuladores y papel** | Para lluvia de ideas y notas rápidas. |
| **Timer visible** |  o app de cuenta regresiva en el proyector. |
| **Botellas de agua y café** | (pequeño detalle para mantener la energía). |

---

## 3️⃣ Bloques del workshop (título, duración, objetivo, dinámica, key takeaway)

### Bloque 1 – **¡Bienvenidos y rompehielos!**  
- **Duración:** 10 min  
- **Objetivo:** Crear clima de confianza y que los participantes se presenten rápidamente.  
- **Dinámica:** “2‑Truths‑1‑Lie” con foco en sus startups (cada uno dice 2 cosas reales y 1 inventada sobre su negocio; los demás adivinan).  
- **Key takeaway:** “Todos estamos aquí para aprender y compartir, no para ser expertos”.

### Bloque 2 – **¿Por qué un asistente de IA?** (Problem‑Fit)  
- **Duración:** 10 min  
- **Objetivo:** Conectar la necesidad real de su startup con la solución IA (ej. atención al cliente, lead‑qualification, soporte interno).  
- **Dinámica:** Mini‑brainstorm en grupos de 4: “¿Cuál es el mayor dolor que tu cliente vive hoy?” → Cada grupo escribe 1‑2 ideas en post‑its.  
- **Key takeaway:** “El asistente de IA es una herramienta para **automatizar** esas tareas que consumen tiempo y mejoran la experiencia del cliente”.

### Bloque 3 – **Conceptos básicos: Qué es y Qué no es**  
- **Duración:** 15 min  
- **Objetivo:** Desmitificar la IA (no es magia, es un modelo entrenado que responde a preguntas).  
- **Dinámica:** Charla relámpago con 5 diapositivas + 2 ejemplos reales (p.ej., bot de FAQ para una tienda de moda).  
- **Key takeaway:** “Un asistente de IA es **un flujo de conversación** guiado por IA, no un robot con conciencia”.

### Bloque 4 – **Plataforma low‑code elegida** (Demo rápida)  
- **Duración:** 20 min  
- **Objetivo:** Mostrar, paso a paso, cómo crear un asistente sin escribir código.  
- **Dinámica:** **Demo en vivo** (10 min) + **Preguntas rápidas** (5 min) + **Mini‑practica** (5 min) donde cada participante crea una “intención” mínima (ej. “hola”).  
- **Key takeaway:** “Con **Dialogflow** (o Bubble + OpenAI) puedes lanzar un bot en menos de 30 min”.

### Bloque 5 – **Manos‑a‑la‑obra: crear la “caja” del asistente**  
- **Duración:** 20 min  
- **Objetivo:** Tener una estructura básica (intenciones, respuestas, fallback).  
- **Dinámica:** Guía paso a paso en la pantalla (compartir pantalla). Cada participante:  
  1. Crea una cuenta (si no la tiene).  
  2. Define 2 intenciones (p.ej., “saludo” y “consulta de producto”).  
  3. Añade 2‑3 ejemplos de entrenamiento.  
- **Key takeaway:** “La **estructura** (intenciones + entrenamiento) es la base; el resto lo hace la IA”.

### Bloque 6 – **Ejercicio principal – Diseña tu bot** (trabajo en parejas)  
- **Duración:** 20 min  
- **Objetivo:** Cada pareja (2‑3 personas) define el **caso de uso** de su asistente (p.ej., “FAQ del producto”, “Captura de leads”, “Soporte post‑venta”).  
- **Dinámica:**  
  1. 5 min: Brainstorm en papel – identificar preguntas frecuentes y flujos.  
  2. 10 min: Configurar el bot en la plataforma (usar la cuenta pre‑creada).  
  3. 5 min: Probar y ajustar (añadir ejemplos, cambiar respuestas).  
- **Key takeaway:** “Un buen asistente se construye **iterando** con preguntas reales de tus clientes”.

### Bloque 7 – **Testing & ajustes en vivo**  
- **Duración:** 15 min  
- **Objetivo:** Mostrar cómo validar la conversación (prueba de usuario, métricas simples).  
- **Dinámica:** Cada pareja hace **2 pruebas**:  
  - Simular cliente (el otro compañero) → observar respuestas.  
  - Recoger “puntos de fricción” y mejorar en 2‑3 minutos.  
- **Key takeaway:** “Iterar rápido → **feedback real** = bot más útil”.

### Bloque 8 – **Show‑and‑Tell: cada equipo comparte su bot**  
- **Duración:** 20 min (≈ 3‑4 min por equipo)  
- **Objetivo:** Celebrar logros, aprender de otros casos y generar ideas de mejora.  
- **Dinámica:** Cada pareja muestra su bot (30 seg) y responde una pregunta rápida del facilitador.  
- **Key takeaway:** “Los **casos de uso reales** son la mejor validación**; compartir acelera el aprendizaje colectivo.

### Bloque 9 – **Próximos pasos + recursos**  
- **Duración:** 15 min  
- **Objetivo:** Dar a los emprendedores un plan de acción concreto para seguir mejorando su asistente después del workshop.  
- **Dinámica:** Lista de 5 pasos (definir KPI, integrar con CRM, entrenar con datos reales, escalar a voz, medir satisfacción).  
- **Key takeaway:** “Tu bot **no es un proyecto único**, es un activo que evoluciona con tu negocio”.

### Bloque 10 – **Cierre + feedback rápido**  
- **Duración:** 5 min  
- **Objetivo:** Recoger impresiones y motivar la continuidad.  
- **Dinámica:** Mini‑encuesta con 2‑3 preguntas (p.ej., “¿Qué fue lo más útil?”, “¿Qué te falta?”).  
- **Key takeaway:** “La energía del grupo y la práctica son la clave; ¡tú puedes construir IA sin ser programador!”

---

## 4️⃣ Ejercicio principal (todos pueden hacerlo)

**Título:** *“Construye tu Asistente de FAQ en 20 min”*  

1. **Formar parejas** (o tríos).  
2. **Seleccionar 3‑5 preguntas frecuentes** que su startup recibe (p.ej., “¿Cuál es el precio?”, “¿Cómo me contacto?”).  
3. **Crear intenciones** en la plataforma (Dialogflow, Bubble + OpenAI, etc.).  
4. **Añadir 2‑3 ejemplos de entrenamiento** por intención.  
5. **Configurar una respuesta** (texto breve + botón de “más info” opcional).  
6. **Probar** con el compañero (simular cliente).  
7. **Ajustar** una respuesta basada en la prueba.  

**Resultado esperado:** Un bot funcional que responde a al menos una de sus preguntas clave, con la capacidad de escalar a un humano (fallback) si lo desean.

---

## 5️⃣ Recursos para llevar a casa

| Tipo | Descripción |
|------|-------------|
| **Cheat‑sheet “IA sin código”** (PDF 2 páginas) | Paso a paso, glosario de términos, enlaces a los planes gratuitos de Dialogflow, OpenAI, Bubble. |
| **Guía “5 pasos para lanzar tu bot en producción”** | Checklist con KPIs (tasa de resolución, tiempo de respuesta), integración con CRM (HubSpot, Zoho), seguridad y cumplimiento. |
| **Plantilla de caso de uso** (Google Sheet) | Columnas: *Pregunta*, *Intención*, *Ejemplos de entrenamiento*, *Respuesta*, *Código de fallback*, *Métricas*. |
| **Lista de herramientas low‑code** | - Dialogflow CX (Google) <br>- Microsoft Bot Framework (Power Virtual Agents) <br>- Bubble.io + OpenAI API <br>- Landbot.io <br>- ManyChat (para WhatsApp) |
| **Enlace a la comunidad** | Grupo privado de WhatsApp/Telegram “IA para Startups LATAM” (acceso al facilitador y a otros emprendedores). |
| **Video resumen (5 min)** | Grabación del demo de la plataforma con subtítulos en español. |

---

## 6️⃣ Slide count estimado (por sección)

| Sección | Nº de slides (aprox.) |
|---------|-----------------------|
| Bienvenida + Ice‑breaker | 2 |
| Problem‑Fit (¿Por qué IA?) | 3 |
| Conceptos básicos | 4 |
| Demo de plataforma low‑code | 6 |
| Guía paso a paso (caja) | 5 |
| Ejercicio principal (instrucciones) | 3 |
| Testing & ajustes | 2 |
| Show‑and‑Tell (ejemplos) | 4 |
| Próximos pasos + recursos | 4 |
| Cierre & feedback | 2 |
| **TOTAL** | **34** |

> **Tip de presentación:** Usa **máximo 1 idea por slide**, imágenes de teléfonos/mockups y colores vivos (naranja, verde, azul) para mantener la energía alta.  

---

## 🎉 Resumen rápido para el facilitador

- **Energía:** Usa dinamismo, preguntas directas y tiempo de “pizarra viva”.  
- **Práctica:** Cada bloque tiene una parte “hands‑on”. No dejes que alguien solo escuche.  
- **Tiempo:** Controla con el cronómetro; avisa 5 min antes de cambiar de fase.  
- **Resultado:** Al final, cada participante (o pareja) tendrá un **bot funcional** que puede seguir mejorando y mostrar a su equipo o inversores.  

¡Listo! Con este outline tendrás un workshop dinámico, 100 % práctico y perfectamente ajustado a emprendedores que no son técnicos pero sí muy motivados. ¡Éxitos y a construir IA! 🚀