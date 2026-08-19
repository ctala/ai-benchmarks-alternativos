# Devstral 2 (Dic 2025) — startup_content/curso_emprendimiento_modulo

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.6 | quality: 9.44
- latency_total: 20.813s | tokens_per_second: 74.2
- input_tokens: 239 | output_tokens: 1545
- judge_score: 4.6 | justificación: 

## Respuesta completa

```markdown
# **Módulo 3: Automatización con IA – De la idea al flujo de trabajo**
*Curso: IA Práctica para Emprendedores*

---

## **🎯 Objetivo del módulo**
Al finalizar este módulo, podrás identificar oportunidades de automatización en tu negocio usando IA, seleccionar herramientas accesibles (como **n8n**) y diseñar flujos de trabajo que ahorren tiempo en tareas repetitivas. Aprenderás con ejemplos reales aplicables a atención al cliente, marketing y ventas, y crearás tu primera automatización paso a paso.

---

## **📚 Contenido teórico**

### **¿Qué es la automatización con IA?**
Automatizar con IA significa usar herramientas que **toman decisiones o ejecutan acciones** basadas en datos, sin intervención humana constante. Por ejemplo:
- Un chatbot que responde preguntas frecuentes.
- Un sistema que publica contenido en redes sociales según un calendario.
- Un filtro que clasifica leads según su probabilidad de compra.

### **Herramientas clave para no-técnicos**
1. **n8n** (recomendada):
   - Plataforma de automatización **open-source** (gratis en su versión básica).
   - Conecta apps como WhatsApp, Google Sheets, Mailchimp, etc., con IA (ej: OpenAI, Hugging Face).
   - Ejemplo: Si un cliente envía un mensaje por WhatsApp, n8n puede responder automáticamente con IA.

2. **Zapier/Make (Integromat)**:
   - Alternativas más simples (pero con planes pagos).
   - Ideales para automatizaciones básicas sin código.

3. **IA generativa (OpenAI, Mistral, etc.)**:
   - Se integran a los flujos para generar respuestas, analizar textos o clasificar datos.

---

## **🔧 3 Ejemplos prácticos para startups**

### **1. Atención al cliente automatizada**
**Problema**: Responder preguntas frecuentes en WhatsApp/email consume horas.
**Solución**:
- Usar un chatbot con IA que:
  - Detecte palabras clave (ej: "precio", "envío").
  - Responda con información predefinida o generada por IA.
  - Escalé a un humano si no entiende.
**Herramientas**: n8n + OpenAI + WhatsApp Business API.

### **2. Generación de contenido para redes sociales**
**Problema**: Crear posts diarios es agotador.
**Solución**:
- Automatizar:
  1. Un prompt en IA que genere textos basados en tu nicho (ej: "10 tips de marketing para panaderías").
  2. Programar publicaciones en Instagram/Facebook con Canva + Buffer.
**Herramientas**: n8n + OpenAI + Buffer.

### **3. Calificación automática de leads**
**Problema**: Perder tiempo contactando leads que no compran.
**Solución**:
- Un flujo que:
  1. Reciba datos de un formulario (ej: "¿Cuál es tu presupuesto?").
  2. Use IA para asignar una puntuación (ej: 1-10) según respuestas.
  3. Envíe los leads "calientes" a tu equipo de ventas.
**Herramientas**: n8n + Google Forms + OpenAI.

---

## **🛠️ Ejercicio práctico: Crea un chatbot para WhatsApp con n8n**

**Objetivo**: Automatizar respuestas a preguntas frecuentes en WhatsApp usando IA.

### **Paso 1: Prepara tus herramientas**
- Regístrate en [n8n.cloud](https://n8n.io/) (plan gratuito).
- Necesitarás:
  - Una cuenta de WhatsApp Business (o Twilio para pruebas).
  - Una API key de OpenAI (gratis con créditos iniciales).

### **Paso 2: Configura el flujo en n8n**
1. **Nodo 1: WhatsApp (Trigger)**:
   - Selecciona "WhatsApp" como nodo inicial.
   - Conecta tu cuenta (sigue las instrucciones de n8n).

2. **Nodo 2: OpenAI (Procesamiento)**:
   - Añade un nodo "OpenAI".
   - Configura el prompt:
     ```
     Eres un asistente de [tu negocio]. Responde de forma breve y amable.
     Si no sabes la respuesta, di: "Un humano te responderá pronto".
     Pregunta del cliente: {{ $json["message"] }}
     ```

3. **Nodo 3: WhatsApp (Respuesta)**:
   - Conecta otro nodo de WhatsApp para enviar la respuesta generada por IA.

### **Paso 3: Prueba y mejora**
- Envía un mensaje a tu WhatsApp Business con una pregunta frecuente (ej: "¿Cuál es tu horario?").
- Verifica que el chatbot responda.
- Ajusta el prompt si las respuestas no son útiles.

**📌 Tip**: Guarda el flujo para reutilizarlo. ¡Puedes añadir más nodos (ej: guardar datos en Google Sheets)!.

---

## **📂 Recursos adicionales**
- **Tutorial en video**: [Cómo usar n8n para automatizar WhatsApp](https://www.youtube.com/watch?v=ejemplo) *(reemplazar con enlace real)*.
- **Plantillas de prompts**: [GitHub con ejemplos para chatbots](https://github.com/ejemplo/prompts).
- **Comunidad**: Grupo de Facebook "Automatización para Emprendedores LATAM" *(crear o linkear uno existente)*.

---

## **❓ Autoevaluación**
1. **¿Cuál de estas tareas NO es buena candidata para automatizar con IA?**
   a) Responder preguntas frecuentes de clientes.
   b) Tomar decisiones estratégicas complejas (ej: lanzar un nuevo producto).
   c) Publicar contenido en redes sociales según un calendario.

2. **En el ejercicio práctico, ¿qué nodo de n8n se encarga de "entender" el mensaje del cliente?**
   a) WhatsApp (Trigger).
   b) OpenAI.
   c) Google Sheets.

3. **Si tu startup recibe 100 leads al día, ¿cómo podrías usar IA para priorizarlos?**
   a) Crear un chatbot que hable con cada lead.
   b) Usar un flujo que asigne una puntuación basada en sus respuestas.
   c) Automatizar el envío de emails genéricos a todos.

**Respuestas**: 1(b), 2(b), 3(b).

---
**🚀 ¡Ahora es tu turno!**
Elige **una tarea repetitiva** en tu negocio y diseña un flujo de automatización en n8n. Comparte tu experiencia en los comentarios del curso.
```