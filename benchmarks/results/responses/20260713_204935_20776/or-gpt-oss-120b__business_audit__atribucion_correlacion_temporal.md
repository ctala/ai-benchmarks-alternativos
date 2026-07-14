# GPT-OSS 120B — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 28.711s | tokens_per_second: 41.3
- input_tokens: 285 | output_tokens: 1186
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y pasos concretos para evaluar la efectividad de la secuencia de correos electrónicos.

## Respuesta completa

**Conclusión provisional:**  
Con la información que has compartido **no se puede afirmar con certeza que la secuencia de 5 emails sea la causa del aumento de ingresos y de las altas en marzo**.  

Los datos que tienes (crecimiento del MRR y número de altas) coinciden temporalmente con el lanzamiento de la secuencia, pero también coinciden con **dos otras intervenciones que podrían haber influido:**

1. **Gasto en publicidad (US$ 400 en marzo).**  
2. **Mención de la comunidad por un creador con gran audiencia (video publicado el 12 de marzo).**

Sin un análisis que des‑confunda estos efectos simultáneos, no podemos atribuir el impulso exclusivamente a la automatización de correos.

---

## Qué datos y análisis necesitas para aislar el efecto de la secuencia de emails

| Tipo de dato | Por qué es necesario | Cómo obtenerlo / cómo medirlo |
|--------------|---------------------|------------------------------|
| **Eventos de envío y apertura de los emails** | Saber cuántos usuarios recibieron cada mensaje, cuántos lo abrieron y cuántos hicieron clic en los enlaces (p.ej. link a la página de precios). | Exportar los logs de la herramienta de email marketing (Open Rate, Click‑Through Rate, fechas/hora de envío). |
| **Conversiones atribuibles a cada email** | Relacionar una alta específica a un email concreto (p.ej. “el tercer email generó 5 suscripciones”). | Implementar *UTM parameters* o enlaces de seguimiento únicos por email, y luego cruzar con la base de datos de pagos. |
| **Control de exposición a publicidad** | Determinar cuántos de los usuarios que se convirtieron vieron la campaña de ads. | Taggear los usuarios que llegaron a través de los anuncios (p.ej. píxel de Facebook/Google, URL con UTM). |
| **Control de exposición a la mención del creador** | Saber cuántos nuevos usuarios provienen del video. | Analítica del tráfico de referencia (referrer = YouTube/TikTok/etc.) y/o códigos de descuento exclusivos del creador. |
| **Segmentación de usuarios** | Comparar grupos que recibieron la secuencia vs. grupos que no la recibieron (p.ej. usuarios que se suscribieron al plan gratuito después del 1 marzo vs. antes). | Crear un “cohort analysis” (cohortes por fecha de ingreso al plan gratuito) y comparar conversion rates. |
| **Historial de tendencias previas** | Establecer una línea base (seasonality, crecimiento orgánico) para ver si el salto de +29 % es fuera de lo esperado. | MRR y número de altas de los últimos 3‑6 meses, con sus respectivas variaciones mensuales. |
| **Variables externas** | Otros factores (p.ej. cambios en precios, mejoras de producto, eventos de la industria) que puedan haber influido. | Registro de cualquier cambio de producto, precios, o eventos relevantes en el mismo periodo. |
| **Test A/B o grupo de control** | La forma más robusta de atribuir causalidad. | Lanzar la secuencia a un subconjunto aleatorio de usuarios gratuitos y comparar su tasa de conversión con la de un grupo que no la reciba. |

### Pasos concretos para un análisis rápido (mínimo viable)

1. **Recolecta los datos de apertura y clics** de cada uno de los 5 emails.  
2. **Vincula los clics a conversiones** mediante los códigos UTM o IDs de usuario.  
3. **Construye una tabla** con:  
   - Usuario ID  
   - Fecha de ingreso al plan gratuito  
   - Emails recibidos / abiertos / clics (sí/no)  
   - Fuente de adquisición (ads, video del creador, orgánico, email)  
   - Fecha de conversión a pago (si ocurre)  
4. **Calcula tasas de conversión** por fuente y por exposición a la secuencia.  
5. **Compara con una cohorte previa** (p.ej. usuarios gratuitos que entraron en enero‑febrero y no recibieron la secuencia).  
6. **Realiza un test de hipótesis** (por ejemplo, chi‑square o test de proporciones) para ver si la diferencia en tasas es estadísticamente significativa.  

Si después de este análisis la tasa de conversión de los usuarios que interactuaron con los emails es significativamente mayor que la de los que no lo hicieron (y mayor que la que proviene de ads o del video), entonces podrás afirmar con mayor confianza que la secuencia de emails tuvo un efecto positivo.

---

## Resumen

- **No podemos afirmar que la secuencia de emails funcionó** con los datos actuales, porque hay al menos dos variables de confusión (publicidad pagada y mención del creador) y falta información de comportamiento dentro de los emails.
- **Para estar seguros** necesitas datos de apertura/clics, tracking de conversiones por canal, cohortes de control y, idealmente, un experimento A/B o un grupo de control que no reciba la secuencia.
- Con esos datos podrás aislar el impacto de la secuencia y cuantificar su ROI real.  

Si quieres que te ayude a diseñar el esquema de tracking o a montar el análisis una vez que tengas los datos, avísame y lo armamos paso a paso.