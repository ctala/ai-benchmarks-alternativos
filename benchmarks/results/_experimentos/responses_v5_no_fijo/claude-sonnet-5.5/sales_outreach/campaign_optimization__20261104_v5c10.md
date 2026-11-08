# Claude Sonnet 5.5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 34.758s | tokens_per_second: 122.8
- input_tokens: 395 | output_tokens: 4269

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

## ⚠️ Primero: los números no cuadran con tu presupuesto
La suma del costo es **$7,100** (2,100 + 1,800 + 3,200), pero tu presupuesto es **$5,000**. Revisa si hubo sobregasto, otro presupuesto o un error de datos. Más abajo planteo la redistribución sobre $5,000.

---

## 1. Métricas por campaña

| Métrica | A (Landing) | B (Blog) | C (Competidor) | Total |
|---|---|---|---|---|
| **CTR** | 3.00% | 4.00% | 6.00% | 3.9% |
| **CPC** | $1.40 | $0.38 | $3.56 | $1.25 |
| **Conv. rate** (signups/clicks) | 3.00% | 0.50% | 4.00% | 1.85% |
| **CPA** | **$46.67** | $75.00 | $88.89 | $67.62 |

Cálculos: CTR = clicks/impresiones, CPC = costo/clicks, CVR = signups/clicks, CPA = costo/signups.

---

## 2. Qué escalar y qué pausar

**Escalar: Campaña A.**
- Tiene el CPA más bajo ($46.67), 38% menos que B y 48% menos que C.
- Su conversion rate es sólida (3%) con CPC moderado.
- Con 30% del costo aporta 43% de los signups (45 de 105).

**Pausar (o reestructurar): Campaña B.**
- Convierte a 0.5%, 6 veces menos que A. Su tráfico es barato pero informacional ("cómo gestionar...") y no tiene intención de compra.
- Tiene el 69% de los clicks pero solo el 23% de los signups.
- Su CPA de $75 es 61% mayor que el de A. Para justificarse, sus signups tendrían que convertir a cliente de pago **1.6 veces mejor** que los de A, y eso es improbable con tráfico de blog.

**Mantener con control: Campaña C.**
- Es la de mayor intención (CTR 6%, CVR 4%), pero tiene el CPA más alto ($88.89) por un CPC de $3.56.
- Solo se justifica si sus signups pagan **1.9 veces más** que los de A. Los usuarios que comparan competidores suelen estar más cerca de comprar, pero **debes verificarlo con datos** de signup → cliente de pago.
- No la pausaría sin ese dato, pero sí le pondría tope de gasto y la optimizaría.

**Advertencia:** con 24 a 45 conversiones por campaña, la muestra es pequeña y los CPA tienen margen de error considerable. Lo que más falta es el **valor real de cada signup** (tasa de activación, pago y LTV). Con eso la decisión entre B y C podría cambiar.

---

## 3. Redistribución de $5,000

| Campaña | Presupuesto | % | Signups esperados* |
|---|---|---|---|
| A – Landing principal | **$3,200** | 64% | ~60 (con CPA degradado a ~$53) |
| C – Competidor | **$1,500** | 30% | ~17 (CPA ~$89) |
| B – Blog (solo test/retargeting) | **$300** | 6% | ~4 |
| **Total** | **$5,000** | | **~80 signups, CPA ~$62** |

\*Asumo que al subir 50% el gasto en A el CPA empeora ~15% por rendimientos decrecientes.

Comparación: hoy obtienes 105 signups con $7,100 (CPA $67.6). Con este plan obtendrías ~80 con $5,000 (CPA ~$62), con 30% menos de gasto.

**Notas de ejecución:**
- Sube A de forma gradual (+20-25% por semana) para no desestabilizar el algoritmo. Revisa el *impression share* perdido por presupuesto, porque ahí está tu margen real de escala.
- En C, quita keywords con peor CPA y pon un tope de CPC.
- Con los $300 de B, deja de pagar por tráfico de blog frío. Úsalo para **retargeting** a lectores con una oferta de demo o trial, y añade negativas ("gratis", "excel", "plantilla", "pdf").
- Si el CPA de A sube de ~$60, frena el escalado y reasigna a C.

---

## 4. A/B tests para el próximo mes

**Aviso sobre muestra:** para detectar un salto de CVR de 3% a 4% necesitas ~5,300 clicks por variante, y A solo tendrá ~2,300 clicks al mes. Por eso:
- Testea **cambios grandes** (lifts de 30-50% o más), no detalles menores.
- Haz **un test a la vez por campaña**.
- Usa conversiones como métrica principal, no CTR.

**Prioridad alta**
1. **Campaña A, landing page:** formulario corto (solo email) vs. actual, o trial sin tarjeta vs. demo. *Hipótesis:* menos fricción sube el CVR de 3% a 4%+.
2. **Campaña C, landing dedicada:** página de comparación ("Migra desde [competidor] en 1 día", con tabla de comparación e importación de datos gratis) vs. la landing genérica. *Hipótesis:* un mensaje específico y una oferta de migración suben el CVR y justifican el CPC alto.
3. **Campaña A, anuncios:** headlines con beneficio cuantificado ("Reduce mermas hasta X%") vs. headlines de característica ("Software de inventario para pymes").

**Prioridad media**
4. **Estrategia de puja en A:** Maximizar conversiones vs. CPA objetivo (~$50). Cámbialo en una sola campaña, nunca en ambas a la vez.
5. **Campaña B (retargeting):** lead magnet (plantilla de inventario o checklist) vs. CTA directo a trial. Mide el costo por lead y la conversión posterior por email.
6. **Prueba social en landing A:** testimonios de pymes, logos o número de clientes arriba del fold vs. sin ellos.

**Medición clave:** configura el seguimiento de signup → activación → pago. Sin esto optimizas hacia un signup barato que quizá no vale lo mismo en cada campaña.

¿Me compartes la tasa de conversión de signup a cliente de pago y el ticket/LTV? Con eso puedo decirte con más precisión si C merece más presupuesto que A.