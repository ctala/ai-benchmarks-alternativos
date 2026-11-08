# Qwen 3.8 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 37.585s | tokens_per_second: 114.6
- input_tokens: 283 | output_tokens: 4309

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

## Mi conclusión

**No se puede saber con estos datos que la secuencia de emails haya funcionado.**  
Lo que sí se puede decir es que **marzo fue mejor que febrero en MRR y altas**, pero hay al menos tres explicaciones plausibles y no puedes atribuir el resultado a los emails.

Dicho de forma simple: **hay una señal positiva, pero no hay evidencia causal.**

---

## Lo que muestran los números

- MRR: $4.100 → $5.300  
  - **+ $1.200**
  - **+29%**

- Altas a plan pago: 9 → 14  
  - **+5 altas**
  - **+55,6%**

Parece bueno. Pero con estos números no puedes decir “la secuencia de emails funcionó”, porque:

1. **Empezaste publicidad el 3 de marzo.**
2. **Un creador grande te mencionó el 12 de marzo.**
3. **La subida de 9 a 14 altas es una diferencia pequeña.**  
   Con tan pocos eventos, +5 altas puede ser ruido, estacionalidad, suerte o efecto de otro canal.

Matemáticamente, la subida de 9 a 14 altas no es estadísticamente robusta por sí sola. Es una mejora posible, pero no una prueba.

---

## Por qué no alcanza con el MRR

El MRR subió $1.200, pero el MRR es una métrica agregada. Puede subir por:

- Nuevas suscripciones.
- Upgrades de usuarios existentes.
- Menos cancelaciones que en febrero.
- Un usuario nuevo pagando más caro.
- Un plan anual que entra como MRR.
- Un descuento que venció.
- Publicidad.
- La mención del creador.
- Los emails.
- Una combinación de todo.

Si no tienes el **puente de MRR**, no sabes de dónde vienen esos $1.200.

Ejemplo:  
Si el plan pago promedio cuesta $85, 14 altas nuevas darían aproximadamente $1.190 de MRR nuevo, casi exactamente el +$1.200. Pero eso no prueba nada, porque podría haber habido churn, expansiones o cambios de precio.

---

## El problema central: no hay grupo de control

Para decir que una campaña funcionó, necesitas comparar:

- Qué pasó con quienes **recibieron** los emails.
- Qué habría pasado con personas similares que **no los recibieron**.

Si lanzaste la secuencia a todos los usuarios gratuitos, no tienes contrafactual. No sabes cuántos habrían subido igual sin los emails.

Además, la publicidad y la mención del creador son eventos externos que pueden haber generado tráfico, registro y conversión por sí solos.

---

## Qué haría falta para estar seguros

### 1. Fechas exactas de las 14 altas

Necesitarías saber cuándo ocurrió cada alta.

Por ejemplo:

| Fecha de alta | ¿Viene de tráfico nuevo? | ¿Viene de usuario gratuito existente? | ¿Recibió emails? |
|---|---|---|---|
| 2 marzo | No | Sí | Sí |
| 4 marzo | Sí, ads | No | No |
| 13 marzo | Sí, creador | No | No |
| 15 marzo | Sí, creador | Sí | Sí |

Si la mayoría de altas ocurrieron después del 12 de marzo, es más probable que la mención haya tenido peso.  
Si muchas ocurrieron entre el 1 y el 12 de marzo, los emails podrían tener algo que ver, pero aún así necesitarías más datos.

---

### 2. Atribución por fuente

Necesitarías saber de dónde vino cada usuario que pagó:

- Orgánico.
- Directo.
- Publicidad.
- Video del creador.
- Email.
- Referido.
- Tráfico nuevo vs existente.

Si no sabes la fuente, no puedes asignar crédito.

---

### 3. Cohortes claras

Deberías separar:

- Usuarios gratuitos que ya estaban en la base el 1 de marzo.
- Usuarios gratuitos que entraron por publicidad.
- Usuarios gratuitos que entraron por la mención.
- Usuarios gratuitos que entraron orgánicamente.
- Usuarios que recibieron la secuencia completa.
- Usuarios que no recibieron la secuencia.

La pregunta correcta no es “¿subieron las altas en marzo?”, sino:

> “¿Qué tasa de conversión tuvo la cohorte expuesta a los emails comparada con cohortes similares no expuestas?”

---

### 4. Métricas de la secuencia de emails

Para evaluar los emails, necesitarías:

- Emails enviados.
- Emails entregados.
- Tasa de apertura.
- Tasa de clics.
- Clics hacia la página de pago.
- Personas que hicieron checkout.
- Personas que pagaron.
- Tiempo desde apertura/clic hasta pago.
- Respuestas o objeciones.

Si la secuencia no generó clics ni conversaciones, difícilmente fue el motor principal.

---

### 5. MRR neto por cohort

