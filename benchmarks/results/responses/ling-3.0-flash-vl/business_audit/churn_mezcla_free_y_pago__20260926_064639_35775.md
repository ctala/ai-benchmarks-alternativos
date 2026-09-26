# Ling 3.0 Flash VL — business_audit/churn_mezcla_free_y_pago

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 16.719s | tokens_per_second: 140.2
- input_tokens: 221 | output_tokens: 2344

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

## 🔍 Primer paso: No entres en pánico — tu métrica está mal medida

Antes de actuar, verifiquemos qué está midiendo realmente tu panel.

### La cuenta matemática

Tu panel calcula: **62 bajas ÷ 200 usuarios = 31%**. La operación es correcta, pero **el denominador está contaminado**.

---

## 📊 Qué está pasando realmente: el problema del denominador

Tu base de 200 usuarios mezcla dos poblaciones con comportamientos radicalmente distintos:

| Segmento | Base | Bajas | Churn real |
|---|---|---|---|
| **Plan gratuito** | 178 | 60 | **33.7%** |
| **Plan de pago** | 22 | 2 | **9.1%** |
| **Total (tal como se reporta)** | 200 | 62 | **31%** |

### ¿Por qué importa esto?

El **31% está inflado artificialmente** porque estás dividiendo bajas comercialmente irrelevantes (usuarios gratuitos que probablemente nunca pagaron ni generaron valor) contra tu base total. Es como calcular la tasa de abandono de un restaurante incluyendo a todos los que entraron a pedir agua gratis.

**La métrica que realmente importa para tu negocio es el churn de pago: ~9.1%.**

---

## 🚨 ¿Qué tan grave es el 9.1% de churn de pago?

No es catastrófico, pero **es una alarma legítima**. Para referencia:

- **Excelente:** < 2% mensual
- **Aceptable:** 3-5% mensual
- **Preocupante:** 6-8% mensual
- **Crítico:** > 8% mensual → tu 9.1% está aquí

**Pero antes de actuar, necesitas responder tres preguntas fundamentales:**

1. **¿Cuántos nuevos pagos tuviste este mes?** Si ganaste 5 nuevos suscriptores y perdiste 2, tu net churn es negativo (buena señal). Si no ganaste ninguno, el problema es de adquisición + retención.
2. **¿Quiénes son los 2 que se fueron?** ¿Tenían algo en común? ¿Fueron churn por mal onboarding, precio, o falta de feature?
3. **¿Los 60 bajas gratuitas son patrón recurrente?** Si siempre fue así, tu 31% "histórico" nunca fue real.

---

## ✅ PLAN DE ACCIÓN (priorizado)

### 🔵 URGENTE — Hoy

| # | Acción | Por qué |
|---|---|---|
| 1 | **Corregir el cálculo del churn en el panel** → segmentar gratuito vs. pago | El 31% te está haciendo tomar decisiones equivocadas. Define dos métricas: churn total y churn de pago. |
| 2 | **Identificar a los 2 usuarios de pago que se fueron** | Una baja de pago siempre es investigable. Habla con ellos (email o llamada). ¿Qué les faltó? ¿Fue precio? ¿Fue producto? |
| 3 | **Calcular net revenue churn** | (Bajas de pago - Nuevos pagos) / Base de pago. Si ganaste suficientes suscriptores nuevos, el problema puede ser menor de lo que crees. |

### 🟡 ESTA SEMANA

| # | Acción | Por qué |
|---|---|---|
| 4 | **Segmentar las 60 bajas gratuitas por antigüedad** | ¿Se fueron en los primeros 3 días? Si sí, el problema es onboarding (no retención). ¿Se fueron después de meses? Entonces hay un problema de engagement. |
| 5 | **Revisar el funnel de conversión gratuito → pago** | Si tu churn gratuito es alto pero tu conversión a pago es baja, el cuello de botella está antes del churn: en el valor percibido. |
| 6 | **Analizar cohortes de usuarios de pago** | ¿El churn de pago ha sido siempre ~9% o es un salto reciente? Si es reciente, qué cambió (producto, precio, competencia)? |

### 🟢 ESTE MES

| # | Acción | Por qué |
|---|---|---|
| 7 | **Definir un North Star Metric de retención real** | Sugiero: **Monthly Paid Churn Rate** + **Net Revenue Churn Rate**. Elimina el churn "total" como KPI principal. |
| 8 | **Implementar alertas tempranas** | Detectar usuarios de pago en riesgo (sin login en 14 días, sin uso de feature clave, etc.) antes de que cancelen. |
| 9 | **Diseñar un experimento de retención para pago** | Onboarding mejorado para nuevos suscriptores, check-in a los 7 días, o programa de valor reactivo. |

---

## 🎯 Resumen ejecutivo para ti

> **Tu plataforma no tiene un churn del 31%. Tiene un churn reportado de 31% que está artificialmente inflado por bajas gratuitas. Tu churn real de pago es ~9.1%, que es preocupante pero no catastrófico. El riesgo real es que sigues tomando decisiones basado en una métrica errónea.**

**Prioridad #1: Corregir la métrica. Prioridad #2: Investigar a los 2 usuarios de pago perdidos. Prioridad #3: Calcular net churn.**

Respira. Actúa con datos, no con pánico. 🧠