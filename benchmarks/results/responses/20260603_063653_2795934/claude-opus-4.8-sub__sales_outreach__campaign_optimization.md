# Claude Opus 4.8 (suscripción) — sales_outreach/campaign_optimization

- model_id: `claude-opus-4-8`
- success: True  | final: 7.12 | quality: 9.92
- latency_total: 43.047s | tokens_per_second: 70.5
- input_tokens: 2026 | output_tokens: 3033
- judge_score: 5.0 | justificación: 

## Respuesta completa

## 1. Métricas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** (clicks/impr) | 3.0% | 4.0% | **6.0%** |
| **CPC** (costo/click) | $1.40 | **$0.38** | $3.56 |
| **Conversion rate** (signup/click) | 3.0% | 0.5% | **4.0%** |
| **CPA** (costo/signup) | **$46.67** | $75.00 | $88.89 |
| Signups | 45 | 24 | 36 |
| Costo | $2,100 | $1,800 | $3,200 |

**Total actual: $7,100 y 105 signups → CPA mezclado $67.6.**

⚠️ Dato importante que saltó al calcular: **estás gastando $7,100, no $5,000**. Vas $2,100 sobre presupuesto. La pregunta no es solo "cómo redistribuir" sino "qué cortar para volver a $5,000".

## 2. Qué escalar y qué pausar

**Escalar → Campaña A.** Tiene el mejor CPA ($46.67, casi mitad que C) con buena conversión (3%). Es eficiente y aún tiene techo de impresiones para crecer. Cada dólar extra acá rinde más que en cualquier otra.

**Reducir/reformar → Campaña B.** El problema no es el tráfico (CPC baratísimo $0.38, CTR sano 4%), es que **convierte 8x peor** (0.5% vs 4% de C). Eso es esperable: keywords informativas ("cómo gestionar inventario") atraen gente que investiga, no que compra. Medirla por signups es injusto, **pero con $5,000 de presupuesto no podés pagar top-funnel a $75/signup**. No la pauses del todo (alimenta el funnel), pero recórtala fuerte.

**Mantener con disciplina → Campaña C.** CPA alto ($88.89) pero engañoso: keywords de competidor = **máxima intención de compra**. CTR 6% y conversión 4% (la mejor) confirman que es tráfico caliente. El problema es el CPC de $3.56 (guerra de pujas). Vale la pena, pero hay que **capar el gasto y optimizar Quality Score**, no dejarla correr a $3,200.

> Caveat clave: este análisis asume que **todos los signups valen igual**. Casi nunca es así. Un signup de C (que ya buscaba un competidor) probablemente convierte a pago mucho mejor que uno de B. Si tenés datos de signup→cliente pagado, recalculá con **CPA de cliente pagado o LTV/CAC** antes de decidir en firme.

## 3. Redistribución de $5,000

| Campaña | Actual | Propuesto | Cambio | Lógica |
|---|---|---|---|---|
| **A** | $2,100 | **$2,500** | +$400 | Escalar el ganador, mejor CPA |
| **C** | $3,200 | **$2,000** | –$1,200 | Capar pujas, intención alta pero cara |
| **B** | $1,800 | **$500** | –$1,300 | Modo mínimo + remarketing |
| **Total** | $7,100 | **$5,000** | –$2,100 | Vuelve a presupuesto |

**Signups proyectados** (asumiendo CPA estable, conservador): A ~54, C ~22, B ~7 → **~83 signups**. Bajás de 105 a ~83 pero gastás $2,100 menos: el **CPA mezclado mejora de $67.6 a ~$60**, y la mezcla queda más cargada hacia tráfico de alta intención.

Si tu meta es **volumen** y conseguís más budget, el orden de escalado es: A → C → B. Si tu meta es **eficiencia**, este reparto ya la mejora.

## 4. A/B tests para el próximo mes

**Campaña A (exprimir al ganador):**
- **Landing**: headline beneficio vs. dolor ("Controla tu inventario en minutos" vs. "Deja de perder plata por stock descuadrado").
- **CTA**: "Prueba gratis" vs. "Agenda demo" — mide cuál trae signups que convierten a pago.
- **Form length**: campos mínimos (email) vs. con campo de tamaño de empresa (califica leads).

**Campaña B (arreglar la conversión, no el tráfico):**
- **Oferta intermedia**: en vez de pedir signup directo, ofrecer lead magnet (plantilla Excel de inventario, checklist) → captura email y nutre. Test: signup directo vs. lead magnet.
- **Segmentar por intención**: separar "restaurante" en su propia landing vertical vs. landing genérica.

**Campaña C (bajar el CPC):**
- **Ad copy** que ataque la debilidad conocida del competidor (precio, soporte, complejidad) vs. copy de paridad de features — mejora CTR → sube Quality Score → baja CPC.
- **Landing de comparación** directa ("[Competidor] vs Nosotros", tabla) vs. landing genérica.

**Cross-campaña:**
- **Remarketing** sobre el tráfico barato de B (que ya gastaste) con un ad de conversión — recuperás señal de los 4,800 clicks que no convirtieron.

**Disciplina de testing**: corré un test por campaña a la vez, fijate que tengas volumen para significancia. Con ~45 signups/mes en A necesitás varias semanas por test — no cambies 3 cosas juntas o no vas a saber qué movió la aguja.

¿Tenés el dato de **signup → cliente pagado** por campaña? Con eso cambio el análisis de "CPA de signup" a "CAC real" y la recomendación de C vs B podría darse vuelta.