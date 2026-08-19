# Sakana Namazu — business_audit/churn_mezcla_free_y_pago

- model_id: `sakana/sakana-namazu`
- success: True  | final: 7.28 | quality: 8.0
- latency_total: 9.187s | tokens_per_second: 222.9
- input_tokens: 202 | output_tokens: 2048

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

Respuesta corta: **no estás en un colapso del 31%, pero tienes un problema de lectura que puede matar tu estrategia si no lo corrés hoy.**

Vos pensaste que estabas en 5%. Tu plataforma te muestra 31%. Ambos números tienen razón de existir, pero **están midiendo poblaciones distintas**. Antes de entrar en pánico, hay que ver qué está viendo realmente cada métrica.

---

### 1. Verificación: qué está pasando realmente con tus datos

El cálculo del dashboard es matemáticamente correcto:

- 62 bajas / 200 usuarios = **31% churn de usuarios totales**

Pero tu negocio no vive de "usuarios totales"; vive de **usuarios que pagan**. Si desagregás por población (lo que un analista de retención debe hacer primero), la película cambia:

| Segmento | Base a inicio de mes | Bajas | Churn real del segmento |
| :--- | :--- | :--- | :--- |
| **Gratuitos** | 178 | 60 | **33,7%** |
| **Pagos** | 22 | 2 | **9,1%** |
| **Total** | 200 | 62 | 31,0% |

**Lo que te dice esto:**
- Tu churn **agregado de 31% es un artefacto matemático**. Está dominado por la enorme masa de usuarios gratuitos (89% de tu base).
- Tu churn **de clientes pagos es 9,1% mensual**. Esto no es 31%, pero tampoco es el 5% que esperabas. Es casi el doble de tu meta, y si se mantiene, anualizado te deja un churn de clientes (logo churn) de aproximadamente **68%** —_un número peligroso para cualquier SaaS_.

**Conclusión:** no es una catástrofe inmediata con fugas masivas de pagos, pero **sí es una alerta roja de retención** si querés escalar.

---

### 2. ¿Qué tan grave es?

- **Los 60 gratuitos que se fueron:** Depende de tu modelo freemium. Si el gratis es solo un embudo de conversión a pago, un churn del 33% puede ser ruido de usuarios que nunca activaron. Si el gratis es parte de tu estrategia de viralización o comunidad, es una sangría que reduce tu conversión futura.
- **Los 2 pagos que se fueron:** Son solo el 9,1% de tu reducida base de 22 pagos, pero son el **100% de tu pérdida de ingresos** este mes. En bases chicas, cada baja pesa una fortuna.

**Gravedad real:** Media-alta. Tenés un problema de **sample size** (22 pagos es muy poco para ser estadísticamente tranquilo) y de **dirección estratégica** ( probablemente estás mirando el indicador equivocado en tu dashboard).

---

### 3. Plan de acción (priorizado)

#### **Fase 1: Dejar