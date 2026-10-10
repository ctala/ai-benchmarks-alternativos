# Claude Haiku 5.5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 7.6 | quality: 8.0
- latency_total: 12.712s | tokens_per_second: 174.2
- input_tokens: 264 | output_tokens: 2215

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

Antes de alarmarte, conviene separar qué está midiendo realmente el 31%. Con tus datos, el número es aritméticamente correcto, pero probablemente no responde a la pregunta que te importa.

## Lo que dicen tus datos

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| Pago | 22 | 2 | **9,1%** |
| Total | 200 | 62 | **31%** |

El 31% es un promedio ponderado dominado por el plan gratuito, que es el 89% de tu base. Por eso el total se parece tanto al churn gratuito.

## Por qué puede no ser "el churn real"

1. **Estás mezclando poblaciones.** Si tu 5% se refiere a clientes de pago, el dato comparable es **9,1%**, no 31%. Eso sigue siendo alto, pero es otro problema.
2. **Tu 5% podría venir de otra definición.** Churn de ingresos (MRR), churn de un periodo distinto, o un cálculo sobre una base diferente. No cuadra con ningún cálculo directo de tus datos: 5% de 200 serían 10 bajas, y 5% de 22 serían 1.
3. **El numerador puede incluir usuarios que no estaban en la base.** Si algunas de las 62 bajas se registraron y cancelaron dentro del mismo mes, no deberían contar contra los 200 de inicio. Hay que verificarlo.
4. **"Baja" en gratuito puede significar otra cosa.** Eliminación de cuenta, inactividad prolongada o expiración de un trial. No es necesariamente pérdida de ingresos.
5. **Muestra pequeña en pago.** Con 22 usuarios y 2 bajas, un dato puede moverse muchísimo con 1 usuario más o menos. No conviene sacar conclusiones fuertes del 9,1%.

## Qué tan grave es

Depende de qué te importa:
- Si el negocio depende de ingresos, lo relevante es el churn de pago y de MRR. Ahí el riesgo es moderado y hay que confirmarlo con más meses de datos.
- Si mides engagement o base total, el churn gratuito de ~34% puede ser real y preocupante, pero también puede reflejar limpieza de cuentas inactivas.

No tengo suficiente información para decir que la situación es grave ni que es normal.

## Plan

**Hoy (verificación, sin alarmar a nadie):**
1. Confirma la fórmula exacta del panel: numerador, denominador, fechas de corte y si incluye altas del mes.
2. Reconstruye la cohorte: toma solo los usuarios activos el día 1 del mes y cuenta cuántos se fueron. Compara con el 31%.
3. Pregunta de dónde salió el 5%: qué métrica, qué periodo, qué segmento. Probablemente la respuesta explica la discrepancia.
4. Separa en el reporte: churn de pago, churn gratuito y churn de ingresos, siempre con su base y número absoluto.

**Esta semana:**
5. Revisa qué significa "baja" en el plan gratuito y si hay cuentas inactivas o eliminaciones masivas.
6. Si el churn de pago se confirma en ~9%, mira las 2 bajas una a una: motivo, uso previo, momento de cancelación. Con 2 casos no hay patrón, pero sí puedes detectar errores de facturación o fallos de producto.
7. Si el churn gratuito es real, segmenta por antigüedad, origen de adquisición y última actividad. Muchas veces el churn gratuito se concentra en usuarios que nunca activaron.

**Antes de comunicar:**
8. No mandes el 31% a stakeholders hasta tener la definición validada. Si ya lo compartiste, manda una nota corta: "Estamos validando la métrica; separamos pago y gratuito; te confirmo en X días."

Si me compartes la fórmula que usa el panel y de dónde sale el 5%, puedo ayudarte a identificar exactamente qué está pasando.