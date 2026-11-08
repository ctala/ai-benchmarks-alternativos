# Kimi K2.7 Code — business_audit/churn_mezcla_free_y_pago

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 59.476s | tokens_per_second: 44.1
- input_tokens: 201 | output_tokens: 2620

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

Respiro primero: **no está todo en 31%**. El panel no está “mintiendo”, pero está mezclando dos poblaciones distintas. Antes de actuar hay que separarlas.

## 1. Verifica qué está midiendo realmente

El cálculo del panel:

- **62 bajas / 200 usuarios a inicio de mes = 31%**

Aritméticamente es correcto, **pero mezcla gratuito y de pago**. En una plataforma los usuarios de pago son tu motor económico; perderlos no es lo mismo que perder usuarios free.

Si segmentamos:

| Segmento | Usuarios inicio | Bajas | Churn real |
|---|---:|---:|---:|
| Gratuito | 178 | 60 | **33,7%** |
| De pago | 22 | 2 | **9,1%** |
| **Total** | **200** | **62** | **31,0%** |

**Conclusión inmediata:** tu churn de pago no es 31%, es 9,1% mensual. Eso cambia totalmente la gravedad.

## 2. ¿Qué tan grave es?

Depende de tu modelo:

- **Si el negocio vive de los pagos:** el churn relevante es el de pagos. **9,1% mensual** sigue siendo preocupante si lo extrapolamos: aproximadamente **68% anual** de pérdida de clientes de pago. Muchos SaaS B2B saludables buscan <2–5% mensual; B2C/Prosupuesto acepta algo más. **No es catastrófico, pero requiere atención urgente.**
- **Si el plan gratuito es principalmente “cebo” para convertir:** 33,7% de churn free puede ser normal si muchos se registran, prueban y se van. Pero si también reduce el volumen de gente que llega a pagar, te está comiendo el funnel.
- **El dato que más duele son los 2 de pago**, no los 60 free. Perder 2 de 22 es perder casi 1 de cada 10 ingresos recurrentes (o más, si esos 2 eran de alto valor).

**Necesitas calcular también:**
- **Churn de ingresos** (revenue churn), no solo de logos.
- **Churn por cohorte** (¿se van en el primer mes? ¿luego de un año?).
- **Churn voluntario vs. fallos de pago** (involuntario).

## 3. Plan de acción (ordenado)

### Ahora mismo (esta semana)

1. **Separa el dashboard.** El churn total puede seguir existiendo, pero la métrica principal debe ser **churn de usuarios de pago** y **churn de ingresos**. Reporta gratuito por separado.
2. **Revisa la definición de “baja”** en el panel:
   - ¿Incluye cancelaciones técnicas (tarjeta rechazada, expiración)?
   - ¿Incluye usuarios que nunca activaron la cuenta?
   - ¿El denominador es “usuarios activos” o “usuarios registrados”?
3. **Contacta a los 2 clientes de pago perdidos.** Si puedes, llámalos o envía una encuesta de salida. En B2B/SaaS, perder solo 2 usuarios puede tener una causa muy específica (un bug, un cambio de precio, un feature que eliminaste).
4. **Revisa los 60 bajas free:** ¿cuántos nunca usaron la plataforma? ¿cuántos se dieron de baja en los primeros 7 días? Eso apunta a un problema de **onboarding**, no de retención.

### En las próximas 2 semanas

5. **Construye cohortes:**
   - Churn por mes de registro.
   - Churn por plan, por tamaño de cuenta, por canal de adquisición, por NPS/satisfacción.
6. **Calcula churn de ingresos:** si un plan paga \$100/mes y otro \$500/mes, perder 2 usuarios no es lo mismo. Necesitas **Net Revenue Retention (NRR)**.
7. **Identifica causas:** tickets de soporte, encuestas de salida, análisis de uso previo a la baja, pagos fallidos, cambios recientes en producto o precios.

### De aquí a 1 mes

8. **Crea alertas tempranas:**
   - Usuarios que no han iniciado sesión en X días.
   - Pagos fallidos.
   - Caídas en uso de funciones clave.
9. **Diseña acciones de retención segmentadas:**
   - **Para pagos:** outreach personalizado, ofertas de retención, resolución de problemas de facturación.
   - **Para free:** mejorar onboarding, tutoriales, activaciones en el primer día/semana, recordatorios de valor antes de cancelar.
10. **Establece metas concretas:** por ejemplo, bajar churn de pago de 9,1% a <6% en 3 meses.

## 4. La pregunta clave que deberías hacerte

> ¿El 31% total me está asustando porque realmente estoy perdiendo dinero, o porque estoy perdiendo muchos usuarios gratuitos que nunca iban a pagar?

Con los datos que tienes, **la respuesta es: principalmente estás perdiendo usuarios gratuitos**. El riesgo económico real está en los 22 de pago. Si logras entender y retener mejor a esos 22, el negocio se sana mucho más rápido que obsesionándote con los 178 free.

Si me dices tu **modelo de precios, ARPU, y cuántos usuarios nuevos entran al mes**, puedo ayudarte a priorizar entre “arreglar el embudo free” o “blindar a los pagos”.