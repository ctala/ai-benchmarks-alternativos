# DeepSeek V4 Flash (NIM) — startup_content/workshop_outline

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 7.13 | quality: 9.24
- latency_total: 64.254s | tokens_per_second: 31.9
- input_tokens: 198 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

Claro, aquí tienes el outline completo para un workshop de 3 horas, diseñado específicamente para emprendedores no técnicos en Latinoamérica. El enfoque es 100% práctico, con un tono enérgico y sin jerga técnica innecesaria.

---

## Título: Construye tu Asistente de IA para tu Startup - Workshop Práctico

**Duración:** 3 horas (180 minutos)
**Audiencia:** 20-30 emprendedores early-stage (sin conocimientos técnicos)
**Formato:** Presencial, con mesas de trabajo en grupos de 4-5 personas.

---

### 1. Agenda Detallada con Tiempos

| Hora (ejemplo) | Bloque | Duración |
|---|---|---|
| 9:00 - 9:15 | **Bienvenida y "Rompehielos IA"** | 15 min |
| 9:15 - 9:45 | **Módulo 1: ¿Qué es un Asistente de IA? (Sin Magia)** | 30 min |
| 9:45 - 10:30 | **Módulo 2: El Corazón del Asistente (Datos + Prompt)** | 45 min |
| 10:30 - 10:45 | **Coffee Break + Networking Relámpago** | 15 min |
| 10:45 - 11:45 | **Módulo 3: Manos a la Obra - Construye tu Asistente** | 60 min |
| 11:45 - 12:15 | **Módulo 4: Demo, Feedback y Próximos Pasos** | 30 min |
| 12:15 - 12:30 | **Cierre, Recursos y Foto Grupal** | 15 min |

---

### 2. Materiales Necesarios (Preparación antes del workshop)

**Para el facilitador:**
- Proyector y laptop con conexión a internet (estable, de respaldo).
- Presentación (slides) con el slide count indicado abajo.
- Micrófono inalámbrico (opcional, pero recomendado para energía).
- Post-its grandes (3 colores: verde, amarillo, rosa) y marcadores gruesos.
- Una pizarra blanca o rotafolio con marcadores.
- **Conexión Wi-Fi:** Clave visible en cada mesa.
- **Lista de reproducción Spotify:** Música instrumental upbeat para los ejercicios.

**Para cada participante (imprimir y tener listo):**
- **1 hoja "Canvas del Asistente"** (diseñada por ti: columnas: Problema, Tarea, Prompt Base, Fuente de Datos).
- **1 hoja "Cheatsheet de Prompts"** (con 5-10 ejemplos de prompts para atención al cliente, ventas, soporte técnico, etc.).
- **Lapicero** (uno por persona).

**Setup del salón:**
- Mesas redondas o en islas (5-6 mesas, 4-5 personas por mesa).
- En cada mesa: 1 laptop (puede ser la del participante) o 1 tablet con acceso a **ChatGPT (gratuito) o Poe.com** (más fácil para no técnicos).
- **Alternativa offline (si no hay internet estable):** Tener instalado localmente un modelo pequeño como **Ollama + Llama 3.2** en 3 laptops de respaldo.

---

### 3. Desglose por Bloques

#### **Bloque 0: Bienvenida y "Rompehielos IA" (15 min)**

- **Título:** "¿Tu startup ya tiene un asistente? (Si no, hoy lo creamos)"
- **Objetivo:** Romper el hielo, conectar con la audiencia y validar que nadie es técnico (y que eso está bien).
- **Dinámica:**
    - Facilitador se presenta (30 segundos, enérgico).
    - **Ejercicio rápido:** "Levanten la mano si alguna vez le pidieron a ChatGPT que les escriba un email. Ahora, levanten la mano si alguna vez le pidieron que haga algo *específico* para su negocio (ej: responder preguntas frecuentes de clientes)."
    - **Discusión en parejas (1 min):** "¿Cuál fue la última tarea aburrida que hiciste en tu startup que odias hacer?" (esto genera el "dolor" que resolveremos).
