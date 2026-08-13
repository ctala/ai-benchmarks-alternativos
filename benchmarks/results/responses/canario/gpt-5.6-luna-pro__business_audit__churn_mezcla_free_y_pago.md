# GPT-5.6 Luna Pro — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 21.352s | tokens_per_second: 253.8
- input_tokens: 7221 | output_tokens: 5419

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

Respira: el **31% está bien calculado para toda la base**, pero probablemente **no es la métrica que importa para el negocio** si tu objetivo del 5% se refería a clientes de pago.

## Qué está midiendo realmente el panel

| Segmento | Base al inicio | Bajas | Churn |
|---|---:|---:|---:|
| Todos los usuarios | 200 | 62 | **31,0%** |
| Gratuitos | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |

Además:

- El **96,8% de las bajas** fueron gratuitas.
- Solo el **3,2% de las bajas** fueron de pago.
- El churn de pago es 2/22, por lo que una sola baja cambia mucho el porcentaje: cada usuario equivale a aproximadamente **4,5 puntos porcentuales**.

## ¿Qué tan grave es?

### Para el negocio de pago

Es **peor que el 5% esperado**, pero no parece una catástrofe con solo 22 clientes:

- Esperarías aproximadamente **1 baja** con un churn del 5%.
- Observaste **2 bajas**.
- Con una base tan pequeña, el porcentaje es muy volátil. No concluiría todavía que existe un deterioro estructural.

Si esos dos clientes representan mucho MRR, sí puede ser grave financieramente. Por eso debes calcular también:

- **Revenue churn**: MRR perdido / MRR al inicio.
- Churn de clientes de pago.
- Expansión, contracción y reactivaciones.
- Churn por plan, antigüedad y canal de adquisición.

### Para el producto gratuito

El dato sí es llamativo: **60 de 178 usuarios gratuitos se dieron de baja**, un 33,7%. Pero primero hay que comprobar qué significa “baja”. Puede incluir:

- Eliminación de cuenta.
- Inactividad o usuarios considerados perdidos por el panel.
- Fin de una prueba gratuita.
- Conversión de gratuito a pago.
- Cambio de plan.
- Usuarios duplicados o registros de baja calidad.

No es correcto interpretar automáticamente esas 60 bajas como pérdida económica equivalente a 60 clientes.

## Plan de acción

### 1. Validar la definición y los datos hoy

Confirma que:

1. El denominador son usuarios **activos al inicio del mes**, no usuarios creados históricamente.
2. Las 62 bajas son cancelaciones reales, no simplemente usuarios inactivos.
3. El plan se asigna según el estado **al inicio del mes**. Si clasificas por el plan actual, podrías estar mezclando conversiones y cambios de plan.
4. No hay duplicados, reactivaciones o cancelaciones administrativas.
5. El periodo mensual está completo y no hay retrasos de facturación.

Usa una definición explícita, por ejemplo:

> Churn mensual de pago = clientes de pago activos al inicio del mes que cancelaron durante el mes / clientes de pago activos al inicio del mes.

### 2. Separa el panel en métricas útiles

No muestres un único churn agregado. Como mínimo, reporta:

- Churn de usuarios gratuitos.
- Churn de clientes de pago.
- Revenue churn.
- Número de clientes de pago al inicio.
- Bajas de pago y MRR perdido.
- Conversiones gratuito → pago.
- Reactivaciones.
- Retención por cohorte.

El 31% puede permanecer como métrica descriptiva de toda la población, pero no debe ser el KPI principal de retención de ingresos.

### 3. Investiga las dos bajas de pago

Para cada una, revisa:

- Motivo declarado de cancelación.
- Antigüedad.
- Plan y MRR.
- Canal de adquisición.
- Uso reciente del producto.
- Tickets o incidencias.
- Si fue una cancelación voluntaria, fallo de cobro o downgrade.
- Si volvió a registrarse o cambió de plan.

Con solo dos casos, haz entrevistas o análisis manual: cada caso aporta mucha información.

### 4. Diagnostica las 60 bajas gratuitas

Divide esas bajas en categorías:

- Usuarios que nunca activaron el producto.
- Usuarios que probaron y abandonaron.
- Usuarios que se convirtieron a pago.
- Usuarios que eliminaron la cuenta.
- Usuarios que simplemente dejaron de usarla.
- Usuarios adquiridos por campañas o canales concretos.

Busca especialmente el embudo:

**registro → activación → primer valor → uso recurrente → conversión**

Es posible que el problema no sea “retención” sino adquisición de usuarios gratuitos con baja intención.

### 5. Define objetivos por población

No uses el 5% sin especificar el denominador. Por ejemplo:

- Churn mensual de pago: objetivo ≤ 5%.
- Revenue churn mensual: objetivo definido según MRR.
- Retención de usuarios gratuitos: medirla por activación y cohortes, no necesariamente con el mismo umbral que el pago.
- Conversión de gratuito a pago: objetivo separado.

### 6. Monitorea durante los próximos 2–3 meses

Con 22 clientes de pago, evita reaccionar a un solo mes. Construye una serie de:

- Clientes de pago al inicio.
- Bajas de pago.
- MRR perdido.
- Churn mensual y media móvil de tres meses.
- Churn por cohorte.

## Conclusión

El **31% no es un error aritmético**: corresponde a los 200 usuarios mezclando gratuitos y de pago. Pero está dominado por los usuarios gratuitos y puede estar exagerando la gravedad comercial.

La lectura correcta, con los datos actuales, es:

- **Usuarios gratuitos:** churn muy alto, que requiere diagnóstico de activación y calidad de adquisición.
- **Clientes de pago:** 2 bajas de 22, **9,1%**, por encima del 5% esperado, pero con una muestra demasiado pequeña para afirmar una tendencia.
- **Prioridad inmediata:** validar qué significa “baja”, calcular el impacto en MRR y analizar individualmente los dos clientes de pago.