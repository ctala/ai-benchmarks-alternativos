# GPT-6 Luna Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 25.283s | tokens_per_second: 121.9
- input_tokens: 4705 | output_tokens: 3082

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

**No aprobaría los $10.000 basándome en este cálculo.** El problema es que el plazo de 24 meses no concuerda con un churn mensual del 8%.

Suponiendo churn constante y sin expansión de ingresos:

- **Vida media esperada:** \(1 / 0,08 = 12,5\) meses, no 24.
- **LTV de ingresos:** \(35 / 0,08 = \$437,50\).
- **LTV de margen bruto:** \(\$437,50 \times 70\% = \$306,25\).
- **LTV/CAC:** \(\$306,25 / \$290 = 1,06\), no 2,9.
- **Recuperación del CAC:** \(\$290 / (\$35 \times 70\%) \approx 11,8\) meses.

Así, cada cliente deja unos **$16,25 de margen bruto esperado después del CAC**, antes de gastos fijos, costo del capital y cualquier desviación en churn o CAC. Es muy poco margen de seguridad; además, escalar puede encarecer la adquisición.

Si buscas una relación de **3:1** como referencia, con estos datos el CAC tendría que ser de unos **$102 o menos**. O, manteniendo el CAC en $290, tendrías que mejorar sustancialmente la retención o el margen.

Primero validaría el churn con cohortes y comprobaría que los $290 representan el **CAC marginal** del canal, no solo un promedio histórico. Si pruebas publicidad, lo haría por etapas y con límites de gasto y criterios de parada; no pondría los $10.000 de una vez.