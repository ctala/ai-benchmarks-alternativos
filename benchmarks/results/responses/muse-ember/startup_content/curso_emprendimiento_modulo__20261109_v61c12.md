# Muse Ember — startup_content/curso_emprendimiento_modulo

- model_id: `meta/muse-ember`
- success: True  | final: 8.84 | quality: 10.0
- latency_total: 12.254s | tokens_per_second: 420.8
- input_tokens: 234 | output_tokens: 5156
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando ejemplos prácticos y una explicación detallada de la automatización con IA, especialmente adecuada para emprendedores.

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
**Curso:** IA Práctica para Emprendedores
**Duración estimada:** 2 a 3 horas
**Nivel:** No técnico. Si sabes usar WhatsApp, Instagram y Google Sheets, puedes hacerlo.

> **La idea de este módulo:** No necesitas contratar un equipo de 5 personas para automatizar tu negocio. Necesitas conectar bien 3 cosas que ya usas.

---

## 1. Objetivo del módulo

Al terminar este módulo serás capaz de diseñar y crear tu primera automatización con IA en n8n, sin escribir código, para ahorrar al menos 5 horas por semana en tareas repetitivas como responder clientes, crear contenido o calificar leads, conectando un disparador simple con el cerebro de una IA y una acción automática en tus herramientas diarias como WhatsApp, Telegram, Instagram o Google Sheets.

## 2. Contenido teórico

### 2.1 ¿Qué es automatizar con IA? En simple

Imagina que tu negocio tiene tareas que se repiten todos los días: responder "¿cuánto cuesta?", crear un post para Instagram, revisar un formulario y decidir si ese cliente es bueno o no.

**Automatización tradicional:** Sigue reglas fijas. Como una calculadora.
*Si el mensaje dice "precio" -> enviar lista de precios.*

**Automatización con IA:** Entiende, lee y decide como un asistente.
*Si el mensaje dice "hola, necesito 24 empanadas para mañana en Surco, ¿llegan?" -> la IA entiende la cantidad, la fecha y la zona, responde personalizado y avisa al dueño.*

La IA no reemplaza tu criterio. Actúa como un empleado digital que trabaja 24/7 en lo repetitivo, mientras tú te enfocas en vender y en los clientes importantes.

### 2.2 Todo flujo tiene 3 piezas

Piensa en un flujo de trabajo como una receta de 3 pasos:

**1. DISPARADOR (Trigger):** Lo que inicia todo.
Ej: Alguien llena un formulario, llega un mensaje de WhatsApp, se crea un archivo en Google Drive.

**2. CEREBRO (IA):** Lo que piensa.
Ej: ChatGPT, Claude o Gemini lee, resume, clasifica, redacta o califica.

**3. ACCIÓN:** Lo que se hace solo.
Ej: Se guarda en una hoja de cálculo, se envía un WhatsApp, se crea un borrador de post, te llega un aviso por Telegram.

Si conectas esas 3 piezas, tienes una automatización.

### 2.3 n8n: Tu herramienta principal (sin tecnicismos)

n8n es una plataforma visual. No escribes código, **conectas bloques como si fueran piezas de LEGO.**

Cada bloque se llama "nodo" y tiene una sola función: recibir información de un lado y pasarla al otro.

Ejemplo visual:
`[Formulario Web] -> [Nodo IA] -> [¿Es cliente A?] -> [Enviar WhatsApp] / [Guardar en Sheets]`

**¿Por qué n8n para emprendedores latinoamericanos?**

| Herramienta | Ideal para | Ventaja | Desventaja |
| :--- | :--- | :--- | :--- |
| **Zapier** | Empezar muy simple | Muy fácil | Caro en dólares, poca IA |
| **Make** | Flujos intermedios | Barato y visual | Curva un poco mayor |
| **n8n** | Flujos con IA potentes | Económico, control total, muchos nodos de IA | Requiere 1 hora para aprender lo básico |

Para este curso usaremos **n8n** porque puedes empezar gratis en su nube, tiene plantillas listas y se conecta con WhatsApp, Instagram, Google, OpenAI y Gemini.

> 💡 **Tip:** La "API" de la que hablan los técnicos es solo una llave de conexión. Es como darle a n8n el permiso para entrar a tu cuenta de OpenAI o Google. La copias y pegas una vez. Nada más.

### 2.4 Regla de oro: Humano en el ciclo

Nunca dejes que la IA publique, venda o responda dinero sin tu revisión al inicio.

Buen flujo: `IA propone -> Tú apruebas con 1 clic -> Se publica/envía`
Mal flujo: `IA publica sola sin control`

