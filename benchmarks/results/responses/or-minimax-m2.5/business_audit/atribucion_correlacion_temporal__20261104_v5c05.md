# MiniMax M2.5 — business_audit/atribucion_correlacion_temporal

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 12.265s | tokens_per_second: 65.6
- input_tokens: 219 | output_tokens: 805

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

## Mi conclusión: no se puede saber

Los datos muestran que marzo fue mejor que febrero en conversiones (+5 altas) y MRR (+$1.200), pero hay un problema fundamental: **lanzaste tres cosas a la vez**.

### Por qué no podemos atribuir el resultado a los emails

| Intervención | Fecha de inicio | Posible impacto |
|--------------|-----------------|-----------------|
| Secuencia de emails | 1 de marzo | ¿Conversión de usuarios gratuitos? |
| Publicidad ($400) | 3 de marzo | ¿Nuevos usuarios que convirtieron? |
| Mención influencer | 12 de marzo | ¿Tráfico de alta calidad? |

Cualquiera de las tres (o las tres combinadas) podría explicar las 5 altas adicionales. No hay forma de distinguir cuál fue la causa.

### Lo que faltaría para saberlo

1. **Un grupo de control**: usuarios gratuitos que NO reciban los emails, para comparar tasas de conversión.

2. **Fuente de las altas**: ¿esas 14 personas vienen de usuarios gratuitos que ya estaban antes del 1 de marzo, o son usuarios nuevos que llegaron por publicidad/influencer?

3. **Datos del funnel**: cuántos usuarios recibieron cada email, cuántos abrieron cada uno, y cuándo convirtieron exactamente.

4. **Churn**: ¿cuántos clientes pagaron se fueron en marzo? El MRR subió $1.200, pero no sé si es neto o si hubo pérdidas.

### Qué haría yo ahora

Si querés seguir experimentando, la forma más limpia sería:

- Pausar la secuencia de emails una semana y ver si bajan las conversiones
- O crear un test A/B con un segmento pequeño de usuarios gratuitos que NO reciba los emails

¿Tenés acceso a analytics donde puedas ver de dónde vinieron las 14 altas de marzo?