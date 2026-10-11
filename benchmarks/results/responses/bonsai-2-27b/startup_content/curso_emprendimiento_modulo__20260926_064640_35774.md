# Bonsai 2 27B — startup_content/curso_emprendimiento_modulo

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 358.985s | tokens_per_second: 30.1
- input_tokens: 270 | output_tokens: 10823
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, cubriendo todos los aspectos solicitados con ejemplos prácticos y un ejercicio detallado.

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

En este módulo aprenderás a convertir tareas repetitivas de tu emprendimiento en flujos automáticos con IA, desde una idea simple hasta un proceso funcional que ahorre tiempo y mejore la experiencia de tus clientes. Entenderás qué es una automatización con IA, cómo funciona una herramienta como **N8N**, y cómo diseñar flujos prácticos para atención al cliente, generación de contenido y calificación de leads. Al final, construirás un flujo real: un sistema que reciba leads nuevos, los califique con IA y los registre automáticamente en Trello, listo para que tu equipo o tú mismo los sigas.

---

## 2. Contenido teórico

### 2.1 ¿Qué es la automatización con IA?

La **automatización** es cuando una tarea se repite sin que tú tengas que hacerla manualmente cada vez. Por ejemplo: cuando un cliente envía un formulario, tú quieres que se cree una tarea, se envíe un correo o se clasifique automáticamente.

La **automatización con IA** suma una capa más: la inteligencia artificial no solo sigue reglas fijas, sino que puede **interpretar texto, clasificar información, resumir, responder, generar ideas o tomar decisiones básicas** sobre datos que le das.

Por ejemplo:

- Una automatización tradicional dice: “Si el cliente escribe *‘envío’*, responder con la información de envíos”.
- Una automatización con IA puede leer un mensaje completo, entender que el cliente pregunta por envíos, devoluciones y tiempos, y responder de forma natural usando el tono de tu marca.

Para un emprendedor, esto significa dejar de depender de respuestas manuales y empezar a crear sistemas que trabajan contigo.

---

### 2.2 El patrón de un flujo de trabajo

Casi toda automatización con IA sigue una estructura simple:

```text
[Disparador] → [Datos] → [IA] → [Acción] → [Medición]
```

1. **Disparador**: algo que inicia el proceso.  
   Ejemplos: una nueva fila en Google Sheets, un formulario enviado, un mensaje en WhatsApp, un comentario en Instagram.

2. **Datos**: la información que el flujo va a usar.  
   Ejemplos: nombre del lead, mensaje del cliente, reseña de un producto, precio, ciudad, fecha.

3. **IA**: la parte donde la inteligencia artificial interpreta o genera algo.  
   Ejemplos: calificar un lead, responder un cliente, generar un post de redes, resumir una reseña.

4. **Acción**: lo que pasa después.  
   Ejemplos: crear una tarjeta en Trello, enviar un correo, guardar en una hoja de cálculo, publicar contenido, notificar por WhatsApp.

5. **Medición**: cómo sabes si el flujo está funcionando.  
   Ejemplos: tiempo de respuesta, cantidad de leads calificados, número de posts generados, tickets resueltos.

La clave no es hacer el sistema más complejo, sino entender claramente:

- ¿Qué problema estoy resolviendo?
- ¿Qué dispara el proceso?
- ¿Qué debe hacer la IA?
- ¿Qué acción sigue?
- ¿Cómo mediré el resultado?

---

### 2.3 N8N: la herramienta para armar tu flujo de trabajo

**N8N** es una herramienta visual que te permite conectar aplicaciones como si fueran piezas de un rompecabezas. En lugar de escribir código, arrastras y conectas “nodos” que representan acciones.

Cada nodo puede hacer una tarea, por ejemplo:

- Recibir datos de Google Forms o Google Sheets.
- Llamar a una IA como Gemini, Claude o OpenAI.
- Crear una tarjeta en Trello.
- Enviar un correo.
- Guardar datos en una base de datos.
- Enviar notificaciones.
- Agendar contenido.

Imagina N8N como un tablero donde tú diseñas el camino que debe seguir tu información.

Ejemplo visual simplificado:

```text
[Google Sheets]
      ↓
[N8N detecta nueva fila]
      ↓
[IA califica el lead]
      ↓
[Trello crea tarjeta]
      ↓
[WhatsApp o correo avisa al equipo]
```

