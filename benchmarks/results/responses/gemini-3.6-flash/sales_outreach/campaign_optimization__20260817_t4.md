# Gemini 3.6 Flash — sales_outreach/campaign_optimization

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 19.162s | tokens_per_second: 185.3
- input_tokens: 292 | output_tokens: 3550

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

Aquí tienes el análisis detallado de tus campañas, la justificación basada en datos y la estrategia para optimizar tu presupuesto de $5,000.

---

### 1. Cálculo de Métricas por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** (Click-Through Rate) | **3.00%** | **4.00%** | **6.00%** |
| **CPC** (Costo por Clic) | **$1.40** | **$0.38** | **$3.56** |
| **CVR** (Tasa de Conversión) | **3.00%** | **0.50%** | **4.00%** |
| **CPA** (Costo por Adquisición) | **$46.67** | **$75.00** | **$88.89** |

*Fórmulas utilizadas:*
*   *CTR = (Clicks / Impresiones) * 100*
*   *CPC = Costo / Clicks*
*   *CVR = (Signups / Clicks) * 100*
*   *CPA = Costo / Signups*

---

### 2. ¿Qué campaña escalar y cuál pausar/reestructurar?

#### **ESCALAR: Campaña A (Landing principal)**
*   **Justificación numéricas:** Es tu campaña más eficiente. Tiene el **CPA más bajo ($46.67)** y una tasa de conversión sólida (3.00%). Con el mismo dinero, la Campaña A te genera casi el doble de clientes que la Campaña C.
*   **Motivo estratégico:** Captura intención de compra directa ("software gestión inventario") a un costo razonable por clic ($1.40).

#### **PAUSAR O REESTRUCTURAR: Campaña C (Competidores)**
*   **Justificación numérica:** Tiene el **CPA más alto ($88.89)** y un CPC exorbitante ($3.56). Se consumió el 45% de tu gasto total anterior ($3,200) pero solo generó el 34% de los signups.
*   **Motivo estratégico:** Aunque la intención del usuario es altísima (CVR del 4%), las subastas por marcas de competidores son costosas. Si tu presupuesto total está limitado a $5,000, esta campaña destruye tu rentabilidad actual.

*(Nota sobre Campaña B: Su CPA de $75 es alto y su CVR de 0.50% es muy bajo, pero genera volumen de tráfico muy barato a $0.38/clic. No debe buscar signups directos, sino alimentar el embudo).*

---

### 3. Redistribución del Presupuesto ($5,000/mes)

Anteriormente gastabas $7,100. Para ajustarte al límite de **$5,000** y maximizar el retorno de inversión (ROI), sugiero la siguiente asignación:

| Campaña | Presupuesto | % del Total | Signups Est. | Razón de la asignación |
| :--- | :--- | :--- | :--- | :--- |
| **Campaña A** | **$3,300** | 66% | ~70 | Maximizar el canal con menor CPA ($46.67). |
| **Campaña B** | **$700** | 14% | ~9 | Mantener tráfico barato para retargeting/captura de leads fríos. |
| **Campaña C** | **$1,000** | 20% | ~11 | Mantener presencia contra competidores, pero recortando pujas altas. |
| **TOTAL** | **$5,000** | **100%** | **~90 Signups** | *(Vs. los 105 signups anteriores pero gastando $2,100 menos)* |

---

### 4. Experimentos A/B Sugeridos para el Próximo Mes

1. **Campaña A (Optimización de Conversión - CRO):**
   * **Test:** Prueba dos versiones de la Landing Page.
   * **Variable:** Cambiar el formulario actual de la landing por uno de "Menos campos" o agregar *Prueba Social* (logos de clientes/testimonios) sobre el pliegue principal.
   * **Objetivo:** Subir la CVR del 3% al 4%. Si lo logras, el CPA bajará a $35.00.

2. **Campaña B (Oferta de Captación / Lead Magnet):**
   * **Test:** Modificar el Call to Action (CTA) en los artículos de blog.
   * **Variable:** En lugar de ofrecer "Registrarte en el Software" (alta fricción para un lector de blog), ofrecer una "Plantilla de Inventario en Excel Gratis" a cambio del correo.
   * **Objetivo:** Aumentar la CVR del 0.5% a un 3-5% en captura de leads para luego hacerles *Email Nurturing*.

3. **Campaña C (Estrategia de Copy y Palabras Clave):**
   * **Test:** Anuncios orientados a la diferencia de precio/facilidad de uso.
   * **Variable:** Comparar un anuncio genérico vs. uno con el titular: *"¿[Competidor] es muy caro/complejo? Conoce la alternativa más ágil"*.
   * **Objetivo:** Mejorar la relevancia y el *Quality Score* de Google para reducir el CPC de $3.56 a menos de $2.50.