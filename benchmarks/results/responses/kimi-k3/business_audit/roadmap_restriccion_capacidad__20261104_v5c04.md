# Kimi K3 — business_audit/roadmap_restriccion_capacidad

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 5.29 | quality: 6.0
- latency_total: 76.919s | tokens_per_second: 53.8
- input_tokens: 388 | output_tokens: 4139

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

## La matemática primero

Tienes 4h/día × 8 semanas ≈ **160h de construcción**. A solo cuesta 3 meses a tiempo completo (~480h, y los rewrites se desvían 2-3x). A no compite por prioridad: **no cabe físicamente**. Eso ya resuelve media decisión, y C cae con ella.

## El trimestre

**Semanas 1-2 — B (arreglar el alta)**
Prioridad absoluta. Perder al 60% en el paso 2 es un impuesto sobre *todo lo demás*: cada video de D, cada euro de marketing, cada mejora futura pierde el 60% antes de llegar. Es la iniciativa con mejor ratio impacto/esfuerzo que tienes.
- Define el éxito antes de tocar código (ej.: completación del paso 2 de 40% → 70%)
- Instrumenta antes y después, o no sabrás si funcionó

**Semanas 3-5 — D (videos)**
Ahora sí: contenido hacia un funnel que funciona. Publica sobre la marcha, no los 10 al final.

**Semanas 6-7 — Atacar tus 2h/día de soporte**
Es tu mejor inversión de capacidad disponible. Si recuperas 0.5-1h/día, son ~50h/mes para siempre, no solo este trimestre. Sospecho que parte de ese soporte viene del paso 2 roto — B ya debería ayudar. Plantillas, FAQ, automatizar lo repetitivo.

**Semana 8 — Buffer + segunda iteración de B**
Los datos de las semanas 1-2 te dirán si necesita otra pasada. Si no, esto absorbe lo que se desvíe (algo se desviará).

## Fuera del trimestre

- **A**: No la empieces "para ir avanzando". Un rewrite a medias es peor que no empezarlo: cero valor entregado, rama que se pudre, y C sigue bloqueada igual. La decisión real de A no es *cuándo* sino *si*: ¿rewrite completo o arreglo quirúrgico de rendimiento? Con los datos de B sabrás si la velocidad realmente te cuesta conversión. Decide eso a fin de trimestre, con 12+ semanas de runway por delante.
- **C**: Bloqueada por A. Una pregunta honesta: ¿la dependencia es técnica dura o es comodidad? Si una versión mínima cabe en el stack actual en 1 semana, puede competir por las semanas 6-7. Si no, próximo trimestre, después de decidir A.

## Resumen

**B → D → reducir soporte → iterar B.** Entregas el arreglo de mayor impacto en la semana 1, alimentas un funnel que ya funciona, y terminas el trimestre con más capacidad de la que empezaste — que es lo que necesitas para que A sea siquiera discutible en Q+1.