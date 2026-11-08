# Muse Glimmer 30B — business_audit/churn_mezcla_free_y_pago

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 16.5s | tokens_per_second: 117.1
- input_tokens: 182 | output_tokens: 1932

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

No es un 31% de churn de clientes de pago. Es un 31% de churn mezclando peras con manzanas, y eso es lo que te está generando pánico.

Tu panel está calculando: 62 bajas / 200 usuarios inicio de mes = 31%

El problema es la población. Estás midiendo churn de **todos** los usuarios, cuando el churn que importa para el negocio es el de los usuarios de pago.

### Qué está pasando realmente

Con tus datos exportados:

* **Churn de Pago:** 2 bajas / 22 usuarios de pago inicio mes = **9.1% mensual**
* **Churn de Gratuito:** 60 bajas / 178 usuarios gratuitos inicio mes = **33.7% mensual**
* **Churn Total reportado:** 62 / 200 = 31%

El 31% está dominado por el plan gratuito. 60 de las 62 bajas son free. Eso no es necesariamente grave, es esperable. La mayoría de usuarios free se registran, prueban y se van. Lo grave es el 9.1% de churn de pago si tu objetivo era 5%.

Un churn mensual del 9% en pago equivale a una retención anual del ~33%, es decir, pierdes 2 de cada 3 clientes pagando al año. Eso sí hay que arreglarlo.

### Plan inmediato

**HOY: Detén el pánico y corrige la métrica**
1. **Separa los KPIs.** Nunca más reportes churn agregado. Define 3 métricas oficiales:
   * Churn de Pago = Cancelaciones de pago / Pagos activos inicio de mes
   * Churn de MRR = MRR perdido por cancelaciones / MRR inicio de mes
   * Retención / Churn de Free = para entender el embudo, no para salud financiera
2. **Audita el panel.** Revisa cómo se calcula "baja". ¿Es cancelación voluntaria? ¿Inactividad? ¿Usuarios que nunca activaron? Un usuario free que se dio de baja a los 2 días no es churn, es falta de activación.

**ESTA SEMANA: Diagnóstico de las bajas de pago**
Tienes solo 2 bajas de pago este mes, es una muestra pequeña y manejable. Hazlo bien:
1. **Entrevista de salida a esas 2 personas.** Pregunta: ¿Qué te hizo quedarte? ¿Qué fue el punto de quiebre? ¿Qué alternativa usaste?
2. **Revisa el cohorte.** ¿Cuándo se dieron de alta esos 2 usuarios? ¿Llegaron a su primer valor? ¿Usaron la feature clave en los primeros 7 días?
3. **Mira el churn de free como embudo.** 33.7% de churn free puede ser bueno si convierte. Calcula: ¿De los 178 free inicio mes, cuántos pasaron a pago este mes? Si tu conversión es 0%, el problema es activación, no retención.

**ESTE MES: Actúa sobre los dos frentes**

*Para Pago:*
* Implementa un check-in a los 14 y 30 días post-pago para detectar señales de riesgo: baja frecuencia de uso, no uso de feature core, tickets de soporte sin resolver.
* Crea una campaña de winback específica para los 2 que se fueron y para los de riesgo.
* Revisa el precio/valor. Un churn de 9% suele ser problema de valor percibido o onboarding, no de producto.

*Para Free:*
* No intentes retener a todos los free. Define qué es un free "sano". Idealmente quieres churn alto de free inactivos y churn bajo de free activos.
* Mejora el onboarding para que lleguen al *aha moment* en < 48h. La mayoría de esas 60 bajas son usuarios que nunca se activaron.
* Pon un límite de tiempo o uso en free para forzar decisión.

En resumen: Tu negocio no está perdiendo el 31% de clientes. Está perdiendo el 9% de clientes de pago y el 34% de usuarios gratuitos. El 9% es preocupante y merece atención inmediata, el 31% es una métrica mal definida.

¿Quieres que te ayude a redefinir la fórmula exacta de churn para tu panel y qué segmentaciones necesitas para que no vuelva a pasar?