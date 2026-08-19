# Claude Opus 5 Fast — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 14.203s | tokens_per_second: 144.2
- input_tokens: 216 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## No, esas son dos métricas distintas

Tu panel mide **euros**, no **personas**. Y con tus propios números, la retención de clientes está por debajo del 100%:

- **Retención de logos:** 36 / 40 = **90%** → churn del **10% mensual**
- **Retención de ingresos (neta):** **114%**

Los ingresos crecen *a pesar* de que se te van clientes, porque las subidas de plan tapan el agujero.

## Un detalle de definición

Si el número supera el 100%, por fuerza es **NRR (net revenue retention)**: incluye expansión. La **GRR (gross revenue retention)**, que solo cuenta churn y bajadas de plan, matemáticamente **nunca puede pasar de 100%**. Tu GRR está claramente por debajo — y es la que mide fugas.

Además, la NRR se calcula sobre la cohorte que ya tenías al inicio del periodo: **los clientes nuevos no entran en ese 114%**. No es un indicador de crecimiento, es un indicador de la salud de tu base actual.

## Lo que pasa si proyectas ese 10% mensual

0,90¹² ≈ **0,28**. De cada 100 clientes de hoy, en un año te quedan ~28. Sobreviven 3 de cada 4... perdón, se van 3 de cada 4.

Para que la NRR siga en 114% el año que viene, la expansión tendría que compensar esa sangría cada mes, indefinidamente, sobre una base cada vez más pequeña.

## Lo que probablemente esconde tu 114%

Ejemplo ilustrativo (asumiendo tickets parecidos, 100 €/mes):

| Concepto | MRR |
|---|---|
| Inicio (40 clientes) | 4.000 € |
| Churn (−4 clientes) | −400 € → GRR 90% |
| Expansión necesaria | **+960 €** |
| Final | 4.560 € → NRR 114% |

Eso son **+24% de expansión bruta** en un mes. Si vino de 4-5 cuentas, esas cuentas casi duplicaron su gasto. Traducción: **tu MRR se está concentrando**. La misma métrica que parece una buena noticia te está avisando de un riesgo — si una de esas cuentas grandes se va o revierte el upgrade, el 114% se convierte en 80% de golpe.

También ojo: con 40 clientes, **un cliente = 2,5 puntos de retención**. Un solo mes no es una tendencia.

## Antes de volcarte en captación

1. **Separa GRR de NRR** en el panel. La GRR es tu métrica de fugas; la NRR sin la GRR al lado es engañosa.
2. **Mira quién se fue.** ¿Los 4 eran del mismo segmento, plan o canal de adquisición? Si el churn está en un perfil concreto y sigues captando ese perfil, estás llenando un cubo agujereado y pagando por el privilegio.
3. **Mide la concentración.** ¿Qué % del MRR está en tus 3 cuentas mayores? Si supera el 30-40%, tu 114% depende de muy pocas decisiones ajenas.
4. **Comprueba si la expansión es estructural o reversible.** Los upgrades por asientos o por uso puntual bajan igual de rápido que suben.

**La respuesta corta:** no puedes dejar de preocuparte por el churn. Con un 10% mensual, cada cliente nuevo que captes entra en un sistema que pierde tres cuartas partes de su base al año. Arreglar la retención hace que la captación rinda