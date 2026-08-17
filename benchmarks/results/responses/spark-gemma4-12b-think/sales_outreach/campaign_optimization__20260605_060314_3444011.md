# Gemma 4 12B (Spark llama-server, reasoning) — sales_outreach/campaign_optimization

- model_id: `gemma-4-12b-it-Q4_K_M.gguf`
- success: True  | final: 7.97 | quality: 9.44
- latency_total: 84.2s | tokens_per_second: 25.6
- input_tokens: 307 | output_tokens: 2157
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes el análisis detallado de tu campaña. Primero, organicemos los datos para poder tomar decisiones estratégicas.

### 1. Cálculo de Métricas (KPIs)

| Campaña | CTR | CPC | CPA (Costo por Signup) | Conv. Rate |
| :--- | :--- | :--- | :--- | :--- |
| **A (Landing)** | 3.00% | $1.40 | **$46.67** | **3.00%** |
| **B (Blog)** | 4.00% | $0.38 | $75.00 | 0.50% |
| **C (Competidor)** | **6.00%** | $3.56 | $88.89 | **4.00%** |

---

### 2. Análisis: ¿Qué escalar y qué pausar?

**Escalar: Campaña A (Landing principal)**
*   **Justificación:** Es tu campaña más eficiente. Tiene el **CPA más bajo ($46.67)**, lo que significa que cada registro te cuesta mucho menos que en las otras. Aunque el CTR es moderado, la intención de búsqueda es alta y la conversión es sólida (3%). Es el "motor" de tus ventas actuales.

**Pausar / Reducir drásticamente: Campaña C (Competidor)**
*   **Justificación:** Aunque tiene el mejor CTR (6%) y la mejor tasa de conversión (4%), su **CPA es el más alto ($88.89)**. Estás pagando casi el doble por cada signup en comparación con la Campaña A. Las palabras clave de competidores suelen ser muy caras y "sucias". Solo deberías mantenerla si el valor de vida del cliente (LTV) es muy alto, pero con un presupuesto de $5,000, es mejor invertir ese dinero en la Campaña A.

**Optimizar (No pausar totalmente): Campaña B (Blog content)**
*   **Justificación:** Esta campaña está funcionando como "Top of Funnel" (reconocimiento). Tiene un CPC muy barato ($0.38), pero su tasa de conversión es bajísima (0.5%). No es una campaña de conversión directa, sino de tráfico.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

Actualmente estás gastando $7,100, por lo que necesitas recortar un 30% del gasto total. Mi recomendación es mover el dinero hacia la eficiencia de la Campaña A y usar la Campaña B como fuente de tráfico para remarketing.

*   **Campaña A (Landing): $3,000 (60%)**
    *   *Objetivo:* Maximizar el volumen de signups con el CPA más bajo.
*   **Campaña B (Blog): $1,000 (20%)**
    *   *Objetivo:* Mantener presencia y atraer tráfico barato. Sugiero usar este tráfico para crear una audiencia de **Remarketing**.
*   **Campaña C (Competidor): $1,000 (20%)**
    *   *Objetivo:* Solo mantener las palabras clave de "competidor" que tengan mayor intención de compra, eliminando las que solo traen curiosos.

---

### 4. Sugerencias de A/B Testing para el próximo mes

Para mejorar los resultados, te sugiero estos tres experimentos:

1.  **Para la Campaña A (Mejorar conversión):**
    *   **Test de Oferta:** Prueba "Prueba gratuita de 14 días" vs. "Demo personalizada". A veces cambiar el llamado a la acción (CTA) reduce el CPA significativamente.
    *   **Test de Landing:** Prueba una landing page con un formulario corto (solo nombre y email) vs. uno largo (nombre, email, empresa, tamaño de inventario).

2.  **Para la Campaña B (Mejorar el bajo Conversion Rate):**
    *   **Lead Magnet:** Como la gente busca "cómo gestionar", no les pidas que se registren al software de inmediato. Ofréceles un **PDF gratuito** ("Checklist de inventario para restaurantes") a cambio de su email. Esto bajará el costo por lead.

3.  **Para la Campaña C (Mejorar la eficiencia):**
    *   **Landing de Comparación:** En lugar de enviar el tráfico del competidor a tu landing principal, crea una landing específica: **"Software X vs. [Competidor]: Por qué las pymes nos prefieren"**. Esto suele aumentar la tasa de conversión en búsquedas de comparación.