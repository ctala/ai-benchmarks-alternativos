# MiMo V2.6 Pro — business_audit/retention_sobre_100_interpretacion

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 77.924s | tokens_per_second: 31.2
- input_tokens: 149 | output_tokens: 2429

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## No — tu lectura mezcla dos métricas distintas

Hay dos errores importantes en la interpretación, y ambos van en el sentido de restarle gravedad a lo que está pasando.

**1. La retención de clientes no puede superar el 100%.** Es una cuenta de clientes: de 40 pasaste a 36, así que la retención de clientes es **90%** y el churn de clientes del mes fue **10%**. Se te fueron 4 clientes, no "prácticamente nadie".

**2. El 114% es retención de *ingresos*, no de clientes.** Y como supera el 100%, casi con certeza es NRR (Net Revenue Retention), que **incluye las expansiones**: subidas de plan, asientos adicionales, add-ons. Fórmula:

```
NRR = (MRR inicial − churn − contracción + expansión) / MRR inicial
```

Un GRR (gross, sin expansión) nunca podría superar el 100%. Si tu panel dice 114%, lo que mide es que los clientes que *sí* quedan te pagan bastante más que antes.

## El ejemplo con números de tu caso

Supongamos MRR inicial de 4.000 (40 clientes × 100):

| Concepto | Importe |
|---|---|
| MRR inicial | 4.000 |
| − 4 clientes perdidos (planes pequeños, ~50 c/u) | −200 |
| + Expansiones (subidas de plan) | +760 |
| **MRR final** | **4.560 → 114%** |

Los ingresos suben, pero **el número de clientes que pagan baja un 10%**. Las subidas de plan taparon el agujero.

## Por qué esto no es para dejar de preocuparte

- **El churn de clientes es serio.** 10% mensual implica retener solo ~28% de la cohorte tras 12 meses (0,9¹²) si la tendencia continúa. Eso no se sostiene aunque el NRR sea estupendo.
- **La expansión tiene techo; el churn no.** Un cliente puede subir de plan dos o tres veces. Pero la pérdida es ilimitada. El 114% depende de que sigan llegando subidas, y ese motor se agota: en algún momento los que quedan ya están en el plan tope.
- **Riesgo de concentración.** Pocos clientes grandes que crecen pueden dar un NRR brillante mientras la base se erosiona. Si esos upgrades vienen de 3-4 cuentas, una sola partida te hunde la métrica.
- **Patrón de fuga de abajo.** Si los que se van son sistemáticamente los de plan pequeño, probablemente tienes un problema de **activación o onboarding**: la gente entra barata, no encuentra valor, y se va. Los que sobreviven son los que encajan. Eso es señal, no ruido.

## Qué mirar antes de decidir

1. **GRR y NRR por separado.** El GRR (sin expansión) te dice cuánto pierdes de verdad; es la métrica que el panel te está escondiendo.
2. **Churn de clientes vs. churn de ingresos.** Ambos, siempre juntos.
3. **Curvas de cohortes por mes de alta** para ver si las cohortes recientes retienen peor que las antiguas.
4. **Por qué se fueron esos 4.** Entrevistas de salida o al menos motivo de baja: ¿no activaron? ¿precio? ¿falta de feature?
5. **Concentración de ingresos**: % de MRR en los 5 clientes principales.
6. Verifica también que tu panel **excluya clientes nuevos** en ese cálculo; si los incluye, el 114% no es NRR, es crecimiento de ingresos, y no mide retención de nada.

## Qué hacer

No es "churn *o* adquisición". Las dos cosas van:

- **Sí sigue captando** y sí sigue vendiendo upsells — el motor de expansión es tu mejor activo y conviene potenciarlo.
- **No abandones el churn.** Prioriza activación de clientes nuevos de plan bajo: es probablemente la causa de las 4 bajas y de la caída del 10% de la base.
- **Corrige el panel mental:** tu narrativa para inversores/equipo debería ser "NRR 114%, retención de clientes 90%, churn de logo 10% mensual". Decir solo "retención 114%" sería, deliberadamente o no, ocultar la parte mala.

**En resumen:** el 114% es real y es algo positivo, pero te está tapando la pérdida de 1 de cada 10 clientes. Es exactamente el tipo de métrica que se ve bien hasta que se veía mal.