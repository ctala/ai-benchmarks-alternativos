# Claude Opus 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.79 | quality: 8.0
- latency_total: 15.97s | tokens_per_second: 99.0
- input_tokens: 264 | output_tokens: 1581

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

# Respira: el 31% no mide lo que crees

Ese 31% mezcla dos poblaciones muy distintas. Al separarlas, el panorama cambia por completo.

## Desglose por segmento

| Segmento | Usuarios inicio | Bajas | Churn |
|---|---|---|---|
| **Pago** | 22 | 2 | **9,1%** |
| **Gratuito** | 178 | 60 | **33,7%** |
| Total (lo que muestra el panel) | 200 | 62 | 31% |

El 97% de las bajas (60 de 62) vienen del plan gratuito. Probablemente tu "5%" se refería a clientes de pago, y ese es el número que importa para tu negocio.

## ¿Qué tan grave es?

**Churn de pago (9,1%): vigilar, sin alarma todavía.**
- Son **2 cancelaciones** sobre 22 clientes. Con un 5% esperarías ~1,1 bajas al mes, así que estás hablando de una cancelación de más.
- Con una base tan pequeña, cada cliente mueve el porcentaje ~4,5 puntos. Un solo mes no es una tendencia.
- Si se repite 2-3 meses seguidos, sí sería una señal real.

**Churn gratuito (33,7%): normal en muchos productos.**
- Los usuarios gratuitos suelen abandonar mucho más. Lo relevante es compararlo con tus meses anteriores, no con el 5%.

## Plan de acción

**1. Verifica qué cuenta el panel como "baja" (hoy)**
- ¿Un usuario que pasa de gratuito a pago se registra como "baja del plan gratuito"? Si es así, algunas de esas 60 bajas son **conversiones**, es decir, buenas noticias.
- ¿El numerador incluye usuarios que se registraron *durante* el mes y se fueron? El denominador solo cuenta los 200 de inicio de mes, así que eso inflaría el porcentaje.
- En el plan gratuito, ¿"baja" significa borrar la cuenta o solo inactividad?

**2. Cambia lo que miras en el panel (esta semana)**
- Reporta el churn **por segmento**, nunca el total mezclado.
- Añade el **churn de ingresos (MRR churn)**: ¿qué porcentaje de la facturación se perdió con esas 2 cancelaciones?
- Saca el histórico de los últimos 3-6 meses de cada segmento para saber si el 33,7% gratuito es habitual o un pico.

**3. Investiga las 2 bajas de pago (esta semana)**
- Contacta a ambos clientes: motivo de la cancelación, antigüedad, plan, uso previo.
- Con solo 2 casos, la conversación directa te dará más información que cualquier métrica.

**4. Para el plan gratuito (próximo mes)**
- Mira **cuándo** se van: ¿en la primera semana (problema de onboarding) o tras meses de uso (falta de valor continuo)?
- Mide la **tasa de conversión gratuito → pago**, que es la métrica clave de ese segmento.

## Resumen
Tu negocio de pago no está perdiendo un tercio de sus clientes. Perdiste 2 de 22, un poco por encima de lo habitual pero dentro del ruido estadístico para una base tan pequeña. Lo urgente es corregir el panel para que no vuelva a mezclar segmentos, y confirmar que las "bajas" gratuitas no incluyan conversiones a pago.