# Kimi K2.7 Code — startup_content/curso_emprendimiento_modulo

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.83 | quality: 9.44
- latency_total: 349.772s | tokens_per_second: 13.6
- input_tokens: 279 | output_tokens: 4758
- judge_score: 4.6 | justificación: 

## Respuesta completa

 # Módulo 3: Automatización con IA — De la idea al flujo de trabajo

**Curso:** IA Práctica para Emprendedores  
**Nivel:** Emprendedor no técnico  
**Tiempo estimado:** 2 - 3 horas (teoría + ejercicio)

---

## 1. Objetivo del módulo

Al finalizar este módulo serás capaz de identificar tareas repetitivas en tu startup, diseñar flujos de trabajo automatizados con inteligencia artificial y construir tu primera automatización funcional sin escribir código. Entenderás cómo conectar herramientas que ya usas (como Google Forms, WhatsApp, email o redes sociales) con modelos de IA para que trabajen por ti, liberando tiempo para que te enfoques en crecer el negocio.

---

## 2. Contenido teórico

### ¿Qué es automatizar con IA?

Automatizar con IA significa crear una secuencia de pasos que se ejecutan solos cuando ocurre un evento, y que incluyen una decisión o acción inteligente hecha por un modelo de lenguaje.

En lugar de contratar un programador para cada tarea, usas una herramienta **visual** donde arrastras bloques (llamados *nodos*) y los conectas como si fueran piezas de un rompecabezas.

> **Idea simple:**  
> *"Cuando pase X, la IA hace Y y luego envía Z."*

**Ejemplo:**  
> Cuando llega un nuevo mensaje de cliente → la IA lo lee → responde automáticamente o lo deriva a un humano.

### El ciclo de una automatización

| Paso | Qué haces | Ejemplo |
|------|-----------|---------|
| 1. Detectar | Identificar una tarea repetitiva | Responder las mismas preguntas por WhatsApp |
| 2. Mapear | Dibujar el flujo paso a paso | Mensaje → IA → Respuesta o derivación |
| 3. Conectar | Unir las herramientas con una plataforma | n8n + WhatsApp + OpenAI |
| 4. Probar | Ejecutar con datos reales | Enviar un mensaje de prueba |
| 5. Activar | Dejar que corra sola | Encender el flujo |
| 6. Mejorar | Revisar resultados y ajustar | Corregir respuestas incorrectas |

### Herramientas clave

| Herramienta | Qué es | Ideal para |
|-------------|--------|------------|
| **n8n** | Automatización visual *open source*. Tienes control total de tus flujos. | Startups que quieren escalar sin depender de Zapier. |
| **Make** | Plataforma visual tipo n8n, muy popular en Latinoamérica. | Conectar apps rápidamente. |
| **Zapier** | La más conocida, fácil de usar, pero más cara a escala. | Primeras automatizaciones simples. |
| **OpenAI / Claude / Gemini** | Modelos de IA que entienden y generan texto. | Responder, clasificar, resumir, redactar. |

En este módulo usaremos **n8n** como ejemplo principal porque es gratis para empezar y te permite crecer sin pagar de más.

### Conceptos que debes conocer

- **Trigger (disparador):** El evento que inicia el flujo.  
  *Ejemplo:* “Nueva fila en Google Sheets” o “Nuevo correo recibido”.
- **Nodo:** Cada bloque del flujo. Puede ser una app, una acción de IA o una condición.
- **Prompt:** La instrucción que le das a la IA para que haga su trabajo.
- **Condición:** Una regla del tipo “si pasa esto, haz esto otro”.  
  *Ejemplo:* “Si el lead tiene presupuesto alto → notificar a ventas”.

---

## 3. Tres ejemplos prácticos de automatización para startups

### Ejemplo 1: Atención al cliente automatizada

**Contexto:** Tu startup recibe preguntas repetidas por WhatsApp, Instagram o correo: precios, horarios, métodos de pago, estado de envío.

**Flujo propuesto:**

```
Nuevo mensaje del cliente
        ↓
[IA] Analiza la intención y busca la respuesta en tu base de conocimiento
        ↓
¿Puede responder sola?
   Sí → Envía respuesta automática
   No → Crea ticket en Notion / Trello y avisa a un humano
```

