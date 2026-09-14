# Fugu Max — business_audit/roadmap_restriccion_capacidad

- model_id: `sakana/fugu-max`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 41.811s | tokens_per_second: 83.1
- input_tokens: 314 | output_tokens: 3476

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

Con tu capacidad real tienes aproximadamente:

- **8 semanas × 5 días × 4 h = 160 horas**
- **A** requiere unos **480 h** si “3 meses a tiempo completo” son 12 semanas × 40 h. A tu ritmo serían aproximadamente **24 semanas**, no 8.
- **C** además está bloqueada por A.

Por tanto, **no intentes completar A este trimestre**. Sería iniciar una reescritura sin llegar al beneficio y consumir todo el trimestre.

## Orden recomendado

### 1. B — Arreglar el alta  
**Semana 1 — 20 horas**

Es la prioridad clara: tienes evidencia real de una fuga del 60% y el esfuerzo es pequeño.

Incluye:

- Instrumentar bien el paso 2 antes de cambiarlo.
- Identificar si el problema es UX, error técnico, requisito innecesario o falta de confianza.
- Implementar el cambio.
- Medir finalización del alta y activación posterior.
- Desplegar al final de la semana, no dedicar tres semanas a perfeccionarlo.

**Criterio de éxito:** reducir de forma significativa el abandono del paso 2, no solo aumentar clics.

---

### 2. D — Producir el contenido  
**Semanas 2 y 3 — 40 horas**

Hazlo solo en formato suficientemente bueno para publicar:

- Guion reutilizable.
- Grabación por lotes.
- Edición mínima.
- Un canal concreto de distribución.
- Una llamada a la acción clara por vídeo.

No produzcas diez vídeos “para tener contenido”. Produce diez piezas con una hipótesis de adquisición o activación detrás. Si no tienes canal de distribución o CTA, sustituiría D por más trabajo sobre B y onboarding.

---

### 3. A — Solo una fase acotada de validación, no la reescritura  
**Semanas 4 a 8 — hasta 100 horas**

No llames a esto “reescribir la plataforma”. Define un entregable limitado:

- Elegir un módulo o flujo representativo.
- Documentar la arquitectura de migración.
- Hacer un benchmark contra la plataforma actual.
- Extraer un pequeño componente mediante una estrategia incremental.
- Probar el framework nuevo en una pieza real.
- Identificar costes, riesgos y dependencias.

Al final del trimestre debes tener una decisión informada:

> “La migración incremental empieza por X y tiene este coste”,  
> o  
> “La reescritura no compensa; seguimos con la arquitectura actual”.

**No empieces una migración que requiera terminarse para generar valor.** Si el primer slice no demuestra una mejora concreta, se detiene.

---

### 4. C — Posponer

No haría el panel este trimestre bajo las condiciones actuales:

- Depende de A.
- A no puede completarse con tu capacidad disponible.
- Su impacto es medio, no alto.
- Intentar desbloquearlo mediante una reescritura te deja sin resultados de cliente.

Si los clientes realmente lo necesitan antes, cambiaría la premisa de dependencia: construiría un **panel mínimo y de solo lectura sobre la plataforma actual**, aunque no sea la solución final. Pero no construiría C como proyecto de tres semanas esperando que A esté lista.

## Calendario

| Semana | Enfoque |
|---|---|
| 1 | B: instrumentar, corregir y desplegar |
| 2 | D: guiones y primeras grabaciones |
| 3 | D: terminar, publicar y medir |
| 4 | A: diseño de migración y prueba técnica |
| 5–8 | A: un único slice vertical en producción o preproducción |

## Decisión resumida

**Haz B. Haz D si tiene distribución concreta. Dedica el resto a des-riesgar A, no a reescribirla. No hagas C todavía.**

El resultado razonable del trimestre sería:

1. Mejorar sustancialmente la conversión del alta.
2. Publicar contenido utilizable, no solo grabarlo.
3. Saber si A merece ejecutarse y cómo dividirla.
4. Llegar al siguiente trimestre sin haber iniciado un proyecto de seis meses disfrazado de proyecto de ocho semanas.