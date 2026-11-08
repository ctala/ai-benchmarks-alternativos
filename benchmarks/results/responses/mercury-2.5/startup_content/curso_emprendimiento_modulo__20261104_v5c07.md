# Mercury 2.5 — startup_content/curso_emprendimiento_modulo

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.35 | quality: 9.72
- latency_total: 4.016s | tokens_per_second: 300.8
- input_tokens: 241 | output_tokens: 1208
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

# Módulo 3: Automatización con IA: De la idea al flujo de trabajo

## 1. Objetivo del módulo
Al finalizar este módulo, serás capaz de diseñar e implementar flujos de trabajo automatizados que integren IA para ahorrar tiempo y reducir errores manuales en tu startup. Entenderás cómo conectar herramientas sin código para que tus sistemas trabajen por ti, desde responder clientes hasta generar contenido y priorizar ventas.

---

## 2. Contenido teórico: Automatización con IA

### ¿Qué es la automatización con IA?
La automatización con IA combina tareas repetitivas (como copiar datos o enviar correos) con inteligencia artificial para tomar decisiones o generar contenido sin intervención humana. Por ejemplo, en lugar de leer 50 correos y responder manualmente, una IA puede clasificarlos y redactar respuestas.

### Herramientas clave: N8N
N8N es una plataforma de automatización "low-code" que conecta aplicaciones como Gmail, Slack, WhatsApp, o bases de datos. Funciona con nodos: cada nodo representa una acción (ej. "recibir mensaje", "procesar con IA", "enviar respuesta").  
- **Ventajas**: Es de bajo costo, flexible y visual (puedes ver el flujo como un diagrama).  
- **Ejemplo de flujo**: Cuando llega un lead desde Facebook → N8N envía sus datos a una IA → La IA clasifica su intención → N8N guarda la información en Google Sheets y avisa al equipo en Slack.

---

## 3. Tres ejemplos prácticos para startups

### Ejemplo 1: Atención al cliente automatizada
**Problema**: Demoras en responder consultas comunes (precios, envíos, horarios).  
**Solución**: Usar un chatbot en WhatsApp/Instagram con IA que responde 24/7 y escaloa casos complejos a un humano.  
**Herramientas**: WhatsApp Business API + N8N + LLM (ej. OpenAI o modelos locales).

### Ejemplo 2: Generación de contenido para redes sociales
**Problema**: Falta de tiempo para crear posts, imágenes y textos.  
**Solución**: Automatizar la creación de contenido a partir de un tema o noticia.  
**Herramientas**: RSS feeds de noticias → N8N → IA de texto (copywriting) + IA de imágenes (ej. DALL·E) → Publicación en Meta/LinkedIn.

### Ejemplo 3: Calificación automática de leads
**Problema**: Tu equipo vende sigue leads fríos que no están listos para comprar.  
**Solución**: Clasificar leads según su comportamiento (páginas visitadas, preguntas realizadas) y priorizar los calientes.  
**Herramientas**: Formulario web → N8N → Análisis con IA (clasificar por intención) → Base de datos + notificación en Slack.

---

## 4. Ejercicio práctico paso a paso
**Objetivo**: Crear un flujo que clasifique leads recibidos por correo y los notifique en Slack.

### Paso 1: Preparar el entorno
1. Crea una cuenta gratuita en [n8n.io](https://n8n.io).
2. Conecta tu cuenta de Gmail (en N8N, ve a *Credentials* → *Add credential* → Gmail).
3. Conecta tu cuenta de Slack (en N8N, ve a *Credentials* → *Add credential* → Slack).

### Paso 2: Diseñar el flujo en N8N
1. En el editor de N8N, arrastra los siguientes nodos:
   - **Gmail Trigger**: Configúralo para detectar correos nuevos con el asunto "Solicitud de demo".
   - **HTTP Request (opcional)**: Si necesitas extraer datos de un sitio web del lead.
   - **LLM Node**: Usa un modelo gratuito (ej. Ollama o API de OpenAI) para analizar el texto del correo y responder: "¿Lead caliente o frío?"  
   - **Slack Node**: Envía un mensaje al canal #leads-que con el resultado.

### Paso 3: Probar y depurar
1. Envía un correo de prueba con asunto "Solicitud de demo" y texto: "Estoy interesado en comprar 50 licencias".
2. Verifica que N8N detecte el correo y envíe el resultado a Slack.
3. Ajusta el prompt del LLM si la clasificación no es precisa.

### Paso 4: Automatizar y monitorear
1. Activa el flujo en N8N.
2. Revisa el registro de ejecuciones para asegurar que funcione correctamente cada día.

---

## 5. Recursos adicionales
- [Documentación oficial de N8N](https://docs.n8n.io)
- [Plantillas gratuitas de automatización en N8N](https://n8n.io/workflows)
- [Curso gratuito de automatización con IA en Coursera](https://www.coursera.org)
- [Lista de herramientas de IA gratuitas para emprendedores](https://ai-directory.com)

---

## 6. Preguntas de autoevaluación

1. ¿Cuál es la principal ventaja de usar N8N para automatizar procesos en tu startup?  
2. Nombra un caso de uso donde la IA pueda ayudarte a calificar leads de forma automática.  
3. ¿Qué pasaría si un flujo de automatización falla a la mitad? ¿Cómo podrías prevenirlo?

---

**Siguiente paso**: Aplica este ejercicio a un caso real de tu negocio y comparte los resultados con tu equipo. ¡La automatización es clave para escalar sin aumentar costos!