**Herramientas:**  
- WhatsApp Business API o Instagram DM  
- n8n  
- OpenAI  
- Google Sheets o Notion (base de conocimiento)

**Resultado esperado:**  
El 70-80% de las preguntas frecuentes se responden solas. Solo los casos complejos llegan a un humano.

---

### Ejemplo 2: Generación de contenido para redes sociales

**Contexto:** Quieres publicar en LinkedIn o Instagram pero no tienes tiempo de crear textos todos los días.

**Flujo propuesto:**

```
Nueva idea en Google Sheets / Notion
        ↓
[IA] Genera 3 opciones de publicación + hashtags + sugerencia de imagen
        ↓
Guarda el borrador en una hoja de aprobación
        ↓
Tú revisas y das "ok"
        ↓
Se programa en Buffer / Metricool
```

**Herramientas:**  
- Google Sheets o Notion  
- n8n  
- OpenAI  
- Buffer, Metricool o LinkedIn directamente

**Resultado esperado:**  
Reduces de 2 horas a 20 minutos la creación semanal de contenido. Mantienes viva tu marca sin contratar a un community manager de inmediato.

---

### Ejemplo 3: Calificación automática de leads

**Contexto:** Llenas un CRM manualmente cada vez que alguien deja sus datos en tu sitio o formulario. Muchos prospectos no son buenos y pierdes tiempo.

**Flujo propuesto:**

```
Nueva respuesta en Google Forms
        ↓
[IA] Lee los datos y clasifica: Frío / Templado / Caliente
        ↓
Escribe la clasificación en Google Sheets
        ↓
Si es "Caliente" → Envía email a ventas + notificación por WhatsApp
Si es "Templado" → Entra a lista de nurturing
Si es "Frío" → No se hace nada por ahora
```

**Herramientas:**  
- Google Forms + Google Sheets  
- n8n  
- OpenAI  
- Email o WhatsApp

**Resultado esperado:**  
Tu equipo de ventas solo atiende leads que realmente valen la pena.

---

## 4. Ejercicio práctico paso a paso

### 🎯 Reto: Construye tu primera automatización de calificación de leads

Al terminar, cada vez que alguien llene tu formulario, la IA clasificará al lead automáticamente y te avisará si es “Caliente”.

---

### Paso 0: Antes de empezar

