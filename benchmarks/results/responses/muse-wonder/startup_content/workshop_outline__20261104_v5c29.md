# Muse Wonder — startup_content/workshop_outline

- model_id: `meta/muse-wonder`
- success: True  | final: 7.84 | quality: 9.72
- latency_total: 35.859s | tokens_per_second: 99.9
- input_tokens: 201 | output_tokens: 3581
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un facilitador de workshops de emprendimiento y tecnologia con experiencia en Latinoamerica.

**user:**

Crea el outline completo para un workshop presencial de 3 horas titulado:
"Construye tu Asistente de IA para tu Startup - Workshop Practico"

La audiencia son emprendedores early-stage no-tecnicos (20-30 personas).

Incluye:
1. Agenda detallada con tiempos (3 horas)
2. Materiales necesarios (que preparar antes)
3. Para cada bloque:
   - Titulo y duracion
   - Objetivo
   - Dinamica (charla, ejercicio, demo, discusion)
   - Key takeaway
4. Ejercicio principal del workshop (que todos puedan hacer)
5. Recursos para llevar a casa
6. Slide count estimado por seccion

El tono debe ser energico y practico, no academico.


## Respuesta completa

# Construye tu Asistente de IA para tu Startup - Workshop Práctico
**Workshop presencial | 3 horas | 20-30 emprendedores early-stage no-técnicos**

**La promesa del workshop:** Nadie se va con teoría. Todos se van con un asistente de IA funcionando, probado con el caso real de su startup.

### 1. AGENDA DETALLADA - 180 MINUTOS

| Hora | Bloque | Duración |
| :--- | :--- | :--- |
| 0:00 - 0:15 | 1. Apertura que engancha | 15 min |
| 0:15 - 0:35 | 2. IA sin humo para startups | 20 min |
| 0:35 - 0:55 | 3. Demo en vivo | 20 min |
| 0:55 - 1:15 | 4. Define tu asistente ideal | 20 min |
| 1:15 - 1:25 | **Break activo** | **10 min** |
| 1:25 - 2:15 | 5. EJERCICIO PRINCIPAL: Constrúyelo | 50 min |
| 2:15 - 2:35 | 6. Rómpelo y mejóralo | 20 min |
| 2:35 - 2:50 | 7. Showcase relámpago | 15 min |
| 2:50 - 3:00 | 8. Cierre y plan de 7 días | 10 min |

### 2. MATERIALES NECESARIOS

**Enviar 48h antes a los participantes:**
Mensaje por WhatsApp/Email: Traer laptop cargada, crear cuenta gratuita en ChatGPT, Claude o Gemini, y traer en 3 líneas: qué vende su startup, a quién, y qué tarea les quita más tiempo.

**Para el facilitador:**
- Laptop + backup de la demo en video/screenshots por si falla el WiFi
- Proyector, clicker, micrófono de solapa, parlante para música
- Cuentas demo ya creadas y logueadas
- Carpeta en Drive con todos los recursos, lista para compartir por QR

**Para la sala:**
- Mesas en grupos de 4-5, no formato auditorio
- 1 Canvas del Asistente impreso A3 por persona + lapiceros
- Post-its y marcadores por mesa
- Enchufes / extensiones en cada mesa - esto es crítico
- WiFi probado, nombre y clave visibles en la primera slide
- Café, agua y música de fondo al inicio y en el break

**Imprimibles:**
Canvas del Asistente, Tarjeta del Prompt Maestro, Checklist de Pruebas

### 3. DESARROLLO POR BLOQUE

#### BLOQUE 1: Apertura que engancha
**Duración:** 15 min | **Slides:** 4

**Objetivo:** Romper el hielo y bajar el miedo a "no soy técnico".
**Dinámica:** Charla interactiva + ejercicio rápido en parejas.
Arrancas con una pregunta: "¿Qué tarea repetitiva harías desaparecer hoy de tu startup?" 2 minutos en parejas, 3 respuestas al aire. Luego presentas tu asistente real funcionando en vivo, no en slides.

**Key Takeaway:** "No necesitas saber programar. Necesitas saber dar buenas instrucciones."

#### BLOQUE 2: IA sin humo para startups
**Duración:** 20 min | **Slides:** 6

**Objetivo:** Entender qué SÍ y qué NO puede hacer un asistente hoy, sin vender humo.
**Dinámica:** Charla práctica con ejemplos latinos reales.
Cubres solo 3 casos de uso rentables para early-stage: 1) Ventas y atención al cliente por WhatsApp/Instagram, 2) Contenido y marketing, 3) Operaciones y productividad del fundador. Qué no hacer: no subir datos sensibles de clientes, no confiar ciegamente en precios/datos legales.

**Key Takeaway:** "Un buen asistente no hace todo. Hace UNA tarea repetitiva, muy bien, todas las veces."

#### BLOQUE 3: Demo en vivo - De cero a asistente en 10 minutos
**Duración:** 20 min | **Slides:** 2

**Objetivo:** Que vean lo simple que es antes de hacerlo ellos.
**Dinámica:** Demo 100% en pantalla.
Construyes frente a ellos un asistente para una startup ficticia pero familiar, ej: una marca de cosmética natural que vende por Instagram. Le das rol, contexto, tono, información del negocio y lo pruebas con preguntas reales de clientes. Te equivocas a propósito y lo corriges en vivo.

**Key Takeaway:** "La magia no está en la herramienta, está en el contexto que le das sobre TU negocio."

#### BLOQUE 4: Define tu asistente ideal
**Duración:** 20 min | **Slides:** 5

