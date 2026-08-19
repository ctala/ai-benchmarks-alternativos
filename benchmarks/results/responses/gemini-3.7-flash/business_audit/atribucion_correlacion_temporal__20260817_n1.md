# Gemini 3.7 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 7.53 | quality: 8.0
- latency_total: 5.977s | tokens_per_second: 205.3
- input_tokens: 223 | output_tokens: 1227

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

**Conclusión directa: Con estos datos, no se puede saber.** 

Cualquiera que te diga que la secuencia fue un éxito (o un fracaso) basándose en estos números te está vendiendo una ilusión. 

El negocio creció en marzo, pero **no podemos atribuirle ese crecimiento a los emails**.

---

### ¿Por qué no lo sabemos? (Los 3 problemas)

1. **Variables cruzadas (Contaminación de causas):**
   En un lapso de 12 días activaste tres palancas distintas:
   * 1 de marzo: Secuencia de emails.
   * 3 de marzo: Publicidad de pago ($400).
   * 12 de marzo: Mención orgánica de un creador grande.
   Cualquiera de estas tres cosas (o una combinación de ellas) pudo haber generado las 5 conversiones extra de marzo.

2. **Muestra muy pequeña:**
   Pasar de 9 a 14 conversiones son **solo 5 clientes más**. En números tan bajos, la variación mensual puede ser puro ruido estadístico, un par de personas que llegaron por el video del creador y una por los anuncios.

3. **Métricas agregadas vs. Métricas de embudo:**
   El MRR y las altas totales son métricas de resultado final del negocio, no métricas de rendimiento de email marketing.

---

### ¿Qué hace falta para saberlo con certeza?

Para medir el impacto real de la secuencia necesitas bajar al nivel de atribución y comportamiento:

1. **Atribución directa (Tracking):**
   * ¿Los enlaces de la secuencia tenían UTMs o parámetros de seguimiento únicos?
   * De las 14 personas que pagaron en marzo: ¿cuántas hicieron clic en un enlace de esos emails antes de pagar? (Si 0 hicieron clic, la secuencia no aportó esas ventas; si fueron 10, el panorama cambia).

2. **Métricas del embudo de email:**
   * Tasa de apertura y clics de cada uno de los 5 correos.
   * Cuántos usuarios del plan gratuito entraron a la secuencia y qué porcentaje convirtió a pago versus el porcentaje histórico de conversión de ese segmento.

3. **Grupo de control (La prueba definitiva para el futuro):**
   * Deja a un porcentaje de usuarios gratuitos (por ejemplo, el 20% o 50%) **sin recibir la secuencia** (grupo de control) y envía la secuencia al resto. Si el grupo que recibe los correos convierte a una tasa significativamente mayor que el que no los recibe en el mismo período de tiempo, entonces sí tienes prueba causal de que la secuencia funciona.