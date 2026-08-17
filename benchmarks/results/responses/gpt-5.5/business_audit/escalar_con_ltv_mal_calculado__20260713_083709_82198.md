# GPT-5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `gpt-5.5`
- success: True  | final: 6.77 | quality: 8.14
- latency_total: 35.197s | tokens_per_second: 55.9
- input_tokens: 186 | output_tokens: 1967

## Respuesta completa

No le daría “fuerte” todavía. Tus unit economics están casi en break-even, no en zona segura para escalar.

### 1) Tu LTV está sobreestimado

Con churn mensual de 8%, la vida media esperada no es 24 meses.

La aproximación estándar es:

\[
\text{Vida media} = \frac{1}{churn} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

Además, el LTV no debería calcularse sobre ingresos brutos, sino sobre margen bruto:

\[
\text{LTV} = \frac{ARPU \times Margen\ bruto}{Churn}
\]

\[
\text{LTV} = \frac{35 \times 0.70}{0.08} = \frac{24.5}{0.08} = 306.25
\]

Tu LTV real aproximado es **$306**, no $840.

---

### 2) Tu LTV/CAC real

\[
\text{LTV/CAC} = \frac{306.25}{290} = 1.06
\]

Eso significa que por cada cliente adquirido con ads estás generando apenas:

\[
306.25 - 290 = 16.25
\]

de contribución bruta esperada durante toda su vida.

Eso es muy poco margen de seguridad.

---

### 3) Si metes $10.000 en ads

Con CAC de $290:

\[
10,000 / 290 = 34.5 \text{ clientes}
\]

Esos clientes generarían LTV bruto total esperado de:

\[
34.5 \times 306.25 = 10,566
\]

Después de CAC:

\[
10,566 - 10,000 = 566
\]

O sea: arriesgas **$10.000** para ganar, en expectativa, unos **$566 de contribución bruta futura**, antes de costes fijos, soporte adicional, descuentos, deuda técnica, impuestos, errores de atribución, etc.

Eso no es una máquina de crecimiento. Es una apuesta muy frágil.

---

### 4) Tu payback también es más largo de lo que parece

Margen bruto mensual por cliente:

\[
35 \times 0.70 = 24.50
\]

Si ignoraras churn, el payback sería:

\[
290 / 24.5 = 11.8 \text{ meses}
\]

Pero con churn, no todos los clientes sobreviven hasta el mes 12. Considerando churn del 8%, el payback real esperado ocurre alrededor de **35 meses**. Y el LTV máximo esperado por cliente es solo $306, así que apenas recuperas el CAC con un pequeño excedente.

---

### 5) Para que escalar con ads tenga sentido

Si quieres un LTV/CAC de 3, tu CAC máximo debería ser:

\[
306.25 / 3 = 102
\]

Con tus números actuales, deberías estar pagando cerca de **$100 por cliente**, no $290.

O alternativamente necesitas mejorar bastante alguno de estos drivers:

- Bajar churn de 8% a aproximadamente **2.8% mensual** para soportar CAC de $290 con LTV/CAC 3.
- Subir precio de $35 a cerca de **$100/mes**, manteniendo margen y churn.
- Mejorar margen bruto.
- Reducir CAC.
- Mejorar onboarding/activación para que el churn de clientes pagados sea mucho menor.

---

### Veredicto

No escalaría fuerte todavía.

Con estos números, **no tienes LTV/CAC de 2.9; tienes aproximadamente 1.06**. Estás casi comprando clientes al precio de todo su valor económico futuro.

Si quieres invertir los $10.000, lo haría como experimento controlado, no como escalamiento agresivo. Por ejemplo:

- Gasta $1.000–$2.000 primero.
- Mide CAC real por canal.
- Separa clientes orgánicos vs pagados.
- Mide churn específico de clientes adquiridos por ads.
- Calcula LTV por cohorte, no con promedio general.
- No escales hasta ver CAC mucho más bajo o churn claramente menor.

Ahora mismo, con CAC de $290 y churn mensual del 8%, yo no aprobaría el plan de crecimiento.