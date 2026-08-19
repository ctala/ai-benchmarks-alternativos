# Claude Opus 5 (suscripción) — startup_content/curso_emprendimiento_modulo

- model_id: `claude-opus-5`
- success: True  | final: 7.73 | quality: 10.0
- latency_total: 223.327s | tokens_per_second: 64.3
- input_tokens: 2 | output_tokens: 14355
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para emprendedores, cubriendo todos los aspectos necesarios del módulo con ejemplos prácticos y consejos claros.

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

# Módulo 3 — Automatización con IA: De la idea al flujo de trabajo

**Curso:** IA Práctica para Emprendedores
**Duración estimada:** 110 minutos (teoría 35 min · ejemplos 25 min · ejercicio 50 min)
**Nivel:** Emprendedor no técnico. No necesitas saber programar.
**Prerrequisitos:** Módulo 1 (cómo funcionan los modelos) y Módulo 2 (cómo escribir prompts que sirvan).
**Entregable al terminar:** un flujo funcionando en tu cuenta que califica leads solo y te avisa cuando entra uno bueno.

---

## 3.1 Objetivo del módulo

Al terminar este módulo vas a poder tomar una tarea repetitiva de tu operación, descomponerla en pasos, decidir cuáles delega a un modelo de IA y cuáles no, y construir ese flujo en n8n sin escribir código. El objetivo no es que aprendas una herramienta: es que salgas con **un proceso que antes te consumía tiempo todos los días corriendo solo**, y con el criterio para repetir el ejercicio con los otros cinco procesos que también te lo consumen.

---

## 3.2 Contenido teórico

### 3.2.1 Qué es automatizar (y qué no)

Automatizar es escribir una regla del tipo: **"cuando pase X, haz Y, después Z"**. Nada más.

Lo que no es automatizar:

- No es tener ChatGPT abierto y pegarle textos a mano. Eso es usar IA, y sigue dependiendo de que tú te acuerdes.
- No es un chatbot en tu web. Eso es un producto; la automatización es la plomería que está detrás.
- No es reemplazar personas. En una startup de 1 a 5 personas, la automatización reemplaza **tu tiempo muerto**, no a tu equipo.

**La regla dura, y es la más importante del módulo:** no automatices un proceso que no hiciste a mano al menos 20 veces. Si no lo hiciste 20 veces, no sabes cuáles son los casos raros, y los casos raros son el 80% del trabajo de construir el flujo. Automatizar un proceso mal definido te da caos más rápido, no menos caos.

### 3.2.2 La anatomía de todo flujo

Cualquier automatización, sin importar la herramienta, tiene tres partes:

| Parte | Qué es | Ejemplos |
|---|---|---|
| **Disparador** (trigger) | Lo que hace arrancar el flujo | Alguien llena un formulario · Llega un correo · Son las 9:00 AM · Hay una fila nueva en una planilla |
| **Pasos** (nodos) | Lo que pasa en el medio | Clasificar, buscar en una base, redactar, filtrar, decidir |
| **Resultado** (acción) | Dónde termina | Guardar en una planilla · Enviar un WhatsApp · Crear una tarea · Publicar un post |

Si puedes escribir tu proceso en esa estructura en una servilleta, lo puedes construir. Si no puedes, el problema no es la herramienta: es que todavía no entiendes tu proceso.

**Ejercicio mental de 2 minutos, hazlo ahora:** toma la tarea que más te fastidia de tu semana y escríbela así:

```
CUANDO ____________________
ENTONCES __________________
Y DESPUÉS _________________
TERMINA EN ________________
```

### 3.2.3 Dónde entra la IA (y dónde no debe entrar)

Antes de la IA, las automatizaciones solo podían mover datos estructurados: copiar un correo de acá para allá. El salto es que ahora un paso del flujo puede **entender texto desordenado y tomar una decisión**.

**Cuatro trabajos donde un modelo rinde muy bien:**

