# Claude Opus 4.6 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 7.3 | quality: 9.44
- latency_total: 38.703s | tokens_per_second: 52.9
- input_tokens: 316 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# Análisis Completo de tus Campañas de Google Ads

## 1. Métricas Calculadas

### Campaña A — Landing Principal

| Métrica | Cálculo | Resultado |
|---|---|---|
| **CTR** | 1,500 / 50,000 | **3.00%** |
| **CPC** | $2,100 / 1,500 | **$1.40** |
| **CPA** | $2,100 / 45 | **$46.67** |
| **Conv. Rate** | 45 / 1,500 | **3.00%** |

### Campaña B — Blog Content

| Métrica | Cálculo | Resultado |
|---|---|---|
| **CTR** | 4,800 / 120,000 | **4.00%** |
| **CPC** | $1,800 / 4,800 | **$0.375** |
| **CPA** | $1,800 / 24 | **$75.00** |
| **Conv. Rate** | 24 / 4,800 | **0.50%** |

### Campaña C — Competidor

| Métrica | Cálculo | Resultado |
|---|---|---|
| **CTR** | 900 / 15,000 | **6.00%** |
| **CPC** | $3,200 / 900 | **$3.56** |
| **CPA** | $3,200 / 36 | **$88.89** |
| **Conv. Rate** | 36 / 900 | **4.00%** |

---

## Tabla Comparativa Resumen

```
Métrica          Campaña A       Campaña B       Campaña C
─────────────────────────────────────────────────────────────
CTR              3.00%           4.00%           6.00%
CPC              $1.40           $0.375          $3.56
CPA              $46.67 ✅ MEJOR  $75.00          $88.89 ❌ PEOR
Conv. Rate       3.00%           0.50%           4.00%
Signups          45              24              36
Costo            $2,100          $1,800          $3,200
─────────────────────────────────────────────────────────────
Costo/signup     EFICIENTE       CARA            MUY CARA
```

---

## 2. ¿Cuál escalar y cuál pausar?

### 🚀 ESCALAR → Campaña A (Landing Principal)

**La justificación es contundente:**

```
✅ CPA más bajo de las tres:         $46.67 (vs $75 y $89)
✅ Conversion rate sólido:            3.00%
✅ CPC razonable:                     $1.40
✅ Intent comercial alto:             Quien busca "software gestión
                                      inventario" QUIERE COMPRAR
✅ Margen de escala:                  Con solo 50K impresiones,
                                      hay mucho espacio para crecer
```

> **Dato clave:** Por cada $100 invertidos, la Campaña A genera **2.14 signups** vs 1.33 (B) vs 1.12 (C).

### ⏸️ PAUSAR → Campaña B (Blog Content)

```
❌ CPA 61% más caro que Campaña A:   $75 vs $46.67
❌ Conversion rate pésimo:            0.50% (6x peor que A)
❌ Tráfico de baja intención:         "cómo gestionar inventario"
                                      = fase informacional, NO compra
❌ 120K impresiones → solo 24 signups = desperdicio de presupuesto
```

> **El problema de fondo:** las keywords informacionales ("cómo gestionar...") atraen gente que busca información gratuita, no software. El CTR de 4% es engañoso porque los clicks no convierten.

### ⚠️ Campaña C — OPTIMIZAR, no pausar

```
⚠️ CPA alto ($88.89) PERO...
✅ Conversion rate altísimo: 4.00% (la mejor de las tres)
✅ CTR del 6.00% (la mejor de las tres)
✅ Intent de compra MÁXIMO: quien busca alternativas YA QUIERE cambiar
```

**El problema no es la audiencia, es el CPC de $3.56.** Esto se puede optimizar con:
- Mejor Quality Score (landing pages específicas de comparación)
- Ajuste de pujas
- Negative keywords más agresivas

---

## 3. Redistribución del Presupuesto de $5,000

### Distribución actual vs. propuesta:

```
                    ACTUAL              PROPUESTA
                    ─────────────────────────────────────
Campaña A           $2,100 (42%)   →    $3,000 (60%)  ↑↑
Campaña B           $1,800 (36%)   →    $  500 (10%)  ↓↓
Campaña C           $3,200 (64%*)  →    $1,500 (30%)  ↓
                    ─────────────────────────────────────
Total               $7,100**            $5,000

* Tu gasto actual EXCEDE los $5K → estás en $7,100
```

> ⚠️ **Alerta:** Gastaste $7,100 el mes pasado con un presupuesto de $5,000. Esto ya es un problema.

### Proyección con nueva distribución:

```
                    Presupuesto    CPA actual    Signups estimados
────────────────────────────────────────────────────────────────────
Campaña A           $3,000         $46.67        ~64 signups
Campaña B*          $  500         $75.00        ~ 7 signups
Campaña C**         $1,500         $70.00***     ~21 signups
────────────────────────────────────────────────────────────────────
TOTAL               $5,000                       ~92 signups
                                                 vs 105 actuales
                                                 PERO con $2,100 MENOS
```

```
*** Estimando mejora de CPA en C tras optimización

📊 Eficiencia:
   - Antes:  105 signups / $7,100 = $67.62 CPA promedio
   - Ahora:   92 signups / $5,000 = $54.35 CPA promedio
   
   → AHORRO del 20% en CPA manteniéndote en presupuesto
```

### ¿Por qué no pausar B completamente?

Los $500 en Campaña B sirven para:
1. **Nutrir el funnel superior** (awareness)
2. **Captar emails** con lead magnets en el blog (no solo signups directos)
3. **Remarketing** → esos 4,800 clicks son audiencia para retargeting
4. Mantener datos activos para posible reactivación

---

## 4. A/B Tests para el Próximo Mes

### 🧪 TEST 1 — Campaña A: Landing Page (Prioridad ALTA)

```
Variante actual:    Landing genérica de producto
Variante B:         Landing con CALCULADORA DE AHORRO
                    "Descubre cuánto pierdes por mala gestión de inventario"

Métrica objetivo:   Conversion Rate (actual: 3.00% → target: 4.5%)
Impacto estimado:   +15 signups/mes con el mismo gasto
Duración:           2 semanas (mínimo 1,000 clicks por variante)
```

### 🧪 TEST 2 — Campaña A: Copy de Anuncios

```
Variante A (actual):  "Software de