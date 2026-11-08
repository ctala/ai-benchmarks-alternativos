# Mercury 3 — business_audit/churn_mezcla_free_y_pago

- model_id: `inception/mercury-3`
- success: True  | final: 7.76 | quality: 8.0
- latency_total: 6.992s | tokens_per_second: 296.1
- input_tokens: 189 | output_tokens: 2070

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

Tranquilo. Antes de entrar en pánico, vamos a separar lo que está pasando. Tu panel te está dando un número técnicamente correcto, pero que mide la población equivocada.

## Lo que realmente dicen tus datos

| Segmento | Usuarios inicio | Bajas | Churn |
|---|---:|---:|---:|
| Plan gratuito | 178 | 60 | **33.7%** |
| Plan de pago | 22 | 2 | **9.1%** |
| Total | 200 | 62 | **31%** |

El 31% es el resultado de mezclar dos poblaciones muy distintas. El churn alto está siendo impulsado casi por completo por el plan gratuito.

## ¿Qué tan grave es?

Depende de qué sea lo que te importa:

- **Si te importa el ingreso**, tu churn real de clientes de pago es **9.1%**, no 31%. Sigue siendo un número que hay que vigilar, pero no es una catástrofe. Además, con solo 22 clientes de pago, 2 bajas representan un 9%; el mes que viene puede ser 0% o 18% sin que cambie mucho el comportamiento real. Es ruido estadístico.

- **Si te importa el crecimiento de la base**, sí tienes un problema real: estás perdiendo un tercio de tus usuarios gratuitos cada mes. Pero antes de alarmarte, hay que entender **por qué**.

## Plan de acción

### 1. Verifica la definición de “baja”
¿Qué cuenta como baja? ¿Cancelación explícita? ¿No renovación? ¿Inactividad de 30 días? Exporta la tabla y mira el motivo de cada baja. Si muchas de las 60 bajas gratuitas son cuentas que nunca usaron el producto o que fueron purgadas por inactividad, entonces no estás “perdiendo” usuarios reales, estás limpiando una base de datos inflada.

### 2. Corrige el panel
Crea dos métricas separadas:

- **Churn de clientes de pago**: bajas de pago / clientes de pago al inicio.
- **Churn de usuarios gratuitos**: bajas gratuitas / usuarios gratuitos al inicio.

Nunca más mezcles ambas en un solo indicador.

### 3. Investiga el churn gratuito
60 de 178 es muchísimo. Mira:

- ¿Cuándo se registraron? ¿Son usuarios viejos o nuevos?
- ¿Cuánto usaron el producto antes de irse? ¿Alguna vez lo usaron?
- ¿Hay algún cambio reciente en el onboarding o en los límites del plan gratuito?

Si son cuentas fantasma, exclúyelas del denominador. Si son usuarios que realmente probaron el producto y se fueron, ahí sí tienes un problema de activación o de propuesta de valor.

### 4. Investiga el churn de pago
2 bajas de 22 es una muestra muy pequeña. Habla con esos dos clientes. Pregúntales por qué se fueron. También revisa su historial de uso: ¿estaban activos antes de cancelar? ¿Dejaron de usar el producto semanas antes?

Con n tan pequeña, no tomes decisiones drásticas basadas en un solo mes. Mira la tendencia de los últimos 3 a 6 meses.

### 5. Define tu métrica de negocio
Si tu modelo depende de ingresos recurrentes, tu norte debe ser:

> **Churn de clientes de pago** = bajas de pago / clientes de pago al inicio.

El churn de gratuitos es relevante para el embudo, pero no debería ser el número que te quite el sueño por la noche.

## Resumen

- El 31% es un artefacto de mezclar planes.
- Tu churn de pago real es ~9%, y con una muestra tan pequeña no es para pánico.
- El churn gratuito de 34% es alto, pero necesitas entender si esos usuarios eran reales o cuentas muertas.
- Corrige el panel, segmenta y monitorea por separado.

Ahora respira. El primer paso es arreglar la métrica. El segundo es hablar con los clientes que se fueron. El tercero es decidir si el problema es de producto, de pricing o de definición.