# GPT-5.6 Terra — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 8.41s | tokens_per_second: 81.6
- input_tokens: 224 | output_tokens: 686

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

**Conclusión:** con estos datos **no se puede saber si la secuencia de emails funcionó**.

Sí se observa una mejora coincidente con marzo:

- MRR: de **$4.100 a $5.300** (+$1.200; +29%).
- Altas de pago: de **9 a 14** (+5; +56%).

Pero no es posible atribuir ese cambio a los emails porque, casi al mismo tiempo, ocurrieron dos intervenciones relevantes:

- Publicidad pagada desde el 3 de marzo ($400).
- Mención de un creador grande el 12 de marzo.

Además, el MRR no depende solo de nuevas altas: puede variar por cancelaciones, upgrades/downgrades, descuentos, recuperaciones de pagos fallidos o cambios de precio. Por tanto, el +29% de MRR no demuestra por sí mismo que los emails generaron conversiones.

## Qué haría falta para estar seguros

La forma más fiable sería un **experimento con grupo de control**:

1. Dividir aleatoriamente a los usuarios gratuitos en dos grupos comparables:
   - **Tratamiento:** recibe la secuencia de 5 emails.
   - **Control:** no recibe la secuencia, o recibe la comunicación habitual.
2. Mantener ambos grupos expuestos al resto de condiciones por igual: misma publicidad, mismo producto y mismo periodo.
3. Medir durante una ventana definida, por ejemplo 30 días:
   - Conversión de gratuito a pago.
   - MRR generado por usuario.
   - Tiempo hasta conversión.
   - Bajas tempranas o reembolsos, para verificar la calidad de las conversiones.
4. Comparar tasas de conversión y estimar si la diferencia es estadísticamente compatible con un efecto real, no con azar.

## Datos útiles mientras no exista experimento

Para una evaluación orientativa —pero todavía no causal— ayudaría tener:

- Número de usuarios gratuitos que entraron en la secuencia.
- Entregabilidad, aperturas, clics y bajas de cada email.
- Cuántas conversiones ocurrieron después de cada email y en qué plazo.
- Fuente de adquisición o atribución de cada alta: anuncio, creador, orgánico, email, directo, etc.
- Evolución diaria o semanal de altas, especialmente antes y después del 12 de marzo.
- Churn, upgrades, downgrades y recuperaciones de pago durante marzo.
- Datos de varios meses anteriores para saber si pasar de 9 a 14 altas está fuera de la variación normal.

En resumen: **marzo fue mejor que febrero, pero no sabemos qué parte —si alguna— corresponde a la secuencia de emails**. La publicidad, la mención del creador y posibles cambios normales en el negocio son explicaciones alternativas plausibles.