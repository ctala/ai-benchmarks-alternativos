# GPT-5.6 Terra — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 6.33 | quality: 7.2
- latency_total: 13.141s | tokens_per_second: 96.1
- input_tokens: 241 | output_tokens: 1263

## Respuesta completa

Tu capacidad real del trimestre es:

- 4 h/día de construcción × 5 días × 8 semanas = **~160 horas**
- Equivale a **~4 semanas “a tiempo completo”**
- No planifiques al 100%: deja margen para bugs, soporte excepcional, revisión y cambios. Capacidad comprometible: **~3–3,5 semanas FTE**

## Orden recomendado

### 1. B — Arreglar el flujo de alta
**Primero, sin duda.**

- Es alto impacto.
- Cuesta ~1 semana FTE, es decir, aproximadamente **2 semanas calendario** con tus 4 h/día.
- Ya tienes una señal muy concreta: pierdes el 60% en el paso 2.
- Mejorar activación/conversión hace que cualquier esfuerzo posterior —incluido contenido— rinda más.

No lo trates como “hacer un cambio y pasar página”. Reserva tiempo para:

1. Instrumentar el embudo si no lo está.
2. Identificar/friccionar el paso 2.
3. Implementar el arreglo.
4. Medir durante al menos varios días.
5. Iterar una vez si el resultado no mejora claramente.

**Objetivo trimestral sugerido:** reducir de forma material la caída del paso 2, no simplemente “entregar una corrección”.

---

### 2. D — Grabar los 10 videos de contenido
**Segundo, después de estabilizar el alta.**

Es ~2 semanas FTE, o **~4 semanas calendario** a tu capacidad actual. Encaja, pero sólo si lo acotas bien.

No repartiría los videos como una tarea secundaria diaria durante ocho semanas: genera cambio de contexto y suele terminar en contenido mediocre o incompleto. Mejor trabajarlo por lotes:

- Semana de guiones/estructura y preparación.
- Semana de grabación/edición/publicación.
- Reutiliza una plantilla, misma escena, misma edición y CTA.
- Cada video debe llevar a un flujo de alta ya corregido.

El contenido tiene más valor una vez que el destino convierte mejor.

---

### 3. Reserva el resto para iteración y distribución
Tras B y D habrás consumido aproximadamente:

- B: 1 semana FTE
- D: 2 semanas FTE
- Total: 3 semanas FTE de 4 disponibles

Te queda aproximadamente **1 semana FTE**, o **2 semanas calendario**, que no deberías llenar de una nueva iniciativa grande.

Úsala para:

- Iterar el onboarding según datos.
- Corregir bugs surgidos de los cambios.
- Publicar/distribuir los videos.
- Hablar con usuarios/clientes.
- Añadir instrumentación mínima para decidir el siguiente trimestre.

---

## Qué no haría este trimestre

### A — Reescritura de plataforma
**No la empezaría como iniciativa de ejecución este trimestre.**

Tu estimación es 3 meses a tiempo completo:

- 12 semanas FTE aproximadamente.
- Tu capacidad trimestral real es ~4 semanas FTE.
- A este ritmo ocuparía cerca de **seis meses calendario**, sin contar interrupciones ni alcance cambiante.

Además, empezar una reescritura sin poder terminarla crea el peor escenario para un fundador solo: mantienes el producto actual, construyes otro en paralelo, retrasas mejoras de conversión y probablemente tampoco desbloqueas C este trimestre.

Si hay riesgos técnicos reales, permite como máximo una **mini-investigación acotada** al final del trimestre: 1–2 días para documentar el problema, alternativas, migración incremental y condiciones que justificarían la reescritura. Pero no empieces el proyecto.

### C — Panel de métricas para clientes
**No este trimestre.**

Depende de A, y A no cabe. Por tanto C tampoco cabe.

Además, antes de construir un panel de 3 semanas, valida qué métricas necesitan realmente los clientes. Puede que un reporte manual, email semanal o exportación simple resuelva el problema con una fracción del esfuerzo.

---

## Plan de 8 semanas

| Semana | Foco |
|---|---|
| 1–2 | **B:** diagnosticar, instrumentar y arreglar el paso 2 del alta |
| 3 | Medir resultado, iterar onboarding y preparar guiones de D |
| 4–5 | **D:** producir/publicar los 10 videos en lote |
| 6 | Distribución de contenido + seguimiento de conversión |
| 7 | Segunda iteración de onboarding / bugs / aprendizaje de clientes |
| 8 | Cierre: métricas, decisión sobre próximo trimestre y análisis acotado de A si sigue siendo prioritario |

## Prioridad final

1. **B — Arreglar alta**
2. **D — Videos**
3. **Iteración, distribución y aprendizaje**
4. **A — Sólo análisis técnico acotado; no reescritura**
5. **C — Pospuesto**

La regla aquí es simple: no priorices por el impacto teórico de A, sino por el impacto entregable dentro de tus ~160 horas reales. B puede mover una métrica crítica este trimestre; A no.