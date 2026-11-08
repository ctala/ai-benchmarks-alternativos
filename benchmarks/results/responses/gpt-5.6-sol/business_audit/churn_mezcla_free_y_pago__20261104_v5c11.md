# GPT-5.6 Sol — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 10.693s | tokens_per_second: 113.8
- input_tokens: 165 | output_tokens: 1217

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

Respira: el **31% es correcto matemáticamente**, pero mezcla dos poblaciones muy distintas y probablemente no es la métrica con la que estabas comparando ese 5%.

### Qué está midiendo realmente

| Segmento | Inicio de mes | Bajas | Churn mensual |
|---|---:|---:|---:|
| Gratuito | 178 | 60 | **33,7%** |
| Pago | 22 | 2 | **9,1%** |
| Total | 200 | 62 | **31,0%** |

El 31% está dominado por el plan gratuito: 60 de las 62 bajas fueron gratuitas.

### ¿Qué tan grave es?

- **No significa que perdiste 31% de tus clientes de pago ni 31% de tus ingresos.**
- Tu churn de usuarios de pago fue **2/22 = 9,1% mensual**. Si tu referencia era 5% para clientes de pago, sí estás por encima, pero la muestra es muy pequeña: cada cliente representa **4,5 puntos porcentuales**. Con una baja habría sido 4,5%; con dos, 9,1%.
- El **33,7% gratuito** puede ser preocupante o normal según el producto. Importa saber si eran usuarios activos, pruebas temporales, cuentas antiguas/inactivas o personas recién registradas sin activarse.
- Aún no se puede calcular el **churn de ingresos**: perder dos cuentas pequeñas no equivale a perder dos cuentas grandes.

## Plan inmediato

### Hoy: validar la definición

Confirma en el panel:

1. ¿“Baja” significa cancelación, eliminación de cuenta o expiración?
2. ¿El denominador incluye solo usuarios existentes al inicio del mes?
3. ¿Los 200 estaban activos o incluye cuentas gratuitas inactivas?
4. ¿Los usuarios que cambiaron de plan cuentan como bajas?
5. ¿Hay reactivaciones, altas nuevas o impagos mezclados?
6. ¿El 5% que recordabas era churn de pago, churn de ingresos o una media de varios meses?

No compares el 31% total con un objetivo de 5% si ese objetivo estaba definido para clientes de pago.

### En las próximas 48 horas: investigar las dos bajas de pago

Con solo dos casos, revísalos individualmente:

- plan e ingresos mensuales;
- antigüedad;
- uso reciente y funciones utilizadas;
- incidencias o tickets;
- impago frente a cancelación voluntaria;
- motivo declarado;
- posibilidad de entrevista o encuesta breve.

Calcula además:

- **Churn de ingresos bruto** = ingresos mensuales perdidos / ingresos recurrentes al inicio;
- **churn involuntario** por fallos de cobro;
- churn por plan, antigüedad y cohorte.

### Esta semana: entender el churn gratuito

Segmenta esas 60 bajas por:

- usuarios activados frente a no activados;
- antigüedad: 0–7, 8–30, 31–90 y más de 90 días;
- actividad en los últimos 30 días;
- canal de adquisición;
- motivo de baja;
- conversión previa o intención de compra.

Si la mayoría nunca llegó al “momento de valor”, el problema es de **onboarding/activación**, no necesariamente de retención madura.

### Desde el próximo mes: separar el tablero

Reportaría al menos cuatro métricas:

1. churn de usuarios gratuitos;
2. churn de clientes de pago;
3. churn bruto de ingresos;
4. retención por cohortes y antigüedad.

Usa también una media móvil de 3 meses para pago, porque con solo 22 clientes la tasa mensual será muy volátil.

### Prioridad

No tomes medidas drásticas basándote en el 31%. La señal que requiere atención es **2 bajas entre 22 clientes de pago**, pero primero determina su valor y motivo. En paralelo, estudia si el 33,7% gratuito reduce activación y futuras conversiones. El objetivo inmediato es aumentar la base pagada y evitar que uno o dos casos individuales distorsionen toda la lectura mensual.