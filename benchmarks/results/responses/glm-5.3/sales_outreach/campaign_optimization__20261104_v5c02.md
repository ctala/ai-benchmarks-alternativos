# GLM 5.3 — sales_outreach/campaign_optimization

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.86 | quality: 8.0
- latency_total: 59.11s | tokens_per_second: 85.8
- input_tokens: 278 | output_tokens: 5072

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

**Nota previa importante:** Gastaste $7,100 con un presupuesto de $5,000 (42% de exceso). Antes de cualquier optimización, revisa los presupuestos a nivel de campaña — esto sugiere que están mal configurados o compartidos.

## 1. Métricas calculadas

| Métrica | Campaña A | Campaña B | Campaña C |
|---|---|---|---|
| CTR | 3.0% | 4.0% | 6.0% |
| CPC | $1.40 | $0.38 | $3.56 |
| CPA | **$46.67** | $75.00 | $88.89 |
| Tasa de conversión | 3.0% | 0.5% | 4.0% |

**Lectura rápida:**
- **A** es la más eficiente en costo por signup
- **B** tiene el click más barato ($0.38) pero convierte 6x peor que A — compras tráfico que no signup
- **C** tiene la mejor señal de calidad (CTR 6%, CVR 4%) pero el click más caro

## 2. Escalar vs. pausar

**Escalar: Campaña A** ✅
- CPA de $46.67 — 38% más barata que B y 47% más barata que C
- Generó 45 signups gastando $2,100; C gastó $3,200 para solo 36 signups
- Sus keywords ("software gestión inventario") tienen intención comercial directa — la intención coincide con el objetivo (signup)

**Pausar en su forma actual: Campaña B** ⛔
- CPA de $75 con CVR de 0.5% es la peor combinación
- El problema no es el tráfico, es el **mismatch de intención**: alguien buscando "cómo gestionar inventario" quiere información, no crear una cuenta
- No la tires: el tráfico es barato y de calidad TOF. Reestrutúrala con lead magnet o úsala como audiencia de retargeting

**Campaña C: optimizar antes de decidir** ⚠️
- La conversión (4%) no es el problema — el CPC de $3.56 sí
- Gente buscando "[competidor] vs" está en fase de decisión: es tráfico valioso
- La decisión depende de tu LTV: si un cliente vale $300+, un CPA de $89 puede ser rentable. Si vale $150, no lo es.

## 3. Redistribución propuesta ($5,000)

| Campaña | Presupuesto | % | Signups proyectados* |
|---|---|---|---|
| A | $3,200 | 64% | ~68 |
| C | $1,500 | 30% | ~17 |
| B (test lead magnet) | $300 | 6% | ~4-8 |
| **Total** | **$5,000** | 100% | **~89-93** |

*Asumiendo CPA estable.

Resultado: ~90 signups vs. los 105 actuales, pero con $2,100 menos de gasto. CPA mezclado baja de $67.62 a ~$55 (**18% más eficiente**).

**Advertencia al escalar:** el CPA de A probablemente suba al aumentar presupuesto (agotas las mejores subastas primero). Escala en incrementos de 15-20% semanal, no de golpe, y monitoriza el CPA marginal.

## 4. A/B tests priorizados para el próximo mes

**Campaña A (prioridad alta — es la que escala):**
1. **Headline de landing:** beneficio específico ("Reduce pérdidas de inventario 30%") vs. descriptivo ("Software de gestión de inventario")
2. **Fricción del formulario:** solo email vs. formulario completo — con 3% de CVR, cada punto de fricción que quites puede mover mucho
3. **Copy del anuncio:** prueba social ("+500 pymes lo usan") vs. precio/propuesta de valor

**Campaña C (alto potencial de mejora):**
4. **Landing comparativa:** tabla "nosotros vs. [competidor]" vs. landing genérica — una landing de comparación puede bajar el CPC (mejor Quality Score) y subir el CVR simultáneamente
5. **Separar ad groups:** "alternativa a X" vs. "X vs" — probablemente tienen intenciones y CPCs distintos

**Campaña B (reestructuración):**
6. **Lead magnet vs. CTA directo:** "Descarga gratis la plantilla de inventario" vs. "Crea tu cuenta" — alinea la oferta con la intención informacional
7. **Retargeting:** construye audiencia con el tráfico de B y muéstrales el mensaje de A (CPCs de $0.38 + intención ya calificada = CPA potencialmente muy bajo)

**Transversal:**
8. **Estrategia de puja en A:** CPC manual → tCPA (45 conversiones/mes es suficiente para que el algoritmo aprenda)

**Consejo metodológico:** con estos volúmenes (24-45 signups/mes), testea una variable a la vez y espera al menos 2-3 semanas o significancia estadística antes de decidir. Si testias todo a la vez, no sabrás qué funcionó.

¿Quieres que profundice en cómo estructurar el test de retargeting de B, o en qué límite de CPA ponerle a C según tu LTV?