# GPT-OSS 20B — startup_content/workshop_outline

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.03 | quality: 9.72
- latency_total: 18.944s | tokens_per_second: 135.3
- input_tokens: 250 | output_tokens: 2563
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

## 📅 3‑Horas Workshop Presencial  
**Título:** *Construye tu Asistente de IA para tu Startup – Workshop Práctico*  
**Audiencia:** Emprendedores early‑stage (20‑30 personas) – no requieren conocimientos técnicos.  
**Duración total:** 180 min

---

## 1️⃣ Agenda Detallada (con tiempos)

| Hora | Bloque | Duración | Slide Count |
|------|--------|----------|-------------|
| 0:00‑0:10 | **1. Bienvenida & Icebreaker** | 10 min | 3 |
| 0:10‑0:25 | **2. ¿Qué es un asistente de IA?** | 15 min | 5 |
| 0:25‑0:55 | **3. Identifica tu oportunidad de IA** | 30 min | 6 |
| 0:55‑1:15 | **4. Estrategia de Prompting** | 20 min | 5 |
| 1:15‑1:45 | **5. Demo sin‑código: ChatGPT + Zapier** | 30 min | 7 |
| 1:45‑2:15 | **6. Ejercicio Principal: Crea tu propio asistente** | 30 min | 8 |
| 2:15‑2:35 | **7. Integración & Escalado** | 20 min | 5 |
| 2:35‑2:50 | **8. Preguntas & Cierre** | 15 min | 3 |

> **Nota:** Los tiempos incluyen breves pausas de 2‑3 min entre bloques para que la energía se mantenga.

---

## 2️⃣ Materiales Necesarios (preparar antes)

| Item | ¿Qué? | ¿Dónde? | ¿Cómo usarlo? |
|------|-------|---------|--------------|
| **Computadoras portátiles** | 1‑1.5 personas | Sala | Acceso a internet y navegadores modernos. |
| **Cámara/Proyector** | Presentación y demos | Sala | Proyectar slides y demos en vivo. |
| **Conexión Wi‑Fi estable** | Todos | Sala | Necesario para llamadas API y herramientas online. |
| **Cuentas gratuitas en:**
  - ChatGPT (OpenAI) | Acceso a API | https://platform.openai.com/signup |
  - Zapier (plan gratuito) | Automatizaciones | https://zapier.com |
  - Landbot, Bubble, o cualquier herramienta no‑código | Crear chatbot | https://landbot.io, https://bubble.io |  
| **Credenciales de API (si aplica)** | API key de OpenAI | Al iniciar sesión en OpenAI. |
| **Plantillas de prompts** | Ejemplos pre‑escritos | Se entregarán en PDF. |
| **Hoja de trabajo “Mapa de IA”** | Cuadro de oportunidades y flujos | Se entregará en PDF. |
| **Lista de recursos** | Guía de lectura, tutoriales, foros | Se entregará al final. |

> **Tip:** Pide a los asistentes que traigan sus laptops con las cuentas creadas antes del workshop para que no pierdan tiempo.

---

## 3️⃣ Bloques (detallados)

### 1️⃣ Bienvenida & Icebreaker  
- **Objetivo:** Romper el hielo, energizar el grupo y establecer expectativas.  
- **Dinámica:** “Dos verdades y una IA” – cada participante comparte dos cosas que hace su startup y una idea de cómo la IA podría ayudar.  
- **Key Takeaway:** Todos ven que la IA es accesible y que cada negocio tiene un punto de entrada.  
- **Slides:** 3 (bienvenida, agenda, reglas de participación)

### 2️⃣ ¿Qué es un asistente de IA?  
- **Objetivo:** Definir asistente de IA y sus componentes clave sin tecnicismos.  
- **Dinámica:** Charla + mini‑quiz interactivo con Kahoot.  
- **Key Takeaway:** Entender la arquitectura simple: “Entrada → Modelo → Salida → Acción”.  
- **Slides:** 5 (definiciones, ejemplos cotidianos, beneficios, casos de éxito, resumen)

### 3️⃣ Identifica tu oportunidad de IA  
- **Objetivo:** Mapear en qué procesos de la startup la IA puede aportar valor.  
- **Dinámica:** Ejercicio de “Mapa de Oportunidades” en grupos de 3‑4.  
- **Key Takeaway:** Cada startup tendrá al menos 2 posibles escenarios de IA listos para prototipar.  
- **Slides:** 6 (ejemplo de mapa, plantilla, ejemplos de oportunidades, instrucciones)

### 4️⃣ Estrategia de Prompting  
- **Objetivo:** Aprender a dar instrucciones claras al modelo para obtener resultados útiles.  
- **Dinámica:** Demo rápida con prompts de “chat‑bot de ventas” y “chat‑bot de soporte”. Luego, los asistentes crean 3 prompts propios.  
- **Key Takeaway:** Un buen prompt = respuesta más precisa y útil.  
- **Slides:** 5 (estructura del prompt, ejemplos, tips de optimización)

