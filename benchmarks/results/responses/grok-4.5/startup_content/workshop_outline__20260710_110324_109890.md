# Grok 4.5 — startup_content/workshop_outline

- model_id: `x-ai/grok-4.5`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 38.143s | tokens_per_second: 98.1
- input_tokens: 387 | output_tokens: 3741
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que se ajusta perfectamente a las necesidades de los emprendedores no técnicos, ofreciendo insights prácticos y útiles.

## Respuesta completa

# Outline Completo: Workshop Presencial
**"Construye tu Asistente de IA para tu Startup - Workshop Práctico"**  
**Duración total:** 3 horas (180 min)  
**Audiencia:** 20-30 emprendedores early-stage no-técnicos  
**Formato:** Presencial, hands-on, 70% práctica / 30% explicación  
**Tono:** Energético, directo, “manos a la obra”, sin jerga técnica innecesaria. Enfocado en resultados rápidos y herramientas 100% accesibles (gratis o freemium).

---

## 1. Agenda Detallada (3 horas)

| Tiempo       | Bloque                                      | Minutos |
|--------------|---------------------------------------------|---------|
| 0:00 – 0:15  | Bienvenida + Icebreaker                     | 15      |
| 0:15 – 0:35  | Por qué tu startup necesita un Asistente IA YA | 20   |
| 0:35 – 1:00  | Demo en vivo: Construyo un asistente en 20 min | 25   |
| 1:00 – 1:20  | Prompt Engineering para no-técnicos         | 20      |
| 1:20 – 1:30  | Break + networking rápido                    | 10      |
| 1:30 – 2:30  | **EJERCICIO PRINCIPAL:** Construye el tuyo  | 60      |
| 2:30 – 2:50  | Demo de participantes + Feedback rápido     | 20      |
| 2:50 – 3:00  | Recursos, next steps y cierre energético    | 10      |

---

## 2. Materiales necesarios (preparar antes)

**Para el facilitador:**
- Proyector + pantalla + HDMI
- Laptop con internet estable + cuenta ChatGPT Plus (o Claude Pro) lista
- Clicker / apuntador
- Timer visible (para ejercicios)
- Flipchart o pizarra + marcadores
- Stickers de colores + post-its
- Lista de asistencia + QR de feedback
- Plantilla de System Prompt (en Google Doc compartido)
- Ejemplos de asistentes reales (PDF/FAQ de startups latam)

**Para los participantes (avisar 48h antes):**
- Laptop o tablet (celular solo como backup)
- Cuenta gratuita de ChatGPT (chat.openai.com) o Claude.ai o Gemini
- Idealmente: ChatGPT Plus (no obligatorio)
- Idea clara de su startup (1 frase)
- 3-5 documentos o FAQs de su negocio (PDF, Google Doc o texto simple) – opcional pero muy recomendado
- Auriculares (por si hay ruido)

**Setup de sala:**
- Mesas en groups of 4-5 (fomenta peer learning)
- Buen WiFi (crítico)
- Café/agua/snacks
- Power strips

**Pre-work (enviar 2 días antes):**
1. Crear cuenta en ChatGPT
2. Escribir en 1 frase: “Mi startup hace X para Y”
3. Pensar: “¿Qué tarea me quita más tiempo o me da flojera?”

---

## 3. Detalle por Bloque

### Bloque 1: Bienvenida + Icebreaker  
**Duración:** 15 min  
**Objetivo:** Romper el hielo, crear energía y conectar el problema real de cada uno con la promesa del workshop.  
**Dinámica:** 
- 3 min intro rápida del facilitador + reglas de oro (“sin preguntas tontas”, “copia sin miedo”, “comparte lo que funciona”).
- Icebreaker “El Asistente de mi vida” (parejas de 2 min): “Si pudieras tener un empleado IA que trabaje 24/7, ¿qué le pedirías que haga mañana?” 
- Compartir en voz alta 4-5 respuestas potentes.  
**Key takeaway:** Hoy no vas a “aprender IA”. Vas a salir con un empleado digital trabajando para tu startup.

**Slides estimados:** 4

---

### Bloque 2: Por qué tu startup necesita un Asistente IA YA  
**Duración:** 20 min  
**Objetivo:** Vender el “por qué ahora” y mostrar casos reales de early-stage en LatAm.  
**Dinámica:** Charla interactiva + 2 mini-casos (5 min c/u).  
- Dolor real: “Estás solo, haces de todo, no duermes”.  
- Casos: 
  - Startup de foodtech que automatizó 70% de atención al cliente con un bot.
  - SaaS B2B que usa un “co-founder IA” para validar features y escribir outreach.  
