# GLM-5.1 — sales_outreach/campaign_optimization

- model_id: `z-ai/glm-5.1`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 48.608s | tokens_per_second: 75.8
- input_tokens: 272 | output_tokens: 3683
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para un emprendedor, proporcionando análisis detallados y recomendaciones prácticas.

## Respuesta completa

Aquí tienes el análisis completo de tus campañas de Google Ads, paso a paso:

### 1. Cálculo de Métricas (CTR, CPC, Tasa de Conversión y CPA)

*Nota: Asumimos "Signups" como la conversión principal.*

**Campaña A (Landing principal)**
*   **CTR (Click-Through Rate):** 1,500 / 50,000 = **3.0%**
*   **CPC (Costo por Clic):** $2,100 / 1,500 = **$1.40**
*   **Tasa de Conversión (CR):** 45 / 1,500 = **3.0%**
*   **CPA (Costo por Adquisición):** $2,100 / 45 = **$46.67**

**Campaña B (Blog content)**
*   **CTR (Click-Through Rate):** 4,800 / 120,000 = **4.0%**
*   **CPC (Costo por Clic):** $1,800 / 4,800 = **$0.38**
*   **Tasa de Conversión (CR):** 24 / 4,800 = **0.5%**
*   **CPA (Costo por Adquisición):** $1,800 / 24 = **$75.00**

**Campaña C (Competidor)**
*   **CTR (Click-Through Rate):** 900 / 15,000 = **6.0%**
*   **CPC (Costo por Clic):** $3,200 / 900 = **$3.56**
*   **Tasa de Conversión (CR):** 36 / 900 = **4.0%**
*   **CPA (Costo por Adquisición):** $3,200 / 36 = **$88.89**

---

### 2. ¿Qué campaña escalar y cuál pausar?

*Nota previa: Tu gasto real del mes fue de $7,100 ($2,100 + $1,800 + $3,200), lo cual supera tu presupuesto de $5,000. Esto es crucial para la redistribución.*

*   **Escalar: Campaña A.**
    *   **Justificación:** Es tu campaña más eficiente. Tiene el **CPA más bajo ($46.67)** y una tasa de conversión sólida del 3%. El tráfico es de intención de compra directa ("software gestion inventario"), lo que significa que los usuarios que llegan ya están buscando una solución. Al escalarla, mantendrás el costo por cliente controlado.
*   **Pausar (o reestructurar drásticamente): Campaña B.**
    *   **Justificación:** Aunque el CPC es baratisimo ($0.38) y genera mucho tráfico, la intención de búsqueda es puramente informativa ("como gestionar inventario"). Esto se refleja en una **tasa de conversión del 0.5%** y un **CPA de $75**. Estás atrayendo a personas que quieren aprender, no necesariamente a comprar un software hoy. Te está drenando presupuesto sin retorno.
*   **Mantener pero optimizar (No pausar aún): Campaña C.**
    *   **Justificación:** Tiene la **tasa de conversión más alta (4%)** y el CTR más alto (6%). El problema es el **CPC altísimo ($3.56)** que eleva el **CPA a $88.89**. La intención de compra es máxima (buscan alternativas a tu competidor), pero el subasta por esas keywords es muy cara. Si logras bajar un poco el CPC mejorando el Quality Score o los anuncios, esta campaña puede ser un oro mina.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

El objetivo es maximizar los Signups dentro del presupuesto, priorizando el menor CPA.

*   **Campaña A (60% = $3,000):**
    *   *Proyección:* A $1.40 CPC -> ~2,142 clics -> Al 3% CR -> **~64 Signups** (CPA ~$46.67)
*   **Campaña C (30% = $1,500):**
    *   *Proyección:* A $3.56 CPC -> ~421 clics -> Al 4% CR -> **~17 Signups** (CPA ~$88.89)
    *   *Razón:* Mantenemos presencia porque la intención de compra es altísima, pero limitamos el gasto porque es ineficiente en costo.
*   **Campaña B (10% = $500) - *Solo si cambias la estrategia*:**
    *   *Razón:* No le daremos $1,800 para mandarlos a la landing de ventas. Le daremos $500 para mandarlos a un artículo de blog que capture leads de forma más suave (ver tests A/B abajo). Si no estás dispuesto a cambiar la landing de esta campaña, **pásale el 10% a la Campaña A** (70% A / 30% C).

*Resultado estimado con nueva distribución:* ~81 Signups por $5,000 (CPA promedio de ~$61.70). Antes gastaste $7,100 para obtener 105 Signups (CPA promedio $67.60). Lograrás un CPA más saludable respetando tu presupuesto.

---

### 4. A/B Tests sugeridos para el próximo mes

**Para la Campaña A (Escalar):**
*   **Test de Landing Page:** Tu CR es del 3%, lo cual está bien para SaaS, pero se puede mejorar. Prueba una versión de la landing donde el formulario de Signup esté "above the fold" (visible sin hacer scroll) vs. la versión actual que requiere hacer clic en un botón CTA primero.
*   **Test de Keywords:** Agrega modificadores de concordancia exacta `[software gestion inventario]` y frase `"inventario pymes"`. Al escalar, no quieres que Google te gaste presupuesto en búsquedas como "software de gestion de inventario gratis" o "inventario pymes excel".

**Para la Campaña B (Corregir intención de búsqueda):**
*   **Test de Oferta/Lead Magnet (Crucial):** La gente que busca "problemas inventario restaurante" no quiere registrarse en un software todavía, quiere soluciones. Crea una landing alternativa que ofrezca un **Recurso Gratuito** (Ej. "Descarga nuestra plantilla de inventario para restaurantes" o "Guía gratuita: Cómo reducir mermas en tu inventario") a cambio de su email. Mide si el CPA de este nuevo "Lead" baja. Luego, nutres ese lead por email para convertirlo en Signup.
*   **Test de Anuncios:** Prueba un título de anuncio que mencione el problema vs. la solución. Ej: "¿Problemas con tu inventario?" vs. "Simplifica tu inventario hoy".

**Para la Campaña C (Bajar el CPC y CPA):**
*   **Test de Landing Page de Comparativa:** No los mandes a tu Home. Mándalos a una landing específica que diga: "[Tu Software] vs [Competidor]: Por qué +500 empresas han migrado". Incluye una tabla comparativa visual. Esto debería aumentar tu CR por encima del 4%, compensando el alto CPC.
*   **Test de Anuncios (Copy de Switching):** Prueba anuncios que hablen directamente al dolor del competidor. Ej: "¿[Competidor] te está cobrando de más? Conoce una alternativa más fácil y barata".
*   **Test de Keywords Negativas:** Revisa el informe de términos de búsqueda. Es muy probable que te estén activando clics en búsquedas como "[competidor] login" o "[competidor] precios". Agrega "login", "soporte", "empleos" como keywords negativas para dejar de tirar dinero a la basura.