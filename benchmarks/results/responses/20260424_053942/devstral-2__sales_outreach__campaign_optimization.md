# Devstral 2 (Dic 2025) — sales_outreach/campaign_optimization

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.7 | quality: 9.72
- latency_total: 21.67s | tokens_per_second: 79.6
- input_tokens: 303 | output_tokens: 1725
- judge_score: 4.8 | justificación: 

## Respuesta completa

Vamos a analizar tus campañas paso a paso con cálculos y recomendaciones basadas en datos.

---

### **1. Cálculo de métricas clave por campaña**
| Métrica               | Fórmula                          | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|-----------------------|----------------------------------|---------------------|------------------|------------------------|
| **CTR (Click-Through Rate)** | (Clicks / Impresiones) × 100 | (1,500 / 50,000) × 100 = **3.0%** | (4,800 / 120,000) × 100 = **4.0%** | (900 / 15,000) × 100 = **6.0%** |
| **CPC (Costo por Click)** | Costo / Clicks                | $2,100 / 1,500 = **$1.40** | $1,800 / 4,800 = **$0.38** | $3,200 / 900 = **$3.56** |
| **Conversion Rate**   | (Signups / Clicks) × 100        | (45 / 1,500) × 100 = **3.0%** | (24 / 4,800) × 100 = **0.5%** | (36 / 900) × 100 = **4.0%** |
| **CPA (Costo por Adquisición)** | Costo / Signups          | $2,100 / 45 = **$46.67** | $1,800 / 24 = **$75.00** | $3,200 / 36 = **$88.89** |

---

### **2. ¿Qué campaña escalar y cuál pausar?**
#### **Análisis por eficiencia:**
- **Campaña C (Competidor):**
  - **Mejor Conversion Rate (4%)** y **CTR más alto (6%)**, pero **CPA más alto ($88.89)**.
  - **CPC elevado ($3.56)**, lo que sugiere alta competencia en keywords de competidores.
  - **Justificación para escalar:** Aunque el CPA es alto, el tráfico es muy relevante (usuarios buscando alternativas están en etapa de decisión). Optimizando el CPC (ej: ajustando pujas o mejorando Quality Score), podría reducir el CPA.

- **Campaña A (Landing Principal):**
  - **CPA más bajo ($46.67)** y **Conversion Rate decente (3%)**.
  - **CTR bajo (3%)**, pero keywords transaccionales ("software gestión inventario") son valiosas.
  - **Justificación para mantener/escalar:** Es la más eficiente en costo por lead. Podría mejorarse el CTR con ajustes en anuncios o landing page.

- **Campaña B (Blog):**
  - **CPA más alto ($75)** y **Conversion Rate muy bajo (0.5%)**.
  - **CPC bajo ($0.38)** y **CTR alto (4%)**, pero el tráfico no convierte.
  - **Justificación para pausar o reducir:** El contenido del blog atrae tráfico de "top of funnel" (investigación), pero no genera signups. Si el objetivo es leads, no es rentable. Si el objetivo es branding, podría mantenerse con menor presupuesto.

#### **Recomendación:**
- **Escalar:** **Campaña C** (competidor) y **Campaña A** (landing).
- **Pausar o reducir:** **Campaña B** (blog), a menos que su objetivo sea branding/awareness (no conversiones directas).

---

### **3. Redistribución del presupuesto ($5,000)**
Basado en el rendimiento actual y potencial de optimización:

| Campaña       | Presupuesto Actual | Presupuesto Sugerido | Justificación |
|---------------|--------------------|----------------------|---------------|
| **Campaña A** | $2,100             | **$2,500** (+$400)   | Mejor CPA y Conversion Rate. Invertir más en keywords transaccionales. |
| **Campaña C** | $3,200             | **$2,000** (-$1,200) | Alto CPA, pero tráfico relevante. Reducir para probar optimizaciones (ej: landing pages específicas para competidores). |
| **Campaña B** | $1,800             | **$500** (-$1,300)   | Bajo ROI en conversiones. Usar solo para remarketing o pruebas de contenido. |
| **Nuevo Test**| -                  | **$0**               | Si hay presupuesto extra, probar una **Campaña D** (ej: remarketing o keywords de "intención comercial alta"). |

**Notas:**
- Si la **Campaña C** lograra reducir su CPA (ej: con mejor Quality Score o landing pages optimizadas), podría recibir más presupuesto.
- La **Campaña B** podría pausarse y usar su presupuesto en pruebas (A/B tests) para las otras campañas.

---

### **4. A/B Tests sugeridos para el próximo mes**
#### **Para Campaña A (Landing Principal):**
1. **Anuncios:**
   - **Test A:** Enfatizar "prueba gratis" vs. **Test B:** Enfatizar "ahorra X horas/semana".
   - **Test C:** Usar extensiones de sitio (ej: enlaces a casos de éxito) vs. sin extensiones.

2. **Landing Page:**
   - **Test A:** Formulario corto (solo email) vs. **Test B:** Formulario largo (email + teléfono + empresa).
   - **Test C:** Video explicativo vs. imagen + texto.

#### **Para Campaña C (Competidor):**
1. **Keywords:**
   - Probar **keywords de competidor + "precio"** (ej: "[competidor] precio vs alternativa") vs. keywords genéricas de alternativa.

2. **Landing Page:**
   - **Test A:** Página comparativa directa ("Nosotros vs [Competidor]") vs. **Test B:** Página genérica de producto.
   - **Test C:** Incluir testimonios de usuarios que migraron del competidor.

#### **Para Campaña B (Blog - si se mantiene):**
1. **Objetivo:**
   - Testear si el tráfico del blog puede convertirse con **pop-ups de exit-intent** o **CTAs en el contenido** (ej: "Descarga guía gratuita de inventario" para captar emails).

2. **Remarketing:**
   - Crear una audiencia de visitantes del blog y mostrarles anuncios de la **Campaña A** (landing principal) con un mensaje como "¿Listo para probar nuestro software?".

---

### **Resumen de acciones clave:**
1. **Pausar o reducir drásticamente la Campaña B** (blog) y reasignar presupuesto a A y C.
2. **Optimizar la Campaña C** para reducir CPA (mejorar Quality Score, probar landing pages específicas).
3. **Escalar la Campaña A** con pruebas en anuncios y landing pages.
4. **Implementar A/B tests** en anuncios, keywords y páginas de destino para mejorar Conversion Rate y CPA.

Si logras reducir el CPA de la **Campaña C** a ~$60-$70, podría volverse la más rentable por la alta intención de compra de sus usuarios.