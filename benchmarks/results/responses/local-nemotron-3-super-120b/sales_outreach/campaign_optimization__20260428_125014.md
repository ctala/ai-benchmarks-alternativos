# Nemotron 3 Super 120B (DGX Spark Q4_K_M) — sales_outreach/campaign_optimization

- model_id: `nemotron-3-super:120b`
- success: True  | final: 6.65 | quality: 9.0
- latency_total: 184.006s | tokens_per_second: 18.5
- input_tokens: 316 | output_tokens: 3409
- judge_score: 4.8 | justificación: 

## Respuesta completa

**1. Métricas de cada campaña**  

| Campaña | Impresiones | Clics | Sign‑ups | Costo | **CTR** | **CPC** | **Conversion Rate** (sign‑ups ÷ clics) | **CPA** (costo ÷ sign‑ups) |
|---------|-------------|-------|----------|-------|--------|--------|----------------------------------------|----------------------------|
| **A** (Landing principal) | 50 000 | 1 500 | 45 | $2 100 | 1 500 / 50 000 = **3,0 %** | $2 100 / 1 500 = **$1,40** | 45 / 1 500 = **3,0 %** | $2 100 / 45 = **$46,67** |
| **B** (Blog content) | 120 000 | 4 800 | 24 | $1 800 | 4 800 / 120 000 = **4,0 %** | $1 800 / 4 800 = **$0,38** | 24 / 4 800 = **0,5 %** | $1 800 / 24 = **$75,00** |
| **C** (Competidor) | 15 000 | 900 | 36 | $3 200 | 900 / 15 000 = **6,0 %** | $3 200 / 900 = **$3,56** | 36 / 900 = **4,0 %** | $3 200 / 36 = **$88,89** |

> **Nota:** CTR = Clics ÷ Impresiones; CPC = Costo ÷ Clics; Conversion Rate = Sign‑ups ÷ Clics; CPA = Costo ÷ Sign‑ups.

---

**2. ¿Qué campaña escalar y qué pausar?**  

| Campaña | CPA (menor = mejor) | Conversion Rate | Comentario |
|---------|--------------------|-----------------|------------|
| **A** | **$46,67** (el más bajo) | 3,0 % | Mejor relación costo‑conversión. Cada dólar genera ~0,021 sign‑up. |
| **B** | $75,00 | 0,5 % | Alto tráfico (CTR 4 %) pero muy bajo costo‑por‑conversión. |
| **C** | $88,89 | 4,0 % | Mejor CTR y conversion rate, pero CPC y CPA son los más altos; el costo por signup es casi el doble de A. |

**Decisión basada en números**

- **Escalar:** **Campaña A** – tiene el CPA más bajo y un conversion rate razonable (3 %). Cada dólar invertido genera más sign‑ups que en B o C.
- **Pausar / reducir drásticamente:** **Campaña C** – pese a su buen CTR y conversion rate, su CPA ($88,89) es casi el doble que el de A. Si el objetivo es maximizar sign‑ups dentro de un presupuesto limitado, seguir invirtiendo aquí es ineficiente.
- **Campaña B** mantiene un CPC muy bajo ($0,38) y un buen volumen de clics, pero su conversion rate es pobre (0,5 %). No se debe pausar totalmente porque puede servir para **branding** o para recopilar datos de palabras clave de cola larga, pero su asignación de presupuesto debe ser mínima si el foco es generar conversiones directas.

---

**3. Redistribución sugerida del presupuesto total de $5 000**

Objetivo: maximizar el número esperado de sign‑ups respetando el límite de $5 000.

| Campaña | CPA actual ($/signup) | Presupuesto propuesto | Sign‑ups esperados (Presupuesto ÷ CPA) |
|---------|----------------------|-----------------------|----------------------------------------|
| **A** | $46,67 | **$3 000** | 3 000 / 46,67 ≈ **64** |
| **B** | $75,00 | **$1 500** | 1 500 / 75 ≈ **20** |
| **C** | $88,89 | **$500** (o pausar) | 500 / 88,89 ≈ **6** |
| **Total** | – | **$5 000** | **≈ 90 sign‑ups** |

**Razonamiento**

- Se asigna la mayor parte del presupuesto a la campaña más eficiente (A).  
- Se mantiene una inversión moderada en B para seguir capturando tráfico de intención informativa (palabras clave tipo “cómo…”, “problemas…”) y para seguir testeando creativos y landing pages.  
- Se reduce C a un mínimo simbólico (o se pausa totalmente) porque su costo por conversión es el más alto; cualquier dólar que le quitemos a C y lo movamos a A o B generará más sign‑ups.

