# Nemotron 3 Super — business_audit/atribucion_correlacion_temporal

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 6.81 | quality: 6.94
- latency_total: 20.759s | tokens_per_second: 62.3
- input_tokens: 243 | output_tokens: 1294

## Respuesta completa

**Conclusión preliminar:**  
Con la información disponible no podemos afirmar con certeza que la secuencia de 5 emails haya sido la causa del aumento de altas al plan pago (de 9 a 14) ni del crecimiento del MRR (+29 %). Los datos muestran una mejora, pero existen al menos dos factores externos que cambiaron simultáneamente y que podrían explicar todo o parte del efecto observado.

**Por qué no podemos atribuir el efecto únicamente a los emails**

| Factor | Qué cambió | Cuándo empezó | Posible impacto en conversiones |
|--------|------------|---------------|---------------------------------|
| Secuencia de emails (5 envíos) | Comunicación automática a usuarios free | 1 marzo | Potencialmente positivo, pero sin grupo de control no sabemos su efecto neto. |
| Publicidad pagada | $400 de inversión en ads | 3 marzo | Puede haber atraído nuevos visitantes y, por tanto, más oportunidades de upgrade. |
| Mención de un creador | Video con audiencia grande | 12 marzo | Generó un pico de visibilidad y posiblemente de registros de alta intención. |

Como los tres eventos se solapan en el mismo mes, cualquier aumento observado podría deberse a uno, varios o ninguno de ellos. Además, el número absoluto de upgrades es bajo (9 → 14), lo que hace que la variabilidad aleatoria sea relativamente grande.

**Qué haría falta para estar seguros**

1. **Grupo de control (A/B test)**  
   - Dividir aleatoriamente a los usuarios free en dos cohorts: uno que reciba la secuencia de emails y otro que no reciba ningún email (o reciba un email placebo).  
   - Comparar la tasa de upgrade (o el MRR generado) entre ambos grupos durante el mismo periodo.

2. **Medición de interacción con los emails**  
   - Tasa de apertura, clics y conversiones por cada email de la secuencia.  
   - Esto permite ver si los usuarios que realmente interactuaron con el contenido son los que upgrades.

3. **Análisis de cohortes temporales**  
   - Seguir a los usuarios que se dieron de alta en febrero y marzo y observar su comportamiento de upgrade semana a semana.  
   - Así se puede ver si el impulso ocurre inmediatamente después de cada email o se retrasa (lo que sugeriría influencia de la publicidad o la mención).

4. **Control de variables externas**  
   - Registrar el gasto diario en ads y el número de impresiones/clics atribuibles a esas campañas.  
   - Anotar la fecha y el alcance de la mención del creador (visualizaciones, tráfico referral).  
   - Incluir esas métricas como covariables en un modelo de regresión (por ejemplo, regresión logística de upgrade) para aislar el efecto del email.

5. **Tamaño de muestra suficiente**  
   - Con solo 5 upgrades adicionales, el intervalo de confianza alrededor de la diferencia es amplio.  
   - Un experimento que alcance, por ejemplo, al menos 30‑50 upgrades en cada brazo reduciría el error estándar y permitiría detectar efectos modestos (por ejemplo, un aumento del 10‑15 % en la tasa de conversión).

6. **Significancia estadística**  
   - Calcular un valor p o un intervalo de confianza para la diferencia en tasas de upgrade entre tratamiento y control.  
   - Si el intervalo incluye cero, no podemos rechazar la hipótesis nula de “sin efecto”.

**Qué podrías hacer ahora (antes de un experimento completo)**  

- **Desglosar los upgrades por fecha**: ver cuántos de los 14 upgrades de marzo ocurrieron antes del 3 marzo (antes de la ads), entre el 3‑12 marco (solo ads) y después del 12 marco (ads + mención). Si la mayoría se concentra después del 12 marco, la mención del creador podría ser el principal driver.  
- **Comparar con meses anteriores**: observar la tendencia de upgrades en enero y febrero (sin emails, sin ads, sin mención). Si la variación mensual habitual es de ±2 upgrades, entonces el salto de 9→14 podría estar fuera del ruido.  
- **Calcular el costo por upgrade atribuible a los emails** (si se asume que todo el aumento se debe a ellos): $0 de gasto directo en emails, pero habría que considerar el costo de oportunidad del tiempo de diseño y automatización.  

**Resumen ejecutivo**  
- Los datos muestran una mejora, pero no permiten aislar el efecto de la secuencia de emails debido a la simultaneidad de cambios en publicidad y una mención de influencer.  
- Para concluir con certeza se necesita un diseño experimental (A/B test) o, al menos, un análisis que controle explícitamente por los otros factores y cuente con un número suficiente de conversiones para reducir la incertidumbre estadística.  
- Hasta que se cuente con esa evidencia, la afirmación más rigurosa es: **no se puede saber si la secuencia de emails funcionó por sí sola**.