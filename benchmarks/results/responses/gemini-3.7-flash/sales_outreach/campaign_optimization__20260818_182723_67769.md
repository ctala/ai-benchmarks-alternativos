# Gemini 3.7 Flash — sales_outreach/campaign_optimization

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 17.694s | tokens_per_second: 162.9
- input_tokens: 291 | output_tokens: 2883

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

Aquí tienes el análisis completo y el plan de acción estratégico para tu presupuesto de **$5,000/mes**.

---

### 1. Métricas Clave por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :---: | :---: | :---: |
| **CTR** *(Clicks / Impr)* | **3.00%** | **4.00%** | **6.00%** |
| **CPC** *(Costo / Clicks)* | **$1.40** | **$0.38** | **$3.56** |
| **CPA** *(Costo / Signups)* | **$46.67** | **$75.00** | **$88.89** |
| **CvR** *(Signups / Clicks)* | **3.00%** | **0.50%** | **4.00%** |

---

### 2. ¿Cuál escalar y cuál pausar? (Justificación)

* **ESCALAR: Campaña A (Landing Principal)**
  * **Por qué:** Es tu campaña más eficiente en costo-beneficio. Genera un **CPA de $46.67** (38% más barato que B y 47% más barato que C) con un sólido ratio de conversión del **3.00%**. Demuestra una clara intención comercial a un costo razonable ($1.40 CPC).
* **PAUSAR: Campaña B (Blog Content)**
  * **Por qué:** Aunque tiene el CPC más bajo ($0.38), su tasa de conversión es crítica (**0.50%**), lo que infla su **CPA a $75.00**. Los usuarios con intención puramente informacional ("cómo gestionar...") consumen contenido pero no compran de inmediato. Este tipo de tráfico debe capturarse orgánicamente (SEO), no pagando en Google Search sin una estrategia clara de captura de leads.
* **OPTIMIZAR (No pausar aún): Campaña C (Competidor)**
  * **Por qué:** Su CPA es el más alto ($88.89) por el costo del clic ($3.56), pero tiene el **mayor Conversion Rate (4.00%)** y el **mayor CTR (6.00%)**. Estos usuarios están al final del embudo (*ready to buy*). Si la apagas, dejas clientes calificados en la mesa; lo que necesitas es optimizar la conversión para bajar el CPA.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

El mes pasado gastaste $7,100. Ajustando al límite real de $5,000 y maximizando signups:

| Campaña | Presupuesto Asignado | % Total | Signups Estimados | Rol Estratégico |
| :--- | :---: | :---: | :---: | :--- |
| **Campaña A** | **$3,400** | 68% | ~73 | **Core de adquisición:** Maximizar volumen al menor costo. |
| **Campaña C** | **$1,300** | 26% | ~15-20 | **Captura de alta intención:** Tráfico calificado de competidores. |
| **Remarketing / Test** | **$300** | 6% | ~5-8 | **Retargeting Display/Search** para quienes visitaron y no convirtieron. |
| **Campaña B** | **$0** | 0% | 0 | **Pausada** en Search pagado. |
| **TOTAL** | **$5,000** | **100%** | **~95-100 signups** | *(Vs. 105 signups anteriores pero gastando $2,100 menos)* |

---

### 4. Propuestas de A/B Testing para el Próximo Mes

#### Test 1: Campaña C (Optimización de Landing de Comparativa)
* **Hipótesis:** Enviar el tráfico de competidores a una landing específica de comparación en vez de la home/genérica aumentará la CvR del 4% al 6%, bajando el CPA a ~$60.
* **Variante A (Control):** Landing estándar actual.
* **Variante B (Test):** Landing *"[Tu Marca] vs [Competidor]"* con una tabla comparativa clara de funciones, pricing más transparente y una oferta de "Migración gratuita de datos".

#### Test 2: Campaña A (Fricción en el Signup)
* **Hipótesis:** Reducir los pasos para registrarse aumentará el conversion rate.
* **Variante A (Control):** Formulario estándar (Email + Nombre + Teléfono + Empresa + Tamaño).
* **Variante B (Test):** Signup en 1 clic con Google/Microsoft SSO o pedir solo *Email de trabajo* en el primer paso y el resto de datos *onboarding* post-registro.

#### Test 3: Campaña C (Keywords Match Types & Negativas)
* **Hipótesis:** Restringir concordancias amplias a **Frase o Exacta** y añadir negativas agresivas (ej. "soporte", "teléfono", "login", "facturación") reducirá clics basura de usuarios existentes del competidor, bajando el CPC de $3.56 a <$2.80.