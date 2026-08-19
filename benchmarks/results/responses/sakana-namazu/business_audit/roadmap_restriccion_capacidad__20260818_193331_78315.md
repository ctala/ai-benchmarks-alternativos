# Sakana Namazu — business_audit/roadmap_restriccion_capacidad

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 40.573s | tokens_per_second: 107.3
- input_tokens: 304 | output_tokens: 4354

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

Aquí es donde un buen jefe de producto te protege de ti mismo.

### La verdad de tu capacidad real

Tienes **8 semanas** y **~4 horas/día** de construcción reales.
Aunque trabajes 6 días a la semana, eso son **~192 horas de construcción** como máximo absoluto en todo el trimestre.

Miremos tus opciones con esos números:

| Iniciativa | Esfuerzo ideal | Traducido a tu velocidad real | ¿Cabe en el trimestre? |
|---|---|---|---|
| **A** Reescritura | ~3 meses a tiempo completo (~480h) | ~6-9 meses a medio tiempo | **Imposible** |
| **B** Onboarding | ~1 semana (~20h) | ~1 semana | Sí |
| **C** Métricas | ~3 semanas (~60h) | ~3 semanas | Solo si dependiera de algo que exista |
| **D** Videos | ~2 semanas (~40h) | ~2 semanas | Sí |

### Orden del trimestre (la única opción realista)

#### 1. Semana 1: B — Arreglar el paso 2 del flujo de alta
**Esta es tu Prioridad 0.** Tienes un embudo que pierde al 60% en un solo escalón. Arreglar eso no es una mejora, es un respirador artificial. Cada hora que inviertas aquí se multiplica por todos los usuarios que vienen después.
*Acción:* Mide exactamente qué pasa en ese paso (datos reales, no suposiciones), parchea o rehaz el flujo, y valida que la caída baje.

#### 2. Semanas 2-3: D — Los 10 videos de contenido
**Solo después de arreglar B.** Ahora que el embudo no pierde agua por el agujero del paso 2, tiene sentido verter agua (tráfico) arriba. Si hubieras hecho D antes, estarías quemando tiempo y oportunidad llevando gente a un onboarding roto.
*Acción:* Grábalos en bloque, edición mínima viable, publiqués y olvídate.

#### 3. Semanas 4-8: Proyecto "Devuélveme mis horas"
No inicies ni A ni C. En lugar de eso, usa ~9-10 semanas restantes para un proyecto invisible de alto impacto: **reducir tus 2 horas diarias de soporte y operación.**
*Acciones:*
- Documenta las 5 preguntas que más te llegan y automatízalas (mensajes automatizados, mejor UX, emails de bienvenida).
- Crea scripts o mini-herramientas internas para las tareas operativas que haces con las manos todos los días.
- Mejora textos de error y estados vacíos para que no necesiten explicación.

**El objetivo es bajar esas 2h de operación a 1h (o menos).** Eso te devolvería un 25% de capacidad de construcción permanente para el siguiente trimestre.

---

### Lo que tienes que matar este trimestre

- **A (la reescritura):** Es una trampa mortal para un fundador solo. Si la empiezas ahora, no la terminarás en 8 semanas ni en 16. Te quedarías sin producto, sin clientes y sin moral. **Pospondr a largo plazo.** Solo se justifica si el framework actual te impide literalmente vender; si no, es deuda técnica que se paga con refactorings tácticos, no con una revolución.
- **C (panel de métricas):** Está bloqueada por A y es "medio impacto". Con 4h/día no hay espacio para dependencias largas. Cuando exista A, la revisas. Hasta entonces, usa Google Sheets, emails automatizados o cualquier hack que no requiera semanas de ingeniería.

### Resumen ejecutivo

1. **Haz B ya.** Es el único "high impact / low effort" real que tienes.
2. **Luego D.** Para rellenar la parte superior del embudo, ahora que no se escapa por abajo.
3. **El resto del trimestre: reduce tu operación.** Esa es tu inversión para ganar velocidad en el siguiente trimestre.
4. **A y C: al congelador.** No caben en tu capacidad real y tienen dependencias letales.