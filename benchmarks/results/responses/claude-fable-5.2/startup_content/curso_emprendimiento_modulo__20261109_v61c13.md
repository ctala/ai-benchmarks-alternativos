# Claude Fable 5.2 — startup_content/curso_emprendimiento_modulo

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.92 | quality: 10.0
- latency_total: 69.086s | tokens_per_second: 104.1
- input_tokens: 390 | output_tokens: 7189
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

# Módulo 3: Automatización con IA: de la idea al flujo de trabajo

**Duración estimada:** 3 horas (1 h de teoría, 2 h de práctica)
**Nivel:** Emprendedor no técnico. No necesitas saber programar.

---

## 1. Objetivo del módulo

Al terminar este módulo podrás identificar qué tareas repetitivas de tu negocio conviene automatizar, diseñar un flujo de trabajo que combine tus herramientas con un modelo de IA y construir tu primera automatización funcional en n8n sin escribir código. No se trata de volverte experto en una herramienta. Se trata de aprender a pensar en flujos (qué lo dispara, qué decide la IA, qué acción se ejecuta) para que la IA trabaje por ti mientras atiendes lo que hace crecer tu empresa.

---

## 2. Contenido teórico

### 2.1 ¿Qué es automatizar con IA?

La automatización tradicional sigue **reglas fijas**: "si llega un correo con la palabra *factura*, muévelo a esta carpeta". Funciona bien, pero se rompe cuando la situación no encaja en la regla.

La automatización con IA agrega **criterio**: el modelo puede leer un mensaje, entender la intención, resumir, clasificar o redactar una respuesta.

| | Automatización tradicional | Automatización con IA |
|---|---|---|
| **Funciona con** | Reglas exactas | Lenguaje natural y contexto |
| **Ejemplo** | Guardar cada pedido en una hoja de cálculo | Leer una queja y decidir si es urgente |
| **Limitación** | No maneja casos ambiguos | Puede equivocarse y requiere supervisión |

Las mejores automatizaciones combinan ambas: reglas para lo predecible, IA para lo que requiere interpretación.

### 2.2 Anatomía de un flujo de trabajo

Todo flujo tiene tres partes:

```
DISPARADOR  →  PROCESO (IA + reglas)  →  ACCIÓN
"Cuando pase X"   "Analiza / decide / redacta"   "Haz Y"
```

- **Disparador (trigger):** el evento que inicia todo, como un formulario enviado o un mensaje de WhatsApp.
- **Proceso:** lo que ocurre con la información. La IA clasifica, resume o genera texto.
- **Acción:** el resultado, como enviar un correo, guardar una fila o avisar al equipo.

### 2.3 Herramientas: ¿por qué n8n?

| Herramienta | Ventaja principal | Considera que... |
|---|---|---|
| **n8n** | Flexible, con nodos de IA integrados; se puede instalar gratis en servidor propio | La curva de aprendizaje es algo mayor |
| **Make** | Visual e intuitiva | El costo sube con el volumen de operaciones |
| **Zapier** | La más simple, con miles de integraciones | Suele ser la más cara al escalar |

Usaremos **n8n** porque muestra con claridad cómo fluye la información, tiene plantillas listas y su costo es amigable para startups en etapa temprana. Lo que aprendas aquí se aplica igual en Make o Zapier.

**Vocabulario básico de n8n:**

- **Nodo:** cada bloque del flujo (un paso).
- **Credencial:** el permiso que le das a n8n para usar tu cuenta de Gmail, Google Sheets, etc.
- **Ejecución:** cada vez que el flujo corre de principio a fin.
- **Expresión:** un dato dinámico que viene de un paso anterior (por ejemplo, el nombre que alguien escribió en un formulario).

### 2.4 ¿Qué automatizar primero?

Una tarea es buena candidata si cumple al menos tres de estos criterios:

- [ ] Se repite varias veces por semana
- [ ] Sigue un patrón parecido cada vez
- [ ] Te quita tiempo, pero no requiere tu mejor talento
- [ ] Un error ocasional no sería grave
- [ ] La información ya está en formato digital

> **Regla de oro: humano en el circuito.** Al principio, haz que la IA proponga y que una persona apruebe. Quita la revisión humana solo cuando hayas comprobado que el flujo es confiable. Nunca automatices al 100 % decisiones sobre dinero, temas legales o datos sensibles de clientes.

---

## 3. Tres ejemplos prácticos para startups

