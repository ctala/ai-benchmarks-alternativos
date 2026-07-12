# MiniMax M3 — business_audit/retention_sobre_100_interpretacion

- model_id: `minimax/minimax-m3`
- success: True  | final: 5.93 | quality: 6.0
- latency_total: 19.605s | tokens_per_second: 85.0
- input_tokens: 284 | output_tokens: 1667

## Respuesta completa

# No, esa lectura es incorrecta. Hay un error de métricas.

## Qué mide realmente la "Retención de ingresos" (NRR)

Esos 114% **no reflejan cuántos clientes conservas**, sino **cuánta facturación generates de los clientes que ya tenías**. La fórmula es aproximadamente:

$$\text{NRR} = \frac{\text{Arr del mes anterior} - \text{churn} - \text{downgrades} + \text{upgrades}}{\text{Arr del mes anterior}}$$

Un NRR > 100% significa que **la expansión (upgrades) supera al churn + contraction**. Punto. Nada más.

## Tu situación real, descifrada

| Métrica | Valor | Qué te dice |
|---|---|---|
| Clientes inicio de mes | 40 | — |
| Clientes fin de mes | 36 | — |
| **Logo churn mensual** | **10%** | 4 clientes se fueron |
| **Logo retention mensual** | **90%** | Conservas 9 de cada 10 |
| NRR | 114% | Los 36 que quedan pagan más que los 40 de antes |

Son dos métricas que responden a preguntas distintas:
- **NRR**: *¿los clientes que me quedan gastan más o menos que antes?*
- **Logo retention**: *¿se me van clientes o no?*

## Por qué ambas cifras pueden coexistir

Los clientes que subieron de plan pagaban, digamos, $50 y ahora pagan $90. Ese delta absorbe la pérdida de los 4 que se fueron. Pero esos 4 **se fueron**. No son ficción contable, sonlogos perdidos que no renovarán, no referirán, y probablemente reflejan un problema real (producto, soporte, encaje, pricing).

## Por qué NO debes ignorar el churn

Tasa de churn mensual del 10%, anualizada compuesta:

$$1 - (0{,}9)^{12} \approx 71\% \text{ de churn anual}$$

Eso es **catastrófico** en SaaS. Un benchmark saludable para SMB/SMB+ suele estar en 3-5% mensual (o 35-50% anual). Estás casi duplicando el rango alto.

El NRR alto te está **tapando un problema grave**. Si la expansión se ralentiza (porque no siempre hay a quién upsell, o los clientes top ya están en el plan más alto), tu NRR colapsará y verás la cruda realidad.

## Lo que te recomiendo medir aparte

1. **Gross Revenue Retention (GRR)** — NRR **sin** contar upgrades. Si te da, por ejemplo, 88%, eso es lo que retienes "de forma inercial". Esa cifra sí te duele.
2. **Logo churn rate mensual** — separada de la métrica de revenue.
3. **Cohortes** — ¿los clientes del mes 1, mes 2, etc. se comportan diferente? Quizás estás adquiriendo mejor y el problema está en retención temprana.
4. **Razón de cancelación** — obligatoria si quieres reducir ese 10%.

## Conclusión

Tu intuición de "captar gente nueva" es lógica solo si el motor de retención funciona. Con un 10% mensual de churn, **estás construyendo sobre arena**: cada mes pierdes 4 clientes y dependes enteramente de que las expansiones sigan compensando. Eso no escala y tiene un techo natural.

El NRR del 114% es una **foto** del mes. El churn del 10% mensual es una **tendencia**. Las tendencias matan SaaS.