# Inkling Small — business_audit/atribucion_correlacion_temporal

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 37.212s | tokens_per_second: 31.6
- input_tokens: 231 | output_tokens: 1175

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

**Conclusión: no se puede saber si la secuencia de emails funcionó.**

Los datos que pasas no permiten separar el efecto de los emails del efecto de la publicidad pagada ni de la mención del creador. Además, el volumen es pequeño (14 altas vs 9) y no tienes ninguna métrica de la secuencia misma ni de atribución.

Por qué la respuesta cómoda sería falsa:
- **Tres intervenciones simultáneas:** lanzaste emails (1 marzo), pagaste ads (3 marzo) y recibiste una mención orgánica masiva (12 marzo). El MRR subió 29 % y las altas subieron 5, pero no sabes cuánto de eso viene de cada canal.
- **No hay grupo de control:** no sabes qué habría pasado sin la secuencia. Si tu tendencia base ya era de crecimiento, esas 5 altas adicionales podrían ser ruido o estacionalidad.
- **No hay datos de la secuencia:** no sabes tasas de apertura, clics ni cuántos de los que recibieron los 5 emails convirtieron. Podrían haber convertido por el video, por el ad, o por otro motivo.
- **MRR no es solo altas:** no pasas bajas/churn ni cambios de plan. Una parte del salto de $1.200 podría ser retención o upsells, no nuevos pagos.
- **La publicidad es confusora directa:** $400 en ads pueden generar tráfico que se convierte sin que los emails tengan nada que ver.

**Qué haría falta para estar seguros:**
1. **Grupo de control:** dividir usuarios gratuitos en dos grupos (con/sin secuencia) y comparar tasas de conversión.
2. **Atribución de las altas:** saber de dónde vienen (email, ads, referral/organico, directo) mediante UTM, códigos de descuento o encuesta al momento de pagar.
3. **Métricas de la secuencia:** entregabilidad, open rate, click rate y conversion rate de cada email.
4. **Datos previos y de tendencia:** MRR y altas de los últimos 3-6 meses para ver si marzo es una anomalía o la norma.
5. **Aislar variables:** lanzar la secuencia sin ads ni influencer, o medir el impacto incremental comparando semanas con/sin cada intervención.
6. **Datos de bajas/churn:** para saber si el MRR subió por nuevos pagos o por menor fuga.

**Recomendación práctica:** no atribuyas ese +29 % a los emails en tu reporte interno. Si quieres validar la secuencia, haz una prueba controlada en el próximo ciclo (por ejemplo, a mitad de la lista de gratuitos) y mide la diferencia de conversión con y sin los 5 emails, manteniendo el resto constante.