*Los siguientes casos son escenarios ilustrativos basados en situaciones típicas de startups latinoamericanas.*

### Ejemplo 1: Atención al cliente automatizada

**Escenario:** una tienda online de cosmética natural en Medellín recibe unos 80 mensajes diarios. El 70 % son las mismas preguntas: envíos, medios de pago y estado del pedido.

```
Mensaje entrante (WhatsApp Business / correo)
        ↓
IA clasifica: ¿pregunta frecuente, reclamo o venta?
        ↓
┌─ Pregunta frecuente → IA responde usando el documento de FAQ
├─ Reclamo → Se notifica a una persona del equipo
└─ Intención de compra → Se envía catálogo y se avisa a ventas
```

**Claves para que funcione:**
- Dale a la IA un documento con tus políticas reales (envíos, devoluciones, horarios) e indícale que responda solo con esa información.
- Incluye siempre una salida: "Si no sabes la respuesta, di que un asesor se comunicará pronto".
- **Métrica a medir:** tiempo de primera respuesta y porcentaje de mensajes resueltos sin intervención humana.

### Ejemplo 2: Generación de contenido para redes sociales

**Escenario:** una fintech de Ciudad de México, con un equipo de cuatro personas, no logra publicar con constancia.

```
Cada lunes 8:00 a. m. (disparador programado)
        ↓
Lee los temas de la semana desde una hoja de Google Sheets
        ↓
IA genera 3 versiones: LinkedIn, Instagram y X
        ↓
Guarda los borradores en la hoja y avisa por Slack o correo
        ↓
Una persona revisa, ajusta y aprueba ✅
```

**Claves para que funcione:**
- Incluye en el prompt tu tono de marca y dos o tres publicaciones tuyas que hayan funcionado bien como ejemplo.
- No publiques automáticamente: la IA hace el borrador y tú das el toque final.
- **Métrica a medir:** horas semanales ahorradas y constancia de publicación.

### Ejemplo 3: Calificación automática de leads

**Escenario:** una startup SaaS B2B en Santiago recibe 40 solicitudes de demo por semana. El fundador pierde horas en llamadas con prospectos que no encajan.

```
Formulario de contacto enviado
        ↓
IA evalúa el lead según el perfil de cliente ideal
        ↓
┌─ CALIENTE → Alerta inmediata al fundador
└─ TIBIO / FRÍO → Solo se registra
        ↓
Todo queda guardado en Google Sheets o en el CRM
```

**Claves para que funcione:**
- Define por escrito tu cliente ideal (tamaño, industria, presupuesto, urgencia). La IA califica tan bien como tú describas tus criterios.
- Pide a la IA que explique la razón de cada clasificación para poder auditarla.
- **Métrica a medir:** tiempo de respuesta a leads calientes y tasa de conversión a reunión.

**Este es el flujo que vas a construir en el ejercicio.**

---

## 4. Ejercicio práctico: tu calificador de leads con IA

**Tiempo:** 45 a 60 minutos
**Resultado:** un formulario que recibe prospectos, los evalúa con IA, los guarda en una hoja de cálculo y te avisa por correo cuando llega uno valioso.

### Lo que necesitas antes de empezar

- Una cuenta en **n8n Cloud** (tiene prueba gratuita).
- Una cuenta de **Google** (para Sheets y Gmail).
- Una **clave API** de un modelo de IA. Puedes usar Google AI Studio (Gemini, con nivel gratuito) u OpenAI (requiere cargar saldo).

### Paso 1: Prepara tu hoja de cálculo

Crea una hoja en Google Sheets llamada **"Leads IA"** con estas columnas en la fila 1:

`Fecha | Nombre | Email | Empresa | Empleados | Necesidad | Presupuesto | Evaluación IA`

### Paso 2: Crea el flujo y el disparador

1. En n8n, haz clic en **Create Workflow** y nómbralo "Calificador de leads".
2. Agrega el nodo **n8n Form Trigger**.
3. Configura el formulario con estos campos: Nombre, Email, Empresa, Empleados, Necesidad (¿qué problema quieres resolver?) y Presupuesto (mensual aproximado).

### Paso 3: Agrega el cerebro (la IA)

1. Agrega el nodo **Basic LLM Chain** y conéctale un modelo de chat (Google Gemini u OpenAI).
2. Crea la credencial pegando tu clave API.
3. En el campo del prompt, pega y adapta este texto:

```
Eres asistente de ventas de [TU EMPRESA]. Vendemos [QUÉ VENDES]
a [DESCRIPCIÓN DE TU CLIENTE IDEAL].

Evalúa este prospecto:
- Nombre: {{ $json.Nombre }}
- Empresa: {{ $json.Empresa }}
- Empleados: {{ $json.Empleados }}
- Necesidad: {{ $json.Necesidad }}
- Presupuesto: {{ $json.Presupuesto }}

Responde exactamente en este formato:
CLASIFICACIÓN: (CALIENTE, TIBIO o FRÍO)
RAZÓN: (una frase)
SIGUIENTE PASO: (una acción concreta)
```

> **Tip:** no necesitas escribir las expresiones `{{ }}` a mano. Arrastra cada campo desde el panel izquierdo hasta el prompt.

### Paso 4: Agrega la decisión

1. Agrega un nodo **If**.
2. Condición: la respuesta de la IA **contiene** el texto `CALIENTE`.

### Paso 5: Configura las acciones

- **Rama verdadera (true):** agrega un nodo **Gmail → Send a message** que te envíe un correo con el asunto "🔥 Lead caliente: [Empresa]" y la evaluación de la IA en el cuerpo.
- **Ambas ramas:** conecta al final un nodo **Google Sheets → Append Row** que guarde los datos del formulario y la evaluación en tu hoja "Leads IA".

### Paso 6: Prueba con datos ficticios

Haz clic en **Test workflow** y llena el formulario dos veces:

1. **Lead ideal:** una empresa que encaja perfecto con tu cliente objetivo.
2. **Lead malo:** alguien sin presupuesto o fuera de tu mercado.

Verifica que:
- [ ] Ambos aparecen en tu hoja de cálculo
- [ ] Solo el lead ideal generó un correo de alerta
- [ ] La razón que da la IA tiene sentido

Si la IA clasifica mal, **mejora el prompt, no el flujo**: describe con más detalle a tu cliente ideal.

### Paso 7: Activa

Cambia el interruptor a **Active** y copia la URL de producción del formulario. Ya puedes compartirla en tu web o redes.

### Reto extra (opcional)

Agrega un paso donde la IA redacte un borrador de correo personalizado para cada lead caliente y te lo envíe para aprobarlo.

**Entregable del módulo:** una captura de pantalla de tu flujo y otra de tu hoja con al menos dos leads evaluados.

---

## 5. Recursos adicionales

- **Documentación oficial de n8n:** docs.n8n.io
- **Plantillas de flujos listas para usar:** n8n.io/workflows
- **Comunidad de n8n (foro de ayuda):** community.n8n.io
- **Google AI Studio (clave API de Gemini):** aistudio.google.com
- **Plataforma de OpenAI (clave API):** platform.openai.com
- **Plantilla sugerida:** crea un "Mapa de automatizaciones" con las columnas tarea, frecuencia, tiempo que consume, riesgo de error y prioridad. Úsalo para elegir tus próximos flujos.

> Las herramientas cambian de precios y funciones con frecuencia. Verifica las condiciones actuales antes de comprometer tu operación con una de ellas.

---

## 6. Preguntas de autoevaluación

**1. ¿Cuáles son los tres componentes de todo flujo de trabajo automatizado? Da un ejemplo de cada uno aplicado a tu negocio.**

*Respuesta esperada:* disparador, proceso y acción. Por ejemplo: llega un pedido por formulario (disparador), la IA verifica si los datos están completos (proceso) y se envía una confirmación al cliente (acción).

**2. Tu flujo de calificación marca como "FRÍO" a prospectos que tú consideras muy buenos. ¿Qué deberías revisar primero y por qué?**

*Respuesta esperada:* el prompt, en particular la descripción del cliente ideal y los criterios de evaluación. La IA califica según las instrucciones que recibe; si los criterios son vagos o incompletos, el resultado también lo será.

**3. Un emprendedor quiere que la IA apruebe reembolsos a clientes automáticamente, sin revisión. ¿Qué le recomendarías?**

*Respuesta esperada:* mantener un humano en el circuito. La IA puede clasificar la solicitud y preparar una recomendación, pero las decisiones que involucran dinero deben tener aprobación humana, al menos hasta comprobar la confiabilidad del flujo y definir límites claros, como montos máximos.

---

**Próximo módulo:** Módulo 4, donde llevarás tus automatizaciones al siguiente nivel con agentes de IA que usan herramientas y toman decisiones de varios pasos.