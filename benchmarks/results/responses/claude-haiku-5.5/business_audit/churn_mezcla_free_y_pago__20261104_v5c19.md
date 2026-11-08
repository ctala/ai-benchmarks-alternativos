# Claude Haiku 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.59 | quality: 8.0
- latency_total: 12.665s | tokens_per_second: 188.1
- input_tokens: 264 | output_tokens: 2382

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

Respira. Con estos números, el 31% no es necesariamente un error ni una catástrofe. Lo más probable es que estén mezclando dos poblaciones.

## 1. Verifica la aritmética y la población

- **Churn blended (lo que reporta el panel):** 62 / 200 = **31%**. Está bien calculado.
- **Churn de pago:** 2 / 22 = **9,1%**.
- **Churn gratuito:** 60 / 178 = **33,7%**.

El 31% es casi todo churn gratuito. Los usuarios de pago, que son los que más te importan económicamente, no explican el número.

**El 5% que esperabas no coincide con ninguno de estos cortes.** Antes de seguir, averigua de dónde salió: ¿era un churn histórico de todos los usuarios, de pago solamente, o de MRR (ingresos)? Si era churn de pago de meses anteriores, 9% hoy es una señal a vigilar, pero con 22 usuarios de pago, una sola baja mueve el porcentaje casi 5 puntos. Con esa muestra no puedes concluir mucho.

## 2. Averigua si el 31% es "real" o un artefacto de definición

Revisa estas causas comunes:
- ¿El plan gratuito cuenta como "cliente" en esa métrica? Si incluye cuentas que nunca activaron, el denominador está inflado.
- ¿Las 60 bajas gratuitas son cuentas inactivas que se purgaron o se cerraron en bloque?
- ¿Hubo expiraciones de prueba o trials que se contaron como bajas?
- ¿Hubo migraciones, cambios de plan, duplicados o fusiones de cuentas que aparecen como bajas?
- ¿El panel cambió su lógica de cálculo este mes?

## 3. Compara contra tu baseline correcto

La pregunta útil no es "¿31% es mucho?" sino "¿33,7% de churn gratuito es normal para nosotros?". Pide:
- Churn gratuito mensual de los últimos 6 a 12 meses.
- Churn de pago y de MRR en el mismo periodo.
- Si el plan gratuito es un embudo de adquisición, un churn alto puede ser esperado y no es un problema de retención.

## 4. Decide la gravedad según el resultado

- **Si el churn gratuito es normal y el de pago también:** no hay crisis. Corrige la métrica y reporta por segmento.
- **Si el churn gratuito subió vs. histórico:** investiga activación, onboarding y si hubo un cambio de producto o precio este mes.
- **Si el churn de pago subió de forma sostenida:** eso sí es prioritario, aunque la muestra sea pequeña. Entrevista a las 2 bajas y a usuarios de pago en riesgo (inactividad, uso bajo).
- **Si el 5% venía de una fuente errónea:** el problema es de reporte, no de producto.

## 5. Plan para las próximas 48 horas

1. **Hoy:** confirma la definición de churn que usa el panel y de dónde salió el 5%.
2. **Hoy:** separa el reporte en tres líneas: churn de pago (logos), churn de pago (MRR) y churn gratuito.
3. **Mañana:** saca el histórico de 6 a 12 meses de cada una.
4. **Mañana:** revisa las 60 bajas gratuitas: fecha de último uso, fecha de creación, si fueron purgas o cancelaciones reales.
5. **Esta semana:** entrevista a las 2 bajas de pago y, si puedes, a 5 a 10 usuarios de pago con uso bajo.
6. **Antes de comunicar a dirección:** presenta el número con contexto: "31% blended; 9% de pago (n=2 bajas sobre 22 cuentas, muestra pequeña); churn gratuito de 34%, comparado con X% histórico".

## Para comunicar sin alarmar ni minimizar

Di algo como: *"El 31% es correcto aritméticamente, pero está dominado por el plan gratuito. El churn de pago fue de 9% sobre una base de 22 cuentas, así que la muestra es pequeña. Estamos validando la definición y comparando con el histórico antes de sacar conclusiones."*

Si me compartes el histórico de churn por segmento y la definición que usa el panel, puedo ayudarte a ver si el cambio es real.