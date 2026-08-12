# Solar Pro 4 — sales_outreach/campaign_optimization

- model_id: `upstage/solar-pro4`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 32.694s | tokens_per_second: 59.8
- input_tokens: 353 | output_tokens: 1954

## Respuesta completa



Aquí tienes el análisis detallado de tu campaña de Google Ads basado en los datos proporcionados, junto con las recomendaciones estratégicas para el próximo mes.

### 1. Cálculo de Métricas por Campaña

Primero, calculamos las métricas clave para entender el rendimiento real.

*   **CTR (Click-Through Rate):** `(Clics / Impresiones) * 100`
*   **CPC (Costo Por Click):** `Costo / Clics`
*   **CPA (Costo Por Adquisición/Signup):** `Costo / Signups`
*   **Conversion Rate (Tasa de Conversión):** `(Signups / Clics) * 100`

| Métrica | Campaña A (Landing Principal) | Campaña B (Blog Content) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clics** | 1,500 | 4,800 | 900 |
| **Signups** | 45 | 24 | 36 |
| **Costo** | $2,100 | $1,800 | $3,200 |
| **CTR** | **3.00%** | **4.00%** | **6.00%** |
| **CPC** | **$1.40** | **$0.38** | **$3.56** |
| **CPA** | **$46.67** | **$75.00** | **$88.89** |
| **Conv. Rate** | **3.00%** | **0.50%** | **4.00%** |

---

### 2. ¿Qué campaña escalar y cuál pausar?

La decisión debe basarse en la eficiencia del gasto (CPA) y la calidad del tráfico (intención de compra).

*   **🏆 Campaña a Escalar: Campaña A (Landing Principal)**
    *   **Justificación:** Es la campaña más equilibrada. Tiene el **CPA más bajo ($46.67)** de las campañas de alto valor, un CTR saludable (3%) y la tasa de conversión más estable (3%). Los keywords indican intención comercial ("software gestión inventario"), lo que significa que el usuario busca resolver su problema ahora.
    *   **Potencial:** Si optimizamos la landing page, hay margen para bajar ese CPA aún más.

*   **⚠️ Campaña a Revisar/Pausar: Campaña B (Blog Content)**
    *   **Justificación:** Aunque el CPC es muy barato ($0.38) y el CTR es alto (4%), la **tasa de conversión es terrible (0.5%)**. Esto indica que el tráfico es demasiado "curioso" o educativo, no comercial. Estás pagando $75 por signup, lo cual es ineficiente comparado con la Campaña A.
    *   **Acción:** No necesariamente pausar totalmente si el objetivo es branding, pero para adquisición de clientes (signups), está quemando presupuesto. Se sugiere **pausar o reducir drásticamente** para ver si el CPA global de la cuenta mejora.

*   **❓ Campaña Mixta: Campaña C (Competidor)**
    *   **Justificación:** Tiene la tasa de conversión más alta (4%), lo que significa que el tráfico es de muy alta intención (buscan cambiarte). Sin embargo, el **CPC es muy alto ($3.56)** y el CPA es el más caro ($88.89).
    *   **Acción:** Mantener, pero con cuidado. Es buena para capturar clientes que ya usan la competencia, pero es costosa. No es la prioridad para escalar con un presupuesto limitado de $5k.

---

### 3. Redistribución del Presupuesto ($5,000)

El objetivo es maximizar el número de Signups (Leads) reduciendo el CPA promedio.

**Estrategia Propuesta:**

1.  **Campaña A (Core): $3,000 (60%)**
    *   *Por qué:* Es tu motor de adquisición más eficiente. Al darle más presupuesto, podemos probar más keywords de intención comercial y escalar lo que funcione.
    *   *Meta:* Mantener CPA bajo $45 y escalar clicks.

2.  **Campaña C (Competidor): $1,500 (30%)**
    *   *Por qué:* Es un canal de ventas calientes. Aunque es caro, convierte bien. No lo eliminamos porque 36 signups son valiosos, pero limitamos el gasto para no afectar la rentabilidad.
    *   *Meta:* Buscar palabras clave de competidor más específicas para bajar el CPC.

3.  **Campaña B (Blog): $500 (10%)**
    *   *Por qué:* Se reduce de $1,800 a $500. Se usa solo para mantener visibilidad en etapas tempranas o para testear si con nuevo copy se mejora la conversión.
    *   *Meta:* Si no se logran al menos 10 signups con este presupuesto, se pasa a 0 el siguiente mes.

**Resumen de la nueva asignación:**
*   **Total:** $5,000
*   **Enfoque:** 90% del presupuesto en intención comercial (A + C), 10% en top of funnel (B).

---

### 4. Sugerencias de A/B Tests para el próximo mes

Para mejorar los números antes de gastar todo el presupuesto, prueba estas variables:

**A. En Campaña A (Landing Principal) - Enfoque en CPA**
*   **Test 1: Headline (Titular).**
    *   *Versión Actual:* Probablemente genérica (ej: "Software de Inventario").
    *   *Versión A:* Enfocada en dolor (ej: "Deja de Perder Dinero por Mal Inventario").
    *   *Versión B:* Enfocada en resultado (ej: "Controla tu Inventario en 5 Minutos").
    *   *Objetivo:* Mejorar la tasa de conversión del 3% al 4-5%.
*   **Test 2: Formulario.**
    *   ¿El signup requiere muchos campos? Prueba reducir el formulario a solo Email + Empresa. Menos fricción suele aumentar las conversiones.

**B. En Campaña B (Blog) - Enfoque en Relevancia**
*   **Test 3: Match Type de Keywords.**
    *   Probablemente estás usando "Broad Match" por el alto volumen de impresiones. Prueba cambiar a **"Phrase Match"** o **"Exact Match"**.
    *   *Objetivo:* Reducir impresiones irrelevantes y subir la tasa de conversación del 0.5%.
*   **Test 4: Mensaje del Anuncio.**
    *   Conecta el blog con la oferta. Ej: "Léiste sobre problemas de inventario? Aquí está la solución". Si no hay conversión, confirma que este canal no es viable para ventas directas.

**C. En Campaña C (Competidor) - Enfoque en CPC**
*   **Test 5: Landing Page Específica.**
    *   ¿Llevan al blog o a la landing de ventas? Prueba enviar el tráfico de "alternativa a [competidor]" a una landing que compare directamente tus precios/características vs. los de ellos.
    *   *Objetivo:* Justificar el CPA alto ($88) aumentando la tasa de conversión o el valor del cliente (LTV).

### Conclusión Ejecutiva
Tu cuenta actual tiene un **CPA promedio de ~$60**. Con la redistribución propuesta (más peso en Campaña A), el objetivo es bajar ese promedio a **$45-$50**, lo que te permitiría obtener aproximadamente **100-110 signups** con los $5,000, en lugar de las ~85 signups actuales. La Campaña B es la principal oportunidad de optimización (eliminando ruido), mientras que la A es tu activo principal a proteger y crecer.