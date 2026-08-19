# MiniMax M2.7 (directo) — business_audit/atribucion_correlacion_temporal

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 21.945s | tokens_per_second: 43.8
- input_tokens: 217 | output_tokens: 961

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

# Respuesta corta: No se puede saber

Los números suben, sí. Pero eso no te dice qué los hizo subir.

---

## Por qué no puedo atribuírselo a los emails

Tenés **tres intervenciones simultáneas**:

| Fecha | Intervención |
|-------|-------------|
| 1 marzo | Secuencia de emails |
| 3 marzo | Publicidad pagada ($400) |
| 12 marzo | Mención de creador con audiencia |

El alza de 9 → 14 altas y el MRR de $4.100 → $5.300 pueden explicarse por **cualquiera** de las tres, por las tres juntas, o por algo totalmente distinto (estacionalidad, viralidad orgánica, etc.).

Asumir que fueron los emails sería una **falacia post hoc**: "pasó después, luego fue por causa de".

---

## Qué necesitarías para estar seguro

### Necesario (para afirmación causal)
- **Grupo de control**: usuarios del plan gratuito que **no** reciban los emails pero sí estén expuestos a la pub y la mención. Así aislás el efecto real.
- **Test A/B** retrospectivo por cohorte: ¿los que abrieron los emails convirtieron más que los que no?

### Muy útil (aunque no concluyente por sí solo)
- **Tasa de apertura y click** de la secuencia → ¿llegaron realmente?
- **Distribución temporal de las 14 altas** → ¿subieron antes o después del 12 de marzo (mención del creador)? Eso te da una pista fuerte.
- **Altas atribuibles a pub** → si pagaste $400, ¿cuántas conversiones atribuís a eso? (aunque sea una estimación).

---

## Mi recomendación concreta

1. **Separar el efecto del creator**: si las 14 altas se concentraron alrededor del 12-15 de marzo, los emails probablemente no son la causa principal.
2. **Analizar por cohorte**: сравненить la tasa de conversión de usuarios que entraron en marzo vs. los que estaban en免费 desde antes (y recibieron los emails).
3. **Si no tenés control**: asume que las tres cosas funcionaron y atribuite el mérito solo cuando puedas medirlo.

---

## Nota final

Es tentador querer concluír que funcionó, porque te costaron tiempo y esfuerzo esos 5 emails. Pero el análisis honesto es: **el MRR subió, pero no tenemos evidencia de cuál de las tres intervenciones lo produjo**. Eso no es un fracaso — es información. La próxima vez, planificá el test antes de lanzar.