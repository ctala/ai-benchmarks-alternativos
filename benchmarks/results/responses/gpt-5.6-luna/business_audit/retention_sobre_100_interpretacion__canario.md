# GPT-5.6 Luna — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.84 | quality: 10.0
- latency_total: 11.645s | tokens_per_second: 83.6
- input_tokens: 128 | output_tokens: 973

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **“Retención de ingresos: 114%” probablemente significa Net Revenue Retention (NRR)**, no retención de clientes.

### Qué significa el 114%

Si empezaste el período con 100 € de ingresos recurrentes de una cohorte de clientes existentes, al final tienes 114 € procedentes de esos mismos clientes, contando:

- ampliaciones de plan,
- compras adicionales,
- reducciones,
- cancelaciones.

Pero **no suele contar los ingresos de clientes nuevos**.

Por tanto, las ampliaciones de algunos clientes han compensado con creces los ingresos perdidos por otros. Eso es positivo, pero no implica que nadie se haya ido.

### Tus datos muestran churn de clientes

Pasaste de 40 a 36 clientes. Si no entró ningún cliente nuevo durante el período, eso implica:

- **4 clientes perdidos**
- **churn de clientes/logos: 10%**
- **retención de clientes/logos: 90%**

Si sí adquiriste clientes nuevos, la retención de la cohorte inicial es incluso peor de lo que sugiere el simple 40 → 36. Por ejemplo, si entraron 2 clientes nuevos, habrías perdido 6 de los 40 originales.

La retención de clientes no puede ser normalmente del 114%. Ese porcentaje corresponde a ingresos, no a número de cuentas.

### Métricas que deberías separar

Mira al menos estas cuatro:

1. **Logo retention / retención de clientes**: qué porcentaje de clientes permanece.
2. **Logo churn**: qué porcentaje de clientes cancela.
3. **Gross Revenue Retention (GRR)**: ingresos retenidos sin contar ampliaciones. No puede superar el 100%.
4. **Net Revenue Retention (NRR)**: ingresos retenidos contando ampliaciones. Puede superar el 100%.

Un NRR del 114% con una caída de 40 a 36 clientes puede significar que los clientes que permanecen están creciendo mucho, pero también que tienes una dependencia importante de unos pocos clientes grandes.

### ¿Puedes dejar de preocuparte por el churn?

No. Puedes considerar que tienes una buena dinámica de expansión, pero **un churn del 10% mensual de clientes sería preocupante** si se mantiene: destruye rápidamente la base, aumenta la presión comercial y puede ocultar problemas de satisfacción o de encaje del producto.

La lectura correcta sería:

> “Estoy perdiendo clientes, pero las ampliaciones de los que permanecen compensan esas pérdidas y hacen crecer los ingresos de la cohorte.”

Analiza específicamente los 4 clientes perdidos, el **GRR**, el churn por segmento y cuánto del 114% procede de uno o dos clientes grandes. Mantén la captación, pero no sustituyas la mejora de retención por ella.