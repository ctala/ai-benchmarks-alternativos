# DeepSeek V4 Flash 0731 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 9.05 | quality: 10.0
- latency_total: 30.903s | tokens_per_second: 234.1
- input_tokens: 224 | output_tokens: 7233

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

No te lo aprobaría. El plan muere en la aritmética.

Tu cliente **no se queda 2 años** si el churn mensual es 8%. El tiempo de vida medio esperado es:

\[
\frac{1}{8\%} = 12.5 \text{ meses}
\]

Y hay que usar margen bruto, no precio:

\[
35 \times 70\% = \$24.5 \text{ por cliente al mes}
\]

Entonces el LTV real es:

\[
24.5 \times 12.5 = \$306.25
\]

Contra un CAC de \$290:

\[
LTV/CAC = \frac{306.25}{290} = 1.06
\]

Eso no es casi 3. Es, literalmente, quedarte con \$16 por cliente antes de cualquier otro costo.

Además, tu payback es:

\[
\frac{290}{24.5} = 11.8 \text{ meses}
\]

Pero con 8% de churn mensual, solo sobrevive al mes 12:

\[
0.92^{12} \approx 37\%
\]

O sea, la mayoría de los clientes nuevos se van antes de devolver el CAC. El promedio positivo sale de unos pocos clientes long-tail; es un modelo frágil para meter \$10.000.

Si metes \$10.000 con CAC de \$290, traes unos 34-35 clientes. Su LTV total esperado sería:

\[
34.5 \times 306.25 = \$10,565
\]

Beneficio esperado total: **\$565**, antes de impuestos, costos fijos, refunds y desviaciones. Eso no es escalar fuerte; es casi jugar ruleta.

Para aprobar publicidad con esta estructura, necesitarías:

- Reducir CAC a **≈\$100** manteniendo churn de 8%, o
- Bajar churn mensual a **≈2.8%** manteniendo CAC \$290.

Ni lo uno ni lo otro con esos números. **No lo doy por ahora.**