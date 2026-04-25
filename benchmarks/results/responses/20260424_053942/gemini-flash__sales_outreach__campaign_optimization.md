# Gemini 2.5 Flash — sales_outreach/campaign_optimization

- model_id: `google/gemini-2.5-flash`
- success: True  | final: 7.4 | quality: 9.44
- latency_total: 11.066s | tokens_per_second: 184.8
- input_tokens: 292 | output_tokens: 2045
- judge_score: 4.6 | justificación: 

## Respuesta completa

¡Claro! Vamos a desglosar estos resultados y a planificar las siguientes acciones.

### 1. Cálculo de Métricas por Campaña

Aquí están los cálculos para cada métrica solicitada:

**Fórmulas:**
*   **CTR (Click-Through Rate):** (Clicks / Impresiones) * 100
*   **CPC (Costo Por Click):** Costo / Clicks
*   **CPA (Costo Por Adquisición):** Costo / Signups
*   **Conversion Rate (Tasa de Conversión):** (Signups / Clicks) * 100

---

**Campana A (Landing principal):**
*   **CTR:** (1,500 / 50,000) * 100 = **3.00%**
*   **CPC:** $2,100 / 1,500 = **$1.40**
*   **CPA:** $2,100 / 45 = **$46.67**
*   **Conversion Rate:** (45 / 1,500) * 100 = **3.00%**

---

**Campana B (Blog content):**
*   **CTR:** (4,800 / 120,000) * 100 = **4.00%**
*   **CPC:** $1,800 / 4,800 = **$0.38**
*   **CPA:** $1,800 / 24 = **$75.00**
*   **Conversion Rate:** (24 / 4,800) * 100 = **0.50%**

---

**Campana C (Competidor):**
*   **CTR:** (900 / 15,000) * 100 = **6.00%**
*   **CPC:** $3,200 / 900 = **$3.56**
*   **CPA:** $3,200 / 36 = **$88.89**
*   **Conversion Rate:** (36 / 900) * 100 = **4.00%**

---

### Resumen de Métricas:

| Campaña                  | Impresiones | Clicks | Signups | Costo      | CTR     | CPC     | CPA      | Conversion Rate |
| :----------------------- | :---------- | :----- | :------ | :--------- | :------ | :------ | :------- | :-------------- |
| **Campana A (Principal)** | 50,000      | 1,500  | 45      | $2,100     | 3.00%   | $1.40   | $46.67   | 3.00%           |
| **Campana B (Blog)**      | 120,000     | 4,800  | 24      | $1,800     | 4.00%   | $0.38   | $75.00   | 0.50%           |
| **Campana C (Competidor)**| 15,000      | 900    | 36      | $3,200     | 6.00%   | $3.56   | $88.89   | 4.00%           |

---

### 2. ¿Cuál campaña escalar y cuál pausar? Justifica con números.

**Campaña a Escalar:** **Campana A (Landing Principal)**

*   **Justificación:**
    *   **CPA más bajo ($46.67):** Esta campaña es la más eficiente en términos de costo por adquisición. Esto significa que cada signup te cuesta menos dinero en comparación con las otras campañas. Es la que te da el mejor retorno por tu inversión directa en signups.
    *   **Conversion Rate sólido (3.00%):** Muestra que las personas que llegan a la landing principal están interesadas y son propensas a convertirse.
    *   **Keywords de alta intención:** "software gestion inventario", "inventario pymes" son términos que indican que el usuario está buscando activamente una solución como la tuya, lo que suele resultar en mejores conversiones.

**Campaña a Pausar:** **Campana C (Competidor)**

*   **Justificación:**
    *   **CPA más alto ($88.89):** Esta campaña es significativamente más cara por cada signup que la Campaña A y B. Aunque tiene un buen Conversion Rate (4.00%), el costo de adquirir esos signups es casi el doble que en la Campaña A.
    *   **CPC más alto ($3.56):** El costo por click es el más elevado, lo que contribuye a su alto CPA.
    *   **Impresiones limitadas:** Aunque tiene el CTR más alto, el volumen de impresiones es el más bajo, lo que sugiere un mercado más pequeño o nicho para estas keywords, y con un CPA tan alto, no es eficiente perseguirlo agresivamente.

**Consideración para Campaña B:** Aunque tiene un CPA alto ($75.00) y un Conversion Rate bajo (0.50%), su CPC es extremadamente bajo ($0.38) y genera un gran volumen de clics a bajo costo. Esto la hace valiosa para la parte superior del embudo (awareness y consideración), aunque no sea la mejor para conversiones directas. **No la pausaría inmediatamente**, pero la reevaluaría con una estrategia de nutrición de leads posterior. Por ahora, priorizaría la Campaña A para signups directos.

---

### 3. ¿Cómo redistribuiría el presupuesto de $5,000?

Basado en la justificación anterior, la estrategia sería:

*   **Aumentar significativamente el presupuesto de la Campaña A:** Es la más eficiente para generar signups.
*   **Mantener o ajustar ligeramente Campaña B:** Aprovechar su bajo CPC para generar tráfico de calidad a bajo costo, pero con una expectativa clara de que su rol es generar leads en la parte superior del embudo, no conversiones directas. Podríamos incluso reducirlo para dar más a la Campaña A, pero no eliminarla por completo debido al valor del tráfico.
*   **Reducir o pausar Campaña C:** Dado su alto CPA y CPC, es la menos eficiente para el presupuesto limitado.

**Propuesta de Redistribución:**

*   **Campana A (Landing principal):** **$3,000 - $3,500** (Original: $2,100)
    *   *Justificación:* Duplicar o casi duplicar el presupuesto aquí para capitalizar su eficiencia en CPA.
*   **Campana B (Blog content):** **$1,000 - $1,500** (Original: $1,800)
    *   *Justificación:* Reducir ligeramente para liberar presupuesto para la Campaña A, pero mantener una inversión decente para seguir generando tráfico de bajo costo y alimentar el embudo. El objetivo principal de esta campaña debería ser generar tráfico cualificado para retargeting o para nutrir a largo plazo.
*   **Campana C (Competidor):** **$0 - $500** (Original: $3,200)
    *   *Justificación:* Dada su ineficiencia, es la primera en ser recortada. Si el presupuesto lo permite y hay una razón estratégica muy fuerte para seguir apareciendo contra competidores (ej. defensa de marca), se podría dejar un presupuesto mínimo ($500) para mantener presencia, pero si el objetivo es maximizar signups con el presupuesto actual, lo ideal sería pausarla por completo.

**Ejemplo de Distribución con $5,000:**

*   **Campana A:** $3,500
*   **Campana B:** $1,500
*   **Campana C:** $0 (Pausada)
*   **Total:** $5,000

---

### 4. ¿Qué A/B tests sugerirías para el próximo mes?

Para optimizar las campañas y mejorar aún más los resultados, aquí hay algunas sugerencias de A/B tests:

**Para Campana A (Landing principal - la que escalamos):**

1.  **A/B Test de Landing Page:**
    *   **Variante A:** Landing Page actual.
    *   **Variante B:** Una nueva versión de la landing page con:
        *   **Titulares más impactantes:** Enfocados en el mayor beneficio o en resolver el dolor principal del cliente.
        *   **CTA (Call-to-Action) diferente:** Probar textos como "Empieza tu prueba gratuita", "Obtén tu demo personalizada", "Calcula tu ROI ahora".
        *   **Elementos de prueba social:** Añadir testimonios, logos de clientes, o casos de estudio prominentes.
        *   **Formulario más corto:** Si el formulario actual es largo