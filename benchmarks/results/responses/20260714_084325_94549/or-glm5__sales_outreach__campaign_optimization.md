# GLM 5 — sales_outreach/campaign_optimization

- model_id: `z-ai/glm-5`
- success: True  | final: 6.76 | quality: 8.0
- latency_total: 169.113s | tokens_per_second: 25.4
- input_tokens: 271 | output_tokens: 4292
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y recomendaciones prácticas para la optimización de campañas.

## Respuesta completa

Aquí tienes el análisis completo de tus campañas de Google Ads.

### 1. Métricas Calculadas

Aquí están los KPIs clave para cada campaña:

| Métrica | **Campaña A** (Landing) | **Campaña B** (Blog) | **Campaña C** (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR (Click-Through Rate)** | **3.00%** (1,500/50,000) | **4.00%** (4,800/120,000) | **6.00%** (900/15,000) |
| **CPC (Costo por Clic)** | **$1.40** ($2,100/1,500) | **$0.38** ($1,800/4,800) | **$3.56** ($3,200/900) |
| **Tasa de Conversión** | **3.00%** (45/1,500) | **0.50%** (24/4,800) | **4.00%** (36/900) |
| **CPA (Costo por Adquisición)**| **$46.67** ($2,100/45) | **$75.00** ($1,800/24) | **$88.89** ($3,200/36) |

**Observación importante:** Tu gasto total actual es de **$7,100** ($2,100 + $1,800 + $3,200), lo cual supera tu presupuesto de $5,000. Estás gastando un 42% más de lo presupuestado.

---

### 2. ¿Cuál campaña escalar y cuál pausar?

**Escalar: Campaña A (Landing principal)**
*   **Justificación:** Es la campaña más eficiente y rentable. Tiene el **CPA más bajo ($46.67)** y una sólida tasa de conversión del 3%. Los keywords son de "fondo de embudo" (el usuario busca software), lo que indica intención de compra clara. Es tu motor de crecimiento principal.

**Pausar/Optimizar: Campaña B (Blog content)**
*   **Justificación:** Aunque el tráfico es barato (CPC $0.38), la calidad del tráfico es muy baja para el objetivo de "Signups". La tasa de conversión es mínima (0.5%), resultando en un **CPA de $75**, casi el doble que la Campaña A.
*   *Nota:* Los keywords son informativos ("cómo gestionar"), por lo que el usuario está buscando respuestas, no comprando software. Gastar $1,800 aquí para obtener solo 24 signups no es rentable comparado con la A.

**Estrategia con Campaña C (Competidor):**
*   Esta campaña es compleja. Tiene la **mejor tasa de conversión (4%)** y el mejor CTR (6%), lo que indica que el tráfico es muy relevante (gente comparando opciones). Sin embargo, el **CPC es muy alto ($3.56)**, lo que dispara el CPA a **$88.89**.
*   **Decisión:** No la escalaría agresivamente, pero tampoco la pausaría del todo. Necesita optimización de pujas (bid adjustment) para bajar el CPC, ya que la intención de compra es altísima.

---

### 3. Redistribución del Presupuesto ($5,000)

El objetivo es maximizar signups manteniendo la rentabilidad. Dado que la Campaña A es la ganadora clara en eficiencia, la mayoría del presupuesto debe ir allí.

**Propuesta de distribución:**

1.  **Campaña A (Principal): $3,500 (70%)**
    *   Al mantener el CPA de $46.67, con $3,500 podrías obtener aprox. **75 signups**.
2.  **Campaña C (Competidor): $1,000 (20%)**
    *   Es arriesgada por el CPC alto, pero la conversión es buena. Reducir presupuesto fuerza al algoritmo a buscar solo las subastas más baratas o relevantes. Con $1,000 buscarías optimizar el CPA antes de inyectar más dinero.
3.  **Campaña B (Blog): $500 (10%)** o **Pausada**.
    *   Si decides mantenerla por temas de branding o remarketing, limita el daño a $500. Si tu prioridad es el retorno de inversión (ROI) inmediato, **pásala a $0 y reasigna ese $500 a la Campaña A**.

*Proyección con esta distribución (Estimado):*
*   Campaña A: ~75 signups.
*   Campaña C: ~11-15 signups (si logramos bajar un poco el CPC).
*   **Total: ~86-90 signups** vs los 105 actuales (que te cuestan $7,100). Gastarías $2,100 menos por casi el mismo resultado, o podrías usar ese dinero extra en la Campaña A para subir a más de 100 signups.

---

### 4. A/B Tests sugeridos para el próximo mes

**Para la Campaña A (La ganadora):**
*   **Test de Landing Page:** Prueba un formulario más corto (solo email y nombre) vs el actual. Si reduces la fricción, podrías subir la conversión del 3% al 5%.
*   **Test de Anuncios:** Prueba diferentes Call to Action (CTA). Ejemplo: "Prueba Gratis" vs "Ver Demo" vs "Descargar Guía".

**Para la Campaña B (La problemática):**
*   **Cambio de Objetivo:** El usuario busca información ("cómo gestionar"). No los obligues a hacer signup directamente.
*   **Test de Oferta:** Cambia el objetivo de la página. En lugar de "Sign up", ofrece un **Lead Magnet** (ej. "Descarga nuestra plantilla de inventario gratis" o "Calculadora de pérdidas"). Capta el lead primero y nútrelo por email.

**Para la Campaña C (La cara):**
*   **Test de Pujas:** Intenta una estrategia de **Target CPA** (Objetivo de costo por adquisición). Fija un objetivo de $60. Google intentará conseguir ese costo, evitando que pagues $3.56 por clic.
*   **Test de Landing:** Crea una página específica de "Comparativa". Si buscan "alternativa a X", muéstrales una tabla comparativa honesta donde tu software gane en precio o facilidad de uso. Esto suele disparar la conversión.