1. **Clasificar.** "Este mensaje, ¿es una queja, una consulta de precio o spam?"
2. **Extraer.** "De este correo largo, sácame nombre, empresa, presupuesto y urgencia en formato ordenado."
3. **Redactar borradores.** "Escribe una respuesta a esta consulta usando este tono y esta información."
4. **Resumir.** "De estas 40 respuestas de la encuesta, dime los 5 temas que más se repiten."

**Tres trabajos donde vas a sufrir:**

1. **Cálculos y matemática exacta.** Para eso está una fórmula, no un modelo. Un modelo puede sumar mal y no te avisa.
2. **Decisiones irreversibles sin revisión humana.** Cobrar, borrar, enviar un contrato, despedir a alguien del programa. Nunca en automático.
3. **Datos que el modelo no tiene.** Si le preguntas por tu inventario y no se lo pasas en el paso anterior, se lo inventa. Con toda confianza.

**Criterio práctico:** si equivocarse cuesta caro y es difícil de revertir, el modelo propone y un humano aprueba. Si equivocarse cuesta poco, que lo haga solo. La mayoría de las tareas de una startup temprana caen en el segundo grupo, y ahí está tu ganancia.

### 3.2.4 El mapa de herramientas: cuál te sirve

| Herramienta | Cómo se siente | Cuándo elegirla | Precio de referencia |
|---|---|---|---|
| **Zapier** | La más simple, todo apuntar y hacer clic | Flujos de 2-3 pasos, sin lógica complicada | Desde ~US$20/mes, sube rápido por volumen |
| **Make** | Visual, más potente que Zapier, más barato | Flujos con ramas y bucles, presupuesto ajustado | Desde ~US$9/mes |
| **n8n** | Visual pero sin techo. Te deja meter mano cuando lo necesitas | Cuando quieres crecer sin cambiar de herramienta, o quieres alojarlo tú | Nube desde ~US$20-25/mes · autoalojado gratis (servidor ~US$6-12/mes) |
| **GPTs / Asistentes** | Conversacional, sin flujo | Tareas que tú disparas manualmente, no automatización real | Incluido en el plan del proveedor |

*(Precios de referencia a la fecha del módulo. Verifícalos antes de contratar: cambian.)*

**Por qué usamos n8n en este curso, sin romance:**

- **No te cobra por paso ejecutado.** Zapier cobra por tarea; un flujo de 8 pasos que corre 1.000 veces al mes te sale carísimo. n8n cobra por *ejecución completa* del flujo, sin importar cuántos pasos tenga. Con volumen, la diferencia es de un orden de magnitud.
- **Tiene nodos de IA nativos.** Conectas OpenAI, Anthropic, Google o un modelo local sin plomería extra.
- **Puedes autoalojarlo.** Si tus datos son sensibles (salud, finanzas, datos de clientes), esto no es un lujo: es el requisito.
- **El techo está lejos.** Vas a poder resolver el 100% de tus casos en la misma herramienta durante años.

**La contra, y es real:** la curva de aprendizaje es más empinada que la de Zapier. Las primeras dos horas te vas a sentir tonto. Es normal. Después de eso no vuelves.

### 3.2.5 Cuánto cuesta de verdad un flujo con IA

Esta es la parte que casi nadie te explica y por la que la gente se asusta sin motivo.

Los modelos cobran por **tokens** (aproximadamente: 1 token ≈ 0,75 palabras en español). Cobran distinto por lo que entra y por lo que sale.

Cuenta real de un clasificador de leads:

```
Prompt de instrucciones:       ~300 tokens
Datos del lead:                ~150 tokens
Respuesta del modelo:          ~80 tokens
─────────────────────────────────────────
Total por lead:                ~530 tokens
```

Con un modelo económico (los "mini" / "flash" / "haiku" de cada proveedor), **calificar 1.000 leads te cuesta entre US$0,20 y US$1**. Menos que un café.

**Dos reglas de costo que te ahorran plata desde el día uno:**

