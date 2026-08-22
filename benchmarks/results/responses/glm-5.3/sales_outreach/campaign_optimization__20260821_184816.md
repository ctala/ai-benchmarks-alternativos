# GLM 5.3 — sales_outreach/campaign_optimization

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 92.321s | tokens_per_second: 72.6
- input_tokens: 278 | output_tokens: 6704

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

# Análisis de tus campañas

**Nota rápida:** tu gasto real del mes fue **$7,100**, no $5,000. Asumo que $5,000 es el marco nuevo para redistribuir.

## 1. Métricas calculadas

| Métrica | Campaña A | Campaña B | Campaña C |
|---|---|---|---|
| CTR | 3.0% | 4.0% | 6.0% |
| CPC | $1.40 | $0.38 | $3.56 |
| CPA | **$46.67** ✅ | $75.00 | $88.89 |
| Tasa de conversión | 3.0% | 0.5% | **4.0%** ✅ |
| Signups por $1,000 | 21.4 | 13.3 | 11.3 |

**Blended actual:** 105 signups / $7,100 = CPA de $67.62

## 2. Cuál escalar y cuál pausar

**Escalar: Campaña A.** CPA 38% más bajo que B y 47% más bajo que C. Cada dólar produce más signups que en cualquier otra campaña.

**Pausar: Campaña B** (en su forma actual). Sí, C tiene peor CPA ($88.89 vs $75), pero la distinción clave es:

- **El problema de C es arreglable:** trae la mejor intención (CTR 6%, CVR 4%), pero paga $3.56 por click. Si bajas el CPC un 30% vía Quality Score, concordancia exacta y negativas, su CPA cae a ~$62 sin tocar la conversión.
- **El problema de B es estructural:** keywords informacionales ("cómo gestionar inventario") atraen gente que quiere *aprender*, no comprar. Optimizar la landing no cambia la intención del buscador. Un CVR de 0.5% en tráfico TOFU es normal — no es un bug, es la naturaleza del canal.

**Mantener C con presupuesto reducido y optimización agresiva.** Los switchers de competidores suelen tener LTV alto.

## 3. Redistribución de los $5,000

| Campaña | Presupuesto | % | Rol |
|---|---|---|---|
| A | $2,800 | 56% | Escalar el ganador |
| C | $1,700 | 34% | Optimizar CPC, capturar switchers |
| **Remarketing (nueva)** | $500 | 10% | Convertir visitantes que no firmaron |

**Proyección si el rendimiento se mantiene:**
- A: ~60 signups (CPA $46.67)
- C optimizada: ~19–24 signups (CPA $70–89)
- Remarketing: variable, pero con CPC bajo y CVR alta sobre los ~7,200 visitantes/mes que ya tienes

**Total estimado: ~80–85 signups a $5,000 → CPA ~$60** (vs. $67.62 actual, con 30% menos presupuesto).

⚠️ Al escalar A, el CPA casi siempre sube (expandes a audiencias menos calificadas). Revisa semanalmente, no mensualmente.

## 4. A/B tests priorizados

**1. Landing de comparación para C (mayor impacto potencial)**
Página dedicada "[Competidor] vs [Tu producto]" con tabla de features, migración fácil y testimonios de switchers — en vez de mandarlos a la landing genérica. Hipótesis: CVR 4% → 5–6%, CPA baja a ~$60–70.

**2. Landing de A: prueba social vs. fricción**
Variante con logos de clientes/número de usuarios arriba + formulario reducido (o CTA "ver demo" vs. "crear cuenta"). Hipótesis: CVR 3% → 4%+.

**3. Copy de anuncios en A**
Titular con resultado cuantificado ("Reduce errores de inventario 30%") vs. copy actual de features.

**4. Lead magnet en B (antes de matarla del todo)**
"Plantilla de inventario para restaurantes" o guía descargable vs. signup directo. Mide costo por *lead*, no por signup. Si sale bajo $8, B justifica existir como generadora de audiencia para remarketing.

**5. RLSA en A y C**
Puja +20–30% para usuarios que ya visitaron tu sitio buscando esas keywords.

**6. Concordancia exacta en C**
"[Competidor] vs" en exacta para controlar el CPC de $3.56.

## Dos verificaciones antes de ejecutar

1. **Revisa conversiones asistidas antes de pausar B.** Si el modelo es last-click, es posible que lectores del blog conviertan días después vía búsqueda de marca o directo, y ese crédito aparezca en A. Si B asiste >15% de las conversiones de A, considera mantenerla con $300–500 como alimentadora de remarketing.
2. **Reporte de términos de búsqueda en las tres campañas.** Casi siempre hay 10–20% de gasto en queries irrelevantes que se eliminan con negativas — es dinero gratis.