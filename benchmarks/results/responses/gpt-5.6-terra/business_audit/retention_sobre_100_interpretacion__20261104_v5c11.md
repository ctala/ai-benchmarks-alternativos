# GPT-5.6 Terra — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 14.39s | tokens_per_second: 85.2
- input_tokens: 128 | output_tokens: 1226

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No necesariamente. **“Retención de ingresos: 114%” normalmente significa NRR/NRR (Net Revenue Retention)**, no retención de clientes.

Indica que, entre los clientes que ya existían al inicio del período, los ingresos recurrentes netos acabaron siendo un **14% mayores**, después de considerar:

- ingresos perdidos por clientes que se fueron,
- downgrades o reducciones,
- upgrades, expansiones o compras adicionales.

La fórmula habitual es:

\[
\text{NRR} = \frac{\text{MRR inicial} - \text{churn de ingresos} - \text{contracciones} + \text{expansiones}}{\text{MRR inicial}}
\]

Por eso puede ser superior al 100% aunque hayas perdido clientes.

### En tu caso

Pasaste de 40 clientes de pago a 36. Si esos 36 son los mismos clientes que tenías el mes anterior y no hay altas nuevas mezcladas en el número:

- **Retención de clientes (logo retention): 36 / 40 = 90%**
- **Churn de clientes (logo churn): 4 / 40 = 10% mensual**

Al mismo tiempo, los clientes restantes pueden haber subido tanto de plan que compensaron los ingresos de los 4 que se fueron y añadieron un 14% adicional. Eso es compatible con una NRR de 114%.

Ejemplo simple:

- MRR inicial de la cohorte: 10.000 €
- Clientes que se van: −1.000 €
- Downgrades: −200 €
- Upgrades de quienes siguen: +2.600 €

\[
(10.000 - 1.000 - 200 + 2.600) / 10.000 = 114\%
\]

La empresa retiene **114% de ingresos netos**, pero ha perdido clientes y tiene una **retención bruta de ingresos** inferior al 100%.

### Lo que no puedes concluir del 114%

No significa que:

- “prácticamente no se me va nadie”;
- la retención de clientes sea superior al 100%;
- no haya churn preocupante;
- debas dedicar todo el esfuerzo a captación.

La retención de clientes no puede superar el 100% para una cohorte inicial. Si aparecen más clientes, son altas nuevas, no “retención”.

Además, si los 36 clientes actuales incluyen clientes nuevos, ni siquiera puedes afirmar que tu retención de logos sea 90%: podrías haber perdido más de 4 de los 40 originales y haberlos reemplazado parcialmente con nuevas altas.

### Qué métrica mirar junto a ese 114%

Separa al menos estas cuatro:

| Métrica | Qué responde |
|---|---|
| **NRR** | ¿La cohorte existente genera más o menos ingresos netos? |
| **GRR / retención bruta de ingresos** | ¿Cuánto ingreso se conserva antes de contar upgrades? Nunca supera 100%. |
| **Retención de logos** | ¿Qué porcentaje de clientes iniciales sigue activo? |
| **Churn de logos** | ¿Qué porcentaje de clientes iniciales se fue? |

Tu NRR de 114% es una señal muy buena: tienes expansión real y probablemente valor percibido por una parte de la base. Pero puede estar ocultando un problema si unos pocos clientes que crecen mucho compensan la pérdida frecuente de clientes pequeños.

### Decisión práctica

No dejes de trabajar el churn. Haz ambas cosas:

1. **Identifica quién se fue y por qué**: segmento, plan, antigüedad, canal de adquisición, caso de uso y motivo de baja.
2. **Mide GRR y logo retention**, no solo NRR.
3. **Analiza concentración**: comprueba si ese 114% depende de 1–3 clientes que subieron mucho de plan.
4. **Replica el patrón de expansión**: entiende qué hizo que algunos clientes subieran de plan y llévalo a cuentas similares.
5. **Invierte en captación**, sí, pero sin usar el crecimiento de unos clientes para ignorar que otros abandonan.

En resumen: **114% de NRR es excelente, pero no equivale a retener más del 100% de clientes.** Con 40 a 36, hay churn de clientes; los upgrades lo han compensado —y superado— en ingresos.