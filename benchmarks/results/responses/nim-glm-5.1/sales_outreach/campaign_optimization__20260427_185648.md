# GLM 5.1 (NIM) — sales_outreach/campaign_optimization

- model_id: `z-ai/glm-5.1`
- success: True  | final: 7.07 | quality: 9.64
- latency_total: 163.912s | tokens_per_second: 9.4
- input_tokens: 270 | output_tokens: 1534
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes un análisis detallado de tus resultados y un plan de acción para optimizar tu presupuesto.

### 1. Cálculo de Métricas (CTR, CPC, Tasa de Conversión y CPA)

*Fórmulas:*
*   **CTR** = (Clicks / Impresiones) * 100
*   **CPC** = Costo / Clicks
*   **Tasa de Conversión (CVR)** = (Signups / Clicks) * 100
*   **CPA** = Costo / Signups

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** | 3.00% | 4.00% | 6.00% |
| **CPC** | $1.40 | $0.38 | $3.56 |
| **Tasa de Conversión** | 3.00% | 0.50% | 4.00% |
| **CPA** | $46.67 | $75.00 | $88.89 |

---

### 2. ¿Qué campaña escalar y cuál pausar?

*   **Escalar: Campaña A (Landing principal)**
    *   *Justificación:* Tiene el **CPA más bajo** ($46.67) y la mejor relación entre volumen de signups (45) y costo. Aunque la Campaña C tiene una tasa de conversión más alta (4%), su CPC es altísimo ($3.56), lo que dispara su CPA a casi $89. La Campaña A es tu "caballo de batalla": es eficiente, rentable y tiene volumen suficiente para escalar.
*   **Pausar / Reducir drásticamente: Campaña C (Competidor)**
    *   *Justificación:* Su CPA de $88.89 es casi el doble que el de la Campaña A. Gastar $3,200 (64% de tu presupuesto) en traer solo 36 usuarios no es sostenible. Aunque los usuarios que buscan alternativas a la competencia tienen alta intención de compra, el subidón de CPC hace que sea ineficiente en este momento.
*   **Ajustar (No pausar aún): Campaña B (Blog content)**
    *   *Justificación:* Su CPA ($75) es alto y su conversión es bajísima (0.5%). Sin embargo, su CPC es baratísimo ($0.38). El problema no es el costo del tráfico, sino que el tráfico es "tibio" (busca información, no software) y la landing del blog no está capturando esos leads. Es candidato a pausar si no se mejora, pero tiene potencial por el bajo CPC.

---

### 3. Redistribución del presupuesto ($5,000)

El error actual es que el 64% del presupuesto se va en la campaña menos eficiente (C). Vamos a invertir esa lógica, priorizando eficiencia y dejando un presupuesto de prueba para mejorar el ToFu (Top of Funnel).

*   **Campaña A (Landing principal): $3,500 (70%)**
    *   *Objetivo:* Escalar el modelo probado. Con un CPA de $46.67, este presupuesto debería traer unos **75 signups**. *Ojo: al escalar, el CPA suele subir un poco (por subasta y audiencias menos relevantes), pero sigue siendo la apuesta más segura.*
*   **Campaña B (Blog content): $1,000 (20%)**
    *   *Objetivo:* Aprovechar el tráfico baratísimo ($0.38) pero mejorando la conversión (ver punto 4). Si logramos subir su CVR del 0.5% al 1.5% (un objetivo realista), podríamos traer unos **39 signups** en lugar de 24 con la mitad del presupuesto anterior.
*   **Campaña C (Competidor): $500 (10%)**
    *   *Objetivo:* No pausarla del todo porque la intención de compra es altísima, pero reducirla a un presupuesto de testeo. Con $500, si mantienes el CPC y CVR, obtendrías unos **5-6 signups**. Si el CPC baja (porque reducimos las pujas agresivas), el CPA mejorará.

*Total estimado de signups con esta distribución:* ~120 signups (frente a los 105 actuales), ahorrando dinero y sentando bases para escalar más en el mes siguiente.

---

### 4. A/B Tests sugeridos para el próximo mes

**Para la Campaña A (La que vamos a escalar):**
*   **A/B Test en la Landing Page (Oferta):** Tu CVR es del 3%, lo cual está bien para SaaS, pero al inyectar más presupuesto necesitas que no baje. Testea tu oferta actual vs. una más agresiva (ej. "14 días gratis" vs. "14 días gratis + Setup gratuito sin tarjeta de crédito").
*   **A/B Test de Palabras clave:** Al escalar, añade variantes de "cola larga" (long-tail) más específicas para evitar que el CPC se dispare, como "software gestión inventario para pymes textiles" o "inventario multitienda".

**Para la Campaña B (La que tenemos que arreglar):**
*   **A/B Test de Landing (Blog vs. Popup/Slide-in):** La gente que busca "problemas inventario restaurante" no quiere ver un formulario de registro de software inmediatamente. Testea tu página actual vs. la misma página pero con un *Lead Magnet* contextual (ej. un pop-up que ofrezca una "Plantilla gratuita de inventario para restaurantes" a cambio del email). Una vez dentro del nurture, los conviertes en signups.
*   **A/B Test de Anuncios:** Testea títulos informativos ("Guía para gestionar inventario") vs. títulos orientados al dolor ("Evita pérdidas por mal inventario"). El que tenga más CTR te dirá qué ángulo atrae mejor a este público.

**Para la Campaña C (La de competidores):**
*   **A/B Test en la Landing (Copywriting):** El tráfico de competidores es el más difícil de convencer. Testea tu mensaje actual vs. una landing dedicada solo a comparar ("Nosotros vs. [Competidor]"). Pon una tabla comparativa donde resaltes tus ventajas clave (ej. si el competidor es caro, destaca tu precio; si es complejo, destaca tu facilidad de uso).
*   **A/B Test de Pujas (Bidding):** Estás pagando $3.56 por click. Testea bajar las pujas manuales o usar "Maximizar conversiones" con un límite de CPA estricto (ej. max $60). Perderás volumen, pero asegurarás rentabilidad.