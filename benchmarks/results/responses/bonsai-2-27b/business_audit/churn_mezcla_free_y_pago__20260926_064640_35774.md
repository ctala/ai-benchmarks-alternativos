# Bonsai 2 27B — business_audit/churn_mezcla_free_y_pago

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 127.268s | tokens_per_second: 43.8
- input_tokens: 227 | output_tokens: 5569

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



No te quedes en el 31%. Ese número está midiendo **toda la base de usuarios**, no necesariamente a los usuarios que te importan económicamente.

## 1) Lo que está pasando

El churn reportado es:

\[
62 / 200 = 31\%
\]

Pero al segmentar por plan:

| Segmento | Usuarios a inicio | Bajas | Churn |
|---|---:|---:|---:|
| Total | 200 | 62 | **31.0%** |
| Gratuito | 178 | 60 | **33.7%** |
| Pago | 22 | 2 | **9.1%** |

Entonces:

- **Churn total:** 31%
- **Churn gratuito:** 33.7%
- **Churn de pago:** 9.1%

El 31% no significa que pierdes un 31% de tus clientes de pago. Significa que pierdes un 31% de todos los usuarios registrados, y tu base está dominada por usuarios gratuitos.

## 2) ¿Qué tan grave es?

**No es una emergencia inmediata, pero sí hay dos problemas distintos.**

### Problema 1: churn gratuito muy alto

Tienes un churn gratuito del **33.7%**. Eso es alto.

Pero depende de lo que sea ese plan gratuito:

- Si son usuarios que nunca pagaron, su churn no afecta directamente tu MRR.
- Si son usuarios que deberían convertirse en pago, sí es grave.
- Si tu CAC depende de convertirlos en pago, también es grave.

El churn gratuito alto indica que probablemente tienes un problema de **activación, onboarding, valor percibido o segmentación de usuarios**.

### Problema 2: churn de pago preocupante

El churn de pago es **9.1%**.

Con solo 22 usuarios de pago, 2 salidas ya mueven mucho el número. Pero 9.1% mensual es una cifra seria para un producto de pago.

No es catastrófico, pero sí es suficiente para actuar.

## 3) Diagnóstico rápido

Tu pánico viene de comparar un churn total contra una expectativa de 5%.

Probablemente:

- Tu expectativa de 5% era **churn de pago**, no churn total.
- El panel te está mostrando churn de **toda la base**, incluyendo free.
- Tu base tiene 89% de usuarios gratuitos:  
  \[
  178 / 200 = 89\%
  \]
- Y el 97% de las bajas son free:  
  \[
  60 / 62 = 96.8\%
  \]

Por eso el churn total se ve enorme.

## 4) Qué métrica deberías estar mirando

No deberías usar “churn total” como métrica principal de salud si tienes free.

Deberías ver:

### Churn de pago

\[
2 / 22 = 9.1\%
\]

Esta es la métrica de ingresos.

### Churn de MRR

Necesitas saber cuánto dinero salió con esos 2 pagos.

Pide al panel:

- MRR a inicio de mes.
- MRR de los 2 pagos que salieron.
- MRR churn.

Ejemplo:

Si los 2 pagos representaban $500 MRR y tu MRR total era $5,000:

\[
500 / 5000 = 10\%
\]

Eso sería un churn de MRR del 10%, que sí es muy serio.

Si solo eran $50 MRR, el impacto financiero sería menor.

### Churn de usuarios activos

Si muchos de los 178 free no estaban activos, el churn puede estar inflado.

Pregúntate:

- ¿Los 200 eran usuarios activos?
- ¿Incluyen cuentas inactivas?
- ¿Incluyen bots, pruebas o cuentas erróneas?
- ¿Es churn de cuentas o de usuarios?

## 5) Plan de acción

## Inmediato: 24-48 horas

### 1. Validar la métrica

Confirma con el panel:

- ¿El churn es mensual?
- ¿Es de cuentas o de usuarios?
- ¿El denominador es usuarios registrados o usuarios activos?
- ¿Incluye cuentas inactivas?
- ¿Se excluyen cambios de plan?
- ¿Hay usuarios que se cancelaron y luego se activaron?
- ¿El 5% al que te referías era churn de pago o churn de usuarios activos?

### 2. Crear el dashboard correcto

Mínimo:

