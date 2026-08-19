# Qwen 3-Next 80B Instruct — startup_content/curso_emprendimiento_modulo

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 8.35 | quality: 9.48
- latency_total: 24.613s | tokens_per_second: 83.2
- input_tokens: 252 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

```markdown
# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

## 🎯 Objetivo del módulo

En este módulo aprenderás a convertir tareas repetitivas y manuales de tu startup en flujos automáticos impulsados por inteligencia artificial. No necesitas ser programador: usarás herramientas visuales fáciles para conectar apps, responder mensajes, generar contenido y clasificar clientes sin tocar una línea de código. Al final, tendrás al menos un flujo automatizado funcionando en tu negocio, ahorrando horas semanales y escalando tu atención al cliente sin aumentar tu equipo.

---

## 📚 Contenido teórico: ¿Qué es la automatización con IA y cómo funciona?

**Automatización con IA** significa usar inteligencia artificial para que programas hagan tareas que antes hacías tú manualmente —como responder emails, escribir publicaciones o decidir qué lead vale la pena llamar— y hacerlo de forma inteligente, aprendiendo con el tiempo.

### ¿Cómo lo logramos sin ser técnicos?
Herramientas como **n8n** (pronunciado “en-ocho-n”) son plataformas visuales que te permiten “conectar” apps como Gmail, WhatsApp, Instagram, Google Sheets y ChatGPT con bloques arrastrables, como Lego.

▶️ **Ejemplo simple**:  
Cuando alguien llena un formulario en tu sitio web → n8n lo detecta → usa IA para leer su mensaje → lo clasifica como “interesado”, “duda” o “no útil” → y guarda el dato en una hoja de cálculo + envía un email de bienvenida automaticamente.

**Ventaja clave**:  
Esto ahorra 5-10 horas/semana en tareas repetitivas, y la IA mejora con cada respuesta que recibe.

> 💡 **Clave para emprendedores**: No necesitas saber Python. Solo necesitas saber *qué tarea te molesta hacer 2 veces por semana*. Esa es tu primera automatización.

---

## 🚀 3 Ejemplos prácticos de automatización para startups

### 1. **Atención al cliente automatizada**
**Problema**: Recibes 20 mensajes diarios por WhatsApp o Instagram preguntando “¿Cuánto cuesta?”, “¿Tienen descuento?”, “¿Cuándo llega?”  
**Solución con IA**:  
- Usa **n8n + WhatsApp Business API + ChatGPT**  
- Cuando llega un mensaje, ChatGPT lo interpreta y responde con un mensaje pre-entrenado (ej: “¡Hola! Nuestro precio es $49/mes. ¿Quieres probarlo gratis 7 días?”)  
- Si el mensaje es complejo (“Quisiera personalizar el producto”), lo deriva a ti con un label “Urgente: necesita respuesta humana”  

✅ **Resultado**: 80% de preguntas comunes respondidas sin intervención.

---

### 2. **Generación de contenido para redes sociales**
**Problema**: Te lleva 3 horas por semana crear 5 publicaciones para Instagram y LinkedIn.  
**Solución con IA**:  
- Usa **n8n + ChatGPT + Canva API (o Google Sheets)**  
- Cada lunes, n8n abre tu calendario en Google Sheets → le pide a ChatGPT: “Crea 5 posts para [tu industria] con tono cercano y emojis” → genera el texto → lo guarda en una hoja → y te envía un link para que lo revises y publiques en 2 minutos  

✅ **Resultado**: 1 hora/semana en lugar de 3, y contenido consistente.

---

### 3. **Calificación automática de leads**
**Problema**: Recibes 50 formularios al mes, pero no sabes cuáles son reales y cuáles son solo curiosos.  
**Solución con IA**:  
- Usas **n8n + Google Forms + ChatGPT**  
- Cuando alguien llena tu formulario (nombre, email, pregunta, presupuesto), n8n envía esa info a ChatGPT con esta instrucción:  
> “Clasifica este lead como ‘ALTA’, ‘MEDIA’ o ‘BAJA’ según:  
> - Si menciona presupuesto > $100 → ALTA  
> - Si pregunta por precio → MEDIA  
> - Si dice ‘solo estoy investigando’ → BAJA  
> Devuelve solo una palabra: ALTA, MEDIA o BAJA”  
- Luego, n8n actualiza tu hoja de Google Sheets con la calificación y envía un email de seguimiento automático solo a los de ALTA.  

✅ **Resultado**: Te enfocas solo en los leads que realmente van a comprar.

---

## 🛠️ Ejercicio práctico paso a paso: Automatiza tu primera respuesta de WhatsApp

### Objetivo:  
Crear un flujo que responda automáticamente a mensajes de WhatsApp con una frase personalizada, usando IA.

### Herramientas que necesitas:
- [n8n.io](https://n8n.io) (gratis hasta 100 ejecuciones/mes)
- Una cuenta de WhatsApp Business (puedes usar tu número personal con la app [Twilio](https://www.twilio.com/) o simularlo con un formulario)
- [ChatGPT](https://chat.openai.com/) (cuenta gratuita basta)

### Pasos:

#### Paso 1: Crea una cuenta en [n8n](https://n8n.io)
Haz clic en “Sign Up” → usa tu email. No necesitas tarjeta.

#### Paso 2: Crea un nuevo flujo
Haz clic en “Create a new workflow”.

#### Paso 3: Agrega el nodo “Webhook”
- Busca “Webhook” en la barra de nodos → arrástralo al canvas.
- Configúralo:  
  - Method: `POST`  
  - Path: `/whatsapp`  
  - Haz clic en “Save”.

> ✅ Copia la URL que aparece (ej: `https://tu-nombre.n8n.cloud/webhook/whatsapp`)

