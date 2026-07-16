# Relanzamiento v4.0 del benchmark — decisión + plan

*Aprobado por Cristian el 16-jul-2026. Sobre `benchmarks.cristiantala.com`.*
*Estado: Fase 1 (scoring congelado) — **mecanismo implementado y probado**. Ver "Estado de ejecución".*

---

## Por qué relanzar (y no solo parchear)

Tres problemas de fondo salieron a la luz. Ninguno es un bug suelto — son de diseño, y juntos justifican un corte con nombre en vez de más parches:

1. **Los números cambian a espaldas del usuario.** El score se calcula como *z-score contra la población*: cada vez que medimos un modelo nuevo, la media se mueve y **la nota de todos se recalcula**, aunque ningún modelo haya cambiado. Un benchmark cuyos números se pudren solos no se puede citar, no se puede confiar, y —comprobado— es una fábrica de bugs.
2. **La calculadora es una herramienta de experto.** El corazón son sliders de peso abstractos ("calidad 70%, costo 15%"). Un emprendedor no piensa en pesos; piensa en un caso de negocio.
3. **La tesis está enterrada.** El mensaje diferenciador —*no existe el mejor modelo; los de arriba empatan en calidad, lo que cambia es el precio*— no se ve por ningún lado.

**La oportunidad:** convertir estos tres arreglos en un relanzamiento posicionado —v4.0— con un mensaje que ningún competidor ofrece.

---

## Los tres cambios del v4.0

### 1. Scoring estable — z-score con referencia CONGELADA ✅ decidido

