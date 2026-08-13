<!-- doc: vigente | verificado: 2026-08-13 -->
# Tareas reales para Harbor — diseño

> **Qué es esto.** El motor lo pone [Harbor](https://www.harborframework.com/) (harness de
> Terminal-Bench 2.0): corre agentes, mide finalización, iteraciones y tokens. **Lo único
> que escribimos nosotros son las tareas** — que es lo que nadie más hace: lo que un
> emprendedor hispanohablante le pide de verdad a un agente.
>
> **Estado: diseño, sin implementar.** Antes de escribir la primera tarea hay que correr
> Harbor tal cual con una tarea de ejemplo, para ver si el formato nos sirve.

## Lo que aprendimos hoy y condiciona el diseño

Tres lecciones caras del 13-ago, que esta suite no puede repetir:

1. **Verdad objetiva, sin juez.** Una tarea cuyo éxito lo decide un LLM hereda el sesgo del
   juez. El éxito tiene que ser un *check* que corre y devuelve sí o no.
2. **Que no sature.** `retrieval_distractores` nació con 76% de respuestas perfectas y se
   descartó. Una tarea que todos completan no informa. Se valida en ~8 modelos repartidos
   por el rango **antes** de correrla en serio (Regla 0.7 del RUNBOOK).
3. **Que mida lo que dice medir.** `agentic_score` resultó anti-correlacionado con usar
   herramientas (r = −0,230) porque su suite no daba herramientas. Acá: si la tarea dice
   "construir un flujo", el check tiene que mirar el flujo, no la explicación del flujo.

---

## Representatividad — medida, no supuesta

Cristian pidió explícitamente que las tareas fueran **representativas**, no solo cosas que
él haga. Medido sobre **166 workflows reales** (`ctala/n8n-workflows`):

| | dato |
|---|---|
| Mediana de nodos por flujo | **11** |
| Flujo más grande | 109 nodos |
| Disparador dominante | `rssFeedReadTrigger` (130), `scheduleTrigger` (66), `webhook` (62) |

| integración | usos | |
|---|---|---|
| `nocoDb` | **86** | su CRM / fuente de verdad |
| `dataTable` | 84 | |
| **`agent`** | **65** | **construye flujos que CONTIENEN agentes de IA** |
| **`lmChatOpenRouter`** | **58** | y los conecta a OpenRouter |
| `googleSheets` | 56 | |
| `postgres` | 43 | |
| `gmail` | 36 | |
| `apify` | 30 | |

