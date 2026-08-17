# Claude Fable 5 (suscripción) — business_audit/retention_sobre_100_interpretacion

- model_id: `claude-fable-5`
- success: True  | final: 5.03 | quality: 6.0
- latency_total: 44.828s | tokens_per_second: 43.3
- input_tokens: 2 | output_tokens: 1939

## Respuesta completa

No es correcto, y la conclusión que estás sacando es justo la trampa de esta métrica.

## Qué mide realmente ese 114%

Retención de ingresos: 114% es **Net Revenue Retention (NRR)**: cuánto ingreso recurrente generan hoy los clientes que ya tenías, incluyendo upgrades y descontando bajas.

**La retención de clientes (logo retention) nunca puede superar el 100%.** Un cliente no puede quedarse "más que quedarse". Lo que supera el 100% es el ingreso, porque la expansión (upgrades) tapó el hueco que dejaron los que se fueron.

## Tus números reales

- Logo retention: en el mejor caso, 36/40 = **90% mensual** → **10% de churn de clientes al mes**.
- Anualizado: 0.90^12 ≈ 28% de tus clientes seguirían en 12 meses. Es decir, **~72% de churn anual**. Eso no es "no se me va nadie", es un balde con un agujero grande.
- Y ojo: si dentro de esos 36 hay clientes *nuevos* del mes, tu churn real es peor que 10%.

Ejemplo con cifras redondas: si partías con $4,000 MRR y perdiste 4 clientes de ~$100 ($400 que se fueron), para llegar a 114% los upgrades tuvieron que aportar ~$960. Tu **Gross Revenue Retention** (retención sin contar expansión) sería ~90%. Ese es el número que te dice cuánto se te escapa; el 114% te dice cuánto lo disimulas.

## Por qué no puedes ignorar el churn

1. **La expansión tiene techo, el churn no.** Un cliente sube de plan una o dos veces y se acaba. El churn compone mes a mes para siempre. Este mes la expansión ganó la carrera; matemáticamente no puede ganarla 12 meses seguidos con 10% de churn.
2. **Riesgo de concentración.** Tu MRR depende cada vez de menos cuentas más grandes. Perder una sola de las que subieron de plan te duele el doble que antes.
3. **Captar sobre un balde roto sale caro.** Con 10% de churn mensual, cada cliente nuevo dura en promedio ~10 meses. Tu CAC efectivo se dispara y el crecimiento nuevo solo reemplaza lo que pierdes.

## Qué haría con esto

- Trackea **tres métricas separadas**: NRR (114%), GRR (~90%) y logo retention (90%). Nunca una sola.
- **Habla con los 4 que se fueron esta semana.** Con una base de 40, cuatro bajas es una señal, no ruido estadístico. Si se van por el mismo motivo, tienes un problema de producto o de segmento, no de suerte.
- Análisis de cohortes: ¿los que se van son recién llegados (problema de onboarding/expectativas) o antiguos (problema de valor sostenido)?

El 114% es una buena noticia real —tu producto tiene poder de expansión—, pero convive con un churn de clientes que, a este ritmo, te vacía la base en un año. No dejes de captar, pero el churn es hoy tu problema más urgente, no el que puedes archivar.