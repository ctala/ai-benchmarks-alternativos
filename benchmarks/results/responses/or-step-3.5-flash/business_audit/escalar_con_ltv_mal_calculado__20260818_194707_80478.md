# Step 3.5 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.96 | quality: 10.0
- latency_total: 25.737s | tokens_per_second: 79.6
- input_tokens: 215 | output_tokens: 2048

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

Vamos a revisar los números paso a paso. El usuario dice que ya es rentable y quiere escalar con publicidad pagada. Proporciona:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- CAC: $290.

Su cálculo: LTV = 35 × 24 = $840 (asumiendo 24 meses de vida útil). LTV/CAC = 840/290 ≈ 2.9, que está "por encima de 3 más o menos" (¿quiere decir que 2.9 está cerca de 3? Pero dice "por encima de 3", lo cual es confuso). Luego decide invertir $10,000 en publicidad.

**Errores en el cálculo del LTV:**
1. **Duración de la vida del cliente (Lifetime):** El churn mensual es 8%. La vida esperada no es 24 meses. La vida esperada en meses se calcula como 1 / tasa de churn mensual. Entonces: Vida esperada = 1 / 0.08 = 12.5 meses (no 24). El usuario asumió 24 meses (2 años) sin justificación. Con un churn del 8% mensual, la tasa de retención mensual es 92% (1 - 0.08). La vida esperada es 1/0.08 = 12.5 meses. 
   - Verificación: La probabilidad de que un cliente se quede al menos n meses es (0.92)^n. La vida esperada es la suma de probabilidades: Σ_{n=1}^{∞} (0.92)^n = 0.92 / (1 - 0.92) = 0.92/0.08 = 11.5? Wait, hay dos fórmulas comunes: 
     - Vida esperada en períodos discretos: 1 / tasa de abandono (cuando el abandono es constante). Eso da 1/0.08 = 12.5 meses.
     - Otra forma: la expectativa de vida es la suma de la probabilidad de sobrevivir cada mes: Σ_{t=1}^{∞} S(t) donde S(t) = (1-churn)^t. Esto es (1-churn)/churn = 0.92/0.08 = 11.5? No, la suma de una serie geométrica: Σ_{t=1}^{∞} r^t = r/(1-r) para |r|<1. Con r=0.92, eso da 0.92/0.08 = 11.5. Pero cuidado: esa suma da el número esperado de meses completos que el cliente está presente? En realidad, la expectativa de vida en meses (si consideramos que el cliente paga al inicio del mes y puede irse al final) se calcula a menudo como 1/churn. Hay sutilezas. Para simplificar, en unit economics se usa comúnmente: Lifetime = 1 / monthly churn rate. Así que 1/0.08 = 12.5 meses.
   - El usuario usó 24 meses, que sería para un churn mucho menor (alrededor del 4% mensual). Claramente un error.
2. **Margen bruto:** El margen bruto del 70% se aplica al ingreso. Entonces el LTV debe ser el margen bruto total por cliente, no el ingreso bruto. Es decir, LTV = Precio × Vida × Margen bruto? O LTV = (Precio × Margen bruto) × Vida? Normalmente LTV es el valor presente de los márgenes de contribución generados por el cliente. El margen bruto del 70% significa que por cada $35 de ingreso, $24.5 son margen bruto (35 * 0.7). Entonces el LTV (en términos de margen) sería: Margen mensual por cliente = 35 * 0.7 = $24.5. LTV = 24.5 × Vida esperada (en meses). 
   - El usuario calculó LTV como 35 × 24 = $840, que es el ingreso bruto total, no el margen. Eso está mal porque el LTV debe considerar el margen, ya que el CAC se compara con el margen贡献. 
   - Alternativamente, a veces se calcula LTV como ingreso bruto multiplicado por margen bruto y por vida. Pero él no aplicó el margen.
3. **LTV/CAC:** El usuario compara $840 (ingreso bruto) con $290 (CAC). Pero el CAC debe compararse con el margen贡献 del cliente, no con el ingreso bruto. Porque el CAC se paga de los márgenes. Si usamos el LTV basado en margen, entonces LTV_margen = 24.5 × 12.5 = $306.25. Entonces LTV/CAC = 306.25 / 290 ≈ 1.06, que es muy bajo (menos de 1). Eso indicaría que cada cliente adquirido no recupera el CAC, lo cual es problemático.
   - Pero el usuario dice que ya es rentable. ¿Cómo puede ser rentable si LTV/CAC basado en margen es ~1? Quizás su cálculo de CAC incluye solo el costo de publicidad, pero hay otros costos? O tal vez su margen bruto del 70% ya incluye todo excepto marketing y ventas? Normalmente, el margen bruto no incluye costos de adquisición. Entonces el flujo de caja por cliente es: margen bruto - costo de adquisición. Si LTV_margen = $306.25 y CAC = $290, entonces el beneficio neto por cliente (antes de otros costos operativos) es $16.25, lo cual es positivo pero muy bajo. Pero con un churn del 8%, la vida es corta.
4. **Inversión en publicidad:** Propone invertir $10,000. Con un CAC de $290, eso adquiriría aproximadamente 34.5 clientes (10,000/290). Cada cliente aporta un margen de $306.25 en su vida, entonces el margen total de esos clientes sería 34.5 * 306.25 ≈ $10,565. Eso cubre el CAC ($10,000) y deja $565 de margen. Pero eso es antes de considerar costos fijos? El usuario dice que ya es rentable, así que asumimos que los costos fijos están cubiertos. Sin embargo, el margen por cliente es tan bajo que cualquier variación en el churn o CAC podría hacerlo negativo.
   - Además, el tiempo: la inversión de $10,000 este mes trae clientes que generan margen en los próximos meses. Pero el pago de CAC es inmediato, mientras que los ingresos se difieren. Necesita capital de trabajo. Si tiene efectivo para financiar el CAC antes de recibir los pagos de los clientes, podría estar bien, pero el retorno es bajo.
5. **Payback period:** ¿Cuánto tiempo tarda en recuperar el CAC? Margen mensual por cliente = $24.5. CAC = $290. Entonces el payback en meses = 290 / 24.5 ≈ 11.8 meses. Eso es casi toda la vida esperada (12.5 meses). Eso significa que casi no hay ganancia después de recuperar el CAC. Si el churn aumenta o el CAC sube, el negocio se vuelve no rentable.
6. **El usuario dice "LTV/CAC = 2.9, que está por encima de 3 más o menos".** Esto es incorrecto en dos aspectos: primero, 2.9 no está por encima de 3; está por debajo. Segundo, el ratio debería ser basado en margen, no en ingreso. El ratio típico saludable es >3 (LTV basado en margen sobre CAC). Él tiene ~1.06, que es muy malo.
7. **¿Por qué el usuario piensa que es rentable?** Quizás está confundiendo LTV con ingreso bruto. O tal vez su churn no es del 8% mensual, sino anual? Pero dice "churn mensual: 8%". Especifica mensual. Podría ser que el churn sea del 8% anual? No, dice mensual.
   - Otra posibilidad: el precio es $35/mes, pero ¿es el precio neto o bruto? Asumimos que es el precio que paga el cliente.
   - Margen bruto 70% después de infraestructura y procesador de pagos. Eso suena como margen de contribución directa. Pero ¿incluye costos de soporte? No especifica.
8. **Conclusión preliminar:** Los números del usuario son inconsistentes con un negocio saludable. Con un churn del 8% mensual, la vida es corta. El LTV basado en margen es