# Qwen 3.8 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 94.191s | tokens_per_second: 84.1
- input_tokens: 283 | output_tokens: 7923

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

No se puede saber con estos datos.

Lo que tienes es una mejora temporal, no una prueba de causalidad. La pregunta real es: **¿habrías tenido menos MRR y menos altas si no hubieras lanzado la secuencia de emails?** Para responder eso necesitas un contrafactual, y aquí no lo tienes.

## Conclusión responsable

**No se puede afirmar que la secuencia de emails funcionó.**

Tampoco se puede afirmar que no funcionó. Lo correcto es decir:

> “En marzo aumentaron las altas y el MRR, pero hubo al menos tres intervenciones simultáneas: secuencia de emails, publicidad pagada y mención de un creador. Con los datos agregados actuales no es posible atribuir el crecimiento a la secuencia de emails.”

Si necesitas un veredicto para un informe o decisión interna: **inconclusivo**.

---

## Qué dicen los números, y qué no dicen

Tienes:

- MRR 28 feb: **$4.100**
- MRR 31 mar: **$5.300**
- Aumento: **+$1.200 / +29%**
- Altas pagadas feb: **9**
- Altas pagadas mar: **14**
- Aumento: **+5 / +55,6%**

Eso solo demuestra que:

1. Marzo tuvo más MRR que febrero.
2. Marzo tuvo más altas que febrero.
3. La secuencia de emails coincidió con ese crecimiento.

Pero no demuestra que la secuencia causó ese crecimiento.

### Por qué no se puede atribuir

#### 1. Hubo otras intervenciones al mismo tiempo

El 1 de marzo lanzaste emails.

El 3 de marzo empezaste a pagar publicidad.

El 12 de marzo un creador con audiencia grande mencionó la comunidad.

Cualquiera de esas tres cosas, o una combinación, puede explicar las 5 altas adicionales.

Incluso si la secuencia ayudó, no sabes si fue la causa principal, una causa menor o si simplemente coincidió con un mes mejor.

#### 2. No tienes segmentación por fuente

No sabes cuántas de las 14 altas de marzo vinieron de:

- usuarios gratuitos que hicieron clic en los emails;
- tráfico de publicidad pagada;
- seguidores del creador;
- tráfico orgánico;
- referidos;
- campañas anteriores;
- conversiones tardías de febrero.

Sin eso, no puedes separar el efecto de los emails del efecto de la publicidad o del creador.

#### 3. El MRR no es una métrica limpia para esto

El MRR puede subir por:

- nuevas altas;
- planes anuales pagados por adelantado;
- upgrades;
- menos churn;
- cambios de precio;
- descuentos;
- reactivaciones;
- usuarios que entraron antes y pagaron después.

Además, si la secuencia iba dirigida a usuarios del plan gratuito, la métrica más relevante no sería MRR total, sino **conversión de gratuito a pago** entre los usuarios que recibieron la secuencia.

#### 4. La muestra es pequeña

9 vs 14 altas mensuales es una diferencia pequeña.

Puede ser una mejora real, pero también puede ser ruido natural. Por ejemplo, si normalmente tienes entre 8 y 12 altas al mes, 14 no es una señal contundente.

Y aunque 14 fuera estadísticamente inusual, seguiría sin demostrar que fue por los emails, porque hubo otros cambios simultáneos.

#### 5. La publicidad y el creador pueden haber aumentado la base gratuita

Si la publicidad o el creador trajeron más usuarios al plan gratuito, entonces podrías tener más usuarios recibiendo la secuencia de emails.

En ese caso, aunque los emails convirtieran, el crecimiento podría deberse principalmente a que entraron más leads, no a que la secuencia fuera más efectiva.

Necesitarías saber:

- usuarios gratuitos al 1 de marzo;
- usuarios gratuitos nuevos durante marzo;
- cuántos entraron por ads;
- cuántos entraron por el creador;
- cuántos convirtieron a pago;
- tasa de conversión gratuita → pago por fuente.

#### 6. No sabes el timing real de las conversiones

Los emails pueden tener efecto inmediato o diferido.

Si la secuencia es de 5 emails, algunas conversiones pueden ocurrir en marzo, otras en abril, y otras nunca.

También puede pasar que el creador o la publicidad generen conversiones más rápidas, mientras los emails generan efecto más lento.

Sin fechas exactas de conversión y fuente, no puedes separar los efectos.

---

## Qué sí se puede decir con prudencia

