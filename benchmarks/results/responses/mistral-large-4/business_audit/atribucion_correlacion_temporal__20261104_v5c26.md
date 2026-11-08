# Mistral Large 4.0 — business_audit/atribucion_correlacion_temporal

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 44.429s | tokens_per_second: 57.1
- input_tokens: 227 | output_tokens: 2539

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

**No se puede saber.** Con estos datos no es posible concluir que la secuencia de emails funcionó, ni que no funcionó. Lo único que sabemos es que marzo fue mejor que febrero en MRR y en altas brutas, pero hay tres intervenciones simultáneas (emails, ads, mención del creador) y faltan datos críticos para atribuir el efecto a ninguna de ellas.

Aquí está el desglose de por qué estos números no sostienen una conclusión:

### 1. No hay contrafactual (grupo de control)
No sabemos qué habría pasado en marzo **sin** la secuencia de emails. Quizás marzo siempre es mejor que febrero (estacionalidad), o quizás el crecimiento venía de antes. Sin comparar contra un grupo que no recibió los emails, cualquier atribución es especulación.

### 2. Confusión de variables (el problema grave)
Lanzaste tres palancas al mismo tiempo:
- **1 marzo:** Emails
- **3 marzo:** Publicidad pagada ($400)
- **12 marzo:** Mención del creador grande

El salto de 9 a 14 altas (y el +$1.200 de MRR) pudo venir de cualquiera de las tres, de una combinación, o de factores externos. Es imposible separarlas con datos agregados mensuales.

### 3. "Altas" no es igual a "MRR neto"
El MRR subió $1.200, pero no sabemos cuántas bajas (churn) hubo en cada mes. Es posible que en marzo entraran 14 usuarios nuevos pero se fueran 8, y en febrero entraran 9 y se fueran 2. Sin datos de cancelaciones, no sabemos si la comunidad realmente creció más o solo "giró" más rápido.

Tampoco sabemos el valor de cada alta: ¿todos pagan el mismo plan? ¿Hubo upgrades de usuarios existentes? Un MRR de +$1.200 con solo 5 altas netas más (14 vs 9) implica un ARPU muy alto o expansiones internas que no estamos viendo.

### 4. Falta el denominador
¿Cuántos usuarios gratuitos había el 1 de marzo? Si eran 200 y se convirtieron 5, es una tasa del 2,5%. Si eran 10.000, es el 0,05%. Sin saber la base, no podemos calcular la tasa de conversión real de la secuencia.

### 5. No sabemos de dónde vienen las altas
No hay tracking de fuente. Los 14 usuarios de marzo pudieron venir de los ads, del video del creador, de búsqueda orgánica, o de los emails. Sin UTMs, campo "cómo nos encontraste" o atribución, no hay forma de asignar crédito.

---

## Qué haría falta para estar seguros

Para poder decir "la secuencia funcionó" con confianza, necesitarías al menos esto en la próxima iteración:

**1. Test A/B con grupo de control (holdout)**
- Divide aleatoriamente a los usuarios gratuitos: 80% recibe la secuencia, 20% no recibe nada (o recibe una versión mínima).
- Compara la tasa de conversión de ambos grupos al final del mes. La diferencia neta es el efecto real de los emails.

**2. Datos diarios, no mensuales**
- Gráfica diaria de altas, MRR y tráfico desde el 25 de febrero hasta el 10 de abril.
- Así podrías ver si hay un pico el 1-5 de marzo (emails), otro el 3-10 (ads) y otro después del 12 (influencer). Si todo sube justo después del 12, probablemente el creador fue el motor.

**3. Churn y movimientos internos**
- Número de cancelaciones por mes.
- Upgrades/downgrades entre planes.
- MRR neto real = altas nuevas + expansiones - churn - contracciones.

**4. Atribución de fuente en el alta**
- Pregunta obligatoria en el checkout: "¿Cómo nos encontraste?" (Email, Anuncio pagado, Video de [Creador], Búsqueda, Otro).
- O usa UTM parameters en todos los enlaces de los emails y los ads.

**5. Métricas de la secuencia misma (engagement, no conversión)**
- Tasa de apertura, CTR y desuscripciones por email.
- Esto te dice si los emails llegaron y se leyeron, pero **no prueba que causaran conversiones** (alguien puede abrir el email y luego entrar por el anuncio).

**6. Datos históricos de estacionalidad**
- ¿Cómo fue marzo vs febrero el año pasado? Si marzo siempre sube un 25-30%, entonces el crecimiento no es atribuible a tus acciones de este año.

**7. Tamaño de la base de usuarios gratuitos**
- Cuántos usuarios gratuitos había el 1 de marzo y cuántos quedan al 31. Necesitas la tasa de conversión sobre el total elegible.

---

## Recomendación práctica para la próxima vez

Si quieres saber si los emails funcionan, haz esto ahora:

1. **Pausa la secuencia para un 20% aleatorio de los usuarios gratuitos nuevos** durante un mes (grupo de control).
2. **Añade UTMs a todos los emails** (`utm_source=email&utm_medium=automation&utm_campaign=secuencia_marzo`) y a los ads.
3. **Añade la pregunta de atribución** en el formulario de pago.
4. **Mide diariamente**, no mensualmente.
5. Al final del mes, compara: tasa de conversión del grupo que recibió emails vs. el que no. Esa diferencia, aislada de ads e influencers, es tu respuesta real.

**Conclusión ahora mismo:** Tienes una correlación positiva en marzo, pero con tres causas posibles y datos insuficientes, la única respuesta honesta es que **no se puede atribuir el éxito a la secuencia de emails**. Podría haber funcionado, podría no haber hecho nada, o podría haber perjudicado (si aumentó las desuscripciones, por ejemplo, y no lo estás midiendo).