N8N es especialmente útil para emprendedores no técnicos porque:

- Es visual.
- No necesitas saber programar para crear flujos básicos.
- Puedes conectar muchas herramientas populares.
- Puedes empezar con flujos pequeños y luego crecer.
- Es flexible: puedes automatizar procesos internos y externos.

Una idea importante: **N8N no reemplaza a la IA, sino que le da un camino**. La IA piensa o genera; N8N mueve esa información a donde debe ir.

---

### 2.4 Principios para automatizar sin complicarte

Antes de crear flujos, aplica estas reglas:

1. **Automatiza lo que ya entiendes.**  
   Si no sabes cómo resolver una tarea manualmente, no intentes automatizarla todavía.

2. **Empieza con un flujo pequeño.**  
   No intentes automatizar toda tu empresa en un día. Empieza por un proceso claro.

3. **Mide desde el inicio.**  
   Si no mides, no sabrás si el flujo te está ahorrando tiempo o generando errores.

4. **No expongas datos sensibles innecesariamente.**  
   Evita enviar contraseñas, datos bancarios completos o información muy privada a herramientas de IA sin protegerlos.

5. **Deja un humano en el control cuando sea importante.**  
   La IA puede sugerir, clasificar o responder, pero decisiones delicadas o de alta confianza deben revisarse por una persona.

6. **Documenta el flujo.**  
   Escribe qué hace cada nodo, quién lo revisa y qué hacer si falla.

---

## 3. Ejemplos prácticos de automatización para startups

---

### 3.1 Atención al cliente automatizada

#### Problema común

Muchas startups pierden tiempo respondiendo mensajes repetitivos:

- “¿Hacen envíos a Bogotá?”
- “¿Cuánto tarda el envío?”
- “¿Aceptan tarjeta o solo efectivo?”
- “¿Cuál es el precio del plan mensual?”
- “¿Tienen garantía?”

Estas preguntas se repiten todos los días. Si se responden manualmente, consumen tiempo que podías usar para vender, crear o mejorar el producto.

#### Flujo de automatización

```text
Mensaje del cliente
      ↓
Bot de IA lee el mensaje
      ↓
IA responde con información de la empresa
      ↓
Si el cliente no queda satisfecho o pide humano:
      ↓
Notifica al equipo de soporte
      ↓
El cliente queda registrado
```

#### Ejemplo real para una startup

Imagina una tienda de ropa en línea en Medellín. Recibe muchos mensajes por WhatsApp o chat web preguntando por tallas, envíos y devoluciones.

Con una automatización con IA:

1. El cliente escribe: “Hola, ¿tienes talla M y cuándo llega a Barranquilla?”
2. La IA responde: “Hola, sí tenemos talla M. El envío a Barranquilla tarda entre 2 y 3 días hábiles. ¿Quieres que te envíe el link para completar tu pedido?”
3. Si el cliente escribe: “Necesito hablar con alguien porque tengo un problema con mi pedido”, la IA no intenta resolver un caso complejo. En cambio, dice: “Claro, te conecto con nuestro equipo de atención. Un momento por favor” y envía una alerta al soporte.

#### Prompt de IA para atención al cliente

```text
Actúa como asistente de atención al cliente de una tienda de ropa en línea.
Tu tono debe ser cálido, claro y profesional.
Responde solo con la información que tengas disponible.
Si el cliente pregunta por algo que no sabes, di que lo consultarás con el equipo.
Si el cliente pide hablar con un humano, no intentes resolver; di que lo conectarás con una persona.
Responde en máximo 3 líneas.
```

#### Indicadores para medir el flujo

- Tiempo promedio de respuesta.
- Porcentaje de mensajes resueltos por IA.
- Cantidad de casos escalados a humanos.
- Satisfacción del cliente.
- Número de tickets o mensajes que dejaron de ser repetitivos.

#### Beneficio principal

La IA atiende las preguntas frecuentes, mientras tu equipo se enfoca en casos complejos y ventas.

---

### 3.2 Generación de contenido para redes sociales

#### Problema común

Las startups necesitan publicar contenido constante, pero el equipo no tiene tiempo para crear posts todos los días.

Ejemplos de contenido útil:

- Testimonios de clientes.
- Beneficios del producto.
- Errores comunes en el sector.
- Tips rápidos.
- Historias de clientes.
- Promociones.
- Consejos de uso.

