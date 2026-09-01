# Qwen 3.8 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 71.791s | tokens_per_second: 95.4
- input_tokens: 227 | output_tokens: 6850

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

Respira: **el 31% no es la métrica que debes usar para entender la gravedad**. Estás midiendo churn de toda la base, donde la mayoría son usuarios gratuitos. En negocios freemium, eso casi siempre infla el “churn total” y genera pánico innecesario.

## 1) Lo que realmente dicen tus números

| Segmento | Bajas | Base inicio | Churn mensual |
|---|---:|---:|---:|
| Total | 62 | 200 | **31.0%** |
| Gratuitos | 60 | 178 | **33.7%** |
| Pagos | 2 | 22 | **9.1%** |

La métrica importante para negocio es, por ahora:

> **Churn de cuentas pagadas: 2 / 22 = 9.1% mensual**  
> Retención mensual pagada: **90.9%**

Si eso se mantuviera todo el año, la retención anual aproximada sería:

> 0.909^12 ≈ **31.7%** de cuentas pagadas retenidas al año  
> Churn anual aproximado: **68.3%**

Pero ojo: con solo 22 usuarios pagos, **2 bajas son una señal fuerte, pero estadísticamente frágil**. Una baja más cambia el churn a ~13.6%; una baja menos, a ~4.5%.

## 2) ¿Qué tan grave es?

Depende de tres cosas:

### A) Si el negocio depende de los usuarios pagos
Si vendes SaaS, memberships, software B2B, etc., **9.1% de churn mensual de cuentas pagadas es alto**. No es para entrar en pánico, pero sí para actuar esta semana.

### B) Cuánto dinero representan esas 2 bajas
El “logo churn” es 9.1%, pero el **MRR churn** puede ser mayor o menor.

Ejemplos:

- Si las 2 bajas son usuarios de $20/mes y el promedio pagado es $50/mes, el impacto es bajo.
- Si las 2 bajas son usuarios de $500/mes y el promedio es $100/mes, el impacto es grave.
- Si uno era anual, otro fue downgrade, o hubo un fallo de pago, la interpretación cambia.

Necesitas calcular:

> **MRR churn = MRR cancelado este mes / MRR al inicio del mes**

### C) Qué es “usuario gratuito” para ti
El 33.7% de bajas de usuarios gratuitos puede ser:

- Normal, si son cuentas inactivas, trials, cuentas de prueba, usuarios que probaste una vez.
- Grave, si son leads calificados que deberían activarse o convertir.
- Irrelevante para ingresos, si el plan gratuito no está diseñado para convertir.

En resumen:

> **El 31% no es el problema. El 9.1% de churn pagado sí merece atención. El 33.7% de churn gratuito es otra conversación.**

---

# Plan inmediato

## Paso 1: Cambia la definición de churn en el panel

Tu panel actual está midiendo:

> Bajas totales / usuarios totales

Eso mezcla gratis y pago. Deberías tener, como mínimo, estas métricas separadas:

### Para negocio / ingresos
- **Paid logo churn**: cuentas pagadas que cancelan / cuentas pagadas al inicio.
- **Paid MRR churn**: MRR cancelado / MRR al inicio.
- **Net revenue retention**: MRR inicio + expansiones − contracciones − churn.
- **Churn involuntario**: fallos de pago, tarjetas rechazadas, errores de facturación.
- **Churn voluntario**: cancelación real por decisión del usuario.

### Para usuarios gratuitos
- **Free user retention**: usuarios gratuitos activos que siguen activos.
- **Activation rate**: usuarios gratuitos que completan la acción clave.
- **Free-to-paid conversion**: % de gratuitos que pagan.
- **Trial churn**, si tienes periodo de prueba.

No uses “churn” como sinónimo de “baja de cualquier cuenta”.

---

## Paso 2: Valida las 2 bajas pagadas antes de actuar

Necesitas responder:

