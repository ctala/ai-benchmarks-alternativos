# Bonsai 2 27B — business_audit/atribucion_correlacion_temporal

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.51 | quality: 10.0
- latency_total: 190.39s | tokens_per_second: 31.1
- input_tokens: 283 | output_tokens: 5928

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
Con los números que pasaste **no hay evidencia suficiente para afirmar que la secuencia de emails funcionó**, ni tampoco para descartar que haya tenido un efecto. Lo que sí se puede decir es que **hubo crecimiento en marzo**, pero no podemos atribuirlo con seguridad a la secuencia.

---

## 1. Qué muestran los datos

Tienes:

- **MRR al 28 de febrero:** $4.100  
- **MRR al 31 de marzo:** $5.300  
- **Crecimiento MRR:** +$1.200, o **+29%**
- **Altas al plan pago en febrero:** 9  
- **Altas al plan pago en marzo:** 14  
- **Crecimiento de altas:** +5, o **+55%**

Y además tienes estos eventos:

- **1 de marzo:** activas la secuencia de 5 emails para usuarios del plan gratuito.
- **3 de marzo:** empiezas a pagar publicidad por $400 al mes.
- **12 de marzo:** un creador con audiencia grande menciona la comunidad.

---

## 2. Por qué no alcanza para concluir que la secuencia funcionó

El problema principal es que **no tienes un contrafactual**.

Para poder decir que la secuencia funcionó, necesitarías poder comparar:

> “¿Cuántos usuarios del plan gratuito se convirtieron en pago **porque recibieron la secuencia**?”  
> contra  
> “¿Cuántos se habrían convertido **si no la hubieran recibido**?”

Con los datos actuales solo tienes un antes y un después:

| Periodo | MRR | Altas pago |
|---|---:|---:|
| Febrero | $4.100 | 9 |
| Marzo | $5.300 | 14 |

Eso muestra crecimiento, pero **no muestra causalidad**.

---

## 3. Factores que confunden la lectura

Hay al menos tres factores que podrían explicar el aumento:

### A. La secuencia de emails

Activada el **1 de marzo**.  
Podría haber contribuido a que algunos usuarios gratuitos se pasaran a pago.

### B. La publicidad

Empezada el **3 de marzo**, con $400 mensuales.  
Aunque sea una cantidad pequeña, si trajo usuarios nuevos o aumentó la visibilidad, podría haber influido.

### C. La mención del creador

El **12 de marzo**, un creador con audiencia grande menciona la comunidad.  
Esto es especialmente relevante porque puede traer:

- nuevos usuarios,
- más registros gratuitos,
- más conversiones a pago,
- más MRR en el segundo half del mes.

Si la mayor parte de las altas de marzo ocurrió **después del 12**, sería más probable que el creador haya tenido efecto. Pero con los datos agregados no lo podemos saber.

---

## 4. El aumento de MRR no necesariamente viene de las 5 altas nuevas

El MRR es una métrica de stock, no solo de nuevas altas.

El salto de $4.100 a $5.300 puede deberse a:

- nuevas altas,
- upgrades de usuarios existentes,
- menor churn,
- cambios de precio,
- usuarios que se quedaron en lugar de salir,
- efecto de la publicidad,
- efecto del creador,
- estacionalidad natural.

Además, pasamos de 9 a 14 altas. Eso son solo **5 altas adicionales**. No es mucho. Puede ser una señal, pero también puede estar dentro del ruido.

Por ejemplo, si en febrero tuviste 9 altas, ver 14 en marzo no es una prueba suficiente de que hubo un cambio estructural. Depende de la base de usuarios gratuitos, la conversión histórica, la variabilidad mensual y otros factores.

---

## 5. Lo que sí podemos decir

Podemos decir esto con confianza:

1. **Hubo crecimiento en marzo.**
2. **El MRR aumentó un 29%.**
3. **Hubo 5 altas más que en febrero.**
4. **La secuencia de emails es una hipótesis plausible.**
5. **La publicidad y la mención del creador también son hipótesis plausibles.**
6. **No se puede atribuir el crecimiento a la secuencia de emails solo con estos datos.**

Lo que **no** podemos decir:

> “La secuencia de emails funcionó.”

Tampoco podemos decir:

> “La secuencia de emails no funcionó.”

La respuesta honesta es:

> **No se puede saber.**

---

## 6. Qué haría falta para estar seguros

Para poder afirmar que la secuencia funcionó, necesitaría al menos una de estas opciones:

---

# Opción ideal: experimento con grupo control

Lo más sólido sería hacer un **test A/B** o un **holdout**.

Por ejemplo:

- Tomas a los usuarios del plan gratuito.
- Los divides al azar en dos grupos:
  - **Grupo A:** recibe la secuencia de emails.
  - **Grupo B:** no recibe la secuencia, o la recibe tardío, o no la recibe durante un periodo.
- Mides a los dos grupos durante el mismo periodo.

Métrica principal:

> ¿Cuántos usuarios del grupo A se convierten a pago en comparación con el grupo B?

Métricas secundarias:

- MRR incremental por usuario,
- tiempo hasta la conversión,
- tasa de apertura/click,
- tasa de completado de la secuencia,
- churn,
- CAC,
- ROI.

Si el grupo que recibió emails convierte significativamente más que el grupo que no la recibió, entonces sí podrías decir que la secuencia tuvo efecto.

---

# Opción menos ideal: atribución por fuente

Si no puedes hacer un test A/B, lo mínimo sería tener **atribución clara**.

Necesitarías saber de dónde vienen las altas:

- ¿De email?
- ¿De publicidad?
- ¿De la mención del creador?
- ¿De orgánico?
- ¿De referral?
- ¿De búsqueda?

Eso se puede hacer con:

- UTM en los enlaces de los emails,
- códigos de descuento por campaña,
- formularios con pregunta de origen,
- tracking de clicks,
- primera/touch attribution,
- registros diarios de nuevas altas.

Con eso podrías ver, por ejemplo:

| Fuente | Altas en marzo |
|---|---:|
| Email | 6 |
| Publicidad | 4 |
| Creador | 2 |
| Orgánico | 2 |

Aun así, eso no sería prueba causal perfecta, pero sería mucho mejor que solo ver el total.

---

# Opción temporal: ver el día a día

También ayudaría muchísimo tener la serie temporal diaria o semanal.

Por ejemplo:

| Fecha | Altas pago | MRR nuevo |
|---|---:|---:|
| 1 marzo | ? | ? |
| 2 marzo | ? | ? |
| 3 marzo | ? | ? |
| 4 marzo | ? | ? |
| 12 marzo | ? | ? |
| 13 marzo | ? | ? |

Con eso podrías ver si el aumento coincide con:

- la activación de la secuencia,
- el inicio de la publicidad,
- la mención del creador.

Por ejemplo:

- Si las altas subieron entre el **1 y el 8 de marzo**, antes del creador y poco después de los emails, sería una pista a favor de la secuencia.
- Si el aumento fuerte aparece **después del 12 de marzo**, sería más probable que el creador influyó.
- Si hay un salto el **3 de marzo**, podría relacionarse con la publicidad.
- Si el crecimiento es gradual todo el mes, podría ser tendencia natural o efecto combinado.

Pero incluso así, sin control, sería una hipótesis, no una prueba.

---

## 7. Datos concretos que necesitaría

Para darte una respuesta más firme, me gustaría ver:

### Sobre la base de usuarios gratuitos

- ¿Cuántos usuarios tienes en el plan gratuito?
- ¿Cuántos recibieron los 5 emails?
- ¿Cuántos completaron la secuencia?
- ¿Cuántos abrieron clic?
- ¿Cuántos abrieron cada email?
- ¿Cuántos se dieron de baja o dejaron de recibir emails?

