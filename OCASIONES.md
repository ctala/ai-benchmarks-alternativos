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
- **Filtro de relevancia de Eco:** en sus 58 casos casi todos aciertan; sirve el más barato disponible que no deje pasar una nota vetada (§ «Etapas donde sirve el más barato»). No se mide en el ranking; queda como regresión.
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
- **Gate de noticias de Eco:** la verificación de claims, la extracción de claims y la traducción de fragmentos entran en «Etapas donde sirve el más barato» y quedan como regresión: en sus casos casi todos aciertan.
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

## Etapas donde sirve el más barato (9-nov-2026)

Cuando en los casos de una etapa casi todos los modelos aciertan, la conclusión es **«en estos casos
casi todos aciertan, así que sirve el más barato disponible»**. No es «cualquier modelo sirve en
producción»: los casos cubren lo que conocemos, no todo lo que puede llegar. La etapa no se mide en
todo el ranking (gasta sin aportar decisión) y sus casos quedan en `benchmarks/tests/` como
**prueba de regresión** (`fuera_por: "regresion"` en `suites.py`: no se miden en lotes ni se
publican), con `--fuera-del-examen`. **Cada fallo real de Eco
en esa etapa se agrega como caso nuevo.** Fila en `DECISIONES.md`.

**«El más barato» cumple dos condiciones:**
1. Pasa la regla de disponibilidad de «el más barato» (DECISIONES, fila del 9-nov): 6 pings de
   `check_endpoints.py` separados 10 minutos, al menos 5 VIVO y ningún MUERTO.
2. No deja pasar **ningún** caso que había que bloquear o vetar. Bloquear de más es tolerable;
   dejar pasar un dato falso o una nota vetada, no.

| Etapa de Eco | Casos | Validación (8 modelos) | ¿Dejó pasar algo? | Conclusión |
|---|---|---|---|---|
| Filtro de relevancia (`noticias_relevancia`) | 58 | 7 de 8 sacan 58/58; Qwen 3-Next 80B falla 5 (las fallas de Gemma 4 31B eran errores 429) | No: las 5 son falsos «no pasa» | Sirve el más barato disponible |
| Verificación de claims (`noticias_verificacion`) | 30 | 98 % de runs perfectos, rango 9,82-10,00 | No: 0 de 240 decisiones del gate distintas; ningún falso RESPALDADO | Sirve el más barato disponible |
| Extracción de claims (`noticias_extraccion`) | 25 (258 afirmaciones) | sd 0,26, rango 9,16-9,87; cada modelo omite 0 a 8 y casi siempre distintas | Condición: no omitir más que Flash Lite GA, ninguna cifra, ninguna del último párrafo | Sirve el más barato disponible |
| Traducción de fragmentos (`noticias_traduccion`) | 15 | 94 % de runs perfectos, sd 0,15 | Condición: ninguna cifra ni unidad alterada (solo Qwen 3-Next 80B dejó «100亿 원») | Sirve el más barato disponible |

**La conclusión se vuelve decisión para Eco** así: entre los modelos vigentes de `models.py`
(rankeados o no: el ranking exige Harbor, que no tiene que ver con filtrar o verificar), del más
barato hacia arriba, el primero que pasa la regresión (los 88 casos de filtro y verificación sin
dejar pasar ninguno, más las condiciones de extracción y traducción) y después los 6 pings. Gemini 3.1 Flash Lite GA, la línea base de Eco, corre siempre la regresión.

**Recomendación del 9-nov-2026** (es recomendación: el cambio en n8n lo decide Cristian, una
etapa a la vez; el detalle está en la fila de DECISIONES):

| Modelo | Precio por millón (entrada / salida) | Filtro | Verificación | Extracción (omitidas de 258) | Traducción |
|---|---|---|---|---|---|
| Gemini 3.1 Flash Lite GA (Eco hoy) | $0,25 / $1,50 | 58/58, 0 vetadas | 30/30, 0 falsos RESPALDADO | 7, 0 cifras, 0 finales | 0 alteradas |
| **Ling 3.0 Flash** (`deepinfra/bf16`) | $0,06 / $0,18 | 58/58, 0 vetadas | 30/30, 0 falsos RESPALDADO | 4, 0 cifras, 0 finales | 0 alteradas |
| Ling 3.0 Flash VL | $0,06 / $0,18 | 58/58, 0 vetadas | 30/30, 0 falsos RESPALDADO | 1, 0 cifras, 0 finales | 0 alteradas |

Ling 3.0 Flash es el más barato vigente que pasa las condiciones y cuesta unas 6 veces menos que
Flash Lite GA. Se recomienda fijado a `deepinfra/bf16`, que es donde se midió: el precio general de
OpenRouter ($0,021 / $0,063) es Novita, que no está medido.

Redacción sigue como ocasión medida: separa modelos (55 % de runs perfectos, sd 0,85).

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

## Preguntas para Cristian (respondidas el 3-nov-2026, salvo la 5)

1. **Fusionar «Vender» y «Responder a clientes» en una sola: Relación comercial.** → Sí. Quedan seis ocasiones.
2. **«Educación y cursos»** → dentro de «Escribir para publicar». No es ocasión propia.
3. **Volumen por ocasión** → defectos: Escribir 100 piezas/mes · Relación comercial 500 mensajes ·
   Automatizar 3.000 ejecuciones · Decidir con documentos 50 documentos · Programar 200 tareas.
   La calculadora los muestra y deja cambiarlos.
4. **Programar solo con el banco de código real; `code_generation` se jubila del titular** → Sí, con una
   condición de Cristian: *"es distinto usar el agente con conversación en español, eso sí lo
   mantendría de alguna manera"*. Las tareas de Harbor se piden en español de founder no programador
   (enunciado, aclaraciones y criterios en español); lo que se verifica sigue siendo el test que pasa.
5. **Apps reales de «Automatizar»** → pendiente. Cristian preguntó cuánto cuesta sumar Sheets y Gmail, y si
   NocoDB es copia de otro benchmark o aporte propio. Ver «Automatizar: qué se copia y qué es nuestro».

**Bump:** el corte es **mayor (v5.0.0)**, decidido el 3-nov-2026.

## Automatizar: qué se copia y qué es nuestro (3-nov-2026)

**Lo que se copia es el método, no el stack.** Toolathlon (HKUST, arXiv 2510.25726) mide 108 tareas sobre
32 apps y 604 herramientas: estado inicial realista, el agente ejecuta, y un script determinístico por tarea
compara el **estado final de la app** contra el esperado. Mezcla servicios remotos (Google Sheets, Notion)
con apps open source en contenedor (poste.io como correo, Canvas LMS, WooCommerce, Kubernetes). El mejor
modelo ronda 39 % pass@1 (cifra de segunda mano).

**NocoDB no está en Toolathlon ni en ningún benchmark público encontrado.** Es aporte propio: el destino de
86 de los 166 flujos de n8n de Cristian. Lo que nadie más mide es «el stack que usa un founder LATAM con
n8n», en español, con datos de acá (RUT, CLP/MXN, nombres).

**Costo de sumar las otras dos apps:**
- *Correo:* Gmail real es impracticable (OAuth, correos reales, limpieza entre corridas); Toolathlon mismo lo
  reemplazó por poste.io. Hacemos igual: servidor de correo en contenedor con la misma superficie de
  herramientas (buscar, leer, responder, etiquetar). Una sesión.
- *Sheets:* Toolathlon lo usa real y remoto. Para nosotros: proyecto de Google Cloud, cuenta de servicio, una
  hoja por tarea que se resetea por corrida, cuota de 300 req/min. Una a dos sesiones. El riesgo es
  credenciales y limpieza, no el modelo.

**Orden propuesto:** NocoDB (sesión 1) → correo en contenedor (sesión 2) → Sheets real (sesión 3). Al final,
una tarea cruzada que es literalmente un flujo de Cristian: llega un lead por correo → se registra en NocoDB
→ se anota en la hoja. Esa es la tarea larga al estilo Toolathlon. Y el correo trae la trampa que ningún
benchmark de agentes mide en español: instrucciones escondidas en el mensaje (`prompt_injection_es`).

> **Objeción de Cristian (3-nov-2026), después de leer lo anterior:** *"NocoDB como prueba no sé si aporta
> mucho, y las otras como Gmail Toolathlon ya la tiene. No estamos aportando algo realmente valioso."*
> Tiene razón: la app no es el valor. Lo que ningún benchmark público da es (a) la misma tarea en español
> contra su versión en inglés, (b) tareas a escala de founder con datos LATAM y trampas que cuestan dinero,
> (c) los modelos baratos, abiertos y locales que Toolathlon no mide, y (d) el precio mensual a volumen con
> pass^k. El orden NocoDB → correo → Sheets de arriba queda **suspendido** hasta decidir eso.

## Enriquecer, no replicar (dirección de Cristian, 3-nov-2026)

> *"Podemos usar los resultados de los distintos benchmarks y enriquecerlo con lo propio. Aquí el resultado
> debe de ser útil."*

Por ocasión, tres columnas y una recomendación que sale de cruzarlas:

