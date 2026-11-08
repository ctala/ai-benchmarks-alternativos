# GPT-6.1 Sol — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 16.056s | tokens_per_second: 57.1
- input_tokens: 165 | output_tokens: 916

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

**No tomes decisiones drásticas por ese 31% todavía.** El cálculo es correcto, pero mide las bajas de **todos los usuarios**, no solo las de clientes de pago. Mezclar ambas poblaciones oculta dónde está el problema.

## Qué está pasando realmente

Suponiendo que las bajas corresponden a los usuarios que estaban al inicio del mes:

| Población | Usuarios al inicio | Bajas | Churn mensual |
|---|---:|---:|---:|
| Total | 200 | 62 | **31,0%** |
| Plan gratuito | 178 | 60 | **33,7%** |
| Plan de pago | 22 | 2 | **9,1%** |

**El 96,8% de las bajas fueron de usuarios gratuitos.** Por tanto, el 31% no significa que hayas perdido al 31% de tus clientes de pago ni al 31% de tus ingresos.

Pero tampoco significa que todo esté bien: **si tu referencia del 5% era churn mensual de clientes de pago, este mes fue del 9,1%, por encima de lo esperado.** Con solo 22 clientes, cada baja mueve la tasa unos 4,5 puntos porcentuales; dos bajas merecen investigación, pero un único mes no demuestra una crisis sostenida.

## ¿Qué tan grave es?

- **Clientes de pago: señal de alerta, no prueba suficiente de una crisis.** Importan los motivos de esas dos bajas, su valor económico y si el patrón se repite.
- **Usuarios gratuitos: pérdida considerable que hay que contextualizar.** Puede indicar mala activación, captación poco adecuada o usuarios de uso puntual. Su gravedad depende de si afecta a la conversión a pago y al valor del producto.
- **Ingresos: aún no se puede determinar el impacto.** Perder dos cuentas pequeñas no equivale a perder las dos mayores.

## Plan de acción

### Hoy: valida la métrica y dimensiona el daño
1. **Confirma qué cuenta como “baja”:** eliminación de cuenta, cancelación, paso de pago a gratuito o inactividad. No son equivalentes.
2. **Comprueba que numerador y denominador corresponden a la misma población.** Si las 62 bajas incluyen usuarios que se registraron este mismo mes, dividirlas entre los 200 iniciales no mide correctamente el churn de la base inicial.
3. **Aclara qué representaba tu 5%:** ¿clientes de pago, usuarios totales o ingresos? ¿Mensual o anual? Solo compáralo con una métrica equivalente.
4. **Calcula el impacto económico:** MRR perdido por cancelaciones respecto al MRR inicial; registra también contracciones y expansiones por separado.

### Próximas 48 horas: investiga las dos bajas de pago
- Revisa antigüedad, plan, uso reciente, incidencias y fallos de cobro.
- Contacta a ambos clientes con una pregunta breve: **“¿Qué te llevó a cancelar y qué habría tenido que ser distinto para que continuaras?”**
- Distingue bajas voluntarias de pagos fallidos: requieren soluciones diferentes.
- Evita descuentos generales antes de conocer el motivo.

### Esta semana: entiende la fuga del plan gratuito
- Separa las bajas por antigüedad, canal de adquisición y nivel de activación.
- Comprueba si se concentran en personas que nunca llegaron al primer momento de valor.
- Revisa si hubo cambios de producto, errores o campañas que atrajeron usuarios poco adecuados.
- Prioriza una mejora concreta según lo encontrado, no una campaña indiscriminada de reactivación.

### Próximos meses: corrige el seguimiento
Crea un panel con:
- Churn de clientes de pago, **porcentaje y número absoluto**.
- Churn de ingresos.
- Retención de usuarios gratuitos y de pago por cohorte.
- Conversión de gratuito a pago.
- Tendencia de varios meses, con definiciones consistentes.

**Mi recomendación:** investiga primero las dos bajas de pago y su impacto en ingresos; después, la activación de los gratuitos. El 31% agregado es alarmante a primera vista, pero no basta para diagnosticar la salud del negocio. Tu señal comercial inmediata es **2 de 22 clientes de pago perdidos**, y esa es la que debes explicar antes de actuar a gran escala.