1. ¿Cuándo cancelaron exactamente?
2. ¿Fue cancelación voluntaria o fallo de pago?
3. ¿Cuánto MRR tenía cada una?
4. ¿Llevaban mucho tiempo pagando o eran nuevas?
5. ¿Usaban el producto antes de cancelar?
6. ¿Tuvieron tickets de soporte, quejas o problemas técnicos?
7. ¿Hubo cambio de precio, producto, contrato, facturación o UX?
8. ¿Fueron downgrade a free o cancelación total?
9. ¿Eran cuentas de prueba, internas, duplicadas o de test?

Si alguna fue un fallo de pago recuperable, no es churn voluntario real.

---

## Paso 3: Contacta a las 2 cuentas pagadas que se fueron

En las próximas 24–48 horas, haz una salida de cliente. No para venderles de inmediato, sino para entender.

Mensaje simple:

> Hola [nombre], vimos que cancelaste tu cuenta de pago. No quiero molestarte, pero si tienes 1 minuto, me ayudaría muchísimo saber qué te llevó a cancelar: ¿fue precio, falta de uso, problema técnico, no era lo que esperabas, facturación u otra cosa? Si quieres, te puedo ofrecer ayuda con algo específico o simplemente escucharte.

Registra la causa en una tabla:

| Cuenta | MRR | Antigüedad | Uso | Soporte | Causa | ¿Recuperable? | Acción |
|---|---:|---:|---:|---:|---|---|---|
| Cliente A | $X | X meses | Alto/Bajo | Sí/No | Precio/valor/fallo | Sí/No | Winback |

Si descubres que el problema fue onboarding, facturación, producto o soporte, ahí está la prioridad.

---

## Paso 4: Revisa los 20 usuarios pagos que quedan

No esperes a que se vayan. Haz un health check rápido.

Segmenta los 20 en:

- **Sanos**: usan el producto, no han tenido problemas, renovarán o son estables.
- **En riesgo**: bajo uso, tickets negativos, sin login, precio nuevo, contrato por renovar.
- **Críticos**: no usan el producto, quejados, pago fallido, sin valor claro.

Pregunta clave por usuario:

> ¿Este usuario pagó porque el producto le resolvió un problema, o pagó por impulso/trial y todavía no ve valor?

Acción:

- A los sanos: agradecer, pedir feedback, pedir testimonio o referral.
- A los en riesgo: outreach humano, revisar onboarding, ofrecer ayuda.
- A los críticos: llamada o correo personalizado, entender bloqueo real.

---

## Paso 5: Separa churn pagado de churn gratuito

El churn gratuito no debería asustarte igual que el pagado. Pero sí debes entender qué significa.

Pregúntate:

- ¿Los 178 usuarios gratuitos son activos?
- ¿Son trials?
- ¿Son cuentas creadas y nunca usadas?
- ¿Son usuarios que simplemente abandonaron?
- ¿El plan gratuito sirve para captar leads o solo para soporte?
- ¿Qué porcentaje de gratuitos termina pagando?

Si el plan gratuito es un embudo, la métrica no es “cuántos se van”, sino:

> ¿Cuántos se activan y cuántos convierten?

Por ejemplo:

- 178 gratuitos → 60 bajas → no necesariamente malo.
- Pero si de 178 gratuitos solo 22 pagan y 2 se van, el problema no es solo churn: puede ser activación, valor, precio o nicho.

---

## Paso 6: Recalcula con la población correcta

Antes de reportar nada, define la población.

### Para churn de negocio
Usa:

> Cuentas pagadas activas al inicio del mes

No:

> Todos los usuarios registrados

### Para churn de producto
Usa:

> Usuarios activos al inicio del mes

No:

> Cuentas creadas alguna vez

### Para churn de trial
Usa:

> Trials iniciados en una cohorte específica

No:

> Todos los usuarios gratuitos mezclados

---

# Qué reportar a stakeholders

No digas:

> “El churn subió a 31%”.

Di:

> “El churn total de cuentas fue 31%, pero ese número mezcla usuarios gratuitos y pagos. El churn de cuentas pagadas fue 9.1% mensual, equivalente a 2 de 22 clientes. El impacto en MRR fue X. Estamos investigando causas, separando churn voluntario de involuntario y contactando a las cuentas afectadas. El churn gratuito fue 33.7%, pero corresponde a la base free y no es la métrica principal para ingresos.”

