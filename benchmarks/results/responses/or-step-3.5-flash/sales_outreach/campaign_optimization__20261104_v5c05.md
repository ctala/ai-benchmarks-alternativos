# Step 3.5 Flash — sales_outreach/campaign_optimization

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.46 | quality: 8.0
- latency_total: 35.266s | tokens_per_second: 98.3
- input_tokens: 280 | output_tokens: 3467

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

### 1. Cálculo de métricas por campaña

| Campaña | CTR (%) | CPC ($) | CPA ($) | Conversion Rate (%) |
|---------|---------|---------|---------|---------------------|
| A       | 3.00%   | 1.40    | 46.67   | 3.00%               |
| B       | 4.00%   | 0.375   | 75.00   | 0.50%               |
| C       | 6.00%   | 3.56    | 88.89   | 4.00%               |

**Cálculos:**  
- **CTR** = (Clicks / Impresiones) × 100  
- **CPC** = Costo / Clicks  
- **CPA** = Costo / Signups  
- **Conversion Rate** = (Signups / Clicks) × 100  

---

### 2. Campaña a escalar y a pausar (justificación numérica)

- **Escalar: Campaña A**  
  - **CPA más bajo ($46.67)**: Obtiene conversiones al menor costo.  
  - **Tasa de conversión sólida (3%)**: Equilibra clicks y conversiones.  
  - **CPC moderado ($1.40)**: Efficiente para keywords de intención comercial directa ("software gestión inventario", "inventario pymes").  
  - **Rentabilidad**: Con $3,200 de presupuesto (ver redistribución), podría generar ~68 signups (3,200 / 46.67), vs. 45 actuales.

- **Pausar: Campaña C**  
  - **CPA más alto ($88.89)**: Cuesta casi el doble que A por conversión.  
  - **CPC elevado ($3.56)**: Keywords de competidor son caras y menos sostenibles.  
  - **Baja escalabilidad**: Aunque tiene buen CTR (6%) y tasa de conversión (4%), su costo total ($3,200) solo rinde 36 signups.  
  - **Alternativa**: Si se reactiva, debe optimizarse landing page y pujas.

- **Nota sobre Campaña B**:  
  - **CTR alto (4%) y CPC muy bajo ($0.375)**, pero **tasa de conversión muy baja (0.5%)**.  
  - **CPA alto ($75)**: Ineficiente por ahora, pero su bajo CPC permite probar optimizaciones (ej. cambiar landing page) antes de descartar.

---

### 3. Redistribución del presupuesto de $5,000/mes

- **Presupuesto actual total**: $2,100 (A) + $1,800 (B) + $3,200 (C) = $7,100 → **excede en $2,100**.  
- **Propuesta ajustada a $5,000**:  
  - **Campaña A**: $3,200 (aumento desde $2,100) → enfocar en lo que mejor funciona.  
  - **Campaña B**: $1,800 (mantener, pero con tests de optimización).  
  - **Campaña C**: $0 (pausada).  
  - **Total**: $5,000.

**Razón**: A tiene el mejor CPA y escalabilidad. B se mantiene para probar mejoras en conversión. C se elimina por alto costo.

---

### 4. A/B tests sugeridos para el próximo mes

#### **Campaña A (Landing principal)**  
- **Test 1**: Landing page simplificada vs. actual.  
  - Objetivo: Aumentar conversion rate >3%.  
  - Cambios: Reducir campos del formulario, añadir testimonios, CTA más prominente.  
- **Test 2**: Nuevos anuncios con enfoque en beneficios (ej. "Ahorra 10h/semana en inventario") vs. mensajes genéricos.  
  - Objetivo: Mejorar CTR >3%.

#### **Campaña B (Blog content)**  
- **Test 1**: Enviar tráfico a **página de captura específica** (ej. "Guía gratuita de inventario") vs. blog post.  
  - Objetivo: Aumentar conversion rate de 0.5% a >2%.  
- **Test 2**: Oferta de lead magnet diferente (ej. plantilla Excel vs. ebook).  
  - Objetivo: Mejorar relevancia y conversión.

#### **Tests cruzados**  
- **Extensiones de anuncio**: Probar extensiones de snippets estructurados o llamadas en todas las campañas.  
- **Pujas automáticas**: En Campaña A, probar "Maximizar conversiones" para mejorar volumen sin subir CPA.  
- **Audiencias**: En Campaña B, añadir audiencias de remarketing para usuarios que leyeron el blog.

---

### Resumen ejecutivo
- **Prioriza Campaña A**: Escala con $3,200/mes por su eficiencia (CPA $46.67).  
- **Optimiza Campaña B**: Mantén presupuesto pero cambia la estrategia de landing page.  
- **Elimina Campaña C**: No es sostenible (CPA $88.89).  
- **Enfoque en conversión**: Tests deben centrarse en mejorar la tasa de conversión de B y mantener la de A.