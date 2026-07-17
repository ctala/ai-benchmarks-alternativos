# Qwen3-Coder-Next (OpenRouter FP8) — startup_content/workshop_outline

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 8.44 | quality: 9.52
- latency_total: 37.339s | tokens_per_second: 54.8
- input_tokens: 211 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

¡Claro! Aquí tienes un **outline completo, práctico y energético** para un workshop presencial de **3 horas** titulado:

---

## 🚀 **"Construye tu Asistente de IA para tu Startup – Workshop Práctico"**  
*Para emprendedores early-stage no técnicos (20–30 personas)*

> 🎯 **Enfoque**: *Aprender haciendo*. Sin código, sin jerga técnica innecesaria. Todo con lógica empresarial + herramientas accesibles.

---

### 📋 **1. Agenda Detallada (3 horas totales)**

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00–0:15 | 🌟 Bienvenida & Mindset IA | 15 min |
| 0:15–0:35 | 🤖 IA no es magia: entiende lo que sí puedes hacer HOY | 20 min |
| 0:35–0:55 | 🔍 Diseña tu asistente: de problema real a caso de uso viable | 20 min |
| 0:55–1:25 | 🛠️ Hands-on: Construye tu MVP de asistente en 30 min | 30 min *(ejercicio principal)* |
| 1:25–1:45 | 🧪 Demostraciones & Feedback en equipo | 20 min |
| 1:45–2:15 | 📈 Escalando: cómo integrar tu asistente en tu startup | 30 min |
| 2:15–2:45 | 🛠️ Herramientas & stack real: qué usar, cómo empezar | 30 min |
| 2:45–3:00 | 🎁 Cierre: Tu plan de acción + recursos para llevar | 15 min |

---

### 🧰 **2. Materiales Necesarios (que preparar antes)**

| Tipo | Detalle |
|------|---------|
| **Para facilitador** | - 1 laptop con proyector + internet estable<br>- Cuenta en **Make (Integromat)** o **Zapier** (demo)<br>- Cuenta en **Google Vertex AI Studio** (o **Dify.ai**, alternativa low-code)<br>- 1 docente de ejemplo (PDF con 3 ejemplos de prompts y salidas)<br>- 1 plantilla de *“Job-to-be-Done”* para asistente (PDF editable) |
| **Para participantes** | - Laptop o tablet (¡¡sí es posible desde celular!!)<br>- Cuenta Google (para usar Vertex AI Studio o ChatGPT Plus)<br>- Impresión opcional: *Plantilla de Diseño de Asistente* (1 pág.)<br>- Acceso a internet (Wi-Fi del espacio garantizado) |
| ** Extras** | - Post-its de colores, marcadores, hojas A4<br>- Snacks y café 🫐☕ |

---

### 📚 **3. Bloques Detallados**

---

#### **Bloque 1: Bienvenida & Mindset IA**  
**Duración**: 15 min  
**Objetivo**: Romper el miedo a la IA, crear confianza y alinear expectativas.  
**Dinámica**:  
- Bienvenida rápida con energía (1 min)  
- *Icebreaker*: “¿Qué tarea de tu startup te gustaría que lo hiciera una IA?” (3 min, escritura rápida en post-its)  
- Charla corta: “IA no es el futuro, es el *ahora* para startups no técnicas” (11 min)  
**Key takeaway**:  
> ✅ *La IA no reemplaza emprendedores: potencia a los que saben preguntar bien.*  
**Slides**: 4  

---

#### **Bloque 2: IA no es magia: entiende lo que sí puedes hacer HOY**  
**Duración**: 20 min  
**Objetivo**: Clarificar capacidades reales vs. hype. Enfocarse en *tasks*, no en modelos.  
**Dinámica**:  
- Demo en vivo: “Hagamos un asistente que responda preguntas de clientes *ahora mismo*” (10 min)  
  - Uso de **Google Vertex AI Studio (free)** o **Dify.ai** (sin login)  
  - Prompt simple → respuesta útil  
