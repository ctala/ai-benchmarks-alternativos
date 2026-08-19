# MiniMax M3 — business_audit/atribucion_correlacion_temporal

- model_id: `minimax/minimax-m3`
- success: True  | final: 4.95 | quality: 4.54
- latency_total: 22.357s | tokens_per_second: 57.8
- input_tokens: 373 | output_tokens: 1292

## Respuesta completa

**Conclusión directa: con estos datos no se puede saber si la secuencia funcionó.**

Los números que me pasas muestran que *algo* mejoró en marzo (MRR +29%, altas +5), pero hay tres cosas moviéndose al mismo tiempo:

1. La secuencia de emails (1 de marzo)
2. La pauta publicitaria de $400 (3 de marzo)
3. La mención del creador con audiencia grande (12 de marzo)

Cualquiera de las tres —o las tres juntas, o ninguna— podría explicar el salto. El resultado es compatible con que la secuencia haya sido un éxito, un fracaso, o irrelevante. Los datos no permiten separar los efectos.

Un detalle adicional que me llama la atención: las altas pasaron de 9 a 14, es decir 5 más. Si el ARPU de esos nuevos usuarios es parecido al de los anteriores, esos 5 usuarios extra explican buena parte (o todo) del incremento de $1.200 en MRR, lo que sugiere que **el crecimiento vino sobre todo de nuevas conversiones, no de upgrades ni de reducción de churn** — pero esto no nos dice *desde qué canal* llegaron.

---

**Qué haría falta para estar seguros**, en orden de utilidad:

1. **Un grupo de control (holdout).** La mitad de los usuarios del plan gratuito recibe la secuencia, la otra mitad no, en un período definido. Comparas conversión a pago entre ambos grupos. Sin esto, cualquier conclusión es especulación.

2. **Métricas atribuibles a la secuencia en sí:** tasa de apertura, CTR, y —lo más importante— cuántos de los 14 nuevos pagantes hicieron click en un email de la secuencia en los X días previos. Eso te da una cota superior del efecto (no todos los que convierten tocaron el email, así que el efecto real está entre 0 y esa cifra).

3. **Línea base más larga.** Un solo mes previo no alcanza para saber si marzo iba a crecer de todas formas por estacionalidad, momentum previo, etc. Idealmente 3–6 meses de historia.

4. **Descomponer las altas por fuente de adquisición:** cuántas vinieron del video del creador, cuántas del anuncio, cuántas "directas/orgánicas", y de esas, cuántas eran usuarias free que recibieron la secuencia.

---

**Lo que haría yo con lo que tenés hoy:** no afirmaría que la secuencia "funcionó" ni que "no funcionó" en ningún reporte. Como mucho diría: "En marzo el MRR creció 29% y las altas 56%, en coincidencia con tres intervenciones simultáneas; no podemos atribuir causalidad sin un test controlado."

Si la secuencia te salió barata de mantener, dejala corriendo y montá un holdout la próxima vez que lances algo. Si te salió cara, la respuesta honesta es que hoy no sabés si vale la pena.