# Kimi K3.1 Pro — business_audit/churn_mezcla_free_y_pago

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 7.79 | quality: 10.0
- latency_total: 223.468s | tokens_per_second: 24.8
- input_tokens: 286 | output_tokens: 5533

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

Respira: **el 31% está bien calculado como tasa agregada, pero no significa que hayas perdido el 31% de tus clientes de pago ni de tus ingresos.** El indicador mezcla dos poblaciones con comportamientos muy distintos.

## Qué está pasando realmente

Suponiendo que las bajas pertenecen a los usuarios que ya estaban al inicio del mes:

| Población | Cálculo | Churn mensual de cuentas |
|---|---:|---:|
| Total, gratuito + pago | 62 / 200 | **31,0%** |
| Plan gratuito | 60 / 178 | **33,7%** |
| Plan de pago | 2 / 22 | **9,1%** |

Dos lecturas importantes:

- **Las bajas gratuitas explican 30 de los 31 puntos porcentuales** del churn total: `60/200 = 30%`. Las bajas de pago aportan 1 punto.
- El churn de pago es **9,1%, no 31%**, pero tampoco está en 5%. Aun así, la base es pequeña: con 22 clientes, una baja equivale a 4,5 puntos; dos bajas ya elevan la tasa a 9,1%. No declares una tendencia con un solo mes.

**Advertencia de medición:** si las 62 bajas incluyen personas que se registraron y se dieron de baja dentro del mismo mes, el denominador de 200 no es comparable. En ese caso, hay que recalcular las tasas sobre la cohorte inicial y reportar esas altas/bajas por separado.

## ¿Qué tan grave es?

- **En ingresos: todavía no se puede saber.** Necesitas el MRR de las dos cuentas de pago perdidas. `2/22 = 9,1%` no implica necesariamente perder 9,1% del MRR, porque las cuentas pueden tener valores distintos.
- **En clientes de pago: es una señal de alerta.** Si un churn de pago de 9,1% se mantuviera todos los meses, sería grave. Pero dos bajas en una base de 22 no bastan para concluir que ese sea tu nuevo nivel habitual.
- **En gratuito: hay muchas bajas, pero su gravedad depende de quiénes eran.** No es lo mismo depurar 60 cuentas inactivas que perder 60 usuarios recién activados. El segundo caso indicaría un problema serio de activación o valor percibido.
- **Tu antiguo 5% no es comparable hasta verificar su definición.** Podía referirse a pago, a ingresos, a otra cohorte, a churn neto o simplemente a otro periodo.

## Plan de acción

### Hoy: validar y contener el riesgo de pago

1. **Reconstruye la cohorte correctamente**
   - Usuarios únicos presentes al inicio del mes, separados por plan.
   - Bajas provenientes exclusivamente de esa cohorte.
   - Altas que cancelaron dentro del mes, reportadas aparte.
   - Comprueba duplicados, zonas horarias, cuentas de prueba, bajas por depuración y cambios de plan.
   - Distingue cancelación de cuenta, downgrade a gratuito, impago y baja voluntaria.

2. **Calcula el impacto económico**
   - Identifica las dos cuentas de pago, su MRR, antigüedad y motivo de baja.
   - Calcula:  
     **Churn bruto de MRR = MRR perdido por esas bajas / MRR de pago al inicio del mes.**
   - Calcula también el churn neto de MRR si hubo downgrades, expansiones o reactivaciones.

3. **Actúa sobre esas dos cuentas**
   - Si fueron impagos: revisa reintentos, avisos y actualización de método de pago.
   - Si fueron voluntarias: revisa uso previo, soporte y motivo; haz una entrevista breve cuando sea posible.
   - Si eran cuentas de alto valor, prioriza una recuperación personalizada. No lances descuentos masivos sin conocer la causa.

### En las próximas 48–72 horas: diagnosticar el gratuito

4. Segmenta las 60 bajas por:
   - Actividad durante los 30 días anteriores.
   - Antigüedad y cohorte de registro.
   - Activación: si completaron la acción principal de tu producto.
   - Canal de adquisición.
   - Posibles purgas, spam, cambios de producto o incidencias técnicas.

5. Compara con los últimos 6–12 meses usando **exactamente la misma definición**. Para pago, muestra tanto el número de bajas como la tasa y acompáñalo de una vista trimestral, porque los porcentajes mensuales serán muy sensibles a una sola cuenta.

### Esta semana: corregir el panel

6. Sustituye el único “churn” por indicadores etiquetados:
   - Churn de cuentas gratuitas.
   - Churn de clientes de pago.
   - Churn bruto y neto de MRR.
   - Activación y conversión de gratuito a pago.
   - Numerador, denominador y población incluida en cada tarjeta.

**Mi lectura:** esto requiere investigación urgente, pero el 31% no demuestra un colapso del negocio. Tu prioridad inmediata es conocer **el MRR y la causa de las dos bajas de pago**; después, determinar si las 60 bajas gratuitas eran cuentas activas o simplemente inactivas. No haría todavía cambios masivos de producto ni campañas generales de retención.