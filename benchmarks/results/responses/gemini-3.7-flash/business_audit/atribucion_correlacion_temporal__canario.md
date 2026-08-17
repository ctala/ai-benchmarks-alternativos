# Gemini 3.7 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 13.591s | tokens_per_second: 93.5
- input_tokens: 221 | output_tokens: 1271

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

**Conclusión:** 

**No se puede saber.** Asignarle el mérito del crecimiento a la secuencia de emails con estos datos sería engañarnos. 

El aumento en el negocio es real (+29% MRR, +5 altas), pero es imposible aislar el impacto de los emails debido a tres problemas graves de atribución y datos:

1. **Contaminación por múltiples variables simultáneas:** En un periodo de 12 días activaste emails, prendiste pauta publicitaria ($400) y recibiste tráfico orgánico de un creador grande. El pico de conversiones pudo haber venido 100% del influencer, 100% de los anuncios, 100% de los emails o de una mezcla aleatoria.
2. **Tamaño de muestra diminuto:** La diferencia entre febrero y marzo son **5 conversiones**. Con números tan bajos, la simple varianza aleatoria (suerte o estacionalidad) puede explicar el cambio sin que ninguna de las acciones haya tenido un efecto real.
3. **Efecto calendario:** Marzo tiene 31 días y febrero 28 (un 10.7% más de tiempo para convertir).

---

### ¿Qué haría falta para estar seguros?

Para poder afirmar que la secuencia funciona (y no tomar decisiones a ciegas), necesitaríamos:

1. **Tracking y Atribución directa (lo mínimo indispensable):**
   * Parámetros UTM específicos en cada enlace dentro de los 5 emails.
   * Registro de cuántas de las 14 conversiones hicieron clic en esos enlaces antes de pagar (para saber si el email fue el punto de contacto decisivo o si la gente convirtió directo desde la web tras ver el video del creador).

2. **Un Grupo de Control (Test A/B):**
   * Dividir a los usuarios gratuitos que entran: 50% recibe la secuencia y el otro 50% no recibe nada (o recibe la comunicación anterior).
   * Si la tasa de conversión (%) del grupo con secuencia es significativamente mayor a la del grupo de control, recién ahí podemos atribuir causalidad.

3. **Métricas intermedias del embudo:**
   * Tasa de apertura y clics (CTR) de cada uno de los 5 correos.
   * Saber en qué email específico se generan las bajas o las conversiones.

4. **Análisis de Cohortes:**
   * Separar a los usuarios: ¿cuántos de los que pagaron en marzo eran usuarios gratuitos viejos (impactados por los emails) vs. usuarios nuevos que llegaron en marzo por la pauta o el influencer?

**Recomendación analítica:** Revisa en tu pasarela de pagos o CRM el ID de los 14 usuarios que convirtieron en marzo y cruza la fecha de su registro inicial con la fecha de compra. Si la mayoría se registró después del 12 de marzo, el mérito fue del creador, no de tu secuencia.