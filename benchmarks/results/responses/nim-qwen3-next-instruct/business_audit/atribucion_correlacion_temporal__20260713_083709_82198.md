# Qwen 3-Next 80B Instruct (NIM) — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3-next-80b-a3b-instruct`
- success: True  | final: 4.46 | quality: 3.6
- latency_total: 9.447s | tokens_per_second: 97.4
- input_tokens: 253 | output_tokens: 920

## Respuesta completa

**Conclusión: No se puede saber si la secuencia de emails funcionó.**

---

### ¿Por qué?

Tienes **tres intervenciones simultáneas** que podrían haber impulsado el crecimiento del MRR y las altas:

1. **La secuencia de emails automáticos** (iniciada el 1 de marzo, dirigida a usuarios gratuitos).
2. **Publicidad pagada** (iniciada el 3 de marzo, $400 totales en el mes).
3. **Mención de un creador con audiencia grande** (el 12 de marzo).

Todas estas acciones ocurren en un período muy cercano, y **no hay datos de atribución** que permitan separar su impacto individual.

---

### Lo que sí sabes:
- El MRR subió un **29%** ($4.100 → $5.300).
- Las altas al plan pago aumentaron de **9 en febrero a 14 en marzo** (+55%).
- Eso sugiere que algo funcionó bien en marzo.

---

### Lo que **no sabes** (y necesitas para estar seguros):

| Pregunta | ¿Por qué importa? |
|--------|------------------|
| **¿Cuántos usuarios gratuitos recibieron la secuencia de emails?** | Si son 50 o 5.000, el impacto potencial es radicalmente distinto. |
| **¿Cuál fue la tasa de conversión de la secuencia de emails?** | ¿Cuántos de quienes recibieron los emails se convirtieron? Sin esto, es un black box. |
| **¿Hubo un aumento en el tráfico orgánico o desde redes sociales justo después del video del creador?** | Si el video generó 10.000 visitas, es probable que ahí vino la mayor parte de las altas. |
| **¿Hubo caídas en la tasa de cancelación?** | ¿El crecimiento fue por más altas, o por menos bajas? |
| **¿Qué porcentaje de las 14 altas de marzo se puede rastrear hasta los emails?** | Si usas UTM, códigos de seguimiento o segmentación en tu CRM, podrías saberlo. |
| **¿Hubo algún cambio en el precio, la página de conversión o la oferta del plan pago en marzo?** | Un cambio en la landing page podría explicar todo. |

---

### ¿Qué deberías hacer para saber si los emails funcionaron?

1. **Implementa seguimiento de fuentes de conversión** (UTM, códigos únicos por canal).
2. **Segmenta los usuarios**: compara la tasa de conversión de quienes recibieron los emails vs. quienes no los recibieron (o los recibieron pero no abrieron).
3. **Haz un experimento A/B**: en el próximo ciclo, envía los emails solo a un 50% de los gratuitos y deja el otro 50% como control. Mide la diferencia.
4. **Analiza el funnel**: ¿cuántos abrieron el primer email? ¿cuántos hicieron clic? ¿cuántos compraron después del email 3?

---

### Bonus: ¿Qué parece más probable que haya movido la aguja?

- La **mención del creador** (el 12/3) tiene un potencial de impacto masivo y de alta credibilidad — probablemente generó un pico de tráfico y conversiones.
- La **publicidad** también puede haber tenido un efecto significativo, especialmente si llegó a audiencias segmentadas.
- Los emails podrían haber tenido un efecto más lento y sostenido, pero **sin datos de atribución, no hay forma de medirlo**.

---

### En resumen:

> **El crecimiento es real. Pero no puedes atribuirlo a los emails.**  
> Decir que “los emails funcionaron” es una conclusión cómoda, pero falsa.  
> **No se puede saber.**  
>  
> Haz el seguimiento en el próximo ciclo, y entonces podrás decirlo con confianza.