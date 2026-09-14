# Qwen 3.8 Max 0902 — business_audit/retention_sobre_100_interpretacion

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 8.05 | quality: 10.0
- latency_total: 138.436s | tokens_per_second: 38.2
- input_tokens: 181 | output_tokens: 5288

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. La lectura correcta es menos halagadora que “no se me va nadie”.

**“Retención de ingresos: 114%” no significa que retienes más del 100% de tus clientes.** Significa que, en términos de ingresos, tu base existente generó más dinero que el mes anterior, probablemente por upgrades, aunque algunos clientes se hayan dado de baja.

En tu caso:

- Mes pasado: **40 clientes de pago**
- Este mes: **36 clientes de pago**

Como mínimo, si no entró ningún cliente nuevo, perdiste **4 clientes**. Eso es un **churn de clientes del 10%** en un mes.

Si además entraron clientes nuevos este mes, entonces la situación puede ser peor: por ejemplo, si entraron 2 nuevos y terminaste con 36, solo habrías retenido 34 de los 40 originales, es decir, una retención de clientes del **85%**.

---

## 1. Retención de clientes no puede ser superior al 100%

La retención de clientes, también llamada **logo retention**, se calcula más o menos así:

\[
\text{Retención de clientes} = \frac{\text{Clientes iniciales que siguen}}{\text{Clientes iniciales}}
\]

Si empezaste con 40 clientes, no puedes retener más de 40. Por tanto, no puede ser superior al 100%.

Lo que sí puede superar el 100% es la **retención de ingresos neta**, porque incluye expansión: upsells, upgrades, cross-sell, mayor uso, etc.

---

## 2. Qué significa probablemente ese 114%

Si tu panel dice “Retención de ingresos: 114%”, probablemente está midiendo **Net Revenue Retention**, o retención neta de ingresos.

La fórmula típica es:

\[
\text{NRR} = \frac{\text{MRR inicial} - \text{MRR perdido por churn} - \text{downgrades} + \text{expansión de clientes existentes}}{\text{MRR inicial}}
\]

Un NRR del 114% significa:

> Por cada 100 € de MRR que tenías el mes pasado en tu base de clientes existente, este mes tienes 114 €, después de descontar bajas y downgrades, pero incluyendo expansiones.

Eso es bueno. Pero no significa que no haya churn. Significa que el crecimiento de algunos clientes compensó las pérdidas de otros.

---

## 3. Ejemplo simple

Imagina que el mes pasado tenías:

- 40 clientes
- Cada uno pagaba 100 €
- MRR inicial: 4.000 €

Este mes:

- Se van 4 clientes: pierdes 400 €
- Los 36 restantes hacen upgrades y pasan a generar 4.560 €

Resultado:

\[
\text{NRR} = \frac{4.560}{4.000} = 114\%
\]

Pero al mismo tiempo:

\[
\text{Retención de clientes} = \frac{36}{40} = 90\%
\]

Es decir:

- **Retención de ingresos:** 114%
- **Retención de clientes:** 90%
- **Churn de clientes:** 10%

Ambas cosas pueden ser ciertas a la vez.

---

## 4. Cuidado: quizá tu panel no esté midiendo retención de verdad

Hay una trampa importante.

Si tu panel está calculando:

\[
\frac{\text{Ingresos de este mes}}{\text{Ingresos del mes pasado}}
\]

y ese 114% incluye clientes nuevos, entonces **no es retención**. Es crecimiento de ingresos.

La retención real debe medir solo lo que ocurre con los clientes que ya existían al inicio del periodo.

Debes verificar si ese 114%:

1. Incluye solo clientes existentes.
2. Excluye nuevos clientes adquiridos este mes.
3. Incluye expansión/upsells.
4. Descuenta churn, downgrades y cancelaciones.
5. Es NRR o GRR.

Si incluye clientes nuevos, el número puede ser engañoso.

---

## 5. La métrica que te falta: GRR

Además del NRR, deberías mirar el **Gross Revenue Retention** o retención bruta de ingresos.

\[
\text{GRR} = \frac{\text{MRR inicial} - \text{churn} - \text{downgrades}}{\text{MRR inicial}}
\]

El GRR no incluye expansión. Por eso nunca puede superar el 100%.

Ejemplo:

- NRR: 114%
- GRR: 88%

Eso significaría:

> Tu base de clientes existente está perdiendo ingresos antes de contar upgrades, pero los upgrades están tapando la fuga.

Eso puede ser válido si la expansión es sostenible, pero es peligroso si depende de unos pocos clientes o de subidas puntuales.

---

## 6. ¿Puedes ignorar el churn y dedicarte solo a captar clientes nuevos?

No. Sería un error.

Aunque el NRR sea superior al 100%, el churn sigue importando por varias razones.

