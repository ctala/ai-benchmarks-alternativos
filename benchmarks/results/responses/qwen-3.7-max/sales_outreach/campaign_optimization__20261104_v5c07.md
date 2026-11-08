# Qwen 3.7 Max — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 31.134s | tokens_per_second: 54.9
- input_tokens: 311 | output_tokens: 1708

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

Aquí tienes el análisis detallado de tus campañas de Google Ads. Los datos presentan un escenario muy común en SaaS/B2B: una campaña de fondo de embudo (Competidor) con alta conversión pero costos elevados, y una de contenido (Blog) que genera volumen pero poca cualificación.

### 1. Métricas Clave por Campaña

| Métrica | Fórmula | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- | :--- |
| **CTR** | Clicks / Impresiones | **3.00%** | **4.00%** | **6.00%** |
| **CPC** | Costo / Clicks | **$1.40** | **$0.38** | **$3.56** |
| **Conversion Rate** | Signups / Clicks | **3.00%** | **0.50%** | **4.00%** |
| **CPA** | Costo / Signups | **$46.67** | **$75.00** | **$88.89** |

> **Nota de diagnóstico:** Aunque la Campaña C tiene el mejor CTR y Conversion Rate, es también la más cara por adquisición. La Campaña B tiene el CPC más bajo del mercado ($0.38), pero su tasa de conversión es 8 veces menor que la de la Landing Principal.

### 2. Estrategia: Escalar vs. Pausar

#### ✅ ESCALAR: Campaña A (Landing Principal)
*   **Justificación:** Es tu campaña más eficiente en equilibrio entre volumen y costo. Tiene el **CPA más bajo ($46.67)** y un Conversion Rate saludable del 3%. Las keywords transaccionales ("software gestion inventario") indican intención de compra clara.
*   **Acción:** Aumentar presupuesto para capturar más demanda transaccional sin disparar el CPA excesivamente.

#### ⚠️ OPTIMIZAR (No pausar aún): Campaña C (Competidor)
*   **Justificación:** Genera signups de alta calidad (CR 4%) porque el usuario ya conoce soluciones similares y está comparando. Sin embargo, el **CPA de $88.89 es casi el doble** que la Campaña A. Pausarla sería perder leads cualificados, pero escalarla tal como está quemaría el presupuesto.
*   **Acción:** Mantener con presupuesto controlado mientras se mejora el Quality Score y la relevancia de la landing para bajar el CPC de $3.56.

#### 🛑 PAUSAR / REESTRUCTURAR: Campaña B (Blog Content)
*   **Justificación:** Con un **CPA de $75.00** y solo 24 signups, estás pagando un precio de lead cualificado por tráfico informativo. El CR del 0.5% indica que la mayoría de los 4,800 clicks no tienen intención de registro inmediato. Estás gastando $1,800 (36% del budget) para obtener solo el 23% de los signups totales.
*   **Acción:** Pausar las keywords genéricas de blog. Si deseas mantener tráfico top-funnel, muévelo a una campaña separada de Display/YouTube o reduce drásticamente la puja, pero **no uses presupuesto de conversión aquí**.

### 3. Redistribución del Presupuesto ($5,000/mes)

El objetivo es maximizar signups manteniendo el CPA promedio lo más cercano posible al de la Campaña A.

| Campaña | Budget Actual | Nuevo Budget | Cambio | Justificación |
| :--- | :--- | :--- | :--- | :--- |
| **A (Landing)** | $2,100 (42%) | **$3,200 (64%)** | +$1,100 | Maximizar canal más rentable. Se proyectan ~68 signups. |
| **B (Blog)** | $1,800 (36%) | **$300 (6%)** | -$1,500 | Solo retargeting o keywords ultra-específicas. |
| **C (Competidor)** | $3,200 (64%)* | **$1,500 (30%)** | -$1,700 | Limitar gasto hasta optimizar CPC. Se proyectan ~17 signups. |
| **TOTAL** | ~~$7,100~~* | **$5,000** | - | *Nota: Tu gasto actual excede el budget declarado.* |

> ⚠️ **Alerta de Presupuesto:** Tus costos actuales suman **$7,100**, no $5,000. La redistribución anterior asume que debes recortar $2,100 inmediatamente. Si tu presupuesto real es $7,100, ajusta proporcionalmente: A=$4,500 / B=$500 / C=$2,100.

**Proyección con $5,000:** ~85 signups/mes a un CPA promedio de ~$58.82 (vs. 105 signups a $67.62 actuales). Menos volumen, pero **mucho más rentable**.

### 4. A/B Tests Sugeridos para el Próximo Mes

Dado que la prioridad es mejorar eficiencia, estos tests están ordenados por impacto esperado:

1.  **Campaña C → Landing Page Específica de Comparativa**
    *   *Hipótesis:* El CPC alto ($3.56) se debe a baja relevancia entre el anuncio "[competidor] vs" y la landing genérica.
    *   *Test:* Crear landing dedicada tipo "Nosotros vs [Competidor]" con tabla comparativa. Meta: subir Quality Score, bajar CPC a <$2.50 y mantener CR >4%.

2.  **Campaña A → Formulario de Signup**
    *   *Hipótesis:* Un CR del 3% puede mejorar reduciendo fricción.
    *   *Test:* Versión A (formulario actual) vs. Versión B (formulario simplificado con solo email + password, o social login). Meta: llevar CR al 4-5%, lo que bajaría el CPA a ~$35.

3.  **Campaña A → Copy del Anuncio**
    *   *Hipótesis:* CTR de 3% es decente pero mejorable en keywords transaccionales.
    *   *Test:* Enfocar copy en beneficio específico ("Reduce mermas 30%") vs. funcionalidad ("Software de inventario cloud"). Meta: subir CTR a >4% para ganar más impresiones premium sin aumentar puja.

4.  **Campaña B (si se mantiene) → Lead Magnet en vez de Signup directo**
    *   *Hipótesis:* El usuario de blog no quiere registrarse, quiere aprender.
    *   *Test:* Cambiar CTA de "Crear cuenta gratis" a "Descargar checklist de gestión de inventario". Capturar email para nutrir vía secuencia automatizada. Meta: aumentar tasa de captura al 3-5% y cualificar leads antes de pedir signup.

**Recomendación inmediata:** Antes de lanzar cualquier test, verifica que tu tracking de conversiones esté correctamente atribuido. Un CR de 0.5% en Blog podría ser un problema de atribución (usuarios que leen el blog y se registran días después por búsqueda directa). Configura ventanas de conversión de 30 días si aún no lo has hecho.