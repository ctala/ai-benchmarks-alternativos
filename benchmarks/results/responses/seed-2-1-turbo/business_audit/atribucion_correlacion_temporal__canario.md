# Seed 2.1 Turbo — business_audit/atribucion_correlacion_temporal

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 80.023s | tokens_per_second: 76.1
- input_tokens: 275 | output_tokens: 6091

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

### Conclusión
No se puede saber si la secuencia de emails funcionó. Los datos que compartes muestran que hubo un crecimiento de MRR y de altas en marzo, pero no hay forma de atribuir ese crecimiento a la secuencia de emails porque coincidieron en el tiempo otros factores que también pueden explicar el aumento, y no hay un grupo de referencia para aislar el efecto de los emails.

---

### Por qué no se puede afirmar con la información actual
Hay tres problemas clave que invalidan cualquier conclusión causal:
1. **Factores confundidores simultáneos**: En marzo lanzaste dos acciones más que directamente generan altas y crecimiento de MRR:
   - Publicidad pagada desde el 3 de marzo (apenas 2 días después de la secuencia de emails)
   - Mención de un creador con audiencia grande el 12 de marzo, que suele generar picos importantes de tráfico y conversiones.
   No hay forma de saber qué parte del aumento corresponde a los emails, qué a la publicidad y qué a la mención del creador. Incluso las conversiones de usuarios que ya eran gratuitos antes de marzo podrían deberse a la mención del creador, no a los emails.

2. **Falta de seguimiento de origen de las conversiones**: No sabes:
   - Cuántas de las 14 altas de marzo vinieron de usuarios que abrieron o cliqueasteon los emails de la secuencia.
   - Si las altas son de usuarios que ya eran gratuitos antes del 1 de marzo (población objetivo de la secuencia) o de usuarios nuevos que entraron en marzo por la publicidad o la mención, o incluso de personas que se suscribieron directamente al plan pago sin pasar por el gratuito.
   - Cuánto del aumento de MRR viene de altas nuevas, y cuánto de otros factores: menos bajas de usuarios existentes, upgrades de plan, etc.

3. **No conocemos la tendencia previa**: No tienes datos de crecimiento de meses anteriores para saber si el aumento de marzo es superior al ritmo que ya venías teniendo. Por ejemplo, si de enero a febrero las altas pasaron de 6 a 9 (un 50% de aumento, similar al 55% de marzo), el crecimiento no sería una novedad. También febrero tiene 3 días menos que marzo, lo que explica una pequeña parte de la diferencia de altas (aunque no toda).

---

### ¿Qué puedes revisar AHORA para acercarte a una respuesta (aún no concluyente)?
Si tienes acceso a datos más detallados de tu herramienta de email marketing, CRM o pasarela de pagos, puedes revisar estos puntos para tener una pista, aunque no te darán una certeza total:
1. **Atribución de conversiones**: Revisa cuántas de las 14 altas de marzo vinieron de clicks en enlaces de la secuencia de emails (si usas UTMs o tu herramienta de email marca conversiones atribuidas a los envíos). Ojo: esto no prueba causalidad (un usuario puede cliquear el email pero haberse decidido a pagar por la mención del creador), pero si ninguna alta viene de los emails, es una señal de que probablemente no funcionaron.
2. **Antigüedad de los usuarios convertidos**: Cuenta cuántos de los 14 usuarios que se pagaron en marzo ya estaban registrados en el plan gratuito antes del 1 de marzo. Si la mayoría son usuarios nuevos de marzo, la secuencia tuvo muy poco o nada que ver con su conversión.
3. **Distribución de altas por fecha**: Mira en qué días de marzo se produjeron las altas. Si hay un pico muy grande justo después del 12 de marzo (cuando salió el video del creador), esa acción explica la mayor parte del aumento. Si hay picos pequeños coincidiendo con cada envío de la secuencia, es una señal positiva (pero no concluyente).
4. **Desglose del MRR**: Revisa cuánto del aumento de $1.200 de MRR viene de altas nuevas, y cuánto de menos bajas o upgrades. Si el aumento viene sobre todo de otros factores que no sean altas de usuarios gratuitos, la secuencia no es la causa.
5. **Tendencia de meses anteriores**: Compara el crecimiento de altas y MRR de enero a febrero para ver si el ritmo de marzo es superior al que ya venías teniendo.

---

### ¿Qué hace falta para estar SEGUROS de si la secuencia funcionó?
La única forma de confirmar causalidad (es decir, que la secuencia de emails es la causa de un aumento de conversiones) es hacer una **prueba A/B con grupo de control**:
1. Divide a los usuarios del plan gratuito de forma completamente aleatoria en dos grupos:
   - **Grupo tratamiento**: Recibe la secuencia de 5 emails.
   - **Grupo control**: No recibe la secuencia (o recibe los emails que enviabas antes de lanzar esta secuencia, si los había).
2. Deja correr la prueba durante un periodo definido (ej: 30 días, el tiempo que dura la secuencia más un margen para que los usuarios se conviertan).
3. Al final, compara la tasa de conversión a pago (y el MRR por usuario) entre ambos grupos. Si la diferencia es estadísticamente significativa (es decir, es muy poco probable que se deba al azar), puedes afirmar que la secuencia funcionó, e incluso medir cuánto aporta exactamente (ej: aumenta la conversión en un 30%).

#### Recomendaciones para que la prueba sea válida:
- Hazla en un periodo donde no haya acciones externas grandes (como menciones de creadores o campañas de publicidad masivas) para que ambos grupos se vean afectados por las mismas condiciones, y solo se diferencien por los emails.
- Si tienes pocos usuarios gratuitos (lo que es normal en una comunidad pequeña), puede que tengas que dejar la prueba corriendo varios meses para acumular suficientes conversiones y que el resultado sea fiable.
- No midas solo la cantidad de altas: también el valor de vida útil de los usuarios que se convierten por la secuencia, para saber si no solo generan más ingresos, sino también usuarios de mejor calidad.