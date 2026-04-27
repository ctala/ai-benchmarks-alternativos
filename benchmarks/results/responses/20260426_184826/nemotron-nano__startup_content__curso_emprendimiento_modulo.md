# Nemotron 3 Nano 30B — startup_content/curso_emprendimiento_modulo

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 8.0 | quality: 9.72
- latency_total: 25.774s | tokens_per_second: 88.5
- input_tokens: 250 | output_tokens: 2281
- judge_score: 4.8 | justificación: 

## Respuesta completa

## Módulo 3 – *Automatización con IA: De la idea al flujo de trabajo*  
**Curso:** IA Práctica para Emprendedores  

---  

### 1. Objetivo del módulo  
Al finalizar este módulo podrás identificar oportunidades de automatización dentro de tu startup, diseñar y ejecutar flujos de trabajo impulsados por inteligencia artificial usando plataformas visuales como **n8n**, y medir su impacto en tiempo y recursos. Aprenderás a transformar una idea simple en un proceso totalmente automatizado que atienda a tus clientes, genere contenido para redes y califique leads sin necesidad de programar.

---  

### 2. Contenido teórico  

#### 2.1 ¿Qué es la automatización con IA?  
La automatización con IA combina **reglas de negocio** (qué tareas se deben realizar) con **modelos de inteligencia artificial** que pueden interpretar texto, imágenes, datos estructurados o incluso comportamientos de usuarios. En lugar de que un humano realice tareas repetitivas, la IA decide *cuándo* y *cómo* ejecutarlas, reduciendo errores y liberando tiempo para actividades de mayor valor.

#### 2.2 Herramientas clave  
- **n8n**: plataforma de código abierto, basada en gráficos, que permite crear flujos de trabajo (workflows) conectando APIs, bases de datos, bots de mensajería y modelos de IA sin escribir código.  
- **Zapier / Make (antes Integromat)**: alternativas SaaS con UI similar, útiles para prototipos rápidos.  
- **Servicios de IA accesibles**:  
  - *GPT‑4* (o modelos de lenguaje) para generación de texto.  
  - *Google Vision* o *CLIP* para análisis de imágenes.  
  - *Google Cloud Vision* o *Amazon Rekognition* para detección de objetos.  
  - *Dialogflow* o *Rasa* para chatbots.  

#### 2.3 Principios básicos de un buen flujo de trabajo  
| Paso | Descripción | Pregunta clave |
|------|-------------|----------------|
| **Trigger** | Evento que inicia el flujo (p.ej., llegada de un email, formulario completado). | ¿Qué dispara la automatización? |
| **Condición** | Filtrado o lógica que decide si el flujo procede. | ¿Cuándo se ejecuta exactamente? |
| **Acción IA** | Llamada a un modelo de IA (p.ej., clasificación, generación). | ¿Qué IA aporta valor aquí? |
| **Salida** | Resultado que se guarda, envía o muestra (p.ej., mensaje, registro). | ¿Qué se entrega al usuario o al sistema? |

---  

### 3. 3 ejemplos prácticos de automatización para startups  

| # | Caso de uso | Flujo resumido (IA + n8n) | Beneficio concreto |
|---|-------------|---------------------------|--------------------|
| 1 | **Atención al cliente automatizada** | 1️⃣ Llegada de mensaje en WhatsApp/Email → 2️⃣ n8n detecta trigger → 3️⃣ Modelo de lenguaje genera respuesta (p.ej., “Gracias por tu consulta, ¿en qué más puedo ayudar?”) → 4️⃣ Envía respuesta al canal original. | Responde 24/7, reduce carga del equipo de soporte. |
| 2 | **Generación de contenido para redes sociales** | 1️⃣ Calendario editorial → 2️⃣ n8n programa disparo diario → 3️⃣ GPT‑4 crea borrador de post basado en tema/keyword → 4️⃣ Formatea texto → 5️⃣ Publica automáticamente en Instagram/Facebook vía API. | Publicaciones constantes sin necesidad de redactar manualmente. |
| 3 | **Calificación automática de leads** | 1️⃣ Formulario de captura → 2️⃣ n8n guarda lead en Google Sheet → 3️⃣ Modelo de clasificación evalúa comportamiento (p.ej., frecuencia de visitas, datos demográficos) → 4️⃣ Asigna puntuación → 5️⃣ Si puntuación > umbral, mueve a “Hot Lead” en CRM. | Prioriza leads de mayor probabilidad de cierre, acelera el pipeline de ventas. |

