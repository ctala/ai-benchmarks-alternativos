# Claude Fable 5.1 — startup_content/workshop_outline

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.7 | quality: 10.0
- latency_total: 113.957s | tokens_per_second: 72.0
- input_tokens: 316 | output_tokens: 8209
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil para emprendedores no técnicos, proporcionando una agenda detallada, materiales necesarios y un ejercicio principal bien estructurado.

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

# Workshop: "Construye tu Asistente de IA para tu Startup"
### Workshop Práctico · 3 horas · 20-30 emprendedores early-stage

---

## 🎯 Promesa del workshop

> "Entras con una idea de negocio y un celular. Sales con un asistente de IA funcionando, entrenado con el contexto de TU startup, que puedes usar mañana mismo."

Sin código. Sin jerga. Sin diapositivas de 40 minutos sobre "qué es un LLM".

---

## 1. Agenda General (180 min)

| Hora | Bloque | Duración | Tipo |
|---|---|---|---|
| 0:00 – 0:15 | **Arranque: Rompe el hielo y el miedo** | 15 min | Dinámica + charla |
| 0:15 – 0:35 | **La IA sin humo: lo que realmente necesitas saber** | 20 min | Charla + demo en vivo |
| 0:35 – 1:05 | **Taller 1: El prompt que vale oro** | 30 min | Ejercicio individual + parejas |
| 1:05 – 1:15 | ☕ **Pausa** | 10 min | — |
| 1:15 – 1:30 | **Diseña tu asistente: ¿qué problema le vas a dar?** | 15 min | Ejercicio con canvas |
| 1:30 – 2:20 | **Taller 2 (EJERCICIO PRINCIPAL): Construye tu asistente** | 50 min | Build en vivo, guiado |
| 2:20 – 2:30 | ☕ **Pausa corta** | 10 min | — |
| 2:30 – 2:50 | **Demo Day relámpago** | 20 min | Presentaciones + feedback |
| 2:50 – 3:00 | **Cierre: tu plan de 7 días** | 10 min | Compromiso + recursos |

**Tiempo de hands-on real: ~95 minutos (más del 50%).** Eso es intencional.

---

## 2. Materiales Necesarios (Preparar ANTES)

### 📋 Checklist del facilitador (1 semana antes)

**Logística**
- [ ] Sala con mesas para trabajo en grupos de 4-5 (no auditorio tipo cine)
- [ ] WiFi probado con 30 dispositivos simultáneos (pide la clave en grande, impresa en cada mesa)
- [ ] Proyector + adaptadores HDMI/USB-C
- [ ] Regletas/extensiones eléctricas en cada mesa (los celulares mueren)
- [ ] Parlante para música en pausas y dinámicas

**Herramientas de IA**
- [ ] Decidir la herramienta principal: **ChatGPT (Projects/GPTs)**, **Claude (Projects)** o **Gemini (Gems)**. Recomendación: elige UNA y sé consistente. Ten un plan B si una cae.
- [ ] Email previo a participantes: "Crea tu cuenta gratuita en [herramienta] antes del workshop" (el 40% no lo hará, así que reserva 5 min para esto)
- [ ] Cuenta de respaldo del facilitador con plan pago para demos sin límites
- [ ] Probar que la herramienta funciona en celular Android e iPhone (muchos no traerán laptop)

**Materiales impresos (1 por persona)**
- [ ] **Canvas "Mi Asistente de IA"** (1 hoja, ver sección 4)
- [ ] **Cheat sheet de prompts** (1 hoja, doble cara)
- [ ] **Hoja de "Plan de 7 días"**
- [ ] Post-its de 3 colores + marcadores en cada mesa

**Digital**
- [ ] Link corto (bit.ly o similar) a carpeta con: slides, plantillas de prompts en texto plano, lista de recursos
- [ ] Código QR del link en la última slide y en cada mesa
- [ ] Grupo de WhatsApp del workshop (creado el día anterior, útil para compartir links en vivo)
- [ ] 3 asistentes de ejemplo ya construidos y probados (ver bloque 5)