- Churn total.
- Churn gratuito.
- Churn de pago.
- Churn de MRR.
- MRR a inicio.
- MRR a fin.
- Usuarios activos.
- Usuarios activos de pago.
- Free-to-paid conversion.
- Activación por coorte.
- D1, D7 y D30 retención.

### 3. Investigar las 2 salidas de pago

Con solo 2 cuentas, no puedes generalizar, pero sí puedes aprender.

Contacta a los 2 usuarios de pago que salieron.

Pregunta:

- ¿Por qué cancelaron?
- ¿Qué esperaban?
- ¿Qué no les funcionó?
- ¿Se sintieron que no recibieron valor?
- ¿Hubo problema técnico?
- ¿Cambiaron de precio?
- ¿Compararon con competencia?
- ¿Pueden volver?

También revisa:

- ¿Hubo incidentes en el producto?
- ¿Cambiaste algo este mes?
- ¿Cambiaste pricing, onboarding, emails, UI, limitaciones?
- ¿Hay quejas recientes?
- ¿Hubo soporte con casos complejos?
- ¿Hay cuentas grandes que casi cancelan?

## 6) Prioridad de acciones

## Prioridad 1: Retención de pago

Aunque sean solo 22 usuarios, son tus ingresos.

Acciones:

1. **Onboarding de pago más fuerte**
   - Asegúrate de que el usuario de pago haga su primera acción de valor pronto.
   - Si no hay onboarding claro, créalo.

2. **Seguimiento a cuentas de pago**
   - Contacta a cuentas nuevas de pago en los primeros 3 días.
   - Revisa si entendieron el valor.
   - Pregunta qué problema están intentando resolver.

3. **Flujo de cancelación**
   - Si alguien va a cancelar, no dejes que salga en frío.
   - Pide el motivo.
   - Ofrece ayuda.
   - A veces una llamada corta recupera el cliente.

4. **Win-back**
   - Crea un flujo para usuarios de pago que cancelan.
   - No solo un email genérico.
   - something personal:
     - “Vimos que cancelaste. ¿Qué no cumplimos?”
     - “¿Puedes volver si resolvemos X?”
     - “Te dejamos un acceso por 7 días para ver si sigue siendo útil.”

5. **Identifica señales de riesgo**
   - Usuarios de pago que no abren el producto.
   - Usuarios que bajan actividad.
   - Usuarios que abren pero no usan la función clave.
   - Usuarios con soporte negativo.
   - Usuarios que no completan onboarding.

## Prioridad 2: Activación de gratuito

El churn gratuito del 33.7% indica que muchos free no se activan o no ven valor.

Acciones:

1. **Define tu “momento de valor”**
   - ¿Qué debe hacer el usuario en los primeros 10 minutos para entender por qué sigue?
   - Ejemplo:
     - “Crear su primer proyecto”
     - “Conectar su cuenta”
     - “Ver su primer reporte”
     - “Invitar a un compañero”

2. **Mide activación**
   - No midas solo registros.
   - Mide:
     - % free que completa onboarding.
     - % free que hace la acción clave.
     - % free que vuelve al día 3.
     - % free que convierte a pago.

3. **Mejora onboarding**
   - Si el usuario no entiende en 5 minutos, se va.
   - Reduce fricción.
   - Guía la primera acción.
   - No le des todas las funciones a la vez.

4. **Segmenta los free**
   - Free que sí activan.
   - Free que nunca activan.
   - Free que casi pagan.
   - Free que llegan de un canal específico.
   - Free que se fueron después de X días.

5. **No trates a todos los free igual**
   - Algunos free son curiosos.
   - Algunos free son prospects reales.
   - Algunos free son noise.

## 7) Qué hacer con el churn de pago

Con 22 usuarios de pago, el churn de 9.1% puede deberse a pocas causas.

Investiga si es:

### Caso A: Producto no entrega valor

Señales:

- Los usuarios cancelan por “no lo necesito”.
- No usan la función principal.
- No completan onboarding.
- No hay uso recurrente.

Acción:

- Reforzar onboarding.
- Crear valor en las primeras 48 horas.
- Mejorar la primera experiencia.
- Asegurar que el usuario resuelva un problema claro.

### Caso B: Problema de soporte o confianza

Señales:

- Cancelan por bugs.
- Hay quejas.
- No responden a soporte.
- Hay errores críticos.

Acción:

- Resolver incidentes.
- Crear flujo de recuperación.
- Mejorar comunicación.
- Hacer follow-up post-incidente.

### Caso C: Precio o expectativas

