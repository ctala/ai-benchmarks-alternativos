# Gemini 3.7 Flash — sales_outreach/campaign_optimization

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 15.011s | tokens_per_second: 136.2
- input_tokens: 291 | output_tokens: 2044

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

Aquí tienes el análisis detallado de tus campañas, junto con la estrategia para optimizar tu nuevo presupuesto de $5,000/mes.

---

### 1. Métricas clave por campaña

| Campaña | CTR | CPC | Tasa de Conversión (CR) | CPA (Costo por Signup) |
| :--- | :---: | :---: | :---: | :---: |
| **A (Landing principal)** | **3.00%** | $1.40 | **3.00%** | **$46.67** *(Mejor)* |
| **B (Blog content)** | 4.00% | **$0.38** | 0.50% | **$75.00** |
| **C (Competidor)** | **6.00%** | $3.56 | **4.00%** | **$88.89** *(Peor)* |

*Fórmulas aplicadas: CTR = Clicks/Impresiones | CPC = Costo/Clicks | CR = Signups/Clicks | CPA = Costo/Signups*

---

### 2. ¿Cuál escalar y cuál pausar/reestructurar?

* **ESCALAR: Campaña A (Landing principal