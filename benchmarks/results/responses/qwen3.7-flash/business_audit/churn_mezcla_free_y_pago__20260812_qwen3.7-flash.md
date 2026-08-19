# Qwen 3.7 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 7.67 | quality: 8.0
- latency_total: 29.734s | tokens_per_second: 92.6
- input_tokens: 189 | output_tokens: 2752

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

No entres en pánico. Como analista de retención, mi primera regla es: **antes de interpretar cualquier número, verifica qué población está midiendo realmente**. En tu caso, el 31% no es un colapso operativo; es un artefacto de agregación.

### 🔍 Desglose real de la métrica
| Segmento | Usuarios inicio mes | Bajas | Churn real |
|----------|---------------------|-------|------------|
| **Gratis** | 178 | 60 | `60/178 ≈ 33.7%` |
| **Pago**   | 22  | 2  | `2/22 ≈ 9.1%` |
| **Global** | 200 | 62 | `62/200 = 31%` (mezcla poblaciones heterogéneas) |

**¿Por qué cambió del 5% al 31%?**  
Lo más probable es que tu dashboard anterior calculaba churn solo sobre la base de pago (o excluía gratis del denominador). Al incluir ahora toda la base en el mismo cálculo, el churn “global” se disparó artificialmente. Los usuarios gratuitos tienen una rotación naturalmente alta; mezclarlos con los pagados distorsiona la lectura.

### 📊 ¿Qué tan grave es?
- **Usuarios gratis (33.7%)**: Normal en modelos freemium. Entre 20-40% mensual es estándar. No indica fallo de producto, sino el costo natural de captar tráfico sin barrera de entrada.
- **Usuarios de pago (9.1%)**: Aquí sí hay señal de alerta. En SaaS/plataformas recurrentes, paid churn mensual saludable suele estar entre 2-5%. 9% requiere investigación inmediata, aunque sea solo 2 cuentas.
- **Impacto financiero**: Depende del ARPU. Si esos 2 pagos representan un % significativo de tu MRR, merece atención priorizada. Si son trial/conversión reciente, puede ser ruido estacional.

---

### 🛠️ Plan de acción inmediato (orden de prioridad)

#### 1. Segmenta el reporte YA
- Cambia la definición de churn en tu panel: `Churn = Cancelaciones / Activos al inicio DEL MISMO SEGMENTO`.
- Crea vistas separadas: `Churn Gratis`, `Churn Pago`, `Churn Cohorte` (si usas suscripciones recurrentes).
- Elimina el “churn global” como KPI principal; úsalo solo como referencia operativa baja.

#### 2. Audita las 2 bajas de pago (esta semana)
- Revisa: último login, uso de features clave, tickets de soporte, motivo de cancelación (survey o chat).
- Pregunta crítica: ¿se fueron por precio, falta de valor percibido, problema técnico o competencia?
- Si el patrón se repite ≥3 meses, activa un flujo de win-back o revisa onboarding de pago.

#### 3. Optimiza la retención de usuarios gratis (sin intentar “fijarla”)
- No busques bajar el churn gratis a 5%; es contraproducente y filtra leads calificados.
- Enfócate en **Time-to-Value**: ¿cuántos días median desde registro hasta la primera acción clave? Si >7 días, el churn será alto.
- Implementa triggers automáticos: email/campaña a día 3, 7 y 14 enfocados en la feature que convierte gratis → pago.
- Considera “soft churn”: bloquea funcionalidades premium tras X días de inactividad en lugar de dar de baja explícita.

#### 4. Ajusta tu stack de métricas de retención
Reemplaza o complementa el churn global con:
- `Paid Churn Mensual` (objetivo: <5%)
- `Free → Paid Conversion Rate` (mide si el funnel compensa la rotación gratis)
- `Net Revenue Retention (NRR)` o `Gross Revenue Retention` (captura expansion/churn real)
- `Cohort Retention` (mes 1, 2, 3) para ver si la calidad de adquisición mejora con el tiempo

#### 5. Configura alertas inteligentes
- Alerta automática si `Paid Churn > 6%` en 7 días.
- Alerta si `Free Churn > 40%` + `Conversion Rate < X%` (indica fuga sin filtrado de calidad).
- Nunca compares churn global entre meses si cambia la composición de la base.

---

### ✅ Resumen ejecutivo
- El 31% es un falso positivo por mezclar poblaciones. Tu producto no se rompió.
- La única señal roja real es el paid churn del ~9%. Ábalo con datos de comportamiento, no con volumen.
- Corrige la definición del dashboard hoy. La tranquilidad operativa vendrá de medir por segmento y seguir cohortes, no snapshots globales.

Si quieres, te ayudo a redactar la nueva fórmula de churn para tu BI, a diseñar el tracker de win-back para las 2 bajas de pago, o a definir los umbrales de alerta por segmento. Solo dime qué herramienta usas (Mixpanel, Amplitude, Metabase, custom DB, etc.) y te doy el SQL/query listo para copiar.