Señales:

- Cancelan por “muy caro”.
- No entienden el valor.
- No ven diferencia con free.
- El plan no justifica el precio.

Acción:

- Revisar pricing.
- Revisar packaging.
- Mejorar justificación de valor.
- No subir precio a ciegas.

### Caso D: Ruido o base pequeña

Con solo 2 cuentas, puede ser un mes atípico.

Acción:

- No reaccionar con cambios grandes solo con un mes.
- Observar 3 meses.
- Pero sí contactar a los que salieron.

## 8) Metas razonables

No intentes bajar el churn total de 31% a 5% ya.

Mejor metas:

### Churn de pago

Objetivo a corto plazo:

- Bajar de **9.1% a <5%** mensual.

Si tu base de pago es pequeña, una meta de **<3-4%** puede ser razonable a mediano plazo.

### Churn gratuito

Depende del modelo:

- Si free es solo funnel:
  - Objetivo: mejorar activación y conversión.
  - Churn free de 33.7% puede ser aceptable si la conversión sube.

- Si free es importante para crecimiento:
  - Objetivo: reducir churn free a **<20-25%**.

- Si free es CAC:
  - No midas solo churn.
  - Mide **costo por free activo** y **costo por free convertido**.

### Churn de MRR

Esta es la métrica financiera.

Objetivo:

- Entender cuánto MRR pierdes al mes.
- Bajar churn de MRR por debajo de un umbral que soporte tu modelo.

## 9) Cómo comunicar esto a tu equipo o a ti mismo

No digas:

> “El churn es 31%.”

Di:

> “El churn total es 31%, pero está dominado por usuarios gratuitos. El churn de pago es 9.1%. El problema inmediato no es que salgan 62 usuarios, sino que tenemos una base con 89% free y un churn gratuito del 33.7%. Para ingresos, el churn de pago es preocupante pero no catastrófico. Necesitamos investigar las 2 salidas de pago, mejorar activación de free y medir churn de MRR.”

## 10) Errores que debes evitar

1. **No cambies el precio solo porque el churn total es alto.**
   - El churn total está inflado por free.

2. **No ignores el churn gratuito.**
   - Si free no activa, no convierte o genera CAC alto, es problema.

3. **No generalices con 2 cuentas de pago.**
   - Con 22 usuarios, 2 salidas son mucho, pero también pueden ser atípicos.

4. **No mires solo registros.**
   - Mide usuarios activos, pagos, MRR y activación.

5. **No confunda churn de cuentas con churn de usuarios.**
   - Si una cuenta tiene muchos usuarios, puede distorsionar.

## 11) Plan de 7 días

### Día 1

- Validar métricas.
- Confirmar denominador.
- Exportar datos.
- Calcular churn por plan.

### Día 2

- Contactar a los 2 usuarios de pago que salieron.
- Preguntar motivo.
- Ofrecer win-back.

### Día 3

- Revisar incidentes, cambios, bugs y soporte.
- Ver si hubo cambios este mes.
- Identificar cuentas de pago en riesgo.

### Día 4

- Crear dashboard:
  - Churn total.
  - Churn free.
  - Churn pago.
  - Churn MRR.
  - Activación.
  - Retención D7/D30.

### Día 5

- Analizar cohortes de free.
- Ver qué usuarios free se activan.
- Ver qué usuarios free se van.
- Identificar diferencia entre free que se quedan y free que se van.

### Día 6

- Mejorar onboarding de pago.
- Crear flujo de cancelación.
- Crear flujo de win-back.

### Día 7

- Definir KPIs:
  - Churn de pago.
  - Churn de MRR.
  - Activación de free.
  - Free-to-paid conversion.
  - Retención D7/D30.
  - MRR net.

## Conclusión

No estás en una crisis total.

El 31% es una métrica de **base total**, no de pagos.

Lo real es:

- **Churn gratuito: 33.7%** → alto, indica problema de activación/retención de free.
- **Churn de pago: 9.1%** → preocupante, indica que hay que investigar la retención de clientes de pago.
- **Churn total: 31%** → no debería ser tu métrica principal si tienes free.

Tu plan inmediato es:

1. Segmentar churn por plan.
2. Investigar las 2 salidas de pago.
3. Medir churn de MRR.
4. Mejorar onboarding de pago.
5. Mejorar activación de free.
6. Crear flujo de cancelación y win-back.
7. Dejar de usar churn total como única métrica de salud.