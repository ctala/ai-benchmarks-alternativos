# Qwen 3.6 27B base (OpenRouter FP8) — business_audit/retention_sobre_100_interpretacion

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 7.16 | quality: 8.0
- latency_total: 43.059s | tokens_per_second: 58.7
- input_tokens: 143 | output_tokens: 2529

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Tu interpretación es intuitiva, pero técnicamente incorrecta y estratégicamente peligrosa.

Lo que ves es **Net Revenue Retention (NRR) o Retención Neta de Ingresos**, no retención de clientes. El NRR mide el comportamiento financiero de tu cohorte inicial, **independientemente de cuántos contratos se pierdan**. El 114% significa que, entre los pagos recurrentes de quienes se quedaron y las expansiones (upsells/cross-sells), el MRR de esa base no solo se mantuvo, sino que creció un 14%.

Sin embargo, tu contexto revela lo que el NRR oculta por diseño: perdiste 4 de 40 clientes. Eso es un **churn de clientes del 10% mensual**. Si se mantiene constante, al año te quedarías con ~28% de tu base actual (`0.9^12 ≈ 0.28`). No es “prácticamente no se me va nadie”; es una fuga estructural que solo se disfraza con expansiones.

### Por qué no puedes dejar de preocuparte por el churn:
1. **El NRR >100% es dependiente de expansión continua.** Si tu equipo se volca 100% a adquisición y el ritmo de upsells se frena, el NRR caerá rápidamente y el churn se manifestará como caída neta de ingresos.
2. **Churn compuesto es implacable.** Un 10% mensual de clientes equivale a ~72% de erosión anual. Para mantener la base estable, necesitarías captar ~100% de clientes nuevos al año solo para reemplazar los que se van, lo que dispara el CAC y destruye la eficiencia del LTV/CAC.
3. **Señal temprana de fricción.** Perder 1 de cada 10 clientes sugiere problemas de onboarding, ajuste precio/valor, competencia o product-market fit en un segmento específico. Ignorarlo ahora, cuando la base es pequeña, multiplicará el costo operativo cuando escalés.

### Qué debes hacer con estos datos:
- **Calcula el Gross Revenue Retention (GRR).** Es el NRR sin contar expansiones. Si el GRR está por debajo del 90%, tu crecimiento depende exclusivamente de vender más a los que ya están, no de retenerlos.
- **Segmenta el churn.** ¿Los 4 que se fueron estaban en el mismo plan? ¿Se fueron en los primeros 30, 60 o 90 días? ¿Por precio, funcionalidad o falta de uso? El churn no es un número, es un diagnóstico.
- **Equilibra la asignación de recursos.** Hasta que el churn de clientes baje del 5% mensual y el GRR supere el 92%, dedicar el 100% del esfuerzo a adquisición es financiar una fuga. Un split 70% retención/éxito del cliente y 30% adquisición suele ser más sostenible en fase temprana.

El NRR del 114% es una señal positiva de que tu producto genera valor adicional y hay espacio de expansión. Pero en SaaS, **el churn de clientes es la gravedad; el NRR es el cohete**. Sin contrarrestar la gravedad, el cohete se agota y la caída es más rápida de lo que parece.

¿Quieres que te ayude a estructurar el cálculo del GRR o a diseñar un marco de análisis del churn por cohorte?