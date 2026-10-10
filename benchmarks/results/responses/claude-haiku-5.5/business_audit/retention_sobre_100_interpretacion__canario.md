# Claude Haiku 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.73 | quality: 8.0
- latency_total: 9.086s | tokens_per_second: 183.7
- input_tokens: 218 | output_tokens: 1669

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, esa lectura es incorrecta, y conviene corregirla antes de tomar decisiones.

**Qué mide realmente el 114%**

La retención neta de ingresos (NRR) compara los ingresos recurrentes que generaba un grupo de clientes al inicio del periodo con lo que generan ese mismo grupo al final. Incluye cuatro efectos:

- **Churn** (clientes que se van): reduce el NRR.
- **Contracción** (clientes que bajan de plan): reduce el NRR.
- **Expansión** (upgrades, más asientos, más uso): aumenta el NRR.
- **Nuevos clientes**: no entran en el cálculo.

Un NRR por encima del 100% solo significa que la expansión compensó con holgura lo que se perdió. No dice nada sobre cuántos clientes se han ido.

**Tu caso**

Pasaste de 40 a 36 clientes de pago. Has perdido 4 de 40, un **10% de churn de logos**. Eso no es "prácticamente nadie". Puede ser un número muy alto según el periodo que estés midiendo, y sería preocupante si es mensual.

Un ejemplo con cifras hipotéticas:

- MRR inicial del grupo: 10.000 €
- Churn de 4 clientes de ~100 €: −400 €
- Expansión de los que subieron de plan: +1.800 €
- MRR final del grupo: 11.400 €
- NRR = 114%, pero la **retención bruta** (GRR, sin contar expansión) es (10.000 − 400) / 10.000 = **96%**

Con ese perfil, el 114% oculta que estás perdiendo clientes y dependes de que unos pocos paguen más.

**Qué mirar antes de decidir nada**

1. **Churn de logos** (clientes perdidos / clientes al inicio): tu 10%.
2. **GRR** (retención bruta de ingresos): cuánto retienes sin contar la expansión. Si está muy por debajo del 90–95%, hay un problema de producto, precio u onboarding.
3. **Concentración de la expansión**: si el 114% viene de 2 o 3 cuentas que subieron mucho, es un riesgo, no una tendencia sana.
4. **Motivos de cancelación**: cuánto tiempo llevaban, qué plan tenían, por qué se fueron.

**Conclusión**

No dejes de preocuparte por el churn. Con 10% de pérdida de clientes, retener es probablemente la palanca más rentable que tienes ahora, porque cada cliente que se queda cuesta menos que uno nuevo. Captar gente nueva sin resolver la fuga es llenar un cubo con un agujero.

Si me pasas el MRR de inicio y de final del mes, separando los clientes perdidos, los que subieron y los que bajaron, puedo calcular tu GRR y tu NRR reales y decirte cuánto del 114% depende de la expansión.