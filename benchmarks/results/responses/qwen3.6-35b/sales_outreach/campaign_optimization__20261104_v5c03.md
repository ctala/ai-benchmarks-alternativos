# Qwen 3.6 35B base (OpenRouter FP8) — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 8.9 | quality: 10.0
- latency_total: 15.614s | tokens_per_second: 132.9
- input_tokens: 311 | output_tokens: 2075

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

Aquí tienes el análisis detallado de tus campañas de Google Ads, seguido de recomendaciones estratégicas para optimizar tu presupuesto.

### 1. Cálculo de KPIs por Campaña

Para realizar los cálculos, utilizaremos las siguientes fórmulas estándar:
*   **CTR (Click-Through Rate):** `(Clicks / Impresiones) * 100`
*   **CPC (Costo por Clic):** `Costo / Clicks`
*   **CR (Conversion Rate):** `(Signups / Clicks) * 100`
*   **CPA (Costo por Adquisición/Signup):** `Costo / Signups`

#### **Campaña A (Landing Principal)**
*   **CTR:** `(1,500 / 50,000) * 100 =` **3.0%**
*   **CPC:** `$2,100 / 1,500 =` **$1.40**
*   **CR:** `(45 / 1,500) * 100 =` **3.0%**
*   **CPA:** `$2,100 / 45 =` **$46.67**

#### **Campaña B (Blog Content)**
*   **CTR:** `(4,800 / 120,000) * 100 =` **4.0%**
*   **CPC:** `$1,800 / 4,800 =` **$0.375**
*   **CR:** `(24 / 4,800) * 100 =` **0.5%**
*   **CPA:** `$1,800 / 24 =` **$75.00**

#### **Campaña C (Competidor)**
*   **CTR:** `(900 / 15,000) * 100 =` **6.0%**
*   **CPC:** `$3,200 / 900 =` **$3.56**
*   **CR:** `(36 / 900) * 100 =` **4.0%**
*   **CPA:** `$3,200 / 36 =` **$88.89**

---

### 2. Análisis: Escalar vs. Pausar

**Recomendación Principal:**
*   **ESCALAR:** **Campaña A (Landing Principal)** y **Campaña C (Competidor)** (con cautela).
*   **PAUSAR/OPTIMIZAR DRÁSTICAMENTE:** **Campaña B (Blog Content)**.

**Justificación Numérica:**

1.  **Eficiencia de Costo (CPA):**
    *   La **Campaña A** tiene el CPA más bajo (**$46.67**), lo que significa que obtienes leads de menor costo.
    *   La **Campaña B** tiene un CPA de **$75.00** y una tasa de conversión muy baja (0.5%). Estás pagando mucho tráfico barato (CPC $0.375) pero ese tráfico no está interesado en comprar (solo lee contenido). Es ineficiente.
    *   La **Campaña C** tiene el CPA más alto (**$88.89**), pero su tasa de conversión es la más alta (4.0%). Indica que el usuario que llega a la landing de competidor tiene mucha intención de compra.

2.  **Intención de Búsqueda:**
    *   **Campaña A:** Intención transaccional/media. Buen equilibrio.
    *   **Campaña B:** Intención informativa. El usuario busca aprender, no comprar. Por eso el CR es tan bajo.
    *   **Campaña C:** Intención transaccional alta. El usuario está comparando y listo para cambiar.

3.  **Problema de la Campaña B:**
    *   Aunque el CPC es muy barato, el CPA es alto porque el CR es ínfimo. Si no puedes mejorar el CR de la landing del blog a algo cercano al 1-2%, no deberías invertir tanto en ella.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

Objetivo: Maximizar el número total de Signups manteniendo un CPA razonable.

**Suposición:** Asumimos que el CPA objetivo máximo es **$60** (un punto medio entre A y C).

| Campaña | CPA Actual | Intención | Presupuesto Sugerido | Signups Esperados | Justificación |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A (Landing)** | $46.67 | Alta | **$2,500** | ~53 | **Estrella.** Mejor CPA. Escalar para dominar el tráfico principal. |
| **C (Competidor)** | $88.89 | Muy Alta | **$1,500** | ~17 | **Premium.** CPA alto, pero conversión excelente. Limitar para no inflar el CPA global. |
| **B (Blog)** | $75.00 | Baja | **$1,000** | ~13 | **Optimizar.** Reducir inversión. Solo mantener para capturar tráfico de topo de embudo. |
| **Total** | | | **$5,000** | **~83 Signups** | |

**Análisis del Resultado:**
*   **Signups Totales Estimados:** 53 + 17 + 13 = **83 Signups**.
*   **CPA Promedio Ponderado:** `$5,000 / 83 =` **$60.24**.

> **Nota:** Si tu CPA objetivo es más estricto (ej. < $50), deberías reducir aún más la Campaña C y la B, y poner todo en la A. Pero la Campaña C es valiosa para capturar clientes de la competencia.

---

### 4. A/B Tests Sugeridos para el Próximo Mes

Para mejorar los resultados, enfócate en estos tests:

#### **Test 1: Landing Page de la Campaña A (Optimización de Conversión)**
*   **Objetivo:** Mejorar el CR actual de 3.0% a 4.5%+.
*   **Prueba:**
    *   **Variante A (Control):** Landing actual.
    *   **Variante B:** Landing con **video demo** en el hero, testimonios más visibles, y formulario de solo 2 campos (email + nombre) en lugar de 5.
*   **Métrica Clave:** Conversion Rate. Si sube a 4.5%, tu CPA bajará a ~$31.

#### **Test 2: Estructura de la Campaña B (Blog) - Segmentación por Intención**
*   **Problema:** El blog atrae mucho tráfico pero muy poco convierte.
*   **Prueba:**
    *   **Variante A (Control):** Mismo blog actual.
    *   **Variante B:** Crear una **landing intermedia** o un **popup de salida** en el blog que ofrezca una "Checklist de Gestión de Inventario" a cambio del email. Luego, hacer un email nurture para convertirlos.
    *   **Alternativa:** Pausar las keywords de "cómo gestionar" (info) y solo pujar por "soluciones problemas inventario" (dolor).
*   **Métrica Clave:** Costo por Lead Generado (no solo signup directo).

#### **Test 3: Mensaje en Campaña C (Competidor) - Diferenciación**
*   **Objetivo:** Justificar el alto CPC ($3.56) con un CR mayor.
*   **Prueba:**
    *   **Variante A (Control):** "Alternativa a [Competidor]".
    *   **Variante B:** "Más barato y fácil que [Competidor]" o "Migra en 24h sin pérdida de datos".
*   **Métrica Clave:** CTR y CR. Si el CTR sube, el Quality Score mejorará y el CPC bajará.

#### **Test 4: Palabras Clave Negativas en Campaña B**
*   **Objetivo:** Reducir gasto innecesario.
*   **Acción:** Revisar los términos de búsqueda reales de la Campaña B y negar palabras como: "gratis", "excel", "plantilla", "pdf", "tutorial". Esto podría reducir impresiones pero mejorar el CR al eliminar tráfico puramente informativo.

### Resumen de Acción Inmediata:
1.  **Reduce el presupuesto de la Campaña B** a $1,000.
2.  **Aumenta el presupuesto de la Campaña A** a $2,500.
3.  **Mantén la Campaña C** en $1,500 pero revisa los anuncios para mejorar el CTR.
4.  **Lanza el Test 1** en la Landing de la Campaña A para intentar bajar el CPA por debajo de $40.