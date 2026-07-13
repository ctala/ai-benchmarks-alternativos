# Claude Fable 5 (suscripción) — business_audit/roadmap_restriccion_capacidad

- model_id: `claude-fable-5`
- success: True  | final: 5.03 | quality: 6.0
- latency_total: 50.279s | tokens_per_second: 38.4
- input_tokens: 2 | output_tokens: 1933

## Respuesta completa

## Primero, la matemática real

4h/día × 5 días × 8 semanas = **~160 horas reales**. Los esfuerzos que estimaste son a tiempo completo (~8h/día), así que a tu capacidad real todo cuesta el doble:

| Iniciativa | Esfuerzo nominal | Esfuerzo real (a 4h/día) | ¿Cabe en 8 semanas? |
|---|---|---|---|
| B – Flujo de alta | 1 semana | ~2 semanas | Sí |
| D – 10 videos | 2 semanas | ~4 semanas | Sí |
| A – Rewrite | 3 meses FT | **~6 meses** | No, ni de cerca |
| C – Panel | 3 semanas | ~6 semanas, **bloqueado por A** | No |

## El orden

**Semanas 1-2: B.** Pierdes al 60% en el paso 2. Es la fuga más grande del negocio y la más barata de tapar. Cada semana que no lo arreglas, todo lo demás (contenido, ads, referidos) rinde al 40%. Instrumenta el funnel antes de tocar nada para poder medir el antes/después. Bonus probable: menos gente atascada en el alta = menos tickets de soporte = recuperas parte de tus 2h diarias de operación.

**Semanas 3-6: D.** Con el alta arreglada, ahora sí vale la pena mandar tráfico. Graba en batch (2-3 sesiones largas, no 10 sesiones sueltas) y el contenido sigue trabajando solo después.

**Semanas 7-8: buffer.** No lo llenes. Como fundador solo, algo se va a atrasar, un cliente se va a caer, vas a perder días en soporte. Si sobra tiempo: iterar B con la data de las semanas 1-6.

## A y C: no, y por qué

**A no es una iniciativa de trimestre, es una hipoteca.** 3 meses a tiempo completo son 6 meses tuyos reales, durante los cuales el producto se congela, el soporte sigue comiéndote 2h/día y no entra nada nuevo. Los rewrites completos en empresas de una persona tienen una tasa de mortalidad altísima. Alternativa: identifica los 2-3 dolores concretos que te hacen querer el rewrite y arréglalos incrementalmente, módulo a módulo, en trimestres futuros.

**C muere con A**, pero cuestiona la dependencia: ¿el panel de métricas *realmente* necesita el framework nuevo, o eso es una racionalización para justificar A? Si puedes construirlo sobre el stack actual, vuelve a la mesa el próximo trimestre. Y antes de construirlo, valida: ¿cuántos clientes lo pidieron con nombre y apellido?

## Resumen

1. B (sem 1-2): tapar la fuga del 60%
2. D (sem 3-6): llenar el embudo ya arreglado
3. Buffer (sem 7-8)
4. A: matar como rewrite, convertir en mejoras incrementales
5. C: próximo trimestre, desacoplado de A y con demanda validada

La regla que ordena todo esto: **con 4h/día, solo caben apuestas que se pagan en semanas, no en meses.**