Al principio, automatiza el 80% y deja el 20% final para ti. Con el tiempo, ganas confianza.

## 3. Tres ejemplos prácticos para startups

### Ejemplo 1: Atención al cliente automatizada

**Problema real:** Una tienda de cosmética en Chile recibe 60 mensajes al día en Instagram y WhatsApp preguntando lo mismo: precio, stock, envío.

**El flujo:**
1.  **Disparador:** Llega un mensaje a WhatsApp Business.
2.  **Cerebro IA:** Lee el mensaje, busca en tu catálogo (un Google Sheets o Drive) y redacta la respuesta en español chileno, amable y breve.
3.  **Acción:** Responde automáticamente. Si la IA no tiene confianza o el cliente quiere comprar, deriva a un humano y te avisa por Telegram: "Cliente caliente, quiere comprar kit $29.990".

**Resultado:** Respuesta en 10 segundos, incluso a las 11pm. Tú solo intervienes cuando hay intención de compra.

**Herramientas:** WhatsApp Business API (vía n8n), OpenAI/Gemini, Telegram para avisos.

### Ejemplo 2: Generación de contenido para redes sociales

**Problema real:** Una panadería en Perú sabe que debe postear 4 veces por semana, pero no tiene tiempo ni ideas.

**El flujo:**
1.  **Disparador:** Tú escribes una idea rápida en Google Sheets: "Pan de masa madre".
2.  **Cerebro IA:** Genera 3 opciones: titular para Instagram, texto corto, hashtags y un prompt para crear la imagen.
3.  **Acción:** Crea un borrador en Notion o en la misma hoja, con todo listo para que lo apruebes. Al aprobar, se programa en Meta Business Suite.

**Resultado:** De 2 horas creando contenido a 20 minutos revisando borradores.

**Herramientas:** Google Sheets, Gemini/ChatGPT, Notion, Meta Business Suite.

### Ejemplo 3: Calificación automática de leads

**Problema real:** Una agencia B2B en Colombia recibe 30 leads por semana desde Instagram Ads. El vendedor pierde tiempo hablando con curiosos sin presupuesto.

**El flujo:**
1.  **Disparador:** Alguien llena un formulario: nombre, WhatsApp, tipo de negocio, presupuesto mensual, urgencia.
2.  **Cerebro IA:** Analiza el fit. Si presupuesto > $500 USD y urgencia alta, lo califica como **A (100-80 pts)**. Si es dudoso, **B**. Si no tiene presupuesto, **C**.
3.  **Acción:** 
    - **A:** Te avisa al instante por WhatsApp/Telegram y le envía un mensaje automático: "Gracias, un asesor te contactará en 15 min".
    - **B:** Le envía un email con casos de éxito.
    - **C:** Lo guarda en una lista de nutrición para enviarle contenido.

**Resultado:** El vendedor solo habla con leads que sí pueden comprar. Cierre 40% más rápido.

**Herramientas:** Formulario (n8n, Typeform o Instagram), IA, Google Sheets (CRM simple), Telegram/WhatsApp.

## 4. Ejercicio práctico paso a paso

### Tu primera automatización en 45 minutos: Calificador de leads con IA

Vas a crear el Ejemplo 3, pero en versión simple.

**Al final tendrás:** Un link de formulario. Cuando alguien lo llene, la IA lo calificará, lo guardará en Google Sheets y te avisará por Telegram si es un cliente A.

#### Qué necesitas (checklist)

