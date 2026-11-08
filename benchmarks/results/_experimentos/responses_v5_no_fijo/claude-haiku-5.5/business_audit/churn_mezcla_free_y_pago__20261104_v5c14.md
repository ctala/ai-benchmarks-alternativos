# Claude Haiku 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 6.19 | quality: 6.0
- latency_total: 13.63s | tokens_per_second: 174.2
- input_tokens: 264 | output_tokens: 2375

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

**Tranquilo: el 31% es aritméticamente correcto.** 62 bajas / 200 usuarios = 31%. La plataforma no parece tener un error de cálculo. El problema es qué población está midiendo.

## Qué está pasando

Tus números desglosados:

| Segmento | Inicio | Bajas | Churn mensual |
|---|---|---|---|
| Gratuito | 178 | 60 | **33.7%** |
| De pago | 22 | 2 | **9.1%** |
| **Total** | 200 | 62 | **31%** |

El 31% está dominado por el plan gratuito, que es el 89% de la base. Es una mezcla: el churn de pago no es 5%, es 9%, y el gratuito pesa tanto que arrastra el total.

## De dónde podría venir el 5%

Hay que confirmar cuál era tu referencia, porque ninguna combinación directa de estos datos da 5%. Revisa si:
- Medías solo pago y con otra definición (por ejemplo, bajas de cuentas activas o solo cancelaciones voluntarias).
- El 5% viene de otro mes, de otro panel o de una métrica de revenue churn.
- Tu referencia era anual o de otra cohorte.

Si el 5% era tu objetivo para la base total, el problema es de expectativa, no de datos.

## Antes de alarmarte, verifica esto

1. **Definición de "baja".** ¿Incluye expiración de prueba, inactividad, cuentas borradas, usuarios que no se reactivan? En freemium, "baja" suele significar cosas muy distintas. Esto puede inflar el 33.7% gratuito.
2. **Cohorte de inicio.** ¿Las 62 bajas son todas de los 200 usuarios de inicio? Si incluyes usuarios que se registraron y se fueron en el mismo mes, el numerador y el denominador no cuadran.
3. **Duplicados y reactivaciones.** Un usuario que se da de baja y vuelve puede contar dos veces.
4. **Downgrades.** Un usuario de pago que pasa a gratuito, ¿cuenta como baja de pago, como baja total o como nada?
5. **Revenue churn.** Si tienes MRR, calcula el churn ponderado por ingreso. Con 2 bajas de pago, el impacto en ingresos puede ser muy distinto del 9% de usuarios.

## Advertencia estadística

Con 22 usuarios de pago y 2 bajas, el 9.1% tiene un intervalo de confianza enorme. Una baja más o menos cambia el resultado a 4.5% o 13.6%. No saques conclusiones sobre el segmento de pago con esta muestra.

## Plan

**Hoy (1-2 horas):**
- Confirma la definición de baja y la fuente del 5% anterior.
- Verifica que el numerador sea subconjunto del denominador (punto 2).
- Reporta el churn desglosado por plan, no solo el total.

**Esta semana:**
- Lee las 2 bajas de pago: ¿motivo, último uso, precio, cambio reciente de producto?
- Muestrea 20-30 bajas gratuitas y clasifícalas: prueba expirada, inactividad, cancelación explícita, error técnico.
- Calcula el churn de los últimos 3-6 meses para ver si este mes es anómalo o es tendencia.

**Decisión que sí importa:**
- Si tu negocio monetiza solo el plan de pago, la métrica clave es el churn de pago y el de revenue, no el total. Ahí el 9% merece atención pero no es catástrofe; depende de tu benchmark.
- Si el plan gratuito es un embudo de conversión, el 33.7% importa por lo que implica para la activación y la conversión a pago, no por sí mismo. Mide cuántos gratuitos llegan a pago y en qué punto abandonan.

**Qué no hacer:** cambiar el reporte o la definición a mitad de mes para "arreglar" el número. Documenta la definición, comunícala a quien recibe el reporte y úsala de forma consistente.

Si me pasas la definición exacta que usa el panel y tu fuente del 5%, puedo ayudarte a reconciliar las cifras.