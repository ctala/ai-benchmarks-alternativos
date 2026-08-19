# Gemini 3.5 Flash Lite — sales_outreach/campaign_optimization

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 7.44 | quality: 8.0
- latency_total: 5.696s | tokens_per_second: 256.0
- input_tokens: 292 | output_tokens: 1458

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

Aquí tienes el análisis detallado de tus campañas de Google Ads y una propuesta estratégica para optimizar tu presupuesto de $5,000/mes.

---

### 1. Cálculo de Métricas por Campaña

Para evaluar el rendimiento, calculamos las siguientes métricas:
*   **CTR (Click-Through Rate):** Clicks / Impresiones
*   **CPC (Costo por Click):** Costo / Clicks
*   **CPA (Costo por Adquisición/Signup):** Costo / Signups
*   **Conversion Rate (CR):** Signups / Clicks

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clicks** | 1,500 | 4,800 | 900 |
| **Signups** | 45 | 24 | 36 |
| **Costo** | $2,100 | $1,800 | $3,200 |
| **CTR** | **3.00%** | **4.00%** | **6.00%** |
| **CPC** | **$1.40** | **$0.375** | **$3.56** |
| **CPA** | **$46.67** | **$75.00** | **$88.89** |
| **Conversion Rate** | **3.00%** | **0.50%** | **4.00%** |

---

### 2. ¿Cuál campaña escalar y cuál pausar?

#### **Campaña a ESCALAR: Campaña A (Landing principal)**
*   **Justificación:** Es la **campeona en eficiencia (CPA de $46.67)**. Aunque la Campaña C tiene mejor tasa de conversión (4%), el costo por click es extremadamente alto ($3.56), lo que encarece el resultado final. La Campaña A atrae tráfico con alta intención comercial ("software gestion inventario") a un costo razonable y con una excelente tasa de conversión del 3%. Es la que genera clientes al menor costo real para tu negocio.

#### **Campaña a PAUSAR (o reducir drásticamente): Campaña B (Blog content)**
*   **Justificación:** Es la **peor en rentabilidad (CPA de $75.00)**. Aunque tiene un CTR alto y un CPC muy barato ($0.375) porque son palabras informativas ("cómo gestionar..."), la tasa de conversión es paupérrima (0.5%). Estás pagando mucho dinero en clicks de usuarios que solo buscan información y no están listos para registrarse en un software. El tráfico de blog es mejor trabajarlo mediante SEO orgánico, no pagando Google Ads de búsqueda.

*(Nota sobre la Campaña C: No la pauses del todo porque trae usuarios muy calificados listos para comprar, pero su CPA actual de $88.89 es alto. Conviene optimizarla, no escalarla).*

---

### 3. Redistribución del presupuesto ($5,000/mes)

Actualmente estás gastando $7,100 ($2,100 + $1,800 + $3,200), lo cual excede tu presupuesto. Vamos a recortar la grasa y enfocar el dinero en lo que sí convierte.

*   **Pausar Campaña B:** $0 (Liberamos $1,800).
*   **Escalar Campaña A:** Aumentamos su presupuesto a **$3,500/mes**. (Esto te traerá aproximadamente 2,500 clicks y unos 75 signups a un CPA de $46).
*   **Optimizar Campaña C (Competencia):** Reducimos su presupuesto a **$1,500/mes** para enfocarnos solo en las palabras clave más rentables y bajar ese CPA. (A un CPA de $88, te dará unos 17 signups; si mejoras la página de destino, podrías conseguir más).

**Resultado proyectado con los $5,000:**
*   Presupuesto total: $5,000
*   Signups estimados: ~92 signups (vs. los 105 actuales gastando $7,100).
*   **Mejora clave:** Tu **CPA blended (promedio) baja de $67.61 a $54.34**, logrando mayor eficiencia con menor presupuesto.

---

### 4. Sugerencias de A/B Tests para el próximo mes

Dado que ya sabemos qué funciona, el objetivo del próximo mes es **mejorar la tasa de conversión** para abaratar aún más el CPA.

1.  **A/B Test en la Landing de la Campaña A:**
    *   *Variable:* El titular (H1) principal.
    *   *Variante A (Actual):* Enfocada en características ("Software de gestión de inventario para PyMEs").
    *   *Variante B (Nueva):* Enfocada en dolor/beneficio ("Reduce tus quiebres de stock en un 30% desde el día 1").
    *   *Por qué:* Los usuarios de esta campaña buscan soluciones directas a problemas operativos.

2.  **A/B Test en la Campaña C (Páginas de Destino / Comparativas):**
    *   *Variable:* Formato de la página para laskeywords "[Competidor] vs".
    *   *Variante A:* Landing page genérica de registro.
    *   *Variante B:* Una tabla comparativa directa (Tu Software vs. Competidor) destacando 3 ventajas clave (precio, soporte, facilidad de uso) con un botón de registro directo.
    *   *Por qué:* Quien busca comparar ya conoce al competidor; darle la comparación masticada acelera la decisión de compra y sube el Conversion Rate del 4% actual.

3.  **A/B Test de Anuncios (Responsive Search Ads) en Campaña A:**
    *   Probar extensiones de enlaces de sitios con "Prueba gratis por 14 días" vs. "Solicita una demo". Medir cuál de los dos llamados a la acción (CTA) atrae usuarios que luego se convierten mejor.