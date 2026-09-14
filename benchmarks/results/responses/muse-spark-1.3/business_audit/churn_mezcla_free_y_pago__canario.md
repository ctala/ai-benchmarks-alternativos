# Muse Spark 1.3 — business_audit/churn_mezcla_free_y_pago

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 18.205s | tokens_per_second: 135.8
- input_tokens: 180 | output_tokens: 2472

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

Respira. No perdiste el 31% de tu negocio. Perdiste el 31% de una métrica mal construida.

Como analista de retención, lo primero que hago antes de interpretar un churn es preguntar: **¿qué población está midiendo realmente?**

Tu panel está mezclando peras con manzanas.

### 1. Lo que tu panel calculó

62 bajas / 200 usuarios inicio = **31%**. Matemáticamente correcto, gerencialmente inútil.

Porque tu base no es homogénea:

**Tu base a inicio de mes:**
* 178 gratuitos (89% de tus usuarios)
* 22 de pago (11% de tus usuarios)

**Tus bajas:**
* 60 gratuitos
* 2 de pago

Si lo segmentas, la historia cambia por completo:

**Churn Gratuito = 60 / 178 = 33.7%**
**Churn Pagado (Logo Churn) = 2 / 22 = 9.1%**

El 31% global está casi totalmente explicado por el plan gratuito: representan el 89% de la base pero el 96.8% de las bajas (60 de 62).

Estabas comparando 31% contra el 5% que tenías en mente. No son comparables. El 5% que recordabas seguramente era de pagados.

### 2. ¿Qué tan grave es entonces?

Mucho menos grave en ingresos, pero sí hay alerta.

**No es grave:** No perdiste 62 clientes que te pagan. Perdiste 2. Tu revenue no cayó 31%.

**Sí es grave:** Tu churn pagado es **9.1% mensual**, casi el doble de tu objetivo de 5%.

Para que lo sientas: un 9.1% mensual sostenido significa que en 12 meses solo te queda el 32% de una cohorte. Fórmula: `(1 - 0.091)^12 = 0.318`. Con 5% te quedaría el 54%. Con un SaaS sano (<3% mensual) te quedaría más del 69%.

Y ojo: con solo 22 clientes de pago, cada baja te mueve 4.5 puntos. Es volátil. Pasar de 1 a 2 bajas te llevó de 4.5% a 9.1%. No entres en pánico, pero sí actúa.

### 3. Tu plan en 3 fases

**HOY: Corrige el tablero**
1.  Deja de mirar el "churn total". Crea 2 métricas oficiales y separadas:
    * Logo Churn Pagado = bajas pagadas / pagados inicio
    * Churn Gratuito = bajas free / free inicio
2.  Define "baja" para free. ¿Se borraron o solo dejaron de entrar 30 días? En freemium, la inactividad no es lo mismo que una cancelación voluntaria. Eso infla el 33.7%.

**ESTA SEMANA: Rescata lo que importa (los 2 pagados)**
Tienes solo 2 casos, no necesitas machine learning, necesitas teléfono.
1.  Averigua quiénes eran: ¿pago fallido involuntario o cancelación voluntaria?
2.  Llámalos / escríbeles personalmente. Pregunta: ¿qué esperabas lograr y qué falló?
3.  Revisa uso previo: último login, tickets de soporte, uso de feature clave en los 14 días antes de irse.
4.  Aplica quick-win anti-churn: reintento de tarjetas (dunning), email de "¿todo bien?" a los 7 días sin uso, oferta de pausa en vez de cancelar.

**ESTE MES: Ataca la causa, no el síntoma**
1.  Para pagados: implementa MRR Churn y Net Revenue Retention, no solo conteo de logos. Un cliente grande que se va duele más que uno chico.
2.  Para gratuitos: no intentes bajar el 33.7% a 5%. Es normal que free churnee alto. Enfócate en: % de free que activan (llegan al "aha moment") y % que convierten a pago. Ahí está tu palanca.
3.  Haz cohortes: ¿esos 60 free se registraron este mismo mes y nunca activaron? Entonces no es un problema de retención, es de adquisición / onboarding.

En resumen: cambia tu titular mental de "perdimos 31%" a **"perdimos 2 de 22 pagados (9.1%). Es el doble de lo esperado, vamos a hablar con ellos y a arreglar el dashboard para no volver a asustarnos por los free."**

¿Quieres que lo hagamos juntos? Pásame si esas 2 bajas de pago fueron por fallo de tarjeta o cancelación, y vemos el guion de rescate.