# Claude Opus 5 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.63 | quality: 8.0
- latency_total: 44.634s | tokens_per_second: 64.8
- input_tokens: 262 | output_tokens: 2891

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

## Primero: el 31% no es tu tasa de churn

Es un promedio mezclado de dos poblaciones que no tienen nada que ver entre sí. Al separarlas:

| Segmento | Inicio de mes | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | **33,7%** |
| Pago | 22 | 2 | **9,1%** |
| Blended (lo que reporta el panel) | 200 | 62 | 31% |

El 31% está dominado por el plan gratuito, que es el 89% de tu base. Matemáticamente, tu métrica principal de retención está midiendo el comportamiento de gente que nunca te pagó. Eso no es una crisis de retención, es una métrica mal especificada.

## La parte incómoda: tampoco tienes evidencia de estar en 5%

Aquí es donde te pido que no te relajes del todo. Con 2 bajas sobre 22 usuarios, el intervalo de confianza del 95% va aproximadamente de **1% a 29%**. Con esa muestra, no puedes distinguir estadísticamente un churn del 5% de uno del 9% ni de uno del 15%. Un usuario más o menos mueve la cifra 4,5 puntos.

Traducción: no pasaste de "31% catastrófico" a "9% manejable". Pasaste de "una métrica equivocada" a "ninguna métrica confiable todavía". Es una mejora real, pero es distinta a la que probablemente quieres oír.

Y si el 9,1% resultara ser real y sostenido, no es trivial: compuesto, implica retener ~32% de los clientes de pago a los 12 meses. Un 5% mensual implicaría ~54%. La diferencia entre esas dos cifras es la diferencia entre un negocio que funciona y uno que no. Vale la pena averiguar cuál es.

## Plan

**Esta semana — arreglar la definición**

1. Separa el dashboard en dos métricas que nunca se promedien: `churn_pago` y `abandono_freemium`. Si tu herramienta no lo permite, calcúlalo en una hoja aparte y deja de mirar el número del panel.
2. Define qué significa "baja" para un usuario gratuito. ¿Canceló, borró la cuenta, o simplemente dejó de entrar? Si es inactividad, no es churn en ningún sentido útil: es un embudo de adquisición con fugas, y se gestiona con otras palancas.
3. Añade **churn de ingresos (MRR)** junto al churn de usuarios. Perder 2 clientes de $20 y perder 2 de $500 aparecen idénticos en tu panel actual. Necesito saber cuál fue.

**Próximas 2 semanas — conseguir señal**

4. Exporta los últimos 6–12 meses de churn de pago mes a mes. Un mes aislado con n=22 no dice nada; una serie de 12 meses sí muestra tendencia. Esto es lo único que va a resolver la ambigüedad del punto anterior.
5. Cohorta a los 178 usuarios gratuitos por fecha de registro. Si hubo un pico de altas hace 1–2 meses (lanzamiento, campaña, Product Hunt), ese 33,7% es el rebote esperado de curiosos, no un deterioro. Si las cohortes viejas también se están cayendo, es otra historia.
6. Habla con los 2 clientes de pago que se fueron. Con esa muestra, la entrevista cualitativa te dará más información que cualquier cálculo.

**Después — la pregunta que probablemente importa más**

7. Con 22 de 200 usuarios pagando, tu conversión free→paid es ~11%. A tu escala, es bastante probable que el cuello de botella esté ahí y no en la retención. Antes de reorganizar el roadmap alrededor del churn, mira cuántos de esos 60 abandonos gratuitos mostraban señales de intención de compra.

## Qué cambiaría mi lectura

- **Si el MRR perdido está concentrado en tu cliente más grande** → sube la prioridad, es riesgo de concentración, no churn promedio.
- **Si la serie histórica muestra 8–12% mensual de forma consistente** → sí es un problema estructural y hay que atacarlo.
- **Si los meses anteriores están en 0–4% y este es un pico** → ruido de muestra pequeña; documéntalo y sigue.
- **Si "baja" en el plan gratuito significa inactividad** → el 33,7% probablemente no significa casi nada.

Para poder afinarlo: ¿cuánto MRR representaban esas 2 bajas, y qué dice la definición de "baja" en tu herramienta?