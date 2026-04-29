# Step 3.5 Flash (NIM) — startup_content/workshop_outline

- model_id: `stepfun-ai/step-3.5-flash`
- success: True  | final: 7.03 | quality: 9.24
- latency_total: 91.418s | tokens_per_second: 22.4
- input_tokens: 211 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# **Workshop: "Construye tu Asistente de IA para tu Startup"**
### *Para emprendedores early-stage no técnicos - 3 horas*

---

## **1. AGENDA DETALLADA (3 horas)**

| Hora | Bloque | Duración |
|------|--------|----------|
| 0:00 - 0:15 | **Bienvenida + Diagnóstico Rápido** | 15 min |
| 0:15 - 0:45 | **Módulo 1: El ABC de Asistentes de IA para Startups** | 30 min |
| 0:45 - 1:30 | **Módulo 2: Demostración en Vivo - De 0 a Asistente Funcional** | 45 min |
| 1:30 - 1:40 | **Break Rápido + Networking** | 10 min |
| 1:40 - 2:40 | **Módulo 3: ¡Manos a la obra! - Construye tu primer asistente** | 60 min |
| 2:40 - 2:55 | **Módulo 4: Pro-tips, errores comunes y próximos pasos** | 15 min |
| 2:55 - 3:00 | **Cierre, preguntas y recursos** | 5 min |

---

## **2. MATERIALES NECESARIOS (PREPARAR ANTES)**

### **Para el facilitador:**
- Proyector/ pantalla grande
- Presentación en Google Slides (compartir link en chat)
- **Cuenta de prueba creada en n8n** (o Zapier/Make) con flujo pre-armado
- Cuenta de OpenAI con créditos de prueba (o usar modelo local gratuito como Ollama si hay problemas de acceso)
- Ejercicio guiado en PDF (1 página) para entregar
- Lista de enlaces a recursos (Google Drive compartido)

### **Para cada participante (indicar en confirmación del taller):**
- **Laptop** con navegador actualizado
- **Conexión a WiFi** estable
- **Cuenta de Google** (para Google Sheets/Docs)
- **Acceso a n8n.cloud** (registro gratuito previo recomendado)
- **Acceso a OpenAI** (cuenta gratuita) - tener código de regalo de $5 listo por si acaso
- **Archivo de ejemplo** (CSV con 10 leads ficticios) descargable desde link previo

---

## **3. DESGLACE POR BLOQUE**

### **BLOQUE 0: Bienvenida + Diagnóstico Rápido** (15 min)
- **Objetivo:** Romper el hielo, identificar dolores comunes y ajustar expectativas.
- **Dinámica:** 
  - Facilitador: "¡Levanten la mano si han usado ChatGPT para su startup!" (rápido).
  - **Pregunta por mentimeter/chat:** "¿Cuál es tu mayor dolor operativo hoy? (Ventas, Soporte, Contenido, Otro)" - resultados en tiempo real.
  - Presentación de la promesa: "Hoy saldrán con un asistente de IA funcionando para **una tarea concreta** de su negocio".
- **Key takeaway:** "La IA no es magia, es automatización de tareas repetitivas. Hoy empezamos por lo pequeño y útil."

### **MÓDULO 1: El ABC de Asistentes de IA para Startups** (30 min) - *~15 slides*
- **Objetivo:** Entender el concepto de "flujo de trabajo" (workflow) y ver casos reales de startups latinas.
- **Dinámica:** 
  - Charla visual con ejemplos concretos: "Asistente de clasificación de leads", "Asistente de respuesta inicial a客户es", "Asistente de resumen de reuniones".
  - **Analogía:** "Como armar un sándwich: pan (input), ingredientes (procesos), sándwich (output)".
  - Mostrar diagramas simples de flujos (trigger → proceso → acción).
- **Key takeaway:** "Tu asistente no 'piensa', sigue una receta (flujo) que tú diseñas."

### **MÓDULO 2: Demostración en Vivo - De 0 a Asistente Funcional** (45 min) - *~20 slides*
- **Objetivo:** Ver el proceso completo sin tocar nada, para perder el miedo.
- **Dinámica:**
  - **Demo en vivo** (compartir pantalla):
    1. Crear trigger: "Nuevo email en Gmail".
    2. Conectar a OpenAI: "Extraer nombre, empresa, intención del email".
    3. Conectar a Google Sheets: "Guardar en nueva fila".
    4. **¡Flujo activado!** Enviar email de prueba y ver resultado en segundos.
  - Preguntas durante la demo ("¿Qué pasa si el email está en español?", "¿Puedo agregar un paso de revisión humana?").
- **Key takeaway:** "Así de simple es. Los bloques son: 1) Algo pasa, 2) La IA lo procesa, 3) Se guarda/actúa."

### **BREAK** (10 min)
- **Dinámica:** "Busquen a alguien que tenga un dolor operativo distinto al suyo y compártanlo".

### **MÓDULO 3: ¡Manos a la obra! - Construye tu primer asistente** (60 min) - *EJERCICIO PRINCIPAL*
- **Objetivo:** Cada participante crea un flujo funcional para **clasificar leads entrantes por email**.
- **Dinámica:**
  1. **Guía paso a paso** en pantalla (todos siguen en sus laptops):
     - Paso 1: Crear trigger en n8n ("Gmail - Nuevo Email").
     - Paso 2: Añadir nodo "OpenAI - Completion" con prompt predefinido: 
       ```
       "Clasifica este email como: 1) Consulta de precio, 2) Soporte técnico, 3) Propuesta comercial, 4) Spam. 
       Email: {{ $json.body }}. Responde solo con la categoría."
       ```
     - Paso 3: Añadir nodo "Google Sheets - Append" (con hoja de cálculo compartida previamente).
  2. **Ronda de 15 minutos** de trabajo individual con facilitadores circulando.
  3. **Puesta en común rápida:** "¿Quién lo logró? ¿Qué error encontraste?" (compartir pantallas voluntarias).
- **Key takeaway:** "Tu primer flujo ya corre. Mañana puedes cambiar el prompt o la salida."

### **MÓDULO 4: Pro-tips, errores comunes y próximos pasos** (15 min) - *~10 slides*
- **Objetivo:** Evitar tropiezos y escalar el concepto.
- **Dinámica:**
  - Lista de "3 errores que todos cometen" (ej: prompts vagos, no probar con datos reales, olvidar manejar errores).
  - **Pro-tips para startups:**
    - Empezar con 1 flujo, 1 tarea.
    - Usar "human in the loop" (notificación por Slack antes de enviar respuesta automática).
    - Monitoreo: cómo ver logs en n8n.
  - Próximos pasos: "¿Y ahora?" → Plantilla para 5 flujos comunes en startups (