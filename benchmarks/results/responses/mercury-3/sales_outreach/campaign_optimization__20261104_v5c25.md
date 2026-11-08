# Mercury 3 — sales_outreach/campaign_optimization

- model_id: `inception/mercury-3`
- success: True  | final: 7.99 | quality: 8.0
- latency_total: 2.974s | tokens_per_second: 433.1
- input_tokens: 256 | output_tokens: 1288

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

Aquí tienes el análisis completo con los cálculos, recomendaciones y un plan de acción para el próximo mes.

---

### 1. Métricas calculadas por campaña

**Fórmulas:**
- **CTR** = (Clicks / Impresiones) × 100  
- **CPC** = Costo / Clicks  
- **CPA** = Costo / Signups  
- **Conversion Rate (CR)** = (Signups / Clicks) × 100  

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clicks** | 1,500 | 4,800 | 900 |
| **Signups** | 45 | 24 | 36 |
| **Costo** | $2,100 | $1,800 | $3,200 |
| **CTR** | 3.0% | 4.0% | 6.0% |
| **CPC** | $1.40 | $0.375 | $3.56 |
| **CPA** | $46.67 | $75.00 | $88.89 |
| **Conversion Rate** | 3.0% | 0.5% | 4.0% |

---

### 2. ¿Cuál escalar y cuál pausar?

**Campaña A (Landing principal) → ESCALAR**  
- Mejor CPA ($46.67) y mejor conversion rate (3%) entre las tres.  
- CTR decente (3%), lo que indica relevancia de keywords.  
- Es la más eficiente: cada $1 invertido genera más signups.

**Campaña C (Competidor) → PAUSAR o REESTRUCTURAR**  
- CPA más alto ($88.89) y CPC muy alto ($3.56).  
- Aunque el CTR es alto (6%), la conversión final es baja (4% de clicks → signups, pero el costo por click es carísimo).  
- Está gastando $3,200 (64% del presupuesto) para solo 36 signups. Es la menos rentable.

**Campaña B (Blog content) → REVISAR / OPTIMIZAR**  
- CTR alto (4%) pero conversion rate muy bajo (0.5%).  
- CPA de $75, casi el doble que la campaña A.  
- El tráfico es barato (CPC $0.375) pero no convierte.  
- No la pausaría del todo, pero sí reduciría gasto y mejoraría la landing o el contenido.

---

### 3. Redistribución del presupuesto ($5,000)

| Campaña | Presupuesto actual | Nuevo presupuesto | % del total | Cambio |
|---|---|---|---|---|
| **A (Landing)** | $2,100 | **$3,000** | 60% | +$900 |
| **B (Blog)** | $1,800 | **$1,200** | 24% | -$600 |
| **C (Competidor)** | $3,200 | **$800** | 16% | -$2,400 |

**Justificación:**  
- Campaña A: recibe el mayor incremento porque es la más eficiente.  
- Campaña B: se reduce pero se mantiene para seguir recopilando datos y testear mejoras.  
- Campaña C: se reduce drásticamente, pero no se elimina por completo (puede ser útil para captar intención de compra de usuarios que ya comparan). Solo se mantiene con un presupuesto mínimo.

**Proyección estimada con nuevo presupuesto (si se mantienen las tasas actuales):**  
- A: ~64 signups (vs 45)  
- B: ~16 signups (vs 24)  
- C: ~9 signups (vs 36)  
- **Total estimado: ~89 signups** (vs 105 actuales, pero con mucho menor costo por signup).

---

### 4. A/B tests sugeridos para el próximo mes

**A. Para Campaña A (escalar):**
- **Test de landing page:** Probar 2 variantes de la página principal (una con video explicativo vs una con texto + imagen).  
- **Test de oferta:** Probar "prueba gratis de 14 días" vs "demo guiada".  
- **Test de keywords:** Añadir keywords de cola larga como "software inventario gratis pymes" y ver si mejoran el CPA.

**B. Para Campaña B (mejorar conversión):**
- **Test de contenido:** Probar 2 versiones del blog post (uno con más storytelling vs uno más técnico/numérico).  
- **Test de CTA:** Probar botón "Descargar guía" vs "Agendar llamada" al final del artículo.  
- **Test de landing de captura:** Probar un lead magnet (ebook/checklist) en lugar de pedir registro directo.

**C. Para Campaña C (reducir costo):**
- **Test de keywords negativas:** Añadir términos como "precio", "gratis", "review" para filtrar tráfico no calificado.  
- **Test de anuncios:** Probar 2 textos de anuncio: uno enfocado en "alternativa más barata" vs otro en "funcionalidades superiores".  
- **Test de oferta:** Probar "comparativa descargable" en lugar de "prueba gratis" para captar leads más calificados.

---

**Resumen ejecutivo:**  
- Escala la campaña A (landing principal).  
- Pausa o reduce drásticamente la campaña C (competidor).  
- Optimiza la campaña B (blog) con mejores CTAs y lead magnets.  
- Redistribuye el presupuesto hacia lo que ya funciona, pero sigue testeando para mejorar el resto.