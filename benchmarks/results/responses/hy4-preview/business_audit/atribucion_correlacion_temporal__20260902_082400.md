# Tencent Hy4 preview — business_audit/atribucion_correlacion_temporal

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 212.271s | tokens_per_second: 58.0
- input_tokens: 256 | output_tokens: 12321

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

## Conclusión: **no se puede saber**

Con estos datos **no podés afirmar que la secuencia de emails funcionó**. Lo único que mostrás es que **marzo fue mejor que febrero** en dos métricas agregadas:

- MRR: **$4.100 → $5.300 (+$1.200, +29%)**
- Altas al plan pago: **9 → 14 (+5 altas)**

Pero en marzo pasaron **tres cosas al mismo tiempo**:

1. **1 de marzo**: arrancó la secuencia de emails a usuarios gratuitos.
2. **3 de marzo**: empezaste a pagar publicidad ($400).
3. **12 de marzo**: un creador grande mencionó la comunidad.

Sin aislar esas variables, **cualquier conclusión de atribución es falsa o, como mínimo, injustificada**.

---

## Por qué los números no alcanzan

### 1. Hay confusión total entre canales
No sabés de dónde salieron las 14 altas de marzo. Necesitás saber si vinieron de:

- usuarios que **ya estaban en el plan gratuito antes del 1/3** (los únicos que recibieron la secuencia, si fue solo una campaña a la base existente);
- usuarios **nuevos** que entraron por publicidad a partir del 3/3;
- usuarios **nuevos** que llegaron por el influencer a partir del 12/3.

Si la mayoría de las conversiones ocurrieron **después del 12 de marzo**, es mucho más probable que el salto venga del influencer o de los ads que de los emails. Si ocurrieron entre el 1 y el 3, los emails son candidatos, pero aun así no descartás que esos usuarios también vieran el video o los anuncios.

### 2. MRR no es “altas × precio”
El aumento de **$1.200 de MRR** no es lo mismo que “14 altas nuevas”. El MRR neto se mueve así:

> MRR nuevo (altas) **+** expansión **−** contracción **−** churn

No me diste:

- el precio / ARPU de los planes;
- si las altas fueron mensuales o anuales;
- cuánto MRR se fue por bajas;
- si hubo upgrades de clientes que ya pagaban.

Un chequeo rápido: **si no hubo expansión** (upgrades de clientes actuales), el MRR nuevo que aportaron las 14 altas tuvo que ser de **al menos ~$86 por alta** ($1.200 / 14), y **más alto si hubo bajas**. Si tu plan cuesta menos que eso, las 14 altas **no alcanzan** para explicar el +29% y el resto salió de expansión, menor churn u otros factores. Si hubo expansión, las altas pudieron aportar menos. Como no tengo el desglose, **no puedo cerrar ese cálculo**.

### 3. El dato “9 vs 14 altas” no mide el impacto de la secuencia
El MRR de marzo **no crece por tener 5 altas más que febrero**. Crece por el MRR de las 14 altas de marzo y por la retención de la base. Las 9 altas de febrero ya estaban incluidas en el MRR del 28/2. Comparar 9 vs 14 solo te dice que **adquiriste más usuarios**, no que los emails hayan sido la causa.

### 4. No hay métricas de la secuencia
No mencionaste:

- cuántos emails se entregaron;
- cuántos se abrieron;
- cuántos se clickearon;
- cuántos convirtieron por email;
- cuántos se dieron de baja o marcaron spam.

Si nadie abrió los emails, **es imposible que hayan generado conversiones**. Sin el embudo de la secuencia, no hay evidencia de mecanismo.

### 5. Muestra chica y sin línea base
Pasar de 9 a 14 altas es una diferencia de **5 conversiones**. Sin historia de varios meses no sabemos si:

- febrero fue un mes malo;
- marzo suele ser estacionalmente mejor;
- esa diferencia es real o es ruido estadístico.

Con 5 altas de diferencia, **cualquier test serio tiene muy poco poder estadístico**.

---

## Qué haría falta para estar seguros

Para poder decir “la secuencia funcionó” (o “no funcionó”), necesitás esto:

### 1. Atribución por canal de cada alta
Saber, para cada una de las 14 altas de marzo:

- qué canal la generó: email, ads, influencer, orgánico, directo;
- si el usuario **ya era gratuito antes del 1/3** o entró después;
- fecha exacta de conversión.

Con UTMs, códigos de descuento, links distintos por canal o una pregunta en el onboarding ya podés separar bastante.

### 2. Cohorte y grupo de control
Definí la cohorte: **todos los usuarios gratuitos activos el 1/3 que recibieron la secuencia**.

Después necesitás un **grupo de control**: usuarios gratuitos aleatorios que **no** recibieron la secuencia (o recibieron una versión neutra), mientras ads e influencer seguían activos para todos. La diferencia en conversión a pago entre ambos grupos es la única forma limpia de medir causalidad.

### 3. Embudo de la secuencia
Métricas por cada uno de los 5 emails:

- entregados;
- abiertos;
- clics;
- conversiones a pago;
- desuscripciones / quejas de spam.

Si el email 1 tuvo 2% de apertura y 0 clics, la secuencia no funcionó, por más que el MRR haya subido.

### 4. Waterfall de MRR de febrero y marzo
Un informe de movimientos de MRR:

- New MRR;
- Expansion MRR;
- Contraction MRR;
- Churned MRR;
- Reactivation MRR.

Así sabés si el +$1.200 vino de nuevas altas, de que se fueron menos clientes, o de upgrades.

### 5. Datos diarios
Altas, churn y MRR por día. Si ves que las conversiones se concentran después del 12/3, el influencer gana peso. Si se concentran justo después de cada email, la secuencia gana peso. Sin daily data, estás mirando un promedio mensual que esconde todo.

### 6. Línea base histórica
Al menos 3–6 meses de:

- altas mensuales;
- tasa de conversión de gratuito a pago;
- churn;
- MRR y sus movimientos.

Para saber si 14 altas y +29% MRR son una anomalía o algo normal.

### 7. Definir qué significa “funcionó”
¿Es más conversiones absolutas? ¿Mayor tasa de conversión de la base gratuita? ¿MRR incremental? ¿ROI positivo? Hoy el objetivo no está definido, así que el éxito tampoco.

---

## Qué podés decir hoy con honestidad

Podés decir:

> “En marzo crecimos en MRR y en altas frente a febrero, pero no puedo atribuir ese crecimiento a la secuencia de emails porque al mismo tiempo lancé publicidad y nos mencionó un influencer. Los datos actuales no permiten aislar el efecto de los emails.”

Y, si querés una **hipótesis no comprobada**: es compatible que la secuencia haya aportado algo, pero el salto de **+$1.200 de MRR** parece grande para explicarlo solo con 14 altas brutas si tu ARPU no es alto; por eso, **el crecimiento probablemente se explica más por la suma de ads + influencer + retención/expansión que por los emails**. Pero **no actúes sobre esta hipótesis**: todavía no está respaldada por datos.

**Recomendación:** no escales ni descartes la secuencia todavía. Implementá atribución por canal, mirá las fechas de las 14 altas y, si podés, hacé un A/B test con holdout antes de volver a lanzar la secuencia junto con otras campañas grandes.