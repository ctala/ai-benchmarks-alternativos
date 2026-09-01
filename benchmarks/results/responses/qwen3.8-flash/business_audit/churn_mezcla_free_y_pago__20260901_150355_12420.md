# Qwen 3.8 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 376.041s | tokens_per_second: 65.4
- input_tokens: 227 | output_tokens: 24576

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

Primero: **respira**. Tu pánico viene de comparar **31% vs 5%** sin segmentar la población.

Tu panel no está diciendo “perdimos 31% de clientes de pago”. Está diciendo:

> **De todos los usuarios registrados/activos al inicio del mes, se dieron de baja 31%.**

Eso incluye **178 usuarios gratuitos** y solo **22 usuarios/pagos**. En un negocio freemium/SaaS, el churn de usuarios gratuitos puede ser enorme y no necesariamente grave para el negocio.

---

## 1. Lo que realmente dicen tus números

| Población | Bajas | Inicio de mes | Churn | Lectura |
|---|---:|---:|---:|---|
| Total usuarios | 62 | 200 | **31.0%** | Métrica mezclada; no usar sola |
| Usuarios gratuitos | 60 | 178 | **33.7%** | 30 puntos del 31% vienen de aquí |
| Usuarios/pagos | 2 | 22 | **9.1%** | Esta es la métrica relevante para retención de negocio |

Descomposición del 31%:

- Free churn aporta: `60 / 200 = 30.0 pp`
- Paid churn aporta: `2 / 200 = 1.0 pp`
- Total: **31.0%**

Además, **96.8% de las bajas fueron usuarios gratuitos**:

`60 / 62 = 96.8%`

Es decir: el 31% está dominado por la población gratuita. No es comparable con un 5% esperado para clientes de pago.

---

## 2. ¿Qué tan grave es?

Depende de qué significaba tu “5% esperado”.

### Escenario A: El 5% esperado era churn mensual de clientes de pago

Entonces la comparación correcta es:

> **Churn de pago actual: 9.1% vs esperado 5%**

Esto es **alto**, pero con una base muy pequeña:

- 1 baja de pago = 4.5 pp de churn
- 2 bajas de pago = 9.1 pp
- Si una de esas 2 fuera error, volverías a 4.5%
- Si fueran 3 bajas, serían 13.6%

Con solo 22 cuentas/usuarios de pago, la métrica es muy ruidosa. Un intervalo de confianza aproximado para 2/22 podría ir del **2.5% al 27.8%**. No es para entrar en pánico, pero sí para investigar.

**Veredicto:** amarillo, no rojo.  
**Acción:** revisar las 2 bajas, validar si son cuentas reales, voluntarias, involuntarias, y calcular impacto en MRR/ARR.

---

### Escenario B: El 5% esperado era churn total de usuarios, incluyendo gratuitos

Si antes tenías 5% de churn total y ahora tienes 31%, probablemente cambió la definición de la población:

- ¿Antes el panel solo medía usuarios de pago?
- ¿Ahora incluye free?
- ¿Ahora incluye usuarios inactivos, trials, cuentas internas, bots o cuentas auto-canceladas?
- ¿Cambió el denominador? ¿Antera era “usuarios activos” y ahora es “usuarios registrados”?

**Veredicto:** el problema principal es de definición/reporting, no necesariamente de retención.

---

### Escenario C: El 5% esperado era churn anual

Si el 5% era anual y ahora tienes 9.1% mensual de pago, eso sí sería muy grave:

- 9.1% mensual anualizado sería aproximadamente:

`1 - (1 - 0.091)^12 ≈ 68% de churn anual`

Eso implicaría una vida promedio del cliente de pago de unos 11 meses, frente a unos 20 meses con 5% mensual.

Pero esto solo aplica si tus planes son mensuales o si el churn mensual es comparable. Si tienes planes anuales, no anualices igual.

**Veredicto:** rojo si era 5% anual; amarillo si era 5% mensual.

---

### Escenario D: La gravedad real depende del dinero, no de los logos

Tener 2 bajas de pago no es lo mismo que tener 2 bajas de alto valor.

Necesitas calcular:

> **Gross MRR/ARR churn = MRR/ARR perdido / MRR/ARR inicial**

Ejemplos:

| Situación | Impacto probable |
|---|---|
| 2 cuentas de pago representan 2% del MRR | Amarillo/verde |
| 2 cuentas de pago representan 15% del MRR | Amarillo-rojo |
| 2 cuentas de pago representan 50% del MRR | Rojo |
| Las 2 bajas son pagos fallidos | Recuperable; revisar dunning |
| Las 2 bajas son voluntarias por producto/precio | Investigar causa raíz |
| Las 2 bajas son clientes nuevos | Posible onboarding/expectativa |
| Las 2 bajas son clientes antiguos | Posible pérdida de valor/competencia |