#### Flujo de automatización

```text
Nueva reseña o feedback del cliente
      ↓
IA extrae lo más valioso
      ↓
IA genera ideas de contenido
      ↓
Se guardan en una hoja de cálculo o agenda
      ↓
Un humano revisa y publica
```

#### Ejemplo real para una startup

Imagina una marca de café en línea en la Ciudad de México. Cada semana recibe reseñas en Google, Instagram o correo.

Una reseña dice:

> “Me encanta el café de origen. El sabor es muy suave y me sirvió mucho para trabajar sin dormir. Lo recomiendo.”

El flujo automático puede convertir esa reseña en varios contenidos:

1. **Post de Instagram:**  
   “¿Buscas café para tu jornada de trabajo? Este cliente lo usa para rendir mejor. Descubre por qué se ha vuelto parte de su rutina.”

2. **Historia:**  
   “Testimonio real: ‘Me sirvió mucho para trabajar sin dormir’. ¿Qué café te ayuda a rendir?”

3. **Post para Facebook:**  
   “Nuestros clientes no solo disfrutan el sabor, también lo usan para mejorar su productividad. Conoce el café que puede acompañarte en tu día a día.”

4. **Correo o newsletter:**  
   “Un cliente nos dijo que este café le ayudó a trabajar mejor. Descubre por qué.”

#### Prompt de IA para generación de contenido

```text
Actúa como estratega de contenido para redes sociales de una startup de café.
Usa la reseña del cliente que te doy.
Genera 5 piezas de contenido diferentes:
1. Un post de Instagram.
2. Una historia de Instagram.
3. Un post para Facebook.
4. Un correo breve.
5. Una idea para video corto.
El tono debe ser cercano, motivador y natural.
No inventes datos que no estén en la reseña.
Cada pieza debe tener máximo 3 líneas.
```

#### Indicadores para medir el flujo

- Cantidad de ideas de contenido generadas por semana.
- Tiempo que se ahorra en creación de contenido.
- Alcance de los posts.
- Engagement: likes, comentarios, guardados, compartidos.
- Tasa de conversión: clics al sitio, pedidos, registros.

#### Beneficio principal

La IA ayuda a convertir feedback real en contenido, mientras un humano mantiene la identidad de la marca y publica con criterio.

---

### 3.3 Calificación automática de leads

#### Problema común

Cuando una startup recibe leads, no todos tienen la misma intención de comprar. Algunos están listos para comprar, otros solo están investigando y otros pueden no ser relevantes.

Si el equipo trata a todos igual, pierde tiempo.

#### Flujo de automatización

```text
Lead entra por formulario
      ↓
Datos se guardan en Google Sheets
      ↓
IA revisa nombre, email, producto, presupuesto, plazo y mensaje
      ↓
IA asigna puntaje de calificación
      ↓
Trello crea una tarjeta con la calificación
      ↓
Si es lead caliente, se envía alerta al equipo
```

#### Ejemplo real para una startup

Imagina una consultoría de tecnología en Buenos Aires. Recibe leads por un formulario con preguntas como:

- Nombre
- Email
- Empresa
- Producto de interés
- Presupuesto aproximado
- Plazo
- Mensaje

Un lead escribe:

```text
Nombre: Mariana
Email: mariana@empresa.com
Empresa: Startups Andina
Producto: Plan de automatización de ventas
Presupuesto: USD 3.000
Plazo: Este mes
Mensaje: Necesitamos automatizar el seguimiento de clientes porque estamos perdiendo oportunidades.
```

La IA puede calificar ese lead así:

```json
{
  "score": 88,
  "reason": "El lead tiene presupuesto, plazo claro y describe un problema concreto que puede resolverse con el servicio.",
  "next_step": "Contactar en 24 horas",
  "priority": "Alta"
}
```

Otro lead escribe:

```text
Nombre: Carlos
Email: carlos@ejemplo.com
Empresa: Sin empresa
Producto: Conocer más
Presupuesto: No tengo claro
Plazo: En algún momento
Mensaje: Solo quiero información general.
```

La IA puede calificar:

```json
{
  "score": 32,
  "reason": "El lead no tiene presupuesto definido ni plazo claro. Su interés es general.",
  "next_step": "Enviar contenido educativo y seguir en seguimiento frío",
  "priority": "Baja"
}
```

