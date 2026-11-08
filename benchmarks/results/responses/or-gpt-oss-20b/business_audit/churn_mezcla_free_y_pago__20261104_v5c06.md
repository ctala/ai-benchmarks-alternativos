# GPT-OSS 20B — business_audit/churn_mezcla_free_y_pago

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 6.49 | quality: 6.0
- latency_total: 10.035s | tokens_per_second: 175.7
- input_tokens: 216 | output_tokens: 1763

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

**Lo que realmente está midiendo tu panel**

| Métrica | Cálculo | Resultado |
|---------|---------|-----------|
| **Churn total** | \( \frac{62}{200} = 0.31 \) | **31 %** |
| **Churn plan gratuito** | \( \frac{60}{178} \approx 0.337 \) | 33.7 % |
| **Churn plan pago** | \( \frac{2}{22} \approx 0.091 \) | 9.1 % |

> **Conclusión:**  
> - El 31 % que reporta el panel es correcto y corresponde al **churn combinado** de usuarios gratuitos y de pago.  
> - Si tu expectativa era 5 % era porque estabas mirando el churn **solo de los usuarios de pago** (9 % ≈ 5 % cuando se redondea).  

---

## 1. ¿Qué tan grave es?

| Segmento | Usuarios | Churn | Comentario |
|----------|----------|-------|------------|
| Gratis | 178 | 33.7 % | Muy alto – indica problemas de **adopción** o de **valor percibido** para usuarios que no están pagando. |
| Pago | 22 | 9.1 % | Aún alto para un segmento de pago, pero mucho menor que el gratuito. |
| Total | 200 | 31 % | Por encima del mercado típico (1‑5 %) si tu producto es SaaS. |

**Impacto**  
- **Ingresos**: 2 bajas de pago en 22 usuarios → 9 % de **pérdida directa** de ingresos.  
- **Costes de adquisición**: Si cada nuevo usuario gratuito cuesta 10 € de marketing y el churn es 33 %, tu ROI se arruina rápidamente.  

---

## 2. Plan de acción inmediato (0‑30 días)

| Paso | Acción | Responsable | Tiempo | Impacto |
|------|--------|-------------|--------|---------|
| 1 | **Confirmar definición de churn** en el dashboard. Añadir una sección de “Definición de métricas” para que el equipo no confunda churn con “cancelaciones de pago”. | Equipo de datos | 1 día | Claridad |
| 2 | **Validar pipeline**: revisa la fuente de datos (CRM, base de datos interna) y el script de cálculo. | Data Engineer | 2 días | Precisión |
| 3 | **Crear segmentación por plan** en el panel (gratuito vs pago). | BI | 3 días | Visibilidad |
| 4 | **Investigación de causas raíz**:  
- Reunión con soporte: “¿Por qué se cancelan 60 usuarios gratuitos?”  
- Encuesta de salida a los 60 usuarios gratuitos. | Customer Success | 5 días | Insight |
| 5 | **Análisis de cohortes**: ¿Cuándo se cancelan los usuarios gratuitos? ¿Es un patrón de “trial → churn”? | Analista de Retención | 7 días | Estrategia |
| 6 | **Comunicación interna**: informar a marketing y producto sobre el churn real y la diferencia con la expectativa. | Retención Lead | 1 día | Alineación |

---

## 3. Plan de mitigación a medio y largo plazo (30 días – 6 meses)

| Área | Acción | Métricas Clave | Frecuencia |
|------|--------|----------------|------------|
| **Onboarding** | Rediseñar el funnel de onboarding para usuarios gratuitos: tutoriales, mensajes de valor y llamadas al plan de pago. | Tasa de activación (≥ 25 % en 7 días) | Mensual |
| **Valor percibido** | Añadir “feature highlight” y casos de éxito dentro de la app. | NPS en usuarios gratuitos (≥ 50) | Trimestral |
| **Upsell** | Implementar “Plan Básico” con precio medio (ej. 9 €/mes) para usuarios gratuitos que muestran alta actividad. | Tasa de conversión a plan básico (≥ 10 %) | Trimestral |
| **Pricing** | Revisar el precio del plan pago y la política de cancelación (e.g., “cancelación automática a 30 días”). | Churn plan pago (≤ 5 %) | Trimestral |
| **Retention Automation** | Crear campañas de email drip para usuarios a los 7, 14, 30 días de inactividad. | Open Rate > 20 %, CTR > 5 % | Mensual |
| **Feedback Loop** | Encuestas de salida cada 30 días, análisis de motivos y ajustes de producto. | Motivo principal de churn | Mensual |
| **A/B Testing** | Probar incentivos (descuento en la primera suscripción pagada) y compararlos con la tasa de churn. | Tasa de conversión | 1‑2 meses |

---

## 4. Próximos pasos concretos

1. **Revisar y documentar** la fórmula de churn que usa el panel.  
2. **Crear un tablero** que muestre:  
   - Churn por plan (gratuito vs pago).  
   - Tasa de cancelación de pago vs cancelación gratuita.  
   - Cohortes de usuarios por mes de ingreso.  
3. **Lanzar la encuesta de salida** a los 60 usuarios que se dieron de baja del plan gratuito para identificar motivos comunes.  
4. **Implementar una campaña de “retención de trial”**: ofrecer un descuento del 20 % en el plan de pago para los usuarios que cancelen después de 7‑14 días.  
5. **Monitorear** el impacto de cada acción en la métrica de churn en un dashboard actualizado cada 2 semanas.

---

### Resumen rápido

- **El 31 % es correcto**; tu error fue comparar con el churn de solo usuarios de pago.  
- El churn del plan gratuito es **muy alto** (33.7 %) y necesita atención inmediata.  
- Un plan de acción dividido en **verificación de datos, segmentación clara, investigación de causas, y estrategias de retención** te permitirá reducir el churn total a un rango competitivo (1‑5 %) en los próximos 6 meses.  

¿Te gustaría que te ayude a diseñar la encuesta de salida o a configurarla en tu herramienta de analytics?