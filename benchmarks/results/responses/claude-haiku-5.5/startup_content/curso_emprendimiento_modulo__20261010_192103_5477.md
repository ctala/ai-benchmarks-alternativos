# Claude Haiku 5.5 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 43.553s | tokens_per_second: 223.1
- input_tokens: 390 | output_tokens: 9715
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores, cubriendo todos los aspectos solicitados con ejemplos prácticos y explicaciones detalladas.

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

---

## 1. Objetivo del módulo

Al terminar este módulo podrás identificar tareas repetitivas en tu startup que pueden automatizarse, diseñar un flujo de trabajo que las conecte con herramientas de inteligencia artificial y ponerlo en marcha con n8n, sin necesidad de saber programar. Te llevarás un flujo funcional de calificación de leads que podrás adaptar a tu negocio.

---

## 2. Contenido teórico

### 2.1 ¿Qué es automatizar?

Automatizar es configurar un proceso para que se ejecute solo, o casi solo, cuando ocurre un evento. Ejemplos cotidianos:

- Cuando alguien llena un formulario, se guarda su información en una hoja de cálculo.
- Cuando entra una venta, se envía un correo de agradecimiento.
- Cuando un cliente escribe "precio", se le responde con la lista de precios.

Antes, cada una de estas tareas dependía de que alguien las hiciera a mano. Automatizar significa **liberar tiempo humano para lo que requiere criterio**: vender, decidir, crear relaciones.

### 2.2 ¿Qué aporta la IA a la automatización?

La automatización tradicional funciona con reglas fijas: *"si el texto contiene 'precio', responde X"*. Si el cliente escribe *"¿cuánto cuesta para mi cafetería de 30 mesas?"*, la regla falla.

La IA (modelos de lenguaje como GPT, Claude o Gemini) permite:

- **Entender texto libre**: clasificar mensajes, extraer datos, detectar intenciones.
- **Generar texto**: redactar respuestas, publicaciones, resúmenes.
- **Tomar decisiones razonadas**: evaluar si un prospecto es prioritario según varios criterios.

La clave: la IA es el "cerebro" que interpreta, y la automatización es el "sistema nervioso" que mueve la información entre tus herramientas.

### 2.3 Anatomía de un flujo de trabajo

Todo flujo tiene tres partes:

| Elemento | Qué es | Ejemplo |
|---|---|---|
| **Disparador (trigger)** | El evento que inicia el flujo | Llega un formulario, un mensaje de WhatsApp, un horario programado |
| **Pasos de procesamiento** | Transformaciones y decisiones | La IA evalúa el mensaje, un condicional separa casos |
| **Acciones** | Lo que el flujo hace al final | Guardar en una hoja, enviar un correo, notificar al equipo |

Cuando diseñes un flujo, escribe primero en papel: **¿qué dispara? ¿qué necesito decidir? ¿qué debe pasar en cada caso?**

### 2.4 Herramientas principales

| Herramienta | Tipo | Ventaja | Limitación |
|---|---|---|---|
| **n8n** | Visual, código abierto | Flexible, puede alojarse en tu servidor, buena relación costo-beneficio, nodos nativos de IA | Curva de aprendizaje moderada |
| **Make** | Visual, en la nube | Interfaz muy pulida, muchas integraciones | Costo crece con el volumen |
| **Zapier** | Visual, en la nube | Lo más fácil para empezar, miles de integraciones | Más caro a volumen alto, menos flexible en lógica compleja |

Este módulo usa **n8n** porque combina facilidad visual con flexibilidad, y porque su versión en la nube permite comenzar sin instalar nada.

### 2.5 Conceptos clave de n8n

- **Workflow**: el flujo completo. Es un lienzo donde conectas bloques.
- **Nodo**: cada bloque del flujo (un disparador, una acción, una decisión).
- **Conexión**: la línea que une nodos y define el orden.
- **Credencial**: la forma segura en que n8n se conecta a tus cuentas (Gmail, Google Sheets, OpenAI). Se configuran una vez.
- **Expresión**: una forma de usar datos de un nodo en otro, por ejemplo `{{ $json.nombre }}` inserta el nombre que llegó en el formulario.
- **Ejecución**: cada vez que el flujo corre. n8n guarda el historial para que revises qué pasó y por qué.

