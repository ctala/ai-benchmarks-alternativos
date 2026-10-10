# Claude Haiku 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.03 | quality: 10.0
- latency_total: 11.813s | tokens_per_second: 157.5
- input_tokens: 366 | output_tokens: 1861

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

**Conclusión: con estos datos no se puede saber si la secuencia de emails funcionó.** Los números son compatibles con que ayudara, con que no hiciera nada, y con que el efecto principal viniera de otra cosa.

**Por qué no se puede atribuir**

- **Tres cambios al mismo tiempo.** Activaste la secuencia el 1 de marzo, pusiste publicidad el 3 y un creador con audiencia grande te mencionó el 12. Cualquiera de los tres puede explicar el aumento.
- **El creador probablemente pesa mucho.** Una mención en un video de una audiencia grande suele traer muchos visitantes de golpe. Si esos visitantes se registraron en el plan gratuito, entraron en la secuencia y eso no lo distingue de un efecto de los emails.
- **Las muestras son muy pequeñas.** Pasar de 9 a 14 altas es una diferencia de 5 personas. Con números tan bajos, una variación de ese tamaño puede aparecer por puro azar. Estadísticamente, no es distinguible de ruido.
- **El MRR mezcla más cosas.** El +29% incluye altas nuevas, bajas, cambios de precio o de plan y upgrades. No sabemos cuánto de ese cambio viene de las 5 altas adicionales.
- **No hay grupo de control.** Todos los usuarios gratuitos recibieron la secuencia, así que no hay con qué comparar qué habría pasado sin ella.

**Qué sí podemos decir**

- Las altas subieron de 9 a 14 y el MRR subió 29%. Ambas cosas son ciertas, pero no nos dicen la causa.
- Es posible que la secuencia haya contribuido. Tampoco hay evidencia de que no lo hiciera.

**Qué haría falta para tener una respuesta**

1. **Un grupo de control real.** Lo más limpio es asignar aleatoriamente a un porcentaje de usuarios gratuitos (por ejemplo, 20-50%) a no recibir la secuencia durante un período, y comparar tasas de conversión. Si no puedes dejar a nadie fuera, un despliegue escalonado por cohortes también sirve.
2. **Atribución por origen.** Separar las altas de marzo por fuente: vino del video del creador, de los anuncios, o fue orgánico. Con UTMs o una pregunta "¿cómo nos conociste?" en el registro, puedes ver qué parte de las 14 altas vino de dónde.
3. **Conversión por exposición.** Comparar la tasa de conversión de quienes abrieron o hicieron clic en los emails frente a quienes no lo hicieron. Ojo: esto no prueba causalidad, porque quien abre emails suele estar más interesado de entrada, pero da una pista.
4. **Más tiempo y más datos.** Con 9 y 14 altas, cualquier conclusión es frágil. Necesitas varios meses o una base de usuarios más grande para que las diferencias sean distinguibles del azar.
5. **Desglose del MRR.** Separar cuánto del cambio vino de altas nuevas, de bajas (churn), de upgrades y de cambios de precio.

**Mientras tanto**

No tomaría decisiones fuertes (como escalar la secuencia o gastar más en publicidad) basándote solo en este mes. Si quieres una señal rápida, mira la tasa de conversión de las altas de marzo que llegaron por email frente a las que llegaron por el creador o por anuncios. Eso no resuelve la pregunta, pero te dice dónde mirar primero.