Necesitas:
- Una cuenta de Google (para Forms y Sheets).
- Una cuenta gratuita en [n8n Cloud](https://www.n8n.io/cloud/) (trial).
- Una cuenta de OpenAI con saldo (puedes cargar desde $5 USD; el uso es muy bajo).

> ⚠️ **Privacidad:** No envíes datos sensibles como números de tarjeta o información médica a modelos de IA de terceros.

---

### Paso 1: Crea tu formulario de captación

1. Abre [Google Forms](https://forms.google.com).
2. Crea un formulario con estas preguntas:
   - Nombre
   - Correo electrónico
   - ¿Qué problema quieres resolver?
   - ¿Cuál es tu presupuesto aproximado? (Bajo / Medio / Alto)
   - ¿En cuánto tiempo planeas decidir? (Inmediato / 1 mes / Más adelante)
3. Guarda las respuestas en una hoja de cálculo de Google Sheets.

---

### Paso 2: Diseña el flujo en papel

Dibuja esto antes de tocar la computadora:

```
Nueva respuesta en Google Forms
            ↓
[IA de OpenAI] clasifica el lead
            ↓
Guarda clasificación en Google Sheets
            ↓
¿Es Caliente?
   Sí → Envía email a ventas
   No → Fin
```

---

### Paso 3: Crea tu cuenta en n8n

1. Entra a [n8n Cloud](https://www.n8n.io/cloud/).
2. Regístrate con tu correo.
3. Crea un nuevo **Workflow** (botón “Add workflow”).

---

### Paso 4: Configura el trigger (el disparador)

1. Agrega un nodo **Google Sheets Trigger**.
2. Conecta tu cuenta de Google.
3. Selecciona la hoja donde se guardan las respuestas del formulario.
4. Elige la opción “Row Added” (fila agregada).
5. Guarda y haz clic en “Test step”.

Si todo está bien, n8n detectará la última respuesta del formulario.

---

### Paso 5: Agrega la IA para clasificar

1. Agrega un nodo **OpenAI**.
2. Conecta tu API Key de OpenAI.
   - Para obtenerla: entra a [platform.openai.com](https://platform.openai.com) → API keys → Create new secret key.
3. En el campo de **prompt** escribe algo como:

```
Eres un asistente de ventas. Clasifica este lead como "Caliente", "Templado" o "Frío".

Reglas:
- Caliente: presupuesto alto y decisión inmediata.
- Templado: presupuesto medio o decisión en 1 mes.
- Frío: presupuesto bajo o decisión indefinida.

Datos del lead:
- Problema: {{$json["¿Qué problema quieres resolver?"]}}
- Presupuesto: {{$json["¿Cuál es tu presupuesto aproximado?"]}}
- Tiempo de decisión: {{$json["¿En cuánto tiempo planeas decidir?"]}}

Responde únicamente con una palabra: Caliente, Templado o Frío.
```

4. Guarda y prueba.

---

### Paso 6: Guarda la clasificación en Google Sheets

1. Agrega un nodo **Google Sheets**.
2. Selecciona la misma hoja.
3. Elige la acción “Update a row”.
4. Indica que quieres escribir la clasificación en una columna vacía (por ejemplo, columna “Clasificación”).

---

### Paso 7: Notifica solo si el lead es Caliente

1. Agrega un nodo **If** (condición).
2. Configura: “Si la clasificación es igual a Caliente”.
3. Si es **sí**, agrega un nodo **Email** o **Slack** para avisar a tu equipo de ventas.
4. Si es **no**, el flujo termina.

---

### Paso 8: Activa y prueba

1. Haz clic en **Save**.
2. Envía una respuesta de prueba desde tu formulario.
3. Revisa que:
   - Se detectó la nueva fila.
   - La IA clasificó correctamente.
   - Se escribió la clasificación en la hoja.
   - Llegó la notificación si era “Caliente”.
4. Cuando todo funcione, activa el flujo con el botón **Active**.

---

### ✅ Checklist de éxito

- [ ] Mi formulario captura datos de calidad.
- [ ] Mi flujo en n8n se ejecuta sin errores.
- [ ] La IA clasifica correctamente en una prueba real.
- [ ] Recibo una notificación cuando el lead es Caliente.
- [ ] Tengo documentado el paso a paso para mi equipo.

---

## 5. Recursos adicionales

| Recurso | Enlace / Descripción |
|---------|----------------------|
| **n8n Cloud** | [https://www.n8n.io/cloud/](https://www.n8n.io/cloud/) — Crea tu cuenta gratuita. |
| **Documentación de n8n** | [https://docs.n8n.io/](https://docs.n8n.io/) — Tutoriales oficiales paso a paso. |
| **OpenAI Platform** | [https://platform.openai.com/](https://platform.openai.com/) — Para obtener tu API Key. |
| **Plantillas de n8n** | Dentro de n8n busca “Workflow Templates” para ver flujos listos. |
| **Comunidad n8n en español** | Busca grupos en Discord y foros oficiales para resolver dudas. |
| **Libro recomendado** | *“Automate This”* de Christopher Steiner — para entender el poder de la automatización en negocios. |
| **Herramienta alternativa** | [Make](https://www.make.com/) — Si prefieres una interfaz similar a n8n. |

---

## 6. Preguntas de autoevaluación

1. **Identificación de oportunidad:**  
   ¿Cuál es una tarea repetitiva de tu startup que hoy consumes tiempo haciendo manualmente y que podrías automatizar con IA? Describe el “antes” y el “después”.

2. **Diseño de flujo:**  
   Si automatizas la atención al cliente, ¿qué preguntas o casos deberían derivarse siempre a un humano? Dibuja o escribe las condiciones.

3. **Aplicación práctica:**  
   Completa la frase con tu propio ejemplo:  
   *“Cuando ocurra __________, la IA hará __________ y luego __________.”*

---

### 🚀 Próximo paso

Comparte tu flujo con un compañero del curso. La mejor forma de aprender automatización es iterar: prueba, mide errores, ajusta el prompt y vuelve a probar.