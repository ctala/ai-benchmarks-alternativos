# GPT-6.1 Terra — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 10.705s | tokens_per_second: 79.4
- input_tokens: 165 | output_tokens: 850

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

Respira: el **31% describe las bajas sobre todos los usuarios**, incluidos los gratuitos. No equivale al churn de clientes de pago. Aun así, hay una señal que conviene investigar.

### Qué muestran los datos

Si las 62 bajas pertenecían a los 200 usuarios que estaban al inicio del mes, los cálculos son:

| Segmento | Bajas / usuarios al inicio | Tasa |
|---|---:|---:|
| Todos | 62 / 200 | 31% |
| Gratuito | 60 / 178 | 33,7% |
| Pago | 2 / 22 | **9,1%** |

El 9,1% está por encima del 5% que esperabas, **si ese 5% también era mensual y medía clientes de pago con la misma definición**. Pero la muestra es pequeña: con 22 clientes, cada baja representa aproximadamente 4,5 puntos porcentuales. Dos bajas merecen atención, aunque un solo mes no basta para establecer una tendencia.

Las 60 bajas gratuitas también importan, pero su impacto depende de si eran usuarios activos, qué potencial tenían de convertirse en clientes y qué significa exactamente “darse de baja”.

### Plan de acción

1. **Hoy: valida la medición.** Confirma que las bajas se cuentan únicamente entre quienes estaban en cada segmento al inicio del mes, y que “baja” significa lo mismo para gratuitos y de pago. Revisa también si la baja de pago se registra al cancelar o al terminar el servicio.

2. **En las próximas 48 horas: investiga las dos bajas de pago.** Contacta a esos clientes para entender el motivo: precio, falta de uso, problemas del producto o un fallo de cobro. Si fue un fallo de pago, intenta recuperarlo con un proceso adecuado de reintento y comunicación.

3. **Separa el panel.** Sigue por separado el churn de clientes de pago, las bajas de usuarios gratuitos y el churn de ingresos. Para este último necesitas los importes que pagaba cada cliente; dos bajas no dicen por sí solas cuánto ingreso perdiste.

4. **Revisa la tendencia.** Compara varios meses usando la misma definición y muestra siempre tanto la tasa como el número de clientes. Examina también una muestra de las bajas gratuitas y su actividad previa para ver si apuntan a un problema de activación.

**Prioridad:** no tomar decisiones de emergencia basándote en el 31%. Primero confirma el cálculo; después entiende por qué se fueron los dos clientes de pago.