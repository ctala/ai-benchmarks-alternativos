# DeepSeek V4.1 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 7.56 | quality: 8.0
- latency_total: 19.658s | tokens_per_second: 115.2
- input_tokens: 165 | output_tokens: 2265

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, esa lectura no es correcta. Un **114% de retención de ingresos** casi con seguridad es **NRR** (*Net Revenue Retention*), no retención de clientes.

### Qué significa ese 114%
Mide los ingresos del **mismo grupo de clientes existentes**, incorporando:

- upsells/upgrades,
- cross-sells,
- downgrades,
- bajas.

Fórmula simplificada:

> **NRR = (ingresos iniciales del cohorte + expansión − contracción − ingresos perdidos por churn) / ingresos iniciales del cohorte**

Un 114% significa que los ingresos de tus clientes existentes crecieron un **14% neto** pese a bajas o downgrades. **No significa que no se vaya nadie**, ni que la retención de clientes sea superior al 100%. La retención de clientes se mide por número de clientes y **no puede superar el 100%**.

### Tus datos: 40 → 36 clientes
Eso implica **4 clientes netos menos**, un **−10% neto** en número de clientes.

- Si este mes no captaste clientes nuevos: retención de clientes = **36/40 = 90%**; churn de clientes = **10%**.
- Si sí captaste nuevos, el churn bruto pudo ser **mayor que 10%**, porque los nuevos están compensando parte de las bajas. Para saberlo necesitas mirar cohortes, no solo el total.

### El riesgo de leerlo mal
Varios clientes subieron de plan y eso puede maquillar la pérdida de otros. Ejemplo ilustrativo, no tus cifras: se van 4 clientes que aportaban 10 de ingresos, pero los 36 restantes suben de plan y aportan 124. Resultado: ingresos finales 114 → **NRR 114%**, aunque perdiste el **10% de los clientes**.

Ese patrón puede ser sano si el churn es de clientes pequeños y la expansión es amplia y sostenible. Pero es peligroso si:

- el churn se concentra en un segmento importante,
- las subidas vienen de pocas cuentas grandes,
- el churn mensual del 10% se compone y se vuelve alto,
- no estás midiendo **GRR** (*Gross Revenue Retention*), que no incluye expansión y sí muestra cuánto ingreso retienes realmente.

### ¿Puedes dejar de preocuparte por el churn y meter todo en captación?
**No.** Sería una mala decisión con estos datos. Captar clientes con churn alto es llenar un balde agujereado. No necesitas abandonar la captación, pero sí equilibrarla con retención.

Priorizaría:

1. Entender por qué se fueron esos 4 clientes netos.
2. Separar **NRR** de **GRR** y de **logo churn**.
3. Medir churn por cohorte y por segmento.
4. Revisar concentración: cuánto de la expansión viene de pocas cuentas.
5. Poner señales de alerta para downgrades y bajas.

Resumen: **114% de NRR es una buena señal de expansión, pero no significa que “prácticamente no se va nadie” ni que la retención de clientes esté por encima del 100%. Tienes un 10% menos de clientes netos que el mes pasado; el churn sigue siendo un problema que debes diagnosticar.**