# Claude Haiku 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.77 | quality: 8.0
- latency_total: 8.366s | tokens_per_second: 164.6
- input_tokens: 218 | output_tokens: 1377

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, esa conclusión no es correcta. Un NRR de 114% no significa que no se vaya nadie.

**Qué mide realmente el NRR**

Es el ingreso que hoy genera el grupo de clientes que ya tenías, dividido entre lo que generaban antes. Suma tres cosas:

- **Expansión** (upgrades, más asientos, más uso)
- **Contracción** (downgrades)
- **Churn** (cancelaciones)

Un 114% puede salir aunque pierdas clientes, si la expansión de los que se quedan compensa con holgura lo que perdiste.

**Tus números apuntan justo a eso**

Pasaste de 40 a 36 clientes de pago, es decir, perdiste alrededor del 10% de tus cuentas en un mes (si además entraron clientes nuevos, el churn real es mayor que ese neto). Mientras tanto, el ingreso de los que quedan subió. Eso es una señal de alarma disfrazada de buena métrica: tu base de clientes se está encogiendo y depende más de unos pocos que suben de plan.

**Qué haría antes de decidir nada**

1. **Mira el logo churn por separado**: porcentaje de clientes perdidos en el periodo, sin mezclar con ingresos.
2. **Calcula el GRR (Gross Revenue Retention)**: igual que el NRR pero excluyendo la expansión. Si está muy por debajo de 100%, estás perdiendo base aunque el NRR se vea bien.
3. **Descompón el 114%**: cuánto viene de upgrades y cuánto de compensar caídas. Si unos pocos clientes grandes explican casi todo, el riesgo de concentración es alto.
4. **Revisa quién se fue**: si son los pequeños, puede ser menos grave; si son clientes con uso activo o de tamaño medio, es un problema de producto o de valor percibido.
5. **Mira ventanas más largas**: un solo mes es ruidoso. El NRR suele analizarse en ventanas de 12 meses por cohortes.

**Sobre tu pregunta de fondo**

No puedes dejar de preocuparte por el churn. Con 36 clientes, perder uno o dos cambia mucho la foto, y adquirir nuevos cuesta dinero mientras que retener a los que tienes suele ser más barato. Antes de redistribuir el esfuerzo de captación, averigua por qué se fueron los 4 (o más) y si la expansión de este mes se repite o fue puntual.