### 2.6 Buenas prácticas para no-técnicos

1. **Empieza pequeño.** Automatiza una sola tarea antes de encadenar diez.
2. **Prueba con datos ficticios** antes de conectar tus clientes reales.
3. **Mantén un humano en el circuito** en decisiones importantes: la IA sugiere, la persona confirma, especialmente al responder a clientes.
4. **Cuida los datos personales.** Revisa qué información envías a servicios de IA y cumple con la normativa de protección de datos de tu país (por ejemplo, la Ley 1581 en Colombia, la LFPDPPP en México o la Ley 29733 en Perú).
5. **Documenta tu flujo.** Un nombre claro y una nota en el nodo explicando qué hace te ahorrarán horas después.
6. **Revisa las ejecuciones con errores** con frecuencia durante las primeras semanas.

---

## 3. Tres ejemplos prácticos para startups

### Ejemplo 1: Atención al cliente automatizada

**Contexto:** Una tienda online de café de especialidad en Guadalajara recibe 80 mensajes diarios por WhatsApp y Facebook: preguntas de envío, precios, estado de pedidos.

**Flujo:**
1. **Disparador:** llega un mensaje al canal de atención.
2. **IA:** clasifica la intención (`envio`, `precio`, `pedido`, `reclamo`, `otro`) y genera una respuesta con base en la información de tu negocio (políticas, catálogo, horarios).
3. **Condicional:** si la intención es `reclamo` o la IA tiene baja confianza, el mensaje pasa a una persona del equipo.
4. **Acción:** si es una consulta simple, la respuesta se envía automáticamente; si no, se crea una tarea en tu gestor de pendientes.

**Resultado esperado:** la mitad de las consultas se resuelven sin intervención humana y los reclamos llegan más rápido a una persona.

**Punto de atención:** siempre incluye una forma clara de hablar con un humano.

---

### Ejemplo 2: Generación de contenido para redes sociales

**Contexto:** Una marca de cosméticos naturales en Bogotá necesita publicar 5 veces por semana, pero el equipo de marketing es de una sola persona.

**Flujo:**
1. **Disparador:** cada lunes a las 8:00 a. m. (programado).
2. **Lectura:** n8n lee una hoja de cálculo con temas, productos de la semana y la voz de la marca.
3. **IA:** genera 5 borradores de publicación adaptados a cada red (Instagram, Facebook, LinkedIn), con su texto, hashtags y una sugerencia de imagen.
4. **Revisión:** los borradores se guardan en una hoja con estado "pendiente de aprobación".
5. **Acción:** una vez aprobados (cambiando el estado a "aprobado"), otro flujo los programa en la herramienta de publicación.

**Resultado esperado:** pasas de dos horas diarias redactando a veinte minutos revisando y ajustando.

**Punto de atención:** la IA puede inventar datos sobre tus productos. Siempre revisa cifras, certificaciones y promesas.

---

### Ejemplo 3: Calificación automática de leads

**Contexto:** Una agencia de software en Santiago recibe solicitudes de cotización por su web. El equipo comercial pierde tiempo con prospectos que no son viables y responde tarde a los que sí lo son.

**Flujo:**
1. **Disparador:** alguien llena el formulario de contacto.
2. **IA:** evalúa la información según tus criterios (presupuesto, urgencia, tamaño de empresa, necesidad clara) y devuelve un puntaje de 0 a 100, una clasificación (caliente, tibio, frío) y una breve justificación.
3. **Condicional:** si el puntaje es 70 o más, se marca como prioritario.
4. **Acciones:** se registra en tu hoja de prospectos, se notifica por correo al vendedor y, si es caliente, se envía una respuesta inmediata agendando una llamada.

**Resultado esperado:** los leads prioritarios reciben atención en minutos y el equipo se enfoca en las oportunidades reales.

**Punto de atención:** calibra los criterios con tus ventas históricas. Compara durante un mes qué decidió la IA frente a lo que decidió tu equipo.

---

## 4. Ejercicio práctico paso a paso

### Proyecto: Calificador de leads con IA

**Tiempo estimado:** 60 a 90 minutos
**Resultado:** un flujo que recibe solicitudes de contacto, las califica con IA, las guarda en una hoja de cálculo y notifica por correo los prospectos prioritarios.