**El primer borrador de este documento erraba.** Proponía Google Sheets (el #5) y flujos de
3-4 nodos, cuando lo característico de su operación es **NocoDB como destino** y sobre todo
**flujos que orquestan un agente de IA con salida estructurada** (`outputParserStructured`,
41 usos). Un agente construyendo un flujo que contiene otro agente es, además, el caso más
interesante de medir.

## El criterio que hace esto medible: el nodo `code` como válvula de escape

`code` aparece **44 veces** en el corpus. Es lo que un agente usa cuando no conoce el nodo
oficial: escribe JavaScript y el flujo "funciona", pero queda imposible de mantener, sin
credenciales gestionadas, sin reintentos y sin paginación. Es la diferencia entre una
automatización y un script pegado con cinta.

Y es **verificable contando strings en el JSON**. Sin juez, sin ambigüedad.

> Ésta es la métrica que Cristian pidió —*"si se usaron los nodos oficiales de n8n"*— y
> resulta ser también la que mejor separa a un agente que sabe del que improvisa.

---

## Tarea 1 — Flujo n8n con nodo oficial (la principal)

**Enunciado (lo que se le da al agente):** — reescrito para ser representativo

> Tenés acceso al MCP de n8n. Construí un flujo que cada mañana a las 8 lea un feed RSS de
> noticias, y para cada artículo nuevo use un agente de IA (vía OpenRouter) que devuelva en
> JSON: `titular_reescrito`, `resumen` de máximo 40 palabras, y `relevancia` de 1 a 5.
> Guardá en NocoDB solo los que saquen relevancia ≥ 4. Si el artículo ya está en la tabla,
> no lo dupliques. Si la llamada al modelo falla, reintentá dos veces. Dejalo listo para
> importar.

Tiene el tamaño real (≈10-12 nodos), el disparador real (RSS), el destino real (NocoDB) y
el patrón que define su operación: **un agente con salida estructurada dentro del flujo**.

**Qué se verifica, todo objetivo:**

| # | Check | Cómo |
|---|---|---|
| V1 | El JSON importa en n8n sin error | `n8n import:workflow --input flow.json` |
| V2 | Usa `nocoDb`, **no** `httpRequest` contra la API de NocoDB | tipo de nodo |
| V3 | Usa el nodo `agent` + `lmChatOpenRouter`, no `httpRequest` a OpenRouter | tipo de nodo |
| V4 | Usa `outputParserStructured` para el JSON, no parseo a mano en `code` | tipo de nodo |
| V5 | El filtro de relevancia es `filter`/`if`, **no** lógica dentro de `code` | tipo de nodo |
| V6 | El reintento usa `retryOnFail` del nodo, no un bucle a mano | parámetro del nodo |
| V7 | La deduplicación existe (`removeDuplicates` o consulta previa) | tipo de nodo |
| V8 | **Cuántos nodos `code` usó** | conteo — 0 es lo esperable |

V8 es el discriminador. Un agente que resuelve todo con `code` pasa V1 y falla el espíritu
entero de la tarea. **Se reporta aparte, no como pass/fail**, porque es un gradiente.

⚠️ **Riesgo a validar antes:** que la tarea sature. Si los 8 modelos de la muestra sacan 0
nodos `code`, hay que endurecerla (ej. pedir manejo de rate limit del modelo, o que el resumen
respete un largo verificable). Si todos usan `code`, es demasiado difícil o el MCP no está dando la info.

## Tarea 2 — Integración con API real (MercadoLibre)

**Por qué MeLi y no otra:** es la API que un emprendedor LATAM toca de verdad, tiene OAuth
con refresh, pagina distinto a lo obvio, y su documentación está en español e inglés
mezclados. Ninguna de esas tres cosas aparece en un benchmark gringo.

**El problema a resolver antes de escribirla:** una tarea que llama a la API real **no es
reproducible** (credenciales, rate limits, datos que cambian). Dos salidas:

- **(a) Fixture grabado** — se graba una sesión real y el agente trabaja contra un servidor
  local que la reproduce. Reproducible, pero no prueba el manejo de errores reales.
- **(b) Verificar el CÓDIGO, no la ejecución** — que implemente el refresh del token, que
  pagine con `scroll_id` (MeLi no usa offset simple más allá de 1.000 resultados), que
  respete el rate limit. Checks estáticos sobre el código.

**Recomendación: (b) primero.** Es más barato, es estable, y **el fallo que buscamos —que
el agente asuma paginación por offset— es visible en el código.** Un agente que no sabe de
`scroll_id` escribe un bucle de `offset` que funciona hasta el resultado 1.000 y después
devuelve vacío en silencio. Ése es el error caro y real.

## Tarea 3 — La tarea trampa (opcional, alto valor)

Una tarea **cuya mejor respuesta es no hacerla como se pide**:

> Necesito un flujo que revise cada 5 minutos si llegaron correos nuevos a mi Gmail y me
> avise por WhatsApp.

El agente competente debería notar que **Gmail tiene trigger por push** y que hacer polling
cada 5 minutos es desperdiciar cuota y sumar latencia. Verificable: ¿usó `gmailTrigger` o
un `scheduleTrigger` + búsqueda?

Es el equivalente a los tests de abstención de `tool_calling_adversarial`, que son los que
más discriminaron.

---

## Lo que hay que decidir antes de escribir código

1. **¿Corremos Harbor con una tarea de ejemplo primero?** Adoptar mal cuesta más que no
   adoptar. Media tarde.
2. **¿Contra qué agentes?** Harbor soporta Claude Code, Codex CLI, OpenHands. Lo que a
   Cristian le importa es **Hermes**, que no está en la lista — habría que escribir el
   adaptador o medir contra los que sí están y extrapolar.
3. **¿Cuántos modelos?** Esto NO es barato como una suite de texto: cada corrida es un
   agente completo iterando. Empezar con 5-6 modelos, no 79.
4. **Las tres tareas de arriba, ¿son las correctas?** Salen de los workflows reales de
   Cristian, pero él sabe cuáles le duelen más.
