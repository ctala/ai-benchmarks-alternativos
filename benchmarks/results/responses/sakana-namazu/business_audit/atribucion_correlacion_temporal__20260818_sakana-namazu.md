# Sakana Namazu — business_audit/atribucion_correlacion_temporal

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 8.994s | tokens_per_second: 227.7
- input_tokens: 270 | output_tokens: 2048

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

**Conclusión: No se puede saber.**  

Con los datos que tienes, no hay forma de atribuir el aumento de altas o de MRR a la secuencia de emails. La tentación de decir “subió el MRR 29% y crecieron las altas, así que funcionó” es exactamente el tipo de trampa en la que un analista no debe caer.

### Por qué los datos no lo sostienen

1. **Tres intervenciones al mismo tiempo**: en marzo ejecutaste tres tácticas distintas (emails automáticos, publicidad pagada y una mención grande de un creador). Los números que muestras son el resultado neto de todo junto, no el efecto aislado de cada uno.
2. **No sabes de dónde vinieron las 14 altas**: ¿fueron usuarios gratuitos existentes que recibieron los emails? ¿gente nueva que llegó por el anuncio y pagó al instante? ¿seguidores del creador que entraron por el video? Sin atribución de fuente en la alta, es imposible saber qué canal generó qué.
3. **Falta de grupo de control**: para saber si los emails funcionan, necesitas comparar una cohorte que los recibió contra otra que no (todo lo demás constante). Sin eso, no sabes si esos usuarios habrían convertido igual por inercia orgánica.
4. **Muestra muy pequeña**: pasar de 9 a 14 altas es solo 5 conversiones más. En muestras tan pequeñas, una sola mención grande o un par de anuncios bien orientados pueden explicar toda la diferencia.
5. **Confusión entre “altas totales” y “conversión de gratis a pago”**: tu secuencia de emails apuntaba a usuarios del plan gratuito. Si las 14 altas incluyen gente nueva que nunca estuvo en el plan gratuito, estarías midiendo crecimiento total en lugar del objetivo real de la campaña.

---

### Qué haría falta para estar seguros

Para poder decir, con rigor, que la secuencia de emails funcionó (y cuánto), necesitarías:

**1. Atribución clara en el momento de la alta**
- En el checkout o formulario de pago, preguntar o trackear cómo llegó el usuario (email, anuncio, referido del creador, orgánico, etc.).

**2. Un grupo de control (test A/B)**
- Dividir a los usuarios gratuitos en dos grupos: 
  - Grupo A: recibe la secuencia de 5 emails.
  - Grupo B: no la recibe (o recibe un solo email genérico).
- Medir la tasa de conversión a pago de ambos grupos