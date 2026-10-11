# Claude Opus 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.17 | quality: 10.0
- latency_total: 19.922s | tokens_per_second: 88.2
- input_tokens: 264 | output_tokens: 1757

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa

# Respira: el 31% mezcla dos poblaciones muy distintas

El panel calcula una sola tasa sobre todos los usuarios, pero tus datos muestran dos realidades separadas.

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |
| Total (lo que muestra el panel) | 200 | 62 | 31% |

**El 97% de las bajas (60 de 62) son usuarios gratuitos.** El 31% es casi por completo un número del plan free.

## ¿Qué tan grave es?

**Plan de pago (lo que afecta tus ingresos): 9,1%.** Es más alto que el 5% que tenías en mente, y conviene vigilarlo. Pero son **2 clientes de 22**. Con una base tan pequeña, una sola baja mueve la tasa unos 4,5 puntos. Con 1 baja tendrías 4,5%; con 2, 9,1%. Un mes con 2 bajas no confirma una tendencia: puede ser ruido. Mira los últimos 3 a 6 meses antes de concluir algo.

**Plan gratuito: 33,7%.** Suena alto, pero en planes gratuitos es frecuente que mucha gente pruebe y se vaya. Su impacto directo en ingresos es cero. Lo relevante es si esos usuarios habrían llegado a pagar.

**Pregunta clave:** ¿tu 5% de referencia era churn de pago? Si es así, compáralo con el 9,1%, no con el 31%.

## Antes de actuar, verifica qué cuenta el panel como "baja"

1. **¿Qué significa "baja" en el plan gratuito?** ¿Cuenta borrada, inactividad de X días, o desuscripción del email? Si es "inactivo 30 días", la cifra no mide lo mismo que una cancelación de pago.
2. **¿Las 62 bajas salen de los 200 iniciales?** Si el panel incluye usuarios que se registraron y se fueron *dentro del mismo mes*, el numerador está inflado respecto al denominador y la tasa queda sobreestimada.
3. **¿Cambió algo este mes?** Una nueva regla de inactividad, una limpieza de cuentas, una migración o un cambio en cómo se calcula la métrica pueden generar saltos así de golpe.
4. **¿Qué medía tu 5% de antes?** Si antes el panel solo contaba usuarios de pago, o usaba otra definición, no estás comparando lo mismo.

## Plan de acción

**Esta semana**
- Responde las 4 preguntas de verificación.
- Contacta a los **2 clientes de pago** que se fueron: por qué cancelaron, cuánto tiempo llevaban y qué plan tenían. Con 22 clientes, cada conversación aporta mucho.
- Calcula el **churn de ingresos (MRR)**: si los 2 que se fueron pagaban poco, el impacto real es menor que el 9,1% de clientes.

**Próximas 2 a 4 semanas**
- Configura el panel para mostrar **churn de pago y churn gratuito por separado**. Una tasa combinada te volverá a asustar cada mes.
- Revisa la tendencia del churn de pago en los últimos meses para distinguir un pico puntual de un patrón.
- En el plan gratuito, mira **cuándo** se van (día 1, semana 1, mes 1). Si la mayoría abandona en los primeros días, tienes un problema de activación u onboarding, no de retención.

**Métrica que más te conviene mirar del lado gratuito**
- **Conversión de gratuito a pago.** Si de 178 usuarios gratuitos conviertes pocos, mejorar eso pesa más que reducir el 33,7% de abandono gratuito.

## Resumen

No tienes un churn del 31% en el negocio. Tienes un **churn de pago del 9,1% basado en 2 clientes** y un plan gratuito con abandono alto, que suele ser normal. Merece atención, no pánico. Si me dices qué medía tu 5% de antes y cómo define el panel una "baja", te ayudo a afinar el diagnóstico.