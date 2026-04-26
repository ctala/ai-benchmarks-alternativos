# Qwen 3.5 397B (NIM) — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 7.08 | quality: 9.36
- latency_total: 88.703s | tokens_per_second: 23.1
- input_tokens: 298 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes un análisis detallado de tus campañas de Google Ads basado en los datos proporcionados. He desglosado los cálculos, la estrategia de optimización y la redistribución del presupuesto para maximizar tu retorno de inversión (ROI).

### 1. Cálculo de Métricas Clave

Para todas las campañas, utilizaremos las siguientes fórmulas:
*   **CTR (Click-Through Rate):** $(Clicks / Impresiones) \times 100$
*   **CPC (Costo Por Click):** $Costo / Clicks$
*   **Conversion Rate (Tasa de Conversión):** $(Signups / Clicks) \times 100$
*   **CPA (Costo Por Adquisición/Signup):** $Costo / Signups$

| Métrica | Campaña A (Principal) | Campaña B (Blog/Info) | Campaña C (Competidor) |
| :--- | :---: | :---: | :---: |
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clicks** | 1,500 | 4,800 | 900 |
| **Signups** | 45 | 24 | 36 |
| **Costo Total** | $2,100 | $1,800 | $3,200 |
| **CTR** | **3.00%** | **4.00%** | **6.00%** |
| **CPC** | **$1.40** | **$0.38** | **$3.56** |
| **Conv. Rate** | **3.00%** | **0.50%** | **4.00%** |
| **CPA** | **$46.67** | **$75.00** | **$88.89** |

---

### 2. Análisis Estratégico: ¿Escalar o Pausar?

#### **Ganadora Clara: Campaña A (Landing Principal)**
*   **Justificación:** Es la campaña más eficiente en términos de negocio. Tiene el **CPA más bajo ($46.67)** y una tasa de conversión sólida (3%).
*   **Análisis:** Aunque su CTR (3%) es menor que el de la competencia, los usuarios que hacen clic tienen una intención de compra muy alta ("software gestión", "inventario pymes"). Estás pagando un CPC razonable ($1.40) y consiguiendo clientes a buen precio.
*   **Acción:** **ESCALAR**. Esta es tu fuente principal de volumen de clientes rentables.

#### **Oportunidad de Optimización: Campaña B (Blog Content)**
*   **Justificación:** Tiene el **CPC más barato ($0.38)** y un buen CTR (4%), lo que indica que el contenido es atractivo. Sin embargo, su **tasa de conversión es muy baja (0.5%)**, lo que dispara el CPA a $75.
*   **Análisis:** El tráfico es de "baja intención" (gente buscando cómo solucionar un problema, no necesariamente comprando ya). No vale la pena pausarla por completo porque el tráfico es muy barato, pero sí requiere arreglar la conversión.
*   **Acción:** **MANTENER Y OPTIMIZAR**. No escalar presupuesto hasta mejorar la landing page o la oferta para este tráfico frío.

#### **Caso Crítico: Campaña C (Competidor)**
*   **Justificación:** Tiene el mejor CTR (6%) y buena tasa de conversión (4%), lo que significa que el anuncio y la landing funcionan bien para ese perfil. El problema es el **costo desorbitado**.
*   **Análisis:** El CPC es de **$3.56**, más del doble que la Campaña A. Esto resulta en un **CPA de $88.89**, casi el doble que la Campaña A. Estás pagando una prima muy alta por robar tráfico a la competencia.
*   **Acción:** **REDUCIR DRÁSTICAMENTE O PAUSAR**. A menos que estos clientes tengan un valor de vida (LTV) mucho mayor o una tasa de retención superior, no es sostenible pagar casi $90 por signup cuando puedes conseguirlos a $46 en la Campaña A.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

El objetivo es bajar el CPA promedio global y aumentar el número total de signups.

**Presupuesto Actual:** $7,100 (Gasto real del mes pasado, excediendo tu límite de $5k).
**Nuevo Objetivo:** $5,000.

**Propuesta de Distribución:**

| Campaña | Asignación Anterior | Nueva Asignación | % del Presupuesto | Razón Estratégica |
| :--- | :---: | :---: | :---: | :--- |
| **Campaña A** | $2,100 | **$3,250** | **65%** | Maximizar volumen en la campaña más rentable. Al aumentar la puja o el presupuesto aquí, esperamos mantener un CPA cercano a $46-$50. |
| **Campaña B** | $1,800 | **$1,000** | **20%** | Mantener presencia para branding y llenar el embudo superior con tráfico barato, pero limitando la exposición al bajo ROI. |
| **Campaña C** | $3,200 | **$750** | **15%** | Reducir drásticamente. Usar solo para capturar oportunidades muy específicas de alta intención sin gastar en volumen. |
| **TOTAL** | $7,100 | **$5,000** | **100%** | |

**Proyección con nuevo presupuesto (Estimada):**
*   **Campaña A:** ~70 signups ($3250 / $46.67)
*   **Campaña B:** ~13 signups ($1000 / $75.00) *Asumiendo misma eficiencia, idealmente mejoraría con tests.*
*   **Campaña C:** ~8 signups ($750 / $88.89)
*   **Total Signups Estimados:** **~91 signups** (vs. los 105 actuales, pero gastando $2,100 menos).
*   **Nuevo CPA Global:** ~$54.94 (Mejora significativa respecto al mix actual ponderado).

---

### 4. Sugerencias de A/B Tests para el Próximo Mes

Dado que la Campaña B tiene mucho tráfico pero poca conversión, y la Campaña C es muy cara, aquí están los tests prioritarios:

#### **A. Para Campaña B (Mejorar Conversión de Tráfico Frío)**
*   **Hipótesis:** Los usuarios que buscan "cómo gestionar" no están listos para comprar, necesitan educación o un "lead magnet".
*   **Test:** Landing Page Actual vs. Landing Page con Lead Magnet.
    *   *Variante A (Control):* Formulario directo de "Prueba Gratis".
    *   *Variante B (Test):* Oferta de "Plantilla de Excel de Inventario Gratis" o "Guía PDF" a cambio del email, seguido de una secuencia de emails automática para vender el software.
*   **Métrica a medir:** Tasa de conversión a lead (no necesariamente signup de pago inmediato) y costo por lead.

#### **B. Para Campaña C (Reducir CPC/CPA)**
*   **Hipótesis:** Las palabras clave de competencia son demasiado genéricas o las pujas son muy agresivas.
*   **Test:** Enfoque de Mensaje vs. Segmentación.
    *   *Variante A (Control):* Anuncios genéricos "Mejor alternativa a [Competidor]".
    *   *Variante B (Test):* Anuncios hiper-específicos atacando una debilidad conocida del competidor (ej. "¿Cansado de las caídas de sistema de [Competidor]?"). Además, probar reducir la puja máxima un 20% para ver si se mantiene el volumen con CPC menor.
*   **Métrica a medir:** CPC y CTR.

#### **C. Para Campaña A (Escalar con seguridad)**
*   **Hipótesis:** Podemos aumentar el volumen sin disparar el CPA ampliando la coincidencia de palabras clave.
*   **Test:** Coincidencia de Palabra Clave.
    *   *Variante A (Control):* Solo coincidencia de frase (" ") y exacta ([ ]).
    *   *Variante B (Test):* Introducir coincidencia amplia (sin modificadores) con una lista de palabras clave negativas muy robusta, utilizando una estrategia de puja de "Maximizar Conversiones" con un CPA objetivo fijado en $50.
*   **Métrica a medir:** Volumen de signups y estabilidad del CPA.

### Resumen Ejecutivo
