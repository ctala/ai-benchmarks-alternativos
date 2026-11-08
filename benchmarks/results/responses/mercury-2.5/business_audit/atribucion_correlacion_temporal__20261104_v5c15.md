# Mercury 2.5 — business_audit/atribucion_correlacion_temporal

- model_id: `inception/mercury-2.5`
- success: True  | final: 9.39 | quality: 10.0
- latency_total: 6.467s | tokens_per_second: 220.2
- input_tokens: 245 | output_tokens: 1424

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



Con los datos actuales, **no se puede saber** con certeza si la secuencia de emails fue la causante del crecimiento.

Aunque hubo una mejora en las métricas clave durante marzo (MRR +29%, altas de 9 a 14), existen variables de confusión significativas que impiden aislar el efecto de los emails:

1.  **Publicidad pagada:** Iniciaste el 3 de marzo. Esto suele generar tráfico directo y conversiones rápidas.
2.  **Mención de creador:** El impacto del video del 12 de marzo pudo haber traído la mayoría de los nuevos usuarios.

Sin datos de atribución, es imposible distinguir si las 14 altas nuevas provienen de usuarios gratuitos que recibieron la secuencia o de nuevas visitas por los otros canales.

**Para estar seguros, haría falta:**
*   **Segmentación:** Comparar la conversión de usuarios que abrieron los emails frente a los que no.
*   **Grupo de control:** Habilitar la secuencia solo para un subconjunto de usuarios y medir la diferencia.
*   **Atribución directa:** Preguntar a los nuevos pagadores "¿Cómo te enteraste de nosotros?" en el onboarding.

Hasta tener esos datos, atribuir el crecimiento solo a los emails es una suposición, no un hecho.