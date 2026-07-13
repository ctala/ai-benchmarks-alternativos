# Qwen 3.5 397B (NIM) — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 5.61 | quality: 6.0
- latency_total: 46.921s | tokens_per_second: 43.6
- input_tokens: 245 | output_tokens: 2048

## Respuesta completa

**Conclusión directa: No se puede saber.**

Con los datos actuales, es estadísticamente irresponsable atribuir el crecimiento a la secuencia de emails. Afirmar que funcionó sería una falacia de *post hoc ergo propter hoc* (después de esto, por lo tanto, a causa de esto).

Aquí está el porqué, desglosado por riesgos de interpretación:

**1. Variables confusas simultáneas (El problema principal)**
Lanzaste tres intervenciones de crecimiento en un窗口 de 12 días:
*   **1 de marzo:** Emails (a base de usuarios existentes).
*   **3 de marzo:** Ads (tráfico nuevo/frío).
*   **12 de marzo:** Influencer (tráfico nuevo/caliente por confianza).

El aumento de MRR (+$1.200) y de altas (+5) es el resultado agregado de las tres. Es muy probable que el influencer (audiencia grande + confianza) tenga un peso mucho mayor que un email automatizado a usuarios que ya estaban en modo "gratuito". Sin atribución, asumir que fueron los emails es ignorar el elefante en la habitación (el video viral).

**2. Tamaño de la muestra insuficiente**
Pasaste de 9 a 14 altas. Una variación de 5 unidades en muestras pequeñas tiene una desviación estándar alta. Podría ser ruido natural, estacionalidad (inicio de mes) o el efecto de las acciones mencionadas. No hay significancia estadística clara solo con estos dos puntos de datos.

**3. Falta de métricas de proceso (Funnel)**
Solo estamos mirando el resultado final (output), no el proceso (input).
*   ¿Cuál fue el *open rate* y el *CTR* de los emails?
*   ¿Cuántos clicks hubo hacia la página de pago desde los emails?
*   Si el CTR fue bajo pero las ventas subieron, es evidencia de que **no** fueron los emails.

---

### ¿Qué haría falta para estar seguros?

Para proteger la toma de decisiones futuras y no gastar presupuesto en una estrategia que quizás no funciona, necesitarías implementar lo siguiente:

1.  **Atribución por UTM y Eventos:**
    *   Cada enlace en los emails debe tener UTMs únicos.
    *   En el checkout, debes capturar `source/medium`.
    *   Necesitas saber: De las 14 altas, ¿cuántas vinieron directamente de un click en el email vs. vs. tráfico directo (influencer) vs. ads?

2.  **Grupo de Control (A/B Testing):**
    *   La única forma científica de saberlo es **no enviarle los emails a una parte aleatoria de los usuarios gratuitos** (ej. 20%) y comparar la tasa de conversión de ese grupo contra el grupo que sí recibió los emails. Si ambos convierten igual, los emails no aportan valor.

3.  **Análisis de Cohortes y Tiempo:**
    *   Graficar las conversiones por día. ¿Hubo picos los días que se enviaron los emails o el pico fue el 13-14 de marzo (post-influencer)?
    *   Comparar la tasa de conversión de usuarios gratuitos a pagos de *este* marzo vs. meses anteriores sin campañas.

4.  **Encuesta de Salida/Entrada:**
    *   Añadir un campo opcional en el checkout: "¿Qué te motivó a comprar hoy?". Las opciones deben incluir "Recibí un email", "Vi un video de [Influencer]",