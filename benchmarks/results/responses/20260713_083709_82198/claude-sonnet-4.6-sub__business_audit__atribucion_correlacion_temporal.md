# Claude Sonnet 4.6 (suscripción) — business_audit/atribucion_correlacion_temporal

- model_id: `claude-sonnet-4-6`
- success: True  | final: 4.53 | quality: 4.8
- latency_total: 33.545s | tokens_per_second: 33.7
- input_tokens: 3 | output_tokens: 1131

## Respuesta completa

## Conclusión directa: no se puede saber si fue la secuencia.

Lo que sí se puede decir: en marzo algo funcionó. Pero tienes tres intervenciones simultáneas y cero forma de separar su efecto.

---

### El problema de atribución

| Intervención | Fecha | Población que impacta |
|---|---|---|
| Secuencia de emails | 1 marzo | Usuarios gratuitos ya existentes |
| Publicidad pagada | 3 marzo | Personas nuevas que aún no te conocían |
| Mención del creador | 12 marzo | Audiencia externa del creador |

Las tres ocurrieron en el mismo mes. El +$1.200 de MRR y las 5 altas adicionales podrían venir de cualquiera de las tres, de dos de ellas, o del efecto combinado. No hay forma de saberlo con lo que tienes.

La mención del creador el 12 de marzo es particularmente sospechosa: ese tipo de evento típicamente genera un pico corto y pronunciado de conversiones. Si la mayoría de las 14 altas llegaron después del 12, la secuencia de emails probablemente tuvo poco que ver.

---

### Qué haría falta para atribuir correctamente

**Mínimo indispensable:**

1. **Fecha exacta de cada alta.** ¿Las 14 conversiones se distribuyeron durante todo marzo o se concentraron después del 12? Si hay un pico post-12 de marzo, el creador explica la mayor parte.

2. **Origen de cada conversión.** ¿Esas personas eran usuarios gratuitos previos (candidatos a ser afectados por el email) o eran personas nuevas que entraron ese mes por ads o por la mención?

3. **Métricas de la secuencia.** Tasa de apertura, clics, y sobre todo: ¿alguno de los 14 que convirtió hizo clic en un email antes de pagar? Sin este dato, el email es una caja negra.

**Para el futuro:**

- Lanzar una sola intervención a la vez, o
- Si no es posible, usar un grupo de control (una fracción de usuarios gratuitos sin secuencia) para tener una línea base.

---

### Lo que sí puedes decir con honestidad

> "En marzo el MRR creció un 29% con tres cambios simultáneos. No tenemos atribución limpia. La secuencia puede haber contribuido, pero no tenemos evidencia de que fue el driver principal."

Eso no es un fracaso analítico. Es exactamente el diagnóstico correcto antes de decidir si invertir más en la secuencia o en otro canal.