**Equipo**
- [ ] 1 facilitador principal + **mínimo 2 ayudantes** circulando por las mesas durante el ejercicio principal. Con 30 personas no-técnicas, esto no es opcional.

---

## 3. Bloques Detallados

---

### 🟢 BLOQUE 1: Arranque — Rompe el hielo y el miedo
**Duración:** 15 min | **Slides:** 4

**Objetivo**
Bajar la ansiedad tecnológica, generar energía y que cada persona diga en voz alta el problema de su negocio.

**Dinámica**
- **(2 min)** Bienvenida directa. Nada de "agradezco a los organizadores por 5 minutos". Promesa del workshop en una frase.
- **(5 min)** Dinámica "El dolor de la semana": cada persona en su mesa dice en 20 segundos: nombre, qué hace su startup, y **una tarea repetitiva que odia hacer**. Un ayudante anota las tareas en post-its y las pega en una pared visible.
- **(5 min)** Facilitador lee 5-6 post-its en voz alta y dice: "Esto. Esto es lo que vamos a atacar hoy." Conecta las tareas con lo que un asistente puede hacer.
- **(3 min)** Reglas del juego: celular abierto está bien, preguntas tontas no existen, si te trabas levanta la mano con el post-it rojo.

**Key takeaway**
> "No vienes a aprender IA. Vienes a quitarte trabajo de encima."

---

### 🟢 BLOQUE 2: La IA sin humo — lo que realmente necesitas saber
**Duración:** 20 min | **Slides:** 8

**Objetivo**
Que entiendan 4 conceptos clave, nada más, y vean con sus propios ojos qué puede y qué NO puede hacer la herramienta.

**Dinámica**
- **(8 min) Charla relámpago — Los 4 conceptos:**
  1. **"Es un practicante brillante con amnesia"**: sabe de todo, no sabe nada de tu negocio, y olvida la conversación anterior si no se lo guardas.
  2. **Prompt = instrucción.** Mientras más contexto, mejor el resultado. Basura entra, basura sale.
  3. **Puede inventar.** Se llama "alucinar". Nunca confíes ciegamente en cifras, leyes o nombres.
  4. **Asistente ≠ chat.** Un asistente es un chat con instrucciones permanentes + documentos de tu negocio. Eso es lo que construimos hoy.

- **(10 min) Demo en vivo — "Antes y después":**
  - Facilitador escribe un prompt malo: *"Escribe un mensaje para mis clientes"*. Resultado genérico y malo. La sala se ríe.
  - Luego el mismo pedido con contexto: quién eres, a quién le hablas, tono, objetivo, ejemplo. Resultado 10x mejor.
  - Mostrar un error real: pedirle un dato que no sabe y ver cómo lo inventa. Fundamental para no generar falsa confianza.

- **(2 min)** Preguntas rápidas. Las complejas van al "parking lot" (hoja en la pared).

**Key takeaway**
> "La diferencia entre un resultado inútil y uno excelente no es la herramienta. Es el contexto que le das."

---

### 🟢 BLOQUE 3: Taller 1 — El prompt que vale oro
**Duración:** 30 min | **Slides:** 5

**Objetivo**
Que cada persona escriba y pruebe un prompt estructurado para una tarea real de su negocio antes de construir el asistente.

**Dinámica**
- **(5 min)** Presentar la fórmula **R-C-T-F** (impresa en la cheat sheet):
  - **Rol:** "Actúa como un experto en..."
  - **Contexto:** "Mi startup hace X, para clientes Y, en [ciudad/país]..."
  - **Tarea:** "Necesito que..."
  - **Formato:** "Dámelo en una tabla / en 3 bullets / en tono informal / máximo 100 palabras"

- **(10 min) Ejercicio individual:** Cada uno toma la tarea del post-it del Bloque 1 y escribe un prompt R-C-T-F en su celular/laptop. Lo ejecuta. Lee el resultado.

- **(10 min) Ejercicio en parejas — "Dale una vuelta más":** Intercambian con el vecino. El vecino lee el resultado y pregunta: "¿Qué le falta para que lo uses tal cual?". Cada uno mejora su prompt con un detalle más (un ejemplo, una restricción, un tono) y vuelve a correrlo.

