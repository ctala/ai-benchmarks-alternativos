# GPT-OSS 120B — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 50.39s | tokens_per_second: 46.7
- input_tokens: 229 | output_tokens: 2354

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

## 1️⃣  ¿Qué está midiendo realmente el “churn 31 %”?

| Métrica que muestra el panel | Cálculo que está usando |
|------------------------------|--------------------------|
| **Churn reportado = 31 %** | **(Bajas totales / Usuarios al inicio del mes) × 100**  <br>→ 62 / 200 = 0.31 → 31 % |

**Población que está usando:** **TODOS** los usuarios que había al inicio del mes, **incluidos los que están en el plan gratuito**.  

En la mayoría de los negocios SaaS el churn que se comunica a la dirección se calcula **solo sobre la base de clientes de pago** (porque son los que generan ingresos). Por eso tenías la expectativa de “~5 %”.

---

## 2️⃣  Cálculo del churn real por segmento

| Segmento | Usuarios al inicio | Bajas en el mes | Churn (bajas / inicio) |
|----------|-------------------|----------------|------------------------|
| **Plan gratuito** | 178 | 60 | 60 / 178 = 33.7 % |
| **Plan de pago** | 22 | 2 | 2 / 22 = 9.1 % |
| **Total** (todos) | 200 | 62 | 31.0 % |

### Churn “relevante” (sobre clientes que pagan)

\[
\text{Churn Pago} = \frac{2}{22} \approx **9 %**
\]

Si la expectativa era ~5 %, el 9 % sigue siendo **alto**, aunque mucho menos catastrófico que 31 %.

---

## 3️⃣  ¿Qué tan grave es?

| Métrica | Umbral típico (SaaS B2C) | Situación actual |
|--------|--------------------------|-------------------|
| **Churn pago** | 3 % – 5 % (mensual) | **9 %** → casi el doble del rango saludable. |
| **Churn gratuito** | No siempre se rastrea, pero > 30 % indica que la mayor parte de los usuarios “prueba” y se va rápidamente. | **33.7 %** → normal en muchos modelos freemium, pero puede estar alimentando una escasa conversión a pago. |
| **Conversión de free → pago** | 2 % – 5 % mensual (dependiendo del producto) | Necesitamos calcularlo (ver paso 4). |

**Conclusión:**  
- El 31 % de churn global es **una métrica engañosa** porque incluye usuarios que nunca pagan.  
- El churn de los clientes de pago (9 %) es el que realmente impacta el ARR/MRR y **requiere acción inmediata**.  
- La alta tasa de churn en el plan gratuito sugiere problemas de onboarding, valor percibido o segmentación de la audiencia.

---

## 4️⃣  Primeros pasos de diagnóstico rápido

| Paso | Acción | Herramienta / Fuente | Resultado esperado |
|------|--------|----------------------|--------------------|
| **4.1** | Verificar **definición de churn** en el panel (¿incluye solo pagos o todos?). | Configuración del BI / documentación del dashboard. | Confirmar que el 31 % es “churn total”. |
| **4.2** | Calcular **tasa de conversión free → pago** del mes anterior y del mismo mes del año pasado. | Exportar tabla de usuarios que pasaron de free a pago en los últimos 30 días. | Saber si la pérdida de usuarios free está afectando la entrada de nuevos pagos. |
| **4.3** | Analizar **perfil de los 2 clientes que cancelaron** (fecha de adquisición, uso, tickets de soporte, plan contratado, motivo de baja). | CRM / tickets de soporte. | Identificar si hay un patrón (p. ej., problemas de facturación, falta de funcionalidades). |
| **4.4** | Revisar **eventos de uso** de los usuarios free que se fueron (última sesión, número de sesiones, features usadas). | Herramienta de analítica de producto (Mixpanel, Amplitude, Heap). | Detectar señales de “desengagement” antes de la baja. |
| **4.5** | Chequear **cambios recientes** en el producto, precios o comunicación (e‑mail, onboarding). | Historial de releases / changelog. | Ver si alguna modificación coincidió con el pico de bajas. |

---

## 5️⃣  Plan de acción inmediato (primeras 2 semanas)