1. **Usa el modelo barato para clasificar y extraer.** El modelo caro es para redactar cosas que la gente va a leer. Clasificar "caliente / tibio / frío" no requiere el modelo más potente del mercado, requiere un buen prompt.
2. **Filtra antes de llamar al modelo.** Si puedes descartar el spam con una regla simple, hazlo con la regla. Cada llamada al modelo que evitas es dinero y segundos ahorrados.

### 3.2.6 El error que casi todos cometen la primera vez

Construyen el flujo perfecto de 14 pasos, lo activan, y a la semana descubren que lleva 6 días fallando en silencio.

**Todo flujo en producción necesita tres cosas antes de que lo dejes solo:**

- **Un log.** Que cada ejecución deje registro en una planilla. Si no lo ves, no existe.
- **Una alerta de error.** n8n tiene "Error Workflow": configúralo para que te mande un mensaje cuando algo falle.
- **Un botón de pánico.** Saber cómo desactivarlo en 10 segundos.

Sin esas tres, no automatizaste: escondiste el problema.

---

## 3.3 Tres ejemplos prácticos para startups

Los tres siguen el mismo esqueleto. Léelos buscando el patrón, no los detalles.

---

### Ejemplo 1 — Atención al cliente automatizada

**El problema:** recibes entre 20 y 60 mensajes al día entre correo, WhatsApp e Instagram. El 70% son las mismas cinco preguntas. Contestarlas te toma 90 minutos diarios y las respondes tarde y mal.

**El flujo:**

```
Llega un mensaje (correo / WhatsApp / formulario)
   ↓
IA clasifica: [precio] [soporte técnico] [devolución] [venta nueva] [spam] [otro]
   ↓
   ├── Es una de las 5 preguntas frecuentes
   │      → IA redacta respuesta usando la base de conocimiento
   │      → Envía automáticamente
   │      → Registra en planilla
   │
   ├── Es venta nueva o algo delicado
   │      → Notifica al humano con un borrador ya escrito
   │      → El humano revisa, ajusta y envía
   │
   └── Es spam
          → Archiva, no hace nada
```

**El prompt del clasificador:**

```
Eres el sistema de triaje de atención al cliente de [TU EMPRESA],
que vende [QUÉ VENDES] a [QUIÉN].

Clasifica el mensaje del cliente en UNA de estas categorías:
- precio: pregunta cuánto cuesta, planes, descuentos
- soporte: algo no funciona, no sabe cómo usar el producto
- devolucion: quiere cancelar, reembolso o reclamo formal
- venta_nueva: prospecto interesado que aún no compra
- spam: publicidad, mensajes automáticos, irrelevante
- otro: no encaja en ninguna de las anteriores

Devuelve SOLO este JSON, sin texto adicional:
{
  "categoria": "...",
  "urgencia": "alta|media|baja",
  "sentimiento": "positivo|neutral|molesto",
  "requiere_humano": true|false,
  "resumen": "una frase de máximo 15 palabras"
}

Marca requiere_humano en true si: el cliente está molesto,
menciona temas legales, pide hablar con una persona,
o la categoría es devolucion.

Mensaje del cliente:
"""
{{ $json.mensaje }}
"""
```

**Qué medir:** porcentaje de mensajes resueltos sin intervención humana (empieza esperando 40-50%, no 90%), tiempo de primera respuesta, y cuántas respuestas automáticas terminaron en queja.

**La trampa:** dejar que la IA responda todo desde el día uno. **Arranca en modo borrador durante dos semanas**: la IA escribe, tú apruebas con un clic. Cuando lleves 100 borradores seguidos que apruebas sin editar, recién ahí le sueltas la mano en las categorías fáciles.

---

### Ejemplo 2 — Generación de contenido para redes sociales

**El problema:** sabes que publicar te trae clientes, pero publicas cuando te acuerdas, que es dos veces al mes.

**El flujo:**

