# Ling 3.0 Flash — sales_outreach/campaign_optimization

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.17 | quality: 10.0
- latency_total: 31.895s | tokens_per_second: 79.4
- input_tokens: 340 | output_tokens: 2531

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estos resultados de mi campana de Google Ads del ultimo mes:

Campana A (Landing principal):
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100
- Keywords: "software gestion inventario", "inventario pymes"

Campana B (Blog content):
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800
- Keywords: "como gestionar inventario", "problemas inventario restaurante"

Campana C (Competidor):
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200
- Keywords: "alternativa a [competidor]", "[competidor] vs"

Mi presupuesto total es $5,000/mes.

1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?


## Respuesta completa

# 📊 Análisis Completo de tu Campaña de Google Ads

---

## 1. Métricas Calculadas por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** (Clics / Impresiones) | 1,500 / 50,000 = **3.00%** | 4,800 / 120,000 = **4.00%** | 900 / 15,000 = **6.00%** |
| **CPC** (Costo / Clics) | $2,100 / 1,500 = **$1.40** | $1,800 / 4,800 = **$0.375** | $3,200 / 900 = **$3.56** |
| **CPA** (Costo / Signups) | $2,100 / 45 = **$46.67** | $1,800 / 24 = **$75.00** | $3,200 / 36 = **$88.89** |
| **Conversion Rate** (Signups / Clics) | 45 / 1,500 = **3.00%** | 24 / 4,800 = **0.50%** | 36 / 900 = **4.00%** |
| **Costo por impresión** | $0.042 | $0.015 | $0.213 |

### Observaciones clave:
- **Campaña A** tiene el mejor CPA ($46.67) y un conversion rate sólido (3%).
- **Campaña B** es barata por clic ($0.375) pero convierte muy mal (0.5%).
- **Campaña C** tiene el CTR más alto (6%) y buen conversion rate (4%), pero el CPA es excesivo ($88.89) por el CPC elevado ($3.56).

---

## 2. ¿Escalar o Pausar?

### ✅ **ESCALAR → Campaña A (Landing Principal)**

**Justificación:**
- Tiene el **CPA más bajo** de todas las campañas: **$46.67** — un 38% más barato que B y un 47% más barato que C.
- Su conversion rate del **3.00%** es 6x superior al de Campaña B.
- Su CPC de $1.40 es equilibrado: no es el más barato, pero la eficiencia de conversión lo compensa ampliamente.
- Es tu campaña con mejor **ratio eficiencia/rendimiento global**.

### ⚠️ **REDUCIDO (no pausar aún) → Campaña C (Competidor)**

**Justificación para no pausarla:**
- Aunque su CPA es alto ($88.89), su **conversion rate del 4.00% es el mejor** de todas.
- Su CTR del 6% indica que el mensaje resuena mucho con usuarios que ya conocen a tu competidor.
- El problema es el **CPC ($3.56)**, no la capacidad de convertir. Si logras bajar el CPC o mejoras el landing, puede volverse muy rentable.
- Las campañas de competitor capture son estratégicas a largo plazo (robarte cuota de mercado).

### ❌ **PAUSAR → Campaña B (Blog Content)**

**Justificación:**
- CPA de **$75.00**: 61% más caro que A y casi tan cara como C.
- Conversion rate de **0.50%**: por cada 200 clics solo consigues 1 signup. Es un rendimiento muy pobre.
- Aunque el CTR (4%) y el CPC ($0.375) parecen atractivos, el bajo conversion rate la hace ineficiente como canal de adquisición.
- **Alternativa:** No la elimines; reubícala como campaña de **remarketing/audiencia** (ver punto 4).

---

## 3. Redistribución del Presupuesto de $5,000

### Propuesta de asignación:

| Campaña | Presupuesto | % del total | Justificación |
|---|---|---|---|
| **Campaña A** (Landing) | **$3,200** | 64% | Escalar tu mejor campaña en eficiencia. Con $3,200 estimas ~68 clics adicionales y ~20 signups extra, manteniendo CPA ~$46.67 |
| **Campaña C** (Competidor) | **$1,300** | 26% | Reducir pero mantener. Con $1,300 obtienes ~365 clics y ~14-15 signups (CPA mejorado a ~$87 si no optimizas, pero con test de landing podría bajar a ~$65-70) |
| **Campaña B** (Blog) | **$500** | 10% | Presupuesto mínimo para mantener visibilidad orgánica y capturar datos para remarketing. Suficiente para ~1,333 clics y ~6-7 signups |