---  

### 4. Ejercicio práctico paso a paso  

**Objetivo del ejercicio:** Crear un flujo en **n8n** que, al recibir un email con un nuevo lead (asunto y cuerpo), clasifique el lead según su nivel de interés y lo guarde en una hoja de Google con la categoría correspondiente.  

#### Paso 0 – Preparación  
1. Regístrate en [n8n.cloud](https://n8n.cloud) (plan gratuito).  
2. Conecta tu cuenta de Gmail y Google Sheets (autoriza permisos).  
3. (Opcional) Regístrate en **Hugging Face** y obtén una API key para usar el modelo *distilbert-base-uncased-finetuned-sst-2-english* (clasificador de sentimiento).  

#### Paso 1 – Crear el trigger  
1. Arrastra un nodo **“Gmail Trigger”** → selecciona **“New Email”**.  
2. Configura el filtro: *subject contains “lead”* (o el label que uses).  

#### Paso 2 – Extraer datos del email  
1. Añade un nodo **“Set”** llamado *extraerDatos* con las siguientes expresiones:  
   - `leadSubject = ${{ $json["subject"] }}`  
   - `leadBody = ${{ $json["body"] }}`  

#### Paso 3 – Llamada al modelo de IA (clasificación)  
1. Arrastra **“HTTP Request”** → método **POST**.  
2. URL: `https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english`  
3. Headers: `Authorization: Bearer <YOUR_HF_TOKEN>` , `Content-Type: application/json`  
4. Body (JSON):  
   ```json
   { "inputs": "{{ $json.leadBody }}" }
   ```  
5. En la respuesta, el campo `label` será **“POSITIVE”** o **“NEGATIVE”**. Usa un nodo **“Function”** para traducir a *Alto/Nbajo interés*:  
   ```js
   var score = $node["HTTP Request"].json.body[0].label === "POSITIVE" ? 1 : 0;
   return [{ json: { interestLevel: score } }];
   ```  

#### Paso 4 – Guardar en Google Sheets  
1. Añade un nodo **“Google Sheets”** → acción **“Append Row”**.  
2. Selecciona la hoja y la hoja destino.  
3. Mapea los campos: `leadSubject`, `leadBody`, `interestLevel`.  

#### Paso 5 – Validar y depurar  
1. Conecta un nodo **“Debug”** antes del último paso para ver el payload completo.  
2. Ejecuta el workflow con un email de prueba.  
3. Verifica que la hoja reciba la fila con la columna *interestLevel* (0 o 1).  

#### Paso 6 – Extender (opcional)  
- Añade una rama **“IF”** que, si `interestLevel = 1`, envíe un email de seguimiento automático.  
- Usa **“Slack”** o **“Discord”** como canal de notificación para el equipo de ventas.  

---  

### 5. Recursos adicionales  

| Tipo | Enlace | Comentario |
|------|--------|------------|
| **Tutorial oficial de n8n** | https://docs.n8n.io/ | Guía completa de nodos y ejemplos. |
| **Curso rápido de n8n (YouTube)** | https://www.youtube.com/watch?v=YvYx8XK5fK8 | 30‑min introducción visual. |
| **Modelos de IA gratuitos en Hugging Face** | https://huggingface.co/models | Busca “sentiment analysis”, “summarization”, etc. |
| **Plantilla de workflow de n8n para leads** | https://github.com/n8n-io/n8n-examples/tree/main/examples/lead-scoring | Importable directamente. |
| **Comunidad Latinoamericana de n8n** | https://discord.com/invite/n8nLatam | Preguntas y ayuda en español. |

---  

### 6. Preguntas de autoevaluación  

1. **¿Cuál es la diferencia entre un *trigger* y una *acción* en un flujo de trabajo de n8n?**  
2. **Menciona dos ventajas de usar un modelo de IA (p.ej., clasificación de texto) dentro de un workflow automatizado.**  
3. **Si tu flujo de automatización falla en la etapa de “Acción IA”, ¿qué pasos deberías revisar antes de volver a ejecutarlo?**  

---  

> **Tip de experto:** Documenta cada nodo con notas breves dentro de n8n (campo “Description”). Así, cuando vuelvas a revisar el flujo después de semanas, entenderás rápidamente su propósito sin tener que desentrañar la lógica de nuevo. ¡Empieza hoy y convierte tu idea en un proceso que trabaje por ti!