```
Cada lunes 8:00 AM (disparador por horario)
   ↓
Lee la planilla "Banco de ideas" y toma 5 filas sin usar
   ↓
Para cada idea:
   IA escribe 1 post adaptado a la red que corresponde
   (formato, largo y tono distintos por red)
   ↓
Guarda los 5 borradores en una planilla "Por aprobar"
   ↓
Te manda un mensaje: "5 posts listos para revisar: [link]"
   ↓
Marcas ✅ en la columna "aprobado"
   ↓
Otro flujo revisa la planilla cada hora y publica
lo aprobado según el calendario
```

**El prompt del redactor:**

```
Escribes contenido para [TU NOMBRE], que le habla a
[TU AUDIENCIA: ej. fundadores de startups en LATAM].

TONO: directo, sin relleno, primera persona. Sin emojis decorativos.
Sin frases de coach motivacional. Sin "en el mundo actual".
Español neutro: nada de modismos de un solo país.

REGLAS DURAS:
- Un post = una idea. No tres.
- Todo dato o cifra debe venir de la idea original.
  Si no hay cifra, NO inventes una.
- Primera línea: gancho concreto, no pregunta genérica.
- Cierra con una acción o una pregunta real, no con "¿tú qué opinas?".

FORMATO SEGÚN RED:
- LinkedIn: 900-1.300 caracteres, párrafos de 1-2 líneas
- Instagram: 400-600 caracteres, más personal
- X: máximo 270 caracteres, una sola idea

IDEA BASE:
Tema: {{ $json.tema }}
Punto clave: {{ $json.punto_clave }}
Ejemplo real o dato: {{ $json.evidencia }}
Red destino: {{ $json.red }}

Devuelve solo el texto del post, sin comillas ni explicaciones.
```

**Qué medir:** cuántos borradores apruebas sin editar (si es menos del 50%, tu prompt está flojo, no el modelo), y si el alcance se mantiene comparado con lo que escribías a mano.

**La trampa:** dejar que la IA invente el tema *y* el texto. El resultado es contenido genérico que no le importa a nadie, con tu cara puesta. **El activo eres tú: las ideas, las cifras y las historias las pones tú en el banco de ideas. La IA solo las viste y las adapta al formato.** Sin banco de ideas, este flujo produce basura eficientemente.

---

### Ejemplo 3 — Calificación automática de leads

**El problema:** te llegan 40 formularios a la semana. Tres son clientes reales. Los descubres el jueves, cuando ya se fueron con el competidor que respondió el martes.

**El flujo:**

```
Alguien llena el formulario
   ↓
(Opcional) Busca datos de la empresa por el dominio del correo
   ↓
IA califica según TU criterio de cliente ideal → puntaje 0-100
   ↓
   ├── 70+ (caliente)
   │      → Alerta inmediata a tu Telegram/WhatsApp
   │      → Crea tarea "Llamar hoy"
   │
   ├── 40-69 (tibio)
   │      → Lo mete en la secuencia de correos educativos
   │
   └── menos de 40 (frío)
          → Solo lo guarda en la planilla, sin acción
   ↓
Todos van a la planilla / CRM con su puntaje y justificación
```

**El prompt del calificador:**

```
Eres el filtro de leads de [TU EMPRESA].
Vendemos [PRODUCTO] a [CLIENTE IDEAL] por [PRECIO/RANGO].

CLIENTE IDEAL (súmale puntos):
- Empresa de [TAMAÑO] en [SECTOR]
- Tiene el problema de [DOLOR ESPECÍFICO]
- Tiene presupuesto de [MONTO] o más
- Quien escribe puede decidir o influye en la decisión
- Necesita resolverlo en menos de 90 días

MALA SEÑAL (réstale puntos):
- Estudiante, tesis o investigación de mercado
- Pide asesoría gratis sin intención de comprar
- Correo genérico sin empresa identificable
- Presupuesto muy por debajo de nuestro precio mínimo
- Competidor haciendo reconocimiento

Devuelve SOLO este JSON:
{
  "puntaje": 0-100,
  "temperatura": "caliente|tibio|frio",
  "razon": "máximo 20 palabras, concreto",
  "señal_mas_fuerte": "el dato que más pesó en tu decisión",
  "que_falta_saber": "la pregunta que haría en el primer contacto"
}

Sé estricto. Un puntaje de 70+ significa que un vendedor
deja lo que está haciendo para llamar. Si dudas, baja el puntaje.

DATOS DEL LEAD:
Nombre: {{ $json.nombre }}
Empresa: {{ $json.empresa }}
Correo: {{ $json.email }}
Qué necesita: {{ $json.mensaje }}
Presupuesto declarado: {{ $json.presupuesto }}
```

