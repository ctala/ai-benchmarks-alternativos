# Gemini 2.5 Pro — sales_outreach/campaign_optimization

- model_id: `google/gemini-2.5-pro`
- success: True  | final: 8.13 | quality: 10.0
- latency_total: 50.992s | tokens_per_second: 89.3
- input_tokens: 291 | output_tokens: 4554
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y recomendaciones prácticas para optimizar las campañas de marketing.

## Respuesta completa

¡Excelente! Analicemos a fondo los resultados de tus campañas para optimizar tu inversión. Aquí tienes un desglose completo y un plan de acción.

Primero, un resumen de tus datos para tener todo en un solo lugar.

| Campaña | Impresiones | Clicks | Signups | Costo | Keywords |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A (Principal)** | 50,000 | 1,500 | 45 | $2,100 | "software gestion inventario" |
| **B (Blog)** | 120,000 | 4,800 | 24 | $1,800 | "como gestionar inventario" |
| **C (Competidor)** | 15,000 | 900 | 36 | $3,200 | "alternativa a [competidor]" |
| **Total Gastado**| | | **105** | **$7,100**| |

---

### 1. Cálculo de Métricas Clave (KPIs)

Aquí están las métricas de rendimiento para cada campaña. Las he calculado para que puedas ver claramente el rendimiento de cada una.

| Métrica | Campaña A (Principal) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** (Tasa de Clics) | **3.0%** | **4.0%** | **6.0%** |
| *(Clicks / Impresiones)* | *(1,500 / 50k)* | *(4,800 / 120k)* | *(900 / 15k)* |
| **CPC** (Costo por Clic) | **$1.40** | **$0.38** | **$3.56** |
| *(Costo / Clicks)* | *($2,100 / 1,500)* | *($1,800 / 4,800)* | *($3,200 / 900)* |
| **Conv. Rate** (Tasa de Conversión) | **3.0%** | **0.5%** | **4.0%** |
| *(Signups / Clicks)* | *(45 / 1,500)* | *(24 / 4,800)* | *(36 / 900)* |
| **CPA** (Costo por Adquisición) | **$46.67** | **$75.00** | **$88.89** |
| *(Costo / Signups)* | *($2,100 / 45)* | *($1,800 / 24)* | *($3,200 / 36)* |

---

### 2. ¿Cuál campaña escalar y cuál pausar?

**Campaña a Escalar: Campaña A (Landing Principal)**

*   **Justificación:** Esta es tu campaña más eficiente y rentable. Tiene el **Costo por Adquisición (CPA) más bajo con diferencia: $46.67**. Esto significa que cada nuevo usuario registrado te cuesta un 38% menos que en la Campaña B y un 47% menos que en la Campaña C. Estás llegando a usuarios con una alta intención de compra ("software gestión inventario") y tu landing page los está convirtiendo eficazmente (tasa de conversión del 3.0%). Cada dólar extra invertido aquí te traerá los resultados más baratos.

**Campaña a Pausar (o Reducir Drásticamente): Campaña C (Competidor)**

*   **Justificación:** Aunque tiene el CTR y la Tasa de Conversión más altos (lo que indica que el público es muy cualificado), su rendimiento es insostenible. El **Costo por Clic (CPC) de $3.56 es altísimo**, lo que dispara el **CPA a $88.89**. Estás pagando casi el doble por un signup en esta campaña en comparación con la Campaña A. A menos que un cliente de un competidor valga el doble para ti, esta campaña está drenando tu presupuesto.

**Campaña a Optimizar (No pausar): Campaña B (Blog Content)**

*   **Justificación:** No hay que pausar esta campaña. Cumple un rol muy importante en la parte alta del embudo (Top of Funnel). Atrae una gran cantidad de tráfico a un **costo por clic muy bajo ($0.38)**. El problema no es el anuncio, es la conversión post-clic (solo 0.5%). La gente llega a tu blog, pero no se registra. En lugar de pausarla, el objetivo aquí es mejorar la tasa de conversión.

---

### 3. Redistribución del Presupuesto de $5,000

