# Qwen 3.8 Omni Flash — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.8-omni-flash`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 98.504s | tokens_per_second: 44.0
- input_tokens: 283 | output_tokens: 4330

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

**Conclusión corta: no se puede saber si la secuencia de emails funcionó con los datos que tienes.**  
Lo que sí puedes decir es que **marzo tuvo mejor desempeño que febrero**, pero **no puedes atribuir esa mejora a los emails** porque hubo al menos dos cambios importantes al mismo tiempo: publicidad pagada y una mención de un creador con audiencia grande.

---

## Qué muestran los números

| Métrica | Febrero | Marzo | Cambio |
|---|---:|---:|---:|
| MRR | $4.100 | $5.300 | +$1.200 / +29% |
| Altas al plan pago | 9 | 14 | +5 / +56% |

Además, como febrero tiene 28 días y marzo 31, conviene mirar tasas diarias:

- Febrero: 9 altas / 28 días = **0,32 altas/día**
- Marzo: 14 altas / 31 días = **0,45 altas/día**

Eso sigue siendo un aumento relevante, aproximadamente **+40% en altas por día**.

Pero ese aumento **coincide** con:

1. **Secuencia de emails iniciada el 1 de marzo**
2. **Publicidad pagada iniciada el 3 de marzo**
3. **Mención de un creador el 12 de marzo**

Por tanto, hay tres posibles causas mezcladas. No puedes separar cuál empujó las conversiones.

---

## Por qué no puedes concluir que los emails funcionaron

### 1. No hay grupo de control

Si todos los usuarios gratuitos recibieron la secuencia, no tienes un grupo comparable que no la recibió.

Sin control, no puedes medir el efecto incremental real.

Quizás los emails convirtieron a 3 personas.  
Quizás no convirtieron a nadie y todo vino de ads.  
Quizás la mención del creador generó la mayor parte del pico.  
Con estos datos, cualquiera de esas explicaciones es posible.

---

### 2. La publicidad puede explicar parte del crecimiento

Empezaste a pagar publicidad el 3 de marzo. Eso puede haber traído:

- usuarios gratuitos que luego vieron los emails;
- usuarios que fueron directamente a la página de pago;
- más tráfico orgánico por brand search;
- más conversiones sin relación causal con la secuencia.

Incluso si los emails “tocaron” a esos usuarios, no sabes si habrían convertido igual sin el email.

---

### 3. La mención del creador puede ser un evento muy fuerte

Un creador con audiencia grande mencionó la comunidad el 12 de marzo. Eso puede generar un pico de conversiones difícil de ignorar.

Si muchas altas ocurrieron entre el 12 y el 31 de marzo, la hipótesis más simple podría ser que la mención tuvo un impacto grande.

No lo sabes porque no tienes el desglose diario.

---

### 4. Las cifras absolutas son pequeñas

Pasaste de 9 a 14 altas. Eso son 5 conversiones adicionales.

Cinco conversiones pueden deberse a:

- un solo creador;
- una campaña de anuncios buena;
- ruido natural;
- un cambio estacional;
- un usuario que entró por casualidad;
- o efectivamente los emails.

Con tan pocas conversiones, la incertidumbre es alta.

---

### 5. El MRR no te dice cuánta parte viene de nuevas altas

El MRR subió $1.200, pero no sabes exactamente por qué.

Pudo subir por:

- altas nuevas;
- upgrades de plan;
- reactivaciones;
- reducción de churn;
- cambios de precio;
- expansiones dentro de cuentas existentes;
- mezcla de planes con diferente ARPU.

Las 5 altas adicionales no necesariamente explican todo el incremento de MRR.

Por ejemplo, si el ticket promedio mensual fuera bajo, 5 altas no sumarían $1.200. Si el ticket promedio fuera alto, sí podrían. Pero sin ARPU o detalle por plan, no puedes cerrarlo.

---

## Qué podrías afirmar con responsabilidad

Una frase correcta sería:

> “Marzo mostró un aumento de MRR y de altas respecto a febrero, pero no podemos atribuirlo con seguridad a la secuencia de emails porque concurrentemente lanzamos publicidad y recibimos una mención de un creador relevante.”

Otra versión más operativa:

> “Los emails no han demostrado todavía su efecto incremental. Puede que hayan ayudado, pero los datos actuales no permiten separar su impacto del de ads y de la mención del creador.”

---

# Qué haría falta para estar seguros

## 1. Un test controlado con holdout

Lo ideal habría sido:

- tomar una muestra aleatoria de usuarios gratuitos;
- enviar la secuencia a, por ejemplo, 80%;
- dejar 20% sin recibir emails;
- mantener ambas cohorts expuestas a las mismas condiciones externas.

Luego compararías:

| Grupo | Conversiones a pago | MRR generado |
|---|---:|---:|
| Recibió emails | ? | ? |
| No recibió emails | ? | ? |

La diferencia sería el efecto estimado de la secuencia.

Ese es el estándar más limpio.

---

## 2. Desglose diario de conversiones

Necesitarías ver las altas al plan pago por día, especialmente alrededor de:

- 1 de marzo: inicio de emails;
- 3 de marzo: inicio de publicidad;
- 12 de marzo: mención del creador.

Por ejemplo:

| Fecha | Altas | Origen estimado |
|---|---:|---|
| 1-2 marzo | ? | ¿emails? |
| 3-11 marzo | ? | ¿ads? |
| 12-31 marzo | ? | ¿mención? |

Si casi todas las altas ocurren después del 12, la mención pesa mucho.  
Si hay un pico temprano antes de ads y antes de la mención, los emails tendrían más evidencia.  
Si las altas están distribuidas durante todo marzo y coinciden con clicks de emails, habría una señal más clara.