Por ahora, **no puedes decir que el negocio está en crisis con 31%**. Puedes decir que:

> El churn de pago fue 9.1% mensual, pero falta validar impacto en ingresos, motivos, tenencia y si son cuentas o usuarios.

---

## 3. Plan inmediato: qué hacer hoy

### Paso 1: Recalcula las métricas por segmento

Reporta tres números separados:

1. **Churn total de usuarios**: 31%  
   - Contexto: incluye free; no usar para decisión de negocio.
2. **Churn de usuarios gratuitos**: 33.7%  
   - Contexto: abandono/inactividad, no necesariamente churn comercial.
3. **Churn de clientes/usuarios de pago**: 9.1%  
   - Contexto: métrica relevante para retención.

Si puedes, separa también:

- Churn de cuentas de pago vs usuarios de pago
- Churn de logos vs churn de MRR
- Churn voluntario vs involuntario
- Churn mensual vs churn anual
- Churn de clientes nuevos vs clientes antiguos

---

### Paso 2: Valida la población que estás midiendo

Pregunta crítica:

> ¿22 usuarios de pago son 22 clientes/cuentas o 22 usuarios dentro de cuentas?

Para churn de negocio, normalmente deberías medir **cuentas/clientes**, no usuarios individuales.

Ejemplo:

- Si 22 usuarios de pago pertenecen a 10 clientes, y 2 usuarios de pago se fueron, puede que no sean 2 cuentas perdidas.
- Si 22 usuarios de pago pertenecen a 22 clientes, entonces sí fue 2/22 = 9.1% de logos.

También valida:

- ¿Incluyes trials?
- ¿Incluyes cuentas internas/test?
- ¿Incluyes usuarios inactivos?
- ¿Incluyes cuentas pausadas?
- ¿Incluyes downgrades como churn?
- ¿Incluyes cancelaciones antes del inicio del mes?
- ¿El corte es por fecha de baja, fecha de invoice, fecha de cancelación o fecha de expiración?
- ¿Hay timezone o duplicados?

---

### Paso 3: Analiza las 2 bajas de pago

Para cada una, saca:

| Campo | Por qué importa |
|---|---|
| `customer_id` | ¿Es una cuenta o un usuario? |
| `plan_type` | Gratis, pago, trial, anual, mensual |
| `MRR/ARR` | Impacto financiero real |
| `tenure` | Cliente nuevo vs antiguo |
| `signup_date` | Cohorte de adquisición |
| `last_login` | Uso previo a la baja |
| `usage_score` | Si estaba activo o dormido |
| `support_tickets` | Problemas previos |
| `billing_status` | Past due, failed payment, refund, chargeback |
| `cancellation_reason` | Voluntario, involuntario, error, competencia, precio, no uso |
| `source/channel` | Adquisición: Google, referral, contenido, outbound |
| `segment` | B2B, SMB, enterprise, self-serve, vertical |

Haz una llamada o encuesta a esas 2 cuentas. En una base tan pequeña, cada baja es información valiosa.

---

### Paso 4: Calcula churn de ingresos, no solo logos

Necesitas:

#### Gross MRR churn

`MRR perdido por bajas / MRR inicial`

#### Net MRR churn

`MRR perdido - expansiones + downgrades / MRR inicial`

#### Net Revenue Retention, NRR

`(MRR inicial + expansiones - churn - downgrades) / MRR inicial`

Reglas prácticas:

- NRR > 100%: tu base actual crece a pesar de churn.
- NRR 90%-100%: aceptable pero con presión.
- NRR < 90%: problema serio de retención/expansión.
- Gross MRR churn > 5% mensual: alta atención.
- Gross MRR churn > 10% mensual: rojo, a menos que tu segmento sea muy transaccional.

Si no tienes MRR inicial, usa al menos precio de plan o ARR/12.

---

## 4. Qué hacer con el churn gratuito del 33.7%

No lo trates como “churn de negocio” salvo que tu modelo dependa de usuarios gratuitos.

Preguntas clave:

1. ¿Qué significa “darse de baja” para un usuario gratuito?
   - ¿Canceló una cuenta?
   - ¿Dejó de entrar?
   - ¿Fue auto-archivado?
   - ¿Era un trial que no convirtió?
   - ¿Era spam/bot?
