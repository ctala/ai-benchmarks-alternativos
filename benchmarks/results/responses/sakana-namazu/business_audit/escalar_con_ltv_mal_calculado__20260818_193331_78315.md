# Sakana Namazu — business_audit/escalar_con_ltv_mal_calculado

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 14.931s | tokens_per_second: 185.5
- input_tokens: 231 | output_tokens: 2769

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

**No le doy.** 

Y no es por conservador. Es que tu aritmética está muerta y ese plan transforma $10.000 en capital quemado. Aquí está la autopsia.

---

### 1. El error de cálculo del LTV
Tú tomaste ingreso bruto ($35) y una vida útil inventada (24 meses). Eso no es LTV, es fantasía contable.

La fórmula básica de LTV con churn mensual es:

> **LTV = (Precio × Margen Bruto) / Churn Mensual**

Con tus números reales:
- **LTV = ($35 × 0,70) / 0,08 = $306,25**

Tu LTV real no es $840. Es **$306**.

---

### 2. El CAC vs. LTV real
- **LTV real:** ~$306
- **CAC pagado:** $290
- **Ratio LTV/CAC:** **1,05**

Un ratio 1:1 significa que gastas un dólar para recuperar un dólogo a lo largo de la vida del cliente. **Estás regalando el negocio a Facebook/Google.** La regla del 3:1 que mencionas ni siquiera está cerca.

---

### 3. Por qué "2 años" es un delirio con 8% de churn
Con un churn del 8% mensual, tu vida media esperada es:

> **1 / 0,08 = 12,5 meses**

No 24. A los 12 meses solo sigue vivo el **37%** de tu cohorte. A los 24 meses, sobrevive el **14%**.

Tu cálculo de 24 meses solo describe a tu cliente *más leal*, no a tu cliente promedio. Y es el promedio el que paga las cuentas.

---

### 4. El agujero de caja (payback period)
Recuperas el CAC con el margen mensual:

> **Payback = $290 / ($35 × 0,70) = ~11,8 meses**

Necesitas casi 12 meses solo para recuperar lo que invertiste. Con 8% de churn mensual, una parte masiva de esos clientes se irá antes de que siquiera hayas cubierto su costo de adquisición.

Si metes $10.000 este mes, adquieres ~34 clientes. Al mes siguiente pierdes ~3 de ellos antes de recuperar ni un centavo de su CAC.

---

### 5. Qué necesitas para poder escalar (sin matar el negocio)
Para llegar a un ratio saludable (>3:1) con un CAC de $290, tu LTV debería ser >$870. Con tu margen del 70%, necesitarías:

- **Opción A:** Bajar el churn a **~2,8% mensual** (rendimiento completamente diferente de producto), o
- **Opción B:** Subir el precio a ~**$100/mes** manteniendo el churn, o
- **Opción C:** Bajar el CAC a **~$100** mientras optimizas retención.

Con 8% de churn a $35, **escalar con paid ads es suicidio de capital**.

---

### Veredicto
Congela los $10.000. No inviertas un peso más en adquisición pagada hasta que:
1. Bajes ese churn mensual (8% es brutal para un negocio de $35/mes; equivale a ~63% anual).
2. Subas el ticket promedio o encuentres canales con CAC < $100.
3. Valides que tu CAC de $290 incluye *todos* los costos (herramientas, salarios, creativos), porque si es solo ad spend, la cifra real es peor.

Muchos planes mueren en la aritmética. El tuyo acaba de fallecer aquí. Soluciona la unit economics primero; el crecimiento es un lujo de quienes ya la tienen sana.
