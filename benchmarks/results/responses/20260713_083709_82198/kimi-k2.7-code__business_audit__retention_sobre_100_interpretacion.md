# Kimi K2.7 Code — business_audit/retention_sobre_100_interpretacion

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.49 | quality: 7.2
- latency_total: 26.074s | tokens_per_second: 43.0
- input_tokens: 160 | output_tokens: 1122

## Respuesta completa

No es correcto. **Retención de ingresos del 114% no significa que no se te vayan clientes.** Significa que los clientes que te quedaron gastan, en conjunto, más que el mes anterior, pero eso oculta una pérdida real de usuarios.

Veamos tu caso concreto:

- Mes pasado: 40 clientes de pago.
- Este mes: 36 clientes de pago.
- Has perdido 4 clientes.

Eso equivale a una **retención de clientes (logo retention) del 90%** y un **churn de clientes del 10% mensual**. Perder 1 de cada 10 clientes cada mes es una cifra muy alta para la mayoría de SaaS.

### Entonces, ¿qué significa el 114%?

Lo más probable es que tu panel esté mostrando **Net Revenue Retention (NRR)** o **Retención Neta de Ingresos**, que se calcula así:

\[
\text{NRR} = \frac{\text{Ingresos actuales de clientes existentes}}{\text{Ingresos del mes anterior de esos mismos clientes}} \times 100
\]

Como varios de los 36 clientes que se quedaron subieron de plan, el ingreso total de esos clientes supera lo que generaban los 40 originales. Los upgrades (expansión) no solo compensaron la pérdida de los 4 clientes que se fueron, sino que la superaron.

### Por qué no puedes dejar de preocuparte por el churn

1. **El churn de clientes del 10% mensual es alto.** Aunque ahora lo estés compensando con upgrades, perder clientes a ese ritmo erosiona tu base y dificulta el crecimiento sostenible.

2. **Depender de la expansión para ocultar la fuga es arriesgado.** Los upgrades pueden agotarse o estancarse. Si un mes los clientes no suben de plan, tu NRR caerá por debajo de 100% rápidamente.

3. **Pierdes opciones de expansión futuras.** Cada cliente que se va no solo deja de pagar hoy, sino que deja de ser candidato a upgrades, compras cruzadas o renovaciones a largo plazo.

4. **El coste de adquisición sube.** Sustituir a clientes que se van con nuevos suele ser más caro que retener a los actuales. Si solo inviertes en captación, puedes estar alimentando una taza agujereada.

### ¿Qué hacer?

No dejes el churn de lado. Investígalo:

- ¿Por qué se fueron esos 4 clientes? ¿Hubo un motivo común?
- ¿Se fueron clientes de un plan o segmento concreto?
- ¿Hubo problemas de onboarding, soporte o encaje con el producto?

Sí, sigue captando clientes nuevos, pero **también repara las fugas**. Un crecimiento sano combina captación, retención de clientes y expansión de ingresos.

En resumen: el 114% de retención de ingresos es una señal positiva, pero **no dice que no haya churn**. Tienes un churn de clientes del 10% mensual, y eso necesita atención.