#### Prompt de IA para calificar leads

```text
Actúa como asistente de ventas para una startup de servicios.
Tengo un lead nuevo con los siguientes datos:
Nombre: {{nombre}}
Email: {{email}}
Empresa: {{empresa}}
Producto de interés: {{producto}}
Presupuesto: {{presupuesto}}
Plazo: {{plazo}}
Mensaje: {{mensaje}}

Califica la intención de compra de este lead del 0 al 100.
Considera: claridad del problema, presupuesto, plazo, interés real y urgencia.
Devuelve solo JSON válido con este formato:
{
  "score": 0-100,
  "reason": "breve explicación",
  "next_step": "acción recomendada",
  "priority": "Alta, Media o Baja"
}
```

#### Indicadores para medir el flujo

- Porcentaje de leads calificados en menos de 5 minutos.
- Tiempo de respuesta al primer contacto.
- Número de leads calientes identificados.
- Conversión de leads en clientes.
- Tiempo que el equipo dedica a revisar leads.

#### Beneficio principal

El equipo de ventas se enfoca primero en los leads con mayor probabilidad de comprar, y no pierde tiempo en contactos fríos.

---

## 4. Ejercicio práctico paso a paso

# Ejercicio: Calificador automático de leads con N8N, Google Sheets, IA y Trello

En este ejercicio vas a crear un flujo que haga lo siguiente:

1. Detecte una nueva fila en Google Sheets.
2. Envíe esa fila a una IA.
3. La IA califique el lead del 0 al 100.
4. N8N cree una tarjeta en Trello.
5. La tarjeta incluya el puntaje, la razón y el siguiente paso.

Este ejercicio es ideal si quieres entender cómo funciona un flujo real sin necesidad de saber programar.

---

### 4.1 Resultado del ejercicio

Al terminar, tendrás un flujo automático que:

- Recibe leads nuevos desde Google Sheets.
- Califica cada lead con IA.
- Crea una tarjeta en Trello.
- Te permite ver de inmediato qué leads son calientes, tibios o fríos.

---

### 4.2 Duración estimada

Entre **45 y 75 minutos**, dependiendo de si ya tienes cuentas o necesitas crearlas.

---

### 4.3 Herramientas que necesitas

1. **N8N**
   - Puedes usar N8N Cloud o una versión local si te la proporcionan.

2. **Google Sheets**
   - Para guardar los leads.

3. **Google Forms**
   - Opcional, para crear un formulario que guarde respuestas en Google Sheets.

4. **Trello**
   - Para registrar las tarjetas de leads.

5. **API de IA**
   - Puedes usar Gemini, OpenAI, Claude u otra IA que tengas disponible.
   - Necesitarás una clave de API o acceso desde N8N.

---

### 4.4 Preparación

#### Paso 1: Crea tu hoja de Google Sheets

Crea una hoja de cálculo con el nombre **Leads**.

Agrega estas columnas:

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| Nombre | Email | Producto | Presupuesto | Plazo | Mensaje |

Deja la primera fila como encabezados.

Ejemplo de una fila:

| Nombre | Email | Producto | Presupuesto | Plazo | Mensaje |
|---|---|---|---|---|---|
| Mariana | mariana@ejemplo.com | Automatización de ventas | USD 3.000 | Este mes | Necesitamos automatizar el seguimiento de clientes. |

---

#### Paso 2: Crea una lista en Trello

Crea un tablero en Trello llamado **Leads**.

Dentro del tablero, crea una lista llamada **Leads Nuevos**.

Puedes agregar etiquetas si quieres:

- Caliente
- Tibio
- Frío
- Pendiente de revisión

---

#### Paso 3: Crea tu cuenta de N8N

Inicia sesión en N8N.

Si no tienes cuenta, créala.

Si usas N8N Cloud, verifica que tengas acceso para crear integraciones con Google Sheets, Trello y IA.

---

## Paso a paso del flujo

### Paso 4: Crea el flujo en N8N

1. En N8N, haz clic en **Create workflow**.
2. Nómbralo: **Calificador de Leads con IA**.
3. Verás un lienzo vacío.

---

### Paso 5: Agrega el nodo de Google Sheets