- **(5 min) Puesta en común:** 2-3 voluntarios leen su "antes y después". El facilitador señala qué cambió.

**Key takeaway**
> "Tu primer prompt nunca es el bueno. El segundo sí. Itera como iteras tu producto."

---

### ☕ PAUSA — 10 min
Música. El facilitador y ayudantes revisan quién no logró crear cuenta y lo resuelven ahora.

---

### 🟢 BLOQUE 4: Diseña tu asistente — ¿Qué problema le vas a dar?
**Duración:** 15 min | **Slides:** 4

**Objetivo**
Que cada persona defina en papel, antes de tocar la herramienta, UN asistente con UN trabajo claro.

**Dinámica**
- **(3 min)** Presentar el **Canvas "Mi Asistente de IA"** (hoja impresa). Mostrar los 3 asistentes de ejemplo ya construidos:
  1. **"Respondedor de WhatsApp"** para una tienda de ropa en Instagram (atención al cliente)
  2. **"Redactor de propuestas"** para una consultora de marketing (ventas)
  3. **"Coach de pitch"** para una fundadora buscando inversión (estrategia)

- **(10 min) Llenar el canvas** (individual, en silencio, con música de fondo):
  - Nombre del asistente
  - Su único trabajo (una frase)
  - Quién lo va a usar (yo / mi equipo / mis clientes)
  - Qué tiene que saber de mi negocio (3-5 cosas)
  - Cómo quiero que hable (tono, idioma, qué nunca debe decir)
  - Cómo sabré que funciona (ejemplo de pregunta → respuesta ideal)

- **(2 min)** Regla de oro antes de pasar al build: **"Si tu asistente hace más de una cosa, hace ninguna."** Recortar.

**Key takeaway**
> "Un asistente con un trabajo claro vale más que diez que hacen 'de todo'."

---

### 🔥 BLOQUE 5: Taller 2 — Construye tu asistente (EJERCICIO PRINCIPAL)
**Duración:** 50 min | **Slides:** 6 (solo pasos, en pantalla permanente)

**Objetivo**
Que el 100% de los participantes salga con un asistente creado, con instrucciones y al menos un documento de contexto cargado, probado con 3 preguntas reales.

**Dinámica**
Ver sección 4 completa más abajo. Resumen de ritmo:
- **(10 min)** Build guiado paso a paso, el facilitador construye uno en pantalla mientras todos replican
- **(25 min)** Trabajo libre con ayudantes circulando
- **(10 min)** Prueba de estrés en parejas
- **(5 min)** Ajustes finales

**Key takeaway**
> "Lo acabas de hacer. Sin código. Sin contratar a nadie. En menos de una hora."

---

### ☕ PAUSA CORTA — 10 min

---

### 🟢 BLOQUE 6: Demo Day relámpago
**Duración:** 20 min | **Slides:** 2

**Objetivo**
Celebrar, generar aprendizaje cruzado y que vean 5-6 casos reales distintos al suyo.

**Dinámica**
- **(2 min)** Reglas: 2 minutos por persona. Muestras tu asistente en el proyector (desde tu celular, se conecta con cable o se comparte pantalla), le haces una pregunta en vivo, la sala ve la respuesta.
- **(15 min)** 6 voluntarios (o elegidos por los ayudantes durante el build, buscando diversidad de industrias). Después de cada demo, 1 comentario de la sala: "¿Qué le agregarías?"
- **(3 min)** Votación con post-its: "El asistente que más me gustaría copiar". Pequeño premio (un libro, un café, lo que sea).

**Key takeaway**
> "Viste 6 negocios distintos resolver 6 problemas distintos con la misma herramienta. Las ideas se cruzan."

---

### 🟢 BLOQUE 7: Cierre — Tu plan de 7 días
**Duración:** 10 min | **Slides:** 4

**Objetivo**
Que nadie se vaya solo con el "qué lindo" y se olvide. Compromiso concreto y recursos en la mano.

