# Claude Haiku 4.5 (suscripción) — business_audit/retention_sobre_100_interpretacion

- model_id: `claude-haiku-4-5`
- success: True  | final: 4.68 | quality: 4.8
- latency_total: 34.567s | tokens_per_second: 45.8
- input_tokens: 10 | output_tokens: 1582

## Respuesta completa

No. **Esa es la lectura intuitiva, no la correcta.**

Desglosemos:

## Qué dice cada número

| Métrica | Tu dato | Qué significa |
|---|---|---|
| **Customer churn** | 40 → 36 = 10% mensual | Perdiste 1 de cada 10 clientes |
| **Revenue retention** | 114% | El ingreso que retuviste + expansión suma 114% del MRR anterior |

Son dos cosas distintas. La retención de ingresos está en 114% **porque los clientes que se quedaron subieron de plan lo suficiente** como para cubrir los que se fueron. Eso es un patrón real, pero **frágil**.

## Por qué sí deberías preocuparte

**Churn del 10% mensual = 71% anual** (compuesto). A ese ritmo, en un año pierdes 7 de cada 10 clientes que tuviste hoy.

La expansión que ves ahora es un colchón temporal. Si:
- Se agota (clientes ya upgradear al tope), o
- El churn acelera (porque los clientes insatisfechos son precisamente los que se van),

tu métrica pasa de 114% a <100% muy rápido.

## Orden correcto de prioridades

1. **Root cause del churn**: ¿por qué se fueron esos 4? Producto, precio, soporte, competencia?
2. **Mantén la expansión activa**: entendé qué hizo que otros subieran (fue intencional o casualidad).
3. **Luego sí escala captación**: recién cuando el churn esté <5% mensual.

Si metes todo a captación hoy, estás clavando un acelerador a un auto que pierde gasolina por una fuga. Ves movimiento, pero el tanque se vacía igual.

**La pregunta que falta**: ¿quién se fue? ¿Los clientes de plan bajo que nunca usaban, o clientes que perdiste por un problema real?