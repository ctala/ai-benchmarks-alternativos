# Claude Haiku 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.63 | quality: 8.0
- latency_total: 11.207s | tokens_per_second: 163.4
- input_tokens: 420 | output_tokens: 1831

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

## Orden del trimestre

**1. B: Arreglar el flujo de alta (semanas 1-2)**
Es lo más barato y de mayor impacto. Perder al 60% en el paso 2 significa que cualquier tráfico que consigas después se desperdicia. Hazlo primero.

**2. D: Videos de contenido (semanas 3-4)**
Grábalos cuando el flujo ya esté arreglado, para que el tráfico que generen convierta. Si los publicas antes, pagas por atraer gente a un embudo roto.

**3. Semanas 5-8: capacidad libre (~100h)**
Dos opciones, en este orden:
- **Reducir las 2h/día de soporte.** Documenta las preguntas más repetidas, crea respuestas guardadas, automatiza lo que se pueda. Liberar 1h/día te da un 25% más de capacidad de construcción, y ese efecto dura para siempre.
- **Medir el resultado de B y D** y decidir qué sigue según los datos.

## Lo que sale del trimestre

**C (panel de métricas): fuera.** Depende de A, y A no cabe en este trimestre. Ni siquiera empezar C tiene sentido.

**A (reescribir la plataforma): no lo empieces ahora.** Son unas 3 semanas-persona completas, y tú tienes ~160h en total este trimestre. Tu capacidad real no alcanza ni para la mitad. Además, una reescritura a medias te deja con dos bases de código y ningún beneficio. Si el dolor técnico es real, escríbelo con ejemplos concretos (qué tarda, qué se rompe, qué te impide lanzar) y planifícalo para el siguiente trimestre, con el soporte ya reducido para tener más horas.

## Cálculo de capacidad

- 4h/día × 5 días × 8 semanas ≈ **160h** de construcción
- B ≈ 20h, D ≈ 40h → **60h usadas**, ~100h para soporte y medición
- A necesitaría 300-500h según cómo lo midas. No entra.

Si tu semana laboral es distinta, ajusta los números, pero la conclusión no cambia.