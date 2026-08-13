# Claude Sonnet 5 (suscripción) — sales_outreach/campaign_optimization

- model_id: `claude-sonnet-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 67.404s | tokens_per_second: 78.3
- input_tokens: 2 | output_tokens: 5281

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

# Análisis Campañas Google Ads — Mes actual

## 1. Métricas por campaña

| Campaña | CTR | CPC | CPA | Conv. rate |
|---|---|---|---|---|
| **A — Landing principal** | 3.0% (1.500/50.000) | $1.40 (2.100/1.500) | **$46.67** (2.100/45) | **3.0%** (45/1.500) |
| **B — Blog content** | 4.0% (4.800/120.000) | $0.38 (1.800/4.800) | $75.00 (1.800/24) | **0.5%** (24/4.800) |
| **C — Competidor** | 6.0% (900/15.000) | $3.56 (3.200/900) | $88.89 (3.200/36) | 4.0% (36/900) |

**Nota antes de seguir:** el gasto total fue $7.100 ($2.100+$1.800+$3.200) contra un presupuesto de $5.000 — **42% de sobregasto**. Si eso fue real, hay un problema de control de presupuesto que resolver aparte del análisis de performance (bidding automático sin tope, o falta de alertas). Si fue un mes con presupuesto ampliado puntualmente, ignora esto. Lo dejo marcado porque cambia la lectura: el CPA blended real del mes es $67.6 (7.100/105), no lo que da cada campaña por separado.

## 2. Qué escalar, qué pausar

**Escalar: Campaña A.**
Tiene el CPA más bajo ($46.67, la mitad que C) y el segundo mejor conversion rate (3.0%, casi igual al 4.0% de C). Keywords de intención comercial directa ("software gestión inventario") — la gente que busca eso ya sabe qué quiere. Además solo usó 3% de las impresiones disponibles del mercado (50K de un universo mucho mayor si C con keywords más nicho ya tiene 15K) — hay espacio para crecer sin saturar de inmediato.

**Pausar o rediseñar: Campaña B.**
El CTR es el más alto (4.0%) pero el conversion rate es **6 veces menor** que A y C (0.5% vs 3-4%). El problema no es tráfico ni interés — es **mismatch de intención**: alguien que busca "cómo gestionar inventario" está en fase de aprendizaje, no de compra. Llevarlo directo a un signup es pedirle el paso equivocado en el momento equivocado. Barato por click ($0.38) pero carísimo por resultado real ($75 de CPA) porque se desperdicia el 99.5% del tráfico.

**Mantener con ajuste: Campaña C.**
CPA más alto ($88.89) pero el mejor conversion rate (4.0%) — quien busca "alternativa a [competidor]" está en decisión final, es el lead de mayor calidad de los tres. El problema es el CPC ($3.56, 2.5x el de A) por competencia directa en esas keywords. Vale la pena mantenerla pero atacar el costo, no el volumen.

## 3. Redistribución de $5.000

Te doy dos versiones. Los números asumen que el CPA se mantiene constante al escalar, lo cual **rara vez pasa en la realidad** — al subir presupuesto agotas primero la audiencia más barata y el CPA marginal sube. Trátalos como techo optimista, no como pronóstico.

**Versión conservadora (mantiene B con presupuesto de testing):**

| Campaña | Presupuesto | % | Signups proyectados |
|---|---|---|---|
| A | $2.800 | 56% | ~60 |
| C | $1.700 | 34% | ~19 |
| B | $500 | 10% | ~7 (con la MISMA oferta — no lo hagas, ver test #2 abajo) |

**Versión agresiva (pausa B, redistribuye todo):**

| Campaña | Presupuesto | % | Signups proyectados |
|---|---|---|---|
| A | $3.250 | 65% | ~70 |
| C | $1.750 | 35% | ~20 |

CPA blended proyectado: **$56** (agresiva) vs **$67.6** (real de este mes) — con $2.100 menos de gasto. Mi recomendación es la agresiva, pero no muevas presupuesto de golpe: escala A en incrementos de 20-30% por semana y mira si el CPA se sostiene antes de seguir subiendo. Si en la semana 2 el CPA de A sube de $47 a $65, ahí está tu techo real de esa campaña — no sigas metiendo plata a ciegas.

## 4. A/B tests para el próximo mes

**Campaña A (escalar):**
- Headline de landing: enfoque específico en pymes vs. genérico "gestión de inventario"
- CTA: "Prueba gratis" vs. "Solicita demo" vs. "Empieza ahora"
- Expansión de keywords cola larga relacionadas ("sistema inventario pequeño negocio", "control stock pyme")

**Campaña B (el fix real, no solo presupuesto):**
- Cambiar el objetivo de conversión: en vez de signup directo, probar un lead magnet (checklist o guía gratis de gestión de inventario) que capture el email y nutra por email después. El tráfico es informativo — dale una oferta informativa primero.
- Landing dedicada para este tráfico, distinta de la de A (el mismatch de intención es el problema real, no el copy)
- Separar keywords puramente informativas ("cómo gestionar inventario") de las que ya muestran dolor específico ("problemas inventario restaurante") — la segunda tiene más intención y probablemente merece su propia campaña con oferta más directa

**Campaña C (bajar el costo, no el volumen):**
- Landing dedicada "vs [competidor]" con tabla comparativa — sube Quality Score, baja CPC
- Copy de anuncio: diferenciación directa vs. comparación de features vs. pricing
- Probar Target CPA bidding en vez de manual para que el sistema optimice el costo por adquisición automáticamente

**General (las tres campañas):**
- Dayparting: identificar si hay franjas horarias con mejor conversion rate
- Mobile vs. desktop: el signup puede tener fricción distinta según dispositivo — si el conversion rate cae fuerte en mobile, el problema puede ser el formulario, no el tráfico