Si no tienes MRR todavía:

> “Necesitamos cerrar el dato de MRR cancelado para dimensionar impacto económico.”

---

# Prioridades según causa

## Si la causa es falta de valor
Acciones:

- Mejorar onboarding.
- Definir la “activación” clara.
- Enviar guías de uso.
- Hacer check-in a 7/14/30 días.
- Entregar quick wins.

## Si la causa es precio
Acciones:

- Revisar si el precio está mal segmentado.
- Ver si hay planes intermedios.
- Ofrecer anualidad.
- No bajar precio general sin evidencia.

## Si la causa es facturación
Acciones:

- Recuperar pagos fallidos.
- Enviar avisos antes del vencimiento.
- Ofrecer medios de pago alternativos.
- Revisar errores de checkout.

## Si la causa es soporte
Acciones:

- SLA de respuesta.
- Ticket review.
- Seguimiento post-cancelación.
- Playbook de retención.

## Si la causa es producto
Acciones:

- Revisar cambios recientes.
- Analizar eventos de abandono.
- Verificar bugs.
- Priorizar features críticas para retención.

---

# Plan de 7 días

## Día 1: Recalcular y limpiar
- Separar free / paid / trial.
- Recalcular paid logo churn.
- Recalcular paid MRR churn.
- Identificar si hubo churn involuntario.
- Validar si las 62 bajas son reales o incluyen cuentas inactivas/test.

## Día 2: Investigar las 2 bajas pagadas
- Revisar uso, soporte, facturación, antigüedad, MRR.
- Contactar a ambas.
- Clasificar causa.

## Día 3: Health check de los 20 pagos
- Clasificar sanos / en riesgo / críticos.
- Enviar outreach a los en riesgo.
- Agendar llamadas si aplica.

## Día 4: Revisar funnel gratuito
- ¿Cuántos gratuitos se activan?
- ¿Cuántos convierten a pago?
- ¿Cuántos trials llegan a pago?
- ¿Qué acción predice mejor la conversión?

## Día 5: Revisar cambios recientes
- ¿Subió precio?
- ¿Cambió plan?
- ¿Hubo bug?
- ¿Hubo problema de facturación?
- ¿Hubo cambio de equipo, soporte o producto?

## Día 6: Crear dashboard mínimo viable
Incluir:

- Cuentas pagadas al inicio.
- Cuentas pagadas al final.
- Nuevas cuentas pagadas.
- Bajas pagadas.
- Churn voluntario.
- Churn involuntario.
- MRR churn.
- Net revenue retention.
- Free-to-paid conversion.
- Activation rate.
- Cohorte de retención pagada.

## Día 7: Reportar y decidir
Reporte final:

> “Churn pagado: X%. Impacto MRR: X. Causas principales: A, B, C. Acciones: contactar clientes, arreglar facturación, mejorar onboarding, etc. Meta para próximos 30 días: reducir churn pagado a Y% y aumentar activación a Z%.”

---

# Regla clave

No midas churn de toda la base si tu negocio cobra solo a una parte.

La métrica correcta para saber si estás vivo es:

> **Retención de clientes pagos y retención de ingresos.**

El churn gratuito importa, pero como embudo, no como pánico financiero.

---

## Mi lectura rápida de tu caso

- **31% total:** engañoso, no usar para tomar decisiones.
- **33.7% gratuito:** posible ruido del modelo freemium; revisar activación.
- **9.1% pagado:** señal de alerta, no catástrofe.
- **2 bajas de 22:** suficiente para investigar, pero muestra pequeña.
- **Gravedad real:** depende de MRR cancelado y causas.

Si me pasas el MRR promedio, precio de cada plan, si hubo fallos de pago y cuánto tiempo llevaban esos 2 clientes pagando, puedo ayudarte a calcular exactamente qué tan grave es y qué acción priorizar primero.