Puedes decir cosas como:

- “Hubo un aumento de MRR en marzo.”
- “Hubo más altas en marzo que en febrero.”
- “La secuencia de emails no puede descartarse como factor.”
- “Pero el crecimiento está contaminado por otras acciones simultáneas.”
- “Hasta no segmentar por fuente y cohortes, no podemos atribuir el resultado a los emails.”

No deberías decir:

- “La secuencia de emails funcionó.”
- “Los emails generaron los $1.200 extra de MRR.”
- “Los emails causaron las 5 altas adicionales.”
- “La secuencia aumentó el MRR un 29%.”

Esas afirmaciones van más allá de lo que los datos sostienen.

---

## Qué haría falta para estar razonablemente seguros

### Escenario ideal: prueba controlada

Para saber si la secuencia funcionó, lo ideal sería repetir o continuar el experimento con un grupo de control.

Por ejemplo:

- usuarios gratuitos elegibles;
- 70% o 80% reciben la secuencia de emails;
- 20% o 30% no reciben la secuencia, o la reciben más tarde;
- ambos grupos están expuestos a las mismas condiciones: misma publicidad, mismas menciones, misma oferta, mismo periodo.

Métrica principal:

> tasa de conversión de gratuito a pago dentro de los próximos 30, 60 o 90 días.

Métricas secundarias:

- MRR incremental;
- CAC;
- tasa de apertura;
- clics;
- bajas;
- spam;
- tiempo hasta conversión;
- calidad de los usuarios convertidos.

Si el grupo que recibió emails convierte mejor que el grupo control, ahí sí tendrías evidencia decente.

---

### Si no puedes hacer un experimento controlado, al menos analiza datos observacionales

Necesitarías reconstruir marzo con más detalle.

#### 1. Desglose de altas por fuente

Para cada alta de marzo, saber:

- fecha;
- usuario;
- cuándo entró al plan gratuito;
- fuente de adquisición;
- si hizo clic en algún email;
- si vino de ads;
- si vino del creador;
- si fue orgánico;
- si fue referido;
- si ya era usuario gratuito antes del 1 de marzo.

Idealmente, una tabla así:

| Fecha alta | Usuario | Fuente original | Recibió secuencia | Clic en email | Hora alta | Fuente atribuida |
|---|---|---|---|---|---|---|
| 10 mar | user123 | orgánico | sí | sí | 20:15 | email |
| 14 mar | user456 | ads | sí | no | 11:03 | ads |
| 18 mar | user789 | creador | sí | sí | 19:40 | mixto |

Sin eso, no puedes atribuir.

#### 2. Cohortes de usuarios gratuitos

Necesitarías comparar cohorts:

- usuarios gratuitos que ya existían al 28 de febrero;
- usuarios gratuitos nuevos entrados en marzo;
- usuarios gratuitos entrados por ads;
- usuarios gratuitos entrados por el creador;
- usuarios gratuitos que abrieron/clickearon emails;
- usuarios gratuitos que no abrieron/clickearon emails.

Pero cuidado: comparar “los que clickearon” vs “los que no clickearon” no prueba causalidad. Los que clickean suelen tener más intención de compra. Eso es sesgo de autoselección.

Aun así, ayuda a entender si los emails generaron actividad.

#### 3. Tasa histórica de conversión gratuito → pago

Necesitarías saber, por ejemplo:

- enero: cuántos usuarios gratuitos, cuántos convirtieron, tasa;
- febrero: cuántos usuarios gratuitos, cuántos convirtieron, tasa;
- marzo: cuántos usuarios gratuitos, cuántos convirtieron, tasa.

Si en marzo la base gratuita creció mucho por ads o por el creador, es normal que suban las altas aunque la tasa de conversión sea igual o peor.

Ejemplo:

- Febrero: 500 usuarios gratuitos → 9 altas → 1,8%
- Marzo: 900 usuarios gratuitos → 14 altas → 1,55%

En ese caso, las altas suben porque hay más gente, pero la conversión mejora no aparece. Y si además hubo ads y creador, el efecto de los emails sigue siendo dudoso.

#### 4. Analizar el timing

Mirar las fechas exactas de las altas.

Preguntas útiles:

- ¿Las altas se concentraron después del 3 de marzo? Posible ads.
- ¿Se concentraron después del 12 de marzo? Posible creador.
- ¿Se distribuyeron a lo largo de los 5 emails? Posible secuencia.
- ¿Hubo un pico el día 1, 2, 3, 4 o 5 de la secuencia?
- ¿Hubo altas de usuarios que clickearon emails, o de usuarios que no?

