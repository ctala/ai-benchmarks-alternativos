# Muse Ember — business_audit/atribucion_correlacion_temporal

- model_id: `meta/muse-ember`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 8.113s | tokens_per_second: 376.6
- input_tokens: 236 | output_tokens: 3055

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

**Conclusión corta: no se puede saber.**

No digo que la secuencia no funcionó. Digo que con estos datos, decir que funcionó — o que no funcionó — sería inventarlo.

Marzo fue mejor en bruto que febrero, eso sí es un hecho. Pero atribuírselo a los emails es imposible porque lanzaste tres cosas a la vez.

### Por qué no se puede atribuir

**1. Tienes 3 cambios superpuestos en 11 días**
- 1 de marzo: secuencia de 5 emails
- 3 de marzo: empiezas publicidad pagada ($400)
- 12 de marzo: mención de un creador grande

No hay una ventana limpia para aislar el efecto de los emails. Todos estos escenarios encajan igual de bien con tus números:

A) Los emails causaron las +5 altas extra (de 9 a 14), publicidad y creador aportaron 0.
B) Los emails aportaron 0, publicidad + creador causaron las +5.
C) Una mezcla de los tres.
D) Los emails incluso perjudicaron un poco, pero publicidad/creador lo compensaron de sobra.

Sin más datos, no hay forma de distinguir A de B, C o D.

**2. Los números son pequeños y ruidosos**
Pasar de 9 a 14 altas son 5 altas más. Con volúmenes así, una diferencia de 5 puede ser simple variación normal de un mes a otro. No tenemos serie histórica para saber si 9 era bajo, 14 era alto, o ambos son normales.

**3. El MRR no mide el efecto de los emails**
MRR subió de $4.100 a $5.300 (+$1.200). Pero el MRR depende de altas nuevas *menos* bajas, más upgrades/downgrades y planes anuales. No me das churn, ARPU ni altas netas.

De hecho, +$1.200 no se explica solo con “5 altas extra” salvo que el precio sea muy alto o haya habido upgrades/planes anuales. Falta el desglose: ¿cuántas bajas hubo en marzo? ¿cuánto vino de clientes nuevos vs. existentes?

**4. Falta el denominador**
La pregunta no es solo “¿hubo más altas?”, es “¿convirtió mejor un usuario gratuito expuesto a los emails?”

Si la publicidad te trajo 200 usuarios gratuitos nuevos en marzo, 14 altas podría ser una tasa de conversión *peor* que en febrero, aunque el número absoluto suba. Sin usuarios gratuitos totales y expuestos a cada email, no hay tasa.

### Qué haría falta para estar seguros

Necesitas variación en la exposición que no esté ligada a los otros canales. En la práctica, para una empresa pequeña:

1. **Grupo de control.** La próxima vez, divide aleatoriamente la lista de gratuitos: 80% recibe la secuencia, 20% no recibe nada durante 3-4 semanas. Ambos grupos viven el mismo marzo — misma publicidad, mismo creador, misma estacionalidad — así que la diferencia en conversión gratuito -> pago sí sería atribuible a los emails.

2. **Atribución por fuente y por fecha.** Marca todo con UTMs y guarda para cada alta: fuente (email / ads / creador / orgánico), fecha, si era usuario gratuito antiguo o nuevo de marzo, y si abrió/clicó los emails. Eso no es prueba causal, pero al menos acota.

3. **Métricas completas por cohorte.** Conversión = altas pagas / usuarios gratuitos elegibles al inicio del periodo, separada por expuestos vs. no expuestos. Y churn/ARPU para interpretar el MRR.

4. **Tiempo.** Con ~10 altas al mes, necesitarás varios meses de test para detectar un efecto pequeño sin que lo tape el ruido.

### Qué puedes rescatar de marzo, sin engañarte

Si tienes los datos guardados, podrías mirar retrospectivamente:
- ¿Las 14 altas de marzo vinieron de usuarios gratuitos antiguos (candidatos a los emails) o de usuarios nuevos traídos por ads/creador?
- ¿Se concentraron después del 12 de marzo?
- ¿Alguna alta ocurrió en las 24-48h tras un email, desde un clic a la página de pago?

Si, por ejemplo, todas vinieron de referidos del creador y ninguna de la base antigua, eso *sugiere* que los emails no movieron nada. Pero seguiría siendo una pista, no una prueba.

Mi recomendación como analista: no escales ni cortes nada basándote en marzo. Trátalo como un mes contaminado por tres experimentos a la vez, y la próxima secuencia lánzala con un grupo de control desde el día uno.