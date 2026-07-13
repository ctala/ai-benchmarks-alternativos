# MiniMax M2.7 — business_audit/atribucion_correlacion_temporal

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 5.02 | quality: 4.8
- latency_total: 35.691s | tokens_per_second: 30.8
- input_tokens: 217 | output_tokens: 1099

## Respuesta completa

## Mi conclusión: No se puede saber

Y no lo digo como evasiva —los números son tentadores, pero el diseño del experimento no permite atribuir causality.

### Lo que sí muestran los datos

| Métrica | Febrero | Marzo | Cambio |
|---------|---------|-------|--------|
| MRR | $4,100 | $5,300 | +$1,200 |
| Altas pagas | 9 | 14 | +5 |

Son buenos números. Pero:

**La suba de MRR ($1,200) no coincide exactamente con 5 nuevas altas.** Si el plan es de ~$85-100/mes, esas 5 altas explican ~$425-500 del crecimiento. El resto ($700-775) podría venir de upgrades, reducción de churn, o reactivaciones — datos que no tienes. No hay forma de saber cuánto vino de cada fuente.

### Por qué no se puede separar el efecto de los emails

Tienes **tres intervenciones simultáneas**:

1. **Secuencia de emails** (lanzada 1 de marzo)
2. **Publicidad paga** ($400 en marzo)
3. **Mención de creador** (12 de marzo)

Cualquiera de las tres, o una combinación, podría explicar las nuevas altas. El timing complica más las cosas: la mención del creador ocurrió el día 12, muy cerca del punto medio del mes.

---

### Qué harían falta para estar seguros

**Mínimo viable:**

- **Fecha de conversión de cada usuario nuevo.** Si las 14 altas de marzo ocurrieron masivamente entre el 5-10 de marzo (inmediatamente después de los emails), hay correlación. Si se concentraron después del 12 (después de la mención del creador), los emails no fueron.
- **Segmento de la secuencia.** ¿Cuántos usuarios gratuitos recibían los emails? ¿Cuántos de los 14 estaban en esa lista?
- **Un grupo de control.** Por ejemplo: 500 usuarios en secuencia, 500 sin ella. Mismo período, misma base. Sin esto, cualquier atribución es conjetura.

**Más robusto:**

- Métricas de los emails: tasa de apertura, clicks, descarte/no entregado
- A/B testeo real: a la mitad le mandás la secuencia, a la otra no, y medís conversión real
- Attribution model: definir cómo rastreas de dónde vino cada usuario nuevo (email, publicidad, mención, otro)

---

### Lo que sí puedo decirte

Si los emails tuvieron una tasa de apertura decente y hubo engagement (clicks), **es razonable pensar que contributed**, pero "contribuyó" no es lo mismo que "funcionó". Los otros factores podrían haber hecho el trabajo pesado.

Si los emails estaban pobremente escritos, con mal timing o dirigidos a usuarios con baja intención de pago, pudieron haber sido ruido de fondo y las otras dos palancas se llevaron todo el mérito.

**Mi recomendación concreta:** Pide a tu herramienta de email marketing los datos de engagement y la fecha de conversión de los 14 usuarios nuevos. Con eso ya podés tener una respuesta más honesta.