1. Busca el nodo **Google Sheets**.
2. Arrástralo al lienzo.
3. Haz clic en el nodo.
4. Conecta tu cuenta de Google.
5. Elige tu cuenta de Google.
6. Autoriza el acceso si te lo pide.
7. Selecciona la hoja de cálculo **Leads**.
8. En la configuración del disparador, elige:
   - Modo: **Watch for new rows** o **Detect new rows**, según tu versión.
   - Hoja: **Leads**.
9. Guarda el nodo.

Este nodo se encargará de detectar cuando alguien agregue una nueva fila a tu hoja.

---

### Paso 6: Agrega el nodo de IA

1. Busca el nodo de IA disponible en tu N8N.
   - Puede llamarse **AI**, **Gemini**, **Claude**, **OpenAI**, **LLM**, etc.
2. Arrástralo después del nodo de Google Sheets.
3. Conecta el nodo de Google Sheets al nodo de IA.
4. En el nodo de IA, escribe el siguiente prompt:

```text
Actúa como asistente de ventas para una startup de servicios.
Tengo un lead nuevo con los siguientes datos:
Nombre: {{item.json.Nombre}}
Email: {{item.json.Email}}
Producto de interés: {{item.json.Producto}}
Presupuesto: {{item.json.Presupuesto}}
Plazo: {{item.json.Plaz}}
Mensaje: {{item.json.Mensaje}}

Califica la intención de compra de este lead del 0 al 100.
Considera: claridad del problema, presupuesto, plazo, interés real y urgencia.
Devuelve solo JSON válido con este formato:
{
  "score": 0-100,
  "reason": "breve explicación",
  "next_step": "acción recomendada",
  "priority": "Alta, Media o Baja"
}
```

> Nota: Si tu versión de N8N muestra los nombres de las columnas de otra forma, ajusta los campos entre `{{ }}` para que coincidan con los encabezados de tu Google Sheets.

---

### Paso 7: Agrega un nodo para organizar la respuesta

1. Busca el nodo **Set** o **Code**.
2. Arrástralo después del nodo de IA.
3. Conecta el nodo de IA al nodo Set.
4. En el nodo Set, crea campos nuevos:
   - `score`
   - `reason`
   - `next_step`
   - `priority`

Si usas **Set**, puedes indicar que cada campo venga de la respuesta JSON de la IA.

Si usas **Code**, puedes usar una lógica simple para extraer los campos.

Ejemplo conceptual:

```text
score = respuesta.json.score
reason = respuesta.json.reason
next_step = respuesta.json.next_step
priority = respuesta.json.priority
```

Este paso es importante porque el nodo de Trello necesita datos claros para crear la tarjeta.

---

### Paso 8: Agrega el nodo de Trello

1. Busca el nodo **Trello**.
2. Arrástralo después del nodo Set.
3. Conecta el nodo Set al nodo de Trello.
4. Conecta tu cuenta de Trello.
5. Autoriza el acceso.
6. Elige el tablero: **Leads**.
7. Elige la lista: **Leads Nuevos**.
8. En la acción, selecciona **Create card**.
9. Configura el título de la tarjeta así:

```text
Lead: {{item.json.Nombre}} - {{item.json.priority}}
```

10. En la descripción de la tarjeta, escribe:

```text
Puntaje: {{item.json.score}}
Motivo: {{item.json.reason}}
Siguiente paso: {{item.json.next_step}}

Datos:
Nombre: {{item.json.Nombre}}
Email: {{item.json.Email}}
Producto: {{item.json.Producto}}
Presupuesto: {{item.json.Presupuesto}}
Plazo: {{item.json.Plaz}}
Mensaje: {{item.json.Mensaje}}
```

11. Guarda el flujo.

---

### Paso 9: Prueba el flujo

1. Ve a tu Google Sheets.
2. Agrega una fila nueva en la hoja **Leads**.
3. Espera unos segundos.
4. En N8N, revisa el flujo.
5. Deberías ver una ejecución.
6. Ve a Trello.
7. En la lista **Leads Nuevos**, debe aparecer una tarjeta nueva.

Ejemplo de tarjeta:

**Título:**

```text
Lead: Mariana - Alta
```

**Descripción:**

