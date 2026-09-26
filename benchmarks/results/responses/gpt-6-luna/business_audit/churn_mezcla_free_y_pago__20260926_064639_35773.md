# GPT-6 Luna — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.09 | quality: 10.0
- latency_total: 12.695s | tokens_per_second: 112.1
- input_tokens: 165 | output_tokens: 1423

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

Respira: **el 31% no significa que hayas perdido el 31% de tus clientes de pago**. Es el cálculo correcto para la población mezclada del panel, pero puede no ser la métrica que te importa para el negocio.

Con los datos que compartiste:

| Segmento | Bajas | Usuarios al inicio | Churn |
|---|---:|---:|---:|
| Todos | 62 | 200 | **31%** |
| Gratuito | 60 | 178 | **33,7%** |
| De pago | 2 | 22 | **9,1%** |

Así que, si ese **5% era el churn mensual de pago**, el dato observado sí está por encima: **2 de 22**. Pero son solo dos bajas en una base pequeña, así que un mes aislado no basta para concluir que haya una tendencia o una crisis.

### Qué haría ahora

1. **Asegura que comparas la misma métrica.** Confirma que los 22 eran clientes de pago activos al inicio del mes y que las dos bajas son cancelaciones efectivas —no solo solicitudes—. Revisa también cómo trata el panel las pausas, impagos y cuentas duplicadas.
2. **Separa las métricas en el panel.** Muestra por separado churn de cuentas gratuitas, churn de clientes de pago y, si importa el ingreso, churn de ingresos recurrentes (MRR). El churn de clientes de pago suele calcularse sobre los clientes de pago activos al inicio del periodo.
3. **Mira el impacto de esas dos bajas.** ¿Cuánto MRR se perdió? ¿Fueron bajas voluntarias o impagos? ¿Tenían algo en común, como plan, antigüedad o motivo de cancelación?
4. **Investiga las dos bajas de pago esta semana.** Revisa tickets y motivos de cancelación y, si puedes, contacta a esos clientes. Es más útil que reaccionar a las 60 bajas gratuitas como si tuvieran el mismo impacto.
5. **Compara varios meses con la misma definición.** Con solo 22 clientes de pago, cada baja mueve mucho el porcentaje. Usa la tendencia de varios meses —y el MRR perdido— antes de cambiar precios o producto.

**En resumen:** el 31% es el churn de toda la población, dominada por usuarios gratuitos. Para el negocio de pago, el dato comparable es **9,1%**, preocupante frente a una meta del 5% pero todavía muy incierto por el tamaño de la base. Primero valida la definición y luego evalúa la tendencia y las causas.