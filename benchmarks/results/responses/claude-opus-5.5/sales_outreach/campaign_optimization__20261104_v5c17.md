# Claude Opus 5.5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.99 | quality: 10.0
- latency_total: 46.849s | tokens_per_second: 95.5
- input_tokens: 395 | output_tokens: 4472

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

# Análisis de campañas de Google Ads

> ⚠️ **Antes de empezar:** el gasto real fue de **$7,100** ($2,100 + $1,800 + $3,200), un 42% por encima de tu presupuesto de $5,000. La redistribución implica recortar, no solo mover dinero.

---

## 1. Métricas por campaña

| Métrica | A (Landing) | B (Blog) | C (Competidor) | **Total** |
|---|---|---|---|---|
| **CTR** (clicks/impr.) | 3.0% | 4.0% | **6.0%** | 4.2% |
| **CPC** (costo/clicks) | $1.40 | **$0.38** | $3.56 | $0.99 |
| **Conversion rate** (signups/clicks) | 3.0% | 0.5% | **4.0%** | 1.4% |
| **CPA** (costo/signups) | **$46.67** | $75.00 | $88.89 | $67.62 |
| **% del gasto** | 30% | 25% | 45% | 100% |
| **% de los signups** | **43%** | 23% | 34% | 100% |

Cada campaña gana en una métrica distinta:
- **C** tiene la mejor intención (CTR 6%, conversión 4%), pero los clicks son muy caros.
- **B** tiene los clicks más baratos, pero casi nadie se registra (0.5%).
- **A** tiene el mejor equilibrio y **el CPA más bajo**, que es la métrica que importa.

---

## 2. Qué escalar y qué reducir

### ✅ Escalar: Campaña A
- CPA de $46.67: **38% más barato que B y 47% más barato que C**.
- Recibe el 30% del gasto y genera el 43% de los signups.
- Las keywords ("software gestión inventario") tienen intención de compra directa.

**Advertencia:** al escalar, el CPA marginal sube porque Google empieza a pujar por subastas menos rentables. Revisa la **cuota de impresiones (Impression Share)**. Si ya está en 80% o más, hay poco espacio para crecer. Si está por debajo del 50% por presupuesto, hay mucho margen.

### ⚠️ Reducir y optimizar: Campaña C (no pausar)
- Es la campaña más cara en CPA ($88.89) y consume el 45% del presupuesto.
- **Pero su conversión es la mejor (4%).** El problema no es el tráfico sino el CPC de $3.56.
- Alguien que busca "alternativa a [competidor]" ya está comparando para comprar. Es probable que **estos signups conviertan a cliente de pago en mayor proporción**.
- Acción: quedarte solo con las keywords de mejor rendimiento y bajar pujas.

### 🔧 Reestructurar: Campaña B (recortar fuerte, no necesariamente pausar)
- Conversión de 0.5%: **6 veces peor que A y 8 veces peor que C**.
- "Cómo gestionar inventario" es una búsqueda informativa. La gente quiere aprender, no comprar.
- Sin embargo, "problemas inventario restaurante" es un nicho que podría funcionar si se trata por separado.
- Acción: pausar las keywords genéricas y mantener solo las verticales.

### 🔑 El dato que te falta
Un signup no es un cliente. Antes de decisiones definitivas, mide la **tasa signup → pago por campaña**. Ejemplo hipotético:

| | CPA signup | Si signup→pago es... | Costo por cliente |
|---|---|---|---|
| A | $46.67 | 20% | $233 |
| C | $88.89 | 40% | $222 ← *sería la mejor* |
| B | $75.00 | 8% | $938 |

Si los usuarios de C pagan el doble que los de A, C pasaría a ser tu mejor campaña. **Configura esta medición antes de recortar C de forma agresiva.**

---

## 3. Redistribución de $5,000

