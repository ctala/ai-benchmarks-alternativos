# GLM 5.3 — business_audit/churn_mezcla_free_y_pago

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.89 | quality: 8.0
- latency_total: 65.303s | tokens_per_second: 67.9
- input_tokens: 177 | output_tokens: 4434

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

Respira. El 31% no es mentira, pero no está midiendo lo que tú crees. Vamos a verificar la población primero, como siempre.

## Qué está midiendo realmente ese 31%

Tu base es 89% gratuita (178/200). Cuando mezclas planes en un solo churn, el número blended es prácticamente el churn del plan gratuito disfrazado de métrica de negocio:

| Segmento | Base inicio de mes | Bajas | Churn real |
|---|---|---|---|
| Gratuito | 178 | 60 | **33.7%** |
| Pago | 22 | 2 | **9.1%** |
| Mezclado (tu panel) | 200 | 62 | 31% |

El 97% de tus bajas son usuarios gratuitos. Estás leyendo una métrica de tu funnel gratuito como si fuera el estado de tu negocio.

## Qué tan grave es: dos fuegos separados

**Gratuito (33.7%):** Alto, pero el churn gratuito suele serlo — no hay costo de salida y muchos se registran sin intención real. La pregunta que importa y el panel no responde: ¿esas 60 bajas son usuarios de su primer mes o usuarios con antigüedad? Si son mayormente nuevos, tienes un problema de activación/onboarding, no un colapso de retención. Son diagnósticos y remedios totalmente distintos.

**Pago (9.1%):** Este es el número que paga las cuentas, y como tasa es alta (si fuera real, anualiza a ~68% de churn anual). Pero son **2 usuarios de 22**. Con esa base, cada usuario mueve la métrica 4.5 puntos. El intervalo de confianza real va de ~2.5% a ~28%. No hagas estadística con n=2: lee esas 2 cancelaciones, habla con esos usuarios si puedes. Ahí está toda la información disponible.

## Sobre el misterio del 5%

Antes de confiar en cualquiera de los dos números: ¿de dónde salía el 5%? Hipótesis probable: antes mirabas churn solo de pago. 1 baja entre ~20 pagos = 5% exacto. Encaja perfecto. Verifica si el panel cambió de denominador (empezó a incluir gratuitos) o si tú cambiaste de vista.

## El plan

**Hoy:**
1. Confirma consistencia numerador/denominador: ¿las 62 bajas son todas del grupo de 200 a inicio de mes, o el panel está contando bajas de usuarios que se registraron y se fueron dentro del mismo mes? (Error clásico que infla churn.)
2. Grafica las 62 bajas por día. Si se acumulan en fechas específicas, busca el disparador: un email, una caída, un cambio de precio, una actualización.
3. Rastrea el origen del 5% anterior.

**Esta semana:**
4. Parte las 60 bajas gratuitas por antigüedad. Primera cohorte vs. usuarios con más de 30/90 días. Esto define si tu problema es activación o producto.
5. Revisa individualmente las 2 bajas de pago. Razones, momento del ciclo de vida, patrón común.
6. Verifica la definición de "baja" en gratuito: ¿borrado de cuenta o inactividad? ¿El denominador incluye gente que nunca activó? Ambas decisiones cambian el número radicalmente.

**Estructural:**
7. Elimina el churn mezclado del panel. Reporta por plan, siempre.
8. Para gratuito, deja de vigilar churn bruto y mide: tasa de activación de nuevas cohortes, retención D7/D30, y conversión gratuito→pago.
9. Para pago, con 22 usuarios, mantén un tracker individual de cuentas. La tasa mensual será ruido durante meses.

## Veredicto

No es una emergencia del 31%. Son dos cosas menores que el panel mezcló en una crisis: probablemente un problema de activación en gratuito (a confirmar con cohortes) y una base de pago demasiado pequeña para medir con tasas — lo que significa que esta semana tu mejor herramienta de retención es una llamada, no un dashboard.