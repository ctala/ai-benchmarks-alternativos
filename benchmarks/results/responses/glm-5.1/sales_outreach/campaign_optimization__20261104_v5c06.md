# GLM-5.1 — sales_outreach/campaign_optimization

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 25.174s | tokens_per_second: 59.3
- input_tokens: 272 | output_tokens: 1492

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

Aquí tienes un análisis detallado de tus resultados de Google Ads y un plan de acción estratégico para optimizar tu presupuesto.

### 1. Cálculo de Métricas (CTR, CPC, CPA, Tasa de Conversión)

**Fórmulas utilizadas:**
*   **CTR (Click-Through Rate):** (Clics / Impresiones) * 100
*   **CPC (Costo Por Clic):** Costo / Clics
*   **Tasa de Conversión:** (Signups / Clics) * 100
*   **CPA (Costo Por Adquisición/Signup):** Costo / Signups

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clics** | 1,500 | 4,800 | 900 |
| **Signups** | 45 | 24 | 36 |
| **Costo** | $2,100 | $1,800 | $3,200 |
| **CTR** | **3.00%** | **4.00%** | **6.00%** |
| **CPC** | **$1.40** | **$0.38** | **$3.56** |
| **Tasa de Conv.** | **3.00%** | **0.50%** | **4.00%** |
| **CPA** | **$46.67** | **$75.00** | **$88.89** |

---

### 2. ¿Cuál campaña escalar y cuál pausar? (Justificación)

*   **Escalar: Campaña A (Landing principal)**
    *   *Justificación:* Es la campaña más rentable y equilibrada. Tiene el **CPA más bajo ($46.67)**, lo que significa que estás adquiriendo clientes potenciales al mejor precio. Además, su tasa de conversión (3%) es saludable y su CPC ($1.40) es razonable para términos de "bottom of funnel" (intención de compra).
*   **Escalar (con ajustes): Campaña C (Competidor)**
    *   *Justificación:* Aunque tiene el CPA más alto ($88.89), tiene la **tasa de conversión más alta (4%)** y el mejor CTR (6%). Las personas que buscan alternativas a tu competidor están muy listas para comprar. Si logras bajar el CPC (que es muy alto, $3.56) mediante mejoras en el Quality Score, esta campaña será una mina de oro.
*   **Pausar / Reducir drásticamente: Campaña B (Blog content)**
    *   *Justificación:* Atrae mucho tráfico barato (CPC de $0.38), pero es tráfico de "top of funnel" (buscando información, no software). Su **tasa de conversión es bajísima (0.50%)** y su **CPA es altísimo ($75.00)**. Te está costando más conseguir un signup desde un artículo de blog que desde tu landing page principal. No es momento para esta campaña si tu presupuesto es limitado y buscas rentabilidad inmediata.

---

### 3. Redistribución del presupuesto ($5,000/mes)

Dado que tu presupuesto es de $5,000 al mes, pero el gasto actual es de $7,100 ($2,100 + $1,800 + $3,200), estás excedido. La redistribución debe enfocarse en eficiencia y captura de demanda existente.

**Nueva distribución sugerida:**
*   **Campaña A (Landing principal): $3,000/mes (60% del presupuesto)**
    *   *Por qué:* Es tu motor de crecimiento rentable. Con $3,000 y manteniendo el CPA actual de $46.67, podrías generar unos **64 signups al mes**.
*   **Campaña C (Competidor): $2,000/mes (40% del presupuesto)**
    *   *Por qué:* Con un CPC tan alto, necesitas presupuesto para mantener visibilidad cuando alguien busca a tu competidor. Con $2,000 y un CPA de $88.89, generarías unos **22 signups al mes**. (Total esperado: ~86 signups/mes).
*   **Campaña B (Blog content): $0/mes (Pausada)**
    *   *Por qué:* Libera los $1,800 que estabas gastando aquí de forma ineficiente y reasigna ese capital a las campañas que convierten.

---

### 4. A/B Tests sugeridos para el próximo mes

Para mejorar los resultados con el nuevo presupuesto, sugiero los siguientes tests:

**Para la Campaña A (Landing):**
1.  **A/B Test de Anuncios (Copy):** Crea dos anuncios diferentes. Uno enfocado en "Ahorra tiempo" y otro en "Reduce errores en inventario". Mide cuál genera un CPA menor.
2.  **A/B Test de Palabras Clave (Match Types):** Prueba cambiar "software gestion inventario" de *Frase (Phrase)* a *Exacta (Exact)*. Esto podría reducir el CPC de $1.40 al evitar búsquedas amplias menos relevantes.

**Para la Campaña C (Competidor):**
1.  **A/B Test en la Landing Page:** El CPC es de $3.56, lo cual es carísimo, probablemente porque Google penaliza el "Quality Score" de anuncios de competidores. Crea una landing page dedicada exclusivamente a compararte con el competidor (Ej: "Por qué cambiar de [Competidor] a [Tu Marca]"). Al aumentar la relevancia, el CPC debería bajar.
2.  **A/B Test de Oferta (Lead Magnet):** Alguien que busca "alternativa a [competidor]" ya tiene un dolor específico. Prueba ofrecer en el anuncio una "Guía de migración gratuita" o "1 mes gratis" en lugar de un "Signup" genérico para subir el CTR y la conversión.

**Para la Campaña B (Si decides reactivarla en el futuro):**
1.  **A/B Test de Captura:** No los envíes a un formulario de signup directo desde el blog. Haz un test donde el CTA del blog ofrezca descargar un "Checklist de gestión de inventario para restaurantes" a cambio del email. Un lead magnet de "top of funnel" subirá la tasa de conversión del 0.50% a algo más aceptable, y podrás nutrir esos correos después.