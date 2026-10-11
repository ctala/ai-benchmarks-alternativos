# GPT-6 Luna Pro — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 22.078s | tokens_per_second: 142.9
- input_tokens: 4603 | output_tokens: 3155

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

Respira: **el 31% no significa que hayas perdido al 31% de tus clientes de pago**. El panel está mezclando usuarios gratuitos y de pago.

Con los datos que compartes:

| Segmento | Bajas / usuarios al inicio | Churn |
|---|---:|---:|
| Total | 62 / 200 | **31%** |
| Gratuito | 60 / 178 | **33,7%** |
| De pago | 2 / 22 | **9,1%** |

Así que la cifra relevante para la retención de pago es, provisionalmente, **9,1%**, no 31%. No es 5%: dos bajas entre 22 cuentas equivalen a 9,1%. Como la base es pequeña, **cada baja representa unos 4,5 puntos porcentuales**; dos casos todavía no bastan para concluir que haya una tendencia estable.

**¿Qué tan grave es?** El 31% puede ser muy poco útil para evaluar el negocio si incluye usuarios gratuitos. El 9,1% de bajas de pago sí merece atención, sobre todo si se repite varios meses, pero su impacto económico no se puede juzgar sin saber cuánto MRR se perdió y sin compararlo con meses anteriores.

### Plan

1. **Comprueba qué cuenta como “baja”.** Verifica que las 62 personas estaban activas al inicio del mes y que la baja fue efectiva este mes; distingue cancelaciones, vencimientos, impagos, cambios de plan y duplicados.
2. **Define y separa las métricas.** Usa como indicador principal el churn de clientes de pago: cuentas de pago que dejaron de pagar durante el mes ÷ cuentas de pago al inicio. Mantén el churn gratuito aparte. Calcula también el **MRR perdido** por esas bajas: dos cuentas pueden tener impactos económicos muy distintos.
3. **Investiga las dos bajas de pago.** Revisa motivo, antigüedad, uso reciente, incidencias de soporte y posibles fallos de pago. Si es apropiado, contacta a esas cuentas para entender qué ocurrió.
4. **Compara con meses anteriores**, usando la misma definición y el mismo segmento. Mira también cuántas cuentas de pago nuevas entraron: no confundas bajas brutas con crecimiento neto.
5. **Ajusta el panel** para que muestre por separado usuarios gratuitos, cuentas de pago y churn de ingresos. No compares el 31% con tu antiguo 5% hasta confirmar que ambos miden la misma población y el mismo tipo de baja.