> **Si el objetivo fuera puramente de branding** (maximizar impresiones y clics sin fijarse en CPA), se podría invertir más en B y C. Pero dado que el KPI que nos importa son los sign‑ups, la distribución anterior es la más lógica.

---

**4. Tests A/B sugeridos para el próximo mes**

| Área | Hipótesis a testear | Variante A (control) | Variante B (test) | Métrica principal a seguir |
|------|--------------------|----------------------|-------------------|----------------------------|
| **Texto de anuncio** (Campaña A) | Un llamado a la acción más directo mejora la conversion rate sin afectar CTR significativamente. | “Descubre nuestro software de gestión de inventario – Prueba gratis” | “Gestión de inventario para PYMES – Demo gratis hoy” | Conversion Rate (sign‑ups ÷ clics) |
| **Extensión de anuncio** (Campaña A) | Añadir enlaces sitelink a casos de estudio aumenta la relevancia y reduce CPA. | Sin sitelinks | Sitelinks: “Casos de éxito”, “Precios”, “Demo en vivo” | CPA y Conversion Rate |
| **Página de aterrizaje** (Campaña A) | Un formulario más corto (solo email) incrementa la conversion rate. | Formulario con nombre, email, teléfono | Formulario solo con email | Conversion Rate y Costo por lead |
| **Match type de keywords** (Campaña B) | Cambiar de “broad match modifier” a “phrase match” reduce clics no relevantes y mejora conversion rate. | +“como gestionar inventario” (BMM) | “como gestionar inventario” (phrase) | CTR, CPC, Conversion Rate |
| **Creativo de video** (Campaña B) | Un video breve de 15 s que muestre un problema común de inventario aumenta el engagement y la conversion rate del landing page vinculado. | Anuncio de texto solo | Anuncio de video + texto | Vista completa del video, CTR, Conversion Rate del landing |
| **Segmentación de audiencia** (Campaña C) | Excluir usuarios que ya han visitado la página de precios (alta intención de compra pero bajo CPA) mejora el ROI. | Audiencia “todos los que buscan [competidor] vs” | Audiencia anterior + exclusión de visitantes de página de precios en los últimos 30 días | CPA y Conversion Rate |
| **Estrategia de puja** (Todas) | Probar “Maximizar conversiones” con un objetivo de CPA target vs. “Maximizar clics” para ver cuál entrega más sign‑ups dentro del mismo gasto. | Maximizar clics (puja manual CPC) | Maximizar conversiones (CPA objetivo $50) | CPA, total de sign‑ups, gasto |
| **Horario de publicación** (Campaña A) | Mostrar anuncios solo en horario laboral (8‑18h) reduce clics de usuarios menos propensos a convertir y baja CPC. | 24 h | 8‑18h (zona local) | CPC, CTR, Conversion Rate |

**Cómo ejecutarlos**

1. **Crear experiencias de experimento** en Google Ads (Campaña → Experimentos) para cada variable, manteniendo el 50 % del tráfico en la variante control y 50 % en la prueba.  
2. **Duración mínima**: 2 semanas o hasta alcanzar un nivel de significancia estadística (p < 0,05) en la métrica principal.  
3. **Analizar**: Si la variante B mejora la métrica principal sin empeorar gravemente los otros KPIs (p.ej., CTR no cae > 20 %), se implementa de forma permanente.  
4. **Iterar**: Los aprendizajes de cada test alimentan el siguiente ciclo (por ejemplo, si el video mejora la conversion rate en B, se prueba el mismo formato en A).

---

### Resumen rápido de acciones

| Acción | Detalle | Impacto esperado |
|-------|---------|------------------|
| **Escalar** | Aumentar presupuesto de Campaña A a ~ $3 000/mes. | +≈ 20 sign‑ups extra vs. gasto actual. |
| **Reducir** | Recortar Campaña C a ≤ $500 (o pausar). | Ahorro de ≈ $2 700 que se reasignan a A/B. |
| **Mantener** | Campaña B con presupuesto medio (~$1 500) para seguir capturando tráfico de intención informativa y seguir testeando. | Mantener volumen de clics y oportunidades de aprendizaje. |
| **Tests** | Enfocarse primero en copy y landing page de A, luego en match type y video de B, y finalmente en exclusiones de audiencia y puja inteligente. | Mejorar conversion rate y/o reducir CPA sin aumentar gasto. |

Con esta redistribución y los tests propuestos deberías pasar de los ~ 45 sign‑ups actuales (Campaña A) a **≈ 90 sign‑ups** por mes dentro del mismo presupuesto de $5 000, mientras sigues obteniendo datos valiosos para optimizar futuras campañas. ¡Éxitos!