- Pregunta al público: “Levanta la mano si hoy haces manualmente algo que un asistente podría hacer”.  
**Key takeaway:** No necesitas ser técnico ni tener presupuesto. Necesitas claridad de caso de uso + un buen prompt.

**Slides estimados:** 7

---

### Bloque 3: Demo en vivo – Construyo un asistente en 20 min  
**Duración:** 25 min  
**Objetivo:** Demostrar que es ridículamente simple y que cualquiera puede hacerlo.  
**Dinámica:** Demo en pantalla completa (screen share).  
Construyo en vivo un “Asistente de Atención al Cliente + Lead Qualifier” para una startup ficticia de educación online (o real de un participante).  
Pasos que muestro:
1. Definir el rol y personalidad
2. Subir knowledge (FAQs + pricing)
3. Dar instrucciones claras de comportamiento
4. Probar con 3 preguntas reales de clientes
5. Iterar en 60 segundos  
**Key takeaway:** Si yo lo hice en 20 minutos en vivo, tú lo vas a hacer mejor porque es TU negocio.

**Slides estimados:** 3 (el resto es pantalla del navegador)

---

### Bloque 4: Prompt Engineering para no-técnicos  
**Duración:** 20 min  
**Objetivo:** Darles el “manual de instrucciones” mínimo viable para que no fallen.  
**Dinámica:** Charla ultra-práctica + fill-in-the-blank en vivo.  
Framework simple que usamos:
**R.O.L.E.S.**  
- **R**ol (quién eres)  
- **O**bjetivo (qué quieres lograr)  
- **L**ímites (qué no puedes hacer)  
- **E**jemplos (few-shot)  
- **S**alida (formato de respuesta)  

Ejercicio rápido de 4 min: reescribir un prompt malo en 1 minuto.  
**Key takeaway:** El 80% del poder de tu asistente está en el System Prompt, no en la herramienta.

**Slides estimados:** 8

---

### Bloque 5: Break  
**Duración:** 10 min  
Café + “ve a hablar con 2 personas que no conoces y diles qué asistente vas a construir”.

---

### Bloque 6: EJERCICIO PRINCIPAL – Construye el tuyo  
**Duración:** 60 min  
**Objetivo:** Que cada participante salga con su primer Asistente de IA funcional y probado.  
**Dinámica:** Trabajo individual + apoyo de peers + facilitador circulando.  
(Ver detalle completo en sección 4)

**Key takeaway:** Tienes un MVP de asistente corriendo. No es teoría.

**Slides estimados:** 5 (checklist + timer en pantalla)

---

### Bloque 7: Demo de participantes + Feedback  
**Duración:** 20 min  
**Objetivo:** Celebrar, aprender de los demás y generar accountability.  
**Dinámica:** 4-5 voluntarios (2 min cada uno) muestran su asistente en vivo (pregunta real).  
Feedback rápido del grupo + facilitador (formato: 1 cosa que me gustó + 1 mejora).  
**Key takeaway:** Ver a otros hacerlo baja la fricción y genera ideas cruzadas.

**Slides estimados:** 2

---

### Bloque 8: Recursos, next steps y cierre  
**Duración:** 10 min  
**Objetivo:** Dejar un camino claro de 7 días y cerrar con energía alta.  
**Dinámica:** Charla rápida + QR de recursos + compromiso público.  
“En 7 días me escribes por WhatsApp o LinkedIn contándome cómo te fue con tu primer cliente real usando el asistente”.  
**Key takeaway:** El workshop termina hoy. Tu asistente empieza a trabajar mañana.

**Slides estimados:** 4

---

## 4. Ejercicio Principal del Workshop (60 min)  
**“Construye y prueba tu primer Asistente de IA en 60 minutos”**  
Todos pueden hacerlo (cero código, herramientas gratuitas).

**Herramientas recomendadas (en orden de preferencia):**
1. ChatGPT (Custom GPT si tienen Plus, o solo Custom Instructions + Project)
2. Claude.ai (Projects) – excelente y gratis
3. Gemini (Gems) o Poe.com (crear bot gratis)

**Paso a paso (facilitador proyecta el checklist):**

**Min 0-10 – Claridad de caso de uso**  
- Elige 1 solo caso de uso de esta lista (o inventa el tuyo):
  - Atención al cliente / FAQ
  -