# Nemotron 3.5 Lightning — sales_outreach/campaign_optimization

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.3 | quality: 10.0
- latency_total: 7.135s | tokens_per_second: 235.7
- input_tokens: 316 | output_tokens: 1682

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

Aquí tienes un análisis detallado de tus campañas basado en los datos proporcionados.

### 1. Cálculo de Métricas

Primero, calculemos las métricas estándar para cada campaña:

*   **CTR (Click-Through Rate):** `(Clics / Impresiones) * 100`
*   **CPC (Cost-Per-Click):** `Costo Total / Clics`
*   **Conversion Rate (CR):** `(Signups / Clics) * 100`
*   **CPA (Cost-Per-Acquisition):** `Costo Total / Signups`

**Campaña A (Landing principal):**
*   **CTR:** (1,500 / 50,000) * 100 = **3.00%**
*   **CPC:** $2,100 / 1,500 = **$1.40**
*   **CR:** (45 / 1,500) * 100 = **3.00%**
*   **CPA:** $2,100 / 45 = **$46.67**

**Campaña B (Blog content):**
*   **CTR:** (4,800 / 120,000) * 100 = **4.00%**
*   **CPC:** $1,800 / 4,800 = **$0.375**
*   **CR:** (24 / 4,800) * 100 = **0.50%**
*   **CPA:** $1,800 / 24 = **$75.00**

**Campaña C (Competidor):**
*   **CTR:** (900 / 15,000) * 100 = **6.00%**
*   **CPC:** $3,200 / 900 = **$3.56**
*   **CR:** (36 / 900) * 100 = **4.00%**
*   **CPA:** $3,200 / 36 = **$88.89**

---

### 2. ¿Qué campana escalar y qué pausar?

Para decidir, hay que mirar la **eficiencia (CPA)** y la **intención del usuario**.

*   **Campaña A:** Tiene un CPA muy bajo ($46.67) y un buen CR (3%). El tráfico es de "intención alta" (la gente busca "software gestion inventario"). Es tu mejor opción actual.
*   **Campaña B:** Tiene un CPA alto ($75) y un CR muy bajo (0.5%). El tráfico es de "intención baja" (personas buscando "como gestionar inventario", quizás solo informándose o teniendo problemas específicos de restaurante, no necesariamente buscando comprar software). Es la menos eficiente.
*   **Campaña C:** Tiene un CR excelente (4%) y un CTR alto, pero el CPA es el más alto ($88.89). El tráfico es de "marca/comparación" (la gente ya conoce el mercado y te busca a ti o a tu competidor). Es cara porque compites por nombres propios.

**Decisión:**

1.  **Pausar la Campaña B:** Es el claro perdedor. Gastar $1,800 para obtener solo 24 signups (CPA $75) es ineficiente comparado con la Campaña A. El tráfico de blog es difícil de monetizar directamente a menos que tengas un embudo de nurturing muy fuerte.
2.  **Escalar la Campaña A:** Es tu "caballo de batalla". Tiene el mejor costo por adquisición. Con un presupuesto de $5,000, esta campaña debería recibir la mayor parte de los fondos porque convierte bien a un precio bajo.
3.  **Analizar la Campaña C:** Tiene una calidad de lead alta (saben lo que quieren), pero es cara. Podría mantenerse con un presupuesto pequeño para capturar demanda de marca, pero no es prioritaria para el crecimiento masivo si el objetivo es volumen de signups con presupuesto limitado.

---

### 3. Redistribución del Presupuesto ($5,000)

Dado que la Campaña B es poco eficiente, te sugiero reasignar ese dinero a la Campaña A y posiblemente a probar nuevos segmentos.

**Propuesta de distribución:**

*   **Campaña A (Landing principal):** **$3,000** (60% del presupuesto).
    *   *Por qué:* Es la más rentable. Al aumentar el presupuesto, puedes obtener más clics a $1.40 el CPC y mantener ese CPA bajo de $46.
*   **Campaña C (Competidor):** **$500** (10% del presupuesto).
    *   *Por qué:* Para mantener la visibilidad ante búsquedas de marca y captar a usuarios listos para cambiar, pero sin arriesgar mucho capital dado el alto CPA.
*   **Campaña B (Blog):** **$0** (Pausado).
    *   *Por qué:* Se detiene la pérdida de dinero en tráfico de baja conversión.
*   **Presupuesto restante ($1,500):**
    *   Se puede usar para **expandir la Campaña A** con nuevos grupos de anuncios basados en palabras clave de "intención media" (ej. "mejor software inventario pyme", "software de stock"), o guardarlo como fondo de contingencia.

---

### 4. A/B Tests sugeridos para el próximo mes

Dado que la Campaña A es la ganadora, los tests deben enfocarse en mejorar su CR o bajar su CPC.

**Test 1: Título y Descripción del Anuncio (Campaña A)**
*   **Hipótesis:** Los usuarios hacen clic, pero quizás el mensaje en la landing no coincide con la expectativa.
*   **Variante A (Control):** El anuncio actual con "Software gestión inventario".
*   **Variante B:** Probar un anuncio que destaque un beneficio directo, ej: "Gestiona tu inventario un 30% más rápido | Prueba gratilla 14 días".
*   **Meta:** Aumentar el CTR y filtrar clicks de usuarios con alta intención de compra.

**Test 2: Llamada a la Acción (CTA) en la Landing Page (Campaña A)**
*   **Hipótesis:** El formulario o botón actual no es lo suficientemente atractivo.
*   **Variante A:** Botón "Registrarse Gratis".
*   **Variante B:** Botón "Ver Demo en Vivo" o "Calcula tus ahorros".
*   **Meta:** Mejorar el Conversion Rate actual del 3%. A veces cambiar "Gratis" por "Demo" atrae a usuarios con más presupuesto.

**Test 3: Segmentación por Dispositivo (Campaña A)**
*   **Hipótesis:** El tráfico móvil tiene un comportamiento distinto al de escritorio.
*   **Acción:** Revisar el informe de dispositivos. Si el móvil tiene un CPA alto, reducir el puja móvil o crear un anuncio específico para móvil con un formulario más corto.

**Resumen de acción:** Deja de perder dinero en la Campaña B, inyecta fondos en la Campaña A y comienza a testar el texto de los anuncios y la landing page para intentar bajar ese CPA de $46 aún más.