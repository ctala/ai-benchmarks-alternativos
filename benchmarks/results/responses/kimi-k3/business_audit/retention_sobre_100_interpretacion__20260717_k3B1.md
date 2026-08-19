# Kimi K3 — business_audit/retention_sobre_100_interpretacion

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.98 | quality: 10.0
- latency_total: 89.146s | tokens_per_second: 33.4
- input_tokens: 245 | output_tokens: 2975
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una interpretación completa y estrategias prácticas para un emprendedor.

## Respuesta completa

No, la lectura no es correcta — y tus propios números lo demuestran.

**Qué mide ese 114%**

Casi con seguridad es Net Revenue Retention (NRR):

> NRR = (MRR inicial + expansión − contracción − churn) / MRR inicial

Mide **ingresos**, no clientes. Un NRR del 114% significa que los upgrades de los clientes que se quedaron generaron más dinero del que perdiste con los que se fueron. Es una métrica de euros, no de logos. Por eso puede superar el 100%, cosa que la retención de clientes jamás puede hacer.

**Lo que dicen tus números de clientes**

Pasaste de 40 a 36 clientes. Asumiendo que no entró nadie nuevo, perdiste 4: un **churn de logos del 10% mensual**. (Si sí entraron nuevos, el churn real es aún mayor.) Si ese ritmo se sostiene:

- En ~7 meses, la mitad de tu base actual ya no estará.
- En 12 meses habrás perdido ~72% de tus clientes (1 − 0,9¹²).

Eso no es "prácticamente no se me va nadie". Es un churn muy alto: en SaaS de pyme, un 3–5% mensual de logos ya se considera zona de preocupación.

**Por qué el 114% puede coexistir con esto, y por qué es frágil**

Es un patrón clásico: NRR alto enmascarando churn alto. Tres problemas:

1. **Tu crecimiento tiene techo matemático.** Con 10% de churn mensual, tu base se estabiliza donde altas nuevas = bajas. Si captas 5 clientes/mes, techo en 50. Si captas 8, techo en 80. La captación no arregla esto; solo el churn lo arregla.
2. **Concentración creciente.** Cada vez más ingresos en menos cuentas. Si mañana se va uno de los que subieron de plan, el NRR se desploma. Y con 36 clientes, 2–3 upgrades mueven la métrica varios puntos: ese 114% es muy volátil con una muestra tan pequeña.
3. **La expansión se agota.** Los que quedan no pueden subir de plan indefinidamente. Estás pidiendo a la expansión que tape una fuga del 10%/mes de forma permanente.

**Qué mirar además del NRR**

- **Gross Revenue Retention (GRR):** igual que el NRR pero excluyendo expansión. Tiene tope en 100% y es el indicador honesto de cuánto ingreso retienes. Con tus números, probablemente esté en el rango 80–90%.
- Logo churn por cohorte, plan y segmento (¿los 4 que se fueron tienen algo en común?).
- Razones de cancelación: encuesta de salida o entrevistas cortas.

**Respuesta a tu pregunta de estrategia**

Meter todo el esfuerzo en captación con un 10% de churn mensual es llenar un cubo agujereado: caro y con techo bajo. El 114% es una buena noticia sobre la salud de los clientes que se quedan — no un permiso para ignorar a los que se van. La prioridad ahora es entender por qué se van esos 4 de cada 40.