- **Key takeaway:** "Hoy no vas a programar. Hoy vas a *diseñar* un asistente que trabaje para ti mientras tú duermes. La IA no es magia, es lógica + datos + un buen prompt."

#### **Bloque 1: Módulo 1 - ¿Qué es un Asistente de IA? (Sin Magia) (30 min)**

- **Título:** "De la Idea al Prompt: El Mapa del Tesoro"
- **Objetivo:** Desmitificar la IA y definir qué es un asistente (vs. un chatbot genérico).
- **Dinámica:**
    - **Charla (15 min):** Explicación visual (slides) de:
        - Chatbot vs. Asistente (el asistente tiene contexto, personalidad y una tarea específica).
        - El "Triángulo Mágico": **Prompt + Datos (contexto) + Personalidad = Asistente**.
        - Ejemplos reales de asistentes para startups (atención al cliente, generación de leads, onboarding).
    - **Demo rápida (5 min):** El facilitador muestra un asistente ya construido (ej: un bot de ventas para una tienda de café) en vivo. Pregunta: "¿Qué problema resuelve?"
    - **Mini-ejercicio (10 min):** En grupos de mesa, cada equipo escribe en un post-it **amarillo** una tarea repetitiva de su startup que quieran delegar. Pegan en la pizarra.
- **Key takeaway:** "Un asistente de IA no es un genio. Es un empleado que solo sabe hacer una cosa, pero la hace increíblemente bien, 24/7, sin quejarse."

#### **Bloque 2: Módulo 2 - El Corazón del Asistente (Datos + Prompt) (45 min)**

- **Título:** "El Prompt es tu Nuevo Lenguaje de Programación"
- **Objetivo:** Enseñar a estructurar un prompt efectivo y entender qué datos necesita el asistente.
- **Dinámica:**
    - **Charla interactiva (15 min):**
        - La fórmula del prompt perfecto: **Rol + Contexto + Tarea + Formato + Ejemplo**.
        - Diferencia entre "Dame ideas" y "Actúa como experto en marketing para startups. Basado en estas 3 características de mi producto (X, Y, Z), genera 5 titulares para Instagram. Formato: lista con emojis."
    - **Ejercicio guiado (20 min):**
        - Cada grupo recibe un escenario (ej: "Eres un asistente de soporte para una app de delivery. Responde a un cliente que dice que su pedido llegó frío.").
        - Usando el **Canvas del Asistente**, escriben el Rol, Contexto, Tarea y Formato.
        - Luego, escriben el prompt completo en un documento compartido (o en papel).
    - **Discusión grupal (10 min):** 3 grupos comparten su prompt. El facilitador lo prueba en vivo en ChatGPT y da feedback.
- **Key takeaway:** "Sin un buen prompt, tu asistente será un vago. Con un prompt bien escrito, será tu mejor empleado. La calidad del input define la calidad del output."

#### **Bloque 3: Coffee Break + Networking Relámpago (15 min)**

- **Dinámica:** Música, café, y una consigna: "Encuentra a alguien de otra mesa y cuéntale en 30 segundos qué asistente estás construyendo. Luego él te cuenta el suyo."
- **Objetivo:** Energizar, conectar y compartir ideas.

#### **Bloque 4: Módulo 3 - Manos a la Obra: Construye tu Asistente (60 min)**

- **Título:** "De la Teoría a la Acción: Tu Primer Asistente en Vivo"
- **Objetivo:** Que cada participante (en su grupo o individual) construya un prototipo funcional de su asistente usando una herramienta sin código.
- **Dinámica (Ejercicio Principal del Workshop):**
    - **Fase 1 (10 min):** Definir el alcance. Cada grupo elige UNA tarea específica de su startup (la del post-it amarillo).
    - **Fase 2 (30 min):** Construcción.
        - Usando **ChatGPT (versión gratuita) o Poe.com**, cada grupo crea un "Custom GPT" o un "Bot" con instrucciones personalizadas.
        - **Instru