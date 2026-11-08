# Gemini 3.8 Flash — sales_outreach/campaign_optimization

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 26.939s | tokens_per_second: 125.0
- input_tokens: 291 | output_tokens: 3368

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

Aquí tienes el análisis detallado de tus campañas, junto con el plan de acción para optimizar tu presupuesto mensual de $5,000 (el mes pasado gastaste $7,100 en total).

---

### 1. Métricas calculadas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :---: | :---: | :---: |
| **CTR** *(Clicks / Impr)* | **3.00%** | **4.00%** | **6.00%** |
| **CPC promedio** *(Costo / Clicks)* | **$1.40** | **$0.38** | **$3.56** |
| **Tasa de Conversión (CvR)** *(Signups / Clicks)* | **3.00%** | **0.50%** | **4.00%** |
| **CPA** *(Costo / Signups)* | **$46.67** | **$75.00** | **$88.89** |

---

### 2. ¿Cuál campaña escalar y cuál pausar?

#### **Escalar: Campaña A (Landing Principal)**
* **Justificación:** Es tu campaña más eficiente en términos de costo por adquisición (**CPA de $46.67**, casi la mitad que Competidores y 38% menor que Blog). 
* Tiene un balance ideal: volumen razonable, un CPC competitivo ($1.40) y una tasa de conversión sólida del 3%. Captura intención de compra directa (Bottom-of-funnel).

#### **Pausar: Campaña B (Blog Content)**
* **Justificación:** Aunque tiene el tráfico más barato ($0.38 CPC) y buen CTR (4.00%), su **tasa de conversión es paupérrima (0.50%)**, inflando el **CPA a $75.00**.
* La intención del usuario es meramente informativa ("cómo gestionar..."), no transaccional. Estás quemando dinero pagando por lectores que no están listos para comprar un software. Este tipo de contenido debe posicionarse vía **SEO orgánico**, no con Google Ads de búsqueda directa.

*(Nota sobre Campaña C: Aunque tiene el CPA más alto de $88.89, su intención y CvR son los más altos (4.00%). No la pauses del todo; lo que la penaliza es un CPC altísimo de $3.56. Debe **reestructurarse**, no eliminarse).*

---

### 3. Redistribución del presupuesto ($5,000/mes)

El mes pasado gastaste $7,100 para conseguir 105 signups. Al ajustar al presupuesto real de $5,000, eliminando el desperdicio de B y controlando los costos de C, puedes conseguir **~90 signups** gastando un 30% menos de dinero.

| Campaña | Presupuesto asignado | % del total | Signups proyectados | Justificación |
| :--- | :---: | :---: | :---: | :--- |
| **Campaña A** | **$3,600** | 72% | ~77 | Maximizar la fuente con mejor CPA ($46.67). |
| **Campaña C** | **$1,400** | 28% | ~18 - 22 | Mantener presencia contra competidores, pero limitando el CPC con puja máxima o Target CPA para bajarlo de $3.56 a ~$2.50. |
| **Campaña B** | **$0** | 0% | 0 | **Pausada temporalmente** para frenar la fuga de presupuesto. |
| **TOTAL** | **$5,000** | 100% | **~95 - 99 signups** | Mantienes casi el mismo volumen de signups ahorrando $2,100. |

---

### 4. A/B Tests sugeridos para el próximo mes

#### **Test 1: Campaña A – Optimización de la Oferta / Fricción (Landing Page)**
* **Hipótesis:** Reducir la fricción inicial subirá la tasa de conversión del 3% al 4.5%, bajando el CPA a ~$31.
* **Variante A (Control):** Registro tradicional solicitando datos de empresa + tarjeta de crédito / formulario largo.
* **Variante B:** "Prueba gratis por 14 días - Sin tarjeta requerida" con registro vía 1-clic (Google Auth).

#### **Test 2: Campaña C – Landing Comparativa vs. Competidor**
* **Hipótesis:** Alguien que busca "alternativa a [competidor]" necesita ver de inmediato por qué tu producto es mejor/más barato antes de registrarse.
* **Variante A:** Enviar el tráfico a la landing general.
* **Variante B:** Landing específica con tabla comparativa directa: *"¿Cansado de [Competidor]? Descubre por qué 500+ empresas migraron con nosotros"* destacando ventajas en precio, soporte local y facilidad de uso.

#### **Test 3 (Estrategia de puja en Campaña C): Maximize Conversions vs. Target CPA**
* **Hipótesis:** El algoritmo está sobrepujando ($3.56 CPC). Forzar un **Target CPA de $55** reducirá el costo por clic inflando los márgenes de rentabilidad, filtrando impresiones de competidores de bajo valor.