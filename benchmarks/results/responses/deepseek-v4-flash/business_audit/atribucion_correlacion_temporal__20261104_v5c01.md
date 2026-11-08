# DeepSeek V4 Flash (OpenRouter) — business_audit/atribucion_correlacion_temporal

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 13.433s | tokens_per_second: 45.4
- input_tokens: 235 | output_tokens: 610

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

## Conclusión: No se puede saber si la secuencia de emails funcionó

Los datos disponibles no permiten aislar el efecto de los emails porque hay **tres eventos distintos** en marzo que pudieron aumentar el MRR y las altas:

1. **Secuencia de emails** (activada el 1 de marzo) dirigida a usuarios del plan gratuito.
2. **Inicio de publicidad paga** (3 de marzo, $400 en el mes).
3. **Mención de un creador con audiencia grande** (12 de marzo).

Cualquier combinación de estos factores pudo generar el incremento observado (MRR +29%, altas +56%). Sin datos de atribución o un grupo de control, es imposible separar sus contribuciones.

### ¿Qué haría falta para estar seguros?

- **Atribución por fuente**: saber cuántas altas llegaron directamente desde los emails (por ejemplo, mediante enlaces con parámetros UTM), cuántas desde los anuncios y cuántas desde la mención del creador.
- **Tasa de conversión histórica**: comparar la tasa de conversión de usuarios gratuitos a pagos *antes* y *después* de la secuencia, controlando por estacionalidad y otras campañas.
- **Datos de churn**: el MRR también depende de cancelaciones. Si en febrero hubo más bajas que en marzo, parte del crecimiento podría deberse a menor churn, no a nuevas altas.
- **Experimento controlado**: lo ideal sería lanzar la secuencia solo a una parte de los usuarios gratuitos (grupo A) y no al resto (grupo B), midiendo la diferencia en conversiones.

Sin esa información, cualquier afirmación sobre la efectividad de los emails sería especulativa.