# Nemotron 3 Super — business_audit/roadmap_restriccion_capacidad

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 38.921s | tokens_per_second: 59.0
- input_tokens: 266 | output_tokens: 2298

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

Aquí tienes el orden realista para las próximas 8 semanas, basado en tu capacidad actual (no en la que te gustaría tener).

### 1. Tu capacidad real
- **4 horas/día** para construir.
- Asumiendo 5 días a la semana: **20 horas/semana**.
- **8 semanas = 160 horas** totales de construcción.
- El soporte y operación (2h/día) ya está descontado; no lo toques.

---

### 2. Veredicto por iniciativa

| Iniciativa | ¿Cabe en 8 semanas? | ¿Se hace este trimestre? | Razón |
|------------|---------------------|--------------------------|-------|
| **B) Arreglar flujo de alta** | Sí (~1 semana / ~20h) | **Sí** | Alto impacto, bajo esfuerzo. Arregla la fuga de ingresos ahora. |
| **D) 10 videos de contenido** | Sí (~2 semanas / ~40h) | **Sí** | Medio impacto, factible. Genera tracción sin bloquear nada. |
| **A) Reescribir plataforma** | No (~3 meses a tiempo completo) | **No** | Ni siquiera si dedicaras el 100% de tus 4h/día. Además, reescribir como fundador solo es una trampa: meses sin entregar valor al cliente. |
| **C) Panel de métricas** | No (depende de A) | **No** | Está bloqueada por A. Si A no se hace, C no existe. |

---

### 3. Hoja de ruta semana a semana

**Semana 1: Iniciativa B**
- Objetivo: Arreglar el paso 2 del flujo de alta y detener la pérdida del 60% de usuarios.
- Métrica de éxito: Tasa de conversión del paso 1 al paso 2 sube visiblemente.
- Tiempo estimado: ~20 horas (1 semana).

**Semanas 2-3: Iniciativa D**
- Objetivo: Grabar los 10 videos de contenido.
- Tiempo estimado: ~40 horas (2 semanas).
- Puedes grabarlos por bloques de tus 4 horas diarias.

**Semanas 4-8: No inicies A ni C**
- Tienes ~5 semanas de holgura (100 horas). No las uses para empezar la reescritura.
- Úsalas para:
  - Soporte y operación imprevista (ya sabes que aparece).
  - Corregir bugs críticos que aparezcan tras el cambio en B.
  - Mejorar lo ya lanzado en B (iterar, no reescribir).
  - **Descubrimiento y diseño de A** para el próximo trimestre: arquitectura, lista de funcionalidades, migración de datos. Pero sin escribir ni una línea de la reescritura todavía.

---

### 4. Resumen del orden

1. **B** (Semana 1)
2. **D** (Semanas 2-3)
3. **Buffer / Operación / Preparación de A para Q siguiente** (Semanas 4-8)

**Regla de oro para fundador solo:** No reescribas la plataforma mientras tengas una fuga de conversión abierta. Arregla la fuga, genera contenido para traer gente, y deja la reescritura para cuando tengas un equipo o al menos un bloque de tiempo dedicado sin presión de ingresos diarios.