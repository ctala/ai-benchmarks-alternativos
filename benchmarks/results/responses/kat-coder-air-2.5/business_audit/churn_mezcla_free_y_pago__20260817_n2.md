# KAT Coder Air v2.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.11 | quality: 10.0
- latency_total: 8.07s | tokens_per_second: 192.3
- input_tokens: 189 | output_tokens: 1552

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



## Diagnóstico rápido

**El churn del 31% es real, pero no es homogéneo.** Al desglosarlo por plan, la situación cambia radicalmente:

| Segmento | Bajas | Usuarios inicio mes | Churn real |
|----------|-------|---------------------|------------|
| Plan gratuito | 60 | 178 | **33.7%** |
| Plan de pago | 2 | 22 | **9.1%** |

### ¿Qué tan grave es?

1. **Plan gratuito (33.7% churn)**: Alto pero **típico en freemium**. Los usuarios gratuitos tienen baja lealtad y alta rotación natural. No es sostenible, pero no es una emergencia inmediata si el objetivo es convertir a pagos.

2. **Plan de pago (9.1% churn)**: **Esto sí es crítico**. Un churn mensual del 9% en clientes de pago equivale a perder el 108% de la base anualizada (si se mantiene). Cada cliente de pago que se va tiene un valor mucho mayor que uno gratuito.

3. **El problema de fondo**: El churn general del 31% está **distorsionado por el volumen de usuarios gratuitos**. Si quitas el plan gratuito, el churn real de tu base de ingresos es del 9.1%, que ya es alto pero manejable.

## Plan de acción inmediato

### Semana 1: Diagnóstico y contención
1. **Verifica la calidad de datos**: Asegúrate de que las 60 bajas gratuitas no sean errores de sincronización o cuentas duplicadas.
2. **Entrevista a los 2 clientes de pago que se fueron**: Llama personalmente. Pregunta específicamente:
   - ¿Qué problema no se resolvió?
   - ¿Qué alternativa elegiste?
   - ¿Qué te hubiéramos ofrecido para quedarte?
3. **Revisa cambios recientes**: ¿Hubo cambios en el producto, precios, soporte o comunicación en los últimos 30 días?

### Semana 2-4: Estrategias por segmento
**Para el plan gratuito:**
- Implementa un **onboarding guiado** que muestre el valor central en los primeros 3 días.
- Crea un **programa de re-engagement** para usuarios gratuitos inactivos (ej: "¿Te falta X funcionalidad? Te ayudamos").
- Define un **umbral de conversión** claro: qué acciones deben completar para ser candidatos a pago.

**Para el plan de pago:**
- **Programa de salud de cuenta**: Identifica usuarios con señales de riesgo (bajo uso, tickets de soporte sin resolver, facturas impagas).
- **Ofrece check-ins proactivos**: Revisa con tus clientes de pago si están obteniendo valor.
- **Crea un programa de lealtad**: Descuentos por antigüedad, acceso anticipado a features, soporte prioritario.

### Métricas que debes empezar a medir
1. **Churn por cohorte** (no solo global)
2. **NPS por segmento**
3. **Tasa de conversión gratuito → pago**
4. **Tiempo hasta la primera acción de valor** (time-to-first-value)

## Prioridad absoluta

**Detén la hemorragia de clientes de pago.** El churn del 9.1% en ese segmento es lo que te mantiene despierto de noche. Los usuarios gratuitos se van y vienen; los de pago son tu sostenibilidad.

¿Quieres que profundice en alguna de estas acciones o necesitas ayuda para diseñar un plan de retención específico para tu tipo de plataforma?