| Área | Acción concreta | Responsable | KPI de seguimiento |
|------|----------------|-------------|---------------------|
| **5.1** **Comunicación interna** | Informar al equipo de producto y a leadership que el 31 % es “churn total”; el churn crítico es 9 % (pago). | Retention Analyst | Aprobación del plan y alineación. |
| **5.2** **Retención de pagos** | - Contactar a los 2 clientes que cancelaron (si no lo hicieron ya). <br>- Ofrecer una entrevista de salida y, si procede, un **upgrade de 1 mes gratuito** o **descuento** para intentar recuperarlos. | Customer Success / Account Manager | % de clientes recuperados (meta: al menos 1). |
| **5.3** **Mejora del onboarding free** | - Crear un “mini‑tour” de 5 min que muestre el valor clave del producto.<br>- Enviar un e‑mail de “primeros 7 días” con tips y casos de uso.<br>- Añadir un trigger de alerta cuando la actividad del usuario free caiga < 30 % de la media en los primeros 5 días. | Product Ops + Marketing | Reducción del churn free en 10 % en el próximo mes. |
| **5.4** **Incentivar la conversión** | - Lanzar una campaña **“Free → Pro”** con 14‑días de trial de una funcionalidad premium.<br>- Ofrecer un **descuento del 20 %** al 3er mes si convierten antes de 30 días. | Growth / Marketing | Incrementar la tasa de conversión free→pago en +2 pp (puntos porcentuales). |
| **5.5** **Monitoreo de métricas** | - Dashboard diario con: churn pago, churn free, conversion rate, número de usuarios activos (DAU/MAU) por segmento.<br>- Alertas cuando churn pago > 7 % o conversion < 2 % en 7 días. | Data Engineering | Detección temprana de nuevas anomalías. |

---

## 6️⃣  Plan de acción a medio plazo (30‑90 días)

| Objetivo | Acción | Responsable | Métrica de éxito |
|----------|--------|-------------|------------------|
| **Reducir churn pago a < 5 %** | - Implementar **programa de health scores** para clientes de pago (uso, tickets, NPS). <br>- Crear **check‑ins proactivos** (correo + llamada) para clientes con score bajo. | CS + Product Success | Churn pago ≤ 5 % al día 90. |
| **Aumentar conversión free→pago** | - Optimizar la **página de precios** (pruebas A/B de mensajes y precios). <br>- Introducir **referidos**: +1 mes gratis por cada amigo que se convierta. | Growth | Conversión ≥ 5 % mensual. |
| **Entender el churn free** | - Realizar **encuestas de salida** automáticas a usuarios que no inician sesión en 7 días. <br>- Analizar cohortes de usuarios free que se quedan > 30 días vs los que salen antes. | Research | Identificar 2‑3 causas principales de churn free. |
| **Mejorar la calidad de los datos** | - Definir **definiciones claras** de “usuario activo”, “baja”, “cliente de pago”. <br>- Documentar en el data‑dictionary y entrenar a todos los equipos. | Data Governance | Reducción de discrepancias de métricas en < 5 % de los reportes. |

---

## 7️⃣  Comunicación externa (si es necesario)

1. **Stakeholders internos** – Enviar un resumen ejecutivo (1 página) con:
   - Qué mide el churn actual (31 % total) y por qué es engañoso.
   - Churn pago real (9 %) y su objetivo (< 5 %).
   - Acciones inmediatas y timeline.

2. **Inversionistas / Board** – Si el churn pago afecta la proyección de ARR, preparar un breve “risk‑mitigation” que incluya el plan de retención y los indicadores que se monitorizarán.

---

## 8️⃣  Resumen rápido (para tu tranquilidad)

| Métrica | Valor actual | Umbral saludable | Acción crítica |
|---------|--------------|------------------|----------------|
| **Churn total (todos)** | 31 % | N/A (no es la métrica clave) | No es prioridad. |
| **Churn pago** | 9 % | ≤ 5 % | Contactar a los que se fueron, health‑score, check‑ins. |
| **Churn free** | 33.7 % | No se controla directamente, pero se busca ↓10 % | Mejorar onboarding, triggers de desengagement. |
| **Conversión free→pago** | (pendiente de cálculo) | ≥ 2‑5 % mensual | Campaña de trial premium + descuentos. |

**En pocas palabras:**  
- El número “31 %” está inflado porque incluye a usuarios que nunca pagan.  
- El verdadero problema es que **el 9 % de tus clientes de pago se fueron**, lo que está por encima del rango saludable.  
- Con un plan de **retención rápida (contactar a los que se fueron, health‑score, onboarding mejorado) y un programa de conversión** podrás volver a los niveles deseados en 2‑3 meses.

¡Ánimo! Con datos claros y acciones focalizadas, el churn se controla. Si necesitas ayuda para montar los dashboards o los scripts de health‑score, avísame y te paso ejemplos. 🚀