Actualmente gastaste $7,100, superando tu presupuesto. La siguiente distribución se basa en tu objetivo de $5,000 y en la estrategia de escalar lo que funciona.

**Propuesta de Nueva Distribución (Total: $5,000):**

1.  **Campaña A (Principal): $3,000** (antes $2,100)
    *   **Razón:** Duplicamos la apuesta en tu campaña ganadora. Con un CPA de ~$47, este presupuesto podría generar aproximadamente **64 signups** (en lugar de 45).
2.  **Campaña B (Blog): $1,500** (antes $1,800)
    *   **Razón:** Mantenemos una inversión sólida para seguir atrayendo tráfico barato y alimentar la parte alta de tu embudo. El foco no es gastar más, sino convertir mejor el tráfico que ya tienes.
3.  **Campaña C (Competidor): $500** (antes $3,200)
    *   **Razón:** Reducimos drásticamente la inversión para detener la sangría de dinero. Este presupuesto reducido te permite no pausarla del todo, sino usarla como un "laboratorio de pruebas" para los A/B tests (ver punto 4) y ver si puedes bajar el CPA. Si las optimizaciones no funcionan, pausa la campaña por completo y reasigna esos $500 a la Campaña A.

---

### 4. Sugerencias de A/B Tests para el Próximo Mes

Aquí tienes pruebas específicas para cada campaña enfocadas en sus debilidades y fortalezas.

#### **Para la Campaña A (La que vas a escalar):**
El objetivo es mantener la eficiencia mientras aumentas el volumen.
*   **Test 1 (Ad Copy):** Crea una variación de tu anuncio principal. Si tu titular actual es "Software de Gestión de Inventario", prueba uno enfocado en el beneficio: "**Reduce Pérdidas con Nuestro Software de Inventario**" o en una oferta: "**Prueba Gratis Nuestro Software de Inventario por 14 Días**".
*   **Test 2 (Landing Page):** Duplica tu landing page principal y en la nueva versión, cambia el titular principal para que coincida con el nuevo anuncio o cambia la posición y el texto del botón de "Sign Up". Mide si la tasa de conversión mejora.

#### **Para la Campaña B (La que vas a optimizar):**
El objetivo es aumentar la tasa de conversión del 0.5%. El tráfico es bueno y barato, ¡hay que aprovecharlo!
*   **Test 1 (CTA en el Blog):** El problema está aquí.
    *   **Versión A (Actual):** Tu blog post actual.
    *   **Versión B (Nueva):** Agrega "Content Upgrades". Por ejemplo, dentro del artículo "como gestionar inventario", ofrece un recurso descargable como "**Descarga nuestro Checklist Gratuito de Gestión de Inventario**" a cambio de un email. Esto captura leads que luego puedes nutrir para que hagan un signup.
    *   **También prueba:** Añadir banners o CTAs más visibles a lo largo del artículo que lleven a la página de registro.
*   **Test 2 (Retargeting):** Crea una audiencia en Google Ads con todos los usuarios que visitaron estos posts de blog pero no se registraron. Lánzales una campaña de remarketing con los anuncios de tu Campaña A, recordándoles los beneficios de tu software.

#### **Para la Campaña C (La que está en observación):**
El objetivo es bajar el CPA drásticamente o confirmar que no es viable.
*   **Test 1 (Landing Page Dedicada):** El CPC es alto porque la competencia por esas keywords es feroz. Para justificar el clic, tu landing page debe ser perfecta. Crea una **página de comparación directa** (ej. "Alternativa a [Competidor]"), donde muestres una tabla comparando características, precio y soporte, destacando tus ventajas. Esto puede aumentar la tasa de conversión lo suficiente como para que el CPA sea aceptable.
*   **Test 2 (Estrategia de Puja):** Si estás usando "Maximizar Clics", cambia a una estrategia de puja inteligente como **"Maximizar Conversiones con un CPA Objetivo"**. Fija un CPA objetivo agresivo (ej. $50, cercano al de tu Campaña A). Google Ads intentará conseguirte solo los clics que tengan más probabilidad de convertir a ese costo, aunque eso signifique reducir el volumen de impresiones y clics.