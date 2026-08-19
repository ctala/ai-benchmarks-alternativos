# Qwen3-Coder-Next (OpenRouter FP8) — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3-coder-next`
- success: True  | final: 7.84 | quality: 10.0
- latency_total: 40.1s | tokens_per_second: 51.1
- input_tokens: 307 | output_tokens: 2048
- judge_score: 5.0 | justificación: 

## Respuesta completa

Vamos a analizar paso a paso cada campana con los datos que compartiste.

---

### **1. Métricas por campana**

| Métrica | Fórmula | Campana A | Campana B | Campana C |
|--------|---------|-----------|-----------|-----------|
| **CTR** (Click-Through Rate) | `(Clicks / Impresiones) × 100` | `(1,500 / 50,000) × 100 = **3.00%**` | `(4,800 / 120,000) × 100 = **4.00%**` | `(900 / 15,000) × 100 = **6.00%**` |
| **CPC** (Costo por Click) | `Costo / Clicks` | `2,100 / 1,500 = **$1.40**` | `1,800 / 4,800 = **$0.375**` | `3,200 / 900 = **$3.56**` |
| **Conversion Rate** (Signups / Clicks) | `(Signups / Clicks) × 100` | `45 / 1,500 = **3.00%**` | `24 / 4,800 = **0.50%**` | `36 / 900 = **4.00%**` |
| **CPA** (Costo por Adquisición) | `Costo / Signups` | `2,100 / 45 = **$46.67**` | `1,800 / 24 = **$75.00**` | `3,200 / 36 = **$88.89**` |

✅ **Resumen de métricas clave:**

| Campana | CTR | CPC | CR | CPA |
|--------|-----|-----|----|-----|
| A (Landing principal) | 3.00% | $1.40 | **3.00%** | **$46.67** |
| B (Blog content) | **4.00%** | **$0.375** | 0.50% | $75.00 |
| C (Competidor) | **6.00%** | $3.56 | **4.00%** | $88.89 |

---

### **2. ¿Qué campana escalar y cuál pausar? Justificación numérica**

#### ✅ **Campana A (Landing principal):**
- **Mejor CPA ($46.67)** → 38% más eficiente que B y 47% más eficiente que C.
- **Mejor tasa de conversión (3.00%)** → casi **6×** mejor que la de B (0.50%) y 75% mejor que C (4.00%).
- CTR sólido (3.00%) y CPC razonable ($1.40).
- **Aunque tiene menos impresiones y clicks, genera más valor por dólar invertido.**

#### ❌ **Campana B (Blog content):**
- **Peor CPA ($75.00)** y **peor tasa de conversión (0.50%)**.
- Aunque tiene **CTR alto (4.00%)**, el contenido del blog no convierte bien (probablemente porque el usuario busca información, no una solución inmediata).
- El CPC es muy bajo ($0.375), pero eso no compensa la baja conversión.
- **No está alineada con el objetivo de adquisición directa.**

#### ⚠️ **Campana C (Competidor):**
- **Mejor CTR (6.00%) y mejor CR (4.00%)**, lo cual es muy positivo: indica que los usuarios están *muy calificados* (buscan explícitamente alternativas).
- **Pero CPA muy alto ($88.89)** porque el CPC es elevado ($3.56), probablemente por competencia por palabras clave transaccionales.
- **Alto potencial, pero mal optimizado en costo.**

🔹 **Conclusión:**
- ✅ **Escalá la Campana A** (es la más rentable).
- ❌ **Pausá la Campana B** (no está convirtiendo, es un drenaje de presupuesto).
- ⚠️ **Reoptimizá la Campana C** (no la pases, pero ajustala para reducir CPA; es una oportunidad).

---

### **3. Redistribución del presupuesto de $5,000**

**Objetivo:** Maximizar signups por dólar → priorizar CPA más bajo y escalabilidad.

#### Propuesta de asignación:

| Campana | Presupuesto | Justificación |
|--------|-------------|---------------|
| **A (Landing)** | **$3,500** (70%) | CPA más bajo, alta calidad de tráfico, potencial de escalar. Con $3,500 → ~75 signups (asumiendo CPA constante: 3,500 / 46.67 ≈ 75). |
| **C (Competidor)** | **$1,200** (24%) | Alto potencial de conversión. Si reducimos CPC a ~$2.50 (mejorando ads/landing/quals), CPA podría bajar a ~$60 → con $1,200 → 20 signups. |
| **B (Blog)** | **$300** (6%) | Solo para testing (ver si variantes de CTA o landing mejoran conversión). |

🔹 **Total:** $5,000  
🔹 **Signups estimados:**  
- A: 3,500 / 46.67 ≈ **75**  
- C: 1,200 / 60 = **20** *(optimista, con mejora en CPC)*  
- B: 300 / 75 = **4**  
➡️ **Total estimado: ~99 signups/mes** (vs. 45+24+36 = 105 con el presupuesto actual, pero a un costo más eficiente: CPA promedio actual = 7,100/105 = $67.62 → con nueva asignación: 5,000/99 ≈ **$50.50/ signup** → **25% más eficiente**).

> 💡 Nota: Si la Campana C mejora su CPC (ej. con match types más precisos, exclusión de términos irrelevantes, landing más específica), podrías subir su presupuesto a $1,500 y reducir B a $0.

---

### **4. A/B Tests sugeridos para el próximo mes**

#### 🔹 **Campana A (prioritaria para A/B):**
1. **CTA en landing page:**
   - A: *"Empezar gratis 14 días"*  
   - B: *"Ver demo en 2 minutos"*  
   *(El tráfico de B es más educativo, así que quizás una demo reduce fricción)*

2. **Headline del anuncio:**
   - A: *"Gestiona tu inventario en segundos"*  
   - B: *"Alternativa fácil y económica a [competidor]"*  
   *(Usa lenguaje de solución rápida vs. comparativa — útil para alinear con intención de búsqueda)*

#### 🔹 **Campana C (para mejorar ROI):**
1. **Landing page específica vs. redirección a landing principal:**
   - A: Redirige al landing principal (actual)  
   - B: Landing *exclusiva* para usuarios que buscan "alternativa a [competidor]" (con comparativa, caso de éxito, CTA de "cambiar ya")  
   *(¡Crucial! Este tráfico es altamente calificado, pero puede estar abandonando si el landing no es relevante)*

2. **Match type y keywords:**
   - Prueba **phrase match** vs. **exact match** para palabras como `"[competidor] alternativa"`  
   - Aisla palabras con bajo CPC + alta conversión (ej. "software competidor X") para ampliar solo esas.

#### 🔹 **Campana B (solo si no la pausas del todo):**
1. **CTA del blog:**
   - A: "Descarga guía gratuita" → redirige a e-book  
   - B: "Prueba 14 días sin compromiso" (con lead magnet: 10% off primer mes)  
   *(Quizás el tráfico de blog está listo para convertirse si ofrecés un incentivo inmediato)*

2. **Integr