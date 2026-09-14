# Gemini 3.8 Flash — sales_outreach/campaign_optimization

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 20.896s | tokens_per_second: 149.2
- input_tokens: 291 | output_tokens: 3117

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

Aquí tienes el análisis completo y las recomendaciones estratégicas para tus campañas.

---

### 1. Métricas clave calculadas

| Campaña | CTR | CPC | CVR (Conv. Rate) | CPA (Costo/Signup) | Gasto Actual |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **A (Landing principal)** | **3.00%** | $1.40 | **3.00%** | **$46.67** | $2,100 |
| **B (Blog content)** | **4.00%** | **$0.38** | **0.50%** | **$75.00** | $1,800 |
| **C (Competidor)** | **6.00%** | $3.56 | **4.00%** | **$88.89** | $3,200 |
| **TOTAL** | *3.95%* | *$0.99* | *1.46%* | *$67.62* | **$7,100** |

*Fórmulas aplicadas:*
* *CTR = (Clicks / Impresiones) × 100*
* *CPC = Costo / Clicks*
* *CVR = (Signups / Clicks) × 100*
* *CPA = Costo / Signups*

---

### 2. ¿Cuál escalar y cuál pausar?

#### **Escalar: Campaña A (Landing principal)**
* **Por qué:** Tiene el **CPA más bajo ($46.67)** y un CVR saludable (3.00%). Estás pagando casi la mitad por usuario registrado en comparación con la campaña de competidores.
* **Intención:** Las keywords ("software gestion inventario") capturan intención transaccional pura con un CPC razonable ($1.40).

#### **Pausar (o reestructurar por completo): Campaña B (Blog content)**
* **Por qué:** Tiene el **peor ratio de conversión (0.50%)** y un CPA elevado ($75.00). 
* **Justificación:** Estás pagando por tráfico puramente informacional ("cómo gestionar...", "problemas..."). Esas búsquedas son ideales para **SEO orgánico**, no para pagar anuncios buscando registros directos de software. Es una fuga de $1,800/mes.

#### *Nota sobre Campaña C:*
No la pauses todavía. Aunque tiene el CPA más alto ($88.89) debido al costo del click ($3.56), tiene el **mejor CVR (4.00%) y el mejor CTR (6.00%)**. La intención es altísima. El problema es el precio de la subasta, no la intención del usuario.

---

### 3. Redistribución del presupuesto ($5,000/mes)

El mes pasado gastaste **$7,100**, por lo que debías ajustar $2,100 para entrar en el presupuesto de $5,000.

| Campaña | Presupuesto | % del Total | Justificación y Resultados Estimados |
| :--- | :---: | :---: | :--- |
| **Campaña A** | **$3,200** | 64% | **Motor principal.** Estimado: ~68 signups al CPA actual ($46.67). |
| **Campaña C** | **$1,500** | 30% | **Captura de cuota.** Limitar CPCs máximos para bajar el CPA. Estimado: ~20-22 signups. |
| **Remarketing / Test** | **$300** | 6% | Campaña de Display/Search Remarketing para quienes visitaron el blog (B) o la landing pero no registraron. |
| **Campaña B** | **$0** | 0% | **PAUSAR** para tráfico frío directo a signup. |
| **TOTAL** | **$5,000** | **100%** | **~88 - 92 signups estimados** (frente a los 105 que obtuviste gastando $7,100; tu CPA global bajaría de $67.62 a ~$54.00). |

---

### 4. Propuestas de A/B Testing para el próximo mes

#### **Test 1: Campaña C (Optimización de CPA y Landing)**
* **Hipótesis:** Si enviamos el tráfico de competidores a una tabla comparativa dedicada en lugar de la home/landing genérica, el CVR subirá y el CPA bajará a menos de $60.
* **A/B Split (50/50):**
  * *Variante A (Control):* Landing actual.
  * *Variante B:* Landing page comparativa directa: *"[Tu Marca] vs [Competidor]: Por qué las PyMEs se están cambiando"* (con tabla comparativa de features y precio más transparente).

#### **Test 2: Campaña A (Estrategia de Oferta de Anuncio)**
* **Hipótesis:** Reducir la fricción inicial aumentará la tasa de conversión de la landing del 3% al 4.5%.
* **A/B Split en Anuncios y Landing:**
  * *Variante A:* "Prueba gratis 14 días" (Requiere registro completo).
  * *Variante B:* "Ver Demo Interactiva en 1 minuto - Sin tarjeta de crédito" (Micro-conversión que capture email antes de abrir la demo).

#### **Test 3: Ajuste de Bidding en Campaña C (Google Ads)**
* Probar cambiar de estrategia de puja: Si estás en *Maximizar Clics* o *Maximizar Conversiones*, cambia a **CPA Objetivo (tCPA) fijado en $60** o define un **CPC Máximo de $2.50** para evitar pagar los $3.56 actuales que inflan tu costo por adquisición.