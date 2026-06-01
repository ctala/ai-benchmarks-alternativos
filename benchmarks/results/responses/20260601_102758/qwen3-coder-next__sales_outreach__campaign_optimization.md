# Qwen3-Coder-Next (OpenRouter FP8) — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.95 | quality: 9.92
- latency_total: 12.359s | tokens_per_second: 165.7
- input_tokens: 307 | output_tokens: 2048
- judge_score: 5.0 | justificación: 

## Respuesta completa

¡Excelente análisis! Vamos a desglosar los datos paso a paso y luego te doy recomendaciones estratégicas concretas.

---

### **1. Cálculo de métricas por campaña**

Fórmulas:
- **CTR (Click-Through Rate)** = (Clicks / Impresiones) × 100  
- **CPC (Costo por clic)** = Costo / Clicks  
- **Conversion Rate (CR)** = (Signups / Clicks) × 100  
- **CPA (Costo por adquisición)** = Costo / Signups  

#### ✅ **Campana A (Landing principal)**  
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100  
- **CTR** = (1,500 / 50,000) × 100 = **3.0%**  
- **CPC** = 2,100 / 1,500 = **$1.40**  
- **CR** = (45 / 1,500) × 100 = **3.0%**  
- **CPA** = 2,100 / 45 = **$46.67**

#### ✅ **Campana B (Blog content)**  
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800  
- **CTR** = (4,800 / 120,000) × 100 = **4.0%**  
- **CPC** = 1,800 / 4,800 = **$0.38**  
- **CR** = (24 / 4,800) × 100 = **0.5%**  
- **CPA** = 1,800 / 24 = **$75.00**

#### ✅ **Campana C (Competidor)**  
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200  
- **CTR** = (900 / 15,000) × 100 = **6.0%**  
- **CPC** = 3,200 / 900 = **$3.56**  
- **CR** = (36 / 900) × 100 = **4.0%**  
- **CPA** = 3,200 / 36 = **$88.89**

---

### **2. ¿Qué escalar y qué pausar? Justificación con números**

| Métrica        | Campana A | Campana B | Campana C |
|----------------|-----------|-----------|-----------|
| **CTR**        | 3.0%      | **4.0%** ↑| **6.0%** ↑↑|
| **CPC**        | $1.40     | **$0.38** ↓↓| $3.56     |
| **CR**         | **3.0%** ↑| 0.5% ↓↓   | **4.0%** ↑↑|
| **CPA**        | **$46.67** ↓| $75.00 ↑| $88.89 ↑↑|

#### 🔍 **Análisis clave:**
- **Campana A (Landing principal)**:  
  ✅ **Mejor equilibrio**: CR del 3% y CPA de **$46.67** es el **más eficiente** en conversión por dólar invertido.  
  ❌ Pero CTR y CPC podrían mejorar (menos clics por impresión que B y C).

- **Campana B (Blog)**:  
  ✅ CTR y CPC **muy bajos** ($0.38 CPC es excelente si convirtiera).  
  ❌ **CR muy baja (0.5%)** → indica **desalineación entre expectativa y contenido** (ej: el usuario busca "cómo gestionar", hace clic en el blog, pero no ve un camino claro hacia signup).  
  → **No escalar sin optimización**.

- **Campana C (Competidor)**:  
  ✅ **CTR y CR más altos** (6% y 4%) → interesado *altamente calificado*.  
  ❌ **CPA muy alto ($88.89)** → probablemente por alta competencia y precios elevados en subastas de marca/competidores.  
  → **No escalar tal cual**, pero sí explotar como *alta intención*.

#### ✅ **Recomendación:**
- **ESCALAR:** **Campana A** (mejor ROI y CPA sostenible).  
- **PAUSAR (o reestructurar profundamente):** **Campana B** (por bajo conversion rate y desalineación con intención de compra).  
- **REVISAR Y OPTIMIZAR:** **Campana C** (no pausar del todo, pero ajustar: reducir presupuesto, probar landing alternativo, usar match type más preciso).

---

### **3. Redistribución del presupuesto de $5,000/mes**

Basado en eficiencia y potencial:
- Campana A: **60% → $3,000** (ahora tiene 70% del presupuesto implícito: $2,100 de $5k → pero con margen para escalar).  
- Campana C: **30% → $1,500** (captar intención alta, pero con contención).  
- Campana B: **10% → $500** (solo para A/B testing de optimización; si no mejora en 2 semanas, pausar).

#### 📊 Asignación propuesta:
| Campana | Presupuesto | % del total | Nota |
|---------|-------------|-------------|------|
| **A (Landing)** | **$3,000** | 60% | Escalable, CPA bajo, CR sólido |
| **C (Competidor)** | **$1,500** | 30% | Intención alta, pero caro → probar optimización |
| **B (Blog)** | **$500** | 10% | Para testear mejoras; no escalar sin mejora CR > 2% |

➡️ *¿Por qué no más para C?* Porque aunque tiene CR alta, el CPA es casi el doble de A. Si puedes bajar su CPA a < $60 (con landing específico o keywords más long-tail), valdría la pena escalar.

---

### **4. A/B Tests sugeridos para el próximo mes**

#### 🔹 **Campana A (Prioridad):**
- **Test 1:** Landing page vs. versión optimizada  
  - *Variante A (actual)*: Landing actual  
  - *Variante B*: Versión con:  
    - CTA más visible (ej: botón flotante, color contrastante)  
    - Pruebas sociales (logos de clientes + testimonios)  
    - Formulario reducido (3 campos en vez de 6)  
  → **Métrica clave:** CR y CPA.

- **Test 2:** Anuncios con enfoque distinto  
  - *Variante A*: "Software de inventario para Pymes"  
  - *Variante B*: "¿Cansado de errores en inventario? Sistema automatizado + soporte incluido"  
  → Medir CTR y CR por mensaje (emocional vs. funcional).

#### 🔹 **Campana C (Competidor):**
- **Test 3:** Landing page específica para “alternativas”  
  - *Variante A*: Mismo landing que Campana A  
  - *Variante B*: Landing *dedicado a comparar vs. [competidor]* (tabla de diferencias, casos de éxito, garantía de migración)  
  → **Objetivo:** Bajar CPA a ≤ $55.

- **Test 4:** Match types y palabras negativas  
  - Eliminar términos genéricos (ej: “inventario”) y enfocarse en:  
    - `"alternativa a [competidor]" EXACT`  
    - `"[competidor] comparar"` PHRASE  
  → Reducir CPC y mejorar CR.

#### 🔹 **Campana B (Blog):**
- **Test 5:** Rediseño del funnel  
  - *Variante A*: Blog → CTA “Descargar guía gratuita” → Email → Signup  
  - *Variante B*: Blog → CTA “Hacer demo rápida” (sin email previo)  
  → Medir cuál genera más *MQLs* y luego signups.

- **Test 