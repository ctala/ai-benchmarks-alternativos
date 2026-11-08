# GPT-6.1 Sol — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 10.807s | tokens_per_second: 50.1
- input_tokens: 224 | output_tokens: 541

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

**Conclusión: marzo mejoró, pero no se puede saber con estos datos si la secuencia de emails funcionó.** Tampoco podemos concluir que no funcionó: su efecto no está aislado.

El MRR pasó de $4.100 a $5.300 (**+$1.200; +29,3%**) y las altas al plan pago de 9 a 14 (**5 más; +55,6%**). Son mejoras observadas, no una estimación del impacto de los emails.

Hay tres problemas para atribuirles el resultado:

- **Coincidieron otras acciones:** la publicidad y la mención del creador pudieron aportar usuarios y ventas, por sí solas o combinadas con los emails.
- **Falta el denominador:** no sabemos cuántos usuarios gratuitos podían convertirse cada mes. Más altas podrían deberse a más usuarios, sin que mejorase la tasa de conversión.
- **El MRR no depende solo de las altas:** también cambia por cancelaciones, cambios de plan y precios. No sabemos qué explica los $1.200 adicionales.

### Qué haría falta para estar seguros

**La mejor prueba sería un experimento aleatorio:** dividir a los usuarios gratuitos elegibles entre un grupo que reciba la secuencia y otro que no la reciba —o que la reciba más tarde—. Ambos deberían medirse durante la misma ventana, por ejemplo, los 30 días posteriores a entrar al experimento.

Compararía:
- **Conversión a pago** sobre el total de usuarios asignados a cada grupo.
- **Ingresos generados por usuario**, y después retención o cancelaciones.

El tamaño de muestra necesario dependería de la conversión habitual y del efecto mínimo que te interese detectar. Con solo 14 altas en marzo, **no daría por hecho que un único mes alcance para obtener una conclusión precisa**.

Para investigar marzo, pediría además:
- Usuarios gratuitos elegibles y nuevos usuarios por fecha y fuente.
- Quién recibió la secuencia y cuándo, y fechas de las conversiones.
- Desglose del cambio de MRR: altas, bajas y cambios de plan.
- Varios meses previos para evaluar tendencia y variación habitual.

Eso permitiría entender mejor lo ocurrido, pero **abrir un email o comprar después de recibirlo no demuestra que el email causara la compra**.

**Mi decisión hoy:** no presentaría el +29% como éxito de la secuencia. Diría: “El negocio creció en marzo; el aporte específico de los emails todavía no está demostrado”, y prepararía una prueba con grupo de control.