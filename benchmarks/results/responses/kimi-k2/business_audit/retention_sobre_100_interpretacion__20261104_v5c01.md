# Kimi K2 — business_audit/retention_sobre_100_interpretacion

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 14.687s | tokens_per_second: 36.4
- input_tokens: 162 | output_tokens: 535

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No. Tu lectura es incorrecta y la estrategia que propones sería dañina.**

---

## Qué dice realmente tu 114%

| Métrica | Valor real |
|--------|-----------|
| **Retención de ingresos** | 114% ✓ |
| **Retención de clientes** | **90%** (36/40) |
| **Churn de clientes** | **10%** |

La retención de ingresos supera el 100% porque los upgrades de los que se quedaron compensaron (y superaron) la pérdida de los 4 que se fueron. **Pero perdiste 4 clientes.** Eso es churn significativo.

---

## El riesgo de tu interpretación

Si "dejas de preocuparte por churn" y enfocas todo en adquisición:

- **Efecto compuesto negativo:** 10% mensual de churn de clientes = ~70% anual. Necesitarías crecer solo para quedarte igual.
- **Cohorte deteriorada:** Los que se van pueden ser los más antiguos o de mayor valor (no lo sabemos).
- **Dependencia de upgrades:** Tu "superávit" de ingresos viene de expansión, que es volátil. Si los upgrades se estabilizan, el 114% colapsa rápidamente.

---

## Lo que necesitas investigar *ahora*

1. **¿Quiénes son los 4 que se fueron?** (tamaño, antigüedad, razón)
2. **¿Los upgrades son sostenibles o puntuales?** (¿contratos anuales? ¿features nuevas?)
3. **¿Hay correlación entre los que se van y los que suben de plan?** (¿cannibalización? ¿cambio de segmento?)

---

## Veredicto

El 114% de retención de ingresos **oculta** un problema de retención de clientes que requiere atención. No es una señal de salud para dejar de lado, es una señal de alerta disfrazada.

¿Tienes datos sobre *quiénes* se fueron y *por qué*? Eso determinará si el 10% de churn es ruido o patrón.