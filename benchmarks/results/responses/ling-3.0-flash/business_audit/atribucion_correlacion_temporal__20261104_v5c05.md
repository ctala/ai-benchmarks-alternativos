# Ling 3.0 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 67.273s | tokens_per_second: 28.7
- input_tokens: 286 | output_tokens: 1928

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

## Conclusión: No se puede saber si la secuencia de emails funcionó.

Y esto no es una evasiva — es la única respuesta honesta que los datos permiten. Te explico por qué.

---

### Lo que los datos sí muestran

- El MRR subió de $4,100 a $5,300 (+29%) en marzo.
- Las altas al plan pago subieron de 9 a 14 (+56%).
- Hubo un incremento real de ingresos.

Eso es todo. Los datos confirman que **algo** generó crecimiento en marzo. No confirman **qué** lo generó.

---

### Por qué no se puede atribuir a los emails

En marzo ocurrieron **tres cambios simultáneos** que pudieron impulsar las conversiones:

1. **Secuencia de emails** (1 de marzo)
2. **Publicidad pagada** de $400 (3 de marzo)
3. **Mención de un creador con audiencia grande** (12 de marzo)

Cualquiera de los tres, o la combinación de ellos, pudo generar las 5 altas adicionales. Sin aislamiento de variables, **no existe forma de repartir el mérito entre estas tres causas**.

Peor aún: ni siquiera sabemos si los 14 pagos nuevos de marzo son personas que **estaban en la comunidad gratuita** y se convirtieron, o si son **usuarios completamente nuevos** que llegaron por publicidad o por el video del creador. Si la mayoría vino por el creador, los emails pudieron haber contribuido cero.

---

### Lo que haría falta para estar seguros

Para poder dar una respuesta concluyente, necesitarías como mínimo:

| Dato | Por qué lo necesitas |
|---|---|
| **Cuántos usuarios gratuitos activos había en marzo** | Para calcular la tasa de conversión real (altas / usuarios gratuitos) |
| **Segmentación de los 14 pagos nuevos por origen** (email, publicidad, creador, orgánico) | Para saber qué canal trajo cada conversión |
| **Métricas de los emails**: apertura, clic, y en qué punto del embudo se convirtieron | Para medir el rendimiento directo de la secuencia |
| **Grupo de control**: usuarios gratuitos que **no** recibieron los emails | Para comparar tasas de conversión con y sin la secuencia |
| **Retención de los 9 pagos de febrero**: ¿cuántos se mantuvieron en marzo? | Para distinguir crecimiento real de fluctuación |
| **Precio del plan pago** | Para reconciliar el MRR con el número de altas y entender el churn |

---

### Lo que haría ahora mismo

Si tuviera que tomar una decisión con la información disponible, **no invertiría más en escalar la secuencia de emails todavía**. No porque sea mala, sino porque no tengo evidencia de que funcione. En su lugar:

1. **Implementaría tracking de origen** para cada alta nueva (que cada canal quede claramente identificado).
2. **Crearía un grupo de control** en la próxima campaña: mitad de los usuarios gratuitos reciben emails, mitad no.
3. **Analizaría las métricas internas de los emails** (aperturas, clics) para ver si hay señales de engagement.
4. **Esperaría al menos un mes más** con estos controles puestos antes de sacar conclusiones.

---

**En resumen:** El crecimiento es real, la atribución no lo es. Los datos no sostienen que la secuencia de emails haya sido la causa. No digo que no lo fue — digo que no se puede saber, y es mejor decirlo ahora que tomar decisiones basándose en una narrativa cómoda.