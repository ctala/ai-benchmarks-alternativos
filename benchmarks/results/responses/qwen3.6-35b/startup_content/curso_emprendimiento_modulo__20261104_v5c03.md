# Qwen 3.6 35B base (OpenRouter FP8) — startup_content/curso_emprendimiento_modulo

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 21.626s | tokens_per_second: 103.2
- input_tokens: 234 | output_tokens: 2231
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando ejemplos prácticos y un ejercicio paso a paso que un emprendedor podría implementar directamente.

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

## 1. Objetivo del Módulo

Al finalizar este módulo, serás capaz de identificar tareas repetitivas en tu negocio que consumen tiempo valioso y diseñar flujos de trabajo automatizados utilizando Inteligencia Artificial e herramientas *No-Code* (como n8n). Tu meta principal es liberar al menos 5-10 horas semanales de tu equipo, permitiendo que te enfoques en la estrategia, la venta y la innovación, mientras la máquina se encarga de la ejecución operativa.

---

## 2. Contenido Teórico: ¿Qué es la Automatización con IA?

### El concepto clave: "Conectar los puntos"

La automatización tradicional (como usar Zapier o Make básico) funciona como un robot que sigue instrucciones rígidas: *"Si llega un email, guarda el adjunto en Dropbox"*. Es útil, pero no piensa.

La **automatización con IA** añade una capa de "cerebro" a ese robot. Ahora el sistema puede:
1.  **Entender** texto, imágenes o datos complejos.
2.  **Tomar decisiones** basadas en ese entendimiento (ej: ¿Este cliente está enojado o feliz?).
3.  **Crear contenido** nuevo (ej: Redactar una respuesta personalizada).

### Herramienta Estrella: n8n

Para este curso, utilizaremos **n8n** (pronunciado "n-eight-n"). ¿Por qué?
*   Es *Open Source* (puedes alojarlo tú mismo para mayor seguridad de datos, crucial para startups).
*   Tiene un modelo de precios generoso para empezar.
*   Es más potente que Zapier para flujos complejos y lógicos.
*   Se integra con casi cualquier API (Google Sheets, WhatsApp, Email, CRMs, IA).

**Concepto de "Workflow" (Flujo de trabajo):**
Imagina una fábrica. La materia prima entra por un lado (ej: un formulario de contacto), pasa por estaciones de trabajo (la IA analiza, la IA redacta, el sistema envía email) y sale por el otro lado (un lead calificado en tu CRM). n8n te permite dibujar esa fábrica digitalmente.

---

## 3. 3 Ejemplos Prácticos para Startups

### Ejemplo 1: Atención al Cliente Automatizada (Soporte Nível 1)
*   **Problema:** Pasas horas respondiendo las mismas preguntas frecuentes ("¿Cuál es el precio?", "¿Hacen envíos a México?").
*   **Solución IA:** Un flujo que toma el mensaje del cliente, lo analiza con un LLM (como GPT-4 o Claude), busca la respuesta en tu base de conocimientos (Notion o PDF) y redacta una respuesta empática y precisa.
*   **Valor:** Respuesta inmediata 24/7. Solo escalas a humano si el sentimiento del mensaje es muy negativo o complejo.

### Ejemplo 2: Generación de Contenido para Redes Sociales
*   **Problema:** Necesitas publicar 3 veces por semana en LinkedIn e Instagram, pero no tienes tiempo de escribir copys creativos y diseñar imágenes.
*   **Solución IA:**
    1.  Tú subes un borrador o una idea central a Google Sheets.
    2.  n8n detecta la nueva fila.
    3.  La IA genera 3 versiones del copy (tono profesional, divertido, urgente).
    4.  Otra nodo de IA (DALL-E o Stable Diffusion) crea la imagen basada en el copy.
    5.  Se guarda todo en una carpeta de Drive lista para publicar o se envía a tu Slack para revisión final.

### Ejemplo 3: Calificación Automática de Leads (Lead Scoring)
*   **Problema:** Tu equipo de ventas pierde tiempo hablando con personas que no tienen presupuesto o no son su cliente ideal.
*   **Solución IA:**
    1.  Un nuevo lead llega por tu formulario web.
    2.  La IA analiza la respuesta abierta del formulario ("Busco reducir costos en logística").
    3.  Cruza datos con tu perfil de cliente ideal (ICP).
    4.  Asigna una puntuación (1-100).
    5.  Si la puntuación es >80, crea una tarea urgente en tu CRM y agenda una llamada. Si es <50, lo envía a una secuencia de nurturing por email.

---

## 4. Ejercicio Práctico Paso a Paso: "El Asistente de Lead Qualification"

