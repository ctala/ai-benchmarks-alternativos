# Gemini 2.5 Flash Lite — sales_outreach/campaign_optimization

- model_id: `google/gemini-2.5-flash-lite`
- success: True  | final: 9.13 | quality: 10.0
- latency_total: 6.51s | tokens_per_second: 314.6
- input_tokens: 291 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y ofrece una utilidad práctica significativa con un análisis detallado de las métricas y recomendaciones para optimizar las campañas.

## Respuesta completa

¡Claro que sí! Analicemos tus campañas de Google Ads y veamos cómo optimizarlas.

## 1. Cálculo de Métricas por Campaña

Vamos a calcular las métricas clave para cada una de tus campañas:

**Fórmulas:**

*   **CTR (Click-Through Rate):** (Clicks / Impresiones) * 100
*   **CPC (Cost Per Click):** Costo / Clicks
*   **Conversion Rate (Tasa de Conversión):** (Signups / Clicks) * 100
*   **CPA (Cost Per Acquisition/Signup):** Costo / Signups

---

### Campaña A (Landing principal)

*   **Impresiones:** 50,000
*   **Clicks:** 1,500
*   **Signups:** 45
*   **Costo:** $2,100

*   **CTR:** (1,500 / 50,000) * 100 = **3%**
*   **CPC:** $2,100 / 1,500 = **$1.40**
*   **Conversion Rate:** (45 / 1,500) * 100 = **3%**
*   **CPA:** $2,100 / 45 = **$46.67**

---

### Campaña B (Blog content)

*   **Impresiones:** 120,000
*   **Clicks:** 4,800
*   **Signups:** 24
*   **Costo:** $1,800

*   **CTR:** (4,800 / 120,000) * 100 = **4%**
*   **CPC:** $1,800 / 4,800 = **$0.38**
*   **Conversion Rate:** (24 / 4,800) * 100 = **0.5%**
*   **CPA:** $1,800 / 24 = **$75.00**

---

### Campaña C (Competidor)

*   **Impresiones:** 15,000
*   **Clicks:** 900
*   **Signups:** 36
*   **Costo:** $3,200

*   **CTR:** (900 / 15,000) * 100 = **6%**
*   **CPC:** $3,200 / 900 = **$3.56**
*   **Conversion Rate:** (36 / 900) * 100 = **4%**
*   **CPA:** $3,200 / 36 = **$88.89**

---

## 2. ¿Qué Campaña Escalar y Cuál Pausar?

Para tomar esta decisión, nos enfocaremos en el **CPA (Costo por Adquisición)** y el **potencial de escalabilidad**. Un CPA más bajo indica que la campaña es más eficiente generando signups.

*   **Campaña A (Landing principal):** CPA = $46.67
*   **Campaña B (Blog content):** CPA = $75.00
*   **Campaña C (Competidor):** CPA = $88.89

**Análisis:**

*   **Campaña A (Landing principal):** Tiene el **CPA más bajo** ($46.67) y una tasa de conversión decente (3%). Esto indica que los usuarios que llegan a tu landing page principal están muy interesados y convierten bien. Su CTR es bueno (3%), lo que sugiere que los anuncios son relevantes.
*   **Campaña B (Blog content):** Tiene un **alto volumen de clics y un CPC muy bajo** ($0.38), lo que es excelente para generar tráfico. Sin embargo, su **tasa de conversión es muy baja (0.5%)**, resultando en un CPA más alto que la Campaña A. Aunque atrae a mucha gente, no la está convirtiendo eficientemente.
*   **Campaña C (Competidor):** Tiene un **CTR muy alto (6%)** y una buena tasa de conversión (4%), lo que sugiere que la oferta de "alternativa" es atractiva. Sin embargo, su **CPC es significativamente alto ($3.56)** y su **CPA es el más elevado ($88.89)**. Los clics son caros y, aunque convierten bien, el costo por signup es el más alto.

