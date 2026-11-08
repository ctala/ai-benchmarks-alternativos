# Ling 3.0 Flash — business_audit/churn_mezcla_free_y_pago

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 67.69s | tokens_per_second: 33.3
- input_tokens: 221 | output_tokens: 2255

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

# 🔍 Parar. Respira. El 31% es un fantasma — vamos a desarmarlo.

---

## 1. La métrica que te asusta está midiendo la población equivocada

Tu panel calcula el churn así:

$$\text{Churn reportado} = \frac{62 \text{ bajas}}{200 \text{ usuarios totales}} = 31\%$$

Pero **mezcla dos poblaciones con comportamientos radicalmente distintos** en el denominador: 178 usuarios gratuitos y 22 de pago. Eso es como calcular la tasa de accidentes de un país sumando peatones y pilotos de F1.

### Lo que el panel **debería** mostrarte (y no muestra):

| Segmento | Base (inicio de mes) | Bajas | Churn real |
|---|---|---|---|
| **Pago** | 22 | 2 | **2 / 22 = 9,1%** |
| **Gratuito** | 178 | 60 | 60 / 178 = 33,7% |
| **Total (panel)** | 200 | 62 | 31% ← **métrica artificial** |

> **Conclusión técnica:** El 31% es un promedio envenenado. Tu churn de **pago real es ~9,1%**, no 31%. Tu cifra del 5% probablemente era —o debería ser— el churn de pago.

---

## 2. ¿Qué tan grave es, realmente?

### Churn gratuito (33,7%) — 🟡 No es urgente
Alto, pero **es la naturaleza del plan gratuito**: usuarios que se registran, prueban y se van sin compromiso. No representan pérdida de ingresos directos. Preocupación: baja.

### Churn de pago (9,1%) — 🟠 Sí es la métrica que importa
Un 9,1% mensual en pagos **es alto pero no catastrófico**. Contextualicemos:

- **< 3% mensual** → Excelente (SaaS saludable)
- **3-5% mensual** → Aceptable / en mejora
- **5-8% mensual** → Requiere atención
- **> 8% mensual** → ⚠️ Alarmante, must be investigated

**Tu 9,1% está en zona de alarma**, pero es **radicalmente diferente** al 31% que te asustó. No estás perdiendo un tercio de tu base — estás perdiendo 2 de 22 usuarios de pago.

---

## 3. Plan de acción (en orden de prioridad)

### 🔴 Inmediato (hoy)
| # | Acción | Por qué |
|---|---|---|
| 1 | **Identifica a los 2 usuarios de pago que se fueron.** ¿Quiénes son? ¿Cuándo se unieron? ¿Cuánto pagaban? | Sin saber a quién perdiste, no puedes entender por qué. |
| 2 | **Envía encuesta de salida (exit survey) a los 2 usuarios de pago + a 10-15 de los 60 gratuitos que se fueron activamente.** | Encuentra patrones: precio, falta de feature, onboarding, soporte. |
| 3 | **Cambia la métrica del panel:** churn de pago = bajas de pago / base de pago a inicio de mes. | Para que el panel no te vuelva a mentir. |

### 🟡 Corto plazo (esta semana)
| # | Acción | Por qué |
|---|---|---|
| 4 | **Segmenta el churn por cohorte de activación.** ¿Los que se fueron eran usuarios que nunca usaron la plataforma o que la usaban activamente? | Si nunca activaron → problema de onboarding. Si usaban y se fueron → problema de valor. |
| 5 | **Revisa si los 200 "usuarios" a inicio de mes eran todos realmente activos.** ¿Cuántos se conectaron al menos una vez este mes? | Si 100 de los 178 gratuitos nunca abrieron la app, el "churn real" se reduce drásticamente. |

### 🟢 Mediano plazo (próximos 30 días)
| # | Acción | Por qué |
|---|---|---|
| 6 | **Define dos dashboards:** uno de churn de pago (KP-1) y otro de churn gratuito. | Cada uno tiene drivers diferentes y no deben mezclarse. |
| 7 | **Establece un benchmark objetivo:** churn de pago < 5% mensual. | Para que "5%" deje de ser una sensación y sea una meta concreta. |
| 8 | **Evalúa si los 22 usuarios de pago son suficientes para sostecer el negocio.** Si el ARPU es bajo, puede que necesites convertir más gratuitos a pagos antes de reducir churn. | El churn de pago duele más si la base es pequeña. |

---

## 4. Resumen ejecutivo para ti

```
Pánico:     31% → era un promedio artificial (gratuitos + pagos juntos).
Realidad:   Churn de pago real = 9,1% (2 de 22)
            Churn gratuito = 33,7% (normal para ese segmento)

Gravedad:   🟠 Media-Alta en pagos — requiere acción, no pánico

Primer paso: Identificar a los 2 usuarios de pago perdidos
              y preguntarles POR QUÉ se fueron.
```

**No cambies nada todavía. Primero, entiende.** El 31% era un humo óptico. El 9,1% es el fuego real — y se puede apagar.