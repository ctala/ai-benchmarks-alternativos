# GPT-5.6 Luna Pro — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 13.327s | tokens_per_second: 235.1
- input_tokens: 4652 | output_tokens: 3133

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No exactamente. **“Retención de ingresos: 114%” probablemente significa NRR (Net Revenue Retention)**, no retención de clientes.

### Qué significa el 114%

La NRR mide cuánto ingreso generó este mes la **misma base de clientes que ya existía el mes pasado**, contando:

- bajas,
- reducciones de plan,
- ampliaciones,
- compras adicionales,

pero normalmente **excluyendo clientes nuevos**.

Una NRR del 114% significa que esa cohorte genera ahora un 14% más de ingresos que antes. La expansión de algunos clientes compensa las pérdidas y contracciones de otros.

### Qué ocurre con tus clientes

Si los 40 clientes del mes pasado son los mismos que estás siguiendo y no hubo clientes nuevos:

- Clientes iniciales: 40
- Clientes actuales: 36
- Clientes perdidos: 4
- **Retención de clientes —logo retention—: 36 / 40 = 90%**
- **Churn de clientes: 10%**

Por tanto, puedes tener simultáneamente:

- **Retención de ingresos: 114%**
- **Retención de clientes: 90%**

No es contradictorio. Por ejemplo, si los cuatro clientes perdidos eran pequeños y varios de los restantes ampliaron mucho su plan, los ingresos pueden crecer aunque pierdas clientes.

### No conviene dejar de preocuparte por el churn

Una NRR superior al 100% es una señal positiva, pero puede ocultar problemas:

- la expansión puede depender de pocos clientes grandes;
- el churn de clientes puede dificultar el crecimiento futuro;
- los clientes que se van podrían ser precisamente los más fáciles de retener o los de un segmento estratégico;
- las ampliaciones actuales podrían no repetirse;
- si pierdes muchos clientes pequeños, quizá exista un problema de producto, precio o onboarding.

Mira al menos estas métricas por separado:

1. **Logo retention / retención de clientes**
2. **Logo churn**
3. **GRR (Gross Revenue Retention)**: ingresos retenidos sin contar expansiones; muestra mejor la pérdida real.
4. **NRR**: incluye expansiones.
5. **Expansión y churn por segmento**
6. **Concentración de ingresos**: cuánto depende la NRR de los clientes grandes.

Además, confirma que el panel calcula la retención sobre una **cohorte inicial** y que no incluye ingresos de clientes nuevos. Si el número de 36 incluye nuevos clientes, entonces no puedes calcular la retención de la cohorte simplemente como 36/40.

La lectura correcta sería: **“Estoy expandiendo bien los ingresos de la base existente, pero aparentemente estoy perdiendo clientes a un ritmo del 10%, si no hubo altas nuevas.”** Captación y reducción del churn deberían seguir siendo esfuerzos complementarios, no sustituirse entre sí.