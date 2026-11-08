# GLM 5.3 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 45.193s | tokens_per_second: 66.2
- input_tokens: 138 | output_tokens: 2994

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, tu lectura tiene dos errores que se refuerzan entre sí. Vamos por partes.

## Qué significa realmente ese 114%

Ese número es casi seguro **Net Revenue Retention (NRR)**: ingresos del mes actual generados por *clientes que ya tenías*, comparados con los ingresos de ese mismo grupo el mes pasado. Que sea 114% significa que la expansión (upgrades) superó a la pérdida por churn y downgrades. Se llama "churn neto de ingresos negativo".

Lo que **no** significa es que no se te vaya nadie.

## Lo que dicen tus números reales

- **Retención de clientes (logo retention): 90% mensual.** Perdiste 4 de 40 clientes. Eso es 10% de churn mensual. Si se mantuviera constante, en un año conservarías 0,9¹² ≈ 28% de tu base: perderías ~72% de los clientes.
- **El ARPU de los sobrevivientes subió ~27%.** (1,14 × 40/36 ≈ 1,267). Los que se quedaron pagan bastante más que el promedio anterior.
- **Corolario incómodo:** los 4 que se fueron eran clientes de gasto por debajo del promedio. Tu ingreso se está concentrando en menos manos.

## Por qué no puedes dejar de preocuparte por el churn

1. **El NRR depende de la base de expansión.** Los upgrades vienen de tus clientes actuales. Con 10% de churn mensual, esa base se encoge y el motor de expansión se queda sin combustible.
2. **Riesgo de concentración.** Si pocos clientes grandes explican el salto, que uno de ellos se vaya te duelen desproporcionadamente. El 114% de este mes puede ser frágil.
3. **Tu GRR sigue siendo menor a 100%.** El *Gross* Revenue Retention (sin contar expansión) nunca puede superar 100%, y perdiste clientes: tu GRR es inferior a 100% por definición. El 114% solo existe porque la expansión tapa la fuga.
4. **Muestra pequeña y un solo mes.** Con n=40 y un mes de datos, un solo upgrade grande puede mover el NRR varios puntos. Verifica además qué ventana usa tu panel (mensual vs. cohortes a 12 meses, que es la forma estándar de medirlo) y si es neto o bruto.

## Qué hacer en lugar de "meter todo en captación"

- Separa los tres indicadores: **logo retention** (90%), **GRR** (calcúlalo) y **NRR** (114%). Cuentan historias distintas y necesitas las tres.
- Investiga *quién* se fue: ¿plan pequeño, antigüedad baja, un segmento concreto? Si el churn se concentra en un perfil, puede haber un problema de encaje producto-cliente o de onboarding, no ruido aleatorio.
- Mide la concentración de la expansión: ¿cuántos clientes explican el +14%? Si son uno o dos, ese 114% no es una tendencia, es un evento.
- Solo entonces decide dónde poner el esfuerzo. Es posible que la respuesta correcta sea "arreglar la fuga del extremo pequeño *y* captar", no una u otra.

La buena noticia es real: tener NRR >100% con churn de logo es mejor que lo contrario. Pero es un matiz sobre una fuga existente, no la ausencia de fuga.