**Recomendación:**

*   **Escalar:** **Campaña A (Landing principal)**. Es la más eficiente en términos de CPA, lo que significa que cada signup te cuesta menos. Al escalar esta campaña, puedes esperar obtener más signups a un costo razonable.
*   **Mantener/Optimizar:** **Campaña B (Blog content)**. No la pausaría porque tiene un excelente CPC y un alto volumen de impresiones y clics. El problema está en la baja tasa de conversión. Hay potencial para mejorarla significativamente.
*   **Pausar/Revisar Profundamente:** **Campaña C (Competidor)**. Dado que es la más cara por signup y su presupuesto actual ya es alto, es la candidata principal a pausar o, al menos, a reducir drásticamente hasta que se pueda optimizar. El alto CPC y CPA hacen que sea difícil justificar su continuidad en su forma actual si el objetivo es la eficiencia.

## 3. Redistribución del Presupuesto de $5,000

Basándonos en la eficiencia (CPA) y el potencial, aquí te propongo una redistribución:

**Presupuesto Actual Total:** $2,100 (A) + $1,800 (B) + $3,200 (C) = **$7,100**

*(Nota: Tus costos actuales superan tu presupuesto total de $5,000. Asumiré que quieres redistribuir un presupuesto TOTAL de $5,000, y que los datos del mes pasado son para analizar, no para replicar exactamente el gasto.)*

Vamos a redistribuir los $5,000 de la siguiente manera:

1.  **Campaña A (Landing principal):** **$2,500**
    *   **Justificación:** Es la más rentable (CPA más bajo). Al asignarle la mayor parte del presupuesto, maximizamos la generación de signups eficientes. Esto te permitiría aumentar su volumen de impresiones y clics, manteniendo un CPA bajo.

2.  **Campaña B (Blog content):** **$2,000**
    *   **Justificación:** A pesar de su bajo Conversion Rate, su CPC es excepcionalmente bajo y atrae mucho tráfico. Queremos mantenerla activa para generar leads a bajo costo de adquisición de clic, pero con el objetivo de mejorar su tasa de conversión. Con este presupuesto, puedes seguir generando volumen mientras trabajas en optimizarla.

3.  **Campaña C (Competidor):** **$500** (o pausar temporalmente)
    *   **Justificación:** Actualmente es la menos eficiente. Un presupuesto pequeño se puede usar para seguir monitoreando a la competencia y realizar pruebas muy específicas, pero no se le asignará una gran parte hasta que su CPA mejore significativamente. Si el objetivo principal es la eficiencia, se podría incluso pausar por completo y reasignar esos $500 a la Campaña A o B.

**Resumen de la Redistribución Propuesta ($5,000):**

*   **Campaña A:** $2,500 (50% del presupuesto)
*   **Campaña B:** $2,000 (40% del presupuesto)
*   **Campaña C:** $500 (10% del presupuesto)

---

## 4. Sugerencias de A/B Tests para el Próximo Mes

Los A/B tests son cruciales para la optimización continua. Aquí tienes algunas ideas:

### Para la Campaña A (Landing Principal - ¡La que vamos a escalar!)

*   **Título y Descripción de Anuncios:**
    *   **Test:** Prueba diferentes titulares y descripciones que enfaticen distintos beneficios (ej. "Ahorra tiempo en tu inventario" vs. "Control total de tu stock").
    *   **Objetivo:** Mejorar el CTR y la relevancia percibida.
*   **Página de Destino (Landing Page):**
    *   **Test:** Prueba dos versiones de tu landing page.
        *   **Variante 1:** Botón de CTA (Call to Action) más prominente, copia más directa.
        *   **Variante 2:** Incluir testimonios de clientes, un video corto demostrativo.
    *   **Objetivo:** Aumentar el Conversion Rate.
*   **Palabras Clave Negativas:**
    *   **Test:** Añadir o refinar la lista de palabras clave negativas. Por ejemplo, si "