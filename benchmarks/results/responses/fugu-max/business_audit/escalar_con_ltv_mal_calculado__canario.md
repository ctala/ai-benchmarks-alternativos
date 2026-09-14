# Fugu Max — business_audit/escalar_con_ltv_mal_calculado

- model_id: `sakana/fugu-max`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 30.201s | tokens_per_second: 56.9
- input_tokens: 259 | output_tokens: 1719

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

**No escalaría fuerte todavía.** Hay dos errores importantes:

### 1. El churn implica una vida media de 12,5 meses, no 24

Con churn mensual constante del 8%:

\[
\text{vida esperada} = \frac{1}{0{,}08}=12{,}5\text{ meses}
\]

La retención después de 24 meses sería:

\[
0{,}92^{24}\approx 13{,}6\%
\]

Por tanto, usando tus datos:

- **LTV de ingresos:**  
  \[
  \$35 \times 12{,}5 = \$437{,}50
  \]

- **LTV de margen bruto:**  
  \[
  \$35 \times 70\% \times 12{,}5 = \$306{,}25
  \]

El LTV relevante para comparar contra CAC es el de margen bruto, no el de ingresos.

### 2. Tu LTV/CAC real es aproximadamente 1,06

\[
\frac{\$306{,}25}{\$290}=1{,}06
\]

Y el período de recuperación del CAC es:

\[
\frac{\$290}{\$35 \times 70\%}
=
\frac{\$290}{\$24{,}50}
\approx 11{,}8\text{ meses}
\]

Eso deja muy poco margen para errores de atribución, costes de soporte, descuentos, churn superior al estimado o variación del CAC.

### ¿Qué pasaría con $10.000?

A un CAC de $290 adquirirías aproximadamente:

\[
\$10.000/\$290 \approx 34{,}5\text{ clientes}
\]

Su margen bruto esperado total sería:

\[
34{,}5 \times \$306{,}25 \approx \$10.560
\]

Después de publicidad quedarían solo unos **$560**, antes de otros costes, y además ese margen se cobra durante aproximadamente un año, no inmediatamente. Si tu CAC de $290 solo incluye publicidad y no creatividades, herramientas, personal u onboarding, el resultado sería peor.

### Qué tendría que cambiar

Para lograr un LTV/CAC de 3 con estos precios y churn:

- **CAC máximo:** aproximadamente **$102**
- O, manteniendo CAC de $290, churn mensual cercano o inferior a **2,8%**
- O, manteniendo churn y CAC, precio aproximado de **$99/mes** antes de considerar otros costes

### Recomendación

No aprobaría los $10.000 como una apuesta de escalamiento. Haría primero un test controlado, por ejemplo **$1.000–$2.000**, con cohortes y límites claros, verificando:

- CAC incremental real, no solo atribuido.
- Retención de los clientes adquiridos por publicidad.
- Payback por cohorte.
- Margen de contribución después de todos los costes variables.
- Si el 8% de churn es realmente estable o empeora en clientes de pago.

Con los números actuales, **eres rentable a nivel de negocio, pero la adquisición pagada no parece suficientemente rentable para escalar fuerte**.