**Dinámica**
- **(4 min)** Llenar la **hoja "Plan de 7 días"**:
  - Día 1-2: Usar mi asistente en una tarea real
  - Día 3-4: Agregarle un documento más de contexto
  - Día 5-7: Mostrárselo a alguien de mi equipo / un cliente y pedir feedback
- **(2 min)** Compartir en el grupo de WhatsApp: "Esta semana voy a usar mi asistente para ______". El facilitador se compromete a responder dudas en ese grupo por 7 días.
- **(2 min)** Presentar recursos (QR en pantalla).
- **(2 min)** Cierre energético. Foto grupal.

**Key takeaway**
> "El asistente que construiste hoy es la versión 1.0. La 2.0 la construyes tú, esta semana."

---

## 4. Ejercicio Principal: "Construye tu Asistente" — Paso a Paso

**Herramienta:** ChatGPT (Projects o GPTs), Claude (Projects) o Gemini (Gems). Todas funcionan con la misma lógica: **instrucciones permanentes + documentos + chat**.

### Paso 1 — Crea el espacio (3 min)
Crear un nuevo Project/GPT/Gem. Ponerle el nombre del canvas.

### Paso 2 — Escribe las instrucciones permanentes (10 min)
Usar esta **plantilla de instrucciones** (impresa y en el link digital, para copiar y pegar):

```
Eres [NOMBRE DEL ASISTENTE], el asistente de [NOMBRE DE LA STARTUP].

SOBRE EL NEGOCIO:
- Qué hacemos: [1-2 frases]
- A quién le vendemos: [cliente ideal]
- Dónde operamos: [ciudad/país]
- Lo que nos diferencia: [1 frase]

TU ÚNICO TRABAJO:
[Una frase clara. Ej: "Responder preguntas de clientes sobre productos, precios y envíos."]

CÓMO HABLAS:
- Tono: [cercano / profesional / divertido]
- Idioma: español [neutro / de México / de Argentina / etc.]
- Siempre: [ej: tutea, usa emojis con moderación, responde corto]
- Nunca: [ej: inventes precios, prometas fechas de entrega, hables de la competencia]

SI NO SABES ALGO:
Di "Déjame confirmarlo con el equipo" y no inventes.

EJEMPLO DE RESPUESTA IDEAL:
Pregunta: [una pregunta típica]
Respuesta: [cómo quieres que responda]
```

### Paso 3 — Dale contexto real (10 min)
Subir o pegar **al menos 1 documento** del negocio. Opciones rápidas para quien no trajo nada:
- Pegar el texto de su página web o perfil de Instagram
- Pegar su lista de productos y precios desde WhatsApp
- Dictar en 3 minutos las preguntas más frecuentes de sus clientes y pegarlas
- Pegar el pitch que ya tienen escrito

*(Los ayudantes tienen en su celular una lista de "contexto de emergencia" para cada tipo de negocio.)*

### Paso 4 — Pruébalo con 3 preguntas reales (7 min)
Hacerle las 3 preguntas que un cliente / inversionista / empleado le haría de verdad. Anotar en el canvas: ✅ bien / ⚠️ regular / ❌ mal.

### Paso 5 — Prueba de estrés en parejas (10 min)
Intercambiar celular con el vecino. El vecino actúa como **cliente difícil**: pregunta algo que no está en el contexto, pide descuento, escribe con errores, pregunta algo fuera de tema. Anotar dónde falla.

### Paso 6 — Ajusta y guarda (5 min)
Volver a las instrucciones. Agregar 1-2 reglas basadas en lo que falló ("Si piden descuento, di que...", "Si preguntan por X, redirige a..."). Volver a probar. Listo.

### ✅ Criterio de éxito
Al final de los 50 min, cada participante tiene:
- [ ] Un asistente con nombre
- [ ] Instrucciones permanentes escritas
- [ ] Al menos 1 documento de contexto cargado
- [ ] 3 preguntas probadas
- [ ] 1 ajuste hecho después de la prueba de estrés

**Plan de contingencia:** Si alguien no puede crear cuenta o la herramienta se cae, trabaja en pareja con alguien de su mesa en la cuenta de esa persona. Mejor construir uno a medias que mirar.

