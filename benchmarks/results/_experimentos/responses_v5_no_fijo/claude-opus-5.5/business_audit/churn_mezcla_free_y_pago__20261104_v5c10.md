# Claude Opus 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.18 | quality: 10.0
- latency_total: 18.157s | tokens_per_second: 95.0
- input_tokens: 264 | output_tokens: 1725

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

# Primero, respira: el 31% no es tu churn de clientes de pago

El panel mezcla dos poblaciones que se comportan de forma muy distinta. Si las separas, el panorama cambia:

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| **Gratuito** | 178 | 60 | **33,7%** |
| **De pago** | 22 | 2 | **9,1%** |
| Total (lo que muestra el panel) | 200 | 62 | 31% |

El 97% de las bajas (60 de 62) vienen del plan gratuito. **El 31% es casi por completo un número de usuarios gratuitos**, no de clientes que te pagan.

## ¿Qué tan grave es?

**Plan de pago (9,1%)**
- Es más alto que el 5% que esperabas, pero con 22 clientes cada baja mueve la métrica unos 4,5 puntos. La diferencia entre 5% y 9% es **una sola cancelación**: el mes pasado probablemente tuviste 1 y este mes 2.
- Con una muestra tan pequeña, un mes aislado no indica una tendencia. Necesitas ver 3 a 6 meses.
- Aun así, un 9% mensual sostenido sería alto (más del 60% anual), así que vale la pena vigilarlo.

**Plan gratuito (33,7%)**
- Es alto, pero los planes gratuitos suelen tener rotación alta. Su gravedad depende de qué significa "baja" para un usuario gratuito, y eso es lo primero que hay que verificar.

## Plan de acción

**1. Verifica la definición de "baja" (hoy mismo)**
- Para usuarios de pago, ¿"baja" es cancelar la suscripción, un pago fallido o un downgrade a gratuito?
- Para gratuitos, ¿es eliminar la cuenta o simplemente inactividad durante X días?
- ¿Cambió la definición o la configuración del panel recientemente? Un salto de 5% a 31% a menudo se debe a que el panel empezó a incluir gratuitos o cambió el criterio de inactividad, no a que se fueran más clientes.
- Confirma qué medía tu "5%" anterior. Si era solo churn de pago, estás comparando peras con manzanas.

**2. Separa las métricas en el panel (esta semana)**
- Churn de clientes de pago (tu métrica principal).
- Churn de ingresos (MRR perdido / MRR inicial). Si los 2 que se fueron estaban en planes baratos, el impacto real es menor, y viceversa.
- Retención o activación de gratuitos (es una métrica de embudo, no de negocio).

**3. Investiga las 2 bajas de pago (esta semana)**
Con solo 2 casos, puedes revisarlos uno por uno:
- ¿Cancelación voluntaria o pago fallido? El churn involuntario se reduce con reintentos de cobro y avisos de tarjeta vencida.
- ¿Cuánto tiempo llevaban? ¿Qué uso tenían antes de irse?
- Si puedes, contáctalos y pregúntales por qué se fueron. Con 22 clientes, cada conversación vale oro.

**4. Analiza la rotación del plan gratuito (próximas 2 semanas)**
- ¿Las bajas se concentran en usuarios recién registrados (por ejemplo, en la primera semana)? Eso indicaría un problema de onboarding o activación, no de retención.
- ¿Llegó este mes una oleada de registros de baja calidad (campaña, tráfico de una fuente nueva)? Eso inflaría las bajas sin que nada se haya roto.
- Revisa la tasa de conversión de gratuito a pago, que probablemente importa más que su churn.

**5. Establece seguimiento por cohortes (este mes)**
- Mide la retención por mes de alta, no solo el agregado mensual.
- Para el plan de pago, mira la media móvil de 3 meses, para que una sola cancelación no te vuelva a asustar.

## En resumen

No tienes un 31% de clientes yéndose. Tienes **2 clientes de pago que cancelaron** (9,1%, poco fiable por el tamaño de la muestra) y **mucha rotación de usuarios gratuitos**, cuya gravedad depende de cómo se define la baja. Lo urgente es verificar la definición, separar las métricas y hablar con esos 2 clientes.