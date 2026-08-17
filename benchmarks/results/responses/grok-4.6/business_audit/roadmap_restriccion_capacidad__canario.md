# Grok 4.6 — business_audit/roadmap_restriccion_capacidad

- model_id: `x-ai/grok-4.6`
- success: True  | final: 6.81 | quality: 8.0
- latency_total: 49.804s | tokens_per_second: 43.6
- input_tokens: 443 | output_tokens: 2170

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

**Haz B primero (esta semana). Luego D. No empieces A ni C este trimestre.**

Capacidad real: 8 semanas × ~4 h/día útiles ≈ 160 h de construcción (asumiendo 5 días/semana). Eso equivale a ~4 semanas-persona a jornada completa. A son ~12 semanas-persona a tiempo completo: no cabe, no se termina y no entrega valor. C está bloqueado por A. Empezar el rewrite ahora consume el trimestre entero sin resultado usable y deja el leak de conversión intacto.

Orden concreto:

1. **Semana 1 (inmediato): B — arreglo del flujo de alta.**  
   Alto impacto, esfuerzo pequeño, independiente, reduce la pérdida del 60 % en el paso 2. Es el único ítem que puede mover números este trimestre y aliviar (o no empeorar) las 2 h diarias de soporte. Termínalo y mídalo antes de tocar otra cosa.

2. **Semanas 2-3: D — los 10 vídeos.**  
   Impacto medio, esfuerzo contenido, no depende de nada. Contenido que puedes publicar mientras el funnel ya no pierde tanta gente. No lo alargues.

3. **Semanas 4-8: no A, no C.**  
   Usa el tiempo restante en:  
   - Iterar B si los datos lo piden (más conversiones = más soporte, así que vigila las 2 h operativas).  
   - Más contenido o mejoras pequeñas incrementales del producto actual.  
   - Deuda operativa que reduzca las 2 h diarias (para ganar capacidad el próximo trimestre).  

A y C quedan para un trimestre posterior, cuando tengas más horas netas o hayas validado que el rewrite sigue siendo la palanca correcta. Un rewrite de 3 meses a tiempo completo en un equipo de una persona con 4 h/día reales es un proyecto de 6+ meses calendario con alto riesgo de no terminar. No lo empieces a medias.

Criterio usado: impacto × probabilidad de terminar dentro de la capacidad real. B gana por goleada. D es el único compañero viable. A y C no caben.