#### Paso 4: Agrega el nodo “ChatGPT”
- Busca “ChatGPT” → arrástralo.
- Conecta el “Webhook” al “ChatGPT” (clic en el círculo del Webhook y arrastra hasta el ChatGPT).
- En “Prompt”, pega esto:  
  ```
  Eres el asistente de [Tu Nombre], dueño de [tu negocio]. Responde amablemente a este mensaje del cliente: "{{ $json.message }}"
  Usa tono cercano, con emojis si es apropiado. Máximo 2 frases.  
  No hables de precios a menos que te lo pidan.
  ```
- En “API Key”, pega tu clave de OpenAI (la obtienes en [platform.openai.com/api-keys](https://platform.openai.com/api-keys)).

#### Paso 5: Agrega el nodo “Debug”
- Busca “Debug” → arrástralo y conéctalo al ChatGPT.
- Haz clic en “Execute Workflow” (botón verde en la esquina superior).

#### Paso 6: Prueba con un mensaje
Abre tu navegador y pega esto en la barra de direcciones (reemplaza tu URL):  
```
https://tu-nombre.n8n.cloud/webhook/whatsapp
```
Pero con un POST (para simular un mensaje).  
Usa [https://webhook.site](https://webhook.site) para probar:  
1. Abre [webhook.site](https://webhook.site)  
2. Copia tu URL de n8n  
3. En webhook.site, haz clic en “Send a sample POST request”  
4. En “Body”, pon:  
```json
{
  "message": "Hola, ¿cuánto cuesta tu servicio?"
}
```
5. Haz clic en “Send”

#### Paso 7: ¡Verifica el resultado!
Vuelve a n8n → haz clic en el nodo “Debug” → verás la respuesta de ChatGPT:  
> “¡Hola! 😊 Gracias por preguntar. Nuestro servicio cuesta $49/mes y puedes probarlo gratis 7 días. ¿Te gustaría agendar una llamada rápida? 📅”

✅ **¡Felicidades!** Acabas de automatizar tu primera respuesta de cliente.

> 💡 **Siguiente paso**: Conecta esto a WhatsApp usando la integración de Twilio (tutorial gratuito en n8n.io/docs/integrations/twilio).

---

## 📎 Recursos adicionales

| Recurso | Descripción |
|--------|-------------|
| [n8n.io](https://n8n.io) | Plataforma gratuita para automatización visual |
| [n8n Templates](https://n8n.io/templates) | Plantillas listas para usar: “Responder WhatsApp”, “Generar contenido”, etc. |
| [OpenAI API Key](https://platform.openai.com/api-keys) | Para usar ChatGPT en tus flujos |
| [Twilio WhatsApp Sandbox](https://www.tw