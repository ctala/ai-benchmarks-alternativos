# Tencent Hy4 preview — business_audit/atribucion_correlacion_temporal

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.18 | quality: 10.0
- latency_total: 253.96s | tokens_per_second: 54.7
- input_tokens: 256 | output_tokens: 13879

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

## Conclusión

**No. Con estos datos no se puede saber si la secuencia de emails funcionó.**  
Y ojo: no estoy diciendo que **no** funcionó. Estoy diciendo que **los datos no permiten afirmar que sí**. Atribuir el crecimiento a los emails sería una conclusión cómoda, pero no sostenida.

Lo único que los datos dicen con seguridad es:

- El MRR pasó de **$4.100** a **$5.300** (**+$1.200**, +29%).
- Las altas al plan pago pasaron de **9 en febrero** a **14 en marzo** (**+5**).
- En marzo hiciste **tres cosas nuevas casi al mismo tiempo**:
  - Secuencia de emails a usuarios free (1 de marzo).
  - Publicidad pagada (3 de marzo, $400).
  - Mención de un creador grande (12 de marzo).

Con eso, decir “la secuencia funcionó” es confundir correlación con causalidad.

---

## Por qué no se puede atribuir el resultado a los emails

### 1. Hay tres intervenciones simultáneas y no hay grupo de control
Emails, ads e influencer ocurrieron en el mismo mes. Sin un **grupo de control** o **holdout** que no haya recibido la secuencia, no hay forma de separar qué parte del cambio vino de cada cosa.

Podría ser que:

- Todo el mérito sea de los emails.
- Todo el mérito sea de los ads.
- Todo el mérito sea del influencer.
- Los emails no hicieron nada y el aumento vino de que los ads/influencer atrajeron más tráfico.
- El aumento sea ruido/estacionalidad.

Todas esas historias son compatibles con los números que tienes.

### 2. El MRR no es la métrica correcta para evaluar una secuencia a usuarios gratuitos
La secuencia iba dirigida a **usuarios del plan gratuito**. Para evaluarla, la métrica relevante no es el MRR total, sino algo como:

- Tasa de conversión de **free → pago**.
- Cuántos upgrades vinieron de usuarios que recibieron los emails.
- MRR incremental de esos upgrades y su retención.

El MRR agregado puede subir por muchas razones que nada tienen que ver con los emails:

- Menos churn en marzo.
- Clientes actuales subiendo de plan.
- Pagos anuales o prepagos mal normalizados.
- Cambios de precio.
- Reactivaciones.

Además, **14 altas no explican por sí solas +$1.200 de MRR** salvo que el ARPU sea muy alto. Si el ingreso medio por usuario fuera, por ejemplo, $29/mes, 14 altas nuevas aportarían solo ~$406. Entonces, ¿de dónde salieron los otros ~$794? Sin un desglose de **New / Expansion / Contraction / Churn**, no se sabe.

### 3. Las “14 altas” no están segmentadas
“Altas al plan pago” es un número agregado. No sabes:

- Cuántas de esas 14 altas eran **usuarios gratuitos que recibieron los emails**.
- Cuántas fueron **registros directos** desde los anuncios o desde el video del creador.
- Cuántas habrían convertido igual sin los emails.
- Cuál es el **tamaño de la base de usuarios free** (el denominador).

Si, por ejemplo, 10 de las 14 altas vinieron del influencer o de los ads, y solo 4 eran upgrades de usuarios free, el impacto de la secuencia es mucho menor de lo que parece.

### 4. Los ads y el influencer pudieron inflar el embudo free
Aunque la secuencia sea para usuarios free, los anuncios y el video pudieron atraer **más usuarios gratuitos**. Si entra más gente al plan free, pueden subir las altas absolutas aunque la **tasa de conversión** no haya mejorado.

Peor aún: si un usuario vio el video del creador y luego se hizo free, recibió tus emails y después pagó, ¿la conversión fue por el email o por el video? Con estos datos no se puede distinguir.

### 5. El aumento de altas es pequeño y cabe dentro del ruido
Pasar de 9 a 14 altas suena a mejora, pero:

- Febrero tiene 28 días; marzo, 31.
- Tasa diaria febrero: 9/28 = **0,32 altas/día**.
- Tasa diaria marzo: 14/31 = **0,45 altas/día**.
- Si marzo hubiera mantenido la tasa de febrero, esperarías ~10 altas, no 9.

El exceso real es de unas **4 altas**. Con números tan bajos, eso entra perfectamente dentro de la variación aleatoria. Una prueba de Poisson daría un p-value de una cola en torno a **0,07–0,13** según cómo ajustes; en dos colas es aún más alto. Es decir: **ni siquiera es un aumento estadísticamente claro**, y mucho menos atribuible a una causa específica.

---

## Qué haría falta para estar seguros

Para poder decir “la secuencia funcionó” con honestidad, necesitarías esto:

### 1. Definir la métrica correcta
Si el objetivo era convertir usuarios free en pagos, mide:

- **Tasa de conversión free → pago**.
- Número de upgrades desde free.
- MRR generado por esos upgrades y retención a 30/60/90 días.

No uses MRR total como si fuera una métrica de conversión.

### 2. Datos desagregados
Necesitas, como mínimo:

- Cuántos usuarios free había y cuántos nuevos entraron en marzo.
- Cuántos recibieron/abrieron/hicieron clic en cada email.
- Cuántas de las 14 altas eran upgrades desde free vs altas directas.
- ARPU por plan y desglose de movimiento de MRR: New, Expansion, Contraction, Churn, Reactivation.
- Histórico de al menos 6–12 meses para saber si 9 o 14 es normal o estacional.

### 3. Tracking y atribución
Cada alta pagada debería poder rastrearse:

- ¿Vino de un anuncio? UTM, campaña, clic.
- ¿Vino del video del creador? Tráfico referido, landing específica, pico de visitas.
- ¿Vino de un email? Enlace con UTM, apertura/clic registrada, fecha de upgrade.
- ¿Era usuario free? Fecha de registro free, si recibió la secuencia, en qué momento convirtió.

Sin eso, todo es especulación.

### 4. Un experimento o grupo de control
La forma más limpia de saberlo:

- **A/B test / holdout**: divides aleatoriamente a los usuarios free en dos grupos:
  - Tratamiento: reciben la secuencia.
  - Control: no la reciben, o reciben la comunicación anterior.
  
  Ads e influencer deben afectar a ambos grupos por igual. Luego comparas tasa de conversión y MRR por usuario.

Si no puedes hacer un holdout total, alternativas:

- **Staggered rollout**: lanzas la secuencia solo a una cohorte y no a otra.
- **Switchback**: días con secuencia vs días sin secuencia.
- **Diferencia en diferencias**: comparas el cambio antes/después en usuarios tratados vs no tratados.
- Aprovechar un grupo no expuesto, por ejemplo usuarios que no recibieron emails por un error técnico.

Importante: con 9–14 conversiones al mes, la muestra es muy pequeña. Necesitarás mucho volumen o varias semanas/meses para tener potencia estadística. Si no llegas a esa potencia, la respuesta seguirá siendo “no se puede saber con precisión”.

### 5. Análisis estadístico honesto
- Intervalos de confianza, no solo “subió”.
- Test de significación.
- Corrección por mirar varias métricas a la vez.
- Series temporales diarias con marcas claras: 1 de marzo, 3 de marzo y 12 de marzo. Si el salto ocurre después del 12, apunta al influencer. Si ocurre después del 3, a los ads. Si no hay movimiento hasta después de esas fechas, los emails no explican el cambio.

---

## Qué decirle al equipo

Algo así:

> “En marzo subieron las altas y el MRR, pero lanzamos la secuencia de emails, empezamos a pagar publicidad y nos mencionó un creador grande casi al mismo tiempo. Sin grupo de control ni tracking por origen, **no podemos atribuir ese crecimiento a la secuencia de emails**. Podría haber ayudado, pero no hay evidencia sólida. Antes de escalarla o descartarla, propongo montar un test A/B con holdout yTracking UTM para aislar el efecto.”

Esa es la conclusión responsable. **No celebren todavía.**