```text
Puntaje: 88
Motivo: El lead tiene presupuesto, plazo claro y describe un problema concreto.
Siguiente paso: Contactar en 24 horas

Datos:
Nombre: Mariana
Email: mariana@ejemplo.com
Producto: Automatización de ventas
Presupuesto: USD 3.000
Plazo: Este mes
Mensaje: Necesitamos automatizar el seguimiento de clientes.
```

---

### Paso 10: Agrega una mejora opcional

Una vez que el flujo básico funcione, puedes agregar una mejora.

#### Opción A: Crear una segunda lista para leads calientes

1. En Trello, crea una lista llamada **Leads Calientes**.
2. En N8N, agrega un nodo **If**.
3. Configura la condición:

```text
Si item.json.score es mayor o igual a 70
```

4. Si es verdadero, crea la tarjeta en **Leads Calientes**.
5. Si es falso, crea la tarjeta en **Leads Nuevos**.

#### Opción B: Enviar una notificación por correo o WhatsApp

1. Agrega un nodo de correo o mensajería.
2. Configura la acción solo si:

```text
score >= 70
```

3. El mensaje puede ser:

```text
Nuevo lead caliente:
Nombre: Mariana
Puntaje: 88
Siguiente paso: Contactar en 24 horas
```

#### Opción C: Guardar la calificación en Google Sheets

1. Agrega un nodo de Google Sheets.
2. Crea una nueva hoja llamada **Calificaciones**.
3. Guarda:
   - Nombre
   - Email
   - Score
   - Reason
   - Next step
   - Priority

---

## 4.5 Errores comunes y cómo resolverlos

### Error 1: El flujo no detecta la nueva fila

**Posibles causas:**

- No estás usando el modo correcto en Google Sheets.
- La fila no tiene todos los datos.
- El encabezado no coincide.
- El flujo no está activo.

**Solución:**

- Verifica que la primera fila tenga los encabezados correctos.
- Asegúrate de que el flujo esté activo.
- Prueba con una fila completa.
- Revisa los logs de ejecución en N8N.

---

### Error 2: La IA devuelve texto en lugar de JSON

**Ejemplo:**

```text
El lead parece caliente porque tiene presupuesto y plazo.
```

**Solución:**

Mejora el prompt:

```text
No escribas texto normal.
Devuelve únicamente JSON válido.
No agregues explicaciones fuera del JSON.
```

---

### Error 3: El nodo de Trello no crea la tarjeta

**Posibles causas:**

- No se conectó correctamente la cuenta de Trello.
- El tablero o la lista no se seleccionaron bien.
- El título o la descripción están vacíos.
- Hay un error en los campos JSON.

**Solución:**

- Revisa la conexión de Trello.
- Verifica que el título tenga datos.
- Revisa la última ejecución en N8N.
- Asegúrate de que los nombres de las columnas coincidan.

---

### Error 4: El flujo tarda mucho

**Posibles causas:**

- La IA está procesando texto largo.
- El prompt es muy complejo.
- El flujo tiene muchas acciones.
- La conexión tiene problemas.

**Solución:**

- Reduce el texto que envías a la IA.
- Pide respuestas cortas.
- Elimina acciones innecesarias.
- Prueba con datos simples.

---

## 4.6 Checklist para tu primer flujo

Antes de publicar o usar el flujo, revisa:

- [ ] El flujo tiene un nombre claro.
- [ ] El disparador está funcionando.
- [ ] Los datos de entrada están completos.
- [ ] El prompt de IA es claro.
- [ ] La IA devuelve JSON válido.
- [ ] El nodo de Trello crea la tarjeta.
- [ ] La tarjeta tiene título y descripción.
- [ ] Probaste con al menos 3 leads diferentes.
- [ ] Definiste quién revisa los leads calientes.
- [ ] Tienes una forma de medir si el flujo funciona.

---

## 5. Recursos adicionales

### 5.1 Plantilla de flujo N8N

Busca o crea una plantilla con este nombre:

```text
Calificador de leads con IA
```

La plantilla debe incluir:

- Google Sheets
- AI / LLM
- Set
- Trello
- If opcional
- Notificación opcional

Si no encuentras una plantilla lista, puedes usar el ejercicio del módulo como base.

---

### 5.2 Prompts recomendados

#### Prompt para atención al cliente

