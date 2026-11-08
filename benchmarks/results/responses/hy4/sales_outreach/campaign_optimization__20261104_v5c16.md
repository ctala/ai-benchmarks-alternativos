# Tencent Hy4 — sales_outreach/campaign_optimization

- model_id: `tencent/hy4`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 23.316s | tokens_per_second: 89.9
- input_tokens: 293 | output_tokens: 2096

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

Excelente dataset. Vamos a desglosarlo con rigor y luego pasar a decisiones accionables. Te dejo todo en formato claro, con cálculos, criterios y recomendaciones tácticas.

---

## 1. Métricas por campaña

| Campaña | Impresiones | Clicks | Signups | Costo | **CTR** | **CPC** | **CVR** | **CPA** |
|--------|-------------|--------|---------|-------|---------|---------|---------|---------|
| **A** | 50,000 | 1,500 | 45 | $2,100 | **3.00%** | **$1.40** | **3.00%** | **$46.67** |
| **B** | 120,000 | 4,800 | 24 | $1,800 | **4.00%** | **$0.375** | **0.50%** | **$75.00** |
| **C** | 15,000 | 900 | 36 | $3,200 | **6.00%** | **$3.56** | **4.00%** | **$88.89** |

**Fórmulas usadas:**
- CTR = Clicks / Impresiones
- CPC = Costo / Clicks
- CVR = Signups / Clicks
- CPA = Costo / Signups

📌 **Totales actuales**: Costo = $7,100 (⚠️ estás **$2,100 por encima** del presupuesto de $5,000). Signups totales = 105 | CPA blended = **$67.62**

---

## 2. Qué escalar y qué pausar (con justificación)

### ✅ **Escalar: Campaña A**
| Razón | Dato |
|------|------|
| **Mejor CPA** | $46.67 (vs $75 B y $88.89 C) |
| **CVR sólido** | 3.00% (6x mejor que B) |
| **CPC eficiente** | $1.40 (4x más barato que C) |
| **Intención de compra** | Keywords transaccionales ("software gestión inventario") |

👉 Es tu **caballo de batalla**. Cada dólar extra aquí rinde ~2.1x más que en B y ~1.9x más que en C.

---

### ⚠️ **Pausar (o reestructurar): Campaña B**
| Razón | Dato |
|------|------|
| **Peor CVR** | 0.50% (1 signup cada 200 clicks) |
| **CPA más alto relativo a eficiencia** | $75 pese a CPC barato |
| **Tráfico informativo** | "cómo gestionar…", "problemas…" = top-of-funnel |
| **Costo de oportunidad** | $1,800 → 24 signups; esos $ en A darían ~39 signups |

📌 **No la elimines del todo**, pero **pausa la puja de búsqueda pura** y muévela a:
- Remarketing (RLSA)
- Campañas de Display/YouTube con objetivo de *consideración*
- O nutrición vía email (lead magnet en vez de signup directo)

> 💡 Regla práctica: **No midas TOFU con CPA de conversión final**. Mídelo con *assisted conversions* o *micro-conversiones* (descarga de guía, tiempo en página).

---

### 🔍 **Mantener con freno: Campaña C**
| Razón | Dato |
|------|------|
| **CTR y CVR altísimos** | 6.00% / 4.00% → intención brutal |
| **Pero CPA caro** | $88.89 por CPC elevado ($3.56) |
| **Volumen limitado** | Solo 15k impresiones (ya casi saturada) |

👉 **No la escales agresivamente**. Es una campaña de *conquista*, excelente para cerrar, pero cara. Optimiza antes de subir presupuesto:
- Mejora Quality Score (ad copy + landing específica "[Competidor] vs TuSaaS")
- Prueba concordancia de frase en vez de amplia
- Sube puja solo en horarios/dispositivos con CPA < $60

---

## 3. Redistribución del presupuesto ($5,000/mes)

> Primero: **corrige el overspend actual** ($7,100 → $5,000).

