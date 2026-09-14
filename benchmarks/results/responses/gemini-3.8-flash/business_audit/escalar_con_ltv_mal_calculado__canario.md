# Gemini 3.8 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 16.513s | tokens_per_second: 137.5
- input_tokens: 192 | output_tokens: 2271

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

**No. Ni se te ocurra meter esos $10.000.** 

Tu plan no tiene un LTV/CAC de 2,9; **tiene un LTV/CAC de 1,05**. Estás al borde de incinerar capital.

Aquí está la autopsia de tus números:

---

### 1. El error del tiempo de vida (Lifespan)
Dijiste que un cliente dura 2 años (24 meses). La matemática del churn mensual dice otra cosa:
$$\text{Vida media del cliente} = \frac{1}{\text{Churn}} = \frac{1}{0,08} = 12,5 \text{ meses}$$

Tus clientes no se quedan 24 meses; se quedan **12,5 meses en promedio**. A los 24 meses, con un 8% de churn mensual, solo te queda el **13,5%** de la cohorte original.

---

### 2. El error del Margen Bruto en el LTV
El LTV se calcula sobre el **Margen Bruto**, no sobre los ingresos brutos. El procesador de pagos y los servidores no te devuelven el dinero.

* Ingreso mensual: $35
* Margen bruto (70%): **$24,50** por mes

$$\text{LTV Real} = \frac{\text{Ingreso mensual} \times \text{Margen}}{\text{Churn}} = \frac{24,50}{0,08} = \$306,25$$

---

### 3. La realidad de tus Unit Economics

| Métrica | Tu cálculo | Realidad |
| :--- | :--- | :--- |
| **LTV** | $840 | **$306,25** |
| **CAC** | $290 | **$290** |
| **LTV / CAC** | **2,9x** | **1,05x** |
| **CAC Payback** | — | **11,8 meses** |

---

### Por qué esto es letal:

1. **Payback tardío en un balde roto:** Necesitas casi **12 meses** ($290 / $24,50) solo para recuperar lo que te costó adquirir al usuario. Pero con un churn del 8% mensual, **el 63% de los usuarios que compres hoy se habrán ido antes de que recuperes su CAC**. Estás subsidiando a los que se van con los pocos que se quedan, para ganar apenas $16 netos por cliente a lo largo de toda su vida.
2. **La trampa de escalar CAC:** El CAC de $290 es tu costo actual. Cuando inyectes $10.000 de golpe, la saturación de audiencia y la menor intención de compra casi seguro empujarán tu CAC por encima de los $310. **Automáticamente pasarás a tener LTV/CAC negativo.**
3. **Flujo de caja:** Pones $10.000 hoy para comprar ~34 clientes. Esos clientes te van a generar solo **$845** de margen bruto el primer mes. Financiar ese hueco de flujo de caja te va a quebrar.

### Qué hacer en su lugar:

* **No aceleres:** Tienes un balde con un agujero enorme (8% mensual es ~63% de churn anual; un SaaS B2B sano suele buscar < 1-2% mensual, y B2C < 3-5%).
* **Sube precios o empaqueta anual:** Si cobras $350 al año por adelantado, eliminas el churn de corto plazo y financias el CAC el día uno.
* **Retención primero:** Si logras bajar el churn del 8% al 4%, tu LTV salta a $612, y tu ratio pasa a 2,1x.

**Conclusión:** Tu negocio no está listo para pauta pagada a escala. Arregla la retención y la monetización antes de poner gasolina.