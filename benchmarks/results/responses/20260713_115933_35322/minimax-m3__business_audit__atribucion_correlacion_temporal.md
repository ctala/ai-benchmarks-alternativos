# MiniMax M3 — business_audit/atribucion_correlacion_temporal

- model_id: `minimax/minimax-m3`
- success: True  | final: 5.95 | quality: 6.0
- latency_total: 24.604s | tokens_per_second: 59.1
- input_tokens: 373 | output_tokens: 1454

## Respuesta completa

# Conclusión corta: **no se puede saber si la secuencia funcionó con estos datos.**

Los números muestran crecimiento, sí. Pero "crecimiento en marzo" no es lo mismo que "la secuencia de emails causó ese crecimiento". Son tres cosas distintas y los datos que me pasaste no las separan.

---

## Por qué no podemos atribuirlo

Tenés tres intervenciones simultáneas en marzo:

| Fecha | Intervención | Tipo |
|-------|-------------|------|
| 1 marzo | Secuencia de 5 emails | Tuyo, testeable |
| 3 marzo | Publicidad paga ($400) | Canal nuevo, cuantificable |
| 12 marzo | Mention de creador grande | Viral, difícil de aislar |

Cualquiera de las tres —o las tres juntas— explican las 5 conversiones extra y el +29% de MRR. **No hay forma de repartir ese crédito con la información que me diste.**

Sumemos a esto:

- **No sé cuántos usuarios free recibieron la secuencia.** Si la base free es 50 o 5.000, la tasa de conversión cambia radicalmente.
- **No sé de dónde vinieron los 14 pagos.** ¿Eran usuarios free que convirtieron gracias al email? ¿O fueron personas nuevas que llegaron por el video del creador y compraron directo? Si fue esto último, los emails no tuvieron nada que ver.
- **9 vs 14 es un número chico.** Con estos volúmenes, la diferencia podría ser ruido estadístico. No sé la varianza histórica de tus meses anteriores.
- **El mention del 12 de marzo es sospechoso.** Un creador grande en la segunda mitad del mes puede traccionar 5+ signups por sí solo.

---

## Qué haría falta para estar seguros

Hay tres niveles de evidencia, de menor a mayor:

### 1. Trazabilidad mínima (atribución directa)
- Asigná **UTMs únicos** a los links de los emails (ej: `?utm_source=email_seq&utm_campaign=marzo`).
- Rastreá en tu sistema de pagos qué conversiones tienen ese UTM.
- Resultado: sabés exactamente cuántos de los 14 vinieron *por el email*.

### 2. Grupo de control (lo mínimo riguroso)
- No le mandes la secuencia al 10–20% de los free users.
- Compará tasa de conversión entre los que recibieron y los que no.
- Si el grupo que recibió convierte significativamente más → la secuencia funciona.
- Si convierten parecido → los emails no mueven la aguja.

### 3. Análisis contrafactual (lo más limpio)
- Compará la conversión de usuarios free en los **3–4 meses previos**, cuando solo tenías marketing orgánico.
- Si marzo está claramente por encima de esa baseline (descontando el efecto conocido de ads), la señal es más creíble.

---

## Lo que yo haría si fuera vos

Mañana mismo:

1. **A/B test rápido**: partí la base free 50/50, mitad recibe la secuencia, mitad no. Dos semanas y tenés respuesta.
2. **UTMs ya** en los próximos envíos para tener atribución de aquí en adelante.
3. **Preguntá en el checkout o en una encuesta de 1 pregunta**: "¿Cómo nos conociste?" — feo pero informativo cuando los volúmenes son chicos.

---

## Una última cosa honesta

"Mejora del 29% en MRR" suena lindo para un reporte. Pero reportar eso sin atribución causal es exactamente el tipo de conclusión cómoda que después te hace gastar presupuesto en cosas que no funcionan. Si el video del creador fue el verdadero motor, lo que necesitás es **buscar más creators**, no optimizar emails. Y con los datos actuales, no podés saber cuál de las dos cosas es.