| Campaña | Presupuesto actual | **Nuevo presupuesto** | Δ | Signups estimados* | CPA esperado |
|--------|-------------------|------------------------|---|--------------------|--------------|
| **A** | $2,100 | **$3,200** | +$1,100 | ~69 | $46.67 |
| **B** | $1,800 | **$400** (solo remarketing / test) | –$1,400 | ~5 (micro) | — |
| **C** | $3,200 | **$1,400** | –$1,800 | ~16 | ~$87 |
| **Total** | $7,100 | **$5,000** | ✅ | **~90 signups** | **~$55.5 blended** |

\* Estimación lineal conservadora (asumo CVR estable; en A podrías mejorar con optimizaciones).

📈 **Resultado esperado**:
- Signups: 105 → ~90 (bajan en volumen, **pero CPA blended cae de $67.62 → ~$55.5**)
- Ahorro: $2,100
- Eficiencia: **+18% más conversiones por dólar**

🔁 Alternativa más agresiva (si validas que A aguanta escala):
- A: $3,600 | C: $1,200 | B: $200 → ~93 signups, CPA ~$53.8

---

## 4. A/B Tests para el próximo mes (priorizados)

### 🧪 Campaña A (donde más ROI hay)
| Test | Hipótesis | Métrica primaria |
|------|-----------|------------------|
| **Landing: "Demo en 30s" vs "Prueba gratis 14 días"** | Reducir fricción sube CVR | CVR / CPA |
| **Headline con dolor concreto**: *"Deja de perder stock en Excel"* vs genérico | Mayor relevancia → mejor QS | CTR + CPC |
| **Concordancia exacta vs frase** en "software gestion inventario" | Menos desperdicio, mismo volumen | CPA |
| **Formulario: 3 campos vs 1 campo (solo email)** | Menos fricción = +signups | CVR |

### 🧪 Campaña C (optimizar antes de escalar)
| Test | Hipótesis | Métrica |
|------|-----------|---------|
| **Landing dedicada "[Competidor] vs [TuMarca]"** vs landing principal | Relevancia ad→LP baja CPC y sube CVR | CPA |
| **Ad copy con precio / migración gratis** | Diferenciador directo | CTR + CVR |
| **Puja por dispositivo** (parece caro en mobile?) | Recortar CPC sin perder intención | CPC / CPA |

### 🧪 Campaña B (reencuadre, no CPA)
| Test | Objetivo |
|------|---------|
| **CTA: "Descargar checklist" en vez de "Regístrate"** | Micro-conversión medible |
| **RLSA: pujar solo a quienes visitaron A** | Traer TOFU al fondo del funnel |
| **Excluir keywords "gratis / tutorial"** | Evitar tráfico nunca-convertible |

### 🧪 Transversal
- **Conversión offline / importar CRM**: ¿los signups de C cierran mejor que los de A? Si LTV de C es 2x, quizá su CPA de $89 sí es rentable → **mide LTV:CAC, no solo CPA**.
- **Día/hora**: C suele convertir mejor en horario laboral; A puede rendir más en fin de semana (pymes).

---

## 🧠 Resumen ejecutivo (para tu reporte)

> *"El mes pasado gastamos $7,100 (41% sobre presupuesto) con un CPA blended de $67.62. La Campaña A es la única con eficiencia real ($46.67). B genera tráfico barato pero casi no convierte (0.5% CVR); C tiene la mejor intención pero el CPC más caro. Reasignamos a A ($3,200), frenamos C ($1,400) y reconvertimos B a remarketing ($400). Esperamos ~90 signups con CPA ~$55. Próximo foco: bajar CVR-fricción en A y Quality Score en C."*

Si quieres, puedo:
- Armarte la **hoja de cálculo con fórmulas** (Google Sheets)
- Simular **escenarios de escala de A** con saturación de keywords
- Diseñar el **copy exacto de los ads del test A/C**

¿Seguimos con alguno? 🚀