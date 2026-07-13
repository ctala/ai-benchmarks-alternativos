# Nemotron 3 Nano 30B — business_audit/atribucion_correlacion_temporal

- model_id: `nvidia/nemotron-3-nano-30b-a3b`
- success: True  | final: 7.09 | quality: 7.2
- latency_total: 24.674s | tokens_per_second: 79.8
- input_tokens: 243 | output_tokens: 1968

## Respuesta completa


**Conclusión provisional:**  
**No se puede afirmar con certeza que la secuencia de 5 emails automáticos haya sido la causa principal del aumento de MRR.** Los datos disponibles muestran una coincidencia temporal (el salto de $4.100 a $5.300 ocurre entre el 28 feb y el 31 mar), pero también hay otros eventos concurrentes que pueden haber influido de forma decisiva.

---

## 1. Qué muestra la información disponible

| Variable | Valor | Comentario |
|----------|-------|------------|
| MRR 28 feb | **$4.100** | Base antes de cualquier intervención |
| MRR 31 mar | **$5.300** | +29 % respecto a febrero |
| Altas plan pago feb | **9** | 9 usuarios que pasaron a plan pago en febrero |
| Altas plan pago mar | **14** | 5 usuarios más que en febrero (≈ 55 % de crecimiento) |
| Inversión publicidad (mar) | **$400** | Gasto iniciado el 3 mar |
| Mención en video (mar) | **Sí** | Creación de contenido por creador con gran audiencia el 12 mar |

### 1.1. Crecimiento de usuarios de pago
- **9 → 14 altas** = +5 usuarios en un mes, lo que representa un **55 % de aumento** en el número de suscriptores.
- Este aumento es **sustancial**, pero el número absoluto sigue siendo bajo (14 suscriptores totales). Por lo tanto, el impacto en MRR depende fuertemente del **valor medio de cada suscripción**.

### 1.2. Posibles impulsores simultáneos
1. **Publicidad pagada** (3 mar, $400).  
   - Puede haber generado tráfico nuevo que se tradujo en altas adicionales.
2. **Mención en video** (12 mar).  
   - Un creador con gran audiencia puede haber dirigido cientos o miles de vistas a la comunidad, generando conversiones fuera de la secuencia de emails.
3. **Secuencia de emails** (activada 1 mar).  
   - Los emails se envían **automáticamente** a los usuarios gratuitos en los primeros días del mes, pero no hay datos de apertura, clics o conversiones asociados a esa campaña.

### 1.3. Magnitud del efecto económico de la publicidad
- $400 invertidos en publicidad → +$1.200 de MRR (5.300 – 4.100).  
- El **ROI** implícito sería aproximadamente **3×** (1 200 / 400).  
- Si la publicidad generó al menos 3‑4 nuevos suscriptores (dependiendo del precio medio), su efecto puede ser mayor que el de la secuencia de emails.

---

## 2. Qué falta para atribuir el crecimiento a la secuencia de emails

| Necesidad | Por qué es indispensable |
|-----------|--------------------------|
| **Datos de interacción de la secuencia** (tasa de apertura, clics, conversiones atribuibles) | Sin saber cuántos usuarios recibieron cada email, cuántos los abrieron y cuántos convirtieron, no podemos estimar su contribución directa. |
| **Segmentación de los 5 nuevos suscriptores** (¿todos provienen de la lista de emails gratuitos? ¿De tráfico externo?) | Si la mayor parte de los nuevos usuarios llegó por la mención en video o por anuncios, el email no tendría un rol decisivo. |
| **Análisis de cohortes**: comparar la tasa de conversión de los usuarios gratuitos que **recibieron** el email vs. los que **no lo recibieron** (por ejemplo, usuarios que se registraron después del 1 mar). | Permite aislar el efecto del email de otros factores externos. |
| **Control de variables temporales**: registrar cuándo cada alta ocurrió y si coincidió con envíos de email (p.ej., si la alta ocurrió 2‑3 días después del primer email). | Si las altas se concentran justo después del envío, sugiere causalidad; si están distribuidas aleatoriamente, la correlación es más débil. |
| **Valor medio de suscripción** (ARPU) antes y después del período. | Si el aumento de MRR se debe a usuarios de mayor ticket, puede deberse a cambios en la oferta o precios, no al email. |
| **Testing A/B** o experimento controlado. | La única forma de probar causalidad de manera rigurosa es dividir a la población en dos grupos (email vs. sin email) y comparar resultados. |