- Discusión guiada: “¿Qué tareas repetitivas de tu startup podrían ser automatizadas con IA?” (10 min, en parejas)  
**Key takeaway**:  
> ✅ *IA = potencia para tareas específicas: responder, resumir, generar ideas, clasificar.*  
**Slides**: 5  

---

#### **Bloque 3: Diseña tu asistente: de problema real a caso de uso viable**  
**Duración**: 20 min  
**Objetivo**: Traducir necesidades del negocio a casos de uso concretos, medibles y rápidos.  
**Dinámica**:  
- Ejercicio en grupos de 3–4: *“Job-to-be-Done”* con plantilla (15 min)  
  - Ejemplo: “Mi cliente me pregunta *‘¿Tiene descuentos para estudiantes?’* y yo pierdo tiempo respondiendo lo mismo”  
- Compartimos 2–3 ejemplos en plenaria (5 min)  
**Key takeaway**:  
> ✅ *Un buen asistente de IA resuelve una tarea específica, repetitiva y valiosa para tus usuarios.*  
**Slides**: 4  

---

#### **🛠️ BLOQUE PRINCIPAL: Hands-on – Construye tu MVP de asistente en 30 min**  
**Duración**: 30 min  
**Objetivo**: Salir con un prototipo funcional y orgulloso.  
**Dinámica**:  
- Pasos guiados en pantalla:  
  1. Ir a [**Vertex AI Studio (free)**](https://cloud.google.com/vertex-ai) o [**Dify.ai**](https://dify.ai)  
  2. Elegir modelo básico (ej. *Gemini Flash* o *GPT-3.5*)  
  3. Escribir **prompt de sistema**:  
     > *“Eres el asistente de [nombre de tu startup]. Ayudas a clientes a entender [tu producto]. Tu tono es [amigable/profesional]. Si no sabes algo, dile: ‘Pregúntale a [tu nombre] directamente’.”*  
  4. Probar con 2 preguntas reales de tu negocio  
  5. Guardar y compartir link (si es posible)  
- Facilitador circula ayudando (¡y gritando “¡MVP listo!” cuando alguien termina 😄)  
**Key takeaway**:  
> ✅ *Puedes tener un asistente funcional en menos de 30 minutos — sin escribir una sola línea de código.*  
**Slides**: 3  

---

#### **Bloque 5: Demostraciones & Feedback en equipo**  
**Duración**: 20 min  
**Objetivo**: Reforzar aprendizaje, generar ideas y divertirse.  
**Dinámica**:  
- 4–5 equipos comparten su asistente (1 min cada uno: ¿qué resuelve? ¿cómo suena?)  
- Feedback positivo: “Me encantó cómo respondiste a ‘¿tiene garantía?’ con voz humana”  
- Preguntas abiertas: “¿Qué harías diferente si tuvieras 1 semana más?”  
**Key takeaway**:  
> ✅ *Un asistente no tiene que ser perfecto: tiene que ser útil.*  
**Slides**: 2  

---

#### **Bloque 6: Escalando: cómo integrar tu asistente en tu startup**  
**Duración**: 30 min  
**Objetivo**: Ver el camino de MVP a producto real.  
**Dinámica**:  
- Charla corta + casos reales:  
  - *Escenario 1*: Asistente en WhatsApp Business (usando **Twilio + IA**)  
  - *Escenario 2*: Chatbot en sitio web (usando **Typebot + Make**)  
  - *Escenario 3*: Asistente interno para tu equipo (usando **Notion AI + database**)  
- Ejercicio rápido: “Dibuja en 1 minuto cómo se vería tu asistente en tu flujo actual”  
**Key takeaway**:  
> ✅ *Tu asistente puede empezar en un chat y terminar en tu producto — paso a paso.*  
**Slides**: 6  

---

#### **Bloque 7: Herramientas & stack real: qué usar, cómo empezar**  
**Duración**: 30 min  
**Objetivo**: Llevar una lista concreta, actualizada y práctica.  
**Dinámica**:  
- *Tool Stack Race*: En equipos, ordenar herramientas por dificultad/costo (free → pro):  
  - **