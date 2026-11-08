# Qwen 3.6 Plus — business_audit/retention_sobre_100_interpretacion

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 47.841s | tokens_per_second: 57.2
- input_tokens: 143 | output_tokens: 2738

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Esa lectura es incorrecta y, estratégicamente, peligrosa. Te explico por qué, separando lo que la métrica realmente dice de lo que tú estás interpretando.

### 🔍 1. Retención de ingresos ≠ Retención de clientes
El `114%` que ves es casi con seguridad **Net Revenue Retention (NRR)**. Esta métrica mide cuánto ingreso generas de tu base inicial después de sumar expansiones (subidas de plan, add-ons, uso adicional) y restar contracciones y churn. **Excluye por definición a los clientes nuevos.**

Que supere el 100% significa una sola cosa: *el ingreso extra que generaron los clientes que se quedaron compensó con creces el ingreso perdido por los que se fueron*. No mide cuántos clientes retienes.

### 📉 2. Tu retención de clientes (logo retention) es del 90%
Pasaste de 40 a 36 clientes. Si en ese periodo no incorporaste clientes nuevos, tu **retención de logos** es `36/40 = 90%`. Es decir, **perdiste el 10% de tu base**. Matemáticamente, la retención de clientes nunca puede superar el 100%: no puedes "retener" más clientes de los que tenías al inicio.

*(Nota: si ese periodo es mensual, un 10% de logo churn equivale a ~70% anualizado, lo cual es insostenible para la mayoría de modelos SaaS. Si es anual, sigue siendo un 10% que merece diagnóstico inmediato).*

### ⚠️ 3. ¿Puedes dejar de preocuparte por el churn y volcar todo a adquisición?
**No.** Confiar en que las subidas de plan taparán indefinidamente la fuga de clientes es una trampa clásica de crecimiento temprano:

| Riesgo | Por qué importa |
|--------|----------------|
| **Techo de expansión** | No puedes subir de plan a un cliente infinitamente. Cuando la expansión se estanca, el NRR caerá por debajo del 100% si el logo churn sigue igual. |
| **LTV/CAC deteriorado** | Cada cliente que se va arrastra el CAC que invertiste en adquirirlo. Un logo churn alto obliga a adquirir más clientes solo para mantener el MRR estable, alargando el payback y reduciendo márgenes. |
| **Señal de producto/onboarding** | Perder 4 de 40 clientes en un periodo sugiere fricción en la adopción, desalineación de expectativas o presión competitiva. Ignorarlo te deja ciego ante problemas estructurales que la métrica de ingresos enmascara. |

### ✅ 4. Qué hacer ahora (visión de analista)
1. **Mide y reporta por separado:** `Logo Retention/Churn` y `Net Revenue Retention`. Son complementarias, no intercambiables.
2. **Haz un análisis de cohortes:** ¿Los 4 que se fueron eran clientes nuevos (<3 meses)? ¿De un plan específico? ¿De un segmento o canal concreto? El churn casi nunca es aleatorio.
3. **No redirijas todo el esfuerzo a adquisición.** En SaaS maduro, la regla práctica es mantener un equilibrio: ~60-70% del esfuerzo en retención/expansión y ~30-40% en adquisición. Si estás en fase early-stage, el ratio puede variar, pero abandonar la retención es suicida a medio plazo.
4. **Usa el 114% de NRR como validación, no como excusa.** Te confirma que tu modelo de precios, upsell o uso adicional funciona. Ahora aplica esa misma disciplina a entender por qué se van clientes y cierra esa fuga.

**En resumen:** tu métrica de ingresos está sana, pero tu base de clientes se está erosionando. En SaaS, el crecimiento sostenible requiere que ambas métricas apunten en la misma dirección. No abandones el churn; diagnostícalo, corrígelo y luego escala la adquisición con una base que no se desmorona.