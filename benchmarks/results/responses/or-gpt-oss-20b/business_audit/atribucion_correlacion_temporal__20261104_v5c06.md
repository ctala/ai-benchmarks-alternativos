# GPT-OSS 20B — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 16.239s | tokens_per_second: 87.6
- input_tokens: 275 | output_tokens: 1423

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

**Conclusión preliminar**

Con la información que has compartido no podemos afirmar con certeza que la secuencia de 5 emails haya sido la causa del aumento de MRR y de las nuevas suscripciones al plan pago. El incremento del 29 % en MRR (de $4.100 a $5.300) y el aumento de usuarios pagados (de 9 a 14) ocurrieron en el mismo periodo en que introduciste:

1. la secuencia de emails para usuarios gratuitos,
2. un gasto de publicidad de $400, y
3. una mención de la comunidad por un creador de gran audiencia.

Estos tres factores son **contribuyentes potenciales** y, sin un análisis que los desagregue, no podemos descartar que alguna de las otras variables (publicidad, referencia externa, estacionalidad, cambios en el precio, mejoras de producto, etc.) haya sido la verdadera fuerza impulsora.

En otras palabras: **no se puede saber** con esta información si la secuencia de emails fue la responsable del crecimiento observado.

---

## Qué falta para estar seguros

Para poder atribuir el crecimiento a la campaña de emails (o a cualquier otro factor) necesitas una metodología que permita separar los efectos de cada variable. A continuación, te detallo los pasos y métricas que deberías recoger:

| Paso | Qué hacer | Por qué es importante |
|------|-----------|-----------------------|
| **1. Define un objetivo claro** | ¿Qué quieres medir? Por ejemplo: tasa de conversión de usuarios gratuitos a pagados, MRR incremental, número de nuevos usuarios pagados, etc. | Evita medir “algo” y luego interpretar los resultados de forma arbitraria. |
| **2. Crea un grupo de control** | Selecciona un subconjunto de usuarios gratuitos que no reciban la secuencia de emails (o que reciban una versión diferente). | Permite comparar directamente el comportamiento de los que recibieron la campaña con los que no, aislando su efecto. |
| **3. Implementa un diseño A/B (o multivariante)** | Envía la secuencia a un 50 % de los usuarios y mantén el otro 50 % sin cambios (o con un email de prueba). | Este experimento te dará una estimación de la diferencia de resultados atribuible a la campaña. |
| **4. Recoge métricas de engagement** | Abiertas, clics, tiempo de lectura, conversión por cada email y por la campaña completa. | Te permite ver si los usuarios realmente interactuaron con el contenido y dónde se pierden. |
| **5. Analiza la temporalidad** | Observa las métricas antes, durante y después de la campaña (por ejemplo, 2 semanas previas y 2 semanas posteriores). | Detecta si el crecimiento se alinea con la secuencia de emails y no con otra actividad externa. |
| **6. Controla las variables externas** | Registra cuándo se empezó la publicidad, cuándo se hizo la mención, y cualquier cambio de precio o producto. | Para poder excluir o ajustar su influencia en el análisis. |
| **7. Usa análisis estadístico** | Pruebas de hipótesis (t‑test, chi‑cuadrado) o modelos de regresión con variables de control (publicidad, referencia, etc.). | Determina si las diferencias son estadísticamente significativas y no producto del azar. |
| **8. Realiza un “difference‑in‑differences”** | Compara la evolución de los grupos de control y tratamiento antes y después de la campaña. | Este método ayuda a eliminar efectos de tendencia comunes. |
| **9. Segmenta por cohortes** | Observa cómo reaccionan usuarios que se unieron en diferentes momentos (febrero, marzo, etc.). | Evita mezclar usuarios que ya habían pasado por la campaña antes de que se lanzara. |
| **10. Documenta y repite** | Lleva un registro de cada experimento y revisa los resultados con nuevos lanzamientos. | La repetición mejora la confianza en la causalidad. |

---

## Qué puedes hacer ahora con la información disponible

Aunque no puedas afirmar causalidad, sí puedes hacer un **análisis descriptivo rápido** para detectar patrones:

1. **Comparar conversiones**  
   - Conversión febrero: 9 pagos / (número de usuarios gratuitos de febrero)  
   - Conversión marzo: 14 pagos / (número de usuarios gratuitos de marzo)  

   Si la tasa de conversión aumentó significativamente, podrías sospechar un efecto positivo, aunque sigue siendo un indicio.

2. **Correlación temporal**  
   - MRR antes: $4.100  
   - MRR después: $5.300  
   - Incremento de publicidad: $400  
   - Mencion externa: 12 marzo  

   Observa si el pico de MRR aparece justo después de la mención o después de la campaña de emails. La coincidencia no prueba causalidad, pero es útil como hipótesis inicial.

3. **Revisa métricas de email (si las tienes)**  
   - Tasa de apertura, clic, conversión a pago.  
   - Si la mayoría de los pagos provienen de usuarios que abrieron el email, podrías tener un indicio de influencia.

---

## Resumen

- **No se puede saber** con la información actual si la secuencia de emails fue la causa del aumento en MRR y suscripciones.
- Para llegar a una conclusión confiable necesitas un **experimento controlado** (A/B testing), métricas de engagement, y un análisis estadístico que controle las variables externas.
- Mientras tanto, puedes hacer un análisis descriptivo y preparar la infraestructura necesaria (segmentación, métricas, control de variables) para futuros experimentos que te permitan afirmar causalidad con mayor certeza.