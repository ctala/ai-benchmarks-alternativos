# MiMo-V2.5 (omnimodal) — startup_content/workshop_outline

- model_id: `xiaomi/mimo-v2.5`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 33.644s | tokens_per_second: 60.9
- input_tokens: 209 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante y clara, con una estructura bien organizada que cubre todos los aspectos solicitados. Ofrece información práctica y útil para emprendedores no técnicos, aunque podría profundizar un poco más en algunos aspectos técnicos.

## Respuesta completa

# 🚀 CONSTRUYE TU ASISTENTE DE IA PARA TU STARTUP
## Workshop Práctico — Outline Completo (3 horas)

---

## 📋 AGENDA GENERAL RESUMIDA

| Bloque | Tiempo | Contenido |
|--------|--------|-----------|
| 0 | 0:00 – 0:15 | Bienvenida + Icebreaker |
| 1 | 0:15 – 0:45 | "El AI Assistant que tu startup necesita" |
| 2 | 0:45 – 1:15 | Demo en vivo: Cómo se construye |
| 3 | 1:15 – 1:30 | ☕ Break |
| 4 | 1:30 – 2:30 | 🔥 Ejercicio Principal: "Tu asistente en acción" |
| 5 | 2:30 – 2:50 | Pilotos, métricas y errores comunes |
| 6 | 2:50 – 3:00 | Cierre + Recursos + Foto grupal |

---

## 📦 MATERIALES NECESARIOS (Preparación)

### **Lo que prepara el facilitador ANTES:**
- [ ] Presentación en Google Slides o Canva (~50-55 slides)
- [ ] Cuenta de **Chatbase** (plan free) probada y funcionando
- [ ] Cuenta de **ChatGPT** (plan Plus recomendado, pero no obligatorio)
- [ ] 3 ejemplos de asistentes AI ya construidos (uno de cada tipo: soporte, ventas, onboarding)
- [ ] Enlace QR para que los asistentes scaneen y accedan a todos los links
- [ ] Hoja de plantilla "Brief de tu Asistente AI" (imprimida o en PDF)
- [ ] Cuenta de **Canva** para que participantes diseñen el avatar (opcional)
- [ ] WiFi estable y funcional (CRÍTICO — tener plan B: hotspot)
- [ ] Proyector + cable HDMI / adaptadores
- [ ] Pizarra o post-its grandes

### **Lo que necesitan los participantes:**
- [ ] Laptop (obligatorio) o celular como mínimo
- [ ] Cuenta de **ChatGPT** abierta (free o Plus)
- [ ] Cuenta de **Chatbase** (pueden crearla en el workshop)
- [ ] Tener claro el **problema** que resuelve su startup (1 frase)
- [ ] (Ideal) Tener algún contenido de su negocio: FAQ, descripción de servicios, posts, etc.

### **Kit del participante (digital):**
- Plantilla "Brief de tu Asistente AI" (Google Doc)
- Guía de prompts para entrenar tu bot (PDF de 2 páginas)
- Lista de herramientas recomendadas
- Acceso a comunidad post-workshop (Slack/Discord/WhatsApp)

---

## 🔎 DESGLOSE POR BLOQUE

---

### **BLOQUE 0: BIENVENIDA + ICEBREAKER**
**⏱ Tiempo: 15 minutos (0:00 – 0:15)**

**🎯 Objetivo:**
Generar energía, crear confianza grupal y que cada persona entienda qué va a lograr hoy.

**📌 Dinámica:**
1. **Bienvenida personal** (3 min): El facilitador se presenta con una anécdota real — *"Hace 6 meses, esta startup que ven aquí usó un chatbot para cerrar sus primeros 40 clientes sin contratar a nadie"* (o historia similar).
2. **El reto del día** (2 min): *"En las próximas 3 horas, cada uno de ustedes va a tener un asistente AI funcionando, conectado a su negocio, listo para compartir con clientes esta noche."* — Mostrar pantalla con el resultado final.
3. **Icebreaker relámpago** (8 min): Cada persona dice en 15 segundos:
   - Su nombre
   - Su startup (en 5 palabras máximo)
   - **"Si mi startup tuviera un empleado invisible que trabajara 24/7, haría ______"**

**📝 Key Takeaway:**
> *"Hoy no ven una charla. Hoy construyen. Se van con algo que funciona."*

**📊 Slides estimadas: 3**
- Slide 1: Título + foto del facilitador
- Slide 2: "¿Qué vas a lograr hoy?" (imagen del resultado)
- Slide 3: Instrucciones del icebreaker

---

### **BLOQUE 1: "EL AI ASSISTANT QUE TU STARTUP NECESITA"**
**⏱ Tiempo: 30 minutos (0:15 – 0:45)**

**🎯 Objetivo:**
Que los participantes entiendan qué es un asistente AI, cuáles son los tipos, y cuál les sirve a SU negocio — sin jerga técnica.

**📌 Dinámica:**
**Charla interactiva + preguntas al público + 1 mini-ejercicio individual**

**Contenido (en orden):**

1. **¿Qué demonios es un Asistente AI?** (5 min)
   - No es un robot. Es un empleado digital que conoce tu negocio.
   - Analogía: *"Es como tener a tu mejor vendedor / soporte, pero que nunca duerme, nunca se enferma y nunca contesta mal."*
   - Diferencia clave: ChatGPT genérico vs. TU asistente entrenado en TU negocio

2. **Los 3 tipos de asistentes que te importan** (8 min)
   - 🟢 **Soporte / FAQ** — Responde preguntas frecuentes (cliente: *"¿Tienen envío gratis?"*)
   - 🔵 **Generación de leads** — Califica y captura info de clientes potenciales
   - 🟡 **Onboarding / Uso** — Ayuda al cliente a usar tu producto o servicio

   *Preguntar al público: "¿Cuántos reciben la misma pregunta todos los días? ¿Cuántos quisieran dormir tranquilos sabiendo que eso se responde solo?"*

3. **¿Para qué SÍ y para qué NO sirve?** (7 min)
   - ✅ FAQ, recomendaciones, calificación de leads, agendar citas, guiar compras
   - ❌ Tomar decisiones financieras, reemplazar asesoría legal/medica, cerrar ventas de alto valor sin supervisión
   - ⚠️ *"El error #1: querer que el bot haga TODO. Empieza con UN caso de uso."*

4. **Mini-ejercicio: "Tu asistente en 1 frase"** (8 min)
   - Cada persona llena en la hoja de plantilla:
     > *"Mi asistente AI se llama ______, atiende a ______ (tipo de cliente), y le ayuda con ______."*
   - 3 voluntarios comparten en voz alta (el facilitador da feedback rápido en vivo)
   - Esto se convierte en la guía del ejercicio principal

5. **Cierre del bloque** (2 min)
   - *"Van a tener su propio asistente. Pero primero, déjenme mostrles cómo funciona."*

**📝 Key Takeaway:**
> *"Un buen asistente AI resuelve UN problema específico muy bien. No intenten construir a Siri. Empiecen con la pregunta que más les repiten."