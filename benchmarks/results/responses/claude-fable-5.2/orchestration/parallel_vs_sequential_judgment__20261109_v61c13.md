# Claude Fable 5.2 — orchestration/parallel_vs_sequential_judgment

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 7.01 | quality: 8.57
- latency_total: 20.926s | tokens_per_second: 83.3
- input_tokens: 1745 | output_tokens: 1744

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un agente orquestador que optimiza la ejecucion.
Clasifica cada tarea como parallelizable o secuencial, justificando por que.
Las tareas paralelas se ejecutan al mismo tiempo para mayor velocidad.
Las tareas secuenciales dependen del resultado de una tarea anterior.

**user:**

Tengo estas 6 tareas para preparar el lanzamiento de un producto:

A. Buscar precios de competidores en el mercado
B. Generar la descripcion del producto basada en las specs tecnicas (archivo: /docs/specs.md)
C. Calcular el precio optimo basado en costos + margen + precios de competidores
D. Crear la landing page con la descripcion y precio
E. Enviar email al equipo de marketing con el enlace de la landing
F. Publicar anuncio en redes sociales

Analiza las dependencias y presenta:
1. Un diagrama de dependencias (que tarea depende de cual)
2. Un plan de ejecucion optimizado (que se puede hacer en paralelo)
3. El tiempo estimado si cada tarea toma ~5 minutos

Ejecuta las tareas que se pueden iniciar inmediatamente.


## Respuesta completa

## 1. Diagrama de dependencias

```
A (precios competidores) ──► C (precio óptimo) ──┐
                                                 ├──► D (landing) ──┬──► E (email a marketing)
B (descripción desde specs) ─────────────────────┘                  └──► F (anuncio en redes)
```

| Tarea | Depende de | Clasificación | Justificación |
|---|---|---|---|
| A | nada | Paralelizable (con B) | Solo requiere buscar en la web |
| B | nada | Paralelizable (con A) | Solo requiere el archivo `/docs/specs.md` |
| C | A | Secuencial | Necesita los precios de competidores, además de costos y margen |
| D | B y C | Secuencial | Necesita la descripción y el precio |
| E | D | Paralelizable (con F) | Necesita el enlace de la landing, pero no depende de F |
| F | D | Paralelizable (con E) | Asumo que el anuncio enlaza a la landing y muestra el precio; no depende de E |

## 2. Plan de ejecución optimizado

| Fase | Tareas | Modo |
|---|---|---|
| 1 | A y B | En paralelo |
| 2 | C | Secuencial (espera a A) |
| 3 | D | Secuencial (espera a B y C) |
| 4 | E y F | En paralelo |

## 3. Tiempo estimado

- **Todo secuencial:** 6 × 5 = 30 minutos
- **Optimizado:** 4 fases × 5 = **20 minutos** (un 33 % menos)
- **Ruta crítica:** A → C → D → E/F. B tiene 5 minutos de holgura, porque su resultado no se usa hasta D.

## Ejecución de la fase 1

Empiezo leyendo `/docs/specs.md`. Es el insumo de B y también lo necesito para A, porque todavía no sé qué producto es y una búsqueda de precios sin esa información no sería útil. En cuanto lo tenga, lanzo en paralelo las búsquedas de A y la redacción de B.