### 5️⃣ Demo sin‑código: ChatGPT + Zapier  
- **Objetivo:** Ver en vivo cómo conectar ChatGPT a una acción concreta (p.ej. enviar un correo, crear un ticket).  
- **Dinámica:** Presentación paso‑a‑paso + live‑coding.  
- **Key Takeaway:** Se puede construir un asistente completo sin escribir código.  
- **Slides:** 7 (flujo de datos, screenshot de configuración, tiempo de respuesta, beneficios)

### 6️⃣ Ejercicio Principal: Crea tu propio asistente  
- **Objetivo:** Que cada participante diseñe y configure un asistente funcional para su startup.  
- **Dinámica:** 
  1. **Mapa de IA** (5 min) – define la tarea.  
  2. **Prompt** (5 min) – escribe el prompt.  
  3. **Zapier (o Landbot)** (10 min) – crea la automatización simple.  
  4. **Prueba** (5 min) – prueba con un usuario ficticio.  
- **Key Takeaway:** Al final tendrás un prototipo “funcional” que puedes probar en tu negocio.  
- **Slides:** 8 (pasos visuales, ejemplos, checklist)

### 7️⃣ Integración & Escalado  
- **Objetivo:** Mostrar cómo integrar el asistente con CRM, email, Slack o tu sitio web.  
- **Dinámica:** Charla + caso práctico de “Escalar un chatbot” en 2‑3 líneas de código (solo explicar).  
- **Key Takeaway:** La integración no es un obstáculo; existen plantillas y APIs listas.  
- **Slides:** 5 (mapa de integración, ejemplos de APIs, costos, planificación)

### 8️⃣ Preguntas & Cierre  
- **Objetivo:** Resolver dudas finales y motivar la acción.  
- **Dinámica:** Preguntas abiertas + “Compromiso de 30 días” – cada uno escribe una acción concreta a implementar.  
- **Key Takeaway:** La IA es una herramienta que se prueba, ajusta y escala.  
- **Slides:** 3 (resumen, próximos pasos, recursos)

---

## 4️⃣ Ejercicio Principal (Todos)

**“Crea tu Asistente IA en 30 min”**

1. **Define la tarea** (ej. “Responder preguntas frecuentes de clientes”) – 5 min.  
2. **Escribe un prompt** que guíe al modelo a dar respuestas útiles – 5 min.  
3. **Configura la automatización** en Zapier (ChatGPT → Gmail o Slack) – 10 min.  
4. **Prueba el asistente** con un escenario de uso real – 5 min.  
5. **Documenta** el flujo en un PDF que puedas compartir con tu equipo – 5 min.

> **Resultado:** Un asistente funcional con una integración básica que ya puede enviarse a un cliente o al sitio web.

---

## 5️⃣ Recursos para Llevar a Casa

| Tipo | Enlace | ¿Por qué lo necesitas? |
|------|--------|------------------------|
| **Plantilla de Prompt** | `prompt_template.pdf` | Guía paso‑a‑paso para crear prompts. |
| **Mapa de Oportunidades IA** | `opportunity_map.pdf` | Estructura para identificar casos de uso. |
| **Checklist de Integración** | `integration_checklist.pdf` | Paso a paso para conectar IA con otras herramientas. |
| **Tutoriales en video** | https://youtu.be/ChatGPTZapierDemo | Repasar la demo en casa. |
| **Lista de Herramientas No‑Código** | https://nomadlist.com/no-code-ia | Opciones gratuitas y de bajo costo. |
| **Community Discord** | https://discord.gg/ia-startups | Grupo de apoyo y preguntas. |
| **Blog de OpenAI** | https://openai.com/blog | Últimas actualizaciones y casos de uso. |

> **Tip:** Guarda estos recursos en una carpeta compartida (Google Drive / OneDrive) y envíalos por email al final del workshop.

---

## 6️⃣ Slide Count Estimado por Sección

| Sección | Slides |
|---------|--------|
| Bienvenida & Icebreaker | 3 |
| ¿Qué es un asistente de IA? | 5 |
| Identifica tu oportunidad de IA | 6 |
| Estrategia de Prompting | 5 |
| Demo sin‑código | 7 |
| Ejercicio Principal | 8 |
| Integración & Escalado | 5 |
| Preguntas & Cierre | 3 |
| **Total** | **42** |

> **Consejo:** Usa slides visuales y minimalistas. Cada slide debe contener solo 2‑3 ideas clave y una ilustración o icono.

---

## 🎉 ¡Listos para el Workshop!  

Con este esquema, tendrás una sesión dinámica, práctica y energizante que dejará a los emprendedores con un prototipo funcional y la motivación para seguir explorando la IA en sus startups. ¡Éxito en la sesión!