- [ ] Cuenta gratuita en n8n: [n8n.cloud](https://n8n.cloud)
- [ ] Cuenta de Google (para Sheets)
- [ ] Cuenta en Telegram (en tu celular)
- [ ] Una llave API gratuita de Google Gemini (en [aistudio.google.com](https://aistudio.google.com)) o de OpenAI

#### Paso 1: Crea el formulario dentro de n8n (5 min)
1. Entra a n8n > **Create Workflow > Start from scratch**
2. Haz clic en el nodo `+` y busca **Form Trigger**.
3. Configura 4 campos: `Nombre`, `WhatsApp`, `Presupuesto mensual (USD)`, `¿Qué tan urgente necesitas el servicio? (Alta/Media/Baja)`
4. Guarda y copia el link que genera n8n. Ese es tu formulario para compartir.

#### Paso 2: Conecta el cerebro IA (15 min)
1. Después del Form Trigger, agrega un nodo **Google Gemini** (o OpenAI).
2. Conecta tu llave API.
3. Pega este prompt listo para copiar:

```
Eres un calificador de leads experto para una agencia de marketing en Latinoamérica.
Analiza estos datos:
Nombre: {{ Nombre }}
Presupuesto: {{ Presupuesto }}
Urgencia: {{ Urgencia }}

Reglas:
- Presupuesto > 500 y Urgencia Alta = A
- Presupuesto 200-500 = B
- Presupuesto < 200 o Urgencia Baja = C

Devuelve SOLO un JSON válido, sin texto extra, con este formato:
{
  "puntaje": 85,
  "categoria": "A",
  "razon": "Tiene presupuesto y urgencia alta",
  "mensaje_sugerido": "Hola [Nombre], gracias por escribirnos..."
}
```

> No te preocupes por la palabra JSON. Solo significa: "entrégame la respuesta en un formato ordenado que n8n pueda leer".

#### Paso 3: Guarda todo en Google Sheets (10 min)
1. Agrega un nodo **Google Sheets > Append**.
2. Conecta tu Google, crea una hoja nueva llamada "Leads IA".
3. Mapea los campos: Fecha, Nombre, WhatsApp, Presupuesto, Puntaje IA, Categoría, Razón.

#### Paso 4: Avisa solo a los clientes A por Telegram (10 min)
1. Agrega un nodo **IF**. Condición: `Categoría es igual a A`
2. En la rama "true", agrega **Telegram > Send Message**.
3. Para conectarlo: abre Telegram, busca **@BotFather**, escribe `/newbot`, crea tu bot y copia el token. Pégalo en n8n. Luego busca **@userinfobot** para obtener tu Chat ID.
4. Mensaje: `🔥 Nuevo Lead A: {{Nombre}} - Puntaje {{puntaje}} - WhatsApp {{WhatsApp}}`

#### Paso 5: Prueba y activa (5 min)
1. Haz clic en **Execute Workflow**.
2. Llena el formulario tú mismo con datos de prueba (ej: Presupuesto 800, Urgencia Alta).
3. Verifica: ¿Llegó a Sheets? ¿Te llegó el Telegram?
4. Prueba con un Lead C (Presupuesto 50). No debería llegarte el aviso.
5. Si funciona, activa el interruptor **Active** arriba a la derecha.

**✅ Checklist final:** ¿El formulario funciona? ¿La IA califica bien? ¿Se guarda en Sheets? ¿Te avisa solo lo importante?

**Errores comunes:** Si el nodo IA falla, revisa que pegaste bien la llave API. Si Telegram no llega, revisa que hayas iniciado conversación con tu bot antes.

## 5. Recursos adicionales

**Para aprender y copiar plantillas:**
1.  **Plantillas oficiales de n8n:** [n8n.io/workflows](https://n8n.io/workflows) - Busca "lead qualification" o "WhatsApp AI"
2.  **Documentación en español (simple):** [docs.n8n.io/es](https://docs.n8n.io)
3.  **Comunidad n8n en español:** Foro oficial y grupos de Telegram de automatización LatAm
4.  **Google Gemini AI Studio:** [aistudio.google.com](https://aistudio.google.com) - IA gratuita para empezar
5.  **Make Academy (gratis):** Buena alternativa si n8n te resulta complejo al inicio

**Plantilla de este módulo:** Descarga la hoja de cálculo con los prompts de los 3 ejemplos y el checklist imprimible del ejercicio.

## 6. Preguntas de autoevaluación

Responde por escrito. Si no puedes responder la 3, repite el ejercicio.

**1. ¿Cuál es la diferencia clave entre una automatización tradicional y una con IA?**
a) La de IA es más cara
b) La tradicional sigue reglas fijas, la de IA entiende lenguaje, clasifica y redacta
c) No hay diferencia
d) La de IA no necesita herramientas

**2. En el flujo de calificación de leads, ¿qué nodo decide si te avisa por Telegram?**
a) El disparador
b) Google Sheets
c) El nodo IF (condición) que revisa si la categoría es A
d) El formulario

**3. Pregunta de aplicación:** Piensa en tu negocio. Escribe un flujo de 3 pasos (Disparador -> IA -> Acción) que podrías automatizar esta semana y que te ahorraría al menos 2 horas. ¿Qué aprobación humana dejarías al final?

<details>
<summary><strong>Ver respuestas</strong></summary>

1. **B**
2. **C**
3. Ejemplo válido: Disparador: Nuevo comentario en Instagram -> IA: Resume y clasifica si es pregunta, queja o lead -> Acción: Guarda en Sheets y te avisa por Telegram solo si es queja o lead. Aprobación humana: tú respondes personalmente.

</details>

---

**Siguiente paso:** En el Módulo 4 vas a conectar esta automatización con WhatsApp Business para que tus clientes hablen directamente con tu asistente de IA.