# Poolside Laguna XS 2.1 — sales_outreach/campaign_optimization

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 9.23 | quality: 10.0
- latency_total: 14.412s | tokens_per_second: 191.8
- input_tokens: 322 | output_tokens: 2765

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

### **1. Cálculo de métricas por campaña**  
#### **Campana A (Landing principal):**  
- **CTR**: (1,500 / 50,000) × 100 = **3.00%**  
- **CPC**: $2,100 / 1,500 = **$1.40**  
- **CPA**: $2,100 / 45 = **$46.67**  
- **Tasa de conversión**: (45 / 1,500) × 100 = **3.00%**  

#### **Campana B (Blog content):**  
- **CTR**: (4,800 / 120,000) × 100 = **4.00%**  
- **CPC**: $1,800 / 4,800 = **$0.38**  
- **CPA**: $1,800 / 24 = **$75.00**  
- **Tasa de conversión**: (24 / 4,800) × 100 = **0.50%**  

#### **Campana C (Competidor):**  
- **CTR**: (900 / 15,000) × 100 = **6.00%**  
- **CPC**: $3,200 / 900 = **$3.56**  
- **CPA**: $3,200 / 36 = **$88.89**  
- **Tasa de conversión**: (36 / 900) × 100 = **4.00%**  

---

### **2. ¿Cuál campaña escalar y cuál pausar?**  
#### **Escalar: Campana A (Landing principal)**  
- **Razones:**  
  - **CPA más bajo** ($46.67 vs. $75 y $88.89).  
  - **Tasa de conversión más alta** (3.00% vs. 0.50% y 4.00%).  
  - **CPC razonable** ($1.40).  
  - Genera **más signups por dólar invertido** (45 signups / $2,100 = 0.0214 signups/$) vs. B (24 / $1,800 = 0.0133) y C (36 / $3,200 = 0.0113).  

#### **Pausar: Campana C (Competidor)**  
- **Razones:**  
  - **CPA más alto** ($88.89) y **CPC elevado** ($3.56).  
  - Aunque tiene alta tasa de conversión (4.00%), el costo por signup es prohibitivo.  
  - **Menos eficiente en ROI** (36 signups / $3,200 = 0.0113 signups/$).  

#### **Campana B (Blog content):**  
- **Mantener con optimización**.  
  - **CTR alto** (4.00%) y **CPC bajo** ($0.38), pero **muy baja tasa de conversión** (0.50%).  
  - Podría mejorarse optimizando la landing page o redirigiendo tráfico a una página más convencional.  

---

### **3. Redistribución del presupuesto ($5,000/mes)**  
#### **Propuesta:**  
- **Campana A (Landing principal):** **$3,500** (70% del presupuesto).  
  - Escalar para maximizar signups a bajo costo.  
- **Campana B (Blog content):** **$1,000** (20% del presupuesto).  
  - Mantener para generar tráfico de calidad, pero optimizar la conversión.  
- **Campana C (Competidor):** **$0** (0%).  
  - Pausar y reanalizar estrategia (ej: ajustar palabras clave, mejorar landing page).  

#### **Justificación:**  
- La campaña A ofrece **mejor relación costo-beneficio**.  
- La campaña B puede ser optimizada con pruebas A/B.  
- La campaña C no justifica el costo alto, a menos que se reduzca el CPC o se mejore la conversión.  

---

### **4. A/B Tests sugeridos para el próximo mes**  
#### **Campana A (Landing principal):**  
1. **Varianzas de llamado a la acción (CTA):**  
   - Testear botones como "Obtener Demo Gratis" vs. "Solicitar Prueba Gratis".  
2. **Diseño de landing page:**  
   - Comparar versión con testimonios vs. versión con casos de éxito.  

#### **Campana B (Blog content):**  
1. **Optimización de landing page:**  
   - Testear una landing page simplificada con formulario de 1 campo vs. formulario completo.  
2. **Palabras clave de intención comercial:**  
   - Agregar keywords como "software gestión inventario precio" para captar usuarios con intención de compra.  

#### **Campana C (Competidor):**  
1. **Palabras clave de cola larga:**  
   - Testear keywords más específicas como "alternativa a [competidor] para pymes".  
2. **Anuncios con enfoque en diferenciación:**  
   - Comparar anuncios que destaquen "menos costoso que [competidor]" vs. "más fácil de usar que [competidor]".  

---

### **Resumen final**  
- **Escalar:** Campana A.  
- **Pausar:** Campana C.  
- **Optimizar:** Campana B.  
- **Presupuesto recomendado:** $3,500 (A), $1,000 (B), $0 (C).  
- **Priorizar A/B tests** para mejorar la conversión de B y validar la viabilidad de C.