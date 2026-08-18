# Seed 2.1 Turbo — business_audit/teardown_competidor_sin_inventar

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 2.95 | quality: 2.0
- latency_total: 33.21s | tokens_per_second: 61.7
- input_tokens: 232 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa


El usuario pide un teardown de competidor, se realizará con datos públicos limitados. Se estructurará en tres bloques con indicación de certeza: datos confirmados, estimaciones de facturación y salud del negocio, y estrategias de competencia. Empezaré por recopilar los datos confirmados que me has proporcionado sin interpretación.

En los datos confirmados, solo se señalará que se muestran 2.400 miembros en la portada, sin interpretar que son miembros activos pagos para evitar confusiones. Para el bloque de estimaciones de facturación y salud del negocio, se elaborarán escenarios pesimista, base y optimista, ya que no se dispone de información unívoca sobre el tipo de miembros mostrados.

Se han incorporado más parámetros para los escenarios de estimación: el precio visible es de $39/mes sin plan anual, los 12 cursos publicados no se han verificado como finalizados, el fundador cuenta con 60.000 seguidores que suponen la principal fuente de tráfico, y la tasa de conversión promedio del nicho oscila entre el 0,5% y el 2%. Se ha definido el rango de conversión de seguidores a miembros pagos: 300 a 1.200. Se ha establecido el rango de churn mensual para comunidades de pago del nicho de creadores, y se ha aclarado que la frecuencia de publicaciones de contenido público no permite inferir la cadencia de contenido interno de forma fiable.

Se ha definido la estructura de los escenarios de estimación de facturación, con un aviso previo de que no es posible calcular la facturación exacta por la falta de datos clave. Se ha definido el escenario pesimista con sus correspondientes supuestos y niveles de certeza, y se ha añadido el supuesto adicional de que la antigüedad del negocio se sitúa entre 1 y 3 años, lo común para creadores con 60.000 seguidores en el nicho de automatización.

Se ha simplificado el cálculo del escenario pesimista: se asume que los miembros activos pagos suponen el 25% del total de miembros históricos mostrados, lo que genera un MRR de $23.400 y un ARR de alrededor de $280.800.

El escenario base (40% de certeza, el rango más probable) se ha definido con tres supuestos confirmados: los 2.400 miembros mostrados incluyen 1.200 activos pagos (el resto son registros históricos inactivos), el 30% de los miembros pagan el 20% menos por el plan anual, y la tasa de abandono mensual se sitúa entre el 4% y el 5%.
