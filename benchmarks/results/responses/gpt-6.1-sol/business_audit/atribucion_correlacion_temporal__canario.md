# GPT-6.1 Sol — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 9.595s | tokens_per_second: 53.6
- input_tokens: 224 | output_tokens: 514

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

**Conclusión: no se puede saber si la secuencia de emails funcionó con estos datos.** Marzo terminó mejor que febrero, pero no podemos atribuir esa mejora a los emails.

Los datos muestran:
- El MRR subió de $4.100 a $5.300: **+$1.200, un 29,3%**.
- Las altas al plan pago pasaron de 9 a 14: **5 más, un 55,6%**.

Pero en marzo también empezaste a pagar publicidad y recibiste una mención de un creador. Cualquiera de esas acciones —o su combinación— pudo contribuir al crecimiento. Además:
- **Falta el denominador:** 14 altas no implican una mayor tasa de conversión si también aumentó mucho la cantidad de usuarios gratuitos.
- **El MRR no mide solo altas:** también cambia por bajas, cambios de plan y descuentos.
- **Hay pocos casos y solo dos meses:** no podemos descartar variación normal ni evaluar una tendencia previa.

### Qué haría falta para estar seguros

**La prueba más sólida sería un experimento con grupo de control:**
1. Asignar al azar a usuarios gratuitos elegibles a dos grupos: uno recibe la secuencia y el otro no.
2. Comparar la conversión a pago durante una misma ventana —por ejemplo, 30 días desde la asignación— y el ingreso generado por usuario.
3. Mantener iguales las demás condiciones y procurar que los canales de adquisición estén equilibrados entre grupos.
4. Reunir suficientes usuarios y conversiones para estimar el efecto con una incertidumbre razonable. Con estos datos no se puede calcular aún qué tamaño de muestra necesitarías.

**Para investigar lo que ya pasó**, pediría:
- Usuarios gratuitos elegibles y fechas de registro.
- Quién recibió la secuencia y cuándo.
- Fechas de conversión y canal de adquisición, distinguiendo usuarios previos a marzo de los nuevos.
- Desglose del cambio de MRR: altas, bajas y cambios de plan.
- Historial de varios meses para contextualizar la variación habitual.

Eso permitiría buscar indicios, pero **ni un clic en un email antes de pagar demuestra que el email causó la compra**.

Mi lectura para tomar decisiones: **marzo mejoró; la contribución de la secuencia sigue sin demostrarse.** No la declararía un éxito ni un fracaso: la pondría a prueba con un control.