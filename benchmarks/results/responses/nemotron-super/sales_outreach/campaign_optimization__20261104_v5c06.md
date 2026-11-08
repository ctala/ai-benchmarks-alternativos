# Nemotron 3 Super — sales_outreach/campaign_optimization

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 9.35 | quality: 10.0
- latency_total: 4.193s | tokens_per_second: 335.5
- input_tokens: 316 | output_tokens: 1407

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

Aquí tienes el análisis completo de tus campañas de Google Ads basado en los datos proporcionados.

### 1. Cálculo de Métricas por Campaña

| Métrica | Campaña A (Landing Principal) | Campaña B (Blog Content) | Campaña C (Competidor) |
| :--- | :---: | :---: | :---: |
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clics** | 1,500 | 4,800 | 900 |
| **Signups (Conversiones)** | 45 | 24 | 36 |
| **Costo** | $2,100 | $1,800 | $3,200 |
| **CTR** (Clics / Imp.) | **3.00%** | **4.00%** | **6.00%** |
| **CPC** (Costo / Clics) | **$1.40** | **$0.375** | **$3.56** |
| **Conversion Rate** (Signups / Clics) | **3.00%** | **0.50%** | **4.00%** |
| **CPA** (Costo / Signups) | **$46.67** | **$75.00** | **$88.89** |

---

### 2. ¿Qué escalar y qué pausar? (Justificación)

**✅ Escalar: Campaña A (Landing Principal)**
*   **Justificación:** Tiene el **CPA más bajo ($46.67)** y una tasa de conversión sólida (3%). Aunque el volumen es medio, es la única campaña que está generando clientes de forma eficiente en términos de costo. Cada signup te cuesta casi la mitad que en la Campaña C.
*   **Potencial:** Tiene espacio para crecer (solo 50,000 impresiones vs 120,000 de la B).

**⏸️ Pausar (o reducir drásticamente): Campaña B (Blog Content)**
*   **Justificación:** Aunque tiene el CPC más barato ($0.37) y mucho tráfico, su **tasa de conversión es pésima (0.5%)**. El tráfico de blog suele ser informativo ("cómo hacer X"), no transaccional ("comprar software"). Estás pagando por visitas que no se convierten. El CPA de $75 es muy alto considerando la calidad del lead.

**⚠️ Mantener con cautela / Optimizar: Campaña C (Competidor)**
*   **Justificación:** Tiene la mejor tasa de conversión (4%) y un CTR excelente (6%), lo que indica alta intención de compra. Sin embargo, el **CPA es el más alto ($88.89)** debido a un CPC muy caro ($3.56).
*   **Decisión:** No pausar por completo porque captura clientes que buscan activamente cambiar de proveedor, pero hay que optimizar las pujas para bajar el CPC.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

Tu gasto actual fue de $7,100 ($2,100 + $1,800 + $3,200), por lo que ya estás por encima del presupuesto. Para ajustarnos a los $5,000 y maximizar el ROI, propongo la siguiente distribución:

| Campaña | Presupuesto Actual | Presupuesto Propuesto | Cambio | Razón |
| :--- | :---: | :---: | :---: | :--- |
| **Campaña A** | $2,100 | **$2,500** | +$400 | Escalar lo que funciona (mejor CPA). |
| **Campaña B** | $1,800 | **$500** | -$1,300 | Reducir drásticamente (baja conversión). |
| **Campaña C** | $3,200 | **$2,000** | -$1,200 | Reducir para bajar el CPA promedio. |
| **Total** | **$7,100** | **$5,000** | **-$2,100** | Ajuste al límite mensual. |

**Estrategia:** Al quitar presupuesto de la B (que no convierte) y de la C (muy cara), liberamos fondos para meter más dinero en la A, que es tu motor de crecimiento eficiente.

---

### 4. Sugerencias de Pruebas A/B para el próximo mes

Para mejorar el rendimiento general, sugiero las siguientes pruebas:

**Para la Campaña A (Escalar volumen):**
*   **Anuncios:** Probar dos versiones del copy. Una enfocada en "Ahorro de tiempo" y otra en "Reducción de errores de inventario". Ver cuál genera más clics con la misma intención.
*   **Landing Page:** Probar el posicionamiento del botón de registro (CTA) y el título principal (H1).

**Para la Campaña C (Bajar Costo):**
*   **Pujas:** Probar cambiar de "Maximizar clics" a "Maximizar conversiones" con un CPA objetivo (Target CPA) para obligar a Google a no pujar tan caro en palabras clave de competidor.
*   **Anuncios:** Incluir un comparativo directo en el texto del anuncio (ej: "20% más barato que [Competidor]") para mejorar el CTR y calificar mejor al usuario antes del clic.

**Para la Campaña B (Si decides mantenerla):**
*   **Landing Page:** En lugar de enviar al usuario al artículo del blog, prueba enviarlo a una landing de "Lead Magnet" (ej: descarga una guía de inventario) para capturar el email y nutrirlo, en lugar de esperar un signup inmediato de software.
*   **Palabras clave:** Agregar palabras clave negativas como "gratis", "plantilla", "excel" para evitar atraer gente que no quiere pagar software.