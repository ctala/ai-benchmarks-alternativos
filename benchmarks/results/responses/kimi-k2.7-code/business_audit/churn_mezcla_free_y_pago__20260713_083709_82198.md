# Kimi K2.7 Code — business_audit/churn_mezcla_free_y_pago

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.32 | quality: 7.2
- latency_total: 58.059s | tokens_per_second: 46.7
- input_tokens: 202 | output_tokens: 2710

## Respuesta completa

**Respuesta corta: no es tan grave como parece, pero sí necesitas separar las métricas.** El 31 % es un *churn de usuarios* fuertemente distorsionado por tu base gratuita. Tus pagos están en una situación distinta y debes actuar sobre ellos primero.

---

## 1. Reconstruye la métrica real

| Segmento | Base inicio de mes | Bajas | Churn real |
|----------|-------------------|-------|------------|
| Total    | 200               | 62    | **31,0 %** |
| Gratuitos| 178               | 60    | **33,7 %** |
| De pago  | 22                | 2     | **9,1 %**  |

- **El 97 % de las bajas (60 de 62) son usuarios gratuitos.** Solo el 3 % son pagos.
- Tu **churn de pago es 9,1 %**, no 31 %.
- Con solo 22 usuarios de pago, cada baja representa ~4,5 puntos porcentuales. Es una muestra pequeña; una o dos bajas más cambiarían mucho la tasa.

---

## 2. ¿Qué tan grave es?

### Lo que NO es grave (o es esperable)
- Que los gratuitos churnen a ~33 % no es raro si son leads de baja calidad, usuarios que nunca se activaron o que solo probaron la app.
- El 31 % total es una métrica “sucia” porque mezcla dos poblaciones con comportamientos muy distintos.

### Lo que SÍ puede ser grave
- **9,1 % mensual de churn en pagos es alto.** Si se mantuviera, anualmente retendrías solo ~32 % de tus clientes pagos (churn anualizado ≈ 68 %).
- **Depende del ingreso:** si esos 2 pagos representan mucho MRR o eran clientes grandes, el daño económico es mayor que el numérico.
- **La base de pagos es muy pequeña:** 22 clientes es frágil; una baja más y ya tienes un mes “catastrófico”.

---

## 3. Plan de acción

### A. Valida la métrica antes de alarmarte (hoy)
- ¿El denominador es correcto? ¿Los 200 son solo usuarios a inicio de mes o incluyen altas del mes?
- ¿Están contando como churn a usuarios gratuitos que nunca convirtieron? En muchos negocios eso es “abandon” más que churn.
- ¿Las bajas son cancelaciones reales o suspensiones por fallo de pago?
- ¿Hubo reactivaciones que no se contaron?

### B. Separa el dashboard
Reporta siempre:
- **Churn de logos totales** (para contexto).
- **Churn de pagos** (más crítico para negocio).
- **Churn de MRR/ARR** (ingresos, no usuarios).
- **Churn por cohorte** (mes de alta, canal, plan, tamaño).

### C. Actúa sobre los pagos (prioridad 1)
- **Contacta a los 2 usuarios que se dieron de baja:** encuesta corta, llamada o email personalizado. Entiende por qué se fueron.
- **Ofrece win-back:** descuento, plan anual, pausa de cuenta o llamada con el CEO/soporte.
- **Revisa a los 20 pagos restantes:** identifica señales de riesgo (bajo uso, tickets de soporte, próximos a renovar).

### D. Analiza los gratuitos (prioridad 2)
- Revisa el **onboarding**: ¿se activan? ¿completan la acción clave?
- Mide **churn por canal de adquisición**: quizá estás trayendo muchos usuarios de baja intención.
- Define si un usuario gratuito que no usa la app es realmente valioso. Considera no reportarlo como churn, sino como “inactivos”.

### E. Mejora la toma de decisiones
- Aumenta la base de pagos para que el churn sea estadísticamente más estable.
- Establece alertas tempranas: uso decreciente, fallos de pago, apertura de tickets.
- Crea **experimentos**: mejoras en onboarding, emails de retención, planes anuales con descuento.

---

## 4. Mensaje para stakeholders

> “Este mes tuvimos un churn aparente del 31 %, pero está dominado por usuarios gratuitos (60 de 62 bajas). El churn real de clientes de pago fue del 9,1 %. Estamos validando los datos, contactando a los 2 pagos que se fueron y revisando cohortes de activación. El foco está en proteger ingresos, no solo reducir el número de usuarios.”

---

## Próximos pasos en 24–48 horas

1. Validar con el equipo de datos la definición y denominador del churn.
2. Calcular el churn de MRR (necesitas ingresos por cliente).
3. Contactar a los 2 pagos cancelados.
4. Auditar onboarding y activación de los usuarios gratuitos.
5. Preparar un dashboard separado por segmentos.

Si me das los ingresos mensuales de cada plan o el valor promedio de los pagos, puedo ayudarte a calcular el **churn de ingresos** y la gravedad económica real.