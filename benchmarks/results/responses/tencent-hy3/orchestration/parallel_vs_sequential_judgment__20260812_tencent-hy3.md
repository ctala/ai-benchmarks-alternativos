# Tencent Hy3 — orchestration/parallel_vs_sequential_judgment

- model_id: `tencent/hy3`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 13.934s | tokens_per_second: 133.3
- input_tokens: 1233 | output_tokens: 1858

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

# 📊 Análisis de Dependencias y Plan de Ejecución

## 1. Diagrama de Dependencias

```
        ┌─────────┐
        │   A     │  Buscar precios competidores
        └────┬────┘
             │
             ▼
        ┌─────────┐      ┌─────────┐
        │   C     │◄─────┤   B     │  Generar descripción (specs)
        │ Precio  │      └────┬────┘
        │ óptimo  │           │
        └────┬────┘           │
             │                │
             └───────┬────────┘
                     ▼
              ┌─────────────┐
              │     D       │  Crear landing page
              └──────┬──────┘
                     │
           ┌─────────┴─────────┐
           ▼                   ▼
      ┌─────────┐         ┌─────────┐
      │   E     │         │   F     │  Publicar redes
      │ Email   │         └─────────┘
      └─────────┘
```

**Tabla de dependencias:**

| Tarea | Depende de | Tipo |
|-------|-----------|------|
| A – Precios competidores | — | 🟢 Independiente |
| B – Descripción (specs) | — | 🟢 Independiente |
| C – Precio óptimo | A | 🔴 Secuencial |
| D – Landing page | B, C | 🔴 Secuencial |
| E – Email marketing | D | 🔴 Secuencial |
| F – Redes sociales | D | 🟡 Paralela (a E, tras D) |

## 2. Plan de Ejecución Optimizado

| Oleada | Tareas en paralelo | Razón |
|--------|-------------------|-------|
| **Oleada 1** | `A` + `B` | Ambas son independientes, no se bloquean entre sí |
| **Oleada 2** | `C` | Requiere el resultado de `A` |
| **Oleada 3** | `D` | Requiere `B` (descripción) y `C` (precio) |
| **Oleada 4** | `E` + `F` | Ambas dependen solo de `D`; se ejecutan en paralelo |

## 3. Tiempo Estimado (5 min por tarea)

- Oleada 1 (A+B paralelo): **5 min**
- Oleada 2 (C): **5 min**
- Oleada 3 (D): **5 min**
- Oleada 4 (E+F paralelo): **5 min**

### ⏱️ **Total optimizado: ~20 minutos** (vs. 30 min secuencial → ahorro de 10 min / 33%)

---

## 🚀 Ejecución de Tareas Inmediatas (Oleada 1)

Inicio ahora las tareas **A** y **B**, que no tienen dependencias. Las ejecuto en paralelo:

- **A**: búsqueda de precios de competidores (web)
- **B**: lectura de specs técnicas para generar la descripción

Ambas son independientes, así que las lanzo en el mismo bloque: