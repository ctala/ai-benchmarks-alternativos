# Qwen 3.8 Max — business_audit/retention_sobre_100_interpretacion

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 8.09 | quality: 10.0
- latency_total: 118.575s | tokens_per_second: 34.9
- input_tokens: 181 | output_tokens: 4137

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Esa lectura no es correcta.

**“Retención de ingresos: 114%” no significa que no se te vaya nadie.** Significa que, en términos de ingresos, tu base existente terminó generando un 14% más que el mes pasado **después de descontar bajas y sumar expansiones/upgrades**. Pero eso puede ocurrir aunque pierdas clientes.

Con tu contexto:

- Mes pasado: **40 clientes de pago**
- Este mes: **36 clientes de pago**
- Si no entraron clientes nuevos, perdiste **4 clientes**
- Eso es una **retención de clientes / logo retention del 90%**
- Y un **churn de clientes del 10%**

Es decir: **la retención de clientes no está por encima del 100%**. Como máximo, si no hubo altas nuevas, retuviste al 90% de los clientes. Si además entraron clientes nuevos este mes, entonces la retención real de los clientes antiguos sería incluso menor que 90%.

La confusión viene de mezclar dos métricas distintas:

| Métrica | Qué mide | Lectura con tu caso |
|---|---|---|
| Retención de clientes / logo retention | % de clientes que se quedan | 90% si no hubo nuevas altas |
| Retención de ingresos / NRR | % de ingresos que conserva la base existente tras churn, downgrades y expansiones | 114% |

### Qué significa realmente ese 114%

Probablemente tu panel esté mostrando **Net Revenue Retention** o retención neta de ingresos. La fórmula típica es:

\[
NRR = \frac{MRR inicial - MRR perdido por churn - MRR perdido por downgrades + MRR ganado por expansiones}{MRR inicial}
\]

Un NRR del 114% significa esto:

- Empezaste con, por ejemplo, **100€ de MRR** en la base existente.
- Perdiste clientes o bajadas de plan.
- Pero los clientes que se quedaron, o algunos de ellos, subieron de plan.
- Al final, esa misma base existente genera **114€**.

O sea: **ingresos suben, clientes bajan**.

### Ejemplo simple

Imagina esto:

- Mes pasado: 40 clientes × 100€ = **4.000€ MRR**
- Este mes se van 4 clientes: **-400€**
- Los 36 restantes suben de plan y generan **+960€ extra**
- MRR final de la base existente: **4.560€**

\[
4.560 / 4.000 = 114\%
\]

El resultado es:

- **Clientes retenidos:** 36/40 = **90%**
- **Retención neta de ingresos:** **114%**

Ambas cosas pueden ser ciertas a la vez.

### ¿Puedes dejar de preocuparte por el churn?

No. Sería un error.

Un NRR del 114% es bueno, pero no debería ocultar el churn de clientes. Razones:

1. **Estás perdiendo clientes.**  
   Pasar de 40 a 36 sin nuevas altas es una pérdida del 10% en un mes. Eso es relevante, especialmente si tu base todavía es pequeña.

2. **El crecimiento por upgrades puede no ser sostenible.**  
   Si unos pocos clientes suben de plan, pueden compensar las bajas este mes. Pero los upgrades no son infinitos. Si sigues perdiendo clientes, tarde o temprano la expansión no será suficiente.

3. **El churn de clientes suele ser una señal temprana de problema.**  
   Puede que se vayan clientes pequeños, de bajo valor o mal encajados. Aun así, conviene entender por qué se van. Si no lo haces, puedes normalizar una fuga.

4. **Tu base se está concentrando.**  
   Si cada vez tienes menos clientes pero más ingresos por cliente, dependes más de cada uno de ellos. Eso aumenta el riesgo.

5. **Con pocos clientes, una métrica mensual puede ser engañosa.**  
   Cuatro clientes pueden mover mucho el porcentaje. Un mes puedes tener 114% y otro mes 85% por una sola baja grande.

### La lectura correcta

La lectura precisa sería:

> “Mi retención neta de ingresos es del 114%, lo cual es positiva porque los clientes que se quedan están expandiendo ingresos. Pero al mismo tiempo he pasado de 40 a 36 clientes, así que tengo churn de clientes. No puedo ignorarlo.”

O, dicho de forma más directa:

> “Estoy reteniendo menos clientes, pero los que se quedan pagan más.”

### Qué deberías mirar además del 114%

No te quedes solo con la retención de ingresos. Desglósala:

- **Logo churn:** % de clientes que se van.
- **MRR churn:** % de ingresos perdidos por bajas.
- **Gross Revenue Retention:** retención de ingresos sin contar expansiones.
- **Expansion MRR:** cuánto ingreso extra viene de upgrades.
- **Contraction MRR:** cuánto ingreso pierdes por downgrades.
- **NRR por cohorte:** cómo se comportan los clientes que entraron en cada mes.
- **Número de clientes activos:** no solo ingresos.

### Conclusión

No, no puedes concluir que “prácticamente no se te va nadie”.

Lo que probablemente está pasando es:

- **Clientes:** bajan de 40 a 36.
- **Ingresos:** suben porque varios clientes restantes subieron de plan.
- **Retención de ingresos:** 114%.
- **Retención de clientes:** 90% como máximo si no hubo nuevas altas.

Por tanto, **no deberías dejar de preocuparte por el churn**. Deberías celebrar el buen NRR, pero investigar por qué perdiste esos clientes y confirmar si la expansión que estás viendo es sostenible o simplemente un efecto puntual de unos pocos upgrades.