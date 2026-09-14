# Fugu Max — business_audit/retention_sobre_100_interpretacion

- model_id: `sakana/fugu-max`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 15.094s | tokens_per_second: 105.1
- input_tokens: 201 | output_tokens: 1586

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No exactamente. **114% de retención de ingresos no significa 114% de retención de clientes**.

Normalmente, esa métrica es la **NRR (Net Revenue Retention)**:

\[
\text{NRR}=\frac{\text{ingresos iniciales} - \text{churn} - \text{contracciones} + \text{expansiones}}{\text{ingresos iniciales}}
\]

Un 114% significa que la cohorte de clientes que ya tenías al inicio genera ahora un **14% más de ingresos en conjunto**, contando upgrades y descontando las bajas. No cuenta, en principio, los ingresos de clientes nuevos.

Con tus datos:

- Si tenías 40 clientes y ahora quedan 36, y esos 4 se fueron, tu **retención de clientes** sería del 90% y tu **churn de clientes** del 10%.
- Si algunos de los 36 son clientes nuevos, entonces la retención de los clientes originales es incluso menor: no puedes calcularla solo con el total actual.
- La retención de clientes no puede ser normalmente superior al 100%; la de ingresos sí puede serlo por las expansiones.

Ejemplo simplificado: si los 40 clientes generaban 4.000 € y cuatro se van, los 36 restantes tendrían que generar 4.560 € para que la NRR fuese del 114%. Es posible, pero implica que los clientes supervivientes han ampliado bastante su gasto.

Por tanto, **no dejes de preocuparte por el churn**. La lectura correcta es:

- **Buena señal:** los clientes que permanecen están ampliando su relación contigo.
- **Señal preocupante:** estás perdiendo clientes, posiblemente a un ritmo relevante.
- **Riesgo:** unas pocas cuentas grandes pueden estar ocultando un churn amplio en cuentas pequeñas.

Deberías mirar al menos estas métricas por separado:

1. **Logo retention:** clientes iniciales que siguen activos / clientes iniciales.
2. **Logo churn:** clientes iniciales perdidos / clientes iniciales.
3. **GRR (Gross Revenue Retention):** ingresos retenidos sin contar expansiones.
4. **NRR:** ingresos retenidos contando expansiones.
5. Churn y expansión por segmento, plan, antigüedad y tamaño de cliente.

Puedes seguir invirtiendo en captación, porque una NRR del 114% suele ser una señal positiva de potencial de expansión, pero no sustituye a resolver el churn. Crecer adquiriendo clientes mientras pierdes muchos de los actuales puede producir crecimiento frágil y caro.