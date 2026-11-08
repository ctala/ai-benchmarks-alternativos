# Nemotron 3 Super — business_audit/atribucion_correlacion_temporal

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.93 | quality: 10.0
- latency_total: 26.88s | tokens_per_second: 70.1
- input_tokens: 243 | output_tokens: 1884

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

**Conclusión: No se puede saber si la secuencia de emails funcionó.**

Con los datos que tienes, no hay base para atribuir el aumento del MRR o de las altas a los emails. Lo único que se puede afirmar es que, en marzo, el MRR creció y hubo más altas que en febrero. Eso no demuestra causalidad.

### Por qué no se puede concluir

1. **No hay grupo de control.**  
   No sabes cuántos usuarios gratuitos se habrían convertido a pago en marzo aunque nunca hubieran recibido los emails. Sin una comparación (usuarios similares que no recibieron la secuencia), no puedes aislar el efecto de los emails.

2. **Hubo otras intervenciones al mismo tiempo.**  
   Empezaste publicidad pagada el 3 de marzo y un creador mencionó la comunidad el 12 de marzo. Cualquiera de esas dos acciones —o ambas— podría haber generado todas, algunas o ninguna de las nuevas altas. Los emails podrían haber sido irrelevantes, o podrían haber ayudado, pero los datos no lo separan.

3. **Falta de atribución por usuario.**  
   Sabes que hubo 14 altas en marzo frente a 9 en febrero, pero no sabes:
   - Si esas 14 personas eran usuarios gratuitos que recibieron los emails.
   - Si llegaron por la publicidad o por el video del creador.
   - Si se inscribieron antes o después de recibir cada email de la secuencia.

4. **El MRR no se desglosa.**  
   El aumento de $1.200 podría venir de nuevas altas, de upgrades de usuarios existentes, de menos cancelaciones (churn) o de una combinación. Sin ese detalle, no puedes vincular el MRR a la conversión de gratuitos a pago.

### Qué haría falta para estar seguros

Para poder decir con confianza si la secuencia de emails funcionó, necesitarías:

- **Un grupo de control:** usuarios del plan gratuito con características similares que no recibieron los emails, para comparar su tasa de conversión.
- **Tracking de la secuencia:** cuántos emails se entregaron, tasas de apertura, clics y, sobre todo, cuántos usuarios se convirtieron a pago *después* de recibir un email específico (con códigos de descuento únicos, UTM o seguimiento por enlace).
- **Origen de cada alta de marzo:** de dónde vino cada uno de los 14 usuarios que se hicieron de pago (email, publicidad, video del creador, búsqueda orgánica, otro).
- **Desglose del MRR:** cuánto del aumento se debe a nuevas altas, cuánto a upgrades y cuánto a menor churn.
- **Histórico previo:** cuántas altas y cuánto MRR hubo en enero y diciembre para saber si febrero fue un mes atípico y si marzo sigue una tendencia estacional.
- **Base de usuarios gratuitos al 1 de marzo:** para calcular la tasa de conversión real de la secuencia (altas por emails ÷ usuarios gratuitos que los recibieron).

Hasta que tengas eso, la respuesta honesta es: **los datos son compatibles con que los emails funcionaron, pero también son compatibles con que no tuvieran ningún efecto.** No hay evidencia suficiente para elegir una u otra.