# Step 3.5 Flash — startup_content/curso_emprendimiento_modulo

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.72 | quality: 9.72
- latency_total: 31.666s | tokens_per_second: 82.0
- input_tokens: 258 | output_tokens: 2596
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un disenador instruccional especializado en emprendimiento y tecnologia.
Creas contenido educativo practico para emprendedores latinoamericanos.
Tu enfoque es hands-on, con ejercicios aplicables y ejemplos reales.

**user:**

Disena el Modulo 3 de un curso llamado "IA Practica para Emprendedores".

El modulo se titula: "Automatizacion con IA: De la idea al flujo de trabajo"

Incluye:
1. Objetivo del modulo (1 parrafo)
2. Contenido teorico (explicacion de automatizacion con IA, herramientas como N8N)
3. 3 ejemplos practicos de automatizacion para startups:
   - Atencion al cliente automatizada
   - Generacion de contenido para redes sociales
   - Calificacion automatica de leads
4. Ejercicio practico paso a paso (que el alumno pueda seguir)
5. Recursos adicionales
6. Preguntas de autoevaluacion (3 preguntas)

Formato: Markdown con buena estructura. Nivel: Emprendedor no-tecnico.


## Respuesta completa

# Módulo 3: Automatización con IA - De la idea al flujo de trabajo

## 1. Objetivo del módulo
Al finalizar este módulo, habrás aprendido a identificar procesos repetitivos en tu startup que pueden ser automatizados con IA, y serás capaz de diseñar e implementar tu primer flujo de trabajo automatizado utilizando herramientas visuales sin código, ahorrando horas de trabajo manual y escalando operaciones con pocos recursos.

---

## 2. Contenido teórico

### ¿Qué es la automatización con IA?
La **automatización con IA** consiste en usar inteligencia artificial para realizar tareas que normalmente requieren intervención humana, como responder mensajes, clasificar información, generar texto o analizar datos. A diferencia de la automatización tradicional (que solo sigue reglas fijas), la IA puede **aprender y adaptarse**, tomando decisiones basadas en contexto.

**Ejemplo clave**:  
- *Automatización tradicional*: "Si el email contiene la palabra 'precio', reenviar a ventas".  
- *Automatización con IA*: "Analizar el email, detectar la intención de compra, asignar prioridad y responder con un presupuesto personalizado".

### Herramientas visuales sin código: N8N
**N8N** es una plataforma de automatización de código abierto que funciona con nodos (bloques) conectados entre sí. Su ventaja para emprendedores:
- **Interfaz visual**: Arrastrar y soltar nodos.
- **Conectores preconstruidos** para Gmail, Google Sheets, WhatsApp, OpenAI, etc.
- **Precio accesible**: Plan gratuito con 100 ejecuciones/día.
- **Auto-hospedable**: Puedes instalarlo en tu propio servidor para mayor control.

> 💡 **Alternativas**: Zapier (más fácil pero pago), Make (similar a Zapier), Huginn (open source, más técnico).

---

## 3. 3 ejemplos prácticos para startups

### 1. Atención al cliente automatizada
**Problema**: Responder consultas frecuentes consume horas del equipo.  
**Solución**:  
- Usar un **chatbot con IA** (ej: integrando OpenAI en WhatsApp/Línea) que:
  - Reconozca preguntas como "¿Cuánto cuesta?" o "¿Envían a mi país?".
  - Responda desde una base de conocimiento (PDF,网页).
  - Escale a un humano si detecta frustración o preguntas complejas.  
**Herramientas**: N8N + OpenAI API + WhatsApp Business API.

### 2. Generación de contenido para redes sociales
**Problema**: Crear posts diarios para Instagram/LinkedIn es tedioso.  
**Solución**:  
- Automatizar la creación de contenido a partir de:
  - **Fuentes**: Nuevos artículos de tu blog, tendencias de Google Trends.
  - **Proceso**: N8N extrae el texto → lo resume con IA → genera 3 opciones de copy + hashtags → publica en Buffer/Hootsuite.  
**Herramientas**: N8N + OpenAI + Buffer API.

### 3. Calificación automática de leads
**Problema**: Recibes 100+ formularios de contacto y no sabes cuáles son clientes potenciales reales.  
**Solución**:  
- Flujo que:
  1. Toma nuevos leads de Google Forms/Typeform.
  2. Usa IA para analizar respuestas abiertas (ej: "Necesito un software para gestionar inventario").
  3. Asigna una **puntuación (1-10)** basada en coincidencia con tu perfil de cliente ideal.
  4. Envía los leads con alta puntuación a tu CRM (HubSpot, PipeDrive) y notifica al equipo por Slack.  
**Herramientas**: N8N + OpenAI + Google Sheets + Slack.

---