**Objetivo:** Que cada uno elija UN caso de uso viable para construir hoy.
**Dinámica:** Ejercicio individual con el Canvas + discusión en mesa.
Presentas los 3 arquetipos para elegir: **Vendedor, Creador de Contenido u Organizador Interno.** Cada uno completa su Canvas: ¿Qué tarea hará? ¿Para quién? ¿Qué información necesita de mi negocio? ¿Cómo debe sonar? ¿Qué NUNCA debe hacer?

**Key Takeaway:** "Si tu asistente no tiene límites claros, va a inventar. Y inventar en tu negocio cuesta clientes."

#### BLOQUE 5: EJERCICIO PRINCIPAL - Construye tu Asistente
**Duración:** 50 min | **Slides:** 4 de instrucciones paso a paso

**Objetivo:** Salir con el asistente creado, configurado y probado.
**Dinámica:** Trabajo individual asistido. Tú y los mentores/ayudantes rotan por mesas. Música de fondo, timer visible en pantalla.

Este es el corazón del workshop. Todos usan la misma **Plantilla de Prompt Maestro** para que nadie se bloquee:

```
Actúa como [ROL: ej. asistente de ventas de mi startup]
Mi negocio es: [qué vendo, para quién, en qué país/ciudad, precios]
Tu tarea principal es: [ej. responder dudas y ayudar a cerrar ventas por WhatsApp]
Tu tono es: [ej. amable, breve, latino, sin ser demasiado formal. Usa emojis con moderación]
Información clave que debes usar: [pegar aquí FAQs, productos, envíos, métodos de pago]
Reglas: Nunca inventes precios. Si no sabes algo, di esto: [...]. Siempre termina con una pregunta para avanzar la venta.
Formato de respuesta: Máximo 4 líneas, listo para copiar y pegar.
```

**Paso a paso en pantalla:**
1.  **10 min - Pega tu contexto:** Completan la plantilla con info real de su startup.
2.  **10 min - Crea tu asistente:** Lo configuran en ChatGPT / Gemini Gem / Claude Project, versión gratuita.
3.  **15 min - Primera prueba:** Lo prueban con 3 preguntas reales que les haría un cliente/usuario.
4.  **15 min - Ajusta en tu mesa:** Intercambian laptop con el de al lado, intentan "romper" el asistente del otro y dan feedback.

**Key Takeaway:** "Tu primera versión va a ser un 6/10. Perfecto. Hoy aprendes a llevarla a 9/10 iterando."

#### BLOQUE 6: Rómpelo y mejóralo
**Duración:** 20 min | **Slides:** 4

**Objetivo:** Aprender a corregir, no a empezar de cero.
**Dinámica:** Charla corta + ejercicio de mejora en vivo.
Enseñas 3 arreglos que solucionan el 90% de los errores: 1) "Sé más breve/concreto", 2) Darle un buen y un mal ejemplo de respuesta, 3) Agregar una regla para lo que está haciendo mal. Voluntario comparte su error en pantalla y lo arreglamos entre todos.

**Key Takeaway:** "No se le pide mejor a la IA. Se le da mejor contexto y mejores ejemplos."

#### BLOQUE 7: Showcase relámpago
**Duración:** 15 min | **Slides:** 1

**Objetivo:** Inspiración entre pares y validación social.
**Dinámica:** Presentaciones voluntarias de 60 segundos.
5-6 emprendedores muestran: qué construyeron, para qué, y una respuesta real del asistente. Aplauso y feedback rápido del grupo: 1 cosa buena, 1 idea para mejorar.

**Key Takeaway:** "Las mejores ideas para tu asistente van a salir de ver lo que hizo otro emprendedor como tú."

#### BLOQUE 8: Cierre y plan de 7 días
**Duración:** 10 min | **Slides:** 3

**Objetivo:** Que no quede en un ejercicio bonito de una tarde.
**Dinámica:** Charla de cierre + compromiso público.
Presentas el Plan de 7 Días: Día 1-2 usarlo tú, Día 3-4 probarlo con clientes reales, Día 5 ajustarlo, Día 6-7 enseñárselo a tu equipo. Cada uno escribe en un post-it dónde lo va a usar mañana y lo pega al salir.

**Key Takeaway:** "Un asistente que no usas esta semana, no lo vas a usar nunca. Mañana, primera prueba real."

### 4. RECURSOS PARA LLEVAR A CASA

Todo entregado vía QR gigante en la última slide y grupo de WhatsApp del workshop:

1.  **Toolkit del Asistente (PDF + Notion/Google Docs editable):** Plantilla de Prompt Maestro lista para copiar/pegar
2.  **Canvas del Asistente en blanco** para crear el segundo y tercer asistente
3.  **Biblioteca de 30 Prompts Listos:** 10 para ventas, 10 para contenido, 10 para productividad
4.  **Checklist de Seguridad:** Qué información NUNCA subir a una IA
5.  **Guía rápida de herramientas gratuitas:** Comparativa simple ChatGPT vs. Claude vs. Gemini para no-técnicos
6.  **Slides del workshop + grabación de la demo**
7.  **Invitación a comunidad de WhatsApp** para compartir avances durante los 7 días

### 5. RESUMEN DE SLIDES

Total estimado: **30 slides.** Es un workshop práctico, la pantalla manda menos que las laptops.

Bloque 1: 4 | Bloque 2: 6 | Bloque 3: 2 | Bloque 4: 5 | Bloque 5: 4 | Bloque 6: 4 | Bloque 7: 1 | Bloque 8: 3 | Slide de Break: 1

**Tip de facilitador para LatAm:** Ten siempre un Plan B sin internet. Si se cae el WiFi, el ejercicio se hace igual completando el Canvas y la plantilla en papel. La herramienta cambia, el método es el mismo.