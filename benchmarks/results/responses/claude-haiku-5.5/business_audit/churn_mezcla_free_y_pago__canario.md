# Claude Haiku 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 11.426s | tokens_per_second: 173.6
- input_tokens: 264 | output_tokens: 1983

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

**No es necesariamente grave. Probablemente el 31% es correcto aritméticamente, pero mide otra población de la que creías.**

## Qué dicen los números

- **Churn total:** 62 / 200 = **31%**. El cálculo es correcto.
- **Churn en plan gratuito:** 60 / 178 = **33,7%**
- **Churn en plan de pago:** 2 / 22 = **9,1%**

Los usuarios gratuitos son el 89% de la base y generan el 97% de las bajas. Por eso el número total se ve tan alto. Si tu 5% venía de otra definición (solo pago, solo ingresos, otro mes), habrá que encontrar de dónde salió. Con estos datos, ninguna combinación directa da 5%: el de pago es 9,1%.

## Lo que hay que verificar antes de alarmarse o tranquilizarse

1. **¿Qué cuenta como "baja"?** Si incluye cancelaciones de cuentas inactivas, eliminaciones o downgrades a gratuito, el número puede inflarse.
2. **¿El denominador es la cohorte correcta?** Si entre las 62 bajas hay usuarios que se registraron y abandonaron este mismo mes, no están en los 200 de inicio. Eso infla el churn. Filtra las bajas por fecha de alta.
3. **¿Tu definición de "churn" es de usuarios o de ingresos?** Un usuario gratuito que se va no reduce tus ingresos. Si lo que te importa es el dinero, el churn de ingresos (MRR churn) es la métrica principal.
4. **Muestra pequeña.** Con 2 bajas de pago, un solo cliente cambia el porcentaje de forma notable (1 baja = 4,5%). No saques conclusiones fuertes de ese número todavía.

## Plan

**Día 1: Entender el número**
- Confirma la definición exacta de "baja" y de "base" que usa el panel.
- Recalcula con la cohorte de inicio de mes y excluye altas y bajas del mismo mes.
- Encuentra de dónde salió el 5% anterior (mes distinto, otra definición, otro filtro).

**Días 2–3: Segmentar**
- Calcula churn de **ingresos** (MRR perdido / MRR inicial). Es la cifra que debes reportar.
- Revisa los 2 usuarios de pago que se fueron: motivo, uso previo, si hubo fallo de cobro o cambio de precio.
- Mira el churn gratuito por cohorte de alta: ¿se concentra en usuarios de la última semana? Eso apuntaría a onboarding o a una campaña de captación de baja calidad.

**Semana 1–2: Decidir**
- Si el churn de pago (9%) está por encima de tu referencia de industria o de tu historial, prioriza entrevistas a quienes se fueron y a usuarios activos en riesgo.
- Si el churn gratuito es alto pero no afecta ingresos, trátalo como un problema de activación/conversión, no de retención de clientes.
- Corrige el panel: etiqueta claramente "churn total (incl. gratuitos)", "churn de pago" y "churn de ingresos", para que nadie vuelva a comparar cifras de poblaciones distintas.

## Qué reportar hoy

> "El churn total es 31%, pero el 97% de las bajas son usuarios gratuitos. El churn de pago es 9% (2 de 22), con muestra pequeña, y estamos revisando esas dos cuentas y el churn de ingresos. El 5% anterior usaba una definición distinta que estamos reconciliando."

Si me pasas el MRR por usuario de pago o la fecha de alta de las 62 bajas, puedo calcular el churn de ingresos y el ajustado por cohorte.