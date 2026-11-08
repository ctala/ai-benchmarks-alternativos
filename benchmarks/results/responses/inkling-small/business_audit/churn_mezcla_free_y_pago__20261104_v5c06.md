# Inkling Small — business_audit/churn_mezcla_free_y_pago

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.48 | quality: 10.0
- latency_total: 71.469s | tokens_per_second: 39.2
- input_tokens: 172 | output_tokens: 2799

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

Antes de interpretar cualquier número, verifico qué población está midiendo tu panel.

**Tu panel mide: TODA la base (libre + pago).**
- Base inicial: 200 (178 gratuitos / 22 de pago).
- Bajas: 62 (60 gratuitos / 2 de pago).
- Cálculo real: 62 / 200 = **31%**.

Pero tu preocupación (y probablemente tu benchmark del 5%) es sobre **clientes de pago / ingresos**. El 31% es un artefacto estadístico: estás mezclando una población con alta rotación natural (gratis) con una de alta retención (pago).

---

### Desagregado real (lo que importa)

| Segmento | Base inicio | Bajas | Churn real | Contexto |
|---|---|---|---|---|
| **Plan gratuito** | 178 | 60 | **33.7%** | Normal/alto; baja rotación de cuentas inactivas o de prueba. |
| **Plan de pago** | 22 | 2 | **9.1%** | **Este es tu número real de negocio.** Comparado con tu 5% anterior, sí hay un incremento (casi el doble). |
| **Global (tu panel)** | 200 | 62 | **31%** | Métrica sin valor estratégico si no segmentas. |

---

### ¿Qué tan grave es?

- **Para la toma de decisiones:** Grave. Un solo número te hace pensar que hay un problema sistémico, cuando en realidad hay dos fenómenos distintos.
- **Para el negocio:** Moderado. Perder **2 de 22 pagadores** (9.1%) no es una catástrofe, pero sí es una señal de alerta que requiere acción. Perder **60 gratuitos** es, por sí solo, poco relevante si no convierten o si son cuentas muertas.

---

### Plan de acción inmediato (haz esto hoy)

**1. Corrige tu métrica de reporte (no mañana)**
No reportes un "churn del 31%". Tu dashboard debe tener:
- **Churn de usuarios pagadores:** 9.1%.
- **Churn de ingresos (Revenue Churn):** Calcula cuánto MRR representaban esos 2 usuarios. Si son iguales, es ~9%; si hay diferencias, podría ser más o menos.
- **Churn de usuarios activos/free:** 33.7%, pero solo como métrica de salud de funnel (¿se activan antes de irse?).

**2. Investiga los 2 pagadores que se fueron (prioridad alta)**
Con solo 22 de pago, cada baja es un 4.5% de tu base. Haz esto hoy:
- ¿Se fueron directo o bajaron a gratuito primero? (Si bajaron, es un problema de valor/precio, no de churn absoluto).
- ¿Hay un patrón común? (mismo mes de onboarding, misma funcionalidad no usada, misma objeción de soporte/pricing).
- Entrevista rápida de salida (email de 2 preguntas).

**3. Decide qué hacer con los 60 gratuitos (prioridad baja / estratégica)**
No gastes presupuesto de retención en ellos hasta responder:
- ¿Son cuentas de prueba que nunca activaron? → Es ruido.
- ¿Hay una limpieza de cuentas inactivas? → Es un evento técnico, no un problema de producto.
- ¿Son tu funnel de conversión? → Si sí, tu problema no es "retención gratuita", sino **activación y conversión a pago**.

**4. Ajusta tu benchmark**
Si tu 5% era de pago, tu real es 9.1%. Eso **sí requiere acción** (quizá onboarding, soporte, precio, o una feature clave que se rompió este mes). Pero no es "la empresa se derrumba".

**5. Corrige el cálculo en tu panel**
Filtra siempre por `plan = pago` para el churn estratégico. Usa **cohortes** (ej. "usuarios que se unieron en enero: ¿cuántos siguen activos en febrero?") para evitar que cuentas antiguas o inactivas distorsionen la tasa mensual.

---

### Resumen para salir del pánico

No estás en 31% de crisis. Estás en:
- **~9% churn pagado:** A investigar y actuar (quizá tu verdadero problema).
- **~34% churn gratuito:** Probablemente ruido o normalidad de un modelo freemium.

**Corrige la métrica primero.** El pánico viene de medir "todos" y pensar que todos importan igual. Una vez que separes los segmentos, el plan se vuelve claro: proteger a los 22 pagadores y optimizar la conversión de los 178 gratuitos, no retener a los 60 que se fueron sin valor.