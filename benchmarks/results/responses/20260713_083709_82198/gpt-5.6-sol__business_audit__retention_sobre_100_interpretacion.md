# GPT-5.6 Sol — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 3.46 | quality: 3.34
- latency_total: 14.499s | tokens_per_second: 47.9
- input_tokens: 128 | output_tokens: 694

## Respuesta completa

No. Estás mezclando **retención de ingresos** con **retención de clientes**.

- **114% de retención neta de ingresos (NRR)** significa que los ingresos del grupo de clientes existente crecieron un 14% después de contar bajas, reducciones de plan y ampliaciones.
- No significa que casi nadie se haya ido. Las subidas de plan pueden estar compensando —e incluso ocultando— el churn.

Con tus cifras, **si los 36 clientes son supervivientes de los 40 y no incluyen altas nuevas**:

- Retención de clientes: \(36 / 40 = 90\%\)
- Churn de clientes mensual: \(4 / 40 = 10\%\)

Un 10% mensual es elevado: si se mantuviera, al cabo de 12 meses conservarías aproximadamente el **28%** de esa cohorte, aunque los ingresos podrían seguir creciendo temporalmente gracias a las expansiones.

Si los 36 incluyen clientes nuevos, la retención real de la cohorte es todavía menor. Por ejemplo, si hay 3 altas nuevas, solo permanecen 33 de los 40 anteriores: **82,5% de retención** y **17,5% de churn**.

Conviene revisar por separado:

1. **Retención de clientes o logos**: qué porcentaje de clientes permanece.
2. **GRR**: ingresos retenidos sin contar ampliaciones; muestra el daño de bajas y downgrades.
3. **NRR**: ingresos retenidos contando ampliaciones; ese 114% probablemente sea esta métrica.
4. **Churn por segmento, plan y antigüedad**, para saber si las mejoras de plan dependen de pocos clientes grandes.

Por tanto, **no deberías dejar de preocuparte por el churn**. Una NRR del 114% es una buena señal de expansión, pero perder 4 de 40 clientes en un mes es una señal de riesgo. Antes de volcar todo el esfuerzo en adquisición, confirma además que el panel calcula el 114% sobre la cohorte inicial y que no incluye ingresos de clientes nuevos.