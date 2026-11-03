<!-- doc: borrador -->
<!-- creado: 2026-11-03 | pendiente de corrección de Cristian -->
# Ocasiones — la unidad en la que un emprendedor decide qué modelo usar

> **Borrador para corregir, no decisión.** Sale de la conversación del 3-nov-2026: el cómo se
> puntúa se puede cambiar (juez fuera, trampas verificables, pass^k, pilares aparte), el qué no:
> *un benchmark que le sirva a un emprendedor hispanohablante para decidir qué modelo ocupar en
> distintas ocasiones*. Este documento define esas ocasiones y qué evidencia alimenta cada una.
> Cuando se apruebe, pasa a `DECISIONES.md` y ordena el corte de medición siguiente.

## Por qué ocasiones y no suites ni pilares

Hoy el sitio ordena por pilar (Razonamiento, Coding, Contenido, Agentes) y por suite. Un miembro
de CAR no pregunta «¿quién gana en `structured_output`?». Pregunta «¿con qué escribo el
newsletter?», «¿con qué respondo a clientes?», «¿con qué armo el flujo de n8n?», «¿cuál corre en mi
Mac sin mandar datos afuera?». Una **ocasión** es esa pregunta, más la salida verificable que la
responde, más las dos o tres restricciones que la acompañan (volumen, velocidad, local, herramientas).

Lo que ya existe y se reutiliza, no se duplica:

| Fuente | Qué aporta | Qué le falta |
|---|---|---|
| `CASOS_DE_USO.md` (jul-2026) | 8 categorías y 50 casos con qué suite los mide | Su columna «modelo ideal» está a mano y caducó; no tiene restricciones ni volumen |
| Asistente del sitio (3 pasos) | Ya pregunta «¿para qué?», «¿cuánto?», «¿algo obligatorio?» | El paso 1 ofrece pilares; en agosto recomendó un modelo que fallaba 1 de 3 tareas agénticas |
| `AGENTS.md` § reglas por caso | Las 5 preguntas previas a recomendar (tarea, volumen, presupuesto, licencia, latencia) | Nombra modelos retirados; es prosa, no dato |
| `bands.py` + `RECOMENDACIONES.md` | Banda de empate estadístico y, dentro de la banda, orden por costo | Se calcula por pilar, no por ocasión |
| Survey de admisión + CRM (1.959 miembros, ago-2026) | El dolor real: no sé usar IA 29,8 % · no consigo clientes 19,4 % · falta de tiempo 7,8 % · escalar 5,9 % · no validé la idea 4,8 % | — |
| Producción de Cristian | El redactor de Eco, los 166 flujos de n8n (NocoDB 86, Sheets 56, Gmail 36, nodo `agent` 65), el código de Flip y CTM, las respuestas en CAR | Es la evidencia de «esto se pide de verdad» |

## Las siete ocasiones

Cada fila dice qué pregunta responde, de dónde sale la demanda, qué suites ya son verificables,
cuáles hay que **convertir** (hoy las decide el juez o una rúbrica de formato), qué hay que
**crear**, y qué restricciones mandan en la decisión.

### 1. Escribir para publicar
Post de LinkedIn, newsletter, noticia SEO, copy de landing, guion corto.

- **Demanda:** «no consigo clientes» (19,4 %) pasa por publicar; el redactor de Eco es el caso real (900 a 1.300 palabras, español neutro, sin inventar cifras).
- **Verificable hoy:** `content_verificable` (σ entre modelos 1,18), `integridad_idioma` (1,64), `verificar_claim`, `creativity` (0,32: separa poco).
- **Convertir:** `content_generation` (σ 0,40), `startup_content` (0,42), `presentation` (0,76), `news_seo_writing` (mixta). Trampa: dato plantado que debe aparecer, cifra que debe cuadrar, hecho que NO debe afirmarse, largo dentro de rango, cero voseo, cero CJK, llamada a la acción presente.
- **Crear:** nada nuevo hasta convertir. `video_script` (pendiente en `CASOS_DE_USO`) solo si un miembro lo pide.
- **Restricciones que mandan:** US$ por millón de tokens de **salida** (es output-heavy), razonamiento apagado (sube costo sin mejorar prosa, medido en Eco), integridad de idioma como filtro duro.

### 2. Responder a clientes y a la comunidad
Soporte con política, respuesta a una presentación de miembro, mensaje a un aplicante, seguimiento por WhatsApp.