2. ¿Son usuarios nuevos o antiguos?
3. ¿Alguna vez activaron el producto?
4. ¿Vienen de canales de baja calidad?
5. ¿Son usuarios que nunca iban a pagar?

### Si el churn gratuito es alto pero esperado

Puede ser normal en freemium. No lo mezcles con churn de pago.

Reporta como:

> **Drop-off gratuito: 33.7%**

Y mide:

- Registro
- Activación
- Primer valor
- D7/D30 retention
- Conversión free → paid
- Costo de soporte por usuario free
- Calidad por canal

### Si el churn gratuito es alto y no esperado

Puede ser problema de:

- Adquisición: atraes usuarios equivocados.
- Onboarding: no entienden el valor.
- Producto: el free plan no entrega valor suficiente.
- Pricing: la conversión es demasiado difícil.
- Datos: cuentas inactivas, bots, spam.

En ese caso, no arregles “retención de pago”; arregla **activación y conversión**.

---

## 5. Plan por tiempo

### Próximas 24 horas

1. **No reportes 31% sin contexto.**
2. Recalcula:
   - Total churn: 31%
   - Free churn: 33.7%
   - Paid churn: 9.1%
3. Valida si 22 son clientes o usuarios.
4. Identifica las 2 bajas de pago.
5. Calcula MRR/ARR perdido.
6. Clasifica cada baja:
   - Voluntaria/involuntaria
   - Error de datos
   - Pago fallido
   - Producto
   - Precio
   - Soporte
   - Onboarding
   - No longer needed
   - Competencia
   - Cierre de empresa
7. Contacta a las 2 cuentas de pago bajas si es posible.

---

### Próximos 2-3 días

1. Revisa cohortes:
   - Clientes de pago por mes de adquisición
   - Churn en primeros 30/60/90 días
   - Churn por plan
   - Churn por canal
   - Churn por segmento
2. Revisa señales previas:
   - Caída de login
   - Caída de uso de feature clave
   - Tickets de soporte
   - NPS bajo
   - Fallos de pago
   - Tiempo sin valor percibido
3. Arma una tabla simple:

| Cuenta | Plan | MRR | Tenure | Última actividad | Motivo | Voluntario/involuntario | Recuperable | Acción |
|---|---:|---:|---:|---:|---|---|---|---|
| A | Pro | $X | 3 meses | 12 días | Precio | Voluntario | Sí | Oferta de save |
| B | Basic | $Y | 1 mes | 25 días | No uso | Voluntario | Posible | Onboarding |

---

### Próximos 7 días

1. Corrige el dashboard.
2. Define KPIs separados:
   - Paid logo churn
   - Paid MRR churn
   - Net revenue retention
   - Free activation
   - Trial conversion
   - Involuntary churn
3. Implementa alertas:
   - 2+ cancelaciones de pago en el mes: revisar
   - 1 cancelación de cuenta top MRR: revisar
   - Gross MRR churn > 3% mensual: alerta
   - Gross MRR churn > 5% mensual: investigación profunda
   - NRR < 90%: escalar
4. Crea un playbook de save:
   - Llamada post-cancelación
   - Encuesta
   - Oferta de migración
   - Soporte prioritario
   - Descuento temporal
   - Revisión de uso
   - Fix de billing
5. Si hay pagos fallidos:
   - Retry automático
   - Email/SMS de recuperación
   - Actualización de tarjeta
   - Periodo de gracia
   - Alternativas de pago
   - Integración con Stripe/Chargebee/Braintree

---

### Próximos 30 días

1. Mide churn con ventana rodante de 3 meses, porque tu base de pago es pequeña.
2. Separa churn de:
   - Clientes nuevos
   - Clientes existentes
   - Cuentas anuales
   - Cuentas mensuales
   - Downgrades
   - Pausas
   - Reactivaciones
3. Evalúa impacto en LTV:
   - Si churn mensual es 9.1%, vida promedio ≈ 11 meses
   - Si churn mensual es 5%, vida promedio ≈ 20 meses
4. Evalúa CAC vs LTV:
   - Si el churn sube, el payback se alarga.
   - Si las 2 cuentas bajas son top MRR, el impacto puede ser mayor que el logo churn.
5. Decide si el problema es:
   - Producto
   - Precio
   - Soporte
   - Onboarding
   - Adquisición
   - Billing
   - Reporting

---

## 6. Qué métricas deberías usar de ahora en adelante

No uses solo “churn total”. Usa este set:

### Para negocio/retenção

