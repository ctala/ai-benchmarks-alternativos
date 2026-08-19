# Seed 2.1 Turbo — orchestration/parallel_vs_sequential_judgment

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 7.68 | quality: 8.57
- latency_total: 12.238s | tokens_per_second: 68.7
- input_tokens: 1329 | output_tokens: 841

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

Analicemos las dependencias y ejecutemos las tareas que pueden iniciar inmediatamente.

## 1. Diagrama de Dependencias

```
A (Buscar precios competidores) ──┐
                                  ├─► C (Calcular precio óptimo) ──┐
B (Generar descripción) ──────────┘                                ├─► D (Crear landing page) ──┬─► E (Enviar email marketing)
                                                                    │                            └─► F (Publicar en redes sociales)
```

**Explicación:**
- **A** y **B** son independientes (no dependen de ninguna otra tarea)
- **C** depende de **A** (necesita precios de competidores)
- **D** depende de **B** y **C** (necesita descripción y precio)
- **E** y **F** dependen de **D** (necesitan la landing page lista)

## 2. Plan de Ejecución Optimizado

| Nivel | Tareas en Paralelo | Tiempo |
|-------|-------------------|--------|
| **Nivel 1** | A + B | 5 min |
| **Nivel 2** | C | 5 min |
| **Nivel 3** | D | 5 min |
| **Nivel 4** | E + F | 5 min |

## 3. Tiempo Estimado

- **Secuencial (6 tareas × 5 min):** 30 minutos
- **Optimizado (en paralelo):** **20 minutos** (4 niveles × 5 min)

---

Ahora ejecuto las tareas del **Nivel 1** que pueden iniciarse inmediatamente:
