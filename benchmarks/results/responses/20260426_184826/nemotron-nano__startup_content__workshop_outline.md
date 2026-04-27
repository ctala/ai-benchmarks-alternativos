# Nemotron 3 Nano 30B — startup_content/workshop_outline

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.9 | quality: 9.44
- latency_total: 33.46s | tokens_per_second: 95.5
- input_tokens: 206 | output_tokens: 3197
- judge_score: 4.6 | justificación: 

## Respuesta completa

## 📚 Outline completo – “Construye tu Asistente de IA para tu Startup – Workshop Práctico”  
**Duración total:** 3 horas (180 min)  
**Público:** Emprendedores *early‑stage* (no‑tech) – 20 – 30 personas  
**Formato:** Presencial, con laptops y acceso a internet

---

### 1️⃣ Agenda detallada (tiempos)

| Tiempo | Bloque | Título | Tipo de actividad |
|--------|--------|--------|-------------------|
| 0:00 – 0:10 | 10 min | **Bienvenida & Calentamiento** | Dinámica rápida de “nombre + problema” |
| 0:10 – 0:30 | 20 min | **Qué es un Asistente de IA y por qué le importa a tu startup** | Charla + Mini‑demo |
| 0:30 – 1:00 | 30 min | **Mapa de casos de uso para startups** | Trabajo en parejas + lluvia de ideas |
| 1:00 – 1:30 | 30 min | **Elección de la plataforma “sin código”** | Charla rápida + comparativa visual |
| 1:30 – 2:30 | 60 min | **Construcción guiada del asistente** | **Ejercicio práctico** (configuración + entrenamiento) |
| 2:30 – 2:50 | 20 min | **Demo de los asistentes creados + Feedback grupal** | Presentaciones relámpago (2 min cada una) |
| 2:50 – 3:00 | 10 min | **Cierre, próximos pasos y entrega de recursos** | Resumen + preguntas rápidas |

> **Total:** 180 min (3 horas)

---

### 2️⃣ Materiales necesarios (para el facilitador y los participantes)

| Material | ¿Quién lo lleva? | Comentario |
|----------|------------------|------------|
| **Laptop con Wi‑Fi** (una por participante) | Cada asistente | Pre‑instalar navegador y acceso a internet |
| **Proyector / TV** | Facilitador | Para mostrar slides y demos |
| **Papel + post‑its** | Facilitador + asistentes | Para brainstorming y sticky‑note voting |
| **Plantilla “Caso de Uso + Prompt”** (imprimida o Google Doc) | Facilitador | Entrega al inicio del ejercicio |
| **Cuentas pre‑creadas** en plataformas elegidas (p.ej., **Botpress**, **Landbot**, **OpenAI Playground**, **Zapier**) | Facilitador | Credenciales compartidas en pantalla |
| **Guía rápida de “Prompt Engineering para no‑tech”** | Facilitador | Impresa y/o PDF para descargar |
| **Lista de recursos** (links, videos, plantillas) | Facilitador | Para repartir al final |
| **Botella de agua / café** | Facilitador | ¡Mantener la energía! |

> **Preparación del facilitador (1‑2 días antes):**  
> 1. Crear cuentas demo y generar tokens de API (solo lectura).  
> 2. Subir a un repositorio (Google Drive o GitHub) las plantillas y guías.  
> 3. Diseñar 30‑35 slides que cubran los puntos de la agenda.  
> 4. Testear el flujo de trabajo “crear asistente → probar → exportar”.  

---

### 3️⃣ Detalle de cada bloque  

#### **Bloque 1 – Bienvenida & Calentamiento** – **10 min**  
- **Objetivo:** Romper el hielo y que cada participante identifique su principal “dolor” que quiere aliviar con IA.  
- **Dinámica:** Cada persona dice su nombre, su startup y **“Mi mayor frustración es…”** (máx. 30 seg). El facilitador anota en una pizarra los temas más repetidos.  
- **Key takeaway:** *Un asistente de IA nace de un problema concreto que queremos resolver.*

#### **Bloque 2 – Qué es un Asistente de IA y su valor** – **20 min**  
- **Objetivo:** Dar una visión clara y sin tecnicismos de cómo funciona un asistente de IA.  
- **Dinámica:**  
  1. **Charla de 5 min** con ejemplos de startups latinas que usan bots (atención al cliente, onboarding, ventas).  
  2. **Mini‑demo de 5 min** (p.ej., un bot que responde preguntas frecuentes en español).  
  3. **Preguntas relámpago** (2‑3 preguntas del público).  
- **Key takeaway:** *Un asistente de IA es simplemente un “robot conversacional” que responde automáticamente a lo que le preguntan.*

#### **Bloque 3 – Mapa de casos de uso** – **30 min**  
- **Objetivo:** Que los emprendedores identifiquen al menos **2‑3 casos de uso viables** dentro de su startup.  
- **Dinámica:**  
  1. En parejas, completan la **Plantilla “Caso de Uso + Prompt”** (problema, audiencia, objetivo, mensaje clave).  
  2. Cada pareja comparte su caso en 1 min (ronda rápida).  
  3. Votación con post‑its: los casos más populares pasan a la siguiente fase.  
- **Key takeaway:** *Elige un caso claro, medible y fácil de automatizar.*

#### **Bloque 4 – Plataformas “sin código”** – **30 min**  
- **Objetivo:** Mostrar 3‑4 opciones de herramientas que permiten crear asistentes sin escribir código.  
- **Dinámica:**  
  1. **Charla visual de 10 min** con una tabla comparativa (precio, facilidad, idioma, integraciones).  
  2. **Demo live** (p.ej., crear un bot en Botpress en 3 min).  
  3. **Ronda de preguntas** y votación de la herramienta que prefieren usar.  