Vamos a construir un flujo simple que califique a un lead que llega por email y lo organiza en una hoja de cálculo.

**Pre-requisitos:**
*   Cuenta gratuita en [n8n.cloud](https://n8n.io) (o instalación local si tienes servidor).
*   Cuenta de OpenAI (para la API Key de GPT).
*   Una cuenta de Gmail (con acceso a la API de Google o IMAP).
*   Una Google Sheet vacía con columnas: `Nombre`, `Email`, `Intención`, `Puntuación`, `Acción`.

### Paso 1: Configurar los Nodos de Datos
1.  Crea un nuevo Workflow en n8n.
2.  Agrega un nodo **Google Sheets** (Trigger: "On New Row"). *Nota: Para simular, podemos usar un nodo "Schedule" o "Webhook" primero, pero asumamos que el dato viene de un formulario a Sheets.*
3.  Conecta tu cuenta de Google Sheets y selecciona tu hoja.

### Paso 2: Analizar la intención con IA
1.  Agrega un nodo **OpenAI** (Text Completion).
2.  En el prompt, escribe algo como:
    > "Eres un experto en ventas B2B. Lee el siguiente mensaje de un cliente potencial: {{ $json['Mensaje'] }}. Determina si es un lead calificado (tienen presupuesto y urgencia) o no. Responde en formato JSON con dos campos: 'score' (número del 1 al 100) y 'veredicto' (Calificado/No Calificado). Solo responde el JSON."
3.  Conecta la salida del nodo de Sheets (el campo del mensaje) a la entrada del prompt de IA.

### Paso 3: Parsear la respuesta de IA
1.  La IA devuelve texto. Necesitamos convertirlo a datos.
2.  Agrega un nodo **Code** (JavaScript).
3.  Escribe un código simple para extraer el JSON que viene de la IA:
    ```javascript
    const response = items[0].json.output;
    try {
      const data = JSON.parse(response);
      items[0].json.score = data.score;
      items[0].json.veredicto = data.veredicto;
    } catch (e) {
      items[0].json.score = 0;
      items[0].json.veredicto = "Error";
    }
    return items;
    ```

### Paso 4: Actualizar la Base de Datos
1.  Agrega un nodo **Google Sheets** (Action: "Update Row").
2.  Conecta el nodo anterior.
3.  Mapea los campos: Pon el `score` y `veredicto` que acabamos de calcular en las columnas correspondientes de tu hoja de cálculo.

### Paso 5: Activar y Probar
1.  Guarda el workflow.
2.  Actívalo.
3.  Ve a tu Google Sheet y añade una fila manualmente con un mensaje de prueba: *"Hola, tengo urgencia de implementar esto para el lunes, ¿cuánto cuesta?"*.
4.  Revisa tu Sheet. Deberías ver que se ha añadido automáticamente una puntuación alta (ej: 90) y el veredicto "Calificado".

---

## 5. Recursos Adicionales

1.  **Documentación Oficial de n8n:** [docs.n8n.io](https://docs.n8n.io) (Excelente para buscar nodos específicos).
2.  **Galería de Workflows de n8n:** [n8n.io/workflows](https://n8n.io/workflows) (Descarga flujos creados por la comunidad y modifícalos).
3.  **Prompt Engineering for n8n:** Busca guías sobre cómo estructurar prompts para que la IA devuelva siempre JSON (esto es vital para que la automatización no se rompa).
4.  **Comunidad de n8n en Discord:** Muy activa, ideal para pedir ayuda si te atascas con una integración.

---

## 6. Preguntas de Autoevaluación

1.  **¿Cuál es la principal ventaja de usar n8n sobre una herramienta como Zapier para una startup que maneja datos sensibles?**
    *   a) Es más barata siempre.
    *   b) Permite alojar la solución en tu propio servidor (self-hosted) para mayor control de datos y seguridad.
    *   c) Tiene más plantillas prediseñadas.

2.  **En el ejercicio práctico, ¿por qué es crucial que el prompt de la IA solicite una respuesta en formato JSON?**
    *   a) Para que el texto sea más bonito.
    *   b) Porque n8n necesita datos estructurados para poder mapear la "puntuación" y el "veredicto" a las columnas correctas de la hoja de cálculo.
    *   c) Para que la IA hable más rápido.

3.  **Si tu flujo de automatización falla porque la IA devuelve texto en lugar de JSON, ¿qué nodo de n8n te ayuda a corregir o limpiar esos datos antes de guardarlos?**
    *   a) El nodo "Error Handler".
    *   b) El nodo "Code" (JavaScript/Python) para parsear la respuesta.
    *   c) El nodo "Email".

*(Respuestas: 1-b, 2-b, 3-b)*