```text
Actúa como asistente de atención al cliente de mi empresa.
Mi empresa vende [producto o servicio].
Mi tono de voz es cálido, claro y profesional.
Responde al cliente usando solo la información que te doy.
Si no tienes información, di que lo consultarás con el equipo.
Si el cliente pide hablar con un humano, no intentes resolver; di que lo conectarás con una persona.
Máximo 3 líneas.
```

#### Prompt para contenido de redes

```text
Actúa como estratega de contenido para una startup de [industria].
Usa la reseña del cliente que te doy.
Genera 5 piezas de contenido:
1. Post de Instagram.
2. Historia.
3. Post de Facebook.
4. Correo breve.
5. Idea para video corto.
El tono debe ser cercano y natural.
No inventes datos.
Cada pieza debe tener máximo 3 líneas.
```

#### Prompt para calificar leads

```text
Actúa como asistente de ventas para una startup de servicios.
Califica la intención de compra de un lead del 0 al 100.
Considera: claridad del problema, presupuesto, plazo, interés real y urgencia.
Devuelve solo JSON válido con este formato:
{
  "score": 0-100,
  "reason": "breve explicación",
  "next_step": "acción recomendada",
  "priority": "Alta, Media o Baja"
}
```

---

### 5.3 Checklist para diseñar un flujo

Usa esta plantilla:

```text
Problema que quiero resolver:
____________________

Disparador:
____________________

Datos necesarios:
____________________

Qué debe hacer la IA:
____________________

Qué acción sigue después:
____________________

Métrica para medir éxito:
____________________

Riesgos posibles:
____________________
```

---

### 5.4 Glossario rápido

| Termo | Explicación simple |
|---|---|
| Automatización | Hacer que una tarea se repita sin intervención manual. |
| IA generativa | IA que crea texto, ideas, respuestas o contenido. |
| Flujo de trabajo | Camino que sigue la información desde el inicio hasta el resultado. |
| Disparador | Lo que inicia el flujo. |
| Nodo | Una acción dentro de N8N. |
| API | Puerta de conexión entre aplicaciones. |
| JSON | Formato estructurado para enviar datos. |
| Lead | Persona o empresa interesada en tu producto o servicio. |
| Calificación de leads | Clasificar qué leads tienen mayor probabilidad de comprar. |
| Escalamiento | Pasar un caso a un humano cuando la IA no debe resolverlo. |

---

### 5.5 Ideas de flujos para practicar después

Una vez que domines el flujo de leads, puedes crear:

1. **Flujo de reseñas a contenido.**
2. **Flujo de soporte con IA.**
3. **Flujo de seguimiento de leads fríos.**
4. **Flujo de publicación de contenido.**
5. **Flujo de reportes semanales automáticos.**
6. **Flujo de análisis de comentarios en redes.**
7. **Flujo de clasificación de correos entrantes.**
8. **Flujo de generación de ideas de marketing.**

---

## 6. Preguntas de autoevaluación

### Pregunta 1

¿Cuál es la diferencia principal entre una automatización tradicional y una automatización con IA?

### Pregunta 2

Si tu flujo de calificación de leads devuelve un texto largo de la IA en lugar de un JSON válido, ¿qué pasos tomarías para corregirlo?

### Pregunta 3

Si implementas un flujo de atención al cliente automatizada, ¿qué tres indicadores usarías para saber si está funcionando bien?

---

## Respuestas sugeridas

### Respuesta 1

Una automatización tradicional sigue reglas fijas, por ejemplo: “si el cliente escribe *envío*, responder con esta información”. Una automatización con IA puede interpretar el lenguaje, entender el contexto, clasificar la intención del cliente, generar respuestas o ideas y tomar decisiones básicas sobre la información que recibe.

### Respuesta 2

Primero revisaría el prompt para dejar claro que la IA debe responder únicamente en JSON válido. Luego agregaría instrucciones como “no agregues texto fuera del JSON” y “usa exactamente este formato”. Después probaría con varios ejemplos de leads, revisaría las respuestas y ajustaría el prompt si la IA sigue agregando explicaciones innecesarias.

### Respuesta 3

Usaría tres indicadores:

1. **Tiempo de respuesta promedio**, para saber si el bot responde más rápido que un humano.
2. **Porcentaje de mensajes resueltos por IA**, para entender cuántos casos no necesitan intervención humana.
3. **Tasa de escalado a humanos**, para verificar si el bot sabe identificar cuándo el cliente necesita una persona.