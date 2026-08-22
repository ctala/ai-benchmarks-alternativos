# GLM 5.3 — business_audit/churn_mezcla_free_y_pago

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.33 | quality: 10.0
- latency_total: 55.435s | tokens_per_second: 64.9
- input_tokens: 177 | output_tokens: 3598

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

# Primero, respira: tu churn de negocio no es 31%

El panel está midiendo una **población mezclada** donde el 89% son usuarios gratuitos, que se van sin fricción porque no pagan nada. Al separar las poblaciones:

| Segmento | Usuarios inicio de mes | Bajas | Churn real |
|---|---|---|---|
| Gratuito | 178 | 60 | **33.7%** |
| Pago | 22 | 2 | **9.1%** |
| Mezclado (lo que reporta el panel) | 200 | 62 | 31.0% |

El 31% es un artefacto aritmético, no una señal de negocio. Estabas comparando un churn de pago (~5%) contra un churn de todos los usuarios. Son métricas de especies distintas.

**El dato tranquilizador:** con 22 usuarios de pago, cada usuario que se va vale 4.5 puntos porcentuales. La diferencia entre tu "5%" recordado y el 9.1% actual es literalmente **un usuario**. Con n=22, esa cifra es estadísticamente ruidosa: el churn de pago real podría estar entre ~2% y ~27%.

# ¿Qué tan grave es? Tres cosas separadas

1. **Churn de pago (9.1%)**: es la cifra que importa y está elevada para SaaS maduro (1-3% mensual), pero con 22 usuarios estás en etapa donde las entrevistas valen más que la tasa.
2. **Churn gratuito (33.7%)**: no es "churn" en el sentido de negocio — es fuga de funnel. Lo relevante ahí es activación y conversión, no retención a toda costa.
3. **El problema operativo real**: casi tomas una decisión de pánico sobre una métrica mal definida. Eso es lo que hay que arreglar primero.

# Plan

**Hoy — corregir la medición**
- Segmenta el panel por plan. El churn mezclado no debe volver a ser tu cifra de cabecera.
- Investiga de dónde salía tu 5%: ¿era churn solo de pago en meses anteriores? ¿Cambió la definición del panel? ¿Creció el plan gratuito recientemente (campaña, freemium nuevo)?
- No comuniques el 31% a nadie como cifra de negocio.

**Esta semana — validar la señal de pago**
- Trae la serie histórica de churn de pago (3-6 meses). ¿El 9.1% es tendencia o ruido de un mes?
- Entrevista a los 2 que se fueron. Con 22 clientes, 2 entrevistas te dicen más que cualquier tasa.
- Calcula churn de **ingresos** (MRR perdido / MRR inicial), no solo de logos: si los que se fueron eran tus cuentas grandes, el 9.1% subestima el daño; si eran las pequeñas, lo sobreestima.

**Esta semana — diagnosticar el gratuito**
- Segmenta las 60 bajas por cohorte de registro y por activación: ¿alguna vez hicieron la acción clave del producto? Bajas de usuarios que nunca activaron son ruido; bajas de usuarios activados son señal.
- Compara contra tu propio baseline, no contra benchmarks externos. Si el gratuito siempre churnea así y el funnel convierte, no hay problema.

**Mediano plazo — gobernanza**
- Define KPIs separados y por escrito: churn de pago (logos), churn de MRR, retención de gratuitos por cohorte, tasa de conversión gratuito→pago.
- Antes de interpretar cualquier métrica del panel, pregunta siempre: ¿qué población está en el denominador?

**Lo que NO hagas:** campañas de retención agresivas sobre usuarios gratuitos o mecanismos para dificultar la baja. El palanca para los gratuitos es activación y conversión, no retención forzada.

¿Quieres que armemos la plantilla de entrevista para los 2 clientes de pago que se fueron, o el cálculo de churn de MRR si me pasas el valor de las suscripciones?