---

### Paso 0: Preparar lo necesario

Necesitarás:

- [ ] Una cuenta en **n8n Cloud** (ofrece prueba gratuita; revisa las condiciones vigentes en su sitio).
- [ ] Una cuenta de **Google** (para Google Sheets y Gmail).
- [ ] Una **API key de OpenAI** (o de otro proveedor de IA compatible). Requiere agregar saldo; con pruebas de este ejercicio el costo es mínimo.
- [ ] Papel o un documento para anotar tus criterios de lead ideal.

---

### Paso 1: Define tu criterio de "lead ideal"

Antes de tocar herramientas, responde en papel:

1. ¿Qué presupuesto mínimo tiene un cliente ideal? Ejemplo: 2.000 USD.
2. ¿Qué tamaño de empresa te interesa? Ejemplo: entre 5 y 200 empleados.
3. ¿Qué necesidad debe expresar? Ejemplo: "automatizar procesos", "desarrollar una app", "migrar sistemas".
4. ¿Qué urgencia es señal de compra? Ejemplo: "necesito empezar este mes".

Escribe estos criterios en tres o cuatro frases. Los usarás en el prompt de la IA.

---

### Paso 2: Crea la hoja de cálculo

1. Abre **Google Sheets** y crea una hoja llamada **"Leads 2025"** (o el año actual).
2. En la primera fila escribe estos encabezados, uno por columna:

| A | B | C | D | E | F | G | H | I |
|---|---|---|---|---|---|---|---|---|
| Fecha | Nombre | Empresa | Email | Presupuesto | Necesidad | Puntaje | Clasificación | Motivo |

3. Guarda el enlace de la hoja. Lo necesitarás después.

---

### Paso 3: Crea el flujo en n8n

1. Inicia sesión en n8n Cloud y haz clic en **"Create workflow"** (Crear flujo).
2. Ponle nombre en la parte superior: **"Calificador de leads"**.

---

### Paso 4: Agrega el disparador (formulario)

1. Haz clic en el botón **+** para agregar el primer nodo.
2. Busca **"Form Trigger"** (Disparador de formulario).
3. Configura el formulario con estos campos:
   - **Nombre** (texto, obligatorio)
   - **Empresa** (texto, obligatorio)
   - **Email** (email, obligatorio)
   - **Presupuesto aproximado en USD** (lista: "Menos de 1.000", "1.000 a 5.000", "Más de 5.000")
   - **Describe tu necesidad** (texto largo, obligatorio)
4. Copia la **URL del formulario de producción** que aparece en el nodo. Ábrela en otra pestaña y envía un formulario de prueba para verificar que funciona.

---

### Paso 5: Agrega la evaluación con IA

1. Conecta el nodo de formulario con un nuevo nodo: **OpenAI** (acción "Message a model" o "Chat", según la versión de n8n).
2. Configura la credencial con tu API key de OpenAI.
3. Selecciona un modelo económico y capaz (por ejemplo, un modelo "mini" de la familia GPT, según lo disponible en tu cuenta).
4. En el campo de **mensaje del sistema** (instrucciones) pega este prompt, adaptando los criterios del Paso 1:

```text
Eres un analista comercial de una agencia de software en Latinoamérica.
Evalúa la solicitud de un prospecto según estos criterios de lead ideal:
- Presupuesto mayor a 1.000 USD
- Empresa con necesidad clara de software o automatización
- Urgencia de inicio en los próximos 3 meses (si se menciona)

Responde ÚNICAMENTE con un objeto JSON válido, sin texto adicional, con estos campos:
{
  "puntaje": número entero de 0 a 100,
  "clasificacion": "caliente" | "tibio" | "frio",
  "motivo": "explicación en máximo 25 palabras"
}

Reglas:
- Puntaje 70 o más = caliente
- Puntaje entre 40 y 69 = tibio
- Puntaje menor a 40 = frio
- Si la necesidad es vaga o no hay información suficiente, asigna puntaje bajo.
```

5. En el mensaje del usuario, usa las expresiones de n8n para pasar los datos del formulario:

```text
Nombre: {{ $json.Nombre }}
Empresa: {{ $json.Empresa }}
Presupuesto: {{ $json["Presupuesto aproximado en USD"] }}
Necesidad: {{ $json["Describe tu necesidad"] }}
```

> **Nota:** los nombres exactos de los campos (`$json.Nombre`, etc.) dependen de cómo escribiste las etiquetas en el formulario. Si algún valor aparece vacío, revisa en la pestaña de **Input** del nodo cómo se llama cada campo y ajusta la expresión.

---

### Paso 6: Convierte la respuesta en datos utilizables

La IA devuelve texto. Necesitamos separar sus campos.

1. Agrega un nodo **Code** (Código) después de OpenAI, en modo "Run Once for All Items", con JavaScript.
2. Pega este código:

```javascript
const texto = $input.first().json.message?.content
  ?? $input.first().json.text
  ?? $input.first().json.output;

const limpio = texto.replace(/```json|```/g, '').trim();
const evaluacion = JSON.parse(limpio);

return [{
  json: {
    puntaje: evaluacion.puntaje,
    clasificacion: evaluacion.clasificacion,
    motivo: evaluacion.motivo
  }
}];
```

> **Si no entiendes el código:** no es necesario. Basta con saber que este bloque lee la respuesta de la IA y la separa en tres datos. Si aparece un error, verifica en la pestaña de **Output** del nodo de OpenAI cómo llega el texto y ajusta el nombre del campo en la primera línea.

3. Haz clic en **Execute step** para probar. Deberías ver los campos `puntaje`, `clasificacion` y `motivo`.

---

### Paso 7: Guarda el lead en la hoja de cálculo

1. Agrega un nodo **Google Sheets**, acción **Append Row** (Agregar fila).
2. Conecta tu cuenta de Google.
3. Selecciona la hoja **"Leads 2025"**.
4. Mapea cada columna con sus datos. Puedes usar estas expresiones:

| Columna | Valor |
|---|---|
| Fecha | `{{ $now.toFormat('yyyy-MM-dd') }}` |
| Nombre | `{{ $('Form Trigger').item.json.Nombre }}` |
| Empresa | `{{ $('Form Trigger').item.json.Empresa }}` |
| Email | `{{ $('Form Trigger').item.json.Email }}` |
| Presupuesto | `{{ $('Form Trigger').item.json["Presupuesto aproximado en USD"] }}` |
| Necesidad | `{{ $('Form Trigger').item.json["Describe tu necesidad"] }}` |
| Puntaje | `{{ $json.puntaje }}` |
| Clasificación | `{{ $json.clasificacion }}` |
| Motivo | `{{ $json.motivo }}` |

> La expresión `$('Form Trigger')` permite recuperar datos de un nodo anterior aunque ya no estés en ese punto del flujo.

---

### Paso 8: Decide qué hacer con los leads calientes

1. Agrega un nodo **IF** (Condicional) después de Google Sheets.
2. Configura la condición: **`{{ $json.puntaje }}` es mayor o igual a `70`**.
3. Del lado **verdadero** agrega un nodo **Gmail** (acción "Send Message").
   - **Para:** tu correo (o el de tu vendedor).
   - **Asunto:** `🔥 Lead caliente: {{ $('Form Trigger').item.json.Empresa }}`
   - **Cuerpo:**
   ```text
   Nuevo lead prioritario.

   Nombre: {{ $('Form Trigger').item.json.Nombre }}
   Empresa: {{ $('Form Trigger').item.json.Empresa }}
   Email: {{ $('Form Trigger').item.json.Email }}
   Puntaje: {{ $json.puntaje }}
   Motivo: {{ $json.motivo }}

   Contactar en las próximas 2 horas.
   ```
4. Del lado **falso** no agregues nada por ahora. Los leads tibios y fríos quedan registrados en la hoja para revisión periódica.

---

### Paso 9: Prueba el flujo

Envía **tres solicitudes de prueba** desde la URL del formulario:

| Prueba | Datos sugeridos | Resultado esperado |
|---|---|---|
| **Lead fuerte** | Presupuesto "Más de 5.000", necesidad: "Necesito automatizar la facturación de mi empresa de 50 empleados y arrancar este mes" | Puntaje alto, clasificación caliente, correo enviado |
| **Lead medio** | Presupuesto "1.000 a 5.000", necesidad: "Estamos evaluando opciones para mejorar nuestra web" | Puntaje medio, clasificación tibio |
| **Lead débil** | Presupuesto "Menos de 1.000", necesidad: "Hola, quiero info" | Puntaje bajo, clasificación frío |

