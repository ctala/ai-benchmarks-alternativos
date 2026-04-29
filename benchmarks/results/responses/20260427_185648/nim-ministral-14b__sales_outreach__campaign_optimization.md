# Ministral 14B (NIM) — sales_outreach/campaign_optimization

- model_id: `mistralai/ministral-14b-instruct-2512`
- success: True  | final: 7.01 | quality: 9.16
- latency_total: 98.484s | tokens_per_second: 20.8
- input_tokens: 303 | output_tokens: 2048
- judge_score: 4.4 | justificación: 

## Respuesta completa

### **1. Métricas clave de cada campaña**
Vamos a calcular las métricas principales para cada campaña:

#### **Fórmulas:**
- **CTR (Click-Through Rate):** `(Clicks / Impresiones) * 100`
- **CPC (Cost per Click):** `Costo total / Clicks`
- **CPA (Cost per Acquisition):** `Costo total / Signups (Conversiones)`
- **Conversion Rate (Tasa de conversión):** `(Signups / Clicks) * 100`

---

#### **Campaña A (Landing principal)**
- **CTR:** `(1,500 / 50,000) * 100 = 3%` ✅
- **CPC:** `$2,100 / 1,500 = $1.40` ⚠️
- **CPA:** `$2,100 / 45 = $46.67` ❌
- **Conversion Rate:** `(45 / 1,500) * 100 = 3%` ⚠️

#### **Campaña B (Blog content)**
- **CTR:** `(4,800 / 120,000) * 100 = 4%` ✅
- **CPC:** `$1,800 / 4,800 = $0.38` ✅
- **CPA:** `$1,800 / 24 = $75` ❌
- **Conversion Rate:** `(24 / 4,800) * 100 = 0.5%` ❌

#### **Campaña C (Competidor)**
- **CTR:** `(900 / 15,000) * 100 = 6%` ✅
- **CPC:** `$3,200 / 900 = $3.56` ❌
- **CPA:** `$3,200 / 36 = $88.89` ❌
- **Conversion Rate:** `(36 / 900) * 100 = 4%` ✅

---
**Resumen comparativo:**
| Campaña | CTR  | CPC    | CPA     | Conv. Rate | Eficiencia (CPA + Conv. Rate) |
|---------|------|--------|---------|------------|-------------------------------|
| **A**   | 3%   | $1.40  | **$46.67** | 3%         | ❌ (CPA alto, CTR bajo)       |
| **B**   | 4%   | **$0.38** | **$75**  | 0.5%       | ❌ (CPA muy alto, bajas conv.)|
| **C**   | **6%** | $3.56  | **$88.89** | **4%**    | ⚠️ (CTR alto, pero CPA malo)  |

**Conclusión:**
- **Campaña A** tiene un **CTR y Conversion Rate decentes**, pero un **CPA muy alto** ($46.67 por signup).
- **Campaña B** tiene el **CPC más bajo**, pero un **CPA catastrófico** ($75) y **muy pocas conversiones**.
- **Campaña C** tiene el **mejor CTR (6%) y Conversion Rate (4%)**, pero el **peor CPA ($88.89) y CPC alto ($3.56)**.

---

### **2. ¿Qué campaña escalar y cuál pausar?**
#### **🔴 Pausar Campaña B (Blog content)**
- **Razones:**
  - **CPA de $75** es el más alto (¡más de 2x que Campaña A!).
  - **Solo 0.5% de conversión**, lo que sugiere que el tráfico del blog no está calificado para signups.
  - Aunque el **CPC es bajo ($0.38)**, el costo por cliente adquirido no justifica el presupuesto.
  - **Keywords como "cómo gestionar inventario" son informativas**, pero no transaccionales. La gente busca guías, no comprar software.

#### **⚠️ Reducir (pero no pausar) Campaña A (Landing principal)**
- Tiene un **buen CTR (3%) y Conversion Rate (3%)**, pero el **CPA es alto ($46.67)**.
- **Posibles problemas:**
  - La landing page podría no estar optimizada para convertir.
  - Las **keywords son genéricas** ("software gestión inventario"), con mucha competencia y CPC alto.
- **Acción:**
  - **Reducir presupuesto en un 30-50%** y enfocarse en optimizar la landing (A/B testing, mejor copy, oferta más clara).
  - Si el CPA no mejora, pausarla después.

#### **🟢 Escalar Campaña C (Competidor)**
- **Razones:**
  - **Mejor CTR (6%) y Conversion Rate (4%)** de todas.
  - **Keywords de intención comercial** ("alternativa a [competidor]", "[competidor] vs"), lo que atrae a usuarios con necesidad clara de comprar.
  - Aunque el **CPA es alto ($88.89)**, es porque las conversiones son **4 veces más eficientes que Campaña B** (más signups por dólar gastado).
- **Acción:**
  - **Aumentar presupuesto hasta un 50-60% del total** (ej. $2,500-$3,000/mes).
  - **Optimizar pujas** para reducir CPC sin perder volumen.
  - **Añadir más keywords de comparación** (ej. "[competidor] review", "[competidor] precios").

---
**Recomendación final de pausas/escalado:**
| Campaña | Acción          | % Presupuesto sugerido |
|---------|----------------|------------------------|
| **A**   | Reducir 50%    | 10-20%                 |
| **B**   | **Pausar**     | 0%                     |
| **C**   | **Escalar**    | 70-80%                 |

---

### **3. Redistribución del presupuesto de $5,000**
**Propósito:**
- **Maximizar signups** con el mejor **ROAS (Retorno de Inversión en Adquisición)**.
- **Enfocarse en Campaña C** (mejor conversión) y **optimizar Campaña A**.

**Distribución sugerida:**
| Campaña | Presupuesto mensual | % del total | Justificación |
|---------|---------------------|------------|---------------|
| **C (Competidor)** | **$3,500**          | **70%**    | Mejor CTR y Conversion Rate. Potencial de escalado con más signups. |
| **A (Landing)**    | **$1,000**          | **20%**    | Reducir para optimizar. Si el CPA baja, aumentar. |
| **Nueva**          | **$500**            | **10%**    | **Pruebas en nuevas keywords o formatos** (ej. Remarketing, Display). |

**Alternativa agresiva (si Campaña C funciona bien):**
- **C: $4,000 (80%)**
- **A: $500 (10%)**
- **Nueva: $500 (10%)**

---
**Notas:**
- Si **Campaña A** mejora su CPA por debajo de **$30**, mover presupuesto de "Nueva" a ella.
- Si **Campaña C** tiene un **CPA > $100**, revisar pujas o audiencia (quizá está muy competitiva).

---

### **4. A/B Tests para el próximo mes**
Para **optimizar Campaña C (Competidor)** y **mejorar Campaña A (Landing)**, prueba estos cambios:

#### **🔹 Campaña C (Escalar - Competidor)**
1. **Diferentes mensajes en anuncios:**
   - **Versión A:** *"Cansado de [competidor]? Prueba nuestra alternativa más rápida y económica."*
   - **Versión B:** *"[Competidor] es caro y lento. Nosotros damos el mismo resultado por la mitad del precio."*
   - **Métrica a medir:** **CTR y CPA**.

2. **Extensiones de anuncio:**
   - Añadir **extensión de enlace a casos de éxito** (ej. "Clientes que migraron de [competidor]").
   - **Test:** Anuncio con vs. sin extensiones.

3. **Audiencia más segmentada:**
   - **Excluir búsquedas genéricas** como "[competidor] gratis".
   - **Incluir palabras clave de dolor** como "problemas con [competidor]".

#### **