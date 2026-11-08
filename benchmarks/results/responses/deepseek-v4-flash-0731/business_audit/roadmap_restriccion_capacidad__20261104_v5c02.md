# DeepSeek V4 Flash 0731 — business_audit/roadmap_restriccion_capacidad

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 28.566s | tokens_per_second: 144.7
- input_tokens: 344 | output_tokens: 4133

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

**No puedes hacer todo. Con 4h/día reales y 8 semanas, tu capacidad es ~160h.**

- **B** (arreglar alta): ~1 semana → **20h**
- **D** (10 videos): ~2 semanas → **40h**
- **C** (panel métricas): ~3 semanas → **60h**, pero **depende de A**
- **A** (reescribir framework): ~3 meses full-time → **mucho más de 160h**, no cabe ni de lejos

**Orden del trimestre:**

1. **Semana 1: B**  
   Es la única iniciativa de alto impacto que cabe ya. Arreglar el paso 2 del alta puede recuperar ingresos/usuarios de forma inmediata. Además, es corta y te da datos para decidir lo demás.

2. **Semanas 2-3: D**  
   Graba los 10 videos. Es contenido que trabaja para ti mientras haces otras cosas. No requiere que A exista. Impacto medio, pero acumulativo.

3. **Semanas 4-8: NO hagas A ni C.**  
   A no termina en el trimestre y C no puede construirse sin A. Empezar A ahora te dejaría con una migración a medias, sin flujo arreglado y sin tracción nueva. Es la forma más rápida de morir como fundador solo.

   Usa esas 5 semanas para:
   - Reducir las 2h/día de soporte (automatizar, documentar, cobrar por soporte).
   - Hablar con clientes y entender qué métricas quieren (para C futuro).
   - Hacer mejoras pequeñas de conversión/activación.
   - Planificar A como proyecto del **próximo trimestre**, dividido en fases pequeñas y solo si el negocio ya no depende de tu intervención diaria.

**En una frase:**  
Primero B, luego D, y olvídate de A/C este trimestre. A es una apuesta de futuro, pero no puedes apostar todo cuando todavía pierdes al 60% en el alta.