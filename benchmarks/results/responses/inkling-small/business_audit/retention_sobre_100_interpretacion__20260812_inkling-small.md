# Inkling Small — business_audit/retention_sobre_100_interpretacion

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 38.93s | tokens_per_second: 57.8
- input_tokens: 136 | output_tokens: 2250
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una interpretación completa y práctica de la retención de ingresos por encima del 100%.

## Respuesta completa

No. Es exactamente al revés de lo que intuyes: **tienes un problema serio de churn que está siendo ocultado por upsells.** No puedes dejar de preocuparte ni meter todo el esfuerzo solo en captación.

Aquí está la lectura precisa:

### 1. 114% es retención de *ingresos*, no de clientes
En SaaS, una cifra >100% es casi siempre **Net Revenue Retention (NRR)** —retención neta de ingresos—, no retención de clientes (logo retention).

- **NRR 114%**: El dinero que te generaban tus clientes del mes pasado, tras sumar upgrades, expansiones y restar downgrades y bajas, terminó siendo un **14% mayor**.
- **Logo retention (clientes)**: 36 / 40 = **90%**. Has perdido al **10% de tu base** en un solo mes.

La retención bruta de ingresos (GRR) nunca supera 100%, porque mide solo lo que se queda de la base sin contar nuevas ventas ni expansiones. Si tu panel dice 114%, es NRR.

### 2. Lo que pasó en tu caso
Perdiste 4 clientes, pero los 36 restantes (o los que se quedaron de tu cohorte) subieron de plan lo suficiente como para que el ingreso total crezca un 14% respecto al mes anterior.

Esto no es "prácticamente nadie se va". Es una **fuga del 10% mensual** que estás parcheando con dinero de upsell.

### 3. Por qué no puedes ignorar el churn
- **Tu base se está encogiendo**: Si pierdes 4 de 40 cada mes, en 6 meses tendrás ~21 clientes, no 40. Aunque cada uno pague más, hay un límite físico de cuánto puedes expandir a una base que se reduce.
- **Churn mensual del 10% = anualizado ~72%** (0,9¹² ≈ 0,28). Eso es insostenible.
- **Dependencia peligrosa**: Si el crecimiento del ingreso depende 100% de que los que sobreviven paguen más, una sola desaceleración en upsells o una crisis de precios te deja con ingresos cayendo en picado porque la base es más pequeña.
- **Costo de reposición**: Captar un cliente nuevo suele ser 5-25x más caro que retener uno existente. Si tu máquina de captación se enfoca solo en reemplazar a los que se van, tu CAC se dispara.

### 4. Qué hacer con esos números
- **Investiga los 4 que se fueron**: ¿Churn voluntario (no encajaban, precio, producto)? ¿Churn involuntario (tarjeta fallida, falta de onboarding)? Eso es tu prioridad inmediata.
- **No dejes de hacer upsell**: El 114% es una fortaleza. Pero úsala para **financiar la retención**, no para justificar la fuga.
- **Separa las métricas en tu panel**: Mide NRR (ingresos) y Logo Retention (clientes) por separado. Si solo miras 114%, te engañas.

**Resumen**: Tienes una **buena expansión y una mala retención de clientes**. El 114% no dice "no hay churn"; dice "los que se quedan pagan mucho más que los que se van". Eso es una estrategia de expansión sobre una base erosionada, no un permiso para ignorar la fuga. Arregla por qué se van esos 4 antes de que sean 10.