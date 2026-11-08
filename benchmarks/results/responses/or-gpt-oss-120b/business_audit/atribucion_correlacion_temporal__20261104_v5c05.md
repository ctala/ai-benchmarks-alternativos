# GPT-OSS 120B — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 8.86 | quality: 10.0
- latency_total: 41.396s | tokens_per_second: 29.4
- input_tokens: 275 | output_tokens: 1217

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

### Conclusión preliminar  

Con los datos que me has compartido **no se puede afirmar con certeza que la secuencia de 5 emails sea la causa del aumento de MRR y de las altas al plan pago**.  

Hay al menos **tres factores simultáneos** que cambiaron en marzo:

| Factor | Cuándo empezó | Qué aportó |
|--------|----------------|------------|
| **Secuencia de emails** | 1 marzo | Posible estímulo directo a usuarios gratuitos |
| **Publicidad pagada** | 3 marzo | $400 de gasto publicitario |
| **Mención de creador** | 12 marzo | Exposición a una audiencia externa |

El MRR pasó de $4 100 a $5 300 (+29 %) y las altas subieron de 9 a 14 (+56 %). Ese crecimiento es real, pero **no podemos des‑atribuirlo** a la secuencia de emails sin un análisis que controle los otros dos estímulos.

---

## ¿Qué falta para estar seguros?

1. **Grupo de control (o segmento de comparación)**  
   - Mantener una parte de los usuarios gratuitos sin recibir la secuencia de emails (o con una versión “placebo”).  
   - Comparar la tasa de conversión de este grupo con la del grupo que recibió los emails.

2. **Métricas de funnel por canal**  
   - **Tasa de apertura y click‑through** de cada email.  
   - **Conversión por email** (usuarios que pasan de gratuito a pago después de abrir / clicar).  
   - **Atribución** de conversiones a la publicidad (píxeles, UTM) y a la mención del creador (códigos de referencia, landing page dedicada).

3. **Análisis temporal**  
   - Graficar la evolución diaria/semanal de MRR, nuevas suscripciones y eventos de “upgrade”.  
   - Identificar picos que coincidan con cada intervención (p.ej., un salto justo después del 12 marzo podría indicar efecto del creador).

4. **Pruebas de significancia estadística**  
   - Aplicar pruebas de chi‑cuadrado o pruebas de proporciones para comparar la tasa de conversión entre grupos (email vs. control).  
   - Calcular intervalos de confianza para el incremento de MRR y para el número de altas.

5. **Modelos de atribución multicanal**  
   - Si dispones de datos de origen de cada usuario (UTM, referencia, origen de tráfico), usar un modelo de atribución (lineal, de posición, Shapley) para repartir el “valor” entre email, ads y mención del creador.

6. **Datos adicionales útiles**  
   - Número total de usuarios gratuitos al inicio y al final del mes.  
   - Número de usuarios que recibieron cada email (para descartar rebotes o direcciones inválidas).  
   - Coste de adquisición por canal (costo de los $400 de ads, posible comisión al creador).  
   - Ingresos recurrentes netos (descontando churn) para ver si el crecimiento es sostenible.

---

## Próximos pasos recomendados

| Acción | Qué implica | Por qué ayuda |
|--------|--------------|--------------|
| **Implementar un experimento A/B** | Dividir aleatoriamente a los usuarios gratuitos en “email” y “sin email”. | Permite estimar el efecto causal de la secuencia. |
| **Añadir tracking UTM y píxeles** | Cada enlace de los emails, ads y video debe llevar UTM único. | Facilita la atribución de cada conversión al canal origen. |
| **Recopilar métricas de email** | Open‑rate, click‑rate, conversion‑rate por cada envío. | Mide la efectividad directa del contenido. |
| **Analizar series temporales** | Visualizar datos diarios y aplicar modelos ARIMA o de intervención. | Detecta cambios estructurales coincidentes con cada acción. |
| **Calcular ROI por canal** | Ingresos atribuibles – coste del canal (ads, posible remuneración al creador). | Evalúa la rentabilidad de cada inversión. |

---

### Resumen corto

- **No podemos saber con los datos actuales si la secuencia de emails “funcionó”.**  
- El aumento de MRR y de altas podría deberse a la secuencia, a la publicidad, a la mención del creador, o a una combinación de los tres.  
- Necesitamos **experimentación controlada, tracking de origen y análisis estadístico** para aislar el efecto de los emails y confirmar su impacto.  

Una vez que tengas esos datos, podrás responder con confianza si la secuencia de emails es la palanca que buscas optimizar. ¡Éxitos con la medición!