### a) El churn de clientes puede estar escondido

Tus ingresos pueden crecer mientras tu base de clientes se reduce. Eso puede funcionar durante un tiempo, pero no es necesariamente sano.

En tu caso, pasaste de 40 a 36 clientes. Eso es una señal clara de pérdida de clientes.

### b) El churn mensual del 10% es alto

Si perdiste 4 de 40, eso es un 10% en un mes.

Si ese ritmo se mantuviera, después de 12 meses:

\[
0,9^{12} \approx 0,28
\]

Estarías reteniendo solo alrededor del 28% de una cohorte anual. Es una fuga muy alta para la mayoría de SaaS.

Obviamente, con 40 clientes una muestra pequeña puede distorsionar. Un mes malo no es necesariamente una tendencia. Pero no deberías ignorarlo.

### c) La adquisición puede estar tapando un cubo con agujeros

Si captas clientes nuevos pero pierdes antiguos, tu crecimiento depende cada vez más de llenar el embudo.

Eso encarece el crecimiento porque:

- Necesitas más marketing.
- Necesitas más ventas.
- Sube el CAC.
- Baja el LTV.
- El payback se alarga.
- El negocio se vuelve más dependiente de adquisición.

### d) El churn te da información valiosa

Los 4 clientes que se fueron pueden decirte cosas importantes:

- ¿Eran clientes mal cualificados?
- ¿No entendieron el producto?
- ¿Fue un problema de onboarding?
- ¿No vieron valor rápido?
- ¿El precio era inadecuado?
- ¿Se fueron a un competidor?
- ¿Eran de un segmento concreto?
- ¿Usaban poco el producto?
- ¿Se fueron después de una subida de plan o precio?

Ignorar el churn es ignorar información sobre tu producto, tu mercado y tu propuesta de valor.

### e) La expansión no siempre es sostenible

Si tu NRR del 114% depende de que varios clientes subieron de plan, pregúntate:

- ¿Fue un cambio puntual o recurrente?
- ¿Quedan clientes con capacidad de subir de plan?
- ¿Los upgrades están ligados a uso real?
- ¿Podrían producirse downgrades más adelante?
- ¿Estás subiendo precios de forma agresiva?

Un upgrade puntual puede mejorar el mes, pero no garantiza retención futura.

---

## 7. La interpretación correcta de tu panel

Tu situación parece ser:

- **Retención de ingresos:** 114%  
  Posiblemente buena señal de expansión en clientes existentes.

- **Retención de clientes:** como máximo 90%  
  Si no hubo clientes nuevos. Si los hubo, podría ser menor.

- **Churn de clientes:** al menos 10%  
  Posiblemente mayor si este mes entraron clientes nuevos.

La lectura honesta sería:

> “Mis ingresos retenidos se ven bien porque varios clientes subieron de plan, pero perdí clientes. El crecimiento de ingresos está compensando el churn, pero no puedo concluir que la retención de clientes sea excelente.”

---

## 8. Qué deberías mirar ahora

Te recomiendo separar estas métricas:

### 1. Logo churn

\[
\frac{\text{Clientes perdidos}}{\text{Clientes iniciales}}
\]

En tu caso, si no hubo nuevos: 4/40 = 10%.

### 2. Logo retention

\[
\frac{\text{Clientes iniciales que siguen}}{\text{Clientes iniciales}}
\]

En tu caso, si no hubo nuevos: 36/40 = 90%.

### 3. MRR churn

Cuánto MRR perdiste por clientes que se dieron de baja.

### 4. Expansion MRR

Cuánto MRR adicional generaste de clientes existentes por upgrades, mayor uso, nuevos asientos, etc.

### 5. GRR

Para saber si tu base de clientes pierde ingresos antes de contar expansiones.

### 6. NRR

Para ver si la expansión compensa churn y downgrades.

### 7. Net MRR change

Variación neta total:

\[
\text{MRR final} = \text{MRR inicial} + \text{Nuevo MRR} + \text{Expansión} - \text{Churn} - \text{Downgrades}
\]

---

## 9. Respuesta directa

**No, no es correcto decir que prácticamente no se te va nadie.**  
De hecho, pasaste de 40 a 36 clientes de pago.

**No, la retención de clientes no está por encima del 100%.**  
Eso no puede ocurrir en retención de clientes. Lo que puede superar el 100% es la retención de ingresos neta por expansión.

**No, no deberías dejar de preocuparte por el churn.**  
Debes entender por qué se fueron esos clientes y si ese 114% es sólido o depende de upgrades puntuales.

La decisión correcta no es “olvidarme del churn y dedicar todo a captación”. La decisión correcta es:

> Mantener adquisición, pero investigar el churn, medir correctamente GRR/NRR y asegurar que la expansión no esté ocultando una fuga de clientes.