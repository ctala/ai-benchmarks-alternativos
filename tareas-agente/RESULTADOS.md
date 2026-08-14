<!-- doc: vigente | verificado: 2026-08-14 -->
# Resultados de la tarea agéntica «cotizar» — Harbor

**Setup:** `harbor run -p tareas-agente/harbor-cotizar -a mini-swe-agent -m openrouter/<modelo>`,
3 intentos por modelo. Reward = tests pasados / 8, parcial por diseño.

## ⚠️ Un 0,0 no siempre significa lo mismo

Hay **dos causas distintas** de reward 0 y mezclarlas produce un ranking falso:

| causa | qué significa | ejemplo |
|---|---|---|
| **Hizo mal la tarea** | el agente corrió, escribió la cotización, y está mal | — |
| **No pudo ni intentarla** | sus endpoints **no soportan tool use**, el agente no arranca | `nousresearch/hermes-4-405b` |

Hermes 4 405B dio 0,0 en los 3 intentos con este error:

    No endpoints found that support tool use.

Nunca vio el encargo. Es exactamente la misma distinción que el runner del repo hace desde
julio con las respuestas vacías (hipo de red · rehúso de política · fallo real), y que acá
no estaba haciendo.

**Y es información valiosa, no ruido:** un modelo que no soporta herramientas **no se puede
usar en un agente**, por bueno que sea su texto. Para la pregunta "¿cuál pongo en mi
agente?", esa es una respuesta definitiva — pero se reporta como *incompatible*, no como
*malo*.

Es el segundo caso del mismo tipo: ayer `nemotron-3-nano-omni` falló las suites de tools
por lo mismo, en su endpoint `:free`.

### Pero no es el mismo caso: verificado dónde más se puede medir

Con los Nemotron la salida era medirlos por NIM, porque ahí sí están. Con Hermes **no hay
salida** (verificado el 14-ago):

| vía | estado |
|---|---|
| OpenRouter | **un solo proveedor (Nebius), `tools = no`** |
| NVIDIA NIM | **no está** — sus 102 modelos no incluyen ninguno de Nous Research |

No es un problema de ruteo que se arregle cambiando de proveedor: es una limitación real
del modelo en toda su distribución accesible hoy. Eso lo vuelve un **dato publicable**:

> **Hermes 4 405B no se puede usar como cerebro de un agente que necesite herramientas.**
> Da igual que su calidad de texto sea 8,20.

Es justo lo que la pregunta que originó este trabajo venía a capturar —*"puede ser muy
eficiente en costo/calidad, pero si no lo puedo usar es otra cosa"*— y que el índice de
calidad no muestra.

## Resultados

| modelo | calidad publicada | reward (3 intentos) | runtime | nota |
|---|---|---|---|---|
| `tencent/hy3` | 8,53 | **1,0** | 4m 21s | |
| `z-ai/glm-5` | 8,33 | **1,0** | 2m 02s | |
| `nousresearch/hermes-4-405b` | 8,20 | — | 1m 09s | **incompatible: sin tool use** |
| `upstage/solar-pro4` | 8,03 | 1,0 (1 intento) | | |
| `qwen/qwen3-coder` | 7,74 | **0,67** (1 intento) | | falla parcial real |

*(lote en curso; se completa al cerrar)*

## Lo que ya se puede decir

1. **La tarea discrimina en la cola, no en la cabeza.** Los modelos de arriba la resuelven
   siempre; `qwen3-coder` (7,74) falla parcialmente. Sirve como **piso de usabilidad**, no
   para ordenar el top.
2. **El tiempo separa donde el reward empata.** GLM-5 resuelve en 2m02 lo que Tencent Hy3
   tarda 4m21 — mismo resultado, menos de la mitad del tiempo.
3. **El andamiaje hace buena parte del trabajo.** En la versión single-shot estos mismos
   modelos sacaban entre 9 y 17 de 17; dentro de un agente, 1,0. Un modelo que falla
   respondiendo de una vez acierta cuando puede leer archivos e iterar.
