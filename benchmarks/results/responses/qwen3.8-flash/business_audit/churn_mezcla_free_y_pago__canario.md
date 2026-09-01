# Qwen 3.8 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 36.264s | tokens_per_second: 87.1
- input_tokens: 227 | output_tokens: 3159

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

Respira. **El 31% no es el número que estás interpretando mal por pánico: lo estás midiendo con la población equivocada.**

Tu panel está mezclando **usuarios gratuitos** con **clientes pagantes**. Eso infla artificialmente el churn si el objetivo es retención de negocio.

## 1) El diagnóstico rápido

### Churn total reportado

- Bajas: 62
- Base inicio: 200
- Churn total: **62 / 200 = 31%**

Pero ese 31% incluye principalmente usuarios gratuitos, que no necesariamente representan ingreso recurrente.

### Churn de usuarios gratuitos

- Gratuitos inicio: 178
- Bajas gratuitas: 60
- Churn gratuito: **60 / 178 = 33.7%**

### Churn de usuarios de pago

- Pagos inicio: 22
- Bajas de pago: 2
- Churn de pago: **2 / 22 = 9.1%**

## 2) ¿Qué tan grave es?

**Depende de qué parte del negocio estás mirando.**

### Si tu negocio depende de usuarios pagantes:

El churn relevante es **9.1% mensual**, no 31%.

Eso es:

- **Mejor de lo que parecía.**
- **Aún preocupante si se sostiene.**
- **Muy sensible por muestra pequeña**: con 22 clientes, 1 cancelación más o menos cambia muchísimo el porcentaje.

Un churn mensual de 9.1% anualizado sería aproximadamente:

`1 - (1 - 0.091)^12 = 68.2%`

Es decir, si ese ritmo se mantuviera, perderías alrededor de dos tercios de tu base pagante al año. Eso sí es grave para un SaaS, pero no es el apocalipsis que sugiere el 31% porque:

- Solo fueron 2 clientes.
- No sabes todavía si fueron cancelaciones voluntarias, fallas de pago, usuarios no activados, churn de prueba, o ruido.
- Un mes con 2 bajas no es tendencia.

### Si tu negocio depende del plan gratuito como embudo:

El 33.7% de churn gratuito puede indicar problemas de activación, expectativa, onboarding o usuarios basura/spam/inactivos.

Pero incluso ahí, **no es necesariamente malo**. En muchos modelos freemium, una parte de los gratuitos se va rápido porque nunca fueron usuarios reales o nunca iban a pagar.

## 3) Lo que no debes hacer

No tomes decisiones grandes basadas en el 31% general.

Ese número está contaminado por la mezcla de poblaciones.

No deberías decir:

> “Estamos perdiendo el 31% de los clientes.”

Deberías decir:

> “Perdimos 2 de 22 clientes pagantes, un churn de pago del 9.1%. También perdimos 60 usuarios gratuitos, pero eso no es churn de ingreso recurrente.”

## 4) Plan inmediato: próximos 48 horas

### Paso 1: Separar el KPI

Crea estas métricas por separado:

| Métrica | Fórmula | Tu caso |
|---|---:|---:|
| Churn total | bajas / usuarios inicio | 31% |
| Churn gratuito | bajas free / free inicio | 33.7% |
| Churn de pago | bajas paid / paid inicio | 9.1% |
| Churn de MRR | MRR perdido / MRR inicio | Falta calcular |
| Churn voluntario | cancelaciones elegidas | Falta separar |
| Churn involuntario | fallas de pago/billing | Falta separar |

Tu panel debería mostrar primero **churn de pago**, no churn total.

### Paso 2: Revisar las 2 bajas de pago

Para cada usuario pagante cancelado, responde:

1. ¿Cuánto tiempo llevaba pagando?
2. ¿Qué plan tenía?
3. ¿Cuánto MRR representaba?
4. ¿Usaba el producto antes de cancelar?
5. ¿Canceló por:
   - falta de valor,
   - precio,
   - cambio de necesidad,
   - bug,
   - soporte,
   - fallo de pago,
   - prueba gratuita que no activó,
   - usuario equivocado?
6. ¿Se puede recuperar?
7. ¿Era un cliente sano o un cliente mal segmentado?

Con 2 bajas, el diagnóstico debe ser manual, no estadístico.

### Paso 3: Revisar si eran clientes reales

Pregúntate:

- ¿Alguno era un trial que pagó una vez y se fue?
- ¿Alguno era un usuario interno, de prueba, demo o spam?
- ¿Alguno se dio de baja por un problema de facturación?
- ¿Alguno nunca activó una función clave?

Si los 2 eran usuarios que nunca activaron valor, el problema puede ser **adquisición/onboarding**, no retención pura.

### Paso 4: Revisar los 60 gratuitos

No los trates como churn de negocio todavía. Clasifícalos:

| Tipo de gratuito | Acción |
|---|---|
| Nunca entró o nunca hizo nada | No es churn relevante; es ruido |
| Trial que no activó valor | Revisar onboarding |
| Usuario inactivo >30 días | Limpia métricas |
| Usuario que probó y se fue | Revisa expectativa/landing |
| Usuario que podría convertir | No es pérdida, es pipeline |
| Spam/bot/prueba | Excluye del KPI |

## 5) Plan de 2 semanas

### A. Arreglar el tablero

Tu panel principal debería mostrar:

1. **Churn de pago mensual**
2. **Churn de MRR mensual**
3. **Clientes pagantes activos**
4. **MRR activo**
5. **Nuevos pagos**
6. **Reactivaciones**
7. **Bajas voluntarias**
8. **Bajas involuntarias**
9. **Cohortes de pago**
10. **Free-to-paid conversion**

No mezcles free y paid en el mismo número.

### B. Definir “cliente pagante activo”

Ejemplo:

> Cliente pagante activo = cuenta con suscripción válida, plan de pago activo y no cancelada al cierre del mes.

Si tienes trials que pagan una sola vez, sepáralos.

### C. Medir MRR churn, no solo logo churn

El churn de cuentas puede mentir.

Si perdiste 2 clientes pequeños, es distinto a perder 1 cliente enterprise.

Calcula:

- MRR inicio.
- MRR perdido por cancelaciones.
- MRR perdido por downgrade.
- MRR recuperado.
- MRR neto.

Ejemplo:

Si esos 2 clientes representaban $100 MRR y tu base era $2,000, el churn de MRR sería 5%, no 9.1%.

### D. Revisar cohortes

No mires solo “este mes”. Mira:

- ¿Qué cohorte de pago canceló?
- ¿Cuántos meses llevaban pagando?
- ¿Qué plan tenían?
- ¿Qué función usaban o no usaban?
- ¿Qué canal de adquisición vino?
- ¿Qué onboarding completaron?

Con solo 2 bajas, revisa los últimos 3-6 meses para ver si hay patrón.

### E. Hacer entrevistas

Si puedes, contacta a los 2 usuarios de baja:

> “Vimos que cancelaste tu plan. No quiero venderte nada. ¿Puedes contarme qué te hizo dar el paso? ¿Qué esperabas y qué faltó?”

Eso vale más que cualquier dashboard.

## 6) Qué reportar a tu equipo o inversores

Puedes decir esto:

> “El panel muestra 31% de churn total, pero ese número incluye usuarios gratuitos. El churn relevante para negocio es de pago: 2 de 22 clientes, equivalente a 9.1% mensual. El 97% de las bajas fueron usuarios gratuitos. Por tanto, el problema no es una fuga masiva de clientes pagantes, sino dos cosas: 1) estamos midiendo churn con la población equivocada, y 2) necesitamos diagnosticar manualmente las 2 cancelaciones de pago y revisar la calidad del embudo gratuito.”

## 7) ¿Cuándo sí sería grave?

Sería grave si:

- Las 2 bajas de pago eran clientes sanos, activos y de alto valor.
- El MRR perdido es grande.
- Otras cuentas de pago están en riesgo.
- La baja se repite en cohortes similares.
- El churn de pago se mantiene >5% mensual durante varios meses.
- No puedes explicar por qué se fueron.
- El churn gratuito incluye muchos usuarios que sí pagaron o estaban cerca de pagar.

## 8) ¿Cuándo sería menos grave?

Sería menos grave si:

- Los 60 gratuitos eran inactivos, spam o trials mal calificados.
- Los 2 pagos eran usuarios pequeños o no activados.
- El churn de MRR es bajo.
- El resto de clientes pagos está activo.
- No hay señales de riesgo en otras cuentas.
- El problema es definición de métrica, no fuga real.

## 9) Prioridades correctas

### Prioridad 1: corregir la métrica

No uses 31% como churn de negocio.

### Prioridad 2: diagnosticar las 2 bajas de pago

Con 22 clientes, esto es manual, no automático.

### Prioridad 3: limpiar el segmento gratuito

Separa usuarios reales, inactivos, trials, spam y potenciales.

### Prioridad 4: empezar a medir retención por cohorte

Mira si los clientes pagos siguen vivos a 30, 60, 90 días.

### Prioridad 5: revisar activación

Si muchos se van antes de activar valor, el problema no es retención: es onboarding o expectativa.

## Conclusión

**No estás perdiendo el 31% de tus clientes pagantes.**

Estás perdiendo:

- **9.1% de clientes de pago** si medimos solo cuentas pagantes.
- **33.7% de usuarios gratuitos**, que no necesariamente afectan ingreso.
- **31% de usuarios totales**, pero esa mezcla no es útil para decidir.

La gravedad real depende de cuánto MRR representaban esas 2 bajas, cuánto llevaban activos, por qué se fueron y si hay más cuentas en riesgo.

Tu primer movimiento no es entrar en pánico. Es **separar free de paid, calcular churn de pago/MRR y hacer diagnóstico manual de las 2 cancelaciones**.