# Muse Ember — business_audit/churn_mezcla_free_y_pago

- model_id: `meta/muse-ember`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 8.337s | tokens_per_second: 376.0
- input_tokens: 181 | output_tokens: 3135

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

No interpretes el 31% todavía. Antes de entrar en pánico, hay que verificar **qué población está midiendo**.

Tu panel mezcló dos poblaciones con comportamientos totalmente distintos: usuarios gratuitos y usuarios de pago. El 31% es aritméticamente correcto, pero como métrica de negocio es engañoso.

### 1. Recalculemos por segmento

| Segmento | Inicio de mes | Bajas | Churn real |
| :--- | :--- | :--- | :--- |
| **Total** | 200 | 62 | **31,0%** |
| **Gratuito** | 178 | 60 | **33,7%** |
| **Pago** | 22 | 2 | **9,1%** |

Eso cambia el diagnóstico por completo:

**No estás perdiendo el 31% de tu negocio. Estás perdiendo el 9,1% de tus clientes de pago.**

Y el 5% que creías tener antes probablemente era *solo* el churn de pago. No es que hayas saltado de 5% a 31% en un mes, es que cambió la definición del panel.

### 2. ¿Qué tan grave es entonces?

**Para el plan gratuito: 33,7% es alto, pero primero hay que auditarlo.**
¿Esos 178 gratuitos estaban activos al inicio del mes, o son cuentas registradas hace meses que ya no usaban el producto y simplemente se dieron de baja / fueron purgadas? Si el denominador incluye “zombies”, el churn de gratuitos no te dice nada sobre retención real. Y si no convertían a pago, perderlos no es perder ingresos.

**Para el plan pago: 9,1% es preocupante, pero no es una crisis.**
Con solo 22 clientes, la métrica es extremadamente volátil:
- 5% de 22 = 1,1 clientes
- 9,1% de 22 = 2 clientes

La diferencia entre tu 5% esperado y el 9,1% actual es **literalmente 1 cliente extra**. Un solo cliente más o menos te mueve 4,5 puntos porcentuales. No puedes tomar decisiones con 1 mes y n=22.

Dicho eso, si se repite, sí es insostenible: con 9,1% mensual te quedas en ~32% de la base en 12 meses sin adquisiciones. Con 5% te quedarías en ~54%. Hay que bajarlo, pero con calma.

### 3. Plan de acción

**En las próximas 48 horas: Verificar, no actuar**

1.  **Audita la definición:** ¿Las 62 bajas son bajas voluntarias reales? ¿O incluye cuentas de prueba, duplicadas, purgas por inactividad e impagos involuntarios? Revisa las 2 bajas de pago en detalle: ¿una fue por tarjeta rechazada?
2.  **Lista a tus 20 clientes de pago que quedan.** Son todo tu ingreso. No lances una campaña masiva a los 60 gratuitos que se fueron.
3.  **Contacta a los 2 pagos que se fueron.** Una llamada de 10 minutos vale más que cualquier dashboard. ¿Fue precio, falta de uso, soporte, o un problema de pago?

**Esta semana: Diagnosticar solo el segmento pago**

1.  Cruza las 2 bajas con: antigüedad (¿eran nuevos?), último uso, tickets de soporte, y fallos de pago. El churn de clientes de <30 días es un problema de onboarding; el de clientes viejos es de valor.
2.  Recalcula el churn gratuito solo sobre **activos en los 30 días previos**. Si baja de 33% a, por ejemplo, 12%, tu problema era de medición, no de producto.
3.  Haz una lista de riesgo con tus 20 pagos: sin login en 14 días, uso cayendo, ticket abierto, pago próximo a vencer. Contacto personal, no descuento automático para todos.

**Este mes: Arreglar la medición para que no vuelva a pasar**

Deja de reportar un churn único. Ten 3 métricas separadas:
1.  **Churn de clientes de pago (logo churn):** bajas de pago / pagos al inicio. Meta: <5%
2.  **Churn de ingresos (revenue churn):** MRR perdido / MRR inicial. Si los 2 que se fueron eran del plan más barato, el impacto es menor.
3.  **Churn de gratuitos activos:** bajas / gratuitos activos al inicio.

Y usa un promedio móvil de 3 meses para el pago hasta que tengas >50 clientes de pago. Con 22, cualquier mes aislado te va a mentir.

**Qué NO hacer:** No gastes tu semana tratando de “rescatar” a los 60 gratuitos con descuentos o emails masivos. Si su tasa de conversión a pago es baja, estás optimizando la métrica equivocada y descuidando a los 20 que sí pagan.

En resumen: tu alarma del 31% es un artefacto de mezclar poblaciones. Tu problema real es manejable: 2 clientes de pago perdidos que hay que entender, y una base de pago demasiado pequeña para medir con confianza.

¿Sabes si esos 2 pagos fueron voluntarios o por fallo de pago, y cuánto tiempo llevaban contigo? Con eso te digo si es un problema de onboarding o de retención de largo plazo.