- **Key takeaway:** *Hay herramientas que permiten lanzar tu asistente en menos de 30 min, sin tocar código.*

#### **Bloque 5 – Construcción guiada del asistente** – **60 min** (el corazón del workshop)  
- **Objetivo:** Cada participante (o grupo de 2‑3) crea su propio asistente paso a paso.  
- **Dinámica:**  
  1. **Instrucciones rápidas** (5 min) – cómo abrir la plataforma elegida, dónde pegar el prompt.  
  2. **Tiempo de hands‑on** (40 min) – los asistentes siguen una **Guía paso a paso** que incluye:  
     - Definir el nombre y tono.  
     - Insertar el prompt principal.  
     - Configurar respuestas de fallback.  
     - Conectar a un canal sencillo (p.ej., WhatsApp sandbox, página web).  
  3. **Testing en vivo** (10 min) – el facilitador hace preguntas de prueba y los participantes verifican respuestas.  
- **Key takeaway:** *Con una buena configuración, tu asistente puede entender y responder en español sin que tú sepas programar.*

#### **Bloque 6 – Demo y feedback grupal** – **20 min**  
- **Objetivo:** Mostrar los resultados y recoger mejoras en tiempo real.  
- **Dinámica:** Cada grupo tiene **2 min** para presentar su asistente (nombre, caso de uso, demo). El resto brinda **2‑3 sugerencias** rápidas.  
- **Key takeaway:** *La retroalimentación rápida ayuda a pulir el mensaje y a descubrir oportunidades de mejora.*

#### **Bloque 7 – Cierre y próximos pasos** – **10 min**  
- **Objetivo:** Consolidar lo aprendido y motivar a continuar la implementación.  
- **Dinámica:**  
  1. Recapitulación de los **3 aprendizajes críticos** (identificar problema, elegir herramienta, entrenar con prompts).  
  2. Anuncio de **“Desafío 7‑días”**: crear una versión mejorada y compartir en el grupo de Slack/WhatsApp del workshop.  
  3. Entrega de **certificados de participación** (opcional).  
- **Key takeaway:** *El verdadero poder está en iterar y escalar el asistente después del workshop.*

---

### 4️⃣ Ejercicio principal – “Construye tu Asistente en 45 min”  

1. **Selección del caso** (10 min) – Cada grupo elige uno de los casos votados.  
2. **Definición del prompt** (10 min) – Redactan un prompt de 2‑3 frases que guíe al asistente (ej.: “Eres el asistente de soporte de *EcoShop*; responde siempre en español, sé amable y ofrece la política de devolución”).  
3. **Configuración en la plataforma** (20 min) –  
   - Crear el proyecto.  
   - Pegar el prompt.  
   - Configurar al menos **3 respuestas** (saludo, respuesta a pregunta frecuente, fallback).  
4. **Prueba rápida** (5 min) – Simulan una conversación (texto en pantalla).  
5. **Iteración relámpago** (5 min) – Ajustan el prompt basado en lo que vieron.  

> **Resultado esperado:** Un bot funcional que responde a 2‑3 preguntas clave de su startup y que pueden seguir mejorando en casa.

---

### 5️⃣ Recursos para llevar a casa  

| Tipo | Contenido | Formato |
|------|-----------|---------|
| **Cheat Sheet “Prompt Engineering para no‑tech”** | 10 ejemplos de prompts listos para copiar | PDF (1 página) |
| **Plantilla “Caso de Uso + Prompt”** | Formato editable para rellenar | Google Doc / PDF |
| **Lista de herramientas “sin código”** | Tabla con links, precios, nivel de soporte | PDF + URL |
| **Video tutorial de 5 min** | “Cómo lanzar tu asistente en Botpress en 5 minutos” | Enlace a YouTube (subido previamente) |
| **Plantilla de roadmap de 30‑días** | Pasos semanales para escalar y medir impacto | PDF |
| **Acceso a la comunidad de emprendedores IA** | Grupo Slack/WhatsApp para follow‑up | Enlace + QR code |
| **Certificado de participación** | Impreso o PDF con nombre y logo del workshop | PDF |

---

### 6️⃣ Estimado de slides por sección  

| Sección | Slides estimados |
|---------|-----------------|
| Bienvenida & Calentamiento | 2 |
| Qué es un Asistente de IA | 6 |
| Mapa de casos de uso | 4 |
| Plataformas “sin código” | 5 |
| Guía paso‑a‑paso (ejercicio) | 12 |
| Demo y feedback | 4 |
| Cierre & próximos pasos | 3 |
| **Total** | **≈ 31‑35 slides** |

*(Cada slide está pensado para ser visual, con iconos y pocos textos; el facilitador complementa con narración.)*

---

## 🎤 Tono del facilitador  
- **Energía:** Usa frases como “¡Vamos a darle vida a tu idea!” y “¡Esto es más fácil de lo que crees!”.  
- **Práctico:** Enfócate en *qué hacer* y *cómo hacerlo* en pocos minutos.  
- **Interactivo:** Pregunta constante, anima a levantar la mano, usa humor ligero (ej.: “Si el bot no entiende, ¡le damos una segunda oportunidad… como a los humanos!”).  
- **Inclusivo:** Refuerza que no se necesita ser programador; todos pueden crear algo útil.

---

### ¡Listo!  
Con este outline tendrás todo lo necesario para montar un workshop dinámico, práctico y memorable que permita a los emprendedores latinoamericanos lanzar su propio asistente de IA en tan solo 3 horas. ¡Éxitos! 🚀