En ausencia de esa información, cualquier afirmación que atribuya el +29 % de MRR al “éxito de la secuencia de emails” sería **especulativa**.

---

## 3. Qué hacer para estar seguros

1. **Recolectar métricas de la campaña de email**  
   - Tasa de apertura, clics, CTA, tiempo de lectura.  
   - Número de conversiones atribuidas a cada email (idealmente con *UTM* o enlaces de seguimiento).  
   - Segmentar por **fecha de alta** para ver si los usuarios que se convirtieron lo hicieron dentro de las 48 h posteriores al envío.

2. **Crear un experimento controlado**  
   - **A/B test**: mantener la secuencia para un subconjunto de usuarios (p.ej., 50 %) y eliminarla o modificarla para el otro 50 %.  
   - Medir diferencias en conversiones, ARPU y churn a 30‑60 días.

3. **Implementar tracking de origen**  
   - UTM en los enlaces de la bio, landing pages y anuncios.  
   - Asignar cada alta a su canal de adquisición (email, publicidad, video, redes orgánicas).  
   - Así se podrá cuantificar el % de altas provenientes de cada fuente.

4. **Analizar cohortes por mes**  
   - Comparar la tasa de conversión de usuarios gratuitos de febrero vs. marzo, ajustando por número de emails enviados.  
   - Si la tasa de conversión se mantiene estable, el aumento de MRR probablemente se deba a factores externos (publicidad/video). Si mejora significativamente, el email tendría un efecto positivo.

5. **Monitorear el valor de cada suscriptor**  
   - Calcular el **ARPU** antes y después del período.  
   - Si el ARPU sube, puede deberse a upgrade a planes más caros, lo cual no está directamente ligado al email.

6. **Documentar hipótesis y pruebas**  
   - Registrar cada variable y resultado en un *tracker* (Google Sheet, Notion, etc.).  
   - Al final de cada mes, revisar si las hipótesis iniciales se confirmaron o refutaron.

---

## 4. Resumen rápido para tu decisión

| Pregunta | Respuesta basada en datos actuales |
|----------|--------------------------------------|
| **¿La secuencia de emails funcionó?** | **No se puede confirmar**. El crecimiento de MRR coincide con otros eventos (publicidad, mención en video) y no contamos con métricas de rendimiento de la campaña de email. |
| **¿Qué necesitamos para estar seguros?** | Datos de interacción (apertura/clics/conversiones), segmentación de altas por canal, experimento A/B o análisis de cohortes que aísle el efecto del email. |
| **Próximos pasos recomendados** | 1) Implementar tracking UTM y registrar conversiones por origen. 2) Ejecutar un test A/B con y sin la secuencia. 3) Analizar cohortes y ARPU para cada canal. 4) Revisar resultados antes de atribuir el crecimiento a la campaña de email. |

---

### Mensaje clave

> **“Los números parecen positivos, pero sin datos de rendimiento de la secuencia de emails no podemos afirmar que haya sido la causa del aumento de MRR. Para validar su impacto, necesitamos medir directamente cuántos usuarios convertidos lo hicieron a raíz del email y compararlo con un grupo de control.”**

Si logras obtener esa evidencia, entonces sí podrás decir con confianza que la secuencia de emails “funcionó”. Hasta entonces, considera los demás factores (publicidad y contenido externo) como los principales impulsores del crecimiento reciente. ¡Éxitos en la siguiente fase de análisis!