**Qué medir:** de los que la IA marcó como calientes, cuántos efectivamente avanzaron. Y al revés, más importante: **de los clientes que sí cerraste, ¿qué puntaje les había puesto la IA?** Si a tu mejor cliente del mes lo marcó frío, tu definición de cliente ideal está mal escrita.

**La trampa:** confiar en el puntaje sin auditar. Revisa 20 calificaciones a mano en la primera semana y ajusta el prompt. Un calificador mal calibrado que descarta buenos leads te cuesta plata real y **no te avisa nunca**.

---

### El patrón que se repite en los tres

```
1. Un disparador claro
2. La IA CLASIFICA o EXTRAE (trabajo barato, alto valor)
3. Una bifurcación por reglas simples, no por IA
4. La IA REDACTA solo en las ramas que lo necesitan
5. El humano aprueba lo irreversible
6. Todo queda registrado
```

Si copias solo esto del módulo, ya vale la pena.

---

## 3.4 Ejercicio práctico: tu primer calificador de leads

**Tiempo:** 50 minutos.
**Al terminar tendrás:** un formulario público que califica solo a quien lo llena, lo guarda en tu planilla y te avisa al teléfono cuando entra alguien que vale la pena.

### Paso 0 — Prepara la mesa (10 min)

Necesitas cuatro cosas:

1. **Cuenta en n8n** → `n8n.io`, plan de prueba gratuito. Sirve perfecto para el ejercicio.
2. **Cuenta en un proveedor de IA** con **US$5 de crédito** cargado (OpenAI, Anthropic o Google). Vas a gastar centavos, pero necesitas el crédito activo.
3. **Una cuenta de Google** con una hoja de cálculo en blanco.
4. **Telegram** instalado en tu teléfono.

Crea la hoja de cálculo con **exactamente estos encabezados en la fila 1**:

| fecha | nombre | empresa | email | mensaje | puntaje | temperatura | razon |
|---|---|---|---|---|---|---|---|

Y crea tu bot de Telegram (2 minutos): abre Telegram, busca `@BotFather`, envía `/newbot`, ponle nombre, y **guarda el token que te devuelve**. Después escríbele algo a tu propio bot para que pueda contestarte.

### Paso 1 — Define tu cliente ideal (5 min, y es el paso más importante)

Antes de tocar la herramienta, responde en una nota:

```
Vendo: ______________________________
A: __________________________________
Que tienen el problema de: ___________
Y pagan alrededor de: ________________

Un lead ES bueno cuando: _____________
Un lead NO es bueno cuando: __________
```

**No sigas sin esto.** Si no lo tienes claro tú, el modelo tampoco lo va a tener y el flujo va a calificar al azar con mucha seguridad.

### Paso 2 — Crea el flujo y el formulario (8 min)

1. En n8n: **Workflows → Add workflow**. Nómbralo `Calificador de Leads`.
2. Clic en el **+** → busca **"On form submission"** (n8n Form Trigger).
3. Configúralo:
   - **Form Title:** `Cuéntanos de tu proyecto`
   - **Form Description:** `Te respondemos en menos de 24 horas.`
   - Agrega estos campos (botón *Add Form Field*):

| Campo | Tipo | Obligatorio |
|---|---|---|
| `nombre` | Text | Sí |
| `empresa` | Text | Sí |
| `email` | Email | Sí |
| `mensaje` | Textarea | Sí |
| `presupuesto` | Dropdown: `Menos de 500` / `500 a 2000` / `Más de 2000` / `Aún no lo sé` | No |

