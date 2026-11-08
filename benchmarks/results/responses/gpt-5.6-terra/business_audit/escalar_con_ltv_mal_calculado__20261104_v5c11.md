# GPT-5.6 Terra — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 22.406s | tokens_per_second: 85.9
- input_tokens: 186 | output_tokens: 1925

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

**No le daría a escala con esos números.** Hay dos errores en el cálculo:

1. Estás usando un LTV de ingresos, no de margen bruto.
2. Un churn mensual de 8% no implica una vida media de 24 meses.

### Recalculo

Con churn mensual de 8%, la vida esperada de un cliente es aproximadamente:

\[
\text{Vida media} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

Tu margen bruto mensual por cliente es:

\[
35 \times 70\% = \$24.50
\]

Por tanto, el LTV basado en margen bruto es:

\[
\text{LTV} = \frac{24.50}{0.08} = \$306.25
\]

Frente a un CAC de $290:

\[
\text{LTV/CAC} = \frac{306.25}{290} = 1.06x
\]

### Qué significa

Por cada cliente adquirido:

| Concepto | Valor |
|---|---:|
| CAC | $290 |
| Ingreso esperado de vida | $437.50 |
| Margen bruto esperado de vida | $306.25 |
| Margen bruto tras recuperar CAC | **$16.25** |
| LTV/CAC real | **1.06x** |

Eso es antes de salarios, herramientas, soporte, ventas, impuestos, devoluciones, descuentos y coste financiero del dinero. En términos reales, es muy probable que esos clientes de pago sean **no rentables**.

Además, recuperarías el CAC muy lentamente. Con $24.50 de margen bruto mensual, el payback “sin churn” parecería de:

\[
290 / 24.5 = 11.8 \text{ meses}
\]

Pero hay churn: al mes 12 solo seguiría activo aproximadamente:

\[
0.92^{12} = 36.8\%
\]

de esa cohorte. En valor esperado, tardarías alrededor de **35 meses** en recuperar los $290 de CAC… y el máximo margen bruto que esa cohorte puede generar en toda su vida es solo ~$306. Es un negocio de adquisición con prácticamente cero colchón.

### Tu supuesto de “2 años” tampoco cuadra con 8% de churn

Con 8% de churn mensual, solo cerca de:

\[
0.92^{24} = 13.5\%
\]

de los clientes siguen activos tras 24 meses. Algunos pueden durar dos años, pero el promedio no.

E incluso si realmente tuvieras una vida media de 24 meses, deberías aplicar margen bruto:

\[
35 \times 24 \times 70\% = \$588
\]

\[
588 / 290 = 2.03x
\]

Eso tampoco llega a 3x.

### Qué tendría que cambiar para justificar CAC de $290

Para alcanzar un LTV/CAC de 3x con tu precio y margen actuales:

\[
\text{CAC máximo} = 306.25 / 3 = \$102
\]

Alternativamente, para sostener un CAC de $290 y lograr 3x, necesitarías un churn mensual cercano a:

\[
\frac{24.5}{290 \times 3} \approx 2.8\%
\]

Es decir: bajar churn de **8% a alrededor de 2.8% mensual**, o elevar significativamente el margen/precio.

### Sobre los $10.000

A $290 de CAC, comprarías aproximadamente:

\[
10,000 / 290 = 34.5 \text{ clientes}
\]

Esos clientes generarían, en expectativa y durante toda su vida:

- ~$15.1k de ingresos;
- ~$10.6k de margen bruto;
- apenas **~$560 de margen bruto después de los $10k de publicidad**.

Y eso asume que el CAC no empeora al escalar, algo que frecuentemente ocurre.

**Conclusión:** no aprobaría una escalada fuerte con este CAC y churn. Haría pruebas pequeñas y controladas, pero el objetivo antes de meter $10k debería ser: CAC cercano o inferior a $100, churn materialmente menor, mayor precio/margen, o una combinación de los tres.