# Muse Glimmer 30B — business_audit/churn_mezcla_free_y_pago

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 7.27 | quality: 8.0
- latency_total: 20.809s | tokens_per_second: 89.7
- input_tokens: 182 | output_tokens: 1867
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, abordando el problema de métricas mezcladas con soluciones prácticas.

## Respuesta completa

No es pánico, es un problema de definición de métrica. Tu panel está mezclando peras con manzanas.

El 31% que ves es churn **blended** de toda la base: 62 bajas / 200 inicio de mes = 31%.

El problema es que tu base no es homogénea. Estás midiendo churn de usuarios de pago con churn de usuarios gratuitos, y son dos fenómenos distintos.

### Qué está pasando realmente

Con los datos que exportaste:

**Plan Gratuito**
* Inicio mes: 178
* Bajas mes: 60
* Churn real gratuito = 60 / 178 = **33.7% mensual**

**Plan de Pago**
* Inicio mes: 22
* Bajas mes: 2
* Churn real de pago = 2 / 22 = **9.1% mensual**

Tu 31% es básicamente el churn del gratuito arrastrando la métrica. El churn que probablemente tenías en mente, el de pago, no es 5% pero tampoco es 31%. Está en 9.1% mensual.

Eso sí es grave. 9.1% mensual se anualiza en ~1 - (1-0.091)^12 = ~69% de churn anual. Es decir, retienes ~31% de tus pagadores al año. Para SaaS saludable se busca <5% mensual de churn de pago, ideal 2-3%.

El churn gratuito del 33% puede ser normal si es un embudo de auto-servicio. Mucha gente prueba y se va. Lo grave es que no lo estés midiendo separado.

### Plan inmediato

**Hoy, 24h: Para de reportar el número equivocado**
1. **Congela el KPI de churn blended.** No lo uses para decisiones. Define 2 KPIs oficiales:
   * Churn de pago mensual = bajas de pago / pagadores al inicio del mes
   * Churn de usuarios activos gratuitos mensual = bajas de gratuitos / gratuitos al inicio del mes
2. **Audita el panel.** Revisa cómo calcula churn. ¿Incluye usuarios que nunca se activaron? ¿Usuarios que se dieron de baja y volvieron? ¿Pruebas que expiraron? Asegúrate de que el denominador sea *usuarios activos al inicio del periodo* y no *usuarios totales creados*.
3. **Habla con los 2 pagadores que se fueron.** Es una muestra pequeña, puedes hacer winback 1:1. Pregunta: ¿Qué evento te hizo cancelar? ¿Qué alternativa usaste? ¿Qué te habría retenido? Es oro puro.

**Esta semana: Diagnóstico**
4. **Cohorte por fecha de alta.** El churn de 9.1% puede estar concentrado en usuarios nuevos. Calcula churn por cohorte de adquisición de pago de los últimos 3-6 meses.
5. **Segmenta el churn de pago.** Por plan, por canal de adquisición, por tiempo desde alta, por uso. ¿Los 2 que se fueron tenían bajo uso? ¿Se fueron en los primeros 30 días?
6. **Mapea el funnel gratuito -> pago.** Con 178 gratuitos y 22 de pago, tu conversión es baja. El churn alto de gratuitos puede ser bueno si filtra malos leads, o malo si estás perdiendo leads calientes. Mira cuántos gratuitos se activan en los primeros 7 días y cuántos llegan a *time to value*.

**30 días: Acción**
7. **Reduce churn de pago temprano.** Si las bajas son en <60 días, es problema de onboarding / valor percibido. Añade un check-in a día 14 y 30, onboarding guiado, y un *success plan* para nuevos pagadores.
8. **Reduce churn de pago tardío.** Si son usuarios maduros, es problema de valor / precio. Implementa encuestas de NPS/CSAT trimestral y un proceso de *save* antes de la cancelación.
9. **Decide qué hacer con el gratuito.** Si el gratuito es top of funnel, acepta un churn alto y optimiza por conversión a pago, no por retención gratuita. Si el gratuito es un plan de producto real, define un límite de inactividad y un programa de re-engagement.

Resumen: No estás perdiendo el 31% de tu negocio. Estás perdiendo el 9.1% de tus pagadores, que es casi el doble de lo que esperabas, y el 33.7% de tus gratuitos. Arregla la definición de métrica hoy y ataca el churn de pago con entrevistas a esos 2 usuarios.

¿Quieres que te ayude a armar la fórmula correcta para tu dashboard y un template de encuesta de salida para los pagadores?