4. Copia la **URL de prueba** del formulario. Ábrela en otra pestaña: deberías ver tu formulario real, público y funcionando. Ya tienes más que muchos.

### Paso 3 — Conecta el cerebro (7 min)

1. Después del formulario, **+** → busca **"Message a model"** (nodo de OpenAI, Anthropic o Google, el que hayas elegido).
2. **Credential → Create new** → pega tu API key del proveedor.
3. **Model:** elige el modelo **económico** del proveedor (los que dicen *mini*, *flash* o *haiku*). No uses el caro.
4. En **Messages**, pega el prompt del Ejemplo 3 **reemplazando los corchetes con tus respuestas del Paso 1**.
5. Activa la opción **"Output Content as JSON"** (o *JSON Output*, según el proveedor). Esto es clave: sin eso te devuelve un párrafo en vez de datos que puedas usar.

### Paso 4 — Prueba antes de seguir (5 min)

**No construyas el resto a ciegas.** Abre tu formulario y envía estos tres casos:

| # | Empresa | Mensaje | Presupuesto | Qué esperas |
|---|---|---|---|---|
| 1 | Distribuidora Norte | "Somos 12 personas, perdemos 2 horas diarias armando pedidos a mano. Necesitamos resolverlo este trimestre." | Más de 2000 | **Caliente (70+)** |
| 2 | — | "Hola, ¿cuánto cuesta?" | Aún no lo sé | **Tibio o frío** |
| 3 | Universidad | "Estoy haciendo mi tesis sobre automatización, ¿me pueden dar una entrevista?" | Menos de 500 | **Frío (<40)** |

Mira la salida del nodo de IA en n8n. **¿Los tres puntajes tienen sentido?**

- Si sí → sigue.
- Si no → **no cambies de modelo, cambia el prompt.** El 95% de las veces el problema es que tu definición de cliente ideal está vaga. Vuelve al Paso 1, sé más específico, prueba de nuevo.

### Paso 5 — Guarda todo en la planilla (5 min)

1. **+** → **Google Sheets** → acción **Append Row**.
2. Conecta tu cuenta de Google, elige el archivo y la hoja.
3. Mapea cada columna arrastrando los datos desde el panel izquierdo:
   - `fecha` → `{{ $now.format('yyyy-MM-dd HH:mm') }}`
   - `nombre`, `empresa`, `email`, `mensaje` → vienen del **formulario**
   - `puntaje`, `temperatura`, `razon` → vienen de la **salida de la IA**

### Paso 6 — La alerta que te cambia el día (7 min)

1. Después de Sheets, **+** → **If** (o *Filter*).
2. Condición: `{{ $json.puntaje }}` **is greater than** `69` (tipo: Number).
3. En la rama **true**: **+** → **Telegram** → **Send Message**.
   - Credential: pega el token de BotFather.
   - Chat ID: escríbele a `@userinfobot` en Telegram y te da el tuyo.
   - Mensaje:

```
🔥 LEAD CALIENTE — {{ $json.puntaje }}/100

{{ $json.nombre }} — {{ $json.empresa }}
{{ $json.email }}

Por qué: {{ $json.razon }}
Pregunta clave: {{ $json.que_falta_saber }}

Llamar hoy.
```

4. La rama **false** la dejas vacía. No hacer nada también es una decisión válida del flujo.

### Paso 7 — Actívalo (3 min)

1. Interruptor **Active** arriba a la derecha.
2. Copia la **URL de producción** del formulario (es distinta a la de prueba).
3. Llena el formulario con el caso caliente una vez más.
4. **Tu teléfono debe sonar en menos de 15 segundos.**

### Terminaste cuando puedas marcar las cuatro:

