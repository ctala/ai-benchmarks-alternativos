# DeepSeek V4 Pro (0813) — business_audit/retention_sobre_100_interpretacion

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 52.52s | tokens_per_second: 58.9
- input_tokens: 218 | output_tokens: 3091

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, tu interpretación no es correcta. La métrica “retención de ingresos” (también llamada *net revenue retention*, NRR) no mide cuántos clientes se quedan, sino cuánto ingreso recurrente conservas (y expandes) de tu base existente. Es perfectamente posible tener una retención de ingresos superior al 100% mientras se pierden clientes, como es tu caso.

## 1. Qué significa realmente “retención de ingresos = 114%”

La fórmula típica de NRR es:

\[
\text{NRR} = \frac{\text{Ingresos recurrentes al final del período (de clientes que estaban al inicio)}}{\text{Ingresos recurrentes al inicio del período}} \times 100
\]

Si el resultado es 114%, significa que por cada 100 €/$ de ingresos recurrentes que tenías al inicio, ahora tienes 114 €/$ **provenientes de los mismos clientes** (sin contar nuevas altas). Ese 14% extra puede venir de:
- Upgrades (subidas de plan) de clientes existentes.
- Compra de funcionalidades adicionales.
- Más asientos/licencias.

Pero **no** te dice nada sobre cuántos clientes se fueron. De hecho, si algunos clientes se dieron de baja y otros aumentaron su facturación lo suficiente, el NRR puede superar 100% incluso con una pérdida neta de clientes.

## 2. La retención de clientes no puede superar el 100%

La retención de clientes (o *logo retention*) se calcula sobre el número de cuentas, no sobre los ingresos:

\[
\text{Retención de clientes} = \frac{\text{Nº de clientes al final del período que ya estaban al inicio}}{\text{Nº de clientes al inicio del período}} \times 100
\]

Por definición, **no puede superar el 100%** a menos que cuentes nuevas altas (lo cual no es retención). Si empiezas con 40 clientes y terminas con 36 (suponiendo que los 36 son todos del grupo original), tu retención de clientes es:

\[
\frac{36}{40} \times 100 = 90\%
\]

Es decir, perdiste 4 clientes (churn de clientes del 10%). Si además hubo nuevas altas, la retención de los clientes originales sería aún menor, porque entre los 36 finales algunos serían nuevos y habrías perdido más de 4 originales.

## 3. Tu caso concreto

- Mes pasado: 40 clientes.
- Este mes: 36 clientes.
- Varios subieron de plan.

Aunque no conocemos los ingresos exactos, es evidente que:
- Perdiste al menos 4 clientes (o más si hubo nuevas altas).
- Los que se quedaron (o algunos) aumentaron tanto su gasto que compensaron la pérdida de ingresos de los que se fueron y la superaron en un 14%.

Por tanto:
- **No** es cierto que “no se te va nadie”. Se te fueron clientes.
- **No** es cierto que tu retención de clientes esté por encima del 100%. Está, como máximo, en 90%.

## 4. ¿Puedes dejar de preocuparte por el churn y centrarte solo en captar?

**No lo recomiendo.** Un NRR alto es positivo, pero no elimina el riesgo del churn de clientes. Razones:

- **El churn de clientes es un síntoma**: si los clientes se van, puede haber problemas de producto, precio, soporte o competencia. Ignorarlo puede agravar la situación.
- **La expansión tiene un límite**: puedes hacer upsell solo a los clientes que permanecen. Si la base se reduce constantemente, cada vez tendrás menos cuentas a las que expandir.
- **Riesgo de concentración**: si dependes de unos pocos clientes que hacen upgrades, su pérdida tendría un impacto desproporcionado. Un cliente grande que se va puede desplomar tu NRR.
- **Crecimiento sostenible**: captar nuevos clientes suele costar más que retener. Si pierdes 10 clientes y ganas 10, no creces en número; solo reemplazas. Si además algunos de los que se van eran grandes, ni siquiera los ingresos crecerán.

## 5. Qué deberías hacer

- **Monitorea ambas métricas**: NRR (salud de ingresos por cliente) y retención de clientes (salud de la base). No son intercambiables.
- **Analiza por qué se van los clientes**: encuestas de cancelación, métricas de uso, soporte. Un churn de clientes del 10% mensual es elevado (anualizado sería catastrófico).
- **No abandones la retención**: busca reducir el churn y, al mismo tiempo, fomentar la expansión. Son esfuerzos complementarios.
- **Equilibra captación y retención**: si tu churn es alto, primero tapa la fuga antes de llenar el cubo con nuevos clientes.

En resumen: tu panel muestra que los ingresos recurrentes de tus clientes existentes crecieron un 14% a pesar de perder clientes, lo cual es bueno, pero **no significa que no tengas churn**. Perdiste clientes, y eso debería preocuparte y ocuparte.