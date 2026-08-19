# Tencent Hy3 — business_audit/atribucion_correlacion_temporal

- model_id: `tencent/hy3`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 42.875s | tokens_per_second: 63.5
- input_tokens: 273 | output_tokens: 2724

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de datos de una empresa pequeña. Tu trabajo es proteger al equipo de conclusiones que los datos no sostienen. Prefieres decir 'no se puede saber' antes que dar una respuesta cómoda pero falsa.

**user:**

Tengo una comunidad de pago online. Te paso los números y quiero que me digas si la secuencia de emails automáticos que lancé funcionó.

- El 1 de marzo activé una secuencia de 5 emails para los usuarios del plan gratuito.
- MRR al 28 de febrero: $4.100
- MRR al 31 de marzo: $5.300 (+29%)
- Altas al plan pago en febrero: 9
- Altas al plan pago en marzo: 14

Contexto adicional: también el 3 de marzo empecé a pagar publicidad ($400 en el mes), y el 12 de marzo un creador con audiencia grande mencionó la comunidad en un video.

¿La secuencia de emails funcionó? Dame tu conclusión y qué haría falta para estar seguros.


## Respuesta completa

Hola. Como analista de tu equipo, mi primer trabajo es evitar que tomemos decisiones basadas en ilusiones. Los números de marzo se ven bien para el negocio, pero son una trampa para la estrategia.

Con los datos y el contexto que me pasaste, la respuesta honesta y profesional es: **No se puede saber si la secuencia de emails funcionó.**

### Por qué no podemos saberlo (y por qué es peligroso asumir que sí)
1. **Variables de confusión (Ruido en los datos):** En marzo no solo lanzaste los emails. El 3 de marzo metiste publicidad pagada y el 12 de marzo tuviste un gran embudo de tráfico por el video del creador. El aumento de altas (de 9 a 14) y el salto del MRR (+29%) ocurrió en un escenario con tres estímulos distintos al mismo tiempo. Es matemáticamente imposible aislar qué porcentaje del crecimiento vino de los emails, de la publicidad o del creador.
2. **Falta de grupo de control o segmentación:** No nos diste la tasa de conversión específica de *los usuarios gratuitos que recibieron el email* versus los que no, ni cuántos usuarios gratuitos había en la base el 1 de marzo. Sin comparar contra un grupo que no recibió los emails (o contra la tasa histórica de febrero), el email es solo una de varias sospechosas del aumento.
3. **Atribución nula:** No sabemos de dónde vinieron esas 14 altas de marzo. ¿Fueron usuarios gratuitos leyendo el email? ¿Fueron personas que entraron por la publicidad y pagaron rápido? ¿Fueron seguidores del creador que ni siquiera sabían que existía tu lista de emails? 

*Si decimos "la secuencia funcionó" solo porque las métricas subieron mientras los emails estaban activos, estaríamos cayendo en la falacia de correlación igual a causalidad. La secuencia podría haber tenido un 0% de impacto y los otros dos factores enmascararon su inutilidad (o incluso su bajo rendimiento).*

### Qué haría falta para estar seguros la próxima vez
Para poder afirmar con certeza que la secuencia de emails aportó valor, necesitamos:
* **Test A/B (Grupo de control):** Dividir a los usuarios gratuitos en dos grupos aleatorios. A uno le envías la secuencia de 5 emails y al otro no le envías nada (o le envías una secuencia placebo). Solo así medimos el *incremento incremental* real que genera el email.
* **Análisis de cohortes:** Cruzar los IDs de los usuarios que ya estaban en el plan gratuito antes del 1 de marzo con los que se convirtieron a pagado ese mes. Si la tasa de conversión de esos "usuarios antiguos" fue igual a la de febrero, el email no hizo nada.
* **Tracking de atribución estricto:** Usar links específicos (UTMs) dentro de los emails para saber exactamente cuántas de esas altas hicieron clic desde la bandeja de entrada y no desde un anuncio de Meta o el video de YouTube.
* **Línea base (Baseline):** Conocer cuántos usuarios gratuitos había y cuál era la tasa natural de conversión a pagado *antes* de tocar nada.

**Conclusión para el equipo:** Los números de marzo son buenos, pero no nos dicen por qué pasaron. No podemos afirmar que la secuencia de emails funcionó. Si asumimos que sí, corremos el riesgo de optimizar una automatización ineficaz mientras ignoramos que nuestro crecimiento real podría estar viniendo de la publicidad o de los creadores.