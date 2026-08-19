# MiMo-V2-Omni (multimodal) — sales_outreach/campaign_optimization

- model_id: `xiaomi/mimo-v2-omni`
- success: True  | final: 7.6 | quality: 9.44
- latency_total: 18.452s | tokens_per_second: 95.8
- input_tokens: 549 | output_tokens: 1767
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Hola! Vamos a analizar tus campañas de Google Ads con datos claros para que tomes decisiones informadas. Aquí está el desglose:

---

## **1. Cálculo de métricas por campaña**

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---------|----------------------|-------------------|-------------------------|
| **CTR** | 3.0% | **4.0%** | **6.0%** |
| **CPC** | $1.40 | **$0.375** | $3.56 |
| **CPA** | $46.67 | $75.00 | **$88.89** |
| **Conv. Rate** | 3.0% | **0.5%** | **4.0%** |
| **Costo Total** | $2,100 | $1,800 | $3,200 |

**Fórmulas usadas:**
- **CTR** = (Clicks / Impresiones) × 100
- **CPC** = Costo / Clicks
- **CPA** = Costo / Signups
- **Conv. Rate** = (Signups / Clicks) × 100

---

## **2. ¿Cuál escalar y cuál pausar?**

### ✅ **Escalar: Campaña C (Competidor)**
- **CPA más alto ($88.89)**, pero **tasa de conversión más alta (4%)**.
- Usuarios con alta intención de compra (búsqueda de alternativas a competidores).
- **ROI potencial:** Aunque el CPA es alto, el valor de vida del cliente (LTV) podría justificarlo si tu producto es premium.

### ✅ **Mantener/optimizar: Campaña A (Landing)**
- Métricas equilibradas: buen CTR (3%), CPA razonable ($46.67), conversión sólida (3%).
- Palabras clave transaccionales ("software gestión inventario") → usuarios listos para comprar.

### ⚠️ **Pausar/reducir: Campaña B (Blog)**
- **CTR alto (4%) y CPC muy bajo ($0.375)**, pero **tasa de conversión pésima (0.5%)**.
- El tráfico es barato, pero no convierte: usuarios buscan información, no comprar.
- **CPA de $75** no es sostenible para leads fríos.

---

## **3. Redistribución del presupuesto ($5,000/mes)**

| Campaña | Asignación Actual | Asignación Sugerida | Justificación |
|---------|-------------------|---------------------|--------------|
| **A (Landing)** | $2,100 (42%) | **$2,000 (40%)** | Mantener rendimiento estable. |
| **B (Blog)** | $1,800 (36%) | **$500 (10%)** | Solo para pruebas o remarketing. |
| **C (Competidor)** | $3,200 (64%) | **$2,500 (50%)** | Escalar donde hay mayor intención de compra. |

**Total:** $5,000  
**Estrategia:**  
- **Campaña C** recibe más presupuesto por su alto valor estratégico (captura de competencia).  
- **Campaña B** se reduce drásticamente: úsala solo para **remarketing** o contenido de embudo superior.  
- **Campaña A** se mantiene como base sólida.

---

## **4. A/B Tests sugeridos para el próximo mes**

### **Para Campaña A (Landing principal):**
1. **Test de landing page:**  
   - Variante A: Landing actual con formulario corto.  
   - Variante B: Landing con testimonios + video demo + formulario en dos pasos.  
2. **Test de oferta:**  
   - Variante A: "Prueba gratis 14 días".  
   - Variante B: "Asesoría gratuita + prueba".

### **Para Campaña B (Blog):**
1. **Test de contenido:**  
   - Variante A: Artículo genérico "Cómo gestionar inventario".  
   - Variante B: Artículo específico "Cómo evitar pérdidas en inventario de restaurante" (con lead magnet descargable).  
2. **Test de segmentación:**  
   - Excluir usuarios que solo buscan información y enfocarse en "intención comercial" (ej: "software para inventario").

### **Para Campaña C (Competidor):**
1. **Test de anuncios:**  
   - Variante A: "Alternativa a [competidor] más fácil de usar".  
   - Variante B: "Compara [tu producto] vs [competidor] - Tabla comparativa".  
2. **Test de landing page:**  
   - Variante A: Página enfocada en diferenciadores vs competidor.  
   - Variante B: Página con casos de éxito de clientes que migraron.

---

## **Resumen ejecutivo:**
- **Prioriza Campaña C** (alta conversión) y **optimiza Campaña A** (consistencia).  
- **Reduce Campaña B** o conviértela en una herramienta de remarketing.  
- **Invierte en pruebas** que mejoren el CPA de Campaña C y la conversión de Campaña A.  

¿Quieres que profundicemos en algún punto o que simulemos escenarios con diferentes presupuestos? 😊