# Tencent Hy3 — sales_outreach/campaign_optimization

- model_id: `tencent/hy3`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 75.815s | tokens_per_second: 75.3
- input_tokens: 298 | output_tokens: 5710

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

Antes de entrar en detalle, hay un **dato crítico** que debes notar: la suma de tus costos actuales es **$7,100** (2,100 + 1,800 + 3,200), lo que significa que estás **sobrepasando tu presupuesto de $5,000 por $2,100 (42% de overspend)**. Esto es clave para la redistribución.

A continuación, los cálculos y recomendaciones:

---

### 1. Métricas de cada campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clicks** | 1,500 | 4,800 | 900 |
| **Signups** | 45 | 24 | 36 |
| **Costo** | $2,100 | $1,800 | $3,200 |
| **CTR** (Clics/Impr.) | **3.0%** | **4.0%** | **6.0%** |
| **CPC** (Costo/Clic) | **$1.40** | **$0.38** | **$3.56** |
| **CVR** (Signups/Clics) | **3.0%** | **0.5%** | **4.0%** |
| **CPA** (Costo/Signup) | **$46.67** | **$75.00** | **$88.89** |

*Definiciones rápidas: CTR = % clics; CPC = costo por clic; CVR = % conversión; CPA = costo por registro (signup).*

---

### 2. ¿Qué campaña escalar y cuál pausar? (Justificación numérica)

**🚀 Escalar: Campaña A (Landing principal)**
*   Tiene el **mejor CPA ($46.67)**, casi la mitad que la C y 38% mejor que B.
*   Su CVR (3%) es sólida para tráfico de palabras clave comerciales ("software", "pymes").
*   Es la que mejor equilibra volumen y eficiencia. Si aumentas su presupuesto, el costo por registro debería mantenerse estable o mejorar.

**⛔ Pausar / Reducir drásticamente: Campaña C (Competidor)**
*   Aunque tiene el **mejor CTR (6%) y mejor CVR (4%)** (el tráfico es de altísima intención), su **CPC es de $3.56** (2.5x más caro que A).
*   Eso la lleva a un **CPA de $88.89**, el peor de las tres. Estás pagando el doble por cada registro comparado con A.
*   *Nota estratégica:* No pausaría C para siempre porque captura intentos de cambio de competidores, pero **con un presupuesto estricto de $5,000, es la candidata a pausar o capar fuertemente** hasta optimizar su costo por clic.

**Campaña B (Blog):** No pausar, pero tampoco escalar todavía. Sus clics son baratísimos ($0.38) pero su CVR (0.5%) es muy baja. Es tráfico de "tofu" (top of funnel).

---

### 3. Redistribución del presupuesto de $5,000

Para ajustarnos al presupuesto y maximizar registros, propongo mover dinero de C hacia A, y recortar un poco B:

| Campaña | Presupuesto propuesto | Cambio vs actual | Registros estimados* |
| :--- | :--- | :--- | :--- |
| **A (Landing)** | **$3,200** | +$1,100 (escalar) | ~68 |
| **B (Blog)** | **$1,000** | -$800 (recortar) | ~13 |
| **C (Competidor)** | **$800** | -$2,400 (capar) | ~9 |
| **Total** | **$5,000** | Ajustado | **~90 signups** |

*\*Estimación usando los CPA actuales. Si pausas C por completo y pones $4,000 en A y $1,000 en B, llegarías a ~99 signups, pero perderías presencia en búsquedas de competidores.*

**Lógica:** Al poner más en A (la más eficiente) y capar C (la más cara), bajas tu CPA combinado de $67.62 actual a aproximadamente **$55 por registro**, ahorrando $2,100 al mes.

---

### 4. A/B Tests sugeridos para el próximo mes

1.  **En Campaña B (Blog) – Test de CTA / Lead Magnet:**
    *   *Hipótesis:* El CVR de 0.5% es muy bajo porque el blog es informativo.
    *   *Test:* Compara un botón de "Regístrate gratis" al final del artículo vs un "Content Upgrade" (ej: descarga una plantilla de inventario a cambio del email). Objetivo: subir CVR al 1.5-2%.

2.  **En Campaña A (Landing) – Test de propuesta de valor:**
    *   *Hipótesis:* El CVR es 3%, pero puede mejorar.
    *   *Test:* Versión A (actual) vs Versión B (con mayor prueba social, testimonios de pymes y garantía de 14 días). Objetivo: llevar CVR a 4-5% y bajar CPA.

3.  **En Campaña C (Competidor) – Landing page de comparación:**
    *   *Hipótesis:* El CPC alto se agrava porque los usuarios no ven una diferencia clara con el competidor.
    *   *Test:* Crea una página tipo "[Competidor] vs Nosotros" (tabla comparativa) solo para esta campaña. Si mejoras el CVR del 4% al 6%, el CPA bajaría de $88.89 a ~$59, justificando aumentar su presupuesto de nuevo.

4.  **Retargeting cruzado:**
    *   Usa el tráfico barato de la Campaña B (que no se convirtió) para alimentar una audiencia de retargeting con anuncios que llevan al Landing de la Campaña A. Así aprovechas los $0.38 clic para empujarlos abajo del funnel.

¿Quieres que te arme la estructura de la landing page de comparación o los textos de los anuncios A/B?