# Qwen 3.7 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 7.68 | quality: 8.0
- latency_total: 37.278s | tokens_per_second: 72.4
- input_tokens: 189 | output_tokens: 2699

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

Calma. El susto viene de una **distorsión de población**, no de un colapso operativo. Como analista de retención, mi primera regla es: *antes de interpretar el % del churn, pregunto contra qué denominador se calculó y quiénes están dentro*.

Aquí está lo que realmente está pasando:

### 🔍 Desagregación de la métrica
| Segmento | Usuarios inicio mes | Bajas | Churn calendario |
|----------|---------------------|-------|------------------|
| Gratuito | 178                 | 60    | `60/178 ≈ 33.7%` |
| Pago     | 22                  | 2     | `2/22 ≈ 9.1%`    |
| **Global** | **200**           | **62**| **31%** (mezcla ambas poblaciones) |

El salto de ~5% a 31% no es un cambio de comportamiento real; es un efecto de **agregación sesgada**. Estás comparando dos grupos con ciclos de vida, motivaciones y sensibilidad al producto totalmente distintos.

---

### 🚦 ¿Qué tan grave es?
- **Plan gratuito:** Un churn del ~34% es típico en modelos freemium si incluyes usuarios de prueba, estacionales o que solo vinieron por contenido/evento. No es alarmante per se, pero sí indica que el filtro o la experiencia inicial puede estar dejando entrar tráfico no cualificado.
- **Plan pago:** Perder 2 de 22 usuarios es un **9.1% mensual**. En términos de MRR/ARR esto sí pesa (depende del ARPU), pero no es crisis estructural. Requiere investigación focalizada, no contención general.
- **Conclusión de severidad:** **Moderada**. No hay fuga masiva ni fallo técnico evidente. El riesgo real es si esas bajas son concentradas en una cohorte nueva, si vienen acompañadas de tickets de error/reclamos, o si el funnel free→paid está debilitándose.

---

### 📋 Plan de Acción (Faseado)

#### ⏱️ Inmediato (24-48h)
1. **Verificar ventana temporal:** Cruza las fechas de baja con tu log de despliegues, cambios de UI, ajustes de precios, campañas de email o integraciones externas. Busca picos concentrados.
2. **Contacto proactivo a los 2 de pago:** Llama o envía mensaje breve. Pregunta: *“¿Qué te llevó a cancelar?”* y *“¿Qué hubiéramos hecho diferente?”*. Registra la razón en un campo estructurado (precio, funcionalidad, soporte, competencia, cambio de necesidad).
3. **Aislar cohorts por antigüedad:** Separa las 62 bajas en: `<30 días`, `30-90 días`, `>90 días`. El churn en cohorts recién registradas suele ser ruido; en cohorts maduras es señal de producto o valor percibido.

#### 📈 Corto Plazo (1-2 semanas)
1. **Separar dashboards de churn:** Nunca midas “churn global” en producción. Crea vistas filtradas por:
   - Plan (Free/Paid/Enterprise)
   - Cohorte de registro
   - Canal de adquisición
   - Nivel de engagement (ej. sesiones/semana, features usadas)
2. **Análisis de triggers de baja:** Exporta comportamiento de los 62 usuarios en los 7 días previos a la cancelación. Frecuencia de uso, errores, tickets abiertos, intentos de upgrade, respuestas a onboarding. Identifica patrones recurrentes.
3. **Revisar conversión free→paid:** Si el churn gratuito es alto y el pago bajo, puede que el funnel esté perdiendo calidad. Evalúa: barreras de pago, tiempo hasta primer valor, claridad de propuesta, trial vs directo.

#### 🏗️ Largo Plazo / Estructura
1. **Política de reporting de retención:** 
   - Churn calendario (%) solo como indicador de flujo mensual.
   - Churn por cohorte como métrica de lealtad real.
   - Siempre segmentado por plan y antigüedad.
2. **Sistema de alertas tempranas:** Configura umbrales por segmento (ej. `Paid Churn >12% en 30d` o `Free Churn concentrado en cohorte <14d`). Evita sorpresas mensuales.
3. **Medición de impacto financiero:** Traduce cada baja a MRR perdido y LTV proyectado. Prioriza acciones según pérdida económica, no por volumen absoluto.

---

### 💡 Nota crítica de analista
El churn no es un número único; es un **termómetro segmentado**. Mezclar gratuitos y pagos en una sola tasa genera falsas alarmas o ceguera real. Tu próximo paso no es “bajar el 31%”, sino entender **qué cohorte, qué plan y qué trigger** mueve esa aguja.

Si quieres, pásame:
- Rango de fechas exactas de las 62 bajas
- Distribución por antigüedad (>30d vs <30d)
- ARPU promedio de los 2 usuarios pagados
Y te armo un análisis de cohortes + hipótesis de causa raíz en 1 página.