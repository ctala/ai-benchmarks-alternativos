# DeepSeek V4 Pro (0813) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 54.951s | tokens_per_second: 64.6
- input_tokens: 281 | output_tokens: 3550

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

No le doy. Tu cálculo tiene un error clave y, al corregirlo, la unidad económica deja de ser atractiva para escalar.

## 1. El error: vida del cliente

Estás usando 24 meses porque “un cliente se queda unos 2 años”, pero con 8% de churn **mensual** la vida media no es 24 meses, sino:

\[
\text{Vida media} = \frac{1}{\text{churn mensual}} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

Además, 8% mensual implica que solo el 36.8% de los clientes sobrevive al año:

\[
0.92^{12} \approx 0.368
\]

Eso es una retención anual baja, no 2 años.

## 2. LTV real

- LTV bruto = $35 × 12.5 = **$437.50**
- LTV neto (margen bruto 70%) = $437.50 × 0.7 = **$306.25**

## 3. LTV / CAC real

\[
\frac{\text{LTV neto}}{\text{CAC}} = \frac{306.25}{290} = 1.06
\]

Esto significa que cada dólar invertido en adquirir un cliente genera solo $1.06 de contribución bruta. Está muy lejos del umbral sano de **3:1** para escalar agresivamente. Incluso usando LTV bruto ($437.50), la relación es 1.51, todavía insuficiente.

## 4. Payback period

\[
\text{Payback} = \frac{\text{CAC}}{\text{Contribución mensual por cliente}} = \frac{290}{35 \times 0.7} = \frac{290}{24.5} \approx 11.8 \text{ meses}
\]

Tardarías casi un año en recuperar solo el CAC por cliente, sin descontar costos fijos, salarios ni el valor del dinero en el tiempo.

## 5. Simulación rápida de los $10,000

Con CAC de $290, $10,000 compran ≈ 34.5 clientes.

- Ingreso mensual bruto incremental: 34.5 × $35 ≈ $1,207
- Margen bruto mensual incremental: $1,207 × 0.7 ≈ $845

Pero con 8% de churn mensual, ese margen se reduce cada mes. El valor total generado por esa cohorte en el tiempo (sin descontar) es:

\[
\frac{845}{0.08} \approx 10,565
\]

Es decir, apenas $565 por encima de los $10,000 invertidos. Y eso es **margen bruto**, sin cubrir overhead, impuestos ni otros gastos operativos. En la práctica estarías empatando o perdiendo dinero.

## 6. Qué necesitarías para escalar

Para tener un LTV/CAC ≥ 3 con tu margen y precio actuales, necesitarías cumplir alguna de estas condiciones:

- **Bajar el churn mensual a ≤ 2.8%** (vida media ≈ 35.7 meses)  
  \[
  \text{LTV neto} = 35 \times 35.7 \times 0.7 \approx 875
  \]
  \[
  875 / 290 \approx 3.0
  \]

- **Reducir el CAC a ≤ $102**  
  \[
  306.25 / 3 \approx 102
  \]

- **Aumentar el LTV neto** (subir precio, aumentar margen o vender más servicios) hasta ≥ $870.

## 7. Recomendación

Antes de meter $10,000 en publicidad pagada, trabaja en:

1. **Retención**: 8% de churn mensual es muy alto. Diagnostica por qué se van los clientes.
2. **CAC**: $290 es alto para un ticket de $35/mes. Optimiza creatividades, landing pages, conversión y segmentación.
3. **Piloto pequeño**: si decides probar, invierte una fracción (no $10,000) y mide el churn real de esa cohorte, el CAC real y el payback.

Con los números actuales, escalar con publicidad pagada no destruye valor por poco, pero no genera un retorno suficiente para justificar el riesgo y la presión de caja. No le doy.