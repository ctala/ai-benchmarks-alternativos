# Qwen 3.8 Max — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.98 | quality: 10.0
- latency_total: 208.275s | tokens_per_second: 35.3
- input_tokens: 283 | output_tokens: 7346

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

Conclusión corta: **con estos datos no se puede saber si la secuencia de emails funcionó**.

Lo que sí puedes decir es:

> “En marzo aumentó el MRR y aumentaron las altas de pago respecto a febrero, y eso coincidió con el lanzamiento de una secuencia de emails, una campaña de publicidad y una mención de un creador grande”.

Pero eso es una **correlación**, no una prueba de causalidad.

No puedes afirmar todavía:

> “La secuencia de emails generó el aumento de MRR”.

Ni tampoco:

> “La secuencia no funcionó”.

Simplemente, **no hay evidencia suficiente para atribuir el resultado a los emails**.

---

## Por qué no se puede concluir todavía

### 1. Hubo varias acciones al mismo tiempo

En marzo pasaron al menos tres cosas:

| Fecha | Acción |
|---|---|
| 1 de marzo | Activaste secuencia de 5 emails |
| 3 de marzo | Empezaste a pagar publicidad |
| 12 de marzo | Un creador grande mencionó la comunidad |

Si el MRR subió, podría deberse a:

- la secuencia de emails;
- la publicidad;
- la mención del creador;
- una combinación de las tres;
- estacionalidad;
- azar;
- cambios en churn, upgrades, precios o planes;
- usuarios que ya iban a pagar igualmente.

Con datos mensuales agregados, no puedes separar esas causas.

---

### 2. El MRR total no mide específicamente el efecto de los emails

El MRR pasó de:

- **$4.100** al 28 de febrero;
- **$5.300** al 31 de marzo.

Eso es un aumento de:

- **$1.200**;
- **+29%**.

Pero el MRR puede subir por muchas razones:

- nuevos usuarios pagos;
- upgrades de plan;
- menor cancelación;
- recuperación de usuarios que habían dejado de pagar;
- cambios de precio;
- planes anuales contabilizados de forma distinta;
- expansión dentro de cuentas existentes;
- menor churn que en febrero.

Para saber si los emails funcionaron, necesitas medir específicamente la conversión de **usuarios gratuitos a pago**, idealmente de usuarios que recibieron la secuencia.

---

### 3. Las altas de pago subieron, pero la muestra es pequeña

Tienes:

- febrero: **9 altas**;
- marzo: **14 altas**.

Además, febrero tuvo 28 días y marzo tuvo 31 días.

Si lo miras por día:

- febrero: 9 / 28 = **0,32 altas/día**;
- marzo: 14 / 31 = **0,45 altas/día**.

Sí, hay una mejora, pero con tan pocos datos puede haber ruido. Cinco altas adicionales pueden ser importantes para una empresa pequeña, pero estadísticamente no bastan para afirmar que una causa específica produjo el cambio.

---

### 4. Falta el contrafactual

La pregunta correcta no es solo:

> “¿Subió el MRR después de lanzar los emails?”

La pregunta correcta es:

> “¿Qué habría pasado con esos usuarios si no hubieran recibido la secuencia de emails?”

Para responder eso necesitas comparar contra algo:

- un grupo que no recibió los emails;
- un grupo similar en semanas anteriores;
- una cohorte comparable;
- un modelo con datos diarios y controles por publicidad y mención del creador.

Sin contrafactual, no hay atribución confiable.

---

## Qué haría falta para estar seguros

Para poder decir con más confianza si la secuencia funcionó, necesitarías al menos uno de estos enfoques, idealmente más de uno.

---

## 1. Experimento con grupo de control

Esta es la forma más limpia.

Para futuros lanzamientos, podrías hacer esto:

1. Tomas usuarios del plan gratuito elegibles para recibir la secuencia.
2. Los divides aleatoriamente en dos grupos:
   - **Grupo A**: recibe la secuencia de 5 emails.
   - **Grupo B**: no recibe la secuencia, o recibe una versión mínima/control.
3. Mides durante 30, 60 o 90 días:
   - cuántos usuarios pasan a pago;
   - cuánto MRR generan;
   - si se mantienen pagando.

La métrica principal sería algo como:

> Tasa de conversión de gratuito a pago.

Por ejemplo:

| Grupo | Usuarios gratuitos | Conversiones a pago | Tasa |
|---|---:|---:|---:|
| Con emails | 500 | 25 | 5% |
| Sin emails | 500 | 15 | 3% |

Ahí podrías estimar un lift:

> 5% - 3% = 2 puntos porcentuales de incremento atribuible a la secuencia.

Y luego traducirlo a MRR incremental.

Sin grupo de control, es mucho más difícil defender que el efecto fue real.

---

## 2. Datos a nivel usuario, no solo totales mensuales

Necesitas poder seguir a cada usuario.

Idealmente, una tabla con algo así:

| Usuario | Plan inicial | Fecha de alta free | Recibió emails | Abrió emails | Hizo clic | Fuente de adquisición | Fecha de conversión | MRR |
|---|---|---|---|---|---|---|---|---:|