## 4. Ejercicio práctico paso a paso
**Vas a crear un flujo que:**
1. Detecte nuevos correos en Gmail con el asunto "Nuevo pedido".
2. Extraiga el cuerpo del email.
3. Use IA para resumir el pedido en 1 línea.
4. Guarde el resumen en una hoja de Google Sheets.
5. Envíe una respuesta automática al cliente confirmando recepción.

### Requisitos previos:
- Cuenta en [n8n.cloud](https://www.n8n.cloud/) (gratis) o instalar N8n local (recomendado para datos sensibles).
- Cuenta de Gmail y Google Sheets.
- API key de OpenAI (consíguela en [platform.openai.com](https://platform.openai.com/)).

### Pasos:

#### Paso 1: Crear el flujo base
1. En N8n, haz clic en **"New Workflow"**.
2. Arrastra el nodo **"Gmail Trigger"** al canvas.
3. Configúralo:
   - Event: `On New Email`
   - Filter: `Subject contains "Nuevo pedido"` (ajusta a tu caso).

#### Paso 2: Extraer el contenido
1. Conecta el nodo **"Gmail Trigger"** a un nodo **"HTML Extract"**.
2. Configúralo para extraer el `body` del email (elimina HTML si es necesario).

#### Paso 3: Procesar con IA
1. Conecta el nodo anterior a **"OpenAI"**.
2. Configura:
   - Operation: `Complete`
   - Prompt: `"Resume este pedido en una línea para el equipo de ventas: {{ $json.body }}"`  
     (Nota: `{{ $json.body }}` inserta el texto extraído).
   - Model: `gpt-3.5-turbo` (más económico).
   - Max Tokens: `100`.

#### Paso 4: Guardar en Google Sheets
1. Conecta **"OpenAI"** a **"Google Sheets"**.
2. Configura:
   - Operation: `Append`
   - Sheet: Crea una hoja con columnas: `Fecha`, `Resumen IA`, `Email remitente`.
   - Mapea los datos: `{{ $now }}` para fecha, `{{ $json.choices[0].text }}` para el resumen, `{{ $json.from }}` para email.

#### Paso 5: Responder automáticamente
1. Conecta **"OpenAI"** (otra salida) a **"Gmail"**.
2. Configura:
   - Operation: `Send Email`
   - To: `{{ $json.from }}` (el remitente original).
   - Subject: `"Confirmación: Recibimos tu pedido"`
   - Message: `"Hola, hemos recibido tu solicitud y un humano la revisará en menos de 24h. Gracias!"`

#### Paso 6: Probar y activar
1. Haz clic en **"Execute Workflow"**.
2. Envía un email de prueba a tu Gmail con el asunto "Nuevo pedido".
3. Verifica que aparezca en Google Sheets y que recibas la respuesta.
4. Si funciona, activa el flujo con el toggle **"Active"**.

> ⚠️ **Consejo de seguridad**: En producción, añade un nodo de "Error Trigger" para manejar fallos y no uses datos reales de clientes en pruebas.

---

## 5. Recursos adicionales

### Tutoriales video (español)
- [N8N para principiantes - 20 min](https://www.youtube.com/watch?v=...)
- [Automatizar Gmail + OpenAI con N8N](https://www.youtube.com/watch?v=...)

### Plantillas listas para importar
- [Flujo de calificación de leads](https://n8n.io/workflows/...) (importar a N8N).
- [Chatbot para WhatsApp con IA](https://n8n.io/workflows/...).

### Documentación esencial
- [N8N Docs: Guía de inicio](https://docs.n8n.io/)
- [OpenAI API: Guía de prompts](https://platform.openai.com/docs/guides/prompt-engineering)
- [Google Sheets API en N8N](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/)

### Comunidades
- **Foro oficial de N8N** (inglés, muy activo): https://community.n8n.io/
- **Grupo de Telegram "Automatización para Emprendedores"** (comparte flujos en español).

### Próximos pasos sugeridos
1. Añade un nodo de **Slack** para notificar al equipo cuando llegue un lead de alta puntuación.
2. Prueba el nodo **"HTTP Request"** para conectar con APIs personalizadas de tu software.
3. Explora el **nodo "AI Classify"** de N8N para categorizar emails sin escribir prompts.

---

## 6. Preguntas de autoevaluación

1. **Conceptual**: ¿Cuál es la diferencia principal entre automatización tradicional y automatización con IA? Da un ejemplo de cada uno relacionado con atención al cliente.
2. **Aplicación**: Si quieres automatizar la publicación en redes sociales a partir de un blog, ¿qué secuencia de nodos en N8N propondrías? (nombra al menos 4 nodos en orden).
3. **Práctica**: En el ejercicio del módulo, ¿qué harías si el resumen generado por OpenAI es muy largo o incluye información irrelevante? (sugiere 2 ajustes en el prompt o configuración).

---

> **Nota para el instructor**: Recuerda que en workshops presenciales, puedes preparar un "kit de supervivencia" con cuentas de prueba de Gmail/Sheets y una API key de OpenAI con saldo limitado para que los alumnos no tengan obstáculos técnicos iniciales.