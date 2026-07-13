# Qwen 3.6 Max — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 5.43 | quality: 6.0
- latency_total: 61.19s | tokens_per_second: 32.1
- input_tokens: 245 | output_tokens: 1964

## Respuesta completa

**Conclusión directa:**  
Con los datos que compartís, **no se puede saber** si la secuencia de emails funcionó. Atribuir el aumento de MRR o de altas a los emails sería una conclusión cómoda, pero los datos no la sostienen.

---

### 🔍 Por qué no se puede afirmar nada todavía

1. **Intervenciones simultáneas sin aislamiento:**  
   El 1/3 activaste emails, el 3/3 empezaste con publicidad ($400) y el 12/3 hubo una mención de un creador con audiencia grande. Los tres estímulos se solapan en el mismo período y cualquiera de ellos (o su combinación) pudo generar las altas adicionales.

2. **Falta de atribución:**  
   No hay datos que indiquen por qué canal llegó cada una de las 14 altas de marzo. Sin UTMs, parámetros de seguimiento o registro de origen, es imposible separar el efecto de los emails del de los ads o del video.

3. **Muestra demasiado pequeña y volátil:**  
   Pasar de 9 a 14 altas es un +56%, pero con N=14 la variabilidad natural es alta. Un par de altas más o menos por azar, estacionalidad o un usuario que recomendó la comunidad pueden explicar la diferencia sin que haya un efecto real de la secuencia.

4. **El MRR no mide conversiones de emails:**  
   El salto de $4.100 a $5.300 puede venir de nuevas altas, pero también de upgrades, menor churn, cambios de precio o renovaciones anticipadas. Sin desglose, el MRR es un indicador agregado que no responde a la pregunta específica.

---

### 📊 Qué haría falta para estar seguros (o al menos acercarnos)

| Qué se necesita | Por qué | Cómo implementarlo (versión ligera) |
|----------------|---------|-------------------------------------|
| **Atribución por alta** | Saber qué canal convirtió a cada usuario | UTMs en links de emails y ads, campo `source` en el checkout, o pregunta post-pago "¿Cómo nos conociste?" |
| **Métricas de la secuencia** | Evaluar si los emails siquiera se consumieron y generaron intención | Open rate, click rate, y conversiones atribuidas por email/paso de la secuencia |
| **Grupo de control o holdout** | Aislar el efecto real de los emails | Dejar un 10-20% de usuarios gratuitos fuera de la secuencia y comparar su tasa de conversión vs. el grupo expuesto |
| **Desglose del MRR** | Entender de dónde vino el ingreso | Separar MRR nuevo, expansion, churn y reactivaciones mes a mes |
| **Ventana de observación más larga** | Reducir ruido y captar el ciclo completo de conversión | Medir al menos 2-3 ciclos completos de la secuencia (ej. 60-90 días) antes de concluir |

---

### ✅ Siguiente paso práctico (sin sobrecargar al equipo)

1. **Activa atribución básica ya:** agrega `?utm_source=email_seq&utm_medium=automation&utm_campaign=free_to_paid` a todos los links de la secuencia. Haz lo mismo para ads y para el link que usó el creador.
2. **Extrae un reporte simple de marzo:** altas con su `source`, y métricas de la secuencia (opens, clicks, conversiones por email).
3. **Si es posible, pausa la secuencia para un 15% de nuevos gratuitos** durante abril y compara tasas de conversión a 30 días.
4. **No tomes decisiones de escala o presupuesto** hasta tener al menos 2 meses con atribución consistente y N > 30 altas/mes.

Si querés, pasame los datos de atribución y las métricas de la secuencia cuando los tengas y te hago un análisis con intervalos de confianza y comparación contra el grupo de control. Hasta entonces, la respuesta honesta es: **no se puede saber**. Y está bien. Es preferible a optimizar sobre un falso positivo.