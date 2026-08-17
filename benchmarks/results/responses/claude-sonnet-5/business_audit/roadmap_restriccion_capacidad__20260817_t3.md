# Claude Sonnet 5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 35.411s | tokens_per_second: 76.9
- input_tokens: 418 | output_tokens: 2722

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

# Primero, la matemática real (esto cambia todo)

Tus estimaciones están en "tiempo completo" (8h/día). Tú tienes 4h/día reales. Hay que convertir todo a tu unidad real antes de decidir nada:

| Iniciativa | Esfuerzo (full-time) | Esfuerzo real (4h/día) |
|---|---|---|
| A | ~13 semanas (520h) | **~26 semanas** |
| B | 1 semana (40h) | ~2 semanas |
| C | 3 semanas (120h) | ~6 semanas |
| D | 2 semanas (80h) | ~4 semanas |

**Capacidad disponible del trimestre: 8 semanas.**

# Conclusión dura: A es matemáticamente imposible este trimestre

26 semanas necesarias vs 8 disponibles. No es "ambicioso", es inviable. Si lo metes en el roadmap, garantizas que todo lo demás se retrasa y A queda a medio hacer (lo peor de los dos mundos: deuda técnica duplicada + nada terminado).

**C depende de A.** Como A no ocurre este trimestre, C tampoco puede ejecutarse. Sale del roadmap por transitividad, no por falta de valor.

# El plan de las 8 semanas

**Semanas 1-2 — B (arreglar el alta)**
Impacto alto, esfuerzo bajo, y cada semana que pasa sigues perdiendo 60% de la gente en el paso 2. Es la decisión con mejor ratio impacto/esfuerzo de las cuatro por lejos. Va primero sin discusión.

**Semanas 3-6 — D (10 videos)**
Impacto medio, no depende de nada, no compite con soporte. Bien para llenar el resto del trimestre con algo que compone (contenido sigue trabajando después de publicado).

**Semanas 7-8 — Buffer, no relleno**
No metas nada más "porque hay hueco". Dos usos concretos:
1. **Colchón**: tus 2h/día de soporte no son estables, y B seguramente generará trabajo de seguimiento (medir, iterar el embudo).
2. **Validar C sin construirlo**: habla con 5-10 clientes, muéstrales un mockup del panel de métricas. Cuesta 2-3 días, no 6 semanas, y te dice si vale la pena construirlo cuando A exista.

# Qué hacer con A (fuera del trimestre, pero no ignorarlo)

A no es una tarea de sprint, es una decisión estructural. Necesita una de estas dos cosas antes de entrar al roadmap:
- **Runway dedicado**: un trimestre completo casi exclusivo a eso (y aun así, 26 semanas reales vs 8 disponibles en un Q es ajustado).
- **Más manos**: contratar o traer ayuda técnica temporal, porque con 4h/día en solitario, A siempre va a perder contra cualquier cosa con impacto en 1-6 semanas.

Decide esto como founder, no lo metas a la fuerza en este trimestre. Ponlo en el radar del siguiente Q como "decisión go/no-go" con presupuesto/contratación, no como ítem de backlog.