1. **Paid logo churn**
   - Clientes de pago perdidos / clientes de pago activos al inicio
   - En tu caso: 2/22 = 9.1%

2. **Gross MRR churn**
   - MRR perdido / MRR inicial
   - Más importante que logos.

3. **Net MRR churn**
   - MRR perdido + downgrades - expansiones / MRR inicial

4. **Net Revenue Retention, NRR**
   - MRR final de la misma cohorte / MRR inicial
   - Mide si tu base crece o se encoge.

5. **Involuntary churn**
   - Bajas por pagos fallidos, tarjetas rechazadas, errores de facturación.

6. **Voluntary churn**
   - Bajas intencionales por producto, precio, competencia, etc.

### Para free/trial

1. **Free activation rate**
   - Usuarios gratuitos que completan acción clave.

2. **Free D7/D30 retention**
   - Retención de usuarios gratuitos.

3. **Trial conversion rate**
   - Trials que pasan a pago.

4. **Free-to-paid conversion**
   - Usuarios gratuitos que se convierten.

5. **Dormancy rate**
   - Usuarios gratuitos inactivos, no necesariamente “churn”.

---

## 7. Cómo debería verse tu panel

En lugar de un solo número “Churn: 31%”, deberías tener:

| KPI | Valor | Contexto |
|---|---:|---|
| Churn total de usuarios | 31.0% | Mezcla free + pago; no usar para negocio |
| Churn gratuito | 33.7% | Drop-off/abandono |
| Churn de pago logo | 9.1% | Métrica clave; base pequeña |
| Churn de pago MRR | Pendiente | Necesitas MRR inicial y perdido |
| Bajas involuntarias | Pendiente | Pagos fallidos, billing |
| Bajas voluntarias | Pendiente | Producto/precio/soporte |
| NRR | Pendiente | Retención + expansión |
| Free → Paid conversion | Pendiente | Salud del funnel |

---

## 8. SQL/validación rápida

Puedes pedir algo así:

```sql
WITH start_snapshot AS (
  SELECT
    user_id,
    customer_id,
    plan_type,
    status,
    mrr,
    subscription_id
  FROM users
  WHERE date_trunc('month', start_date) = '2026-06-01'
    AND status IN ('active', 'trial', 'free', 'paid')
),
churned AS (
  SELECT
    user_id,
    customer_id,
    plan_type,
    subscription_id,
    mrr,
    churn_date,
    reason_code,
    is_involuntary
  FROM user_events
  WHERE event_type = 'cancellation'
    AND churn_date BETWEEN '2026-06-01' AND '2026-06-30'
)
SELECT
  plan_type,
  COUNT(DISTINCT s.user_id) AS active_start,
  COUNT(DISTINCT c.user_id) AS churned,
  COUNT(DISTINCT c.user_id)::numeric / COUNT(DISTINCT s.user_id) AS churn_rate
FROM start_snapshot s
LEFT JOIN churned c
  ON s.user_id = c.user_id
GROUP BY plan_type;
```

Pero antes de ejecutar, valida:

- ¿Usamos `user_id` o `customer_id`?
- ¿Excluimos trials?
- ¿Excluimos internos/test?
- ¿Excluimos bots?
- ¿Definimos “activo” correctamente?
- ¿Estamos usando fecha de baja o fecha de expiración?
- ¿Incluimos downgrades?
- ¿Incluimos pausas?
- ¿Reconciliamos con Stripe/billing?

---

## 9. Mensaje para stakeholders

Puedes enviar algo así:

> El 31% reportado corresponde a churn mezclado de todos los usuarios, incluyendo 178 usuarios gratuitos. De las 62 bajas, 60 fueron gratuitas y solo 2 fueron de pago.  
>   
> El churn de pago fue 9.1% mensual (2/22). Es una señal a revisar, pero la base es pequeña: una sola baja adicional o una corrección de datos cambia mucho el porcentaje.  
>   
> Estamos validando impacto en MRR/ARR, motivos de baja, si fueron voluntarias o involuntarias, y si son cuentas o usuarios. La métrica relevante para negocio no es 31%, sino churn de pago por logo y por MRR.

---

## 10. Mi lectura final

### El 31% no es una crisis, es una mala lectura de población

Tu panel está midiendo **todos los usuarios**, mientras que tu expectativa de 5% probablemente venía de una métrica más enfocada en **clientes de pago** o usuarios activos relevantes.

### El número que sí merece atención es 9.1%

Pero no entres en pánico todavía porque:

- Solo son 2 bajas.
- La base de pago es pequeña.
- Un error o una baja recuperable puede cambiar el número.