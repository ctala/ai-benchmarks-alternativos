# GPT-5.6 Luna — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 6.62 | quality: 7.2
- latency_total: 11.872s | tokens_per_second: 136.5
- input_tokens: 165 | output_tokens: 1621

## Respuesta completa

Primero: **el 31% no parece ser el churn de clientes de pago**. Es el churn de toda la base, porque:

\[
62 / 200 = 31\%
\]

La mezcla de planes cambia mucho la lectura:

| Segmento | Base inicial | Bajas | Churn |
|---|---:|---:|---:|
| Gratis | 178 | 60 | **33,7%** |
| Pago | 22 | 2 | **9,1%** |
| Total | 200 | 62 | **31,0%** |

## ¿Qué tan grave es?

### Para el negocio de pago: preocupante, pero no necesariamente una crisis

Tu churn de pago observado es **9,1% mensual**, no 31%. Si tu referencia esperada era 5%, estás por encima, pero la muestra es muy pequeña: **2 bajas sobre solo 22 clientes**. Una sola baja adicional o menos cambia mucho el porcentaje.

Por ejemplo:

- 1 baja de pago: 4,5%
- 2 bajas: 9,1%
- 3 bajas: 13,6%

Por eso no concluiría todavía que existe un deterioro estructural. Sí lo trataría como una señal que requiere investigación inmediata.

### Para la base total: el 31% está dominado por usuarios gratuitos

Los usuarios gratuitos representan el **89% de la base inicial** y generan **97% de las bajas** —60 de 62—. Por tanto, el número agregado está describiendo principalmente el comportamiento del plan gratuito, no la retención de ingresos.

No mezcles ambos segmentos en una única métrica principal si el objetivo es evaluar la salud comercial.

## Qué verificar antes de interpretar

Confirma estas definiciones:

1. **Denominador:** ¿los 200 eran usuarios activos al inicio de mes o incluye usuarios ya inactivos?
2. **Baja:** ¿es cancelación explícita, eliminación de cuenta, falta de uso o expiración de una prueba?
3. **Plan al momento de la baja:** ¿algún usuario gratuito se convirtió en pago o se dio de baja antes de ser clasificado?
4. **Periodo:** ¿son bajas ocurridas durante el mes o usuarios que terminaron el mes sin actividad?
5. **Duplicados y movimientos:** ¿hay cambios de plan, pausas, reactivaciones o cuentas duplicadas?
6. **Comparabilidad con el 5%:** ¿ese 5% correspondía a clientes de pago, a una cohorte, a churn de ingresos o a otra definición?

También separaría:

- **Churn de logos de pago:** 2 / 22 = 9,1%
- **Churn de ingresos:** MRR perdido / MRR inicial
- **Churn de usuarios gratuitos:** 60 / 178 = 33,7%
- **Churn por cohorte:** usuarios adquiridos en cada mes y su retención posterior

El churn de logos de pago puede ser 9,1% aunque el impacto económico sea pequeño o grande, dependiendo de qué clientes se fueron.

## Plan de acción

### Hoy: validar y descomponer

1. Congela el cálculo actual como **“churn total de usuarios”**, no como churn comercial.
2. Reconstruye una tabla con:
   - usuario;
   - plan al inicio;
   - plan al darse de baja;
   - fecha de alta;
   - fecha de baja;
   - motivo de baja;
   - MRR, si aplica;
   - última actividad;
   - canal de adquisición.
3. Calcula para los clientes de pago:
   - churn de logos;
   - churn de ingresos;
   - bajas voluntarias vs. involuntarias;
   - churn por antigüedad;
   - churn por plan, país, canal y uso del producto.
4. Revisa individualmente los **2 clientes de pago perdidos**. Con una base de 22, cada caso importa mucho.

### En los próximos 7 días: encontrar la causa

Para los 2 clientes de pago:

- Contacta con ellos con una encuesta breve o entrevista.
- Identifica si fue precio, falta de valor, problemas técnicos, onboarding, falta de uso o cambio de necesidad.
- Comprueba si hubo fallos de cobro o expiración de tarjeta; eso sería churn involuntario y requiere un tratamiento distinto.
- Revisa su uso durante los 30 días anteriores a la baja.

Para los 60 gratuitos:

- No asumas que son “clientes perdidos”. Puede que sean cuentas de prueba, usuarios de baja intención o usuarios que simplemente dejaron de usar el producto.
- Calcula su activación y retención por cohorte.
- Compara bajas de usuarios gratuitos recién registrados contra usuarios que ya habían alcanzado una acción de valor.

### En los próximos 30 días: corregir el sistema de medición y la retención

Define un cuadro de mando separado:

1. **Retención de pago**
   - churn mensual de clientes;
   - churn de ingresos;
   - retención neta y bruta de ingresos;
   - churn voluntario e involuntario.

2. **Embudo gratuito**
   - activación;
   - usuarios activos semanales/mensuales;
   - conversión a pago;
   - retención por cohorte;
   - tiempo hasta la primera acción de valor.

3. **Alertas**
   - alerta cuando haya más de 1 baja de pago en el mes;
   - alerta por caída de uso antes de la cancelación;
   - alerta por errores de cobro;
   - seguimiento de cuentas de alto valor con baja actividad.

## Mi lectura ejecutiva

No reportaría internamente “tenemos 31% de churn” sin contexto. Diría:

> “El churn agregado es 31%, pero está fuertemente influido por el plan gratuito: 60 de las 62 bajas provienen de ese segmento. El churn de pago fue 9,1%, equivalente a 2 de 22 clientes, por encima de la referencia del 5%, aunque con una muestra pequeña. Estamos validando definición, causas y efecto sobre ingresos.”

La prioridad no es intentar reducir inmediatamente el 31% agregado. Es:

1. **validar que la métrica esté bien definida;**
2. **entender las 2 bajas de pago;**
3. **medir el impacto en MRR;**
4. **analizar si las bajas gratuitas son realmente un problema o un comportamiento esperado del embudo.**

No estás ante evidencia suficiente para entrar en pánico, pero sí ante una señal clara de que el panel está mezclando poblaciones que deben analizarse por separado.