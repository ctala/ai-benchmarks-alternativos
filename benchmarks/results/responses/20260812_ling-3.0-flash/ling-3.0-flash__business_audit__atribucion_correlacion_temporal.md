# Ling 3.0 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.55 | quality: 10.0
- latency_total: 4.673s | tokens_per_second: 331.3
- input_tokens: 286 | output_tokens: 1548
- judge_score: 5.0 | justificación: 

## Respuesta completa

## Conclusión: **No se puede saber si la secuencia de emails funcionó.**

Los datos que me pasas muestran una correlación temporal entre el lanzamiento de la secuencia y el aumento de altas, pero la correlación no es causalidad, y aquí hay razones para no dar por sentado que los emails fueron la causa.

---

### El problema fundamental: tres cambios simultáneos

| Cambio | Fecha | Efecto potencial |
|---|---|---|
| Secuencia de 5 emails | 1 de marzo | Conversión de gratis → pago |
| Publicidad pagada ($400) | 3 de marzo | Tráfico + conversiones nuevas |
| Mención de un creador | 12 de marzo | Tráfico viral + conversiones |

Las 5 altas adicionales de marzo (de 9 a 14) podrían deberse a **cualquiera de los tres**, a una combinación, o a ninguna. No hay forma de aislar el efecto de la secuencia de emails con la información disponible.

### Lo que los datos NO nos dicen

- **¿Cuántos usuarios del plan gratuito recibieron los emails?** Sin la base de envío, no podemos calcular una tasa de conversión real.
- **¿Cómo interactuaron con la secuencia?** No tenemos tasas de apertura, clics ni conversiones dentro del funnel de email.
- **¿De dónde vinieron las 14 altas?** No sabemos si fueron usuarios nuevos (captados por publicidad o el video) o upgrades de usuarios gratuitos existentes (que podrían haber sido influidos por los emails).
- **¿El MRR subió solo por volumen?** 5 altas más podrían explicar parte del aumento, pero no sabemos el valor promedio de esas altas ni si son de usuarios nuevos o existentes.

---

### Qué haría falta para estar seguros

1. **Grupo de control (A/B test):** Una muestra aleatoria de usuarios gratuitos que **no** recibiera la secuencia. Si las altas en el grupo de control se mantienen igual y suben solo en el grupo que recibió emails, ahí sí tendrías evidencia.

2. **Funnel del email:** Tasa de apertura → clic en el email → visita a la página de conversión → alta real. Eso te diría si el email tuvo impacto en el comportamiento del usuario.

3. **Atribución por canal:** Sistema para saber si cada alta vino de email, publicidad, referido del creador, tráfico orgánico, etc.

4. **Datos de cohortes:** Separar las altas de marzo en subgrupos (ej. altas de la primera quincena vs. segunda quincena, ya que la mención del creador fue el día 12).

---

### Lo que haría yo ahora

No descartaría la secuencia de emails — es una hipótesis razonable — pero **tampoco la celebraría como la ganadora** de ese aumento. Lo más honesto es decirle al equipo: *"Los números son compatibles con que funcionó, pero no podemos descartar que la publicidad o el video del creador expliquen todo o parte del aumento."*

Y la siguiente pregunta no debería ser "¿funcionó?", sino **"¿cómo diseñamos un test para averiguarlo?"**