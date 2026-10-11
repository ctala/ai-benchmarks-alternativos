# Bonsai 2 27B — business_audit/atribucion_correlacion_temporal

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 91.008s | tokens_per_second: 44.3
- input_tokens: 283 | output_tokens: 4028

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



**Conclusión corta: no se puede saber.**  
Con los datos que pasaste **no puedo afirmar que la secuencia de emails funcionó**, ni tampoco que no funcionó. Lo que sí puedo decir es que **hubo crecimiento**, pero ese crecimiento podría deberse a la secuencia, a la publicidad, al creador, a una mezcla de factores o simplemente a una fluctuación normal.

Mi recomendación sería presentarlo así al equipo:

> “Hay una mejora en MRR y altas, pero no hay evidencia suficiente para atribuir esa mejora a la secuencia de emails. No se puede concluir que funcionó.”

---

## Por qué no alcanza para dar una conclusión

### 1. No hay grupo de control

Para saber si los emails causaron el aumento, idealmente habría que comparar:

- Usuarios gratuitos que recibieron la secuencia.
- Usuarios similares que **no** recibieron la secuencia, o recibieron un delay, o no recibieron ese mensaje.

Como no hay ese control, no puedo aislar el efecto de los emails.

---

### 2. Hay variables que entraron al mismo tiempo

Tú mencionas tres cosas importantes:

- 1 de marzo: secuencia de 5 emails.
- 3 de marzo: inicio de publicidad.
- 12 de marzo: creador menciona la comunidad.

Esto hace muy difícil atribuir el aumento del MRR o de las altas solo a los emails.

Por ejemplo:

- ¿Las nuevas altas vinieron de la publicidad?
- ¿Vinieron del video del creador?
- ¿Vinieron de los emails?
- ¿Fue una combinación?
- ¿Algunas altas eran usuarios que ya estaban en la comunidad y terminaron de comprar por otra razón?

Con los datos actuales no lo puedo separar.

---

### 3. El MRR no es lo mismo que las nuevas altas

Pasaste:

- MRR al 28 de febrero: **$4.100**
- MRR al 31 de marzo: **$5.300**
- Altas en febrero: **9**
- Altas en marzo: **14**

El MRR subió 29%, pero solo subieron 5 altas. Eso puede pasar por varias razones:

- Menos bajas/cancelaciones.
- Aumento de precio.
- Upgrade de plan.
- Altas de mayor valor.
- Altas de menor valor.
- Efecto de la publicidad.
- Efecto del creador.
- Efecto de los emails.

Por eso no puedo decir: “El MRR subió, por lo tanto los emails funcionaron”.

---

### 4. La muestra es pequeña

Pasamos de 9 a 14 altas. Eso es solo **5 altas adicionales**. Con números tan bajos, cualquier evento puede distorsionar mucho el resultado.

Por ejemplo, si el creador trajo 3 altas, ya se explica parte del aumento. Si la publicidad trajo 4, también. No hay forma de saberlo sin más datos.

---

## Qué haría falta para estar seguros

Para poder decir con confianza que la secuencia funcionó, me gustaría ver al menos esto:

### 1. Un test A/B con grupo control

La forma más limpia sería:

- Tomar usuarios gratuitos elegibles.
- Dividirlos en dos grupos:
  - Grupo A: recibe la secuencia de 5 emails.
  - Grupo B: no recibe la secuencia, o la recibe mucho después.
- Medir durante 30 o 60 días:
  - ¿Cuántos se pasaron a plan pago?
  - ¿Cuánto MRR generaron?
  - ¿Cuál fue el CAC?
  - ¿Cuánto duraron en la comunidad?

Si el grupo de emails convierte significativamente más, entonces sí podríamos decir que funcionó.

---

### 2. Cohortes por fuente o por primera interacción

Si no se puede hacer un test A/B, haría falta analizar:

- Usuarios que llegaron desde la secuencia de emails.
- Usuarios que llegaron desde publicidad.
- Usuarios que llegaron desde el creador.
- Usuarios que ya estaban en la comunidad y compraron sin ninguna de esas fuentes.

Y comparar:

- Tasa de conversión.
- Tiempo hasta conversión.
- MRR por usuario.
- Churn.
- LTV.

Pero aun así, sin control, solo sería una señal, no una prueba causal.

---

### 3. Atribución real de las ventas

Necesitaría saber:

- ¿Cuántas altas clickearon el email?
- ¿Cuántas llegaron desde el enlace del email?
- ¿Cuántas llegaron desde la publicidad?
- ¿Cuántas llegaron desde el video del creador?
- ¿Se usó UTM, código, landing page específica o seguimiento en CRM?

Sin eso, no puedo separar el efecto de cada canal.

---

### 4. Comparar contra una línea base

También ayudaría saber cómo estaba creciendo la comunidad antes de marzo.

Por ejemplo:

- ¿En enero hubo 8, 10 o 14 altas?
- ¿El MRR estaba creciendo naturalmente?
- ¿Había alguna campaña previa?
- ¿El plan gratuito ya tenía usuarios calientes?

Si febrero era un mes bajo y marzo tenía publicidad + creador, el aumento puede ser más bien por esos factores.

---

### 5. Medir el efecto en el tiempo

Una secuencia de 5 emails puede no tener efecto inmediato. A veces:

- El primer email abre la puerta.
- El segundo o tercero genera clic.
- La compra llega días después.
- Algunos usuarios abren pero no compran hasta semanas después.

Por eso no basta mirar solo marzo. Haría falta ver:

- 7 días.
- 14 días.
- 30 días.
- 60 días.

Y comparar si el grupo tratado convierte más que el grupo no tratado.

---

## Cómo plantearía la próxima validación

Si yo tuviera que diseñar esto para no tomar una decisión equivocada, haría algo así:

### Prueba mínima

1. Elegir usuarios gratuitos activos.
2. Dividirlos en:
   - Grupo con secuencia.
   - Grupo sin secuencia.
3. Enviar la secuencia solo al grupo tratado.
4. Medir durante 30/60 días:
   - Conversión a pago.
   - MRR incremental.
   - CAC.
   - Retención.
   - Churn.
5. Comparar ambas cohortes.

### Métrica clave

No me quedaría solo con “¿subió el MRR?”. Me fijaría en:

> **Altas pagas incrementales por usuario tratado vs. control**  
> y  
> **MRR incremental por usuario tratado vs. control**

Y también:

> **ROAS de los emails** = MRR incremental / costo de la secuencia o costo de la campaña.

Aunque los emails sean baratos, si no hay conversión incremental, no es una victoria.

---

## Mi veredicto final

**No se puede saber.**

Con los números actuales:

- Sí hay crecimiento.
- Sí hay más altas en marzo que en febrero.
- Sí subió el MRR.
- Pero **no se puede atribuir ese crecimiento a la secuencia de emails**.

Lo más honesto sería decir:

> “La secuencia pudo haber contribuido, pero no tenemos evidencia suficiente para afirmar que fue la causa del crecimiento. Además, hay publicidad y una mención de un creador ocurridas en el mismo periodo, que también pueden explicar parte o todo del resultado.”

Si quiero ser aún más directo:

> **No cerraría que funcionó. Lo que puedo sostener es que hay una señal positiva, pero no es suficiente para tomar una decisión de negocio basada solo en esto.**