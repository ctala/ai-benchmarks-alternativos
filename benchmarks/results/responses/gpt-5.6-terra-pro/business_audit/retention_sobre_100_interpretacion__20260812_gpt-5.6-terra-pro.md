# GPT-5.6 Terra Pro — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 21.248s | tokens_per_second: 165.3
- input_tokens: 5213 | output_tokens: 3512

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No necesariamente. Ese **114% probablemente es Retención Neta de Ingresos (NRR)**, no retención de clientes.

Significa algo como:

> De cada 100 € de MRR que tenías en la cohorte inicial, tras bajas, downgrades y upgrades, conservas 114 €.

Es una señal positiva: las expansiones de clientes existentes están compensando —y superando— los ingresos perdidos por churn y reducciones de plan.

Pero no implica que “prácticamente no se te va nadie”.

Con tus datos:

- Mes pasado: **40 clientes de pago**
- Este mes: **36 clientes de pago**

Si esos 36 proceden de los 40 iniciales y no hay reactivaciones o altas mezcladas, tu **retención de clientes (logo retention)** sería como máximo:

\[
36 / 40 = 90\%
\]

Es decir, habrías perdido aproximadamente el **10% de los clientes** en un mes, aunque tus ingresos retenidos netos sean 114%.

La aparente contradicción es totalmente posible:

- Algunos clientes se van → baja la retención de logos.
- Los que permanecen aumentan de plan → sube el MRR de expansión.
- La expansión supera el MRR perdido → NRR superior al 100%.

Ejemplo simple:

| Concepto | MRR |
|---|---:|
| MRR inicial de la cohorte | 10.000 € |
| MRR perdido por clientes que cancelan | -1.500 € |
| MRR perdido por downgrades | -200 € |
| MRR ganado en upgrades | +3.100 € |
| MRR final de esa cohorte | 11.400 € |

\[
NRR = 11.400 / 10.000 = 114\%
\]

Aun así, puede haber habido bastantes cancelaciones.

No conviene dejar de preocuparte por el churn ni dedicar todo a adquisición. Un NRR de 114% puede ocultar riesgos importantes:

1. **Dependencia de pocos clientes grandes.** Si unos pocos hacen upgrade, sostienen el indicador; si uno se va, el impacto puede ser grande.
2. **Churn de clientes pequeños.** Puede ser tolerable en ciertos modelos, pero también indicar problemas de onboarding, pricing, soporte o encaje producto-mercado.
3. **El crecimiento no siempre se repite.** Los upgrades pueden tener un límite: no puedes expandir indefinidamente a la misma base.
4. **El coste de adquirir nuevos clientes sigue importando.** Perder logos obliga a reemplazarlos continuamente, incluso si el MRR neto aguanta.

Mira el panel y confirma la definición exacta:

- **NRR / Retención neta de ingresos:** incluye expansiones; puede superar 100%.
- **GRR / Retención bruta de ingresos:** excluye expansiones; normalmente no puede superar 100%.
- **Retención de clientes / Logo retention:** mide clientes retenidos, no euros; tampoco debería superar 100% para una cohorte cerrada.
- **Churn de clientes:** porcentaje de logos perdidos.
- **Churn de ingresos:** MRR perdido por cancelaciones y downgrades.

En tu caso, la lectura adecuada sería:

> “La base existente está expandiendo muy bien en ingresos, pero el número de clientes ha caído de 40 a 36. Debemos entender si esas cuatro bajas son un patrón aceptable y si el crecimiento depende de expansiones concentradas en pocos clientes.”

Es buena noticia para monetización y expansión; no es una autorización para ignorar el churn.