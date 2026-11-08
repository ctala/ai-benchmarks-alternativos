# Tencent Hy3 — orchestration/parallel_vs_sequential_judgment

- model_id: `tencent/hy3`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 34.192s | tokens_per_second: 62.6
- input_tokens: 1233 | output_tokens: 2142

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

# Análisis de Orquestación - Lanzamiento de Producto

## 1. Diagrama de Dependencias

```
        ┌──> [A] Precios competencia ──┐
        │                             ├──> [C] Precio óptimo ──┐
[INICIO]├──> [B] Descripción (specs) ─┘                       │
        │                                                     ├──> [D] Landing page ──┬──> [E] Email marketing
        └─────────────────────────────────────────────────────┘                    └──> [F] Anuncio redes
```

| Tarea | Depende de | Tipo |
|-------|-----------|------|
| **A** Buscar precios competencia | — | 🟢 Paralelizable (inicio inmediato) |
| **B** Generar descripción (specs) | — | 🟢 Paralelizable (inicio inmediato) |
| **C** Calcular precio óptimo | A (precios) | 🔴 Secuencial |
| **D** Crear landing page | B (descripción) + C (precio) | 🔴 Secuencial |
| **E** Email a marketing | D (link landing) | 🔴 Secuencial |
| **F** Anuncio redes sociales | D (landing lista) | 🔴 Secuencial |

**Justificación:** A y B son independientes (A solo necesita investigación de mercado, B solo lee `/docs/specs.md`). C requiere los precios de A. D requiere tanto la descripción (B) como el precio (C). E y F ambas requieren que la landing (D) esté publicada. E y F **no** dependen entre sí → se ejecutan en paralelo.

## 2. Plan de Ejecución Optimizado (por oleadas)

| Oleada | Tareas en paralelo | Min |
|--------|-------------------|-----|
| **1** | A + B | 5 |
| **2** | C | 5 |
| **3** | D | 5 |
| **4** | E + F | 5 |

## 3. Tiempo Estimado

- **Paralelo optimizado:** 4 oleadas × 5 min = **20 minutos**
- (vs. secuencial: 6 × 5 = 30 min → **ahorro de 10 min / 33%**)

---

## 🚀 Ejecución de tareas inmediatas (Oleada 1: A + B)

Para ejecutar A y B necesito el contexto del producto. Leo las specs primero y luego lanzo **A** (búsqueda web) y **B** (descripción) en paralelo.