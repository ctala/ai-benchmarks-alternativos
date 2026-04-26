# MiMo-V2.5 (omnimodal) — startup_content/workshop_outline

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 7.33 | quality: 9.24
- latency_total: 17.844s | tokens_per_second: 114.8
- input_tokens: 209 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# 🚀 "CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP"
## Workshop Presencial — 3 Horas

---

## 📋 AGENDA GENERAL

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 | Bienvenida + Icebreaker | 15 min |
| 0:15 | Bloque 1: La Revolución de los Asistentes IA | 15 min |
| 0:30 | Bloque 2: Anatomía de un Asistente IA | 20 min |
| 0:50 | Bloque 3: Prompt Engineering para Fundadores | 25 min |
| 1:15 | ☕ BREAK | 10 min |
| 1:25 | Bloque 4: Demo en Vivo — Construcción Paso a Paso | 20 min |
| 1:45 | Bloque 5: ⚡ EJERCICIO PRINCIPAL — ¡Construye el Tuyo! | 45 min |
| 2:30 | Bloque 6: Testing, Iteración y Trucos Avanzados | 10 min |
| 2:40 | Bloque 7: Show & Tell + Preguntas | 15 min |
| 2:55 | Cierre + Recursos para Llevar a Casa | 5 min |
| **3:00** | **FIN** | **Total: 180 min** |

---

## 🧰 MATERIALES NECESARIOS (Preparación Pre-Workshop)

### Para el Facilitador:
- [ ] Laptop con conexión a internet estable + proyector/pantalla grande
- [ ] Cuenta de **ChatGPT Plus** activa (para demostrar Custom GPTs)
- [ ] Cuenta **alternativa de respaldo** (Gemini, Claude) por si hay caída
- [ ] **2-3 Custom GPTs ya construidos** como ejemplos listos (uno de atención al cliente, uno de ventas, uno de onboarding)
- [ ] Presentación en slides (Google Slides / Canva)
- [ ] Timer visible (app tipo "Big Timer" proyectada)
- [ ] Música ambiental para las sesiones de trabajo
- [ ] Webcam portátil o document cam para mostrar pantallas de cerca
- [ ] **Cable HDMI + adaptador USB-C** (y backup)

### Para los Participantes (enviar 48h antes):
- [ ] ✅ Laptop propia (obligatorio)
- [ ] ✅ Cuenta activa en **ChatGPT** (plan gratuito funciona, Plus es ideal — $20 USD/mes)
- [ ] ✅ Acceso al **Custom GPT Builder** (disponible en ChatGPT Plus)
- [ ] ✅ **Alternativa GRATUITA**: Cuenta en **Google Gemini** + **Botpress** (para quienes no tengan ChatGPT Plus)
- [ ] ✅ Traer **escrito en papel o digital**: una descripción de 3 oraciones de su startup y su cliente ideal
- [ ] ✅ Traer **10 preguntas frecuentes** que recibe su startup regularmente

### Para el Espacio:
- [ ] Mesas en formato "islas" (4-5 personas por mesa)
- [ ] Pizarras/flipcharts por mesa (1 por grupo)
- [ ] Post-its, marcadores, Sharpies
- [ ] Snacks y café ☕
- [ ] WiFi con señal fuerte (verificar capacidad para 30 dispositivos)
- [ ] Cargadores de emergencia (3-4 power banks)
- [ ] QR code impreso con link a carpeta de recursos

---

## 📑 DESGLOSE POR BLOQUE

---

### 🎉 BIENVENIDA + ICEBREAKER
**Duración:** 15 minutos
**Slides:** 5

**Objetivo:** Generar energía, romper el hielo, crear expectativa y alinear expectativas.

**Dinámica:** Charla interactiva + dinámica rápida

**Contenido:**

| Min | Actividad |
|-----|-----------|
| 0-3 | **Bienvenida personalizada.** El facilitador llega con energía alta. Frase apertura: *"Hoy no van a aprender sobre IA. Hoy van a SALIR de aquí con un asistente de IA funcionando para su startup. En sus manos."* |
| 3-7 | **Dinámica "El Pitch de 30 Segundos Rápido":** Cada persona se presenta con: nombre, startup, y en UNA frase: *"Si tu startup tuviera un asistente mágico, ¿qué haría?"* (Se hace en parejas, no con todo el grupo — 2 min cada uno). |
| 7-10 | **3 preguntas rápidas al aire** (manos arriba): "¿Quién ya usó ChatGPT?" → "¿Quién tiene una startup en etapa temprana?" → "¿Quién nunca programó nada en su vida?" (Validar que es el público correcto, generar confianza). |
| 10-13 | **Promesa del workshop:** Mostrar el resultado final — proyectar un Custom GPT funcionando en vivo. *"Algo parecido a esto van a tener al final de hoy, personalizado para SU negocio."* |
| 13-15 | **Logística rápida:** Baños, break, WiFi (mostrar QR), reglas del espacio (celulares en modo silencio, preguntar siempre, no hay preguntas tontas). |

**Key Takeaway:** *"Vas a salir de aquí con algo real que puedes usar mañana en tu negocio."*

---

### 🧠 BLOQUE 1: LA REVOLUCIÓN DE LOS ASISTENTES IA
**Duración:** 15 minutos
**Slides:** 8-10

**Objetivo:** Entender qué son los asistentes de IA, por qué ahora es el momento perfecto para los emprendedores, y desmitificar la tecnología.

**Dinámica:** Charla visual + storytelling + mini-discusión

**Contenido:**

| Min | Actividad |
|-----|-----------|
| 15-18 | **Storyt