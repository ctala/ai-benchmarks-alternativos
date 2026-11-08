# GPT-OSS 120B — sales_outreach/campaign_optimization

- model_id: `openai/gpt-oss-120b`
- success: True  | final: 7.42 | quality: 8.0
- latency_total: 91.874s | tokens_per_second: 36.6
- input_tokens: 309 | output_tokens: 3359

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

## 1️⃣ Cálculo de métricas  

| Campaña | Impresiones | Clicks | Sign‑ups | Costo ($) | **CTR** | **CPC** | **CPA** | **Conversion Rate** |
|---------|-------------|--------|----------|-----------|--------|--------|--------|----------------------|
| **A – Landing principal** | 50 000 | 1 500 | 45 | 2 100 | 1 500 ÷ 50 000 = **3 %** | 2 100 ÷ 1 500 = **$1,40** | 2 100 ÷ 45 = **$46,67** | 45 ÷ 1 500 = **3 %** |
| **B – Blog content** | 120 000 | 4 800 | 24 | 1 800 | 4 800 ÷ 120 000 = **4 %** | 1 800 ÷ 4 800 = **$0,38** | 1 800 ÷ 24 = **$75,00** | 24 ÷ 4 800 = **0,5 %** |
| **C – Competidor** | 15 000 | 900 | 36 | 3 200 | 900 ÷ 15 000 = **6 %** | 3 200 ÷ 900 = **$3,56** | 3 200 ÷ 36 = **$88,89** | 36 ÷ 900 = **4 %** |

> **Definiciones**  
> - **CTR** (Click‑Through‑Rate) = Clicks / Impresiones × 100 %  
> - **CPC** (Cost‑Per‑Click) = Costo / Clicks  
> - **CPA** (Cost‑Per‑Acquisition) = Costo / Sign‑ups  
> - **Conversion Rate** = Sign‑ups / Clicks × 100 %  

---

## 2️⃣ ¿Qué campaña escalar y cuál pausar?  

| Métrica | Campaña A | Campaña B | Campaña C |
|--------|-----------|-----------|-----------|
| **CPA (menor = mejor)** | **$46,67** | $75,00 | $88,89 |
| **Conversion Rate (mayor = mejor)** | **3 %** | 0,5 % | **4 %** |
| **CPC (menor = mejor)** | $1,40 | **$0,38** | $3,56 |
| **CTR (mayor = mejor)** | 3 % | 4 % | **6 %** |
| **Sign‑ups / $ gasto** (eficiencia) | 0,0214 sign‑ups/$ | 0,0133 sign‑ups/$ | 0,0113 sign‑ups/$ |

### 🎯 Campaña a **escalar** → **Campaña A**  
- CPA más bajo (≈ $47) → cada dólar genera más conversiones.  
- Buen conversion rate (3 %) y un CPC razonable.  
- Genera 45 sign‑ups con 2 100 $, es la **más rentable** de las tres.

### ⏸️ Campaña a **pausar** → **Campaña B**  
- Aunque tiene el CPC más barato, su CPA es alto ($75) y la tasa de conversión es muy baja (0,5 %).  
- Cada $ 1 gasta en clicks que casi nunca se convierten (solo 24 sign‑ups con 1 800 $).  
- Al pausar esta campaña recuperamos $ 1 800 que pueden reinvertirse en A y/o C.

> **Nota**: La Campaña C tiene el mejor CTR y la mayor tasa de conversión (4 %) pero su CPA es el más alto ($89) y el CPC muy costoso. No la pausamos, pero sí la **optimizamos** antes de asignarle más presupuesto.

---

## 3️⃣ Redistribución del presupuesto de $5 000  

**Situación actual (gasto total = $7 100)**  

| Campaña | Gasto actual |
|---------|--------------|
| A | $2 100 |
| B | $1 800 |
| C | $3 200 |
| **TOTAL** | **$7 100** |

### Paso 1 – Eliminar B  
- Ahorro = $1 800 → presupuesto restante = $5 000 – ($2 100 + $3 200) = **‑$300** (exceso).  
- Necesitamos recortar $300 adicionales de A o C.

### Paso 2 – Reasignar según eficiencia  
- **Eficiencia (sign‑ups/$)**:  
  - A = 45 / 2 100 ≈ 0,0214  
  - C = 36 / 3 200 ≈ 0,0113  

  → A es **≈ 2×** más eficiente que C.  

#### Propuesta de distribución (redondeada)

| Campaña | Nuevo presupuesto | Razonamiento |
|--------|-------------------|--------------|
| **A – Landing principal** | **$3 500** (≈ 70 % del total) | Aprovecha el mejor CPA y la mayor eficiencia. |
| **C – Competidor** | **$1 500** (≈ 30 % del total) | Mantiene presencia en búsquedas de competidores, pero con control de costos. |
| **B – Blog content** | **$0** (pausada) | Bajo ROI. |

**Estimación de resultados con los nuevos presupuestos** (asumiendo que los ratios se mantengan):

- **Campaña A**: $3 500 ÷ $46,67 ≈ **75 sign‑ups** (↑ +30).  
- **Campaña C**: $1 500 ÷ $88,89 ≈ **17 sign‑ups** (↓ -19).  