---

## 5. Recursos para Llevar a Casa

### 📄 Físicos (entregados en el workshop)
1. **Canvas "Mi Asistente de IA"** (lleno, es suyo)
2. **Cheat sheet de prompts** — fórmula R-C-T-F + 10 prompts listos para startups:
   - Redactar respuesta a cliente molesto
   - Generar 20 ideas de contenido para Instagram
   - Resumir una reunión desde notas desordenadas
   - Escribir propuesta comercial
   - Preparar respuestas difíciles de inversionistas
   - Analizar feedback de clientes y encontrar patrones
   - Traducir mi pitch a "lenguaje de abuela" (claridad)
   - Crear descripción de puesto para mi primera contratación
   - Redactar email de cobranza amable
   - Revisar mi landing page y decirme qué no se entiende
3. **Hoja "Plan de 7 días"**

### 💻 Digitales (link + QR)
4. **Slides del workshop** en PDF
5. **Plantilla de instrucciones** en texto plano (para copiar y pegar)
6. **3 asistentes de ejemplo** con sus instrucciones completas, para inspirarse o copiar
7. **Guía "Los 5 errores que vas a cometer esta semana"** (1 página): sobrecargar al asistente, confiar en datos inventados, no actualizar el contexto, no mostrárselo a nadie, abandonarlo a los 3 días
8. **Video de 8 minutos** grabado por el facilitador repitiendo el paso a paso del build (para quien quiera rehacerlo con calma)
9. **Lista de herramientas comparadas** (ChatGPT / Claude / Gemini): qué incluye el plan gratis, cuánto cuesta el pago en USD, cuál sirve para qué
10. **Grupo de WhatsApp activo 7 días** con el facilitador para dudas

### 🎁 Bonus
11. **Mini-reto de 30 días** (opcional): un prompt por día enviado por WhatsApp para quien quiera seguir practicando

---

## 6. Slide Count Estimado

| Bloque | Slides | Notas |
|---|---|---|
| Portada + promesa | 2 | |
| 1. Arranque | 4 | Reglas, dinámica, foto de tareas |
| 2. IA sin humo | 8 | 4 conceptos (1 slide c/u) + demo + alucinación |
| 3. Taller 1: Prompts | 5 | Fórmula R-C-T-F, instrucciones del ejercicio, ejemplo antes/después |
| Pausa | 1 | Slide fija con hora de regreso + WiFi |
| 4. Diseña tu asistente | 4 | Canvas, 3 ejemplos, regla de oro |
| 5. Build (ejercicio principal) | 6 | 1 slide por paso, permanece en pantalla |
| Pausa corta | 1 | |
| 6. Demo Day | 2 | Reglas + temporizador |
| 7. Cierre | 4 | Plan 7 días, recursos + QR, foto, gracias |
| **TOTAL** | **37 slides** | **~1 slide cada 5 min. Más de eso es charla, no workshop.** |

**Regla de diseño de slides:** Máximo 15 palabras por slide. Mucha imagen, mucho ejemplo real, cero bullets de 8 líneas. Si una slide necesita explicación de más de 2 minutos, es que debería ser un ejercicio.

---

## 🔑 Notas finales para el facilitador

- **Tu enemigo es la charla larga.** Si llevas más de 10 minutos hablando sin que ellos hagan algo, perdiste la sala.
- **Los ayudantes son el 50% del éxito.** Bríefalos 30 min antes: dónde se traban los no-técnicos (crear cuenta, encontrar el botón de "instrucciones", subir archivos desde celular).
- **Celebra en voz alta cada pequeño logro.** "¡Ya tenemos 10 asistentes creados!" cambia la energía de la sala.
- **Ten el plan B listo.** Si el WiFi se cae, los celulares con datos siguen funcionando. Si la herramienta se cae, cambia a otra: la lógica es idéntica.
- **Termina a tiempo.** Un emprendedor valora más que respetes su hora que 15 minutos extra de contenido.

¡Éxitos con el workshop! 🚀