### Sobre las conversiones

- ¿Cuántos usuarios gratuitos se convirtieron a pago en marzo?
- ¿De esos, cuántos venían de la secuencia de emails?
- ¿Cuántos entraron al plan gratuito antes del 1 de marzo?
- ¿Cuántos entraron después?
- ¿Cuántos se convirtieron en los primeros días de marzo?
- ¿Cuántos se convirtieron después del 12 de marzo?

### Sobre el MRR

- ¿El MRR de $5.300 incluye solo nuevos usuarios?
- ¿Incluye upgrades?
- ¿Incluye menor churn?
- ¿Hubo cambios de precio?
- ¿Puedes desglosar el MRR entre:
  - nuevos pagos,
  - upgrades,
  - cancelaciones,
  - usuarios existentes?

### Sobre publicidad

- ¿Cuántas visitas trajo la publicidad?
- ¿Cuántos registros gratuitos trajo?
- ¿Cuántas altas a pago atribuyes a publicidad?
- ¿Qué canal usaste?
- ¿Qué oferta usaste?

### Sobre el creador

- ¿Cuántas visitas trajo la mención?
- ¿Cuántos registros trajo?
- ¿Cuántas altas a pago trajo?
- ¿Puedes identificar visitas con UTM o código del creador?

---

## 8. Cómo mediría que la secuencia funcionó

Yo definiría “funcionó” así:

> La secuencia generó conversiones a pago incrementalmente mayores que las que habrían ocurrido sin la secuencia.

Para eso, la métrica principal sería:

> **Tasa de conversión de usuarios gratuitos a pago dentro de un periodo fijo, comparando usuarios expuestos a la secuencia vs usuarios no expuestos.**

Por ejemplo:

| Grupo | Usuarios gratuitos | Se convirtieron a pago en 30 días | Tasa |
|---|---:|---:|---:|
| Recibió emails | 1.000 | 40 | 4,0% |
| No recibió emails | 1.000 | 25 | 2,5% |

Eso sí mostraría un efecto positivo.

Pero si solo tengo:

> “En febrero hubo 9 altas y en marzo hubo 14”,

no puedo afirmar que la secuencia fue la causa.

---

## 9. Mi recomendación práctica

No diría que la secuencia funcionó.  
Tampoco diría que fracasó.

Yo diría:

> **Hay una señal positiva, pero está contaminada por publicidad y una mención de un creador. Para tomar una decisión de inversión o escalado, necesitamos un test controlado.**

### Plan mínimo para los próximos 30 días

1. **No escalar la secuencia como si ya estuviera probada.**
2. **Crear un grupo control.**
   - Por ejemplo, del 20% al 30% de los usuarios gratuitos no reciban la secuencia o la reciban con retraso.
3. **Medir conversiones por grupo.**
   - Conversion a pago en 30 días.
   - MRR incremental.
   - Tiempo hasta conversión.
4. **Añadir tracking de origen.**
   - UTM en emails.
   - Código promocional opcional.
   - Preguntar en el formulario de alta: “¿Cómo nos conociste?”
5. **Registrar día a día.**
   - Altas,
   - MRR nuevo,
   - churn,
   - clicks,
   - visitas,
   - eventos de publicidad,
   - eventos del creador.
6. **Después de 30 a 45 días, comparar.**

Si el grupo con emails convierte significativamente más que el grupo sin emails, entonces sí podrías decir que funcionó.

---

## 10. Conclusión final

**No se puede saber con estos datos.**

Lo que tenemos es:

- crecimiento de MRR,
- más altas,
- una secuencia de emails activada,
- publicidad nueva,
- una mención de un creador.

Eso no permite atribuir el resultado a la secuencia.

La respuesta responsable sería:

> **Los datos muestran crecimiento en marzo, pero no permiten afirmar que la secuencia de emails fue la causa. Para concluir que funcionó, necesitaríamos un grupo control, atribución por fuente y datos diarios de conversiones.**