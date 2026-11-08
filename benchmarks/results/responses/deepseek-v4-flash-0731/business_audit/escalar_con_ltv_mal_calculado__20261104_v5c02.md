# DeepSeek V4 Flash 0731 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 9.13 | quality: 10.0
- latency_total: 23.344s | tokens_per_second: 201.5
- input_tokens: 282 | output_tokens: 4703

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

No le des. Con esos números, escalar con publicidad pagada te va a dejar casi en cero o en pérdida si algo se desvía.

Tu error está en dos puntos:

1. **Vida media del cliente no es 24 meses.**  
   Con churn mensual de 8%, la vida media es:

   \[
   1 / 0.08 = 12.5 \text{ meses}
   \]

   No 24 meses. De hecho, la mitad de tus clientes ya se fue antes del mes 8.3.

2. **LTV se calcula con margen bruto, no con precio.**  
   Tu margen mensual por cliente es:

   \[
   35 \times 70\% = 24.50
   \]

   Entonces:

   \[
   LTV = 24.50 \times 12.5 = 306.25
   \]

   Contra un CAC de $290:

   \[
   LTV/CAC = 306.25 / 290 = 1.06
   \]

   Eso no es 2.9. Es prácticamente 1.

---

### Lo que significa en la práctica

- Por cada cliente pagado, apenas ganas $16.25 de margen sobre el CAC, antes de costos fijos.
- Con $10,000 en ads adquieres ~34 clientes.
- El valor total esperado de ese cohorte es:

\[
34 \times 306.25 \approx 10,565
\]

  O sea, ganancia marginal esperada: ~$565.  
  Un solo ajuste en el churn o un cohorte malo te deja en negativo.

- Tu payback simple es:

\[
290 / 24.50 = 11.8 \text{ meses}
\]

  Pero con 8% de churn mensual, solo ~37% de los clientes sigue al mes 12. La mayoría no alcanza a pagar su CAC.

---

### Para escalar con ads necesitas algo como LTV/CAC ≥ 3

Con tu LTV real de $306, tu CAC máximo para un ratio de 3 sería:

\[
306.25 / 3 \approx 102
\]

O sea, necesitas bajar el CAC de $290 a ~$100, o bajar el churn drásticamente. Por ejemplo, para tener LTV/CAC = 3 con CAC $290, necesitarías un churn mensual de ~2.8%, no 8%.

---

**Conclusión: no metas $10,000 en publicidad con estos números.** Primero baja CAC, mejora retención o sube precio/margen. Si no, estarías comprando clientes que apenas se pagan a sí mismos, sin dejar dinero real para crecer.