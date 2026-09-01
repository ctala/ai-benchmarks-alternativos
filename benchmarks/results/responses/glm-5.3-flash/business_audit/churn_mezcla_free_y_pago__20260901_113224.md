# GLM 5.3 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 97.198s | tokens_per_second: 40.4
- input_tokens: 177 | output_tokens: 3926

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

Respira: el 31% es un cálculo correcto de algo que casi no te dice nada. El panel mezcla dos poblaciones que se van por razones distintas y que valen cosas distintas.

## Lo que realmente mide ese 31%

| Población | Inicio de mes | Bajas | Churn | Qué significa |
|---|---|---|---|---|
| Gratuitos | 178 | 60 | **33,7%** | Nunca pagaron; su salida no toca ingresos |
| Pago | 22 | 2 | **9,1%** | Este es tu churn real de negocio |
| Total (panel) | 200 | 62 | 31% | Mezcla de dos poblaciones con valor muy distinto |

El panel no miente, pero responde la pregunta equivocada: "¿qué % de cuentas se fue?" cuando tu pregunta de negocio es "¿qué % de valor se fue?".

## ¿De dónde salió el salto de 5% a 31%?

Un negocio casi nunca multiplica su churn real por 6 en un mes sin que haya un evento visible (subida de precios, caída del servicio, lote de renovaciones fallidas). Lo más probable es que **cambió lo que mides, no tu negocio**. Hipótesis a verificar:

1. El 5% anterior era churn solo de pago (ej.: 1/22 ≈ 4,5% el mes pasado) y el panel empezó a incluir gratuitos.
2. El 5% era churn de ingresos (MRR), no de número de cuentas.
3. Cambió la definición de "baja": si un usuario gratuito cuenta como baja por inactividad de 30 días, acabas de empezar a medir algo distinto.

Revisa la configuración del panel y exportaciones de meses anteriores. Necesitas esta respuesta antes del próximo reporte, porque alguien te va a preguntar.

## ¿Qué tan grave es?

- **Pago (9,1% mensual):** alto para B2B (si se sostuviera, perderías ~2 de cada 3 clientes en un año), pero son **n=2**. Con 22 clientes, cada baja mueve la tasa 4,5 puntos. Un mes no hace tendencia; dos salidas pueden ser casualidad o un motivo común fácil de arreglar.
- **Gratuitos (33,7%):** suena fuerte, pero pregunta primero cómo define "baja" un usuario gratuito. Si es inactividad, es un número de embudo, no de negocio. Para gratuitos lo que importa es activación y conversión a pago (tienes 22/200 = 11% de base paga).

## Plan

1. **Hoy:** aclara en el panel qué cuenta como "baja" para gratuitos, desde cuándo los incluye, y reconstruye de dónde salió el 5% histórico.
2. **Esta semana:** contacta a los 2 clientes de pago que se fueron. Con n=2, la entrevista vale más que cualquier tasa. ¿Por qué se fueron? ¿Había señales? ¿Era evitable?
3. **Cambia el dashboard:** el titular debe ser churn de pago (logos y, mejor aún, churn de MRR). Los gratuitos se reportan como activación y conversión, no como churn.
4. **Revisa antigüedad de los 60 gratuitos que se fueron:** si son mayormente de cohortes recientes (una campaña, por ejemplo), el % se infla solo y no indica deterioro.
5. **Calcula churn de MRR:** si los 2 que cancelaron eran los planes más caros, el 9,1% subestima el daño real.

**En una línea:** la cifra que llevas al equipo es 9,1% (o churn de MRR), no 31% — y verifica el panel antes de que ese 31% llegue a oídos de alguien más.