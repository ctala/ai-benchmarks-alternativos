# GPT-5.6 Luna Pro — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.87 | quality: 10.0
- latency_total: 18.708s | tokens_per_second: 41.8
- input_tokens: 127 | output_tokens: 782

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No exactamente. Ese **114% probablemente es la retención neta de ingresos (NRR)**, no la retención de clientes.

La NRR mide cuánto ingreso genera este mes la **cohorte de clientes que ya existía al inicio del período**, incluyendo:

- renovaciones,
- ampliaciones de plan,
- reducciones,
- cancelaciones.

Una NRR del 114% significa que esa cohorte genera ahora un 14% más de ingresos que antes. Puede ocurrir aunque pierdas clientes, si los que permanecen se expanden suficientemente.

Con tus datos:

- Clientes iniciales: 40
- Clientes actuales: 36
- Si no hubo clientes nuevos, la retención de clientes sería **36/40 = 90%**, es decir, **10% de churn de clientes**.
- Si algunos de esos 36 son nuevos, entonces no puedes calcular la retención de clientes solo con ese total. Necesitas saber cuántos de los 40 originales siguen activos.

Ejemplo: si partieras de 100 € de ingresos:

- 20 € se pierden por cancelaciones o reducciones;
- 34 € se ganan mediante ampliaciones;
- ingresos de la cohorte: 114 €;
- NRR: **114%**.

Pero habrías perdido clientes.

También conviene distinguir:

- **Retención bruta de ingresos (GRR):** incluye renovaciones, cancelaciones y reducciones, pero no ampliaciones. Nunca debería superar el 100%.
- **Retención neta de ingresos (NRR):** incluye también ampliaciones; puede superar el 100%.
- **Retención de clientes o logo retention:** proporción de clientes iniciales que continúan.
- **Churn de clientes:** porcentaje de clientes iniciales que se pierden.

Por tanto, **no dejaría de preocuparme por el churn**. Una NRR del 114% es una señal positiva sobre la expansión de los clientes que permanecen, pero una pérdida de clientes puede:

- indicar problemas de producto, onboarding o satisfacción;
- concentrar demasiado los ingresos en pocos clientes;
- hacer que la NRR caiga si se agota el potencial de expansión;
- dificultar el crecimiento a largo plazo aunque la facturación actual aumente.

Para evaluar bien el mes, revisa al menos:

1. NRR y GRR de la cohorte inicial.
2. Retención de clientes y churn de logos.
3. Ingresos perdidos por cancelaciones frente a ingresos ganados por expansión.
4. Retención por segmento, tamaño y plan.
5. Cuántos clientes nuevos explican la diferencia entre 36 y los clientes iniciales.

La lectura correcta sería: **“Los clientes que permanecen están expandiendo sus ingresos, pero aparentemente estoy perdiendo clientes; debo gestionar ambas cosas, no sustituir la retención por adquisición.”**