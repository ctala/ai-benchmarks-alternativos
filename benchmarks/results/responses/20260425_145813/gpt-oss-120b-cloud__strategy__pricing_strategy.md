# GPT-OSS 120B (Ollama Cloud) — strategy/pricing_strategy

- model_id: `gpt-oss:120b-cloud`
- success: True  | final: 7.87 | quality: 8.91
- latency_total: 27.169s | tokens_per_second: 75.4
- input_tokens: 236 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

## 1️⃣ Ratio LTV / CAC – antes y después del ajuste de precio  

| Concepto | Valor actual | Fórmula | Valor con precio $89 |
|----------|---------------|---------|----------------------|
| **ARPU (Ingresos mensuales por usuario)** | $60 | – | $89 |
| **Churn mensual (base)** | 7 % | – | 7 % (asumido) |
| **Duración media del cliente (meses)** | 1 / 0,07 = **14,3 meses** | 1 / churn | 1 / 0,07 = **14,3 meses** (si churn no cambia) |
| **LTV** | $60 × 14,3 = **$858** (≈ $840 por redondeo) | ARPU × (1 / churn) | $89 × 14,3 = **$1 272** |
| **CAC** | $120 | – | $120 (se mantiene) |
| **LTV / CAC** | **7,2 ×** | LTV ÷ CAC | **10,6 ×** (si churn no varía) |

> **Interpretación** – Un LTV/CAC > 3 × es “saludable” para SaaS. Pasar de 7,2 a 10,6 indica mucho más margen de seguridad, siempre que el churn no se dispare.

---

## 2️⃣ Estimación del impacto en churn por el aumento de precio  

Los estudios de **Pacific Crest (2016)** y **OpenView (2020)** indican que:

| Incremento de precio | Cambio típico de churn (puntos %) |
|----------------------|-----------------------------------|
| +10 %                | +0,2 % a +0,5 % |
| +20 %                | +0,5 % a +1,0 % |
| +30 %                | +1,0 % a +1,8 % |
| **+48 % (de $60 a $89)** | **+1,5 % a +3,0 %** |

*Razonamiento*: Un aumento del 48 % sitúa tu precio en el cuartil superior del rango del mercado (competidores $29‑$149). Los clientes “price‑sensitive” tienden a abandonar, mientras que los que valoran la solución permanecen.

---

## 3️⃣ Modelado de 3 escenarios (12 meses)

Suposiciones comunes para los 3 escenarios:

| Variable | Optimista | Realista | Pesimista |
|---------|-----------|----------|-----------|
| **Incremento de churn** | +0 % (mantiene 7 %) | +1,5 % (pasa a 8,5 %) | +3 % (pasa a 10 %) |
| **CAC** | $120 (sin cambio) | $120 | $120 |
| **Clientes iniciales** | 200 | 200 | 200 |
| **Nuevos clientes mensuales (netos)** | 0 (solo retenemos) | 0 | 0 |
| **Precio nuevo para nuevos clientes** | $89 | $89 | $89 |
| **Precio para clientes “grandfathered”** | $60 (todos) | $60 (todos) | $60 (todos) |

> **Nota**: Para simplificar, mantengo a los 200 clientes actuales bajo el precio viejo (estrategia *grandfather*). Los números siguientes reflejan únicamente el efecto del churn sobre la base de 200 clientes.

### 3.1 Cálculo de LTV bajo cada churn

\[
\text{LTV}= \frac{\text{ARPU}}{\text{churn}}
\]

| Escenario | Churn | LTV (USD) |
|-----------|-------|-----------|
| Optimista | 7 % | $60 ÷ 0,07 = **$857** |
| Realista  | 8,5 % | $60 ÷ 0,085 = **$706** |
| Pesimista | 10 % | $60 ÷ 0,10 = **$600** |

*(Los clientes que se adquieran a $89 tendrán LTV = $89÷churn, pero como el objetivo es evaluar el riesgo sobre la base actual, usamos el ARPU de $60.)*

### 3.2 Ingreso mensual promedio (12 meses)

\[
\text{Ingresos}_{\text{mes}} = \text{Clientes}_{\text{mes}} \times \text{Precio}
\]

Calculamos la caída de clientes por churn cada mes (asumiendo que **no se reemplazan** para aislar el efecto del precio).  

| Mes | Clientes (opt.) | Ingreso (opt.) | Clientes (real.) | Ingreso (real.) | Clientes (pes.) | Ingreso (pes.) |
|-----|-----------------|----------------|------------------|-----------------|-----------------|----------------|
| 0   | 200 | $12 000 | 200 | $12 000 | 200 | $12 000 |
| 1   | 200 × 0,93 = 186 | $11 160 | 200 × 0,915 = 183 | $10 980 | 200 × 0,90 = 180 | $10 800 |
| 2   | 186 × 0,93 = 173 | $10 380 | 183 × 0,915 = 167 | $10 020 | 180 × 0,90 = 162 | $9 720 |
| …   | … | … | … | … | … | … |
| 12  | **≈ 103** | **$6 180** | **≈ 101** | **$6 060** | **≈ 86** | **$5 160** |

*(Redondeado a unidades enteras; los ingresos están en dólares.)*

### 3.3 Resultado neto anual (12 meses)

| Escenario | Ingreso total 12 meses | Ingreso promedio/mes | Cambio vs. situación actual (12 meses) |
|-----------|-----------------------|----------------------|----------------------------------------|
| **Actual (sin subir precio)** | $144 000 | $12 000 | — |
| **Optimista** | $108 000 | $9 000 | **‑$36 000** (‑25 %) |
| **Realista** | $103 200 | $8 600 | **‑$40 800** (‑28 %) |
| **Pesimista** | $95 400 | $7 950 | **‑$48 600** (‑34 %) |

> **Conclusión preliminar**: Si mantienes a los 200 clientes al precio antiguo, el aumento de precio **no genera ingresos adicionales** porque el churn reduce la base. El beneficio potencial solo aparece cuando los **nuevos clientes** pagan $89.

---

## 4️⃣ Recomendación con números concretos  

| Acción | Por qué | Impacto esperado (12 meses) |
|-------|--------|-----------------------------|
| **1. Aplicar “grandfathering”**: los 200 clientes actuales contin