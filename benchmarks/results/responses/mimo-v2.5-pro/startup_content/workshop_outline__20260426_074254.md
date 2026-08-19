# MiMo-V2.5 Pro — startup_content/workshop_outline

- model_id: `xiaomi/mimo-v2.5-pro`
- success: True  | final: 7.23 | quality: 9.24
- latency_total: 30.976s | tokens_per_second: 66.1
- input_tokens: 209 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# 🚀 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
## Workshop Práctico — 3 Horas Presencial

---

## 📋 INFORMACIÓN GENERAL

| Detalle | Especificación |
|---|---|
| **Duración total** | 3 horas (180 minutos) |
| **Audiencia** | 20-30 emprendedores early-stage, no-técnicos |
| **Formato** | Presencial, altamente participativo |
| **Ratio ideal** | 70% práctica / 30% teoría |
| **Tono** | Energético, directo, sin jerga técnica innecesaria |
| **Plataforma principal** | ChatGPT (versión gratuita o Plus) + Custom GPTs |
| **Plataforma alternativa** | Poe, Claude Projects, o Vapi para asistentes de voz |

---

## 🔧 MATERIALES NECESARIOS (Preparación Previa)

### Para el facilitador:
- [ ] Proyector/pantalla grande + sonido
- [ ] Laptop con ChatGPT Plus abierto y Custom GPTs funcionando
- [ ] 2-3 Custom GPTs de ejemplo ya creados (uno de atención al cliente, uno de ventas, uno de productividad interna)
- [ ] Presentación (Google Slides/Canva) — estimada: 35-40 slides
- [ ] Cronómetro visible para todos (proyectado o físico grande)
- [ ] Micrófono (si el espacio lo requiere)
- [ ] Música de fondo para ejercicios (playlist Spotify preparada)
- [ ] 2 asistentes/voluntarios para ayudar a resolver dudas técnicas durante el ejercicio

### Para cada participante:
- [ ] Laptop o tablet (confirmar con anticipación que todos traen dispositivo)
- [ ] Cuenta de ChatGPT creada ANTES del workshop (instrucciones enviadas por email 48h antes)
- [ ] Workbook impreso (8-10 páginas) con:
  - Plantilla "Canvas de tu Asistente IA" (1 página)
  - Guía de prompts para copiar/pegar (2 páginas)
  - Checklist de configuración de Custom GPT (1 página)
  - Espacio para notas y borradores (4 páginas)
  - Lista de recursos y links QR (1 página)
- [ ] Marcadores/Post-its en cada mesa (4 colores)
- [ ] Etiqueta con nombre + nombre de startup

### Logística del espacio:
- [ ] Mesas redondas de 5-6 personas (fomenta colaboración)
- [ ] WiFi de alta velocidad (CRÍTICO — verificar capacidad para 30+ dispositivos simultáneos)
- [ ] Enchufes/multicontactos accesibles
- [ ] Coffee break preparado (agua, café, snacks energéticos)
- [ ] Impresión de QR codes grandes con links a recursos

---

## 📅 AGENDA DETALLADA

---

### 🔥 BLOQUE 1: "DESPIERTA EL MONSTRUO"
**Apertura y Contexto Explosivo**

| | |
|---|---|
| **Duración** | 20 minutos (0:00 - 0:20) |
| **Objetivo** | Generar energía, crear comunidad, y que cada participante entienda POR QUÉ un asistente de IA puede ser el "empleado #1" de su startup |
| **Dinámica** | Ice-breaker interactivo + Demo en vivo impactante |
| **Slides estimados** | 5-6 |

**Desglose:**

**0:00 - 0:08 — Ice-Breaker: "El Pitch del Caos" (8 min)**
- Cada persona se presenta en 15 segundos: nombre, startup, y el problema más tedioso/repetitivo que tiene en su día a día
- El facilitador va anotando en un pizarrón o slide los problemas más comunes (atención al cliente, emails, investigación de mercado, etc.)
- *Objetivo oculto: mapear los use cases reales de la audiencia*

**0:08 - 0:15 — Demo en Vivo: "Tu Competencia Ya Lo Hace" (7 min)**
- El facilitador muestra EN VIVO un Custom GPT funcionando:
  - Ejemplo 1: Un asistente de atención al cliente que responde como si fuera la marca (usando un caso hipotético de startup local)
  - Ejemplo 2: Un asistente que investiga competidores en 30 segundos
  - Ejemplo 3: Un asistente que genera respuestas de ventas personalizadas
- Momento "wow" — hacer que el público interactúe con el asistente en tiempo real
- **Frase clave:** *"Este asistente trabaja 24/7, no se enferma, no llega tarde, y cuesta menos que un café al día."*

**0:15 - 0:20 — Contexto Rápido: "El Estado del Arte" (5 min)**
- Datos impactantes sobre adopción de IA en startups LATAM (2-3 datos duros)
- La diferencia entre usar ChatGPT "genérico" vs. tener un asistente ENTRENADO para TU negocio
- Qué vamos a construir hoy: un Custom GPT funcional que cada persona se lleva a casa

> **🎯 Key Takeaway:** *"Un asistente de IA personalizado no es un lujo de big tech — es el primer empleado que toda startup debería contratar. Y hoy vas a construir el tuyo."*

---

### 🧠 BLOQUE 2: "PIENSA ANTES DE CONSTRUIR"
**Estrategia y Diseño de tu Asistente**

| | |
|---|---|
| **Duración** | 25 minutos (0:20 - 0:45) |
| **Objetivo** | Que cada participante defina con claridad QUÉ hará su asistente, PARA QUIÉN, y CON QUÉ información operará |
| **Dinámica** | Mini-charla (10 min) + Ejercicio individual con plantilla (15 min) |
| **Slides estimados** | 8-10 |

**Desglose:**

**0:20 - 0:30 — Mini-Charla: "El Canvas de tu Asistente IA" (10 min)**
- Presentar la plantilla del **"AI Assistant Canvas"** (en el workbook):
  - **👤 Usuario:** ¿Quién va a hablar con tu asistente? (cliente, equipo, proveedor)
  - **🎯 Misión:** ¿Cuál es su trabajo principal en UNA frase?
  - **💬 Tono:** ¿Cómo habla? (formal, amigable, experto, divertido)
  - **📚 Conocimiento:** ¿Qué SABE tu asistente? (docs, FAQs, info de producto, precios)
  - **🚧 Límites:** ¿Qué NO debe hacer o decir?
  - **🔄 Flujos clave:** ¿Cuáles son las 3-5 preguntas/situaciones más comunes?
  - **✅ Éxito:** ¿Cómo sabes que está funcionando bien?
- Ejemplos de malos vs. buenos asistentes (casos reales de startups LATAM)
- **Error #1:** "Quiero que haga todo" → Error: un asistente que hace todo, no hace nada bien
- **Regla de oro:** "Un asistente, un trabajo, hecho PERFECTO"

**0:30 - 0:45 — Ejercicio: "Llena tu Canvas" (15 min)**
- Música de fondo activa
- Cada participante llena su plantilla individualmente
- Facilitadores circulan para ayudar y provocar mejoras
- Al final: 3 voluntarios comparten su canvas en 30 segundos cada uno
- Feedback rápido del facilitador ("Amplía esto...", "Aquí estás siendo demasiado genérico...")

> **🎯 Key Takeaway:** *"El 80% del éxito de tu asistente no está en la tecnología — está en la claridad con la que defines su trabajo. Hoy definiste ese trabajo."*

---

### 🛠️ BLOQUE 3: "MANOS A LA OBRA"
**Construcción del Custom GPT (Ejercicio Principal)**

|