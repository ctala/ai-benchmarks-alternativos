# GPT-5.6 Luna Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 20.068s | tokens_per_second: 195.7
- input_tokens: 5610 | output_tokens: 3927

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

No escalaría fuerte todavía. El error está en estimar la vida media del cliente y en usar ingresos en vez de margen bruto.

### Recalculo

Con churn mensual del 8%:

\[
\text{Vida media} \approx \frac{1}{0.08}=12.5\text{ meses}
\]

Ingresos esperados por cliente:

\[
35 \times 12.5 = \$437.50
\]

LTV basado en margen bruto:

\[
\$437.50 \times 70\% = \$306.25
\]

Por tanto:

\[
\text{LTV/CAC}=\frac{306.25}{290}=1.06
\]

No es 2,9. Es aproximadamente **1,06 usando margen bruto**, lo que deja muy poco margen para costes fijos, soporte, ventas, impagos, descuentos o errores de atribución.

### Qué implica gastar $10.000

A un CAC de $290, adquirirías aproximadamente:

\[
\frac{10,000}{290}=34.5\text{ clientes}
\]

Margen bruto esperado de esos clientes:

\[
34.5 \times 306.25 \approx \$10,560
\]

Después de los $10.000 de publicidad, la contribución esperada sería solo de unos **$560**, antes de costes fijos y otros gastos. Además, ese retorno se genera durante unos 12,5 meses, no inmediatamente.

El periodo de recuperación del CAC sería:

\[
\frac{290}{35 \times 70\%}
=\frac{290}{24.50}
\approx 11.8\text{ meses}
\]

Eso es demasiado ajustado para escalar agresivamente, especialmente si el churn de los clientes adquiridos por publicidad es peor que el promedio.

### Umbrales útiles

Para conseguir un LTV/CAC de 3 con estos datos, el CAC máximo sería:

\[
\frac{306.25}{3} \approx \$102
\]

O, manteniendo CAC de $290 y margen del 70%, necesitarías aproximadamente:

- Precio mensual de unos **$99,40**, o
- Churn mensual cercano al **2,8%**.

### Recomendación

No aprobaría aún los $10.000 como “escala fuerte”. Haría una prueba controlada, quizá con una fracción del presupuesto, y exigiría:

1. Cohortes separadas de clientes pagados frente a orgánicos.
2. CAC totalmente cargado, incluyendo creatividades, agencias y descuentos.
3. Retención real de esas cohortes.
4. Payback máximo definido, por ejemplo 6–9 meses.
5. Escalar solo si el CAC baja sustancialmente o el churn de los clientes adquiridos es mucho menor.

Con la aritmética actual, estás comprando crecimiento casi a punto de equilibrio, no crecimiento rentable.