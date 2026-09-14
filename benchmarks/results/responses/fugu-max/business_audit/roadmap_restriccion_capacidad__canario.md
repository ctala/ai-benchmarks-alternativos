# Fugu Max — business_audit/roadmap_restriccion_capacidad

- model_id: `sakana/fugu-max`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 26.44s | tokens_per_second: 92.2
- input_tokens: 314 | output_tokens: 2439

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

Con tu capacidad real tienes:

- **4 h/día × 5 días × 8 semanas = ~160 horas**
- Si las estimaciones están expresadas a tiempo completo:
  - **A:** ~480 h → unas **24 semanas** a tu ritmo actual
  - **B:** ~40 h → unas **2 semanas**
  - **C:** ~120 h → unas **6 semanas**, además depende de A
  - **D:** ~80 h → unas **4 semanas**

## Orden recomendado

### Semanas 1–2: B — arreglar el alta

Es la mejor inversión del trimestre: tiene impacto alto, es corta y afecta directamente a una métrica crítica.

Plan:

1. Instrumentar bien cada paso y los errores.
2. Revisar sesiones o hablar con usuarios que abandonan.
3. Corregir el problema principal.
4. Lanzar y medir.
5. Hacer una segunda iteración si los datos lo justifican.

Define antes el éxito: por ejemplo, subir la finalización del paso 2 del **40% a al menos 60–70%**, sin empeorar activación, calidad de usuarios o soporte.

No la trates como “una semana de construcción”; reserva tiempo para medir y corregir.

### Semanas 3–6: D — producir y publicar el contenido

D sería la siguiente iniciativa, pero solo si “grabar 10 videos” incluye:

- tema y audiencia definidos;
- guiones o estructura reutilizable;
- grabación por lotes;
- publicación;
- llamada a la acción;
- alguna métrica de resultado.

Diez videos almacenados no tienen impacto. Diez videos publicados con distribución y una hipótesis comercial sí.

Si todavía no tienes canal de distribución o una forma clara de convertir ese contenido en demanda, no gastaría cuatro semanas completas en D. En ese caso, usaría este bloque para mejoras incrementales de producto, ventas o reducción de soporte.

### Semanas 7–8: validación, segunda iteración y preparación de A

No empezaría la reescritura todavía. Usaría estas dos semanas para:

- consolidar los resultados de B;
- arreglar problemas derivados del cambio;
- reducir tareas operativas repetitivas;
- hacer el diseño técnico y la selección de la primera parte de la plataforma que migrarías;
- estimar A por módulos, no como una reescritura monolítica.

El entregable de A este trimestre debería ser un **plan de migración con una primera vertical pequeña validada**, no “empezar a reescribir toda la plataforma”.

## Qué hacer con A y C

### A: no la construyas este trimestre

Aunque tenga impacto alto, consume aproximadamente todo tu horizonte y no produce necesariamente valor visible durante las ocho semanas. A tu capacidad actual, una reescritura de tres meses a tiempo completo puede convertirse fácilmente en cinco o seis meses de calendario.

Solo la adelantaría si la plataforma actual:

- impide vender;
- genera incidentes graves;
- bloquea cualquier mejora importante;
- o tiene un riesgo técnico existencial.

En otro caso, conviértela en una iniciativa del próximo trimestre, empezando por una migración incremental y no por un “big bang”.

### C: déjala fuera

No tiene sentido planificar C este trimestre tal como está definida: depende de A, y A no cabe. Si el panel tiene valor comercial urgente, intenta desacoplarlo y construir una versión mínima con la plataforma actual. Pero eso sería una nueva iniciativa, no el C original de tres semanas dependiente de A.

## Resumen

**Plan del trimestre:**

1. **B — semanas 1–2**
2. **D — semanas 3–6**, solo con distribución clara
3. **Semanas 7–8 — medición, iteraciones, reducción de operación y diseño incremental de A**
4. **A — próximo trimestre**
5. **C — después de A, o reescrito como un MVP independiente**

La decisión importante es no confundir “alto impacto potencial” con “iniciativa que cabe en tu capacidad actual”. Este trimestre debes capturar primero el impacto rápido y medible de B, no iniciar una reescritura que consuma todo tu margen.