- [ ] El formulario es público y cualquiera puede llenarlo
- [ ] Cada envío aparece como fila nueva en tu planilla, con puntaje y razón
- [ ] Los leads de 70+ llegan a tu Telegram
- [ ] Los leads bajo 70 **no** te llegan (esta es la que la gente olvida probar, y es la que hace que el sistema sirva)

### Errores que vas a cometer (y cómo salir)

| Síntoma | Causa real | Solución |
|---|---|---|
| La IA devuelve un párrafo, no JSON | Falta activar el modo JSON output | Actívalo en el nodo del modelo |
| El nodo Sheets falla | Los encabezados no coinciden exactamente | Revisa mayúsculas, tildes y espacios |
| Todo sale con puntaje 50 | Tu definición de cliente ideal es vaga | Vuelve al Paso 1 y sé brutalmente específico |
| No llega el Telegram | Nunca le escribiste primero al bot | Mándale un `/start` a tu bot |
| Funciona en prueba, no en producción | Usaste la URL de test | Usa la URL de producción del trigger |

### Si te sobró tiempo: tres mejoras en orden de valor

1. **Agrega una columna `resultado_real`** en la planilla y llénala a mano cuando cierres o pierdas. En un mes tienes datos duros para ajustar el prompt. Esto vale más que las otras dos juntas.
2. **Respuesta automática al lead** con un nodo de correo: "recibimos tu mensaje". Baja tu tiempo de respuesta percibido a cero.
3. **Resumen semanal**: un segundo flujo que cada lunes lee la planilla y te manda "esta semana: 23 leads, 4 calientes, 2 sin contactar".

---

## 3.5 Recursos adicionales

**Para seguir aprendiendo la herramienta**

- Documentación oficial de n8n → `docs.n8n.io` (empieza por *Try it out* y por *Expressions*)
- Biblioteca de plantillas de n8n → `n8n.io/workflows` — más de mil flujos que puedes importar y desarmar. Aprender leyendo flujos ajenos es 3× más rápido que construir desde cero.
- Canal de YouTube de n8n: la serie de nivel principiante son ~2 horas bien invertidas

**Para escribir mejores prompts dentro de tus flujos**

- Guías oficiales de prompting de tu proveedor (OpenAI, Anthropic y Google tienen la suya, y son cortas)
- Repasa el Módulo 2 de este curso: el 90% de los flujos que fallan, fallan por el prompt, no por la plomería

**Para elegir el modelo correcto por costo y calidad**

- Compara precios por millón de tokens en la página de pricing de cada proveedor antes de escalar. La diferencia entre el modelo económico y el premium puede ser de 20× para tareas donde no se nota la diferencia.
- Benchmarks públicos de modelos en español para tareas de clasificación y redacción

**Plantillas de este módulo**

- Los tres prompts (clasificador de soporte, redactor de contenido, calificador de leads) están en el material descargable. Cópialos y reemplaza los corchetes: son puntos de partida probados, no teoría.

---

## 3.6 Preguntas de autoevaluación

Respóndelas por escrito antes de mirar el criterio. Si no puedes responder la 1 y la 3, repite el módulo.

---

**Pregunta 1.**
Tienes un flujo que responde consultas de clientes de forma totalmente automática. Un cliente escribe: *"Llevo 3 semanas esperando mi pedido, esto es una vergüenza, voy a ir al SERNAC/PROFECO"*. El flujo detecta la palabra "pedido", lo clasifica como consulta de estado y envía la respuesta automática estándar.

**¿Qué está mal en el diseño del flujo, y qué dos cambios concretos harías?**

<details>
<summary>Criterio de respuesta correcta</summary>

El problema no es que la IA se equivocara de categoría: es que **el flujo no tiene ruta de escape para casos delicados**. Una decisión con consecuencia legal o reputacional se ejecutó sin revisión humana.

Los dos cambios que debiste mencionar:

1. **Agregar detección de sentimiento y una condición de escalamiento**: si el sentimiento es "molesto", si menciona autoridad regulatoria, temas legales, o pide hablar con una persona → el flujo **no responde**, notifica a un humano con el contexto y un borrador sugerido.
2. **Aplicar el criterio de reversibilidad**: enviar una respuesta fría a un cliente furioso es caro y difícil de revertir → esa rama es "la IA propone, el humano aprueba".

Punto extra si mencionaste que el flujo debía dejar registro y alerta para que el error se detectara el mismo día, no un mes después.
</details>

---

**Pregunta 2.**
Estás diseñando un flujo con 6 pasos. Dos de ellos podrían usar IA. Tu volumen es de 3.000 ejecuciones al mes y quieres mantener el costo por debajo de US$10 mensuales.

**¿Qué decisiones tomas sobre (a) qué pasos usan IA, (b) qué modelo usas en cada uno, y (c) qué haces antes de llamar al modelo?**

<details>
<summary>Criterio de respuesta correcta</summary>

**(a)** Solo usan IA los pasos que requieren *entender texto desordenado*: clasificar, extraer o redactar. Filtros, condiciones, cálculos, fechas y movimiento de datos se resuelven con nodos normales — son gratis, instantáneos y no alucinan.

**(b)** El paso de **clasificar o extraer usa el modelo económico** (mini / flash / haiku). El paso de **redactar algo que un cliente va a leer** puede justificar el modelo premium. Nunca al revés.

**(c)** **Filtras antes de llamar al modelo.** Si una regla simple descarta spam, duplicados o casos fuera de alcance, esa llamada nunca se paga. Reducir 3.000 llamadas a 1.800 con un filtro previo baja el costo 40% sin tocar nada más.

Cálculo de referencia: 3.000 ejecuciones × ~500 tokens × modelo económico ≈ **menos de US$3/mes**. El presupuesto de US$10 sobra con holgura si respetas estas tres reglas — y no alcanza si mandas todo al modelo premium.
</details>

---

**Pregunta 3.**
Un socio te dice: *"Automaticemos la aprobación de descuentos. Que la IA lea el pedido y decida si aplica el 20%."*

**¿Automatizarías ese proceso hoy? Justifica usando al menos dos criterios del módulo.**

<details>
<summary>Criterio de respuesta correcta</summary>

**No, no como está planteado.** Al menos dos de estos criterios:

1. **Regla de las 20 veces**: si el proceso no se ha ejecutado a mano suficientes veces con criterios escritos, no existe un proceso que automatizar. Estarías automatizando la intuición de alguien, y la intuición no se puede poner en un prompt.
2. **Reversibilidad**: aprobar un descuento afecta el margen y crea un precedente con el cliente. Es difícil de revertir → la IA propone, el humano aprueba.
3. **Matemática exacta**: si el descuento depende de umbrales de monto, márgenes o inventario, eso es una fórmula, no un modelo. El modelo puede calcular mal y no te avisa.

**Qué sí propondrías:** que la IA **extraiga** los datos del pedido y **arme el caso** ("cliente recurrente, tercer pedido, monto US$1.400, margen actual 34%, descuento solicitado 20% → margen resultante 14%"), lo mande a tu Telegram y tú apruebes con un clic. Automatizas el trabajo aburrido (leer, extraer, calcular, presentar) y conservas la decisión.

Después de 100 aprobaciones con criterio consistente, ya tienes el proceso documentado, y **ahí sí** puedes automatizar las decisiones fáciles con reglas duras y dejar solo los casos límite para revisión.
</details>

---

## Cierre del módulo

Si el ejercicio te funcionó, en las próximas 48 horas vas a tener la tentación de automatizar todo. No lo hagas.

**Toma una sola cosa más de tu semana**, la que más te fastidia, escríbela en la estructura *CUANDO → ENTONCES → DESPUÉS → TERMINA EN*, y constrúyela. Un flujo bien hecho y vivo vale más que ocho a medio terminar y desactivados.

**Tarea para el Módulo 4:** trae tu flujo funcionando y **el número de leads que procesó en la semana**. Vamos a usar esa data real para conectar varios flujos entre sí.