| Campaña | Antes | Después | Cambio | Signups estimados* |
|---|---|---|---|---|
| **A — Landing** | $2,100 | **$2,800** | +33% | 50–56 (CPA marginal ~$50–55) |
| **C — Competidor** | $3,200 | **$1,300** | −59% | 16–19 (CPA ~$70–80 al quedarte solo con lo mejor) |
| **B — Blog (solo vertical restaurante)** | $1,800 | **$500** | −72% | 7–10 (CPA ~$50–70 con keywords específicas) |
| **Remarketing (nuevo)** | $0 | **$400** | — | 8–12 (CPA ~$35–50) |
| **Total** | $7,100 | **$5,000** | −30% | **~81–97** |

\*Estimaciones, no garantías. Valídalas en 2–3 semanas.

**Resultado esperado:** CPA mezclado de **~$52–62** frente a $67.62 actual. Tendrías menos signups en total (porque gastas un 30% menos), pero cada uno sale más barato.

**Por qué remarketing:** B generó 4,800 visitas al blog que no convirtieron. Es tráfico ya pagado que conoce tu marca. Volver a impactarlo suele ser mucho más barato que atraer tráfico nuevo. B funcionaría como fuente de audiencias y el remarketing cerraría la venta.

**Regla de ajuste:** revisa cada 2 semanas. Si el CPA marginal de A pasa de $60, deja de escalarla y mueve ese dinero a la siguiente mejor opción.

---

## 4. A/B tests para el próximo mes

### Primero, un problema de volumen
Con una conversión base del 3%, detectar una mejora del 20% (de 3.0% a 3.6%) requiere **~13,000 clicks por variante**. La campaña A genera unos 2,000 al mes, así que **no podrás validar cambios pequeños**. Conviene:
- Probar **cambios grandes** (que busquen mejoras del 50% o más, lo que requiere ~2,000 clicks por variante).
- Probar donde hay más volumen: **anuncios (CTR)**, que se miden con impresiones y no con clicks.

### Tests priorizados

| # | Test | Dónde | Hipótesis | Métrica |
|---|---|---|---|---|
| **1** | **Landing de comparación dedicada** (tabla vs. el competidor, oferta de migración gratis) vs. landing genérica | C | Quien busca "alternativa a X" quiere ver diferencias concretas. Puede bajar el CPA de C en un 30–40% | Conversion rate |
| **2** | **Smart bidding (CPA objetivo ~$50)** vs. estrategia actual, con la función Experimentos de Google Ads | A | Que el algoritmo optimice por conversión, no por clicks | CPA |
| **3** | **CTA de prueba gratis** vs. **CTA de demo** o "empieza sin tarjeta" | A | Reducir la fricción del registro | Conversion rate y signup→pago |
| **4** | **Lead magnet** (plantilla Excel de inventario para restaurantes) vs. CTA directo a signup | B | El tráfico informativo convierte mejor con un paso intermedio. Capturas el email y lo nutres después | Leads y CPA por lead |
| **5** | **Anuncios con precio** ("desde $X/mes") vs. **anuncios de dolor** ("deja de perder inventario") | A y C | El precio filtra clics de baja calidad y puede subir la conversión aunque baje el CTR | CTR y conversion rate |
| **6** | **Landing vertical para restaurantes** vs. landing genérica | B | Si el nicho funciona, abre una campaña nueva y rentable | Conversion rate |

**Orden sugerido:** empieza por el **#1 y el #2**, que tienen el mayor impacto potencial en dinero. Prueba un solo cambio por test y deja cada uno al menos 2 semanas para cubrir la variación entre días de la semana.

---

### Resumen
1. **Escala A**, pero vigila la cuota de impresiones y el CPA marginal.
2. **No mates C todavía**: puede que traiga los mejores clientes. Mide signup→pago antes de decidir.
3. **Convierte B** de canal de conversión a generador de audiencias para remarketing.
4. **Prioriza tests grandes**, porque tu volumen no permite detectar mejoras pequeñas.