**Total esperado**: **≈ 92 sign‑ups** frente a los 105 actuales, pero con **costo total $5 000** (un ahorro de $2 100).  

> Si después del primer mes la campaña C logra reducir su CPA (ej. mediante pruebas A/B de landing), se puede volver a redistribuir más presupuesto a C.

---

## 4️⃣ A/B tests recomendados para el próximo mes  

### 4.1. Campaña A (Landing principal)  
| Variable | Hipótesis | Variante A | Variante B |
|----------|-----------|------------|------------|
| **Título principal** | Un mensaje de “solución rápida” aumentará la conversión. | “Gestiona tu inventario en minutos” | “Software de gestión de inventario para pymes” |
| **Formulario** | Menos campos → mayor tasa de registro. | 4 campos (nombre, email, empresa, teléfono) | 2 campos (email + nombre) |
| **CTA botón** | Texto orientado a beneficio → +CTR. | “Prueba gratis ahora” | “Comienza tu demo” |
| **Prueba social** | Mostrar testimonios mejora confianza. | Sin testimonios | 2‑3 testimonios con logotipos de clientes reales |
| **Colores del botón** | Color contrastante incrementa clics. | Azul (predeterminado) | Verde brillante |

> Métrica a medir: **Conversion Rate** (sign‑ups / clicks). Goal: +15 % respecto a la base.

### 4.2. Campaña B (Blog content) – (Si se decide mantener una pequeña parte)  
| Variable | Hipótesis | Variante A | Variante B |
|----------|-----------|------------|------------|
| **Lead magnet** | Un checklist práctico genera más leads que un e‑book. | E‑book “Guía completa de gestión de inventario” | Checklist “10 errores que debes evitar en inventario” |
| **Formato del anuncio** | Anuncio con pregunta aumenta CTR. | “¿Problemas con tu inventario? Descubre la solución” | “Software de inventario para pymes” |
| **Segmentación de palabras clave** | Palabras “cómo gestionar” atraen tráfico informativo → menor CPA. | “como gestionar inventario” | “software inventario pymes” |
| **Landing page** | Página de contenido (blog) vs página de captura dedicada. | Blog con formulario al final | Página de captura enfocada al lead magnet |

> Métrica a medir: **CPA** y **Conversion Rate**. Goal: reducir CPA a <$60 y subir conversion a >1 %.

### 4.3. Campaña C (Competidor)  
| Variable | Hipótesis | Variante A | Variante B |
|----------|-----------|------------|------------|
| **Copy del anuncio** | Enfatizar diferencia de precio/funcionalidad reduce CPA. | “¿Buscas una alternativa a [competidor]? Más barato y sin límites.” | “[Competidor] vs nuestra solución – 2× más rápido.” |
| **Oferta** | Un trial gratuito de 14 días aumenta conversiones. | “Demo gratis” | “Prueba 14 días sin compromiso” |
| **Landing page** | Landing tipo comparativa (tabla) mejora confianza. | Landing genérica del producto | Landing comparativa con tabla “Nuestro vs [competidor]” |
| **Extensiones de anuncio** | Añadir extensiones de llamada y de sitio mejora CTR. | Sin extensiones | Extensiones de llamada + enlaces de sitio |

> Métrica a medir: **CPA** y **Conversion Rate**. Goal: bajar CPA a <$70 y mantener conversion ≥3,5 %.

### 4.4. Estrategias de puja y segmentación (aplicable a todas)  
| Test | Hipótesis | Variante A | Variante B |
|------|-----------|------------|------------|
| **Tipo de puja** | “Target CPA” optimiza mejor que “Max clicks”. | Max clicks | Target CPA (valor objetivo $50) |
| **Dayparting** | Mostrar anuncios solo en horarios de mayor conversión reduce CPA. | 24 h/7 d | 8 am‑8 pm (horario laboral) |
| **Dispositivo** | Excluir dispositivos con peor performance. | Todas | Solo desktop + móvil (excluye tablet) |
| **Audiencias** | Audiencias de remarketing (visitantes del sitio) convierten mejor. | Solo búsqueda | Búsqueda + listas de remarketing (RLSA) |

> Métrica a medir: **CPA** y **ROAS** (retorno de gasto publicitario). Goal: mejorar ROAS en al menos un 20 % respecto al baseline.

---

## Resumen ejecutivo

| Acción | Razón |
|--------|-------|
| **Escalar Campaña A** | Mejor CPA ($46) y alta eficiencia (0,021 sign‑ups/$). |
| **Pausar Campaña B** | Muy bajo conversion rate (0,5 %) y CPA alto ($75). |
| **Mantener y optimizar Campaña C** | Alto CTR y conversion (4 %) pero CPA elevado; necesita pruebas de copy/landing. |
| **Redistribuir presupuesto** | $3 500 a A, $1 500 a C (total $5 000). |
| **A/B tests** | 10+ pruebas en landing, copy, formularios, ofertas y pujas para bajar CPA y subir conversiones. |

Con esta redistribución y los experimentos propuestos, el objetivo es **maximizar la generación de leads dentro del presupuesto de $5 000**, mejorando la eficiencia de gasto y preparando la base para crecer de forma sostenible en los próximos meses. 🚀