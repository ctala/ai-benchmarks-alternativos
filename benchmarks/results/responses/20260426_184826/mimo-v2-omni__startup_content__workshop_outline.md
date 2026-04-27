# MiMo-V2-Omni (multimodal) — startup_content/workshop_outline

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 7.53 | quality: 9.24
- latency_total: 26.567s | tokens_per_second: 77.1
- input_tokens: 209 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# 🚀 "Construye tu Asistente de IA para tu Startup"
## Workshop Práctico — 3 Horas

---

## 📋 INFORMACIÓN GENERAL

| Detalle | Descripción |
|---|---|
| **Duración** | 3 horas (180 min) |
| **Audiencia** | Emprendedores early-stage, no técnicos |
| **Capacidad** | 20-30 personas |
| **Nivel** | Principiante (cero código) |
| **Herramienta principal** | Custom GPTs de OpenAI (gratis con cuenta) |
| **Objetivo final** | Cada participante sale con su propio Asistente de IA funcionando |

---

## 🧰 MATERIALES A PREPARAR ANTES

### Para el facilitador:
- [ ] Presentación en slides (≈55 slides total)
- [ ] 2-3 Custom GPTs de demo ya creados (ej: asistente de ventas, soporte al cliente, onboarding)
- [ ] Cuenta de OpenAI verificada (para demo en vivo)
- [ ] Timer visible (proyector o pantalla)
- [ ] Música ambiente para momentos de trabajo (lo-fi / energética)
- [ ] Pizarra blanca o digital para anotar respuestas
- [ ] Link de acceso al recurso compartido (Google Drive con templates)

### Para cada participante (enviar 48h antes):
- [ ] Cuenta de OpenAI creada y verificada → **openai.com** (gratis)
- [ ] Traer laptop con navegador actualizado
- [ ] Tener claro: **¿Qué problema resuelve tu startup?**
- [ ] Tener claro: **¿Cuál es tu principal interacción con clientes?**

### En el venue:
- [ ] Mesas en grupos de 4-5 personas
- [ ] WiFi estable (¡CRÍTICO! tener plan B hotspot)
- [ ] Toma de corriente por mesa o al menos cada 2
- [ ] Pizarras small-format (1 por mesa) o post-its grandes
- [ ] Café/snacks disponibles
- [ ] Name tags con espacio grande para el nombre

---

## 📐 AGENDA DETALLADA

---

### BLOQUE 1 — APERTURA Y MOTIVACIÓN
**⏱ Duración: 20 minutos (0:00 → 0:20)**

> **🎯 Objetivo:** Generar energía, crear urgencia, y demostrar que SÍ pueden hacerlo aunque no sean técnicos.

**SLIDES: 5**

| Minuto | Qué ocurre | Detalle |
|---|---|---|
| 0:00-0:03 | **Apertura con energía** | Bienvenida, regla #1 del taller: *"Hoy no se pregunta 'si puedo', solo 'cómo'"*. Presentarte con tu historia personal con IA. |
| 0:03-0:07 | **La pregunta que rompe todo** | Pregunta al grupo: *"¿Cuántos de ustedes creen que construir un asistente de IA requiere programar?"* → Levantar manos → Romper ese mito con datos: *"En 2024, el 80% de las herramientas de IA se construyen sin código."* |
| 0:07-0:14 | **Demo en vivo (WOW moment)** | Mostrar 2 Custom GPTs funcionando en vivo: **1)** Un asistente de ventas que califica leads como un SDR experto. **2)** Un asistente de soporte que responde FAQs de un producto ficticio. Decir: *"Esto lo construí en 7 minutos. Hoy ustedes van a construir el suyo."* |
| 0:14-0:18 | **El framework mental** | Presentar el modelo: **Problema del cliente → Flujo de conversación → Asistente de IA**. Mostrar 3 ejemplos reales de startups latam que usan asistentes (casos reales o inspirados). |
| 0:18-0:20 | **Configurar expectativas** | Agenda rápida visual. *"Vamos a construir, no solo a escuchar."* Pedir que abran su laptop y verifiquen que pueden entrar a openai.com. |

**🔑 Key Takeaway:** *"No necesitas ser ingeniero. Necesitas entender a tu cliente y saber comunicarle eso a la IA."*

**Dinámica:** Charla + Demo en vivo + Encuesta con levantada de manos

---

### BLOQUE 2 — PROMPT ENGINEERING PARA EMPRENDEDORES
**⏱ Duración: 25 minutos (0:20 → 0:45)**

> **🎯 Objetivo:** Entender cómo "hablarle" a la IA para que haga lo que necesitas. Sin esto, no pueden construir nada.

**SLIDES: 8**

| Minuto | Qué ocurre | Detalle |
|---|---|---|
| 0:20-0:28 | **Charla: La estructura que lo cambia todo** | Presentar el framework **R-A-O** (Rol → Acción → Output). Explicar con ejemplos malos vs buenos. Ejemplo malo: *"Eres un asistente"*. Ejemplo bueno: *"Eres Carlos, un asistente de ventas B2B para una startup de logística en México. Hablas con dueños de e-commerce. Tu objetivo es calificar si tienen más de 100 pedidos/mes antes de agendar una demo. Preguntas máximo 5 cosas. Eres directo pero amable."* |
| 0:28-0:33 | **Charla: Los 5 ingredientes de un prompt poderoso** | Presentar: **1)** Personalidad/rol, **2)** Contexto del negocio, **3)** Reglas de comportamiento, **4)** Formato de respuesta, **5)** Ejemplos de lo que SÍ y NO hacer. Usar analogía: *"Es como entrenar un nuevo empleado. Le dices quién es, qué hace, cómo habla, y qué no debe hacer."* |
| 0:33-0:40 | **⚡ Ejercicio rápido: "El peor prompt vs el mejor"** | En parejas. Reciben una tarjeta con un prompt malísimo. Tienen 4 minutos para mejorarlo usando el framework R-AO. Luego 3 parejas comparten. El facilitador muestra la versión "pro" y compara. **Ejercicio en papel para que