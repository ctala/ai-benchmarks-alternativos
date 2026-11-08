# Claude Sonnet 5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 6.91 | quality: 8.0
- latency_total: 20.091s | tokens_per_second: 87.2
- input_tokens: 393 | output_tokens: 1751

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

# Análisis de Campañas Google Ads

## 1. Métricas calculadas

| Métrica | Campaña A | Campaña B | Campaña C |
|---|---|---|---|
| **CTR** (Clicks/Impresiones) | 3.0% | 4.0% | 6.0% |
| **CPC** (Costo/Clicks) | $1.40 | $0.375 | $3.56 |
| **Conv. Rate** (Signups/Clicks) | 3.0% | 0.5% | 4.0% |
| **CPA** (Costo/Signups) | $46.67 | $75.00 | $88.89 |

**Datos adicionales útiles:**
- Signups totales: 105
- Costo total: $7,100 (⚠️ ya excede tu presupuesto de $5,000 — probablemente estás gastando de más o el periodo reportado no es exactamente 30 días)

---

## 2. Qué escalar y qué pausar

### 🟢 ESCALAR: Campaña A
- **Mejor CPA** ($46.67) con volumen decente de signups (45)
- Conversion rate sólido (3%) con tráfico "frío" genérico
- Es tu campaña más eficiente en costo-por-adquisición *y* en volumen

### 🟡 OPTIMIZAR (no pausar aún): Campaña C
- CPA más alto ($88.89) pero CTR excelente (6%) y conversion rate excelente (4%)
- El problema no es la intención de búsqueda (la gente que busca "alternativa a X" convierte bien), sino el **CPC caro** ($3.56) — probablemente por competencia en keywords de marca de terceros
- Acción: negociar pujas, revisar Quality Score, o segmentar mejor el mensaje del anuncio

### 🔴 PAUSAR o rediseñar completamente: Campaña B
- CTR más alto (4%) = el anuncio es atractivo, pero...
- **Conversion rate de solo 0.5%** = hay un desajuste brutal entre expectativa y landing page
- Keywords como "como gestionar inventario" atraen tráfico informativo (TOFU), no gente lista para registrarse
- CPA de $75 con solo 24 signups es ineficiente dado el volumen de clicks (4,800)

**Diagnóstico clave:** Campaña B está atrayendo gente en fase de investigación. Necesita un lead magnet (ebook, checklist) ANTES de pedir signup directo, no la misma landing que A y C.

---

## 3. Redistribución de presupuesto ($5,000)

| Campaña | Presupuesto actual | Nuevo presupuesto | Cambio | Razón |
|---|---|---|---|---|
| A | $2,100 | **$2,800** (56%) | +33% | Mejor CPA, escalar lo que funciona |
| B | $1,800 | **$700** (14%) | -61% | Reducir drásticamente hasta arreglar el funnel |
| C | $3,200 | **$1,500** (30%) | -53% | Mantener pero reducir hasta bajar el CPC |

**Lógica:** No pauso C del todo porque tiene el mejor conversion rate — solo necesita ser más eficiente en costo. Reduzco B agresivamente porque el problema es estructural (landing/oferta), no de presupuesto.

---

## 4. A/B Tests sugeridos para el próximo mes

### Para Campaña A (escalar con inteligencia)
- **Test de landing:** versión actual vs. una con prueba social (testimonios/logos de clientes) arriba del fold
- **Test de CTA:** "Empieza gratis" vs. "Solicita demo" vs. "Prueba 14 días"

### Para Campaña B (arreglar el funnel)
- **Test de oferta:** Landing de signup directo vs. Landing con lead magnet ("Descarga la guía: Cómo reducir mermas de inventario en restaurantes")
- **Test de keyword intent:** Separar keywords informativas ("como gestionar inventario") de keywords con intención comercial ("problemas inventario restaurante") en campañas distintas, con landings diferentes para cada una

### Para Campaña C (bajar CPC sin perder conversión)
- **Test de copy del anuncio:** Mensaje directo comparativo ("[Tu producto] vs [Competidor]: Tabla comparativa") vs. mensaje de diferenciación ("La alternativa que [Competidor] no te ofrece")
- **Test de landing dedicada:** Crear landing específica de comparación vs. seguir usando la landing principal — esto puede mejorar Quality Score y bajar CPC

### Test transversal (las 3 campañas)
- **Test de formulario:** Signup de 1 campo (solo email) vs. formulario actual — para ver si el conversion rate de B mejora al reducir friction, y si A/C se mantienen estables o mejoran también

---

**Próxima revisión sugerida:** en 2-3 semanas, no esperar el mes completo, para matar rápido lo que no funcione en B y C.