# Qwen 3.8 Max — business_audit/retention_sobre_100_interpretacion

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 6.73 | quality: 8.0
- latency_total: 72.396s | tokens_per_second: 47.2
- input_tokens: 181 | output_tokens: 3417

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. La lectura correcta es **justa al revés**: una retención de ingresos del 114% **no significa** que no se te vaya nadie, y tampoco significa que la retención de clientes esté por encima del 100%.

## Qué significa “retención de ingresos: 114%”

Si tu panel habla de retención de ingresos, casi seguro está midiendo algo parecido al **Net Revenue Retention** o retención neta de ingresos:

\[
\text{NRR} = \frac{\text{Ingresos actuales de la base existente}}{\text{Ingresos iniciales de esa base}} \times 100
\]

Incluye:

- clientes que se dieron de baja,
- clientes que bajaron de plan,
- clientes que subieron de plan,
- expansiones, upsells, etc.

Un 114% significa algo así:

> “Empecé con 100 € de MRR de mis clientes existentes y ahora esos mismos clientes me dan 114 € de MRR, incluso después de bajas y bajadas de plan.”

Eso puede pasar si los clientes que se quedan gastan más.

Pero **no significa**:

> “El 114% de mis clientes sigue conmigo.”

Eso no tiene sentido en retención de clientes. La retención de clientes o logo retention, como mucho, puede ser 100%.

---

## Tu caso concreto

Dices:

- mes pasado: 40 clientes de pago;
- este mes: 36 clientes de pago;
- varios subieron de plan.

Si asumimos que no hubo clientes nuevos y que los 36 actuales vienen de los 40 anteriores:

\[
\text{Retención de clientes} = \frac{36}{40} = 90\%
\]

\[
\text{Churn de clientes} = \frac{4}{40} = 10\%
\]

Si además hubo clientes nuevos este mes, entonces la retención real de clientes antiguos sería todavía menor, porque parte de esos 36 podrían ser nuevos y no clientes retenidos.

Así que, con los datos que das, tu retención de clientes **no está por encima del 100%**. Como mucho, estaría en torno al 90%.

---

## Ejemplo simple

Imagina que el mes pasado tenías:

- 40 clientes;
- cada uno pagaba 100 €;
- MRR total: 4.000 €.

Este mes se van 4 clientes:

- pierdes 400 € de MRR.

Pero los 36 restantes suben de plan y pasan a pagar, por ejemplo, 126,67 € de media:

\[
36 \times 126,67 \approx 4.560 €
\]

Comparado con los 4.000 € iniciales:

\[
\frac{4.560}{4.000} = 114\%
\]

Resultado:

- pierdes 4 clientes;
- tu retención de clientes es 90%;
- pero tu retención de ingresos es 114%.

Eso es perfectamente posible.

---

## Entonces, ¿puedes olvidarte del churn?

No. Sería un error.

Una retención de ingresos del 114% es buena señal, pero puede estar escondiendo un problema: estás perdiendo clientes y compensándolo con expansiones de los que se quedan.

Eso puede ser sano si la expansión es sólida, pero puede ser frágil si:

1. **Dependes de unos pocos clientes que suben de plan.**  
   Si esos clientes se van o dejan de crecer, el 114% se cae.

2. **Tu churn de clientes es alto.**  
   Perder 4 de 40 es un 10%. Si eso se repite cada mes, necesitas captar o expandir mucho constantemente.

3. **La expansión no es sostenible.**  
   Puede venir de un cambio de plan puntual, un descuento, una migración anual, un uso temporal, etc.

4. **Estás tapando un problema de producto o de valor.**  
   Si los clientes se van, aunque otros paguen más, conviene entender por qué se van.

---

## Métricas que deberías separar

Para no engañarte, mira al menos estas tres:

### 1. Retención de clientes / logo retention

\[
\frac{\text{Clientes que siguen}}{\text{Clientes iniciales}}
\]

Te dice si se te va mucha gente.

En tu caso, aproximadamente 90% si no hubo nuevos.

---

### 2. Retención bruta de ingresos / Gross Revenue Retention

Mide cuánto ingreso conservas de la base existente **sin contar expansiones**.

\[
\text{GRR} = \frac{\text{MRR inicial} - \text{contracción} - \text{churn}}{\text{MRR inicial}}
\]

Esta métrica no puede superar el 100%.

Si tu GRR es bajo, significa que tu base de ingresos se erosiona y dependes demasiado del upsell.

---

### 3. Retención neta de ingresos / Net Revenue Retention

Esa es probablemente la del 114%.

Incluye expansión:

\[
\text{NRR} = \text{GRR} + \text{expansión}
\]

Un NRR alto es bueno, pero hay que verlo junto con el GRR y el churn de clientes.

---

## Conclusión

Tu panel no dice “no se me va nadie”.

Lo que probablemente dice es:

> “Los clientes que se quedan están gastando más que antes.”

Pero tus datos muestran otra cosa:

> “He pasado de 40 a 36 clientes, así que sí se ha ido gente.”

Por tanto, no deberías dejar de preocuparte por el churn. Deberías hacer esto:

1. Confirmar si ese 114% es **NRR**.
2. Calcular tu **churn de clientes**.
3. Calcular tu **GRR**.
4. Ver cuánta expansión tienes y si está concentrada en pocos clientes.
5. Hablar con los clientes que se fueron.
6. No basar todo el crecimiento en captar clientes nuevos si estás perdiendo el 10% mensual.

La lectura correcta es:

> “Tengo una buena capacidad de expansión, pero también tengo churn. No puedo ignorarlo.”