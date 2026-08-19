# GPT-OSS 120B — sales_outreach/campaign_optimization

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.66 | quality: 8.0
- latency_total: 25.01s | tokens_per_second: 81.9
- input_tokens: 322 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

## 1️⃣ Métricas de cada campaña  

| Campaña | Impresiones | Clicks | Sign‑ups | Costo | **CTR** | **CPC** | **CPA** | **Conversion Rate** |
|---------|-------------|--------|----------|-------|---------|---------|---------|----------------------|
| **A – Landing principal** | 50 000 | 1 500 | 45 | $2 100 | **3 %** (1 500 ÷ 50 000) | **$1,40** ($2 100 ÷ 1 500) | **$46,67** ($2 100 ÷ 45) | **3 %** (45 ÷ 1 500) |
| **B – Blog content** | 120 000 | 4 800 | 24 | $1 800 | **4 %** (4 800 ÷ 120 000) | **$0,38** ($1 800 ÷ 4 800) | **$75,00** ($1 800 ÷ 24) | **0,5 %** (24 ÷ 4 800) |
| **C – Competidor** | 15 000 | 900 | 36 | $3 200 | **6 %** (900 ÷ 15 000) | **$3,56** ($3 200 ÷ 900) | **$88,89** ($3 200 ÷ 36) | **4 %** (36 ÷ 900) |

> **Definiciones**  
> * **CTR** = Clicks ÷ Impresiones × 100 %  
> * **CPC** = Costo ÷ Clicks  
> * **CPA** = Costo ÷ Sign‑ups (costo por adquisición)  
> * **Conversion Rate** = Sign‑ups ÷ Clicks × 100 %  

---

## 2️⃣ ¿Qué campaña escalar y cuál pausar?  

| Métrica | Campaña A | Campaña B | Campaña C |
|---------|-----------|-----------|-----------|
| CPA (costo por registro) | **$46,67** (mejor) | $75,00 (alto) | $88,89 (muy alto) |
| Conversion Rate | **3 %** (buena) | 0,5 % (muy baja) | **4 %** (mejor) |
| CPC | $1,40 (razonable) | **$0,38** (muy barato) | $3,56 (costoso) |
| CTR | 3 % | **4 %** (ligeramente mejor) | **6 %** (máximo) |
| Volumen de sign‑ups | 45 (45 % del total) | 24 (23 % del total) | 36 (34 % del total) |

### **Campaña a escalar → Campaña A**  
* **CPA más bajo** ($46,67) → cada dólar genera más registros.  
* **Conversion Rate sólido** (3 %) y **CPC razonable**.  
* La landing principal está alineada con el objetivo de “sign‑ups”, por lo que invertir más aquí maximiza la eficiencia del gasto.

### **Campaña a pausar → Campaña B**  
* **Conversion Rate muy bajo** (0,5 %).  
* A pesar del **CPC bajo**, el **CPA** ($75) es 60 % mayor que A y el número de registros obtenidos es el más bajo.  
* El tráfico del blog está generando clics pero casi no se convierte; es mejor redirigir esos recursos a fuentes con mayor retorno.

### **Campaña C → Mantener con presupuesto reducido**  
* Tiene el **CTR más alto** (6 %) y una **Conversion Rate decente** (4 %).  
* Sin embargo, el **CPC y CPA** son los más caros.  
* No la pausamos totalmente porque nos permite “robar” búsquedas de la competencia, pero sí se le asigna un presupuesto mucho menor y se optimiza (ej. ajustar pujas, usar palabras‑clave negativas, probar anuncios de “comparación”).

---

## 3️⃣ Redistribución del presupuesto de $5 000  

### Situación actual  
- Gasto total en el mes: **$7 100** (excede el límite de $5 000).  
- Necesitamos recortar **$2 100** sin perder la mayor parte del rendimiento.

### Prioridad basada en **CPA** (más bajo = más registros por dólar)

| Campaña | CPA | Sign‑ups esperados por $1 000 | Propuesta de presupuesto | Sign‑ups estimados |
|---------|-----|------------------------------|---------------------------|--------------------|
| **A** | $46,67 | 21,4 | **$3 500** (70 % del presupuesto) | 3 500 ÷ 46,67 ≈ **75** |
| **C** | $88,89 | 11,3 | **$1 000** (20 %) | 1 000 ÷ 88,89 ≈ **11** |
| **B** | $75,00 | 13,3 | **$500** (10 %) | 500 ÷ 75 ≈ **7** |
| **Total** | — | — | **$5 000** | **≈ 93** registros |

> **