**El problema no es el z-score; es recalcular su referencia cada vez.** Probamos la alternativa "obvia" (normalización absoluta fija) y **falla feo**: la calidad se apelotona (todos entre 7.9 y 8.5) mientras el costo tiene rango enorme, así que sin estandarizar ganan los baratos-mediocres (Gemini Flash Lite salía #1, Opus se hundía al #47). El z-score existe para resolver eso — y lo resuelve bien. Su único defecto es la inestabilidad.

**El fix decidido:** congelar la media/desviación (`norm_stats`) + el rescale (offset/slope) en `scoring_reference.json`. Todo modelo nuevo se puntúa contra esa referencia fija. **La referencia se recalcula (recalibra) solo al cortar una versión** (`v4.0 → v4.1 …`) — *"cada vez que hacemos una versión nueva, se recalcula el z-score"*.

| | Hoy (z-score vivo) | v4.0 (referencia congelada) |
|---|---|---|
| Score al agregar un modelo | se recalcula para todos | **no se mueve** |
| Ranking dentro de una versión | cambia solo | **estable, citable** |
| Recalibración | silenciosa, en cada regeneración | **evento deliberado y versionado** |

### 2. La cara nueva — calculadora guiada (el wizard)

*(Mockup funcional ya construido y revisado.)*

- **Puerta de entrada guiada:** 3 preguntas de negocio (qué tarea · cuánto gastás · algo sensible) → **una recomendación concreta**, no una tabla.
- **El wizard configura los sliders, no los reemplaza:** el mismo motor, dos puertas. El principiante nunca ve un slider; el experto entra directo a "avanzado"; el intermedio afina a mano. Nunca se contradicen.
- **El kit multi-modelo:** como medimos por tarea, lo óptimo casi nunca es un solo modelo. La recomendación muestra el "kit" —el más barato-bueno de cada tarea— con su costo total.
- **La tesis, adelante:** *"No existe el mejor modelo. Los de arriba dan casi la misma calidad; lo que cambia, hasta 100 veces, es el precio."*
- **El contenido no se pierde:** las 65 páginas (comparaciones, "mejor para X", familias) siguen siendo el motor SEO; el wizard **enruta hacia ellas** (hub-and-spoke).

### 3. Descubrible e indexable — SEO/AEO completo

El wizard es JavaScript; Google no lo indexa. Regla: **el asistente convierte, las páginas indexan** — ambas del mismo `models.json`.

- Cada respuesta del asistente = **URL estática propia**, renderizada server-side con el contenido indexable.
- `sitemap.xml` + `llms.txt` + `llms-full.txt` actualizados en el pipeline.
- Schema: `WebApplication` + `FAQPage` + `ItemList`. OG images por página. Robots AI-aware.

---

## Cómo se mide — la página de metodología (transparencia = ventaja)

*Pedido de Cristian, 16-jul. Página pública propia (`/metodologia` o similar) + bloque resumido en la home. Es a la vez confianza para el humano y contexto para los LLM que nos citan (AEO). Escrita para alguien que no sabe nada.*

**Qué mide el benchmark.** No preguntamos a un modelo "¿esto está bien?" —cuando le preguntás eso, un juez LLM dice que sí casi siempre—. Le damos **exámenes con respuesta verificable** (¿resolvió el problema?, ¿el número es correcto?, ¿respetó el formato?, ¿se negó a filtrar una credencial?) y contamos cuántos pasa. Cada modelo corre el mismo examen decenas de veces; solo entra al ranking con **≥50 corridas válidas**.

**Las cuatro cosas que puntuamos por modelo:**
- **Calidad** — cuántos exámenes resolvió bien (0–10).
- **Precio** — cuánto cuesta correr una tarea típica, con el precio real de OpenRouter (nunca "gratis").
- **Velocidad** — cuántas palabras por segundo genera.
- **Latencia** — cuánto tarda en empezar a responder.

**Qué es el z-score y por qué lo usamos.** Acá está el truco que casi nadie explica: **la calidad de los buenos modelos se apelotona.** Los de arriba sacan todos entre 7.9 y 8.5 — diferencias chicas. El precio, en cambio, va de 3 centavos a 39 dólares por millón de tokens: un rango gigante. Si sumamos calidad y precio tal cual, **el precio aplasta a la calidad** y el ranking lo terminan ganando modelos baratos y mediocres (lo probamos: da un ranking que nadie creería).

El **z-score** arregla eso: a cada dimensión la mide *en desviaciones respecto al promedio de los modelos*, no en su escala cruda. Así "estar medio punto arriba en calidad" y "ser 10× más barato" quedan en la misma vara, y el peso que le ponés a cada cosa (calidad 70%, precio 15%…) **manda de verdad**, en vez de que el precio decida por su cuenta.

**Por qué lo congelamos por versión.** El z-score se calcula *contra la población de modelos*. Si lo recalculáramos cada vez que agregamos uno, la nota de todos se movería sin que ningún modelo cambie — números que caducan solos. Por eso **congelamos la referencia** (el promedio y la dispersión) al publicar una versión, y la recalculamos solo al sacar la siguiente. Dentro de una versión, tu número no se mueve a tus espaldas. Cuando recalibramos, lo **anunciamos** (`v4.0 → v4.1`).

**Lo que el benchmark NO hace.** No dice "este es el mejor modelo". Dice: *para esta tarea, con este presupuesto, estos son los que rinden — y este es el más barato que lo hace bien.* Casi siempre la respuesta óptima es **usar varios modelos**, uno por tipo de tarea.

> Este contenido es la fuente del bloque "cómo se mide" del sitio y del explicador que acompaña cada score.

---

## Cómo se comunica el relanzamiento

El ángulo —el que nadie más tiene— es **la honestidad medida**:

1. **"Scores que no cambian a tus espaldas."** Un benchmark versionado, no un número que se pudre.
2. **"No te damos el #1. Te preguntamos tu caso."** La tesis hecha producto.
3. **"El más barato que hace bien lo tuyo."** Contra las listas "top 10" de siempre.

Distribución con los canales que ya existen: post pilar (reescrito) + carrusel LinkedIn + newsletter + changelog en Skool.

---

## Plan de ejecución por fases

| Fase | Qué | Estado |
|---|---|---|
| **0** | Terminar el backfill agéntico (la suite que separa a Sol/Fable) | 🔄 en curso, rama `agentic-backfill` |
| **1** | Congelar la referencia del z-score + versionado en el scoring | ✅ **mecanismo implementado y probado** (ver abajo) |
| **2** | Construir la calculadora guiada sobre el motor real (z-score congelado) | pendiente — el mockup es el plano |
| **3** | Infra SEO/AEO (URLs estáticas, sitemap, llms.txt, schema) + página "Cómo se mide" | pendiente |
| **4** | Anunciar v4.0 (pilar + carrusel + newsletter + Skool) | pendiente |

---

## Estado de ejecución (fase 1)

**Implementado y probado el 16-jul-2026** en `benchmarks/export_for_pages.py` (rama `agentic-backfill`):

- `scoring_reference.json` guarda la referencia congelada (`norm_stats` + `norm_stats_by_pillar` + `score_rescale` + `version`).
- El export la lee y NO la recalcula. **Sin archivo → cae al z-score vivo histórico** (cero regresión) y avisa por consola.
- `python export_for_pages.py --recalibrate --scoring-version vX.Y` recalcula y **congela** (evento de versión).
- **Prueba:** `frozen == live` sobre el mismo dataset = 0 diferencias (congelar captura el z-score exacto). Estabilidad garantizada estructuralmente (la referencia es un archivo constante).

**El corte de v4.0 (`--recalibrate --scoring-version v4.0`) se corre cuando el backfill agéntico termine**, sobre el dataset completo — no antes, para no congelar contra datos parciales.

### El agéntico: dentro + eje propio (decidido 16-jul)

Al validar el freeze se destapó que la suite agéntica (`agent_long_horizon`) **ha estado dentro del `quality_avg` desde abril** (2.881 runs: 2.081 viejos + 800 del backfill), no es solo el backfill. Es donde los premium (Luna/Sol/Fable) se diferencian del resto. **Decisión de Cristian:** el agéntico **sigue contando en la calidad titular** (Luna se mantiene #1 — sacarlo hundía a Luna al #3 y flotaba a Ministral 14B por el sesgo barato del compuesto, ocultando justo la diferenciación premium) **y además se expone como eje propio** (`agentic_score`) para que el wizard filtre por casos de uso agénticos.

- Cambio en el código: **puramente aditivo** (probado: 0 diferencias vs el original sobre los mismos datos). Solo agrega los campos `agentic_runs/agentic_quality/agentic_score`.
- *"Una suite a medias no debería mover el ranking"* se resuelve por operación, no por código: **no se regenera/despliega producción a mitad del backfill.** Cuando esté completo, el movimiento es señal real y aterriza en la recalibración v4.0 — deliberada y anunciada. *(Cristian: "si vamos a tener todo lo agéntico listo, ningún problema".)*

---

## Lo que NO cambia

- **Los tests, la data cruda, el método de medición** — intactos.
- **Las 65 páginas** — siguen, mejoradas con CTA de vuelta al asistente.
- **El ranking sensato** — la referencia congelada preserva el orden actual.