Con eso puedes responder preguntas como:

- ¿Los que pagaron en marzo eran usuarios gratuitos existentes?
- ¿Habían recibido la secuencia?
- ¿Pagaron después de abrir o hacer clic en algún email?
- ¿Venían de publicidad?
- ¿Venían de la mención del creador?
- ¿Se registraron antes o después del 12 de marzo?
- ¿La conversión ocurrió después del email 1, 2, 3, 4 o 5?

Sin datos a nivel usuario, solo tienes una foto agregada.

---

## 3. Atribución de fuente de adquisición

Necesitas saber de dónde vinieron las 14 altas de marzo.

Por ejemplo:

| Fuente | Altas de marzo |
|---|---:|
| Usuarios free existentes que recibieron emails | ? |
| Tráfico de publicidad | ? |
| Tráfico del creador | ? |
| Orgánico | ? |
| Referidos | ? |
| Desconocido | ? |

Si descubres que la mayoría de las 14 altas vinieron de usuarios que ya estaban en el plan gratuito y que además recibieron/abrieron/ clickearon la secuencia, la hipótesis de los emails se fortalece.

Si descubres que la mayoría vino directamente de la campaña pagada o de la mención del creador, entonces la secuencia probablemente no fue la causa principal.

Para eso necesitas:

- UTMs;
- códigos de campaña;
- enlaces específicos;
- cupones del creador;
- páginas de aterrizaje separadas;
- encuestas de onboarding tipo: “¿Cómo conociste la comunidad?”;
- eventos de analytics bien configurados.

---

## 4. Desglose del MRR

El aumento de MRR de $1.200 debería descomponerse así:

| Componente | MRR |
|---|---:|
| MRR inicial | $4.100 |
| Nuevo MRR por altas | ? |
| Expansión de usuarios existentes | ? |
| Contracción / downgrades | ? |
| Churn / cancelaciones | ? |
| Reactivaciones | ? |
| MRR final | $5.300 |

Si no sabes cuánto del aumento vino de nuevas altas, expansión o menor churn, no puedes conectarlo limpiamente con la secuencia.

---

## 5. Comparación por cohortes

Si no puedes hacer un experimento, una alternativa razonable es comparar cohortes.

Por ejemplo:

- usuarios gratuitos registrados en enero;
- usuarios gratuitos registrados en febrero;
- usuarios gratuitos registrados en marzo;
- usuarios gratuitos registrados en abril.

Luego mides:

- cuántos convierten a pago;
- cuántos días tardan;
- qué fuente tenían;
- si recibieron emails;
- si estuvieron expuestos a publicidad o al creador.

Pero ojo: esto solo ayuda si las cohortes son comparables. Si marzo recibió tráfico nuevo por el creador o por publicidad, la cohorte de marzo puede ser muy distinta a la de febrero.

---

## 6. Serie de tiempo diaria

Con datos diarios podrías ver mejor el patrón.

Por ejemplo:

| Fecha | Altas free | Altas pago | Evento |
|---|---:|---:|---|
| 1 mar | ? | ? | Lanzamiento emails |
| 2 mar | ? | ? |  |
| 3 mar | ? | ? | Inicio ads |
| 4 mar | ? | ? |  |
| 12 mar | ? | ? | Mención creador |
| 13 mar | ? | ? |  |

Con eso podrías observar si el salto ocurre:

- justo después de los emails;
- justo después de los ads;
- justo después del creador;
- de forma gradual;
- en varios picos.

Aun así, con solo dos meses y eventos simultáneos, una serie temporal no resuelve todo. Pero ayudaría mucho más que comparar solo febrero contra marzo.

---

## Qué análisis rápido puedes hacer ya con lo que tienes

Si quieres una primera aproximación, te recomendaría revisar estas preguntas concretas.

### 1. ¿Quiénes fueron las 14 altas de marzo?

Clasifícalas en:

- usuarios que ya estaban en plan gratuito antes de marzo;
- usuarios nuevos que llegaron en marzo;
- usuarios que llegaron por publicidad;
- usuarios que llegaron por el creador;
- usuarios que llegaron por orgánico u otros canales.

Si las 14 altas son usuarios nuevos que llegaron después del 12 de marzo por la mención del creador, no puedes atribuirlo a la secuencia.

Si son usuarios gratuitos antiguos que recibieron los emails, la hipótesis mejora.

---

### 2. ¿Esos usuarios recibieron y abrieron los emails?

No basta con que “estuvieran en la lista”.

Necesitas ver:

- email enviado;
- email entregado;
- email abierto;
- link clickeado;
- fecha/hora del clic;
- fecha/hora de la conversión.

Si un usuario pagó antes de recibir el primer email, no puede atribuirse a la secuencia.

Si pagó después de hacer clic en el email 3 o 4, hay más plausibilidad.

Pero incluso ahí hay sesgo: los usuarios que abren emails suelen ser más activos o estar más interesados. Por eso el grupo de control sigue siendo importante.

---

### 3. ¿La conversión ocurrió cerca de algún email?

