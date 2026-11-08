# Claude Opus 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 25.434s | tokens_per_second: 91.7
- input_tokens: 420 | output_tokens: 2332

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

# Plan del trimestre

## Primero, la capacidad real

- **8 semanas × 5 días × 4 h = ~160 h de construcción.**
- Si tus estimaciones de "tiempo completo" se basan en tu jornada de 6 h, trabajas al **~67 % de ese ritmo**. Cada semana estimada te cuesta **~1,5 semanas de calendario**.
- En total tienes **~5,3 semanas "de tiempo completo"** este trimestre, y menos si dejas margen para imprevistos (debes dejarlo).

| Iniciativa | Esfuerzo estimado | Semanas reales para ti | ¿Cabe? |
|---|---|---|---|
| A) Reescritura | ~13 sem | **~20 sem** | ❌ Ni de lejos |
| B) Flujo de alta | 1 sem | **~1,5 sem** | ✅ |
| C) Panel de métricas | 3 sem + A | Bloqueada por A | ❌ |
| D) 10 vídeos | 2 sem | **~3 sem** | ✅ |

**A y C quedan fuera del trimestre.** No es una decisión de prioridad: es aritmética.

## El orden

**Semanas 1–2 → B: arreglar el alta**
- Es lo de mayor impacto por hora con mucha diferencia: perder al 60 % en el paso 2 significa que más de la mitad de todo lo que consigues se pierde ahí.
- Deja montada la medición del embudo antes de tocar nada, para comparar antes y después.

**Semanas 3–5 → D: los 10 vídeos**
- Van después de B a propósito. Los vídeos traen tráfico, y no tiene sentido mandarlo a un embudo que pierde 6 de cada 10 personas. B multiplica el retorno de D.
- Publícalos de forma escalonada si puedes, para ir viendo qué funciona.

**Semanas 6–7 → Recuperar capacidad (lo que no está en tu lista)**
- Tu mayor restricción no es ninguna iniciativa: son las **2 h diarias de soporte**. Dedica estas semanas a reducirlas con documentación, respuestas plantilla, automatizaciones o arreglando las causas de los tickets más repetidos.
- Si recuperas 1 h al día, pasas de 4 h a 5 h de construcción: **+25 % de capacidad para siempre**. Ninguna de tus cuatro iniciativas tiene ese retorno.
- Reserva 2–3 días para un **análisis de A**: qué te frena exactamente del framework actual y si se puede migrar por partes en lugar de reescribir todo.

**Semana 8 → Margen**
- Las estimaciones de un fundador solo casi siempre se quedan cortas. Si llegas aquí sin retrasos, adelanta trabajo de soporte o graba algún vídeo extra.

## Por qué no empezar A "aunque sea un poco"

Una reescritura a medias es el peor estado posible: mantienes dos bases de código, no entregas nada nuevo a clientes y el soporte sigue consumiéndote. Con 4 h/día, A te ocuparía **casi dos trimestres completos sin entregar nada**. Antes de comprometerte, el análisis de la semana 6–7 debería responder:

1. **¿La reescritura completa es necesaria, o hay una migración incremental?**
2. **¿C depende de verdad de A?** Muchas veces se puede hacer una versión mínima del panel sobre la plataforma actual. Si es así, C podría entrar el trimestre que viene sin esperar a A.

## Si tus estimaciones son de jornadas de 8 h

Entonces vas al 50 %: B te lleva ~2 semanas y D ~4. Ocuparían 6 de las 8 semanas. El orden sería el mismo, pero el bloque de soporte se reduciría a lo mínimo y quedarían 2 semanas de margen.

**Resumen:** B → D → reducir soporte y analizar A → margen. A y C pasan al trimestre siguiente, y llegarás a ellos con más capacidad y con datos para decidir.