Para cada prueba revisa:
- [ ] La fila aparece en Google Sheets con todos los datos.
- [ ] El puntaje y la clasificación tienen sentido.
- [ ] El correo llega solo en el caso caliente.

Si algo no coincide con lo esperado, ajusta el prompt del Paso 5 o los criterios.

---

### Paso 10: Activa el flujo

1. En la esquina superior derecha, activa el interruptor **Active** (Activo).
2. Comparte la URL del formulario en tu sitio web o en tu perfil.
3. Revisa las ejecuciones durante la primera semana desde la pestaña **Executions** (Ejecuciones).

**Checklist final:**
- [ ] Formulario funcionando con URL de producción.
- [ ] IA devolviendo JSON válido en todas las pruebas.
- [ ] Hoja de cálculo registrando cada lead.
- [ ] Correo enviado solo a leads calientes.
- [ ] Flujo activo.

---

### Desafío opcional

Agrega un nodo que, para los leads calientes, cree automáticamente un enlace de agendamiento (por ejemplo, con Calendly) y lo incluya en el correo. ¿Qué cambiaría en tu proceso comercial?

---

## 5. Recursos adicionales

**Documentación oficial**
- Documentación de n8n: https://docs.n8n.io
- Plantillas de flujos de n8n (galería pública con ejemplos listos para importar): https://n8n.io/workflows
- Documentación de la API de OpenAI: https://platform.openai.com/docs

**Aprendizaje**
- Cursos gratuitos de n8n en su canal de YouTube y su academia en línea.
- Guía de prompts de OpenAI para extraer datos estructurados (busca "structured outputs").

**Comunidad**
- Foro de la comunidad de n8n, con soporte para principiantes.
- Grupos de automatización e IA para emprendedores en LinkedIn y Facebook en español.

**Herramientas complementarias**
- Google Sheets y Google Forms (gestión de datos básica).
- Calendly o Cal.com (agendamiento).
- Buffer o Metricool (programación de redes sociales).

**Para profundizar en protección de datos**
- Revisa la normativa de tu país y la política de datos del proveedor de IA que uses (qué datos guardan y si entrenan con ellos).

---

## 6. Preguntas de autoevaluación

**Pregunta 1.** Una startup quiere automatizar la respuesta a sus clientes por WhatsApp. ¿Cuál de estos elementos corresponde al *disparador* del flujo?

a) La respuesta enviada al cliente
b) La clasificación de la intención por la IA
c) La llegada de un nuevo mensaje al canal
d) El registro del mensaje en una hoja de cálculo

**Pregunta 2.** ¿Por qué es importante incluir un paso de revisión humana en flujos que generan contenido o responden a clientes, aunque la IA sea muy precisa?

a) Porque las herramientas de automatización no pueden enviar correos
b) Porque la IA puede cometer errores, inventar datos o responder de forma inadecuada, y estos errores afectan la imagen de la marca
c) Porque la ley prohíbe el uso de inteligencia artificial en empresas
d) Porque sin revisión humana el flujo no se puede activar en n8n

**Pregunta 3.** En el ejercicio de calificación de leads, ¿por qué se pide a la IA que responda en formato JSON con campos definidos?

a) Porque el formato JSON es más bonito visualmente
b) Porque permite que n8n separe cada dato (puntaje, clasificación, motivo) y lo use en pasos posteriores de forma confiable
c) Porque OpenAI solo funciona con JSON
d) Porque Google Sheets no acepta texto libre

---

### Respuestas (para instructores)

1. **c)** El disparador es el evento que inicia el flujo: la llegada del mensaje. Las demás opciones son pasos o acciones posteriores.
2. **b)** La IA puede equivocarse o generar información incorrecta, y la revisión humana protege a la marca y a los clientes.
3. **b)** Un formato estructurado permite que el flujo trate cada dato de forma predecible. Si la IA respondiera en texto libre, sería más difícil usar el puntaje en una condición.