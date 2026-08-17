# Sakana Namazu — business_audit/roadmap_restriccion_capacidad

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 10.381s | tokens_per_second: 197.3
- input_tokens: 304 | output_tokens: 2048

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

El usuario es un fundador solitario con 6 horas de trabajo enfocado al día. 2 horas se van en soporte y operaciones no delegables, le quedan 4 horas diarias reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Calculemos la capacidad total real:
- 4 horas/día × 5 días × 8 semanas = 160 horas.
- Si trabaja fines de semana (poco realista para sostenibilidad), serían más, pero asumo semana laboral estándar de fundador: 5-6 días. Usemos 5 días para ser conservadores: 160 horas. Si es 6 días: 192h. Digamos que tiene ~160-180 horas reales de construcción.

Iniciativas:
A) Reescribir plataforma: ~3 meses a tiempo completo. A tiempo completo asumiendo 4h/día de construcción? O 8h/día? El usuario no especifica. Pero dice "3 meses a tiempo completo". Si a tiempo completo = 8h/día, eso sería ~480h. Si significa dedicación total del founding time (6h/día), sería ~360h. En cualquier caso, mucho más de lo que tiene (160-180h solo de construcción). Es imposible terminarlo en el trimestre. Además, reescribir todo con soporte diario es una trampa de muerte para un solo fundador.

B) Arreglar flujo de alta: ~1 semana. Eso sería ~20h (4h × 5 días). Es factible y alto impacto. Corregir un 60% de abandono en paso 2 es dinero gratis.

C) Panel de métricas: ~3 semanas (~60h). Depende de A. Como A no se puede hacer, C queda bloqueado o requiere workaround. Impacto medio. No priorizar si bloqueado.

D) 10 videos: ~2 semanas (~40h). Impacto medio. Trabajo de marketing/contenido. Podría hacerse pero compite con B.

Prioridad clara:
1. B primero. Es rápido, alto impacto, no tiene dependencias, mejora conversión existente.
2. Luego decidir entre D y quizás un C reducido sin reescritura. Pero C depende de A. Si A no se hace, o se hace un MVP de métricas sobre la base actual, o se salta. D es más predecible y no tiene dependencias técnicas. Sin embargo, D es marketing; si el funnel de alta está roto (60% abandono), mejor arreglar B antes de traer tráfico con D. Pero D puede ser hecho después de B.

¿Qué hacer con A?
Posponerlo. Es un "rewrite trap". Con 8 semanas y 4h/día, no da. Además, el riesgo de una reescritura total para un solo fundador que también da soporte es altísimo: bug crítico en producción mientras reescribes, context switching, etc. Sugiero explícitamente descartarlo para este trimestre y reconsiderar en 6 meses si la deuda técnica realmente lo justifica.

Plan recomendado:
Semanas 1-2: B (arreglar onboarding). Medir. El impacto de pasar de 40% de retención en paso 2 a, digamos, 70%+, significa casi duplicar clientes potenciales.
Semanas 3-4: D (videos). Construir activos de marketing que trabajen mientras dormís. Ideal para fundador solo: escala sin tu tiempo continuo.
Semanas 5-8: 👉 Aquí hay una decisión. Quedan ~4 semanas (80h). 

Opción sobre C: Como depende de A, evaluar si se puede hacer un "panel de métricas v0" sin reescritura. Si la dependencia es estricta, no hacer C y usar el tiempo para:
- Refactorizar solo las partes críticas que permitan C sin reescritura total.
- O mejoras de quick-wins de UX donde haya fricción.
- O preparar el terreno para A (spikes, decisiones de arquitectura) pero no ejecutar A.

Mejor propuesta:
Semanas 5-8: Trabajar en deuda técnica "quirúrgica" y/o pequeñas mejoras de retención; o un C reducido si se puede desbloquear. También se puede usar 1 semana para automatizar/atajar partes del soporte diario para liberar horas del siguiente trimestre.

Aclaración clave: "Priorizas con la capacidad real del equipo, no con la ideal." Debo ser brutalmente honesto: A es imposible. C está bloqueado.

Estructura de respuesta:
1. Capacidad real disponible (cuenta de la vieja).
2. Veredicto por iniciativa (Go / No-Go / Modificado).
3. Plan de 8 semanas detallado.
4. Reglas de oro para founder solo.

Veamos números:
- 8 semanas × 5 días × 4h = 160h. Si trabaja 1 sábado a la semana: 8×6×4=192h. Usemos ~160-180h como caja.

Estimaciones en horas:
- B: 1 semana = 20h. 
- D: 2 semanas = 40h.
- C: 3 semanas = 60h (pero bloqueado por A).
- A: 3 meses TC. Si TC=40h/semana → 480h. Si TC=20h/semana (su realidad) → 240h. En cualquier caso, >160h y ocupa TODO el trimestre sin margen.

Plan:
Semana 1-2: B (20h). Si termina antes, buffer.
Semana 3-4: D (40h). 
Semanas 5-8: ~80-100h.

¿Qué hacer en semanas 5-8?
Opción 1: "Matar" C como tal y hacer un "Métricas MVP" sin reescritura, si es posible. Debe preguntarse: ¿es la dependencia de A real o autoimpuesta? Si es real (por ejemplo, requiere endpoints que solo existen en nuevo framework), entonces C se pospone con A. Si es autoimpuesta (quiero hacerlo "bien" en nuevo stack), entonces se desbloquea haciéndolo en lo actual.

Como jefe de producto de empresa de una persona, debo ser franco. La respuesta debe ser ejecutiva y sin azúcar.

Conclusión del orden:
1. B (inmediato, semana 1-2).
2. D (semana 3-4).
3. Sustituir C por "Quick-wins de retención" o "Desbloqueo de soporte" en semanas 5-8.
4. A: al congelador. No empezar. Hasta quizás hacer un "spike" de decisión de 2-4h en semana 8 si es necesario, pero no más.

Necesito ser cuidadoso con C: el usuario dice "Depende de que A esté terminado". Entonces C es no-go este trimestre a menos que rompa esa dependencia. Debo recomendar explícitamente NO intentar empezar A para desbloquear C; no le dará tiempo y quedará con dos cosas a medias.

Otra cosa: el flujo de alta roto al 60% en paso 2 es un cuello de botella severo. Arreglar B aumenta el valor de todo lo demás (incluido futuro tráfico). Es claramente P0.

Refinando semanas 5-8:
Como tiene soporte 2h diarias, quizás puede reducir ese soporte automatizando respuestas o creando documentación/video FAQs (relacionado con D). Los videos pueden incluir tutoriales que reduzcan soporte. Entonces D no solo es marketing, también reduce carga de soporte futura.

D propuesta: 5 videos de contenido puro + 5 tutoriales/tour del producto. Así sirven para marketing Y soporte. Eso optimiza las 2h diarias de soporte en el futuro.

Semanas 5-8:
- 2 semanas: Iterar B basado en datos. O hacer "2da ronda" de mejoras de conversión (email de bienvenida, empty states, etc.). 
- 2 semanas: Trab