- **Demanda:** es lo que Cristian hace a diario en CAR y lo que automatiza Nyx; el hueco «responder a un miembro con contexto propio» está detectado desde agosto.
- **Verificable hoy:** `policy_adherence` (σ 0,85), `multi_turn` (0,56).
- **Convertir:** `customer_support` (hoy juez, mixta). Trampa al estilo τ-bench: una política escrita que el modelo recibe, un dato del cliente que debe usar, una condición que obliga a escalar, un hecho que no puede inventar.
- **Crear:** suite «responder a un miembro» con presentaciones reales anonimizadas y checks: nombra el proyecto de la persona, no repite lo que ella dijo, no da consejo imperativo fuera de dominio, termina en pregunta o acción. Es la operación real del copilot.
- **Restricciones que mandan:** latencia en conversación, precio por conversación, seguridad (`prompt_injection_es`) si lee mensajes de desconocidos.

### 3. Vender: cotizar, calificar y hacer seguimiento
Cotización desde un tarifario, calificación de un lead, correo de seguimiento, propuesta.

- **Demanda:** «no consigo clientes» y «no sé cobrar» (cinco fuentes distintas entre mayo y septiembre).
- **Verificable hoy:** `sales_outreach` (σ 1,05), `business_audit` (0,71), y en Harbor `harbor-cotizar` (74 modelos, 231 corridas, cuatro trampas de tarifario) y `harbor-facturacion`.
- **Convertir:** nada: esta ocasión ya nació verificable.
- **Crear:** `lead_qualification` (pendiente desde julio): lead con datos parciales, decidir si vale seguimiento y por qué, con verdad plantada.
- **Restricciones que mandan:** fiabilidad (pass^k) por encima de calidad media: una cotización mal hecha una de cada tres veces no sirve; precio por tarea.

### 4. Automatizar con agentes
Flujos de n8n que llaman herramientas, Nyx ejecutando tareas, salida estructurada hacia NocoDB o Sheets, ruteo entre modelos.

- **Demanda:** «falta de tiempo» (7,8 %) y «escalar» (5,9 %); 65 de los 166 flujos reales contienen un nodo `agent`. Es el multiplicador de la tesis de CAR.
- **Verificable hoy:** `structured_output` (σ 1,21), `tool_calling` (fuera del índice, con `tool_calling_score_avg`), `harbor-ruteo`, `harbor-reunion`.
- **Convertir:** `tool_calling_adversarial` (hoy juez), `orchestration` y `agent_capabilities` (mixtas; el pilar Agentes mide prosa). Estándar BFCL: llamada esperada, estado final, trayectoria con tope de pasos, alucinación de herramienta.
- **Crear:** tareas al estilo Toolathlon contra instancias reales en contenedor: NocoDB con datos, una hoja de Sheets, un buzón; el check mira el **estado de la app**, no el texto. Una por ocasión agente, en Harbor, con solución oráculo.
- **Restricciones que mandan:** tiene que existir endpoint con herramientas (`sirve_para_agentes`), pass^k, velocidad bajo concurrencia (pendiente v4.1), precio por ejecución.

### 5. Entender y decidir con documentos y datos
Resumir una reunión y sacar los pendientes, auditar un P&L, extraer y verificar afirmaciones de una noticia, leer una factura, revisar un contrato.

- **Demanda:** «escalar», «no validé la idea»; el gate de noticias de Eco (extraer y verificar claims) corre en producción.
- **Verificable hoy:** `business_audit`, `business_strategy`, `deep_reasoning` (σ 0,89), `hallucination` (0,84), `extraer_claims`, `verificar_claim`, `ocr_extraction`, `strategy` (1,05).
- **Convertir:** `summarization` (hoy juez, correlación −0,20 con su propia rúbrica) con checks de datos obligatorios, pendientes con responsable y fecha, y cifra que no puede cambiar; `task_management` y `reasoning` igual.
- **Crear:** `contract_review` (pendiente desde julio) con cláusulas plantadas de verdad objetiva.
- **Restricciones que mandan:** contexto largo real (`niah_es` como filtro cuando el documento es grande), honestidad ante dato ausente, precio por documento.

### 6. Programar mi producto
Funcionalidades, bugs y refactors en el código propio, con un agente de código.

> **Duda de Cristian (3-nov-2026):** *«siempre probamos coding de manera sencilla, no sé si
> deberíamos»*. Tiene razón en el diagnóstico: `code_generation` son 4 tests de una sola llamada
> puntuados por el juez; miden «escribe un fragmento», no «programa». Opción a decidir: que esta
> ocasión tome su evidencia **solo** del banco de código real (Harbor, repos propios, tests
> ocultos, agente + modelo) y `code_generation` se jubile del titular en vez de convertirse.
> `structured_output` y `string_precision` se quedan, pero bajo «Automatizar», que es lo que miden.

