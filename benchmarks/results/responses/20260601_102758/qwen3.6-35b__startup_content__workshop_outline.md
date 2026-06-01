# Qwen 3.6 35B base (OpenRouter FP8) — startup_content/workshop_outline

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 7.67 | quality: 9.72
- latency_total: 29.519s | tokens_per_second: 144.1
- input_tokens: 202 | output_tokens: 4254
- judge_score: 4.8 | justificación: 

## Respuesta completa

# 🚀 Outline: "Construye tu Asistente de IA para tu Startup - Workshop Práctico"
*Facilitador: Enfoque LATAM | Audiencia: Emprendedores early-stage no-técnicos | Duración: 3 horas*

---

## 📅 1. Agenda Detallada (180 min)
| Hora | Actividad |
|------|-----------|
| 0:00 - 0:15 | Bienvenida, rompehielos & contexto LATAM |
| 0:15 - 0:45 | **Bloque 1:** De la idea al flujo: ¿Qué automatizo primero? |
| 0:45 - 1:15 | **Bloque 2:** El stack no-code que sí funciona (sin humo) |
| 1:15 - 1:25 | ☕ Break & networking estratégico |
| 1:25 - 2:25 | **Bloque 3:** 🛠️ Ejercicio Principal: Tu MVP en 60 min |
| 2:25 - 2:50 | **Bloque 4:** Despliegue, métricas y próximos pasos |
| 2:50 - 3:00 | Cierre, compromiso & Q&A relámpago |

---

## 🎒 2. Materiales Necesarios (Preparar antes)
**Para el facilitador:**
- Proyector + pantalla + audio portátil
- WiFi de respaldo (hotspot móvil o línea dedicada)
- Cuentas demo activas en las herramientas clave
- Plantillas impresas: `Canvas de Flujo`, `Checklist de Despliegue`, `Post-its`, marcadores
- Power strips (enchufes múltiples) + adaptadores internacionales
- Link de formulario pre-workshop (recopilar: nombre, sector, dolor principal, FAQ base)

**Para los participantes (enviar 48h antes):**
- Laptop con Chrome/Edge actualizado
- Cuentas gratuitas creadas: `Make.com`, `Tidio` o `Chatbase`, `Google Sheets`
- 1 archivo PDF o link con las 10 preguntas más frecuentes de su startup
- Conexión WiFi estable (o celular con hotspot)

---

## 🧩 3. Estructura por Bloque

### 🔹 Bloque 1: De la idea al flujo: ¿Qué automatizo primero?
- **Duración:** 30 min
- **Objetivo:** Identificar un proceso repetitivo de alto impacto y traducirlo en un flujo lógico sin código.
- **Dinámica:** 
  - Charla energética (10 min): "La IA no es magia, es un empleado que no duerme. Pero necesita instrucciones claras."
  - Ejercicio rápido en parejas (10 min): Mapear su dolor principal en el `Canvas de Flujo`.
  - Discusión abierta (10 min): 3 voluntarios comparten; facilitador valida viabilidad.
- **Key Takeaway:** `Un flujo claro > una IA mágica. Empieza por lo que te quita 5h/semana.`

### 🔹 Bloque 2: El stack no-code que sí funciona (sin humo)
- **Duración:** 30 min
- **Objetivo:** Conocer herramientas accesibles, sus límites y cómo se conectan entre sí.
- **Dinámica:**
  - Demo en vivo (15 min): Mostrar cómo se mueve un dato desde un formulario → IA → respuesta → CRM.
  - Explicación de arquitectura (10 min): "Trigger → Procesador → Acción". Comparativa rápida de Make vs Zapier vs n8n.
  - Mini Q&A (5 min): Resolver dudas de acceso, pagos y límites free.
- **Key Takeaway:** `No necesitas código, necesitas lógica y buenas herramientas. El stack se elige por el caso, no al revés.`

### 🔹 Bloque 3: 🛠️ Ejercicio Principal: Tu MVP en 60 min
- **Duración:** 60 min
- **Objetivo:** Construir un prototipo funcional que atienda un caso real de su startup.
- **Dinámica:** 
  - Instrucción paso a paso (10 min)
  - Hands-on guiado + mentoría en mesa (40 min)
  - Demo relámpago (10 min): 3 equipos muestran su bot funcionando.
