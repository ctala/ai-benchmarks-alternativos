# Fugu Max — business_audit/escalar_con_ltv_mal_calculado

- model_id: `sakana/fugu-max`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 21.453s | tokens_per_second: 58.2
- input_tokens: 259 | output_tokens: 1248

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

No lo aprobaría **con esos números**. Hay dos errores clave:

1. **La vida media no es 24 meses.**  
   Con un churn mensual constante de 8%:

   \[
   \text{vida media}=\frac{1}{0.08}=12.5\text{ meses}
   \]

2. **El LTV debe usar margen bruto si lo comparas contra CAC.**

   \[
   \text{LTV}=\frac{\$35 \times 70\%}{8\%}
   =\frac{\$24.50}{0.08}
   =\$306.25
   \]

   Por tanto:

   \[
   \text{LTV/CAC}=\frac{306.25}{290}=1.06
   \]

Eso es muy distinto de 2.9, y está lejos de un objetivo habitual de 3x.

### Economía por cliente

- Ingreso mensual: **$35**
- Margen bruto mensual: **$24.50**
- CAC: **$290**
- Payback:

  \[
  290 / 24.5 = 11.8\text{ meses}
  \]

- LTV bruto antes de CAC: **$306.25**
- Margen de contribución después del CAC durante toda la vida esperada:

  \[
  306.25-290=\$16.25
  \]

Y esos $16.25 son **antes** de salarios, ventas, soporte, overhead, descuentos, impagos, impuestos y costo de capital. En la práctica, la adquisición probablemente sea poco o nada rentable.

### Qué ocurre con los $10.000

A un CAC de $290 comprarías aproximadamente:

\[
10{,}000/290=34.5
\]

clientes.

El margen bruto mensual inicial sería aproximadamente:

\[
34.5 \times 24.5=\$845
\]

Pero el valor total esperado del margen bruto de esa cohorte sería solo:

\[
34.5 \times 306.25 \approx \$10{,}560
\]

frente a $10.000 de publicidad, sin descontar el tiempo ni otros costes. Es un margen esperado de apenas unos **$560**, que desaparecería con pequeñas desviaciones en CAC, churn o margen.

### Recomendación

**No escalaría fuerte todavía.** Puedes hacer un test controlado, pero no comprometería los $10.000 como presupuesto de expansión sin validar:

- CAC por canal y por cohorte.
- Churn real de clientes adquiridos por publicidad.
- Tiempo hasta conversión y payback.
- Retención neta y cancelaciones tempranas.
- Costos variables adicionales no incluidos en el 70%.

Con estos supuestos, para llegar a un LTV/CAC de 3x el CAC máximo sería:

\[
306.25/3 \approx \$102
\]

Así que necesitas aproximadamente una de estas mejoras:

- bajar CAC de $290 a cerca de **$100**;
- reducir el churn mensual de 8% a aproximadamente **2.8%** o menos;
- aumentar precio o margen;
- mejorar la retención y monetización de clientes.

**Veredicto: no le des todavía como estrategia de escala.** Si gastas los $10.000, trátalos como presupuesto de experimento con límites y criterios de corte, no como una inversión que ya demostró ser rentable.