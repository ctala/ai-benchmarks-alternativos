# Sakana Namazu — business_audit/retention_sobre_100_interpretacion

- model_id: `sakana/sakana-namazu`
- success: True  | final: 7.21 | quality: 8.0
- latency_total: 14.301s | tokens_per_second: 143.2
- input_tokens: 161 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No. Esa lectura es peligrosamente incorrecta.**

Una Retención de Ingresos del 114 % (en realidad, **Net Revenue Retention** o NRR) no significa que no se te vaya nadie. Significa que los clientes que te quedan están pagando lo suficiente como para compensar las bajas e, incluso, superar los ingresos del mes anterior.

Con tus números, la realidad es mucho menos halagüeña:

*   **Retención de clientes (*logo retention*):** Caíste de 40 a 36. Eso es una pérdida del **10 % de clientes en un mes**. Annualizado, eso se acerca a un *churn* anual de clientes del ~70 %. En SaaS, eso es catastrófico.
*   **Retención de ingresos (NRR):** 114 %. Los 36 clientes que se quedaron subieron de plan (expansión/upsell) y generaron 14 % más de ingresos que los 40 originales.

---

### Por qué no puedes ignorar el *churn*

**1. Estás perdiendo 1 de cada 10 clientes cada mes.**  
Aunque tus clientes restantes sean muy grandes o estén expandiendo mucho, un *churn* del 10 % mensual de clientes significa que tu base se estás desgastando. Captar nuevos clientes para un barco que pierde 10 % de su tripulación mensualmente es extremadamente ineficiente.

**2. Dependes de pocos clientes para crecer.**  
Si la expansión viene de un puñado de cuentas grandes, tu negocio es frágil. La pérdida de uno o dos de esos "salvadores" podría hacer que tu NRR del 114 % se desplome al 80 % en un solo mes.

**3. Es más caro reemplazar que retener.**  
Necesitarás contratar, gastar en marketing y hacer *sales* solo para volver a tener 40 clientes… y luego otros 4 para crecer. Eso destruye tu *Payback Period* y tu *Customer Acquisition Cost* (CAC).

---

### Lo que debes hacer

No se trata de elegir entre retención o captación. **Debes hacer las dos, pero priorizar diagnosticar la fuga:**

1.  **Entender por qué se fueron esos 4 clientes.** ¿Fue * onboarding*? ¿Falta de valor? ¿Precio? ¿Product-market fit?
2.  **Medir por separado.** Tu panel debería mostrar:
    *   **Gross Revenue Retention (GRR):** Cuánto ingreso conservas sin contar expansiones. Con tus números, probablemente esté por debajo del 90 %.
    *   **Net Revenue Retention (NRR):** Ese 114 % que ya ves.
    *   **Logo Churn:** El 10 % mensual que debería estar en rojo.
3.  **No destinar "todo" al esfuerzo de captación.** Una buena regla práctica: si pierdes más del 