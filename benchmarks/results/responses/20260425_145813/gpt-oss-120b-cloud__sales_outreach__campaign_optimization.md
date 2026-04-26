# GPT-OSS 120B (Ollama Cloud) — sales_outreach/campaign_optimization

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.84 | quality: 8.82
- latency_total: 23.723s | tokens_per_second: 86.3
- input_tokens: 322 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

## 1️⃣ Cálculo de métricas (CTR, CPC, CPA y Conversion Rate)

| Campaña | Impresiones | Clicks | Sign‑ups | Costo ($) | **CTR** | **CPC** | **CPA** | **Conversion Rate** |
|---------|-------------|--------|----------|-----------|---------|---------|----------|---------------------|
| **A – Landing principal** | 50 000 | 1 500 | 45 | 2 100 | 1 500 ÷ 50 000 = **3 %** | 2 100 ÷ 1 500 = **1,40 $** | 2 100 ÷ 45 = **46,67 $** | 45 ÷ 1 500 = **3 %** |
| **B – Blog content** | 120 000 | 4 800 | 24 | 1 800 | 4 800 ÷ 120 000 = **4 %** | 1 800 ÷ 4 800 = **0,38 $** | 1 800 ÷ 24 = **75,00 $** | 24 ÷ 4 800 = **0,5 %** |
| **C – Competidor** | 15 000 | 900 | 36 | 3 200 | 900 ÷ 15 000 = **6 %** | 3 200 ÷ 900 = **3,56 $** | 3 200 ÷ 36 = **88,89 $** | 36 ÷ 900 = **4 %** |

> **Definiciones**  
> • **CTR (Click‑Through Rate)** = Clicks / Impresiones.  
> • **CPC (Cost per Click)** = Costo / Clicks.  
> • **CPA (Cost per Acquisition)** = Costo / Sign‑ups.  
> • **Conversion Rate** = Sign‑ups / Clicks.

---

## 2️⃣ ¿Qué campaña escalar y cuál pausar?  

### Resumen numérico rápido  

| Métrica | Mejor | Peor |
|---------|-------|------|
| **CPA (menor es mejor)** | **A – 46,67 $** | C – 88,89 $ |
| **Conversion Rate (mayor es mejor)** | **C – 4 %** | B – 0,5 % |
| **CPC (menor es mejor)** | **B – 0,38 $** | C – 3,56 $ |
| **CTR (mayor es mejor)** | **C – 6 %** | A – 3 % |

### Análisis

| Campaña | Por qué **escalar** | Por qué **pausar** |
|---------|--------------------|--------------------|
| **A – Landing principal** | • CPA más bajo (46,67 $) → generación de leads más barata. <br>• Conversión razonable (3 %). <br>• Buen equilibrio entre costo y volumen. | — |
| **B – Blog content** | — | • CPA más alto (75 $) y **conversion rate extremadamente baja** (0,5 %). <br>• Aunque el CPC es barato y el CTR es aceptable, el funnel termina en muy pocos sign‑ups. <br>• La mayor parte del gasto no se traduce en resultados. |
| **C – Competidor** | • CTR y Conversion Rate más altos (6 % y 4 %). <br>• Atrae usuarios más “calificados” (probablemente con intención de cambiar). | • CPA es el peor (88,89 $) y el CPC es >3 × el de A. <br>• Actualmente está sobre‑gastando sin producir suficientes leads. |

### Decisión

* **Escalar**: **Campaña A** (la “máquina de leads” con mejor CPA).  
* **Mantener con ajustes**: **Campaña C** (alto interés pero demasiado cara). Se puede seguir invirtiendo, pero con una estrategia de optimización (p.ej., pujas más agresivas, limitar a palabras “competidor + prueba gratis”).  
* **Pausar**: **Campaña B** – su bajo rendimiento en CPA y Conversion Rate no justifica el gasto.

---

## 3️⃣ Redistribución del presupuesto de **$5 000/mes**

### Situación actual (gasto total = $7 100)

| Campaña | Gasto actual | % del gasto |
|---------|--------------|------------|
| A | $2 100 | 29,6 % |
| B | $1 800 | 25,4 % |
| C | $3 200 | 45,1 % |
| **TOTAL** | **$7 100** | **100 %** |

### Propuesta de nuevo presupuesto

| Campaña | Nuevo presupuesto | Razonamiento |
|---------|-------------------|--------------|
| **A – Landing principal** | **$3 000** (60 % del presupuesto) | Incrementar 43 % la inversión porque su CPA es el mejor. Cada $1 000 adicional genera ≈ 21 sign‑ups (45 sign‑ups / $2 100 × $1 000). |
| **C – Competidor** | **$2 000** (40 % del presupuesto) | Mantener presencia frente al competidor, pero reducir el gasto para bajar el CPA. Cada $1 000 genera ≈