- **Demanda:** «producto / MVP» es chico en el survey (1,7 %) pero es donde Cristian gasta US$730 al mes en suscripciones y donde más preguntan los miembros técnicos.
- **Verificable hoy:** `string_precision` (σ 1,11) y, sobre todo, el banco de código real del Spark: 30 tareas de commits reales de Flip (TypeScript, NestJS, Nuxt) y CTM (PHP), tests ocultos, repos privados, es decir **sin contaminación**, lo que SWE-bench Pro consigue comprando repos comerciales.
- **Convertir:** `code_generation` (hoy juez): checks que ejecutan el código contra casos, no que lo leen.
- **Crear:** línea base de Opus 5.5 en el banco de 8 y de 27 tareas (sin ella nada se declara usable), y la columna «reportado por el vendedor vs medido acá».
- **Restricciones que mandan:** agente + modelo (el techo es el modelo, no el agente), local o nube, costo por tarea resuelta, tiempo por tarea.

### 7. Correr local y que los datos no salgan
Privacidad, costo cero marginal, Spark o Mac.

- **Demanda:** «open-source / privacidad» ya es una restricción del asistente; es el caso del Spark y de los miembros con datos de clientes.
- **Es un filtro transversal, no una suite:** pesos abiertos con `weights_url`, tamaño en parámetros (`params_b`, hoy falta en 29 de 49 abiertos), memoria que exige, velocidad medida en el hardware (tok/s con 1 y con 4 usuarios), y la misma evidencia de las ocasiones 1 a 6 medida en el runtime local (el CJK de Ollama no era del modelo, era del runtime).
- **Crear:** el campo `params_b`; la tabla «qué corre en 8 / 16 / 32 / 128 GB» derivada del dato y no a mano.

## Dos ejes que no son ocasiones sino restricciones

- **Seguridad** (`prompt_injection_es`, σ 2,92: la suite que más separa de todo el benchmark). Obligatoria en cualquier ocasión donde el modelo lee texto de desconocidos (2, 4, 5).
- **Contexto largo** (`niah_es`). Obligatoria cuando el documento o el hilo supera lo que cabe en una llamada corta (2, 5, 6).

## Cómo se presenta la respuesta de una ocasión

1. **Filtro duro** por las restricciones declaradas (herramientas, abierto, local, seguridad mínima).
2. **Banda de empate** por calidad verificable de la ocasión (`bands.py`), con el intervalo publicado. Si 94 de 107 empatan, se dice.
3. **Fiabilidad** (pass^k) como segunda columna: cuántas veces de k resolvió todas las trampas.
4. **Precio para el volumen declarado**, en US$ al mes, y velocidad en el modo de uso (1 usuario o concurrente).
5. La recomendación es la banda, ordenada por precio. Nunca «el mejor es X».

El paso 1 del asistente pasa de pilares a estas siete ocasiones; los pasos 2 y 3 ya hacen el resto.

## Lo que falta, resumido por ocasión

| Ocasión | Verificable hoy | A convertir | A crear | Evidencia agéntica real |
|---|---|---|---|---|
| 1 Escribir | 4 suites | 4 | — | no aplica |
| 2 Responder | 2 | 1 | 1 | parcial (copilot) |
| 3 Vender | 2 + 2 Harbor | 0 | 1 | sí (cotizar) |
| 4 Automatizar | 2 + 2 Harbor | 3 | tareas con apps reales | no todavía |
| 5 Decidir con documentos | 8 | 3 | 1 | no aplica |
| 6 Programar | 1 + banco Spark | 1 | línea base Opus | sí (30 tareas) |
| 7 Local | filtro | — | `params_b`, tabla por GB | hereda |

Trece conversiones, cuatro suites nuevas, un banco de tareas con apps reales y dos campos de datos.
Es el alcance del corte de medición siguiente; va en una ventana declarada, con bump mayor, porque
el juez sale del titular y caduca lo publicado.

## Preguntas para Cristian

1. ¿Siete ocasiones o se funden «Vender» y «Responder a clientes» en una sola de relación comercial?
2. «Educación y cursos» era la categoría 8 de `CASOS_DE_USO`. ¿Entra como ocasión propia o queda dentro de «Escribir para publicar»?
3. ¿Qué volumen típico declaras por ocasión para que el precio salga en US$ al mes sin que el usuario lo calcule? (Ejemplo: Escribir 100 piezas al mes; Automatizar 3.000 ejecuciones.)
4. ¿«Programar» se mide solo con el banco de código real y `code_generation` se jubila del titular? (ver la nota en la ocasión 6)
5. Para «Automatizar», ¿las apps reales del banco son NocoDB, Sheets y Gmail, o prefieres empezar solo con NocoDB, que es el destino de 86 de tus flujos?
