# Claude Opus 5.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.76 | quality: 8.0
- latency_total: 21.18s | tokens_per_second: 89.0
- input_tokens: 420 | output_tokens: 1885

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

# Plan del trimestre: B → D → colchón. A y C no entran.

## Capacidad real

- **8 semanas × 5 días × 4 h = ~160 h** de construcción.
- Supongo que tus estimaciones "a tiempo completo" son semanas de 6 h/día (30 h). Entonces **160 h ≈ 5,3 semanas a tiempo completo**. Si las estimaste pensando en jornadas de 8 h, tienes aún menos (~4 semanas).

| Iniciativa | Esfuerzo en horas | ¿Cabe? |
|---|---|---|
| A) Reescritura | ~13 sem × 30 h = **~390 h** | ❌ Es 2,4 veces tu trimestre entero |
| B) Flujo de alta | **~30 h** | ✅ |
| C) Panel de métricas | ~90 h, pero **bloqueado por A** | ❌ No puede empezar |
| D) 10 videos | **~60 h** | ✅ |

## Orden

**Semanas 1–2: B (flujo de alta)**
- Va primero porque es lo más barato con mayor impacto, y además multiplica todo lo demás: los videos traerán tráfico a un alta que hoy pierde al 60%.
- Define antes la métrica: % que pasa del paso 2. Mide la línea base y lanza.

**Semanas 2–5: D (videos)**
- Agrupa la grabación (por ejemplo, 3–4 videos por sesión) para no fragmentar tu foco.
- Así lanzas el contenido cuando el alta ya no tiene fugas.

**Semanas 6–8: colchón deliberado (~70 h)**
No lo llenes de antemano. Úsalo para:
1. **Iterar sobre B** con datos reales. Un primer arreglo rara vez es el definitivo.
2. **Recuperar parte de tus 2 h diarias de soporte.** Es tu mayor palanca: bajar de 2 h a 1 h te da +25% de capacidad de construcción para siempre. Sirven FAQs, plantillas o automatizar lo repetitivo. Ojo: si B funciona, entrará más gente y el soporte subirá.
3. **Absorber retrasos.** Tus estimaciones de 1 y 2 semanas probablemente se queden cortas.

## Por qué A no entra (ni siquiera "empezarla")

- No cabe. Y las reescrituras casi siempre tardan más de lo estimado.
- Empezarla a medias es el peor escenario. Acabarías manteniendo dos sistemas, con el soporte diario encima, sin terminar ninguno.
- Lo que sí puedes hacer, si sobra colchón: **3–5 h para un documento de decisión sobre A**. ¿Qué duele exactamente hoy? ¿Se puede migrar por partes en lugar de reescribir todo? ¿Qué tendría que cambiar en tu operación para dedicarle 3 meses?

## Una pregunta sobre C

¿De verdad depende de A, o es más cómodo hacerlo en el framework nuevo? Si una versión mínima del panel se puede hacer en tu plataforma actual, quizá sea candidata para el próximo trimestre sin esperar a la reescritura. Vale la pena comprobarlo antes de dar por hecho que está bloqueada.

**Resumen:** B (sem. 1–2) → D (sem. 2–5) → iterar B y reducir soporte (sem. 6–8). A queda como decisión para el próximo trimestre, no como trabajo de este.