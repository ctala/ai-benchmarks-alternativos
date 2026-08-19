# Ling 3.0 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 7.435s | tokens_per_second: 353.6
- input_tokens: 221 | output_tokens: 2629
- judge_score: 5.0 | justificación: 

## Respuesta completa

# Primero: respira. El 31% te está engañando.

El error más común en retención es **mirar la métrica blended sin segmentar la población**. Y tu panel está haciendo exactamente eso. Vamos a desarmarlo.

---

## 1. Qué está midiendo realmente ese 31%

| Segmento | Usuarios inicio | Bajas este mes | Churn real |
|---|---|---|---|
| **Plan gratuito** | 178 | 60 | **33.7%** |
| **Plan de pago** | 22 | 2 | **9.1%** |
| **Total mezclado** | 200 | 62 | 31.0% |

El 31% es un **promedio ponderado que mezcla dos comportamientos radicalmente distintos**. Está dominado por el plan gratuito (178 de 200 = 89% de la base), que tiene una volatilidad natural muy alta porque no hay compromiso financiero.

---

## 2. Qué tan grave es, por segmento

### 🔴 Plan de pago — ESTO SÍ ES UNA EMERGENCIA
- **9.1% mensual de churn** → si se sostiene, la tasa anualizada es ≈ **68.6%**
- Es decir: pierdes casi 7 de cada 10 clientes de pago al año
- Eso no es sostenible. Incluso un SaaS maduro rara vez supera 5-7% anual (≈0.4-0.6% mensual)
- Tu muestra es pequeña (n=22), así que 2 bajas ya representan un cambio significativo

### 🟡 Plan gratuito — MENOS URGENTE PERO CON SEÑALES
- 33.7% mensual suena espantoso, pero **el churn de usuarios free es inherentemente alto** en la mayoría de plataformas. La pregunta clave no es "¿es alto?" sino **"¿es más alto de lo normal para ti?"**
- Si antes estaba en un 20-25% y ahora subió a 33.7%, ahí sí hay un problema

---

## 3. La pregunta que debes responder AHORA

> ¿**Cuál era tu churn reportado anterior de 5%**: ¿lo estabas calculando sobre el total mezclado o solo sobre los de pago?

Porque cambia completamente el diagnóstico:

| Si el 5% anterior era... | Entonces... |
|---|---|
| **Blended total** | Pasaste de 5% a 31% → algo cambió drásticamente (¿evento, cambio de producto, campaña de adquisición tóxica?) |
| **Solo de pago** | El churn de pago pasó de 5% a 9.1% → deterioro real pero más gradual |

---

## 4. Plan de acción (en orden de prioridad)

### 🚨 Semana 1 — Contener el sangrado de pago
1. **Segmenta en tu panel el churn por plan desde hoy.** No tomes decisiones con el número blended.
2. **Identifica a los 2 usuarios de pago que se fueron:** ¿por qué se fueron? ¿fue precio? ¿experiencia? ¿competencia? Haz outreach directo si aún tienes contacto.
3. **Revisa el funnel de conversión gratuito → pago:** si los free se van antes de convertir, el problema no es retención sino activación.
4. **Revisa la adquisición del mes:** ¿llegaron usuarios free de baja calidad? ¿campaña nueva? ¿referidos sin filtro?

### 📊 Semana 2 — Entender el free churn
5. **Establece tu baseline histórico de churn gratuito.** Si siempre fue ~30% y ahora es 33.7%, es ruido. Si antes era 15%, hay un problema real.
6. **Mide el "activation rate" de los free:** ¿cuántos free users completan el primer valor real del producto? Si el churn de free correlaciona con baja activación, el problema es de onboarding, no de retención.

### 📈 Semana 3-4 — Métricas que importan
7. **Define tus métricas reales:**
   - **Paid Monthly Churn** → tu métrica de salud principal
   - **Free-to-Paid Conversion Rate** → tu métrica de crecimiento
   - **Free Voluntary Churn** → tu métrica de producto/activación
8. **Deja de reportar el churn blended.** Es una métrica engañosa que mezcla manzanas con naranjas.

---

## Resumen ejecutivo

| | ¿Qué pasa? | ¿Qué tan grave? |
|---|---|---|
| **Churn blended 31%** | Está inflado por la base gratuita | ⚠️ La métrica está mal definida, no necesariamente la situación |
| **Churn de pago 9.1%** | Pérdida real de ingresos | 🔴 **Crítico** — actúa ya |
| **Churn de free 33.7%** | Volatilidad esperada, pero revisa baseline | 🟡 Revisa si es normal para ti |

**No estás en crisis por el 31%. Estás en crisis porque 2 de 22 clientes de pago se fueron y eso es una tasa destructiva.** Enfócate ahí primero.

¿Quieres que te ayude a armar el análisis de *por qué* se fueron esos 2 usuarios de pago o a diseñar el nuevo dashboard segmentado?