- **Key Takeaway:** `Un MVP funcional en 1 hora es posible. Lanzar es aprender, no perfeccionar.`

### 🔹 Bloque 4: Despliegue, métricas y próximos pasos
- **Duración:** 25 min
- **Objetivo:** Entender cómo publicar, medir y escalar sin romper el presupuesto.
- **Dinámica:**
  - Charla práctica (10 min): Dónde alojar, cómo configurar dominio, métricas que importan (CTR, resolución, costo/interacción).
  - Checklist en vivo (10 min): Revisión rápida de `Checklist de Despliegue`.
  - Discusión abierta (5 min): Obstáculos comunes en LATAM (pagos, compliance, WhatsApp-first).
- **Key Takeaway:** `La IA no reemplaza tu hustle, lo potencia. Mide, itera, lanza.`

### 🔹 Cierre: Compromiso y comunidad
- **Duración:** 10 min
- **Objetivo:** Cerrar con acción concreta y red de apoyo.
- **Dinámica:** Pitch relámpago (3 min) + firma de `Compromiso de 7 días` + Q&A final (5 min).
- **Key Takeaway:** `Tu asistente no se construye en un workshop, se construye en tu semana. Empieza hoy.`

---

## 🛠️ 4. Ejercicio Principal (Paso a Paso)
**Nombre:** `Bot de FAQs + Captura de Lead (WhatsApp/Web)`
**Herramientas:** `Tidio (UI) + Make.com (Lógica) + Google Sheets (Base) + LLM gratuito (OpenRouter/Google AI Studio)`
**Viabilidad:** 100% no-code, tiers gratuitos cubren el ejercicio.

**Flujo:**
1. **Trigger:** Usuario escribe "¿Cuánto cuesta?" o "¿Cómo pago?" en el chat.
2. **Procesador:** Make.com detecta la palabra clave → llama a la API de LLM con un prompt predefinido + contexto de su PDF.
3. **Acción:** El bot responde en <3 seg → guarda el lead en Google Sheets → envía un link de pago/booking si aplica.
4. **Despliegue:** Publicar en web o WhatsApp Business API (simulado en Tidio para el taller).

**Guía para no-técnicos:**
- Usar `Make.com` visual: arrastrar bloques, conectar flechas.
- Prompt template incluido en materiales: `"Actúa como el asistente de [Startup]. Responde en max 3 líneas. Usa solo info de este contexto: [pegar]. Si no sabes, di: 'Te conecto con un humano'."`
- Validación en vivo: facilitador circula con checklist de 5 puntos (conexión, prompt, respuesta, guardado, UI).

---

## 📦 5. Recursos para Llevar a Casa
- 📄 `Cheat Sheet: Stack No-Code para Startups LATAM` (comparativa gratuita/pago, límites, soporte español)
- 🤖 `Biblioteca de 15 Prompts Listos` (FAQ, calificación de leads, soporte post-venta, onboarding)
- 📊 `Dashboard de Métricas IA` (plantilla en Notion/Sheets para trackear resolución, costo, feedback)
- 🔗 `Checklist de Despliegue Seguro` (compliance básico LATAM, privacidad, fallback humano)
- 🌐 `Comunidad Privada (Telegram/Discord)` + acceso a grabación del workshop
- 🎁 `Cupones de prueba` (Make, Tidio, OpenRouter) + link a `Directorio de Agencias No-Code Verificadas LATAM`

---

## 📊 6. Slide Count Estimado por Sección
| Sección | Slides | Notas |
|---------|--------|-------|
| Bienvenida & Contexto | 8 | Fotos de casos LATAM, agenda, reglas del juego |
| Bloque 1 | 12 | Canvas visual, ejemplos de flujos, errores comunes |
| Bloque 2 | 15 | Arquitectura, comparativa herramientas, demo screenshots |
| Break | 0 | - |
| Bloque 3 | 5 | Solo pasos clave + links + QR al material de apoyo (el resto es pantalla compartida en vivo) |
| Bloque 4 | 10 | Métricas, checklist, compliance, roadmap 30 días |
| Cierre | 5 | Compromiso, comunidad, Q&A |
| **Total** | **~50** | Diseño limpio, 1 idea/slide, 70% visual/20% texto, 10% interacción |

---

