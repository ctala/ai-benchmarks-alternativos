# Muse Glimmer 30B — business_audit/churn_mezcla_free_y_pago

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 29.152s | tokens_per_second: 62.3
- input_tokens: 182 | output_tokens: 1815

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

No es un 31% de churn de clientes de pago. Es un 31% de churn de *usuarios totales* y eso es una métrica distinta. Tu pánico es comprensible, pero la alarma real es menor y más específica.

### Qué está pasando realmente

Tu panel está calculando churn como: `Bajas del mes / Usuarios a inicio de mes`

62 / 200 = 31%

El problema es la población. No puedes mezclar free y pago.

Con tus datos exportados:

* **Churn total reportado:** 62 / 200 = 31%
* **Churn plan gratuito:** 60 / 178 = 33.7%
* **Churn plan de pago:** 2 / 22 = 9.1%

Si esperabas un 5%, tu expectativa era de churn de pago. El 9.1% mensual de pago sí es grave, porque equivale a ~68% anualizado. El churn de free no es comparable.

El churn de free suele ser alto y hasta deseable: la mayoría prueba y se va. Lo que importa es que los free se conviertan y que los de pago se queden.

### Plan de acción inmediato

**Hoy, 24h: Detener el fuego y validar**

1. **Congela la narrativa.** No reportes el 31% como churn. Comunica internamente: "El panel está midiendo churn total. El churn de pago es 9.1%".
2. **Valida los 2 pagos que se fueron.** Revisa fecha de alta, plan, MRR, motivo de baja en el sistema, tickets de soporte y uso en los últimos 30 días. Haz entrevistas de salida rápidas: ¿Precio? ¿Falta de valor? ¿Bug? ¿No renovación?
3. **Valida los 60 free.** ¿Son bajas voluntarias o purgas por inactividad? Muchas plataformas eliminan cuentas inactivas >90 días. Eso no es churn, es limpieza.

**Esta semana: Arreglar la métrica**

1. **Define churn correctamente por segmento:**
   * *Churn de pago = Clientes de pago que cancelan en el mes / Clientes de pago al inicio del mes*
   * *Churn de ingresos = MRR perdido por cancelaciones / MRR al inicio del mes*
   * *Churn de free = opcional, para tracking de activación, no para salud del negocio*
2. **Corrige el panel.** El churn debe calcularse solo sobre la base que genera ingresos. Si sumas usuarios nuevos en el mes, usa la fórmula más precisa: `Churn = Cancelaciones / Usuarios promedio del mes`.
3. **Crea un dashboard de retención por cohorte.** No te sirve un número global. Necesitas ver: de los que se registraron en Enero, ¿qué % sigue en Marzo? Eso te dirá si el problema es de onboarding o de producto maduro.

**Próximos 30 días: Reducir el churn de pago del 9% al 5%**

1. **Análisis de causa raíz de los 2 pagos.** Con tan pocos casos, puedes hacer un análisis 100%. Busca patrones: mismo plan, misma funcionalidad no usada, mismo momento de cancelación tras el primer mes.
2. **Implementa un proceso de rescate.** Antes de que se vayan: alerta de uso bajo, email de win-back a los 14 días de inactividad, llamada de CSM para cuentas >X MRR.
3. **Mejora el momento de valor.** El 9% sugiere que la gente no alcanza el "Aha moment". Revisa métricas de activación en los primeros 7-14 días y fricción en onboarding.
4. **Encuesta de salida obligatoria.** 2 preguntas: "¿Qué te hizo quedarte?" y "¿Qué te hizo irte?". Con 2 casos ya tienes señal.

### Resumen

No es un desastre del 31%. Es un mal cálculo de métrica + un churn de pago real del 9.1% que sí necesita atención urgente.

Tu prioridad no es el free. Es entender por qué 1 de cada 11 clientes de pago se va cada mes y cerrar esa fuga.

¿Quieres que te ayude a armar el query exacto para calcular churn de pago y revenue churn correctamente en tu base de datos?