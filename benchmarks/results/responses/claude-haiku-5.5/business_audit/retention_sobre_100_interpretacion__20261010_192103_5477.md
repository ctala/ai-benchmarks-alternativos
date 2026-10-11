# Claude Haiku 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.04 | quality: 10.0
- latency_total: 11.154s | tokens_per_second: 165.9
- input_tokens: 218 | output_tokens: 1850

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No es correcto. El 114% de **retención neta de ingresos (NRR)** no significa que se vaya poca gente. Significa que los ingresos de los clientes que tenías hace un mes son hoy un 14% más altos, después de contar bajas, bajadas de plan y subidas de plan.

Tus números muestran dos cosas a la vez:

- **Retención de clientes (logos):** 36 de 40 = **90%**. Perdiste 4 clientes, un 10% de churn.
- **Retención de ingresos (NRR):** 114%. Los clientes que se quedaron pagan tanto más que compensa con creces esas 4 bajas.

Las dos métricas son ciertas al mismo tiempo. El NRR esconde el churn porque la expansión lo tapa.

**Por qué no deberías dejar de preocuparte por el churn:**

1. **Falta un dato clave: la retención bruta de ingresos (GRR).** Es el ingreso que conservas sin contar expansiones: `(ingreso inicial − bajas − bajadas de plan) / ingreso inicial`. Como máximo llega al 100%, y casi siempre está por debajo del NRR. Si tu GRR es, por ejemplo, del 85-90%, estás perdiendo base y depende de la expansión para crecer.

2. **La expansión puede estar concentrada.** Si dos o tres cuentas grandes explican la mayor parte del 114%, tu NRR depende de ellas. Si una se va, el número se hunde.

3. **Las bajas pueden ser las cuentas que más importan.** Si los 4 que se fueron eran de los planes básicos, el ticket medio sube por una razón que no es buena: pierdes la base de entrada. Compruébalo.

4. **La expansión tiene techo.** Los que subieron de plan pueden no volver a subir. Captar clientes nuevos cuesta dinero, y reemplazar bajas constantes es caro.

**Qué revisaría ahora:**

- GRR del último trimestre (y por cohortes, si puedes).
- Motivos de baja de los 4 clientes (encuesta de salida o soporte).
- Qué porcentaje del aumento de ingresos viene de los 3 o 5 clientes que más han subido.
- Logo churn mensual de los últimos 6 meses: ¿sube o baja?

**Conclusión:** el 114% dice que tu negocio extrae más valor de los clientes que se quedan, y eso es una buena señal. Pero no es razón para dejar de atender el churn. Yo lo trataría como prioridad junto con la captación, no como algo resuelto.