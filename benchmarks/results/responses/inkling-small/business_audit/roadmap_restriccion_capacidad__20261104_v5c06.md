# Inkling Small — business_audit/roadmap_restriccion_capacidad

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 90.692s | tokens_per_second: 34.3
- input_tokens: 248 | output_tokens: 3110

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

**Verdad cruda primero:** tienes ~160 horas de construcción en este trimestre (4h/día × ~20 días hábiles × 2 meses). El proyecto A consume ~480 horas a tiempo completo. No cabe. Si empiezas A, al cierre del trimestre tendrás una plataforma a medio reescribir, el flujo de alta roto y 0 videos.

Como jefe de producto de una sola persona, mi regla es: **no hacer rewrites que matan a fundadores solitarios cuando hay sangre en el embudo.**

Aquí está tu orden realista y el calendario de 8 semanas.

---

### El orden (y por qué)

| Prioridad | Iniciativa | Decisión para este trimestre | Razón |
|---|---|---|---|
| **1** | **B: Flujo de alta** | **Hacer ahora, semana 1.** | Impacto alto, esfuerzo 1 semana (~20h). Recuperas 60% de gente que se va. Es el único proyecto que paga inmediatamente y libera presión de soporte. |
| **2** | **D: Videos de contenido** | **Semanas 2-3.** | Impacto medio, 2 semanas (~40h). Una vez que B funcione, necesitas alimentar ese flujo arreglado. Es ejecutable en bloques de 4h sin depender de nadie. |
| **3** | **A: Reescribir framework** | **NO iniciar. Posponer al Q+1.** | Es 3 meses a tiempo completo. A tu ritmo real son ~6 meses. Además es riesgo de muerte: mientras reescribes, no vendes ni mejoras. Si es crítico, haz un **spike de 1 semana** en semana 7-8 solo para validar arquitectura, no código. |
| **4** | **C: Panel de métricas** | **Bloqueado / eliminar del trimestre.** | Depende de A. Si A no va, C no va. No malgastes 3 semanas en un panel que nadie verá si tu base es inestable. |

---

### Plan de semanas (4h/día reales)

**Semana 1: B (flujo de alta)**
- Solo eso. No toques nada más. Arregla paso 2, mide si sube la conversión.
- *Objetivo:* pasar de ~40% de retención a >70% en ese paso.

**Semanas 2-3: D (10 videos)**
- 2 videos por semana. Graba en lote (batch): un día de guión, un día de grabación, un día de edición básica.
- Usa el flujo de alta ya arreglado como gancho de los videos (ej. “mira cómo resolví el paso 2”).

**Semana 4: Buffer / validación**
- No empiezas A. Mides si B realmente bajó la fuga.
- Usa estas 20h para automatizar o documentar algo de tu soporte diario y recuperar 30 min/día para construcción futura.

**Semanas 5-6: Trabajo incremental (no A)**
- Si B funciona, haz mejoras pequeñas en la plataforma actual (no rewrite): optimiza el paso 2, añade una notificación, limpia deuda técnica que ralentiza.
- Esto es “A en miniatura”: mejoras reales sin riesgo de romper todo.

**Semanas 7-8: Spike de A (opcional) o descanso estratégico**
- Si después de B y D tienes tracción y el framework es un cuello de botella real, dedicas 1 semana a un **spike técnico** (diseño, no código) para planear el rewrite del Q+1.
- Si no, usa estas semanas para que el negocio respire: más contenido, más soporte automatizado, o un MVP mínimo de C *solo si* descubriste que puedes hacerlo sin A.

---

### Por qué A debe morir este trimestre

Como fundador solo, **el rewrite es un engaño de productividad.** Parece “impacto alto en el futuro”, pero en la práctica:
- Consumes 100% de tu capacidad de construcción.
- No tocas ingresos ni retención hoy.
- Al final de 8 semanas tendrás 40% de una plataforma nueva y 100% de un flujo de alta roto.

Si tu framework es tan malo que requiere 3 meses de rewrite, entonces **la solución es sobrevivir lo suficiente con B para que el Q+1 financie ese rewrite con ayuda o con más horas.** No lo hagas con 4h/día.

---

### Qué hacer con las 2h de soporte

Como no puedes delegar hoy, usa 30 min de esas 2h para:
- Escribir una respuesta guardada (template) para las 3 preguntas más frecuentes de paso 2.
- Eso reduce tu carga y te da 30 min más de construcción.

---

**Resumen para que lo copies:**  
**B → D → (no A) → (C bloqueado)**. Si intentas hacer A, fallas. Si haces B primero, ganas dinero y tiempo. El trimestre se gana arreglando el embudo, no construyendo castillos de arena.