# Grok 4.6 — business_audit/roadmap_restriccion_capacidad

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 42.438s | tokens_per_second: 60.1
- input_tokens: 443 | output_tokens: 2551

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

**B primero (ya), luego D. A y C no entran este trimestre.**

Capacidad real: 8 semanas × ~4 h/día de construcción. Eso son ~160 h (asumiendo 5 días laborables). Equivale a unas 4 semanas-persona a tiempo completo. El soporte/ops ya se come 2 h/día y no baja solo; si B funciona puede subir un poco la carga.

- **A** son ~3 meses a tiempo completo. Ni cabe ni se acerca. Empezarlo deja el trimestre a medias, aumenta riesgo de roturas (más soporte) y no entrega valor usable. Queda fuera.
- **C** depende de A terminado. Queda fuera.
- **B** es 1 semana, impacto alto e inmediato (estás perdiendo al 60 % en el paso 2). Es el único palanca que cabe de verdad y que puede mejorar el resto (más conversión = más señal, posiblemente menos fricción operativa a medio plazo).
- **D** es 2 semanas, impacto medio, independiente. Encaja después de tapar el agujero.

Orden concreto (calendario de 8 semanas):

- Semanas 1-2: solo B. Cierra el flujo de alta. Mide el drop antes/después. No toques nada más hasta que esté en producción y estable.
- Semanas 3-5/6: D. Los 10 vídeos. Prioriza los que apunten al problema que acabas de arreglar o a adquisición cualificada.
- Semanas restantes: buffer (imprevistos, soporte extra, pulido de B, o el siguiente ítem pequeño que surja). No empieces A. No empieces C.

Si al terminar B+D sobra tiempo real, reevalúa con datos nuevos. Un rewrite de plataforma con 4 h/día y ops encima es la forma clásica de no cerrar el trimestre con nada usable. El funnel roto sí lo es.