No solo MRR total. Necesitarías:

- MRR nuevo por fuente.
- MRR perdido por cancelaciones.
- MRR perdido por downgrades.
- MRR ganado por upgrades.
- MRR reactivado.

Ejemplo de puente de MRR:

```text
MRR febrero: $4.100
+ MRR nuevas suscripciones: $1.300
- MRR cancelaciones: -$100
+ MRR upgrades: $100
MRR marzo: $5.300
```

Si no tienes esto, el +29% es solo una foto final, no una explicación.

---

## Qué te diría si tuvieras que comunicar al equipo

Yo no escribiría:

> “La secuencia de emails funcionó y generó +29% de MRR”.

Escribiría algo como:

> “En marzo aumentamos MRR de $4.100 a $5.300 y las altas pasaron de 9 a 14. Lanzamos una secuencia de emails, pero también activamos publicidad y recibimos una mención de un creador grande. Por ahora no podemos atribuir el crecimiento a los emails. Necesitamos datos por fecha, fuente, cohorte y conversión para saber qué funcionó.”

Eso protege a la empresa de tomar decisiones con una causa equivocada.

---

## Si tuvieras que apostar con lo que tienes

Con la información actual, mi lectura sería:

- **Es posible que los emails hayan ayudado.**
- **Pero no hay evidencia suficiente para afirmar que funcionaron.**
- **La mención del creador y la publicidad son explicaciones igualmente o más plausibles.**
- **El crecimiento parece bueno, pero la causa no está clara.**

Si tuviera que ordenar probabilidades de forma intuitiva, sin datos nuevos:

1. La mención del creador puede haber sido un driver importante.
2. La publicidad puede haber aumentado tráfico y registros.
3. Los emails pueden haber convertido parte de esa atención.
4. El crecimiento podría ser una combinación de los tres.

Pero esto es una hipótesis, no una conclusión.

---

## Lo mínimo que necesitaría para darte una respuesta más segura

Pásame estos datos y puedo ayudarte a acercarnos:

### Sobre las altas

Para cada una de las 14 altas de marzo:

- Fecha exacta.
- Plan contratado.
- Precio.
- Si venía de un usuario gratuito existente o de un registro nuevo.
- Fuente de tráfico: email, ads, YouTube, orgánico, directo, otro.
- Si había recibido los emails antes de pagar.
- Si abrió o hizo clic en algún email.

### Sobre la secuencia de emails

- Cuántos usuarios gratuitos recibieron la secuencia.
- Cuántos emails se enviaron.
- Entregabilidad.
- Aperturas.
- Clics.
- Clics a checkout.
- Conversión post-clic.
- Si la secuencia se aplicaba también a usuarios gratuitos nuevos.

### Sobre el MRR

- MRR inicial y final por componente.
- Nuevas suscripciones.
- Cancelaciones.
- Downgrades.
- Upgrades.
- Reactivaciones.
- Precio promedio por plan.
- Si hubo promociones, descuentos o cambios de precio.

### Sobre publicidad y creador

- Gasto publicitario por día.
- Clics.
- Impresiones.
- Registros gratuitos generados.
- Conversión a pago.
- Tráfico después del video del creador.
- Registros gratuitos después del video.
- Altas después del video.

---

## Cómo deberías haberlo medido

La forma más limpia habría sido un A/B test:

- Tomar usuarios gratuitos elegibles.
- Dividirlos al azar.
- 50% recibe la secuencia de emails.
- 50% no la recibe.
- Comparar conversión a pago en los siguientes 14 o 30 días.

Métrica principal:

> **Tasa de conversión de gratuito a pago por cohorte.**

No usar solo MRR total, porque está contaminado por churn, expansiones, precio y canales nuevos.

---

## Qué haría yo ahora

Si ya lanzaste todo junto, no te recomiendo matar la secuencia ni celebrarla todavía.

Haría esto:

1. **Exportar las 14 altas de marzo con fecha y fuente.**
2. **Marcar cuáles vinieron de usuarios gratuitos existentes.**
3. **Marcar cuáles vinieron de tráfico nuevo.**
4. **Cruzar con el envío de emails.**
5. **Ver si hay un pico de altas después del 12 de marzo.**
6. **Revisar si la publicidad generó registros antes que pagos.**
7. **Construir un puente de MRR.**
8. **Diseñar el próximo test con grupo de control.**

---

## Resumen final

**No se puede decir que la secuencia de emails funcionó con estos datos.**

Hay crecimiento, sí. Pero el crecimiento coincide con al menos dos eventos importantes: publicidad y una mención externa. Además, el número de altas es pequeño y el MRR total no separa causas.

Lo honesto es decir:

> “Marzo mejoró, pero todavía no sabemos si la secuencia de emails fue la causa. Necesitamos atribución por fecha, fuente, cohorte y conversión para confirmar o descartarlo.”