Puedes revisar algo como:

| Usuario | Email abierto | Clic | Conversión | Días entre clic y pago |
|---|---|---|---|---:|
| Usuario 1 | Email 2 | Sí | Sí | 1 día |
| Usuario 2 | Email 4 | Sí | Sí | 2 días |
| Usuario 3 | Ninguno | No | Sí | ? |

Si muchas conversiones ocurren poco después de clics concretos, es una señal. Pero no prueba causalidad por sí sola.

---

### 4. ¿Hubo un pico después del creador?

Revisa las altas diarias desde el 12 de marzo.

Si ves un salto fuerte justo después del 12, el creador puede explicar buena parte del aumento.

Si el aumento fue previo y sostenido desde el 1-3 de marzo, podría ser más consistente con emails o ads, aunque todavía sin prueba clara.

---

## Qué métricas deberías usar para evaluar la secuencia

No evalúes la secuencia solo por MRR total. Para una secuencia dirigida a usuarios gratuitos, las métricas más adecuadas serían:

### Métricas principales

1. **Tasa de conversión de free a pago**  
   Ejemplo:

   > Usuarios gratuitos que reciben la secuencia y se vuelven de pago en 30 días.

2. **MRR incremental por usuario expuesto**  
   Ejemplo:

   > MRR adicional generado por usuarios que recibieron la secuencia, comparado con un grupo de control.

3. **Tiempo hasta conversión**  
   ¿Pagan después del email 1, 3 o 5?

4. **Retención posterior**  
   No sirve si pagan un mes y luego se van.

---

### Métricas secundarias

- tasa de apertura;
- tasa de clic;
- tasa de baja;
- clics por email;
- conversión por email;
- ingresos por usuario expuesto;
- costo de herramientas de email;
- comparación contra usuarios no expuestos.

Pero ojo: apertura y clic no prueban causalidad. Solo muestran interés.

---

## Cómo saber si realmente “funcionó”

Para decir que funcionó, yo pediría ver algo como esto:

### Escenario ideal

- Tienes un grupo de control aleatorio.
- La secuencia aumenta la conversión de free a pago.
- El aumento es consistente durante varias semanas.
- El MRR incremental supera el costo de la secuencia.
- Los usuarios convertidos se mantienen pagando.
- El efecto sigue existiendo después de descontar tráfico de ads y del creador.

Ejemplo de conclusión válida:

> “Entre usuarios gratuitos similares, los que recibieron la secuencia convirtieron un 4,2% a pago en 30 días, frente a 2,1% del grupo control. El lift estimado es de 2,1 puntos porcentuales, generando aproximadamente $X de MRR incremental”.

Eso sí sería una conclusión defendible.

---

## Mi recomendación práctica

No tomes decisiones fuertes todavía con esta información.

Yo haría esto:

### Paso 1: Auditoría rápida de las 14 altas de marzo

Clasifica cada alta por:

- fecha;
- origen;
- si era usuario free previo;
- si recibió emails;
- si abrió/clickeó;
- si pagó después de un email;
- si vino de ads;
- si vino del creador.

Eso te dará una primera señal.

---

### Paso 2: No atribuyas todo el MRR a los emails

Por ahora, la conclusión más honesta es:

> “Marzo creció, pero no sabemos cuánto de ese crecimiento vino de la secuencia de emails”.

---

### Paso 3: Diseña una prueba para la próxima cohorte

Para nuevos usuarios gratuitos, reserva un porcentaje como control.

Por ejemplo:

- 80% recibe la secuencia;
- 20% no recibe la secuencia o recibe una versión reducida.

Luego comparas conversión a 30 o 60 días.

Si no puedes dejar usuarios sin emails por temor a perder ingresos, puedes hacer una prueba más pequeña o por tiempo limitado, pero necesitas algún grupo de comparación.

---

### Paso 4: Define qué significa “funcionar”

Antes de medir, define el criterio.

Por ejemplo:

> “La secuencia funciona si aumenta la conversión de free a pago en al menos 1 punto porcentual y genera MRR incremental suficiente para justificar el costo y esfuerzo”.

Sin ese criterio, cualquier subida puede parecer éxito y cualquier bajada puede parecer fracaso.

---

## Respuesta final

Con los datos que tienes ahora:

> **No se puede afirmar que la secuencia de emails automáticos funcionó.**

Lo que sí puedes decir es:

> “Hubo una mejora en MRR y altas durante marzo, pero coincide con otras dos acciones importantes: publicidad y mención de un creador. Además, los datos están agregados por mes y no permiten aislar el efecto de los emails”.

Para estar seguros, necesitarías:

1. datos por usuario;
2. atribución de fuente;
3. desglose del MRR;
4. comparación con grupo de control o cohorte comparable;
5. seguimiento de conversiones después de cada email;
6. idealmente, un experimento aleatorio con usuarios que no reciban la secuencia.

Mi conclusión operativa sería:

> “La secuencia puede haber ayudado, pero con esta evidencia no podemos saberlo. Antes de escalarla o atribuirle el crecimiento, hay que instrumentar mejor y probarla con un grupo de control”.