---

## 3. Atribución por canal

Necesitarías clasificar cada alta según su origen:

- vino de email;
- vino de anuncio;
- vino de mención/orgánico;
- vino de búsqueda directa;
- vino de referral;
- origen desconocido.

Para eso harían falta:

- UTMs en links de emails y ads;
- eventos de conversión etiquetados;
- códigos o cupones únicos por canal;
- seguimiento de sesiones;
- atribución multi-touch si alguien vio email, luego clickeó anuncio, luego convirtió.

Sin esto, estás mezclando señales.

---

## 4. Métricas intermedias de la secuencia

No basta con mirar conversiones finales. Para evaluar emails necesitas ver el funnel:

| Etapa | Métrica |
|---|---:|
| Emails enviados | ? |
| Emails entregados | ? |
| Tasa de apertura | ? |
| Tasa de clics | ? |
| Visitas a página de upgrade desde email | ? |
| Inicios de checkout desde email | ? |
| Conversión final desde email | ? |
| Conversión total en periodo | ? |

Si muchos clickearon el email y luego convirtieron, hay evidencia de asociación.  
Aún no sería prueba causal perfecta, pero sería mucho más útil que solo comparar febrero y marzo.

---

## 5. Comparar cohortes comparables

Si no puedes hacer un holdout perfecto, busca grupos comparables:

- usuarios gratuitos que entraron antes del 1 de marzo vs después;
- usuarios de otro segmento que no recibieron la secuencia;
- usuarios que optaron por no recibir emails promocionales, si existiera ese grupo;
- usuarios de otro idioma, región o plan similar;
- cohortes históricas ajustadas por estacionalidad.

Pero cuidado: estos grupos deben ser realmente comparables. Si difieren en intención, antigüedad o fuente, la comparación puede engañarte.

---

## 6. Medir MRR neto, no solo MRR bruto

Necesitarías descomponer el cambio de MRR:

| Componente | Febrero | Marzo | Diferencia |
|---|---:|---:|---:|
| MRR nuevo por altas | ? | ? | ? |
| MRR por upgrades | ? | ? | ? |
| MRR por reactivaciones | ? | ? | ? |
| MRR perdido por bajas | ? | ? | ? |
| MRR perdido por downgrades | ? | ? | ? |
| MRR neto | $4.100 | $5.300 | +$1.200 |

Esto evita confundir crecimiento real con movimientos internos de planes.

---

## 7. Evaluar sostenibilidad

Una campaña puede generar un pico temporal. Para saber si tuvo impacto real, mira abril:

- ¿las conversiones se mantienen?
- ¿el MRR se sostiene?
- ¿hubo churn posterior a las altas de marzo?
- ¿las personas convertidas por email siguen activas?
- ¿el incremento fue solo un adelantamiento de conversiones que habrían ocurrido después?

A veces una campaña no crea demanda nueva, solo acelera decisiones.

---

# Mi lectura práctica con lo que tienes

Con la información actual:

- **Hay una señal positiva**: marzo mejoró frente a febrero.
- **No hay evidencia causal suficiente**: no puedes decir que la secuencia funcionó.
- **Hay confusión severa**: ads y mención del creador ocurrieron casi al mismo tiempo.
- **El volumen de conversiones es pequeño**: 5 altas extra no permiten conclusiones firmes.
- **El MRR subió, pero no está desglosado**: no sabes si fue por altas, upgrades, menor churn u otros factores.

Por tanto, mi recomendación sería tratar la secuencia como **“pendiente de validación”**, no como ganadora confirmada.

---

# Qué haría yo ahora

## Si quieres analizar retrospectivamente

Pide estos datos:

1. Altas al plan pago por día en febrero y marzo.
2. Origen de cada alta: email, ads, orgánico, referral, directo, desconocido.
3. Número de usuarios gratuitos que recibieron la secuencia.
4. Aperturas, clicks y conversiones atribuidas a emails.
5. Gasto publicitario diario y conversiones desde ads.
6. Tráfico y conversiones antes/después del 12 de marzo.
7. Detalle de MRR: nuevas altas, upgrades, churn, downgrades, reactivaciones.
8. ARPU promedio por plan.

Con eso podrías hacer una hipótesis más sólida, aunque todavía no sería un experimento limpio.

---

## Si quieres decidir si repetir la secuencia

No la apagues solo porque no puedas probar causalidad perfecta.  
Tampoco la declares exitosa.

Yo haría esto:

- mantenerla, pero con medición más fina;
- crear un holdout pequeño en el siguiente envío;
- usar links trackeados;
- separar clearly el efecto de ads;
- medir conversiones por cohorte;
- revisar si el pico de marzo se sostiene en abril.

---

## Si quieres una respuesta simple para tu equipo

Puedes decir:

> “Marzo creció, pero todavía no podemos afirmar que la secuencia de emails haya sido la causa. Hubo publicidad y una mención de creador casi al mismo tiempo. Para saber si los emails funcionaron, necesitamos un holdout o al menos atribución por canal y desglose diario de conversiones.”

---

## Veredicto final

**¿Funcionó la secuencia de emails?**  
**No se puede saber con estos datos.**

**¿Hubo mejora en marzo?**  
Sí, parece haberla.

**¿Esa mejora se debe a los emails?**  
No está demostrado. Podría deberse a emails, a publicidad, a la mención del creador, a una combinación de los tres o a ruido estacional.

**¿Qué haría falta para estar seguros?**  
Un grupo de control o holdout, atribución por canal, métricas diarias, funnel de email completo y desglose de MRR neto.