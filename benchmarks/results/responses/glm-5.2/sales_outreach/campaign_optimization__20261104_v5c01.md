# GLM 5.2 — sales_outreach/campaign_optimization

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 20.257s | tokens_per_second: 77.3
- input_tokens: 272 | output_tokens: 1565

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

Aquí tienes un análisis detallado de tus resultados en Google Ads. Tienes datos muy claros y una excelente oportunidad para optimizar tu presupuesto.

### 1. Cálculo de Métricas (CTR, CPC, CPA, Tasa de Conversión)

**Fórmulas utilizadas:**
*   **CTR (Click-Through Rate):** (Clics / Impresiones) * 100
*   **CPC (Costo Por Clic):** Costo / Clics
*   **Tasa de Conversión (CR):** (Signups / Clics) * 100
*   **CPA (Costo Por Adquisición/Signup):** Costo / Signups

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** | **3.00%** *(1,500/50k)* | **4.00%** *(4,800/120k)* | **6.00%** *(900/15k)* |
| **CPC** | **$1.40** *($2,100/1,500)* | **$0.38** *($1,800/4,800)* | **$3.56** *($3,200/900)* |
| **Tasa de Conv.** | **3.00%** *(45/1,500)* | **0.50%** *(24/4,800)* | **4.00%** *(36/900)* |
| **CPA** | **$46.67** *($2,100/45)* | **$75.00** *($1,800/24)* | **$88.89** *($3,200/36)* |

---

### 2. ¿Cuál campaña escalar y cuál pausar?

**Debes ESCALAR la Campaña A (Landing principal):**
*   **Justificación numérica:** Es la campaña más rentable. Tiene el **CPA más bajo de todas ($46.67)**. Aunque su CTR (3%) es menor que el de la Campaña C, su tasa de conversión (3%) es sólida y su CPC ($1.40) es sostenible. Por cada dólar invertido aquí, obtienes signups a un costo muy eficiente.

**Debes PAUSAR la Campaña B (Blog content):**
*   **Justificación numérica:** Aunque genera mucho tráfico barato (CPC de $0.38), la intención de compra es bajísima. Su **tasa de conversión es solo del 0.5%**, lo que infla el **CPA a $75.00**. El 80% de tu tráfico viene de aquí, pero solo genera el 23% de tus signups. Es un agujero negro para tu presupuesto.

**Caso especial - Campaña C (Competidor):**
*   No la pausarías de inmediato, pero **tampoco la escalarías ciegamente**. Tiene el mejor CTR (6%) y la mejor tasa de conversión (4%) porque la intención de compra es altísima (buscan alternativas). Sin embargo, el CPC es carísimo ($3.56) y el CPA sube a $88.89. Debes optimizarla antes de inyectarle más dinero.

---

### 3. Redistribución del presupuesto de $5,000/mes

Actualmente gastaste $7,100 el mes pasado, pero tu límite es $5,000. Basado en el rendimiento, así debería dividirse el presupuesto para maximizar signups:

*   **Campaña A (Landing): $3,000 (60% del presupuesto)**
    *   *Proyección:* A un CPA de $46.67, esta campaña debería generarte unos **64 signups**.
*   **Campaña C (Competidor): $1,500 (30% del presupuesto)**
    *   *Proyección:* A un CPA de $88.89, esta campaña debería generarte unos **16 signups**.
    *   *Nota:* Le asignamos menos porque es cara, pero la mantenemos porque trae usuarios de alta calidad que están hartos de tu competencia.
*   **Campaña B (Blog): $500 (10% del presupuesto)**
    *   *Estrategia:* En lugar de pausarla del todo, redúcela a una prueba mínima. Usa el tráfico del blog para *retargeting* (mostrarles anuncios de la Campaña A después de que lean el blog).
    *   *Proyección:* A un CPA de $75, generaría unos **6 signups**.

**Total estimado el próximo mes:** ~86 signups (frente a los 105 que tuviste el mes pasado, pero ahora respetando tu presupuesto de $5,000 y reduciendo el costo total por signup de $67 a $58).

---

### 4. A/B Tests sugeridos para el próximo mes

Para mejorar estos números el próximo mes, te sugiero los siguientes tests:

**Para la Campaña A (La que vas a escalar):**
1.  **A/B Test de Landing Page:** El CTR es de 3% (estándar) pero quieres que la tasa de conversión suba del 3%. Prueba dos titulares principales en la landing: *Enfoque 1 (Beneficio): "Ahorra 10 horas a la semana gestionando tu inventario"* vs *Enfoque 2 (Punto de dolor): "Nunca más pierdas ventas por falta de stock"*.
2.  **A/B Test de Anuncios (RSA):** Sube el CPC ($1.40). Para escalar, necesitarás pujar más alto. Testea nuevos titulares enfocados en la velocidad de implementación ("Configúralo en 5 minutos") para captar a los que vienen de la Campaña C.

**Para la Campaña C (Competidor):**
1.  **A/B Test de Oferta en el Anuncio:** El CPC es altísimo ($3.56). Para amortizarlo, tu anuncio debe destacar. Testea un anuncio que ofrezca un incentivo directo: "Migra de [Competidor] y obtén un 20% de descuento el primer mes" vs "La alternativa más rápida y económica a [Competidor]".
2.  **A/B Test de Landing de Competidor:** Crea una landing page específica para este tráfico (no envíes a la home). Haz un A/B test entre una tabla comparativa (Tú vs Competidor) y una página de testimonios de clientes que dejaron al competidor.

**Para la Campaña B (Blog):**
1.  **A/B Test de Captura en el Blog:** El problema es la conversión (0.5%). En lugar de enviarlos a una landing genérica, pon un *pop-up* o banner dentro del artículo del blog ofreciendo una guía PDF descargable gratuita ("Plantilla de gestión de inventario para restaurantes"). El lead dejará su email ahí mismo sin salir del blog. Luego, pásalo por email marketing.