# Tencent Hy4 preview — business_audit/escalar_con_ltv_mal_calculado

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 64.746s | tokens_per_second: 58.8
- input_tokens: 228 | output_tokens: 3804

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

**Frena el camión. No le des.** 

Como analista de unit economics, mi trabajo es decirte que este plan tiene tres errores graves de concepto y aritmética. Si metes esos $10.000 en publicidad hoy, básicamente estás comprando una máquina de quemar dinero.

Aquí está el por qué tu cuenta no cierra y cuáles son tus números reales.

### Los 3 errores en tu cuenta

1. **Confundiste Facturación con Margen Bruto:** El LTV (Lifetime Value) **siempre** se calcula sobre el margen bruto (lo que realmente te queda en el bolsillo), nunca sobre el precio de venta. Al cliente le cobras $35, pero con un margen del 70%, a vos solo te entran **$24,50 limpios por mes**.
2. **El "Lifetime" no es de 2 años:** Si tu churn mensual es del 8%, la vida promedio de un cliente es `1 / 0.08 = 12,5 meses`. Para que un cliente promedio se quede 24 meses (2 años), tu churn tendría que ser del 4% mensual. 
3. **Matemática optimista:** $840 dividido $290 da **2,89**. Decís que está "por encima de 3 más o menos", pero 2,89 es menor que 3. En finanzas, el optimismo no paga las facturas.

---

### Tus verdaderos Unit Economics

Hagamos la cuenta como se debe hacer en el mundo real:

*   **Margen Bruto Mensual:** $24,50
*   **Vida Promedio del Cliente:** 12,5 meses
*   **LTV Real:** $24,50 × 12,5 = **$306,25**
*   **CAC:** $290
*   **Ratio LTV / CAC Real:** 306,25 / 290 = **1,05**

Un ratio sano para escalar es 3 o superior. Un ratio de **1,05** significa que, a lo largo de toda la vida de un cliente, apenas recuperas lo que gastaste para adquirirlo. 

### El Tiempo de Recupero (Payback Period)
Vas a tardar **11,8 meses** ($290 / $24,50) en recuperar lo que te costó la publicidad. Como el cliente se te va a los 12,5 meses, te queda **medio mes de ganancia bruta**. 

**¿Qué pasa si metes $10.000?**
A un CAC de $290, vas a comprar 34 clientes. Esos 34 clientes te van a generar una ganancia bruta total (después de pagar la publicidad) de apenas **$562 dólares en todo el próximo año**. 

¿Vas a pagar sueldos, alquiler, software y herramientas con $562 por un año entero? Imposible. Vas a fundir la caja.

---

### Cómo arreglar la ecuación para poder escalar

Para prender la manguera de la publicidad, necesitás que ese LTV/CAC esté cerca de 3. Tenés tres palancas para arreglar esto antes de gastar un peso:

1.  **Bajar el Churn (La más importante):** Si mejorás el onboarding o el producto y bajás el churn del 8% al 4% mensual, la vida del cliente sube a 25 meses. Tu LTV salta a **$612** y tu ratio LTV/CAC sube a 2,1. Mucho más sano.
2.  **Subir el precio:** Si el mercado lo tolera, subir el precio a $49/mes (manteniendo el 70% de margen) te deja $34,30 limpios por mes. Con un churn del 8%, tu LTV sube a $428.
3.  **Bajar el CAC:** ¿Podés optimizar tu landing page, mejorar tus copys o probar nuevos creativos? Si bajás el CAC a $150, el negocio cambia radicalmente.

**Conclusión:** No escales todavía. Usá este mes para atacar el churn o subir el precio. Cuando el LTV/CAC cruce la barrera del 3, ahí metele con todo.