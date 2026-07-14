# GPT-5.6 Sol — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 21.872s | tokens_per_second: 34.6
- input_tokens: 224 | output_tokens: 757
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis exhaustivo y práctico para evaluar el impacto de la secuencia de correos electrónicos.

## Respuesta completa

## Conclusión

**No se puede saber con estos datos si la secuencia de emails funcionó.**

Los resultados de marzo son positivos:

- MRR: de **$4.100 a $5.300**, un aumento de **$1.200 (+29%)**.
- Altas de pago: de **9 a 14**, un aumento de **5 altas (+56%)**.

Pero no podemos atribuir ese crecimiento a los emails porque en el mismo mes comenzaron dos acciones adicionales:

- Publicidad desde el 3 de marzo.
- Mención de un creador desde el 12 de marzo.

Además, comparar febrero con marzo no controla estacionalidad, cambios en el número de usuarios gratuitos, bajas, cambios de plan u otros factores. El aumento de MRR tampoco tiene por qué provenir exclusivamente de esas 14 altas.

## Qué haría falta para estar seguros

La mejor opción sería un **experimento con grupo de control**:

1. Dividir aleatoriamente a los usuarios gratuitos elegibles en dos grupos comparables.
2. Enviar la secuencia a uno y no al otro.
3. Medir durante el mismo periodo:
   - Conversión a pago.
   - MRR generado.
   - Bajas o reembolsos.
   - Ingreso o LTV por usuario.
4. Calcular la diferencia entre grupos y su incertidumbre estadística.

También habría que registrar por separado:

- Número de usuarios gratuitos expuestos a los emails.
- Altas atribuidas a publicidad y su coste.
- Altas vinculadas a la mención del creador.
- Fecha exacta y fuente de cada conversión.
- Aperturas y clics, aunque estos indicadores por sí solos **no prueban impacto comercial**.
- Puente del MRR: nuevo MRR, expansión, contracción y churn.

Si ya no es posible crear un control, se puede hacer un análisis menos concluyente usando fechas de conversión, fuentes etiquetadas, cohortes históricas y tasas de conversión antes y después. Serviría para obtener indicios, pero no para demostrar causalidad.

**Veredicto:** marzo mejoró, y la secuencia pudo contribuir, pero los datos actuales no permiten afirmar que fue la causa ni estimar cuánto MRR incremental generó.