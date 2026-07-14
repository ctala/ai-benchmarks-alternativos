# DeepSeek V3 — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 18.484s | tokens_per_second: 69.1
- input_tokens: 272 | output_tokens: 1277
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y recomendaciones prácticas para optimizar la campaña de marketing.

## Respuesta completa

Vamos a analizar paso a paso.  

## **1. Calcula CTR, CPC, CPA, y conversion rate de cada campaña**  

**Fórmulas:**  
- CTR = Clicks / Impresiones  
- CPC = Costo / Clicks  
- CPA = Costo / Signups  
- Conversion Rate = Signups / Clicks  

---

### **Campaña A (Landing principal)**  
- CTR = 1500 / 50000 = **3%**  
- CPC = 2100 / 1500 = **$1.40**  
- CPA = 2100 / 45 = **$46.67**  
- Conversion Rate = 45 / 1500 = **3%**  

---

### **Campaña B (Blog content)**  
- CTR = 4800 / 120000 = **4%**  
- CPC = 1800 / 4800 = **$0.375**  
- CPA = 1800 / 24 = **$75**  
- Conversion Rate = 24 / 4800 = **0.5%**  

---

### **Campaña C (Competidor)**  
- CTR = 900 / 15000 = **6%**  
- CPC = 3200 / 900 = **$3.56**  
- CPA = 3200 / 36 = **$88.89**  
- Conversion Rate = 36 / 900 = **4%**  

---

**Tabla resumen:**

| Campaña | CTR   | CPC   | CPA   | CR   |
|---------|-------|-------|-------|------|
| A       | 3%    | $1.40 | $46.67| 3%   |
| B       | 4%    | $0.375| $75   | 0.5% |
| C       | 6%    | $3.56 | $88.89| 4%   |

---

## **2. ¿Qué campaña escalar y qué pausar? Justifica con números**  

**Objetivo principal:** Maximizar signups con menor CPA.  

- **CPA más bajo:** Campaña A ($46.67).  
- **CPA más alto:** Campaña C ($88.89) y Campaña B ($75).  

**Campaña B:**  
- CPC muy bajo ($0.375), CTR decente (4%), pero **conversión rate muy pobre (0.5%)**. Esto indica que los clicks vienen de usuarios menos comprometidos (quizás solo buscan información, no comprar).  
- CPA alto ($75) → menos eficiente en generar signups.  

**Campaña C:**  
- CTR alto (6%), conversión rate decente (4%), pero CPC alto ($3.56) y CPA muy alto ($88.89).  
- Posiblemente keywords de competidor atraen clicks pero luego la comparación no convierte tan bien a signup.  

**Campaña A:**  
- CPA más bajo ($46.67), CPC razonable ($1.40), conversión rate 3%.  
- Keywords más comerciales (“software gestión inventario”) → usuarios más cerca de comprar.  

**Decisión:**  
- **Escalar:** Campaña A (mejor CPA, conversión comercial).  
- **Pausar:** Campaña B (CPA alto, CR muy bajo, aunque CPC bajo, no vale para nuestro objetivo de signups).  
- Campaña C podría mantenerse pero con menos presupuesto si queremos capturar usuarios comparando con competidor, aunque es menos eficiente.  

---

## **3. ¿Cómo redistribuiría el presupuesto de $5,000?**  

Actualmente gasto total = $2100 + $1800 + $3200 = $7100 (excede $5000, ajustaremos).  

Propuesta:  
- Eliminar Campaña B ($1800).  
- Reducir Campaña C porque CPA alto; quizás asignar solo $1000 para mantener presencia en keywords de competidores pero optimizar.  
- Aumentar Campaña A porque mejor CPA; si escalamos, quizás aumentar a $4000.  

**Nueva distribución:**  
- Campaña A: **$4000**  
- Campaña C: **$1000**  
- Total: $5000  

---

## **4. ¿Qué A/B tests sugerirías para el próximo mes?**  

**Para Campaña A (Landing principal):**  
- Testar nuevas keywords comerciales relacionadas: “control de stock”, “sistema inventario pequeño negocio”.  
- A/B test en la landing page:  
  1. Formulario más corto vs. más largo (captura menos datos pero más conversiones?).  
  2. Agregar un botón “Ver demo gratis” vs. “Registrarse ahora”.  
  3. Testar llamadas a la acción específicas por keyword.  

**Para Campaña C (Competidor):**  
- Testar copy de ads: “Mejor que [competidor]” vs. “Alternativa económica a [competidor]”.  
- Landing page específica para competidores: mostrar tabla de comparativa directa vs. solo beneficios de nuestro producto.  

**General:**  
- Segmentar por dispositivo (mobile vs desktop) y ajustar bids.  
- Testar extensión de llamada en ads para Campaña A.  

---

**Resumen ejecutivo:**  
- **Escalar Campaña A** (CPA $46.67).  
- **Pausar Campaña B** (CR 0.5% muy bajo).  
- **Reducir Campaña C** (CPA $88.89 alto).  
- Redistribuir: $4000 a A, $1000 a C.  
- A/B tests en keywords, copy, y landing pages.