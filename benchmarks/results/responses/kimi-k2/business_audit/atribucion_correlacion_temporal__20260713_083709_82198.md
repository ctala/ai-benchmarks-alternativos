# Kimi K2 — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 4.19 | quality: 3.34
- latency_total: 18.512s | tokens_per_second: 31.5
- input_tokens: 271 | output_tokens: 584

## Respuesta completa

## Conclusión: No se puede saber

El crecimiento de marzo es **real**, pero **no atribuible** a la secuencia de emails con los datos que tienes.

---

## Por qué no podemos aislar el efecto

| Factor | Cuándo empezó | Qué pudo impulsar |
|--------|-------------|-------------------|
| **Secuencia de emails** | 1 de marzo | Conversiones de gratuitos a pagos |
| **Publicidad pagada** | 3 de marzo | Nuevos usuarios (gratuitos y pagos) |
| **Mención del creador** | 12 de marzo | Probablemente el impacto más grande |

**Problema crítico:** No sabes de dónde vinieron las 14 altas de marzo. ¿Cuántas fueron:
- Usuarios gratuitos previos que recibieron los emails?
- Nuevos usuarios que llegaron por publicidad?
- Nuevos usuarios que llegaron por la mención (y posiblemente se pagaron directo)?

---

## Lo que **sí** podemos decir

- El MRR creció $1.200
- Hubo 5 altas más que en febrero
- **Pero** la mención del creador sola explica fácilmente ese delta (y más)

---

## Qué haría falta para estar seguros

| Dato | Para qué sirve |
|------|---------------|
| **Atribución de origen de cada alta** | Saber cuántos venían de tráfico orgánico previo vs. nuevos canales |
| **Tasa de conversión de la lista gratuita** | Comparar marzo vs. meses anteriores sin emails |
| **Fecha de alta de cada usuario** | Si muchas fueron post-12 de marzo, la mención es el factor dominante |
| **Gasto en publicidad desagregado por día** | Para ver si el retorno justifica el coste |
| **Emails abiertos/clicados y conversión posterior** | El funnel real de la secuencia |

---

## Hipótesis alternativa que no puedo descartar

La mención del creador pudo haber **amplificado** la efectividad de los emails (más gente conoció la comunidad, luego los emails cerraron), pero también pudo haber **eclipsado** por completo cualquier efecto marginal de la secuencia.

Sin datos de atribución, elegir una explicación es preferencia, no análisis.