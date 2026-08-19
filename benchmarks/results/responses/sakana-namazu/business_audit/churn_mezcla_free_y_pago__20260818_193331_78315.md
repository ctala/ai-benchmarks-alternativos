# Sakana Namazu — business_audit/churn_mezcla_free_y_pago

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 13.619s | tokens_per_second: 212.4
- input_tokens: 202 | output_tokens: 2892

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

Primero: **no es un 31% para tu negocio real**. Tu panel está mezclando dos poblaciones distintas y te está mostrando una métrica agregada que te distorsiona la realidad. Eso genera el pánico. Vamos a separar las señales.

---

### 1. Verificación de la población que estás midiendo

Tu panel calculó:
- **62 bajas / 200 usuarios totales = 31%**

Pero eso es matemáticamente correcto y estratégicamente **inútil** porque tu base tiene 89% de usuarios gratuitos y solo 11% de pagos. Las bajas se concentran en la población que no paga.

Si segmentas por plan (lo que debes hacer siempre), obtienes esto:

| Métrica | Total | Plan Gratuito | Plan de Pago |
|---------|-------|---------------|--------------|
| **Usuarios a inicio de mes** | 200 | 178 | 22 |
| **Bajas este mes** | 62 | 60 | 2 |
| **Churn real** | **31.0%** | **33.7%** | **9.1%** |

---

### 2. ¿Qué tan grave es?

No es homogéneo. Depende de qué plan sea tu motor de ingresos.

#### El churn de pago (~9.1% mensual)
- Si tu negocio es **SaaS B2B**, esto es **rojo**. Un 9% mensual anualizado ronda el 68% de churn anual. Eso destruye LTV y suele indicar problema de producto, onboarding o promise gap.
- Si es **B2C / freemium / contenido**, es **amarillo/naranja**. Sigues teniendo una fuga importante, pero no es la catástrofe que parecía el 31%.
- **Lo bueno:** solo perdiste 2 pagos. Es una muestra muy pequeña para afirmar una tendencia definitiva, pero no puedes ignorarla.

#### El churn gratuito (~33.7% mensual)
- Es alto, pero los usuarios gratuitos siempre hacen eso: se van sin fricción.
- Si tu modelo depende de convertirlos a pago, esto es un problema de **adquisición/activación/onboarding**, no tanto de "retención" tradicional.
- Si muchos de esos 178 free son cuentas inactivas, bots o registros nunca activados, el churn real de usuarios comprometidos es menor.

**Conclusión:** Tu negocio no se está cayendo a pedazos. Probablemente tienes un problema de filtro de calidad en la parte gratuita, y posiblemente un inicio de alerta en la parte paga.

---

### 3. Plan de acción inmediato (los próximos 7 a 30 días)

#### Paso 1: Separar métricas para siempre
Nunca más reportes un solo churn agregado si tienen comportamientos diferentes. Tu dashboard debe mostrar:
- **Churn de Revenue** (lo más importante)
- **Churn de Usuarios Pagos**
- **Churn de Usuarios Gratuitos (activos)**
- **Churn de Trial / Registrados nunca activos** (si aplica)

#### Paso 2: Audita esas 60 bajas gratuitas (prioridad alta)
Descarga la lista de los 60 usuarios que se fueron y responde:
- ¿Se registraron este mismo mes? (Si sí, es un problema de onboarding, no de retención).
- ¿Nunca activaron una función clave? (usuarios "muertos" que purgaron su cuenta).
- ¿Hubo un pico por una campaña de marketing reciente que trajo mala calidad de leads?
- ¿Fueron bots/spam? (Muy común en free).

**Objetivo:** Determinar si es churn o simple limpieza de cuentas fantasma.

#### Paso 3: Investiga las 2 bajas de pago como si fueran 200
Con solo 2 bajas, haz análisis cualitativo:
- ¿Cuánto tiempo tenían de antigüedad?
- ¿Por qué se dieron de baja? (mail directo, encuesta de salida, llamada).
- ¿Tenían algún patrón en común? (mismo plan, mismo canal de adquisición, mismo error de facturación).

Si tu base de pago es 22, perder 2 es una señal. Si el mes que viene pierdes 3 ó 4, se confirma la tendencia.

#### Paso 4: Revisa la ventana de medición
Verifica si tu panel calcula churn sobre **usuarios totales** o sobre **usuarios activos/recurrentes**.
- Si incluye a los 178 free sin filtro de actividad, tu denominador está inflado de baja calidad.
- Ideal: calcula churn sobre "usuarios activos el mes pasado y elegibles para renovar este mes".

#### Paso 5: Activa controles diferenciados
- **Gratuitos:** Implementa un "engagement filter". Si un free no hace X acción en Y días, no lo cuentes como activo para churn; o mejor aún, automatiza reactivación por email/notification.
- **Pagos:** Revisa los próximos 30 días. Identifica quiénes están en riesgo (menos login, fallas de pago, soporte reciente) y lánzales una campaña de retención proactiva.

---

### 4. ¿Y el 5% que esperabas?

Es muy probable que tu referencia del 5% correspondía a:
- **Churn de revenue**, o
- **Churn de únicamente usuarios pagos**, o
- **Un período anterior** donde tenías más usuarios y la base gratuita no dominaba tanto.

Si logras que el churn de pagos se estabilice en ~5% y limpias tu embudo gratuito, el "31%" del panel bajará drásticamente solo por efecto de dejar de mezclar población.

---

### Resumen ejecutivo para ti

- **Deja de mirar el 31%.** Es ruido estadístico generado por tu base gratuita masiva.
- **Tu verdadera métrica de salud está en el 9.1% de pagos.** Si de esos 22 usuarios depende tu negocio, ahí debes poner el miedo y la energía.
- **Prioridad 1:** Entender si esas 60 bajas gratuitas son falla de onboarding o purga natural.
- **Prioridad 2:** Investigar las 2 bajas de pago y monitorear con atención a los 22 de la base.

En retención, **la métrica agregada miente cuando la población es heterogénea**. Ya encontraste el error. Ahora arregla el dashboard antes de arreglar el producto.