### Resultado estimado del mes con redistribución:
- **Signups totales estimados:** ~41-42 signups (vs. 105 actuales con presupuesto ilimitado, pero con mejor eficiencia general)
- **CPA promedio ponderado:** ~$59 (vs. $55.56 actual)
- **Mejora clave:** Al enfocar en A y optimizar C, el CPA promedio puede bajar a **~$50-55** en el próximo mes.

> **💡 Nota:** Si el objetivo es máxima adquisición pura, asignaría $4,000 a A y $1,000 a C, pausando B. Pero mantener algo de B y C tiene valor estratégico.

---

## 4. A/B Tests Sugeridos para el Próximo Mes

### 🔬 Campaña A (Landing Principal) — Prioridad ALTA

| Test | Variante A (Control) | Variante B | Métrica a optimizar |
|---|---|---|---|
| **Headline del landing** | Actual | Incluir nombre del competidor o "Alternativa a [Competidor]" | Conversion Rate |
| **CTA** | Botón actual (ej: "Regístrate") | Botón con urgencia: "Empieza tu prueba gratis →" o "Obtén demo en 2 min" | CTR del CTA / Conversion Rate |
| **Formulario** | Formulario largo (nombre, email, empresa, teléfono) | Formulario corto (solo email + nombre) | Conversion Rate |
| **Social proof** | Sin testimonios | Agregar 2-3 testimonios de clientes + logos de empresas | Conversion Rate |
| **Precio visible** | Precio arriba | Precio abajo o "Desde $X/mes" con comparador | Conversion Rate |

### 🔬 Campaña C (Competidor) — Prioridad MEDIA-ALTA

| Test | Variante A | Variante B | Métrica |
|---|---|---|---|
| **Landing page** | Landing genérica | Landing con comparativa directa (tabla: [Competidor] vs [Tu producto]) | Conversion Rate |
| **Copy del ad** | "Mejor alternativa a [Competidor]" | "¿[Competidor] no cumple? Prueba [Tu producto] gratis" | CTR + CPC |
| **Extensión de sitio** | Sin extensiones | Agregar extensión de llamada + sitelinks a testimonios | CTR |

### 🔬 Campaña B (Blog) — Prioridad MEDIA

| Test | Variante A | Variante B | Métrica |
|---|---|---|---|
| **Ubicación de CTA** | CTA al final del post | CTA flotante lateral + CTA en medio del contenido | Conversion Rate |
| **Tipo de lead magnet** | Newsletter | "Descarga guía gratuita de gestión de inventario" (lead magnet tangible) | Conversion Rate |
| **Audiencia** | Todo el tráfico | Solo remarketing a visitantes que pasaron >60s en el sitio | CPA |

### 🧪 Test estratégico transversal:

- **Test de audiencia en Campaña C:** Crear una lista de audiencia similar (Lookalike) basada en los signups de Campaña A y probarla en Campaña C. Esto podría reducir el CPC de $3.56 al mejorar la relevancia del anuncio.

---

## 📋 Resumen Ejecutivo de Acciones

| Acción | Prioridad | Impacto estimado |
|---|---|---|
| Escalar Campaña A a $3,200 | 🔴 Inmediata | +20 signups/mes a menor CPA |
| Reducir Campaña C a $1,300 | 🔴 Inmediata | Optimizar eficiencia de budget |
| Pausar Campaña B (o reducir a $500) | 🔴 Inmediata | Ahorro de $1,300 |
| A/B test headline en Campaña A | 🟡 Semana 1-2 | Potencial +15-20% conversion rate |
| Crear landing comparativa para Campaña C | 🟡 Semana 1-2 | Potencial reducir CPA a ~$60-65 |
| Implementar CTA flotante en Blog | 🟢 Semana 2-3 | Potencial triplicar conversiones de B |
| Crear audiencia Lookalike para Campaña C | 🟢 Semana 3-4 | Potencial reducir CPC 20-30% |

Con estas acciones, tu meta para el próximo mes debería ser alcanzar un **CPA promedio de ~$45-50** y un **total de 80-100 signups** con los $5,000 de presupuesto.