1. **Lo que ya midieron otros, independientes** (banda informativa desde el 3-nov, no filtro): Terminal-Bench y SWE-bench para Programar;
   Toolathlon y τ²-bench para Automatizar y Relación comercial; Artificial Analysis para velocidad y precio;
   la categoría *Spanish* de LMArena como única señal pública en español (preferencia, no verificable).
   Solo leaderboards independientes, nunca la tarjeta del vendor (lección Ornith). Cada celda con fuente y fecha.
2. **Lo que nadie mide y nosotros sí:** la misma tarea en español vs inglés (el «gap español»), tareas a
   escala de founder con datos LATAM y trampas que cuestan dinero, pass^k, y los modelos baratos, abiertos y
   locales que los leaderboards no cubren.
3. **Precio mensual al volumen declarado** de la ocasión.

**Consecuencias:** `Programar` toma el filtro de Terminal-Bench/SWE-bench y agrega solo tareas de Harbor en
español de founder. `Automatizar` no replica apps: toma Toolathlon/τ²-bench y agrega pocas tareas en español
con trampa. Las suites propias que sobreviven son las que miden algo que no está afuera.

**Riesgos a resolver antes de construir:** cobertura (los leaderboards traen 20-40 modelos; de nuestros 115,
muchos quedarán «sin dato público» y hay que decir qué se hace con ellos), comparabilidad entre harnesses
distintos (no se promedian: se muestran como bandas), caducidad (ingesta por script con fecha, no a mano;
precedente: `effort.py --actualizar` ya trae datos de OpenRouter).

**Resuelto el 3-nov-2026 (DECISIONES):** la cobertura se midió y no sostiene un filtro. La foto de
Terminal-Bench 2.0 es de mayo: 5 de 115 con Terminus 2, 14 con cualquier agente, y la familia actual no
aparece; Toolathlon y SWE-bench Pro no se pueden ingestar. Las fuentes externas quedan como banda
informativa (solo con la misma versión exacta), el conjunto base es vigentes del índice ∩ llamables por
OpenRouter, y `sin_dato_comunitario` es la norma. La dirección aguanta porque se apoya en la capa propia.

## Modelos sin dato público: medirlos nosotros con el harness oficial (Cristian, 3-nov-2026)

> *"En los modelos que ellos no midan, podríamos analizar si hacemos las mediciones. Por ejemplo, lo de
> Qwen 3.8 contra Ornith es importante que exista. Y eso lo podemos publicar en nuestro benchmark y hacerle
> referencia desde Hugging Face."*

- **Qué:** correr el **harness oficial** del benchmark externo (no una imitación) sobre los modelos que su
  leaderboard no cubre, y publicar el resultado como «corrida independiente con el harness oficial», con
  logs, fecha, versión del harness y costo. Donde el leaderboard acepte envíos por PR, se envía: la cita
  más fuerte es aparecer en el leaderboard de ellos.
- **Primer caso:** Qwen 3.8 Flash vs Ornith 1.5 (RL fine-tune de Qwen, MIT, solo cifras del vendor). Hoy la
  única evidencia externa es nuestro 3/8. Una corrida con el harness oficial es la primera independiente
  que existiría, y se publica en la discusión del repo del modelo en Hugging Face y en la nuestra.
- **Orden:** Terminal-Bench primero (todo en contenedor, sin cuentas remotas, harness maduro) → Toolathlon
  después (necesita cuentas de Google y Notion). Los modelos abiertos chicos pueden correr en el Spark por
  `sparkctl`, a costo cero de API, cuando Cristian lo autorice.
- **Riesgo de proceso:** esto es medir **fuera del runner**, y `check_caminos` lo sanciona por diseño. Hace
  falta un camino declarado (`externos/` con procedencia, recibo de presupuesto y checksum del harness) y su
  fila en `DECISIONES.md` antes de la primera corrida. No se salta el guardrail: se le abre una puerta con
  nombre.
- **Honestidad al publicar:** «medido por nosotros con el harness oficial vX, N intentos, fecha» y nunca
  «según Terminal-Bench». La diferencia es la que le reprochamos a Ornith.

**Dato que abarata el primer caso:** nuestro banco `tareas-agente/harbor-*` ya corre sobre
[Harbor](https://www.harborframework.com/), el harness de Terminal-Bench 2.0 (`PLAN-TAREAS-HARBOR.md`,
`export_harbor.py`, `jobs/`). Correr el set oficial de Terminal-Bench 2 sobre Qwen 3.8 Flash y Ornith 1.5 es
cambiar el set de tareas, no montar infraestructura nueva.

**Qué fuentes externas entran y cuáles no → `FUENTES-EXTERNAS.md`** (criterio de cinco puntos y veredicto por fuente, 3-nov-2026).
