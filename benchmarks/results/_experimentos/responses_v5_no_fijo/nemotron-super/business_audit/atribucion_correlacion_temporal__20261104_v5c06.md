# Nemotron 3 Super — business_audit/atribucion_correlacion_temporal

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 33.848s | tokens_per_second: 48.9
- input_tokens: 243 | output_tokens: 1655

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

**Conclusión provisional:**  
Con la información disponible no podemos afirmar con certeza que la secuencia de 5 emails automáticos haya sido la causa directa del aumento de MRR y de las altas al plan pago en marzo. El incremento observado es coherente con lo que podría generar esa secuencia, pero también coincidió con otras iniciativas (publicidad pagada y una mención de un creador influyente) que pueden haber contribuido de forma independiente o sinérgica.

---

### Por qué no podemos estar seguros todavía

| Factor | Qué sabemos | Por qué dificulta la atribución |
|--------|-------------|---------------------------------|
| **Secuencia de emails** | Activada el 1 de marzo para todos los usuarios del plan gratuito. | No hay un grupo de control (usuarios que no recibieron los emails) para comparar su comportamiento. |
| **Publicidad pagada** | $400 invertidos en marzo (presumiblemente desde el 3 de marzo). | La publicidad puede haber generado tráfico nuevo y conversiones que no están vinculadas a la secuencia de emails. |
| **Mención de creador** | Video publicado el 12 de marzo con audiencia grande. | Un impulso puntual de visibilidad puede haber generado un pico de inscripciones y upgrades justo después de esa fecha. |
| **Estacionalidad / tendencias** | Sólo dos puntos de MRR (28 feb y 31 mar). | No podemos descartar variaciones mensuales habituales (p.ej., fin de mes, ciclos de facturación). |
| **Datos de conversión** | Solo conocemos el número total de altas al plan pago (9 → 14). | No sabemos cuántas de esas altas provinieron de usuarios que recibieron los emails, cuántas hicieron clic en ellos, ni el tiempo entre la apertura del email y la conversión. |

---

### Qué haría falta para estar seguros

1. **Experimento controlado (A/B test)**  
   - Dividir aleatoriamente a los usuarios del plan gratuito en dos grupos:  
     - *Grupo tratamiento*: recibe la secuencia de 5 emails.  
     - *Grupo control*: no recibe los emails (o recibe una secuencia placebo).  
   - Medir, durante el mismo periodo, la tasa de conversión a plan pago, el MRR generado y otros indicadores (open‑rate, click‑through‑rate, tiempo hasta conversión).

2. **Atribución detallada**  
   - Etiquetar cada email con UTM o identificadores únicos para rastrear clics y posteriores acciones en la plataforma.  
   - Registrar la fecha/hora exacta de cada apertura, clic y posterior upgrade.  
   - Así se puede calcular la **conversión atribuible a los emails** (p.ej., % de usuarios que hicieron clic y luego se suscribieron dentro de X días).

3. **Desagregar los efectos de publicidad y mención del creador**  
   - Mantener un registro diario de gasto publicitario, impresiones, clics y conversiones atribuibles a esos canales.  
   - Para la mención del creador, anotar el tráfico y las conversiones provenientes de ese video (por ejemplo, mediante enlaces de referencia o códigos promocionales únicos).  
   - Con esos datos se puede hacer un modelo de **atribución multicanal** (regresión lineal, modelo de Shapley value, etc.) para estimar la contribución incremental de cada fuente.

4. **Control de estacionalidad y tendencias de fondo**  
   - Comparar marzo con los mismos meses de años anteriores (si existen datos históricos) o con un promedio de varios meses previos para ver si el aumento del 29 % está fuera de la variabilidad esperada.  
   - Si se dispone de datos semanales o diarios, se pueden aplicar técnicas de series temporales (p.ej., ARIMA, Prophet) para estimar el efecto esperado sin intervención y luego medir el residuo atribuible a la secuencia.

5. **Métricas intermedias de la secuencia**  
   - Tasa de apertura, de clic, de clic‑a‑conversión por cada email.  
   - Tiempo medio entre el primer email y la conversión.  
   - Estos indicadores ayudan a diagnosticar si la secuencia está funcionando como se espera (p.ej., si los emails con mayor contenido de valor o prueba social generan más conversiones).

6. **Análisis de cohorte**  
   - Agrupar a los usuarios según la fecha en que se registraron al plan gratuito y observar su comportamiento de conversión a lo largo del tiempo, separando aquellos que recibieron la secuencia en su primer mes vs. aquellos que se registraron después de que la secuencia ya estaba activa.

---

### Resumen práctico para el próximo ciclo

| Acción | Qué hacer | Qué nos dará |
|--------|-----------|--------------|
| Lanzar A/B test de emails | 50 % de usuarios gratuitos reciben la secuencia; 50 % no reciben nada (o reciben un email neutro). | Medida aislada del efecto causal de la secuencia. |
| Taggear cada enlace de email | UTM_source=email_seq&utm_medium=email&utm_campaign=marzo2025. | Capacidad de rastrear clics y conversiones directamente a cada envío. |
| Separar tracking de ads y creador | Usar códigos promocionales diferentes (e.g., ADSMAR12, CREADOR12) o URLs únicas. | Cuantificación independiente de cada fuente de tráfico. |
| Recolectar datos diarios de MRR y conversiones | Construir un dashboard que muestre MRR nuevo, source, y métricas de email. | Visualización rápida de tendencias y detección de outliers. |
| Comparar con meses históricos | Calcular el crecimiento medio mensual de MRR y su desviación estándar. | Evaluar si el +29 % es estadísticamente significativo fuera de la variabilidad normal. |

Solo con ese nivel de detalle podremos afirmar con confianza si la secuencia de emails **funcionó**, cuánto contribuyó al aumento de MRR y si vale la pena escalarla, optimizarla o descartarla. Hasta entonces, la interpretación más honesta es: *la secuencia pudo haber tenido un impacto positivo, pero no podemos isolarlo de los otros estímulos de marketing que ocurrieron simultáneamente*.