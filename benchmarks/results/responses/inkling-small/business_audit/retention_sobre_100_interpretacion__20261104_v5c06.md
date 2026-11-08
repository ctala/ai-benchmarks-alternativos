# Inkling Small — business_audit/retention_sobre_100_interpretacion

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 83.992s | tokens_per_second: 32.1
- input_tokens: 135 | output_tokens: 2694

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No. Es justo al revés de lo que parece: ese 114% está ocultando un problema de churn, no eliminándolo.** No puedes dejar de preocuparte por la pérdida de clientes ni apostar todo a captación.

Aquí está la lectura precisa de tu panel frente a tu contexto:

### 1. Qué dice realmente el 114%
Ese número es casi seguro **Net Revenue Retention (NRR)**, es decir, retención **de ingresos**, no de clientes. Significa que los clientes que se quedaron y no se fueron generaron un crecimiento neto del 14% en ingresos respecto a tu base existente del mes anterior, una vez descontados los que bajaron o se fueron.

Cómo es posible con tu contexto (40 → 36 clientes):
- Perdiste **4 clientes** (churn de logos del 10%).
- Eso te costó ingresos.
- Pero los que se quedaron **subieron de plan** (upsell/expansión) lo suficiente como para que, en términos monetarios, la base vieja ahora valga un 14% más.

**Conclusión matemática:** Tu expansión compensó y superó tu fuga. Pero la fuga existe.

### 2. Lo que no es
- **No es retención de clientes > 100%.** La retención de clientes (logo retention) está en torno al **90%** si esos 36 incluyen solo tu base anterior (o menos, si entre ellos hay nuevos). Eso es un churn de logos significativo.
- **No es que "prácticamente no se va nadie".** Se fueron 4 de 40. Eso es una rotación de clientes real.

### 3. Por qué es peligrosa esta interpretación intuitiva
Un NRR de 114% es saludable en el papel, pero **si tu crecimiento de ingresos depende de que los sobrevivientes paguen mucho más para compensar los que se van, tienes un modelo frágil:**

| Riesgo | Qué pasa si sigues pensando que todo está bien |
|--------|-----------------------------------------------|
| **Saturación del upsell** | Ya subieron. ¿Cuánto más pueden subir? Si se estanca la expansión, tu NRR cae por debajo de 100% inmediatamente porque el churn de logos sigue ahí. |
| **Churn oculto** | El 10% que se fue puede ser tu segmento más vulnerable o de menor valor. Si sigues perdiendo clientes, tu CAC efectivo crece: cada nuevo cliente debe reemplazar al que se va *y* crecer la base. |
| **Calidad de producto/mercado** | Perder 1 de cada 10 clientes periódicamente suele señalar problemas de onboarding, fit o competencia. Ignorarlo para "meter todo en captación" es llenar una bañera con agujeros. |

### 4. Respuesta directa a tus preguntas
> *"¿Correcto que la retención de clientes está por encima del 100%?"*  
**No.** Estás confundiendo ingresos con clientes.

> *"¿Puedo dejar de preocuparme por el churn y meter todo en captación?"*  
**No, rotundamente no.** De hecho, deberías investigar **por qué se fueron esos 4** antes de escalar captación. Si no cierras la fuga:
- Gastas más en marketing para reemplazar lo que se pierde.
- Tu NRR puede colapsar si los upsells no se repiten.
- Creces a costa de una base cada vez más dependiente de un grupo pequeño de clientes que paguen mucho.

### 5. Qué hacer con esa métrica
Usa el **114% como un indicador de expansión saludable**, pero contrástalo con:
- **Logo retention / Churn de clientes:** ¿Por qué pasó de 40 a 36? ¿Qué plan o segmento se fue?
- **Gross Revenue Retention (GRR):** Si tu NRR es 114%, tu GRR (sin expansión) probablemente esté cerca de 85-90%, lo que confirma que sin upsell estás perdiendo ingresos.
- **Cohort analysis:** ¿Los que subieron de plan son los mismos que se quedaron? ¿O los 36 incluyen clientes nuevos?

**En resumen:** Tienes un buen *upsell*, pero un *churn de clientes real*. No dejes de preocuparte por el churn; **el 114% te está dando permiso para crecer, no para descuidar la retención.** Si escalaras captación ahora sin arreglar la fuga de 4 de 40, estarías acelerando un negocio que pierde clientes y depende de que los que quedan paguen cada vez más.

¿Quieres que analicemos qué segmento de los 4 que se fueron podría estar tirando tu base, o cómo separar la métrica de expansión de la de retención de clientes?