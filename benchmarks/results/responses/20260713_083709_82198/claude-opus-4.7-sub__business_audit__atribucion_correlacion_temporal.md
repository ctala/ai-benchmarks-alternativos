# Claude Opus 4.7 (suscripción) — business_audit/atribucion_correlacion_temporal

- model_id: `claude-opus-4-7`
- success: True  | final: 6.07 | quality: 7.2
- latency_total: 41.677s | tokens_per_second: 34.3
- input_tokens: 6 | output_tokens: 1428

## Respuesta completa

# No se puede saber si la secuencia funcionó

Con los datos que me pasás, **no puedo atribuir el crecimiento a los emails**. Te explico por qué y qué haría falta.

## El problema: tres cosas cambiaron al mismo tiempo

En marzo activaste tres palancas casi en simultáneo:

1. **1 de marzo** — secuencia de 5 emails al plan gratuito
2. **3 de marzo** — $400 en publicidad paga
3. **12 de marzo** — mención de un creador con audiencia grande

Las 5 altas extra (9 → 14) podrían venir de cualquiera de las tres, de una combinación, o incluso de estacionalidad de marzo vs febrero (marzo tiene 3 días más, ~11% más de exposición base). **No hay forma matemática de separar los efectos con estos datos.**

Esto se llama variables confundidas: cuando dos o más causas posibles se mueven a la vez, la correlación temporal con el resultado no prueba nada sobre cuál causó qué.

## Además, la muestra es diminuta

Pasar de 9 a 14 altas son **5 conversiones de diferencia**. Con números tan chicos, el ruido normal mes a mes puede explicar el salto sin que haya pasado nada real. Necesitarías varios meses de historial para saber cuál es la variabilidad "de base" de tu negocio.

## Y ojo con el MRR

El MRR subió 29% ($4.100 → $5.300 = +$1.200). Si dividís $1.200 entre 5 altas nuevas netas, da $240 por alta, muy por encima de cualquier plan mensual razonable. Eso sugiere que **parte del salto de MRR no viene de altas nuevas** — puede ser upgrades de tier, pases a anual, recuperación de churn, o cambios de precio. Sin desglosar el MRR por fuente (new / expansion / reactivation / churn), el "+29%" tampoco te dice nada específico sobre la secuencia de emails.

## Qué haría falta para estar seguros

En orden de impacto:

1. **Métricas propias de la secuencia de email**, no del MRR global:
   - Cuántos free recibieron el email 1, 2, 3, 4, 5
   - Open rate y click rate por email
   - Cuántos de los que clickearon terminaron pagando (con UTM o link único por email)
   - Ventana de atribución clara (¿cuenta como "por email" si paga a los 30 días?)

2. **Desglose del MRR de marzo**: cuánto es new business, cuánto expansion, cuánto reactivation. Sin esto el +29% es opaco.

3. **Aislar variables**. Idealmente:
   - Grupo control: un subset del plan gratuito que NO recibió la secuencia
   - Comparar tasa de conversión del grupo con email vs sin email
   - Si no querés hacer holdout, al menos separar temporalmente: mes con emails y sin ads/mención, después mes con emails + ads

4. **Fuente de cada alta de marzo**: preguntar en el onboarding "¿cómo llegaste?" o mirar UTMs. Si de las 14 altas, 8 vienen del creador, 4 de ads y 2 de email, la historia cambia por completo.

5. **Baseline histórico**. ¿Cuánto varían las altas mes a mes normalmente? Si en tu negocio es normal oscilar entre 7 y 15 altas mensuales sin hacer nada, el salto a 14 está dentro del ruido.

## Conclusión

**"La secuencia funcionó" es una respuesta que los datos no sostienen.** Puede que haya funcionado, puede que no haya movido nada, puede incluso que haya restado (poco probable, pero no lo podés descartar). Lo único que sabés con certeza es que en marzo hiciste tres cosas y las altas subieron 5. Nada más.

Antes de escalar la inversión en emails, ads o creadores basándote en este mes, invertí una semana en instrumentar los puntos 1 y 4. Sin eso, cualquier decisión de presupuesto va a ciegas.