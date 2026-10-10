# Claude Fable 5.1 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 32.201s | tokens_per_second: 61.5
- input_tokens: 366 | output_tokens: 1980

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de datos de una empresa pequeña. Tu trabajo es proteger al equipo de conclusiones que los datos no sostienen. Prefieres decir 'no se puede saber' antes que dar una respuesta cómoda pero falsa.

**user:**

Tengo una comunidad de pago online. Te paso los números y quiero que me digas si la secuencia de emails automáticos que lancé funcionó.

- El 1 de marzo activé una secuencia de 5 emails para los usuarios del plan gratuito.
- MRR al 28 de febrero: $4.100
- MRR al 31 de marzo: $5.300 (+29%)
- Altas al plan pago en febrero: 9
- Altas al plan pago en marzo: 14

Contexto adicional: también el 3 de marzo empecé a pagar publicidad ($400 en el mes), y el 12 de marzo un creador con audiencia grande mencionó la comunidad en un video.

¿La secuencia de emails funcionó? Dame tu conclusión y qué haría falta para estar seguros.


## Respuesta completa

**Conclusión corta: no se puede saber.** Y no es una respuesta tímida: con estos datos no se puede ni siquiera afirmar que la secuencia haya tenido un efecto positivo "probablemente". El resultado de marzo es compatible con tres escenarios distintos: que los emails funcionaran muy bien, que no hicieran nada, o incluso que la publicidad y el creador hubieran traído más altas sin ellos.

## Por qué no se puede atribuir nada

**1. Tres cambios en el mismo mes.** Emails (1 de marzo), publicidad (3 de marzo) y la mención del creador (12 de marzo). Cualquier mejora en marzo puede venir de cualquiera de los tres o de la combinación. No hay forma de separar las contribuciones con los agregados mensuales.

**2. La diferencia es de 5 altas.** Pasar de 9 a 14 suena a +55%, pero en números absolutos son 5 personas. No sé cuánto varía tu cifra mensual normalmente. Si en enero tuviste 6 y en diciembre 13, 14 está dentro del ruido habitual. Necesito al menos 4-6 meses previos para saber si 14 es anormal.

**3. Los emails solo llegan a usuarios del plan gratuito que ya existían.** La publicidad y el creador traen gente *nueva*. Pregunta clave: de esas 14 altas, ¿cuántas eran usuarios que estaban en el plan gratuito antes del 1 de marzo? Si la mayoría se registró después del día 12 y pagó a los pocos días, eso apunta al creador, no a la secuencia (que, además, dura 5 emails y apenas habría empezado para ellos).

**4. El MRR no cuadra solo con altas.** +$1.200 de MRR con 14 altas implica un ticket medio alto o que hubo otros movimientos (upgrades, cambios de precio, menos bajas que otros meses). Sin el dato de bajas (churn) de febrero y marzo, el +29% no me dice nada específico sobre conversión.

## Qué haría falta para estar razonablemente seguros

**Con los datos que probablemente ya tienes:**
- Fecha de cada alta de marzo y fecha en que ese usuario entró al plan gratuito. Si las altas se concentran después del 12 y son usuarios de menos de 2 semanas de antigüedad, el crédito es del creador.
- De las 14, cuántas abrieron o hicieron clic en algún email de la secuencia antes de pagar. Es correlación, no causa, pero si es 0 o 1 ya tienes respuesta.
- Altas mensuales de los últimos 6 meses para ver la variabilidad normal.
- Bajas de febrero y marzo.
- Las métricas de los anuncios (clics, registros atribuidos por UTM).

**Para tener una respuesta real a futuro:**
- **Grupo de control (holdout):** de los usuarios gratuitos que entran a la secuencia, excluye aleatoriamente un 20-30% y compara la tasa de conversión a pago entre los que la reciben y los que no, a 30 y 60 días. Es lo único que aísla el efecto de los emails de todo lo demás. Con una comunidad pequeña tardará unos meses en acumular suficiente muestra, pero es la única forma limpia.
- Si no quieres holdout, al menos **no lances cambios a la vez**. Un canal nuevo por mes y conversión medida por cohorte de origen.

## Resumen

El mes fue bueno. Lo que no puedes decir, y te recomiendo no decir, es "la secuencia de emails subió el MRR un 29%". Si tienes que tomar una decisión ahora: mantén la secuencia (es barata y no hay señal de que perjudique), monta el holdout, y en 2-3 meses tendrás una respuesta de verdad.