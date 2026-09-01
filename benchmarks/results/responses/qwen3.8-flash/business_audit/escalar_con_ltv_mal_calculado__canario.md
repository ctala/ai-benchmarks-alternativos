# Qwen 3.8 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 129.453s | tokens_per_second: 80.5
- input_tokens: 255 | output_tokens: 10415

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

No. **Con estos números, no le des al $10.000 en publicidad para escalar fuerte.** El plan muere en la aritmética.

## Respuesta corta

Tu cálculo tiene dos errores grandes:

1. **Estás usando ingreso por cliente, no margen bruto.**  
   El LTV/CAC debe medirse con **margen bruto o contribución**, no con ingresos puros.

2. **Con 8% de churn mensual, un cliente no vive 2 años en promedio.**  
   Vive aproximadamente **12,5 meses**, no 24.

Con tus propios números, la economía unitaria es muy frágil:

- Precio: **$35/mes**
- Margen bruto: **70%**
- Margen bruto mensual por cliente:  
  **$35 × 0,70 = $24,50/mes**
- Churn mensual: **8%**
- Vida promedio del cliente:  
  **1 / 0,08 = 12,5 meses**
- LTV bruto correcto:  
  **$24,50 / 0,08 = $306,25**
- CAC: **$290**

Entonces:

**LTV/CAC = $306,25 / $290 = 1,06**

No es 2,9. Es **1,06**.

Y ojo: **1,06 no significa que ganas bien**. Significa que, después de pagar publicidad y costos variables, cada cliente te deja solo:

**$306,25 − $290 = $16,25**

de margen bruto acumulado durante toda su vida promedio, antes de soporte, operaciones, equipo, herramientas, administración, refunds, ventas, etc.

Eso no escala. Eso se apaga.

---

## Tu cálculo original, corregido

Tú hiciste:

**$35 × 24 meses = $840**

Eso es ingreso bruto asumiendo 24 meses de vida.

Pero dos problemas:

### 1. $840 no es tu LTV económico

De esos $840, solo te quedan $24,50 por mes como margen bruto.

Si realmente durara 24 meses, el margen bruto sería:

**$24,50 × 24 = $588**

Y aún así:

**$588 / $290 = 2,03**

Sigue estando debajo del 3x.

### 2. 24 meses no es consistente con 8% de churn mensual

Con 8% de churn mensual, retención mensual es 92%.

Supervivencia después de 12 meses:

**0,92¹² ≈ 37%**

Después de 24 meses:

**0,92²⁴ ≈ 13%**

Es decir, la mayoría se va mucho antes de los 2 años.

La vida promedio correcta es:

**1 / churn = 1 / 0,08 = 12,5 meses**

---

## Payback: aquí también se complica

Puedes pensar: “Bueno, si el cliente paga $24,50/mes de margen, recupero los $290 de CAC en 11,8 meses”.

Eso sería si **todos los clientes vivieran más de 12 meses**.

Pero con 8% de churn mensual, no.

El margen bruto esperado acumulado por cohorte se calcula así:

**$24,50 × [1 − 0,92^t] / 0,08**

Algunos números aproximados por cliente:

| Tiempo | Margen bruto esperado acumulado |
|---:|---:|
| 6 meses | ~$121 |
| 12 meses | ~$194 |
| 24 meses | ~$265 |
| 35 meses | ~$290 |

Es decir, en promedio, un cliente con estos números **recupera su CAC alrededor del mes 35**, no en 12 meses.

Eso es un problema grave de caja y riesgo.

---

## ¿Qué pasa si metes $10.000 este mes?

Con CAC de $290:

**$10.000 / $290 ≈ 34,5 clientes nuevos**

Ese mes, esos clientes generan:

**34,5 × $24,50 ≈ $845/mes de margen bruto**

Si solo gastas $10.000 una vez, esa cohorte genera:

- En 12 meses: aproximadamente **$6.700** de margen bruto esperado.
- En 24 meses: aproximadamente **$9.100** de margen bruto esperado.

Es decir, después de un año, esa cohorte todavía no te devolvió los $10.000.

Y eso es solo margen bruto. No incluye:

- tu equipo,
- soporte,
- herramientas,
- administración,
- impuestos,
- refunds,
- costos de ventas,
- operación,
- riesgo de que el CAC suba al escalar.

Así que el agujero real puede ser mayor.

---

## Qué necesitarías para que el plan se apruebe

Para una empresa SaaS/subscription, un piso razonable suele ser:

**LTV/CAC ≥ 3**  
y, idealmente, **payback ≤ 6–12 meses**.

Con tus números actuales, tienes varias opciones.

### Opción A: bajar CAC

Para que LTV/CAC sea 3x con LTV bruto de $306,25:

**CAC máximo = $306,25 / 3 ≈ $102**

Hoy estás en $290.

Necesitarías bajar el CAC a aproximadamente:

**$102**

Eso es una reducción del 65%.

---

### Opción B: bajar churn

Para que con CAC de $290 tengas LTV/CAC de 3x:

Necesitas:

**LTV bruto = $290 × 3 = $870**

Con margen mensual de $24,50, necesitas vida promedio:

**$870 / $24,50 ≈ 35,5 meses**

Churn mensual equivalente:

**1 / 35,5 ≈ 2,8%**

Es decir, tendrías que bajar el churn de:

**8% mensual → 2,8% mensual**

Eso es muchísimo.

---

### Opción C: subir precio o margen

Si mantienes churn de 8% y CAC de $290, para LTV/CAC de 3x necesitas:

**LTV bruto = $870**

Como:

**LTV bruto = precio × margen % / churn**

Entonces:

**precio × margen % = $870 × 0,08 = $69,60**

Si tu margen bruto sigue siendo 70%:

**precio = $69,60 / 0,70 ≈ $99,40/mes**

Es decir, con los demás números igual, necesitarías cobrar alrededor de:

**$99–100/mes**, no $35.

---

### Opción D: agregar expansión de ingresos

Si el producto tiene upsells, cross-sells, seats, features, usage-based pricing, etc., el LTV puede subir.

Pero con los números que me diste, no hay evidencia de eso.

El LTV bruto actual es $306,25. Para llegar a 3x con CAC de $290, necesitas $870 de LTV bruto.

Faltarían:

**$870 − $306,25 = $563,75**

de margen bruto adicional por cliente.

Eso no es un ajuste pequeño.

---

## Regla práctica para este caso

Con tus números actuales:

| Métrica | Valor |
|---|---:|
| Precio | $35/mes |
| Margen bruto | 70% |
| Margen mensual por cliente | $24,50 |
| Churn | 8% mensual |
| Vida promedio | 12,5 meses |
| LTV bruto | $306,25 |
| CAC | $290 |
| LTV/CAC | 1,06 |
| Margen bruto después de CAC | $16,25 |

Eso no es un negocio que pueda escalar fuerte con paid ads.

Es un negocio donde cada cliente nuevo, en promedio, apenas cubre su costo de adquisición.

---

## Mi recomendación como analista

**No apruebo el plan de escalar con $10.000 en publicidad este mes.**

No porque el churn sea alto, o el CAC sea alto, o el precio sea bajo por separado. Es porque **la combinación no funciona**.

Antes de meter más plata en ads, necesitas arreglar una o varias de estas variables:

1. **Bajar CAC**  
   De $290 a menos de $102 si quieres 3x.

2. **Bajar churn**  
   De 8% mensual a menos de 3% mensual si quieres 3x.

3. **Subir precio o margen**  
   De $35/mes a casi $100/mes, o mejorar la estructura de costos.

4. **Añadir ingresos por cliente**  
   Expansión, upsells, annual plans, usage-based pricing, referrals, etc.

5. **Cambiar el modelo de adquisición**  
   Quizá paid ads no es el canal correcto para este ticket, este churn y este margen.

---

## ¿Puedes gastar $10.000 igual?

Solo si no es “escalar fuerte”, sino un **experimento limitado de aprendizaje**.

Por ejemplo:

- gastar $1.000–$2.000,
- medir cohortes reales,
- ver si el churn mejora con onboarding,
- probar precios más altos,
- probar annual plans,
- probar canales más baratos,
- validar si el CAC sube o baja al escalar.

Pero como plan de crecimiento agresivo: **no**.

Si ya eres rentable, no quieres usar esa rentabilidad para comprar un canal que destruye valor.

---

## Veredicto final

**No le des.**

Tu LTV/CAC real, usando margen bruto y churn, es aproximadamente:

**1,06**

No 2,9.

Con $290 de CAC y $306 de LTV bruto, cada cliente te deja solo $16 de margen bruto durante toda su vida promedio, antes de otros costos.

Para escalar fuerte, necesitas al menos algo como:

**CAC ≤ $102**  
o  
**churn ≤ 2,8% mensual**  
o  
**precio/margen mucho más alto**  
o  
**expansión de ingresos significativa**.

Hoy, la aritmética no aprueba el plan.