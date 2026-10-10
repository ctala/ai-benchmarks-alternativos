# Claude Fable 5.1 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.85 | quality: 10.0
- latency_total: 54.982s | tokens_per_second: 68.7
- input_tokens: 395 | output_tokens: 3777

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

# Análisis de campañas Google Ads

## 1. Métricas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** (clicks/impresiones) | 3.0% | 4.0% | **6.0%** |
| **CPC** (costo/clicks) | $1.40 | **$0.38** | $3.56 |
| **Conversion rate** (signups/clicks) | 3.0% | 0.5% | **4.0%** |
| **CPA** (costo/signups) | **$46.67** | $75.00 | $88.89 |
| Signups | 45 | 24 | 36 |

**Totales:** $7,100 gastados → 105 signups → CPA blended de **$67.62**.

> ⚠️ Ojo: gastaste $7,100 contra un presupuesto de $5,000. Al redistribuir a $5k vas a tener ~30% menos volumen, así que el objetivo realista no es "más signups" sino **mejor CPA con menos dinero**.

---

## 2. Qué escalar y qué pausar

### 🟢 Escalar: Campaña A
- Mejor CPA ($46.67), 48% más barato que C y 38% más barato que B.
- CVR sólido (3%) con intención comercial clara ("software gestión inventario").
- Genera el 43% de los signups con el 30% del gasto.
- Riesgo a vigilar: al subir presupuesto el CPC suele subir (compites por más impression share). Revisa la columna *"Impr. share perdido por presupuesto"* en Google Ads para saber cuánto margen de crecimiento real tienes.

### 🟡 Reducir y reestructurar (no pausar del todo): Campaña C
- Tiene el **mejor CVR (4%)** y el CTR más alto: la gente que busca "alternativa a X" ya está en modo compra. Probablemente son los signups que mejor convierten a pago.
- El problema es el CPC ($3.56): pagas 2.5x más por click que en A. Las keywords de competidor son caras por naturaleza.
- No la pausaría hasta saber **cuántos de esos 36 signups se convirtieron en clientes de pago**. Si su tasa trial→pago es el doble que la de A, en realidad es tu campaña más rentable.

### 🔴 Pausar o cambiar de objetivo: Campaña B
- CVR de 0.5% es la señal clave: tráfico barato pero que no quiere comprar. Son búsquedas informacionales ("cómo gestionar inventario") y tu landing les pide un signup que no están listos para dar.
- Pagas $75 por un signup que, además, probablemente es el de menor calidad de las tres.
- Si la mantienes, tiene que ser con otro rol: **alimentar audiencias de remarketing**, no generar signups directos.

---

## 3. Redistribución del presupuesto ($5,000)

| Campaña | Actual | Propuesto | % | Cambio |
|---|---|---|---|---|
| A (Landing) | $2,100 | **$2,800** | 56% | +33% |
| C (Competidor) | $3,200 | **$1,500** | 30% | -53% |
| B (Blog) | $1,800 | **$700** | 14% | -61% |

**Cómo ejecutar cada recorte:**

- **C → $1,500:** Revisa el rendimiento por keyword. Normalmente "alternativa a [competidor]" convierte mejor que "[competidor] vs" (la segunda incluye gente comparando sin intención de cambiar). Pasa a concordancia exacta, agrega negativas ("gratis", "precio", "login", "tutorial") y baja pujas en horarios flojos.
- **B → $700:** Quédate solo con "problemas inventario restaurante" (es más específica, con dolor explícito). Pausa "cómo gestionar inventario". Cambia el objetivo: la landing debe ofrecer un recurso (plantilla, checklist) a cambio de email, y esa audiencia la retargeteas con anuncios de A.

**Proyección conservadora** (asumiendo que el CPA de A sube ~10% al escalar):
- A: ~55 signups · C: ~17 · B: ~9 → **~80 signups a CPA ≈ $62**

Es decir: **-24% de signups con -30% de gasto**, y un mix de leads de mayor intención. Si después del primer mes A mantiene CPA bajo $55, muévele otros $500 desde B.

---

## 4. A/B tests para el próximo mes

Una advertencia antes: con ~45–55 signups/mes en A, solo vas a detectar diferencias grandes (>40% de lift) con significancia estadística. Prioriza tests de alto impacto, no micro-optimizaciones de color de botón.

**Campaña A (la que más vale la pena optimizar)**
1. **Headline de landing:** feature ("Software de gestión de inventario") vs. resultado ("Deja de perder dinero por quiebres de stock"). Alto impacto, fácil de medir.
2. **CTA:** "Empieza gratis" vs. "Ver demo de 2 min". Cambia el tipo de compromiso.
3. **Largo del formulario:** solo email vs. email + empresa + tamaño. Formulario corto sube CVR; el largo sube calidad. Define qué prefieres.

**Campaña C**
4. **Landing dedicada de comparación** ("[Tu producto] vs [Competidor]": tabla de features, precio, migración gratis) vs. la landing genérica. Es el test con más potencial: la gente que busca "alternativa a X" quiere ver esa comparación y hoy probablemente aterriza en una página que no la menciona.
5. **Copy del anuncio:** mencionar precio ("desde $X/mes") vs. mencionar migración ("importa tus datos en 1 click").

**Campaña B**
6. **Lead magnet vs. signup directo:** post de blog con CTA a trial vs. landing con plantilla descargable + secuencia de email. Mide signups a 30 días, no inmediatos.

**A nivel cuenta**
7. **Estrategia de puja en A:** CPC manual vs. "Maximizar conversiones" con tCPA de $50. Ya estás en el umbral de ~30+ conversiones/mes que necesita el algoritmo, pero no lo actives en C (con 36 conversiones y CPC alto el algoritmo puede dispararte el gasto).

---

## Lo más importante que te falta medir

Todo este análisis asume que **un signup vale lo mismo en las tres campañas**, y casi seguro no es así. Antes de tomar decisiones definitivas, saca para cada campaña:

- Signup → activación (usó el producto)
- Signup → cliente de pago
- Ticket promedio

Si los signups de C pagan 3x más seguido que los de B, el CPA de $89 es una ganga y el de $75 es un desperdicio. Importa esas conversiones a Google Ads como conversión secundaria y en 2 meses vas a poder optimizar por lo que realmente importa: costo por cliente, no costo por signup.