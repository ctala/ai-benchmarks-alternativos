# Nex-N2-Mini — business_audit/roadmap_restriccion_capacidad

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.1 | quality: 10.0
- latency_total: 33.405s | tokens_per_second: 202.1
- input_tokens: 254 | output_tokens: 6752

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

Con tu capacidad real, **no estás priorizando 4 iniciativas**. Estás priorizando **160h teóricas** en 8 semanas:

- 8 semanas × 5 días × 4h/día = **160h**
- En la práctica, con buffer de solo fundador, calcula **110-120h útiles**

Y A requiere ~3 meses full-time, es decir, mucho más de lo que tienes.

## Orden recomendado del trimestre

### 1) B — Arreglar el flujo de alta  
**Semana 1**

Es lo más prioritario porque:

- Impacto alto.
- Esfuerzo bajo.
- Corrige una fuga de 60% antes de intentar atraer más gente.
- Es la iniciativa con mejor relación impacto/esfuerzo.

**Objetivo:** reducir la pérdida en el paso 2 y medir activación antes/after.

---

### 2) D — Grabar 10 videos de contenido  
**Semanas 2-3**

Después de cerrar la fuga de onboarding, tiene sentido generar más demanda.

Hazlo en bloque:

- Guiones: 1 día.
- Grabación: 1 día.
- Edición: 2-3 días.
- Programación/publicación: resto.

**Objetivo:** tener 10 piezas listas y empezar a alimentar pipeline.

---

### 3) Validar B / segundo round de onboarding  
**Semana 4**

No asumas que B quedó resuelto con una primera corrección.

Mide:

- Conversión paso 1 → paso 2.
- Conversión paso 2 → finalización.
- Activación real.
- Tickets de soporte relacionados con alta.

Si la conversión no mejora, usa esa semana para iterar B antes de hacer nada más grande.

---

### 4) C — Panel de métricas  
**Deferred / fuera este trimestre**

C depende de A. Y A no se va a terminar en este trimestre.

Si haces C ahora, probablemente vas a reescribir o rehacer trabajo.

Solo haría C si lo reduces a una versión manual o desacoplada:

- Reporte semanal en CSV.
- Dashboard manual con métricas clave.
- Reporte para los 3-5 clientes más importantes.

Pero el panel completo queda fuera.

---

### 5) A — Reescribir la plataforma  
**No este trimestre**

A tiene impacto futuro alto, pero no cabe en la capacidad real.

No hagas reescritura este trimestre. Como máximo, dedica 5-10h a investigación técnica y decide cuándo revisarlo.

**Decisión:** A queda para el siguiente trimestre o para cuando tengas más capacidad.

---

## Plan concreto de 8 semanas

| Semana | Trabajo |
|---|---|
| 1 | B: arreglar flujo de alta |
| 2 | QA de B + guiones/estructura de videos |
| 3 | D: grabación de videos |
| 4 | D: edición/publicación |
| 5 | Medir B e iterar si hace falta |
| 6 | Publicar/optimizar contenido + revisar métricas |
| 7 | Segundo round de mejora de onboarding o contenido |
| 8 | Cierre: decidir si B funcionó, documentar A y posponer C |

## Orden final

**B → D → validar/iterar B → A solo como investigación → C queda fuera**

Mi decisión como founder solo sería:

> Este trimestre no reescribo la plataforma ni construyo el panel. Primero cierro la fuga de alta, luego genero demanda con contenido y mido. Si B no mejora la conversión, sigo arreglando onboarding antes de tocar nada más grande.