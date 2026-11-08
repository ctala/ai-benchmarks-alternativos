# GPT-5.6 Sol — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 23.526s | tokens_per_second: 88.2
- input_tokens: 186 | output_tokens: 2076

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

No. Con esos números, la publicidad está prácticamente en punto de equilibrio, no lista para escalar.

### Recálculo

Con churn mensual de 8%, la vida media esperada es:

\[
1 / 0,08 = 12,5 \text{ meses}
\]

No 24 meses. Además, el LTV debe calcularse sobre margen bruto:

\[
LTV = 35 \times 70\% \div 8\% = \$306,25
\]

Por tanto:

\[
LTV/CAC = 306,25 / 290 = 1,06
\]

| Métrica | Resultado |
|---|---:|
| LTV de ingresos | $437,50 |
| LTV de margen bruto | $306,25 |
| CAC | $290 |
| LTV/CAC correcto | **1,06×** |
| Beneficio bruto esperado tras CAC | **$16,25 por cliente** |

Esto es antes de salarios, soporte, marketing interno, gastos generales, impuestos y coste del capital.

Incluso si realmente duraran 24 meses, el LTV correcto sería:

\[
35 \times 24 \times 70\% = \$588
\]

Eso daría solo **2,03×**, no 2,9×.

### Qué ocurriría con $10.000

A CAC constante adquirirías aproximadamente:

\[
10.000 / 290 = 34,5 \text{ clientes}
\]

Su margen bruto de vida esperado sería unos **$10.560**, dejando apenas **$560** después de publicidad y antes del resto de gastos. Además, el CAC suele empeorar al aumentar el presupuesto.

Con churn, la cohorte tardaría aproximadamente **36 meses** en recuperar colectivamente el CAC; solo alrededor del 5% seguiría activa entonces.

### Umbrales útiles

Para llegar a **3× LTV/CAC** manteniendo los demás números:

- El CAC debería bajar a aproximadamente **$102**, o
- El churn mensual debería bajar de 8% a aproximadamente **2,8%**.

**Veredicto:** no metería $10.000 como apuesta de escalado. Como máximo, lo usaría como experimento controlado y por fases, midiendo CAC incremental y retención específica de los clientes pagados. Primero necesitas reducir drásticamente CAC o churn. Tu rentabilidad actual puede venir de clientes orgánicos; eso no demuestra que el canal pagado sea rentable.