# Claude Fable 5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.52 | quality: 8.0
- latency_total: 23.85s | tokens_per_second: 48.7
- input_tokens: 216 | output_tokens: 1162
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una interpretación completa y consejos prácticos para un emprendedor.

## Respuesta completa

No, no es correcto, y me alegra que preguntes antes de tomar decisiones con ese dato.

## Qué mide realmente ese 114%

Ese número es **retención neta de ingresos (NRR)**, no retención de clientes. Mide cuántos ingresos conservas de tu base existente, incluyendo *upgrades*. La fórmula mezcla dos fuerzas opuestas:

- **Expansión:** clientes que suben de plan (+)
- **Churn y downgrades:** clientes que se van o pagan menos (−)

Un 114% solo dice que la expansión superó al churn. **No dice que el churn sea bajo.**

## Tus números reales

- Clientes el mes pasado: 40
- Clientes este mes: 36
- **Churn de clientes (logo churn): 10% mensual**

Un 10% mensual es muy alto. Anualizado, si se mantuviera, retendrías apenas ~28% de tus clientes al cabo de un año (0,9¹² ≈ 0,28). Perderías casi tres de cada cuatro.

Lo que está pasando es que **unos pocos clientes que expanden están tapando la fuga**. El 114% neto probablemente esconde algo como: −15/20% de ingresos por churn, +30% por expansión.

## Por qué esto es frágil

1. **La expansión tiene techo.** Los clientes que suben de plan no lo harán todos los meses. El churn, en cambio, es recurrente.
2. **Riesgo de concentración.** Tu NRR depende cada vez más de menos cuentas. Si una de las que expandió se va, el número se desploma.
3. **Base pequeña.** Con 40 clientes, 4 bajas mueven mucho las métricas; un mes malo de expansión y tu NRR cae por debajo de 100% de golpe.
4. **Captar nuevos clientes con un cubo agujereado es caro.** Cada cliente nuevo que traigas te durará, en promedio, muy poco.

## Qué haría yo

- **Separa las métricas:** rastrea NRR, GRR (retención bruta, sin contar expansión) y logo retention por separado. Tu GRR es probablemente el dato más preocupante y el panel no te lo está enseñando.
- **Habla con los 4 que se fueron.** Con volúmenes así de pequeños, 4 entrevistas te dan más información que cualquier dashboard.
- **Prioriza churn sobre adquisición** hasta que el logo churn baje a niveles razonables (para SaaS SMB, <3% mensual; ideal <1-2%).

En resumen: el 114% es una buena noticia sobre tu capacidad de expansión, pero es una métrica neta que está enmascarando un problema de retención serio. No dejes de preocuparte por el churn; es justo ahora cuando más deberías hacerlo.