Un gráfico de altas diarias con líneas verticales en:

- 1 mar: secuencia;
- 3 mar: ads;
- 12 mar: creador.

ayudaría mucho.

#### 5. Medir el embudo de emails

Para la secuencia necesitas:

- cuántos emails fueron enviados;
- entregabilidad;
- aperturas;
- clics;
- bajas;
- reportes de spam;
- conversiones desde clic;
- conversiones asistidas por email.

Si los emails no generaron clics o conversiones observables, es difícil sostener que fueron la causa.

#### 6. MRR waterfall

Necesitarías desglosar el cambio de MRR:

```text
MRR inicial
+ nuevo MRR de altas
+ expansiones
- contracciones
- churn
+ reactivaciones
± ajustes/descuentos
= MRR final
```

Sin esto, no sabes si los $1.200 extra vinieron de las 14 altas, de menos churn, de upgrades o de planes anuales.

---

## Qué datos concretos pediría para poder opinar mejor

Si fueras mi cliente, te pediría:

1. **Usuarios gratuitos al 28 de febrero.**
2. **Altas al plan gratuito en marzo.**
3. **Altas al plan gratuito por fuente:** orgánico, ads, creador, referido, email, otros.
4. **Altas al plan pago en marzo por fecha y fuente.**
5. **Si cada usuario pago ya era gratuito antes del 1 de marzo o entró después.**
6. **Emails enviados, entregados, abiertos y clickeados.**
7. **Conversiones atribuidas a clics en emails.**
8. **Gasto y resultados de ads:** impresiones, clics, leads, conversiones, CAC.
9. **Tráfico generado por el creador:** visitas, registros gratuitos, altas pagadas.
10. **Historial de altas pagadas por mes:** al menos noviembre, diciembre, enero, febrero.
11. **Historial de MRR por mes.**
12. **Churn de febrero y marzo.**
13. **Precio promedio de los planes nuevos.**
14. **Si hubo cambios de precio, descuentos, ofertas o cambios en el producto.**

Con eso ya podríamos hacer una atribución mucho más seria.

---

## Qué análisis haría yo con esos datos

Intentaría estimar cuántas altas “esperadas” habría tenido en marzo sin la secuencia, y luego ver si las observadas superan esa expectativa.

Una versión simple sería:

```text
Altas esperadas = usuarios gratuitos elegibles × tasa histórica de conversión gratuito → pago
Altas incrementales = altas observadas - altas esperadas
```

Pero eso aún sería imperfecto si ads y creador cambiaron la calidad de los usuarios.

Lo robusto sería comparar grupos:

```text
Tasa de conversión grupo con secuencia vs tasa de conversión grupo sin secuencia
```

o:

```text
Tasa de conversión usuarios expuestos a email vs usuarios no expuestos, controlando por fuente y cohortes
```

Si no puedes controlar por fuente, no puedes separar emails de ads/creador.

---

## Mi recomendación práctica para el equipo

### Para este resultado

No digas:

> “La secuencia de emails funcionó.”

Di:

> “La secuencia de emails es una hipótesis posible, pero el resultado de marzo no permite atribuir el crecimiento a los emails porque coincidieron publicidad pagada y una mención de un creador. Necesitamos segmentación por fuente y un test con grupo control.”

### Para la próxima decisión

Si quieres saber si la secuencia realmente funciona, haz esto:

1. Mantén publicidad y creador, si quieres seguir creciendo.
2. Pero para medir emails, usa un grupo control.
3. A los usuarios gratuitos elegibles, asigna aleatoriamente:
   - grupo A: recibe la secuencia;
   - grupo B: no recibe la secuencia.
4. Mide conversión gratuita → pago a 30/60/90 días.
5. Añade UTM links y atribución por fuente.
6. No uses solo MRR total como métrica de éxito.

---

## Resumen corto

**¿La secuencia de emails funcionó?**

No se puede saber con los datos que tienes.

Lo que sí se puede decir es que hubo más MRR y más altas en marzo, pero el resultado está contaminado por al menos dos intervenciones adicionales: publicidad pagada y mención de un creador.

Para estar seguros, necesitarías una prueba controlada o, como mínimo, datos segmentados por cohortes, fuentes, fechas, clics de email, tráfico de ads, tráfico del creador, conversión gratuito → pago y desglose de MRR.