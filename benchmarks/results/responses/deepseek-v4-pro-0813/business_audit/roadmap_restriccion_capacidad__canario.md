# DeepSeek V4 Pro (0813) — business_audit/roadmap_restriccion_capacidad

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 24.675s | tokens_per_second: 84.1
- input_tokens: 343 | output_tokens: 2074

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

Con tu capacidad real (**4 h/día efectoras**, 8 semanas ≈ **160 h totales**), la priorización cambia frente a lo que harías con un equipo ideal.

---

## Orden propuesto para el trimestre

### 1. B — Arreglar el flujo de alta (semanas 1–2, ~40 h)
**Hazlo primero, sin excepción.**

- Es lo de mayor impacto por hora invertida: hoy pierdes al **60%** en el paso 2.  
- Si mejoras esa conversión, todo lo demás (crecimiento, retención, métricas) se amplifica.  
- Esfuerzo estimado: 1 semana full-time (40 h) → con tus 4 h/día, ocupa **2 semanas calendario**.

**Criterio de salida:** medir de nuevo el abandono en el paso 2 y validar mejora, no solo “terminar el arreglo”.

---

### 2. D — Grabar 10 videos de contenido (semanas 3–6, ~80 h)
**Segundo trimestre, una vez que el alta ya no pierde gente.**

- Impacto medio, pero no depende de A ni de otras piezas.  
- Atrae/educa clientes y puede reducir soporte futuro.  
- Esfuerzo: 2 semanas full-time (80 h) → **4 semanas calendario** a tu ritmo.

**Matiz:** si tras arreglar B ves que el alta requiere iteraciones adicionales, no dudes en recortar D para asegurar B. La conversión manda.

---

### 3. A — Reescribir la plataforma: **descartada para este trimestre**
No es que no sea importante, es que **no cabe**.

- 3 meses a tiempo completo ≈ **480 h**.  
- Tú dispones de ~160 h en todo el trimestre.  
- Incluso dedicándole el 100% de tus 4 h/día, llegarías a un tercio de la reescritura. Dejar un sistema a medio migrar es peor que no empezar.

**Recomendación:** no la conviertas en objetivo trimestral. Déjala en el backlog y, si quieres, usa un espacio marginal (última semana) para hacer un spike técnico o definir alcance, sin comprometerte a migrar.

---

### 4. C — Panel de métricas: **bloqueada por A, se cae este trimestre**
Depende explícitamente de que A esté terminada. Como A no se termina, C no ocurre.

**Alternativa realista si te duele dejarla fuera:**  
Pregúntate si puedes construir una versión mínima del panel sobre la plataforma actual, sin reescribir nada. Si la respuesta es sí, podrías considerar reemplazar D o usar las semanas finales. Pero no cuentes con ella como estaba definida.

---

## Resumen visual del trimestre

| Semanas | Foco principal | Horas reales |
|---------|----------------|--------------|
| 1–2     | B: arreglar alta | ~40 h |
| 3–6     | D: 10 videos     | ~80 h |
| 7       | Iterar B con datos, buffer, soporte | ~20 h |
| 8       | Planificar A (spike/alcance), buffer | ~20 h |

**No empieces A como proyecto de migración.**  
**No persigas C mientras A no exista.**

Lo único innegociable es B. El resto es secundario.