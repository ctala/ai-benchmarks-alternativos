# Claude Sonnet 5.5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 35.968s | tokens_per_second: 122.4
- input_tokens: 395 | output_tokens: 4404

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

**Dato importante:** el gasto total fue **$7,100**, no $5,000. Te pasaste del presupuesto por $2,100 (42%). Conviene revisar los límites de presupuesto diario, porque Google puede gastar hasta 2x el diario en un día.

## 1. Métricas por campaña

| Métrica | A (Landing) | B (Blog) | C (Competidor) | Total |
|---|---|---|---|---|
| **CTR** | 3.0% | 4.0% | 6.0% | 4.1% |
| **CPC** | $1.40 | $0.38 | $3.56 | $1.03 |
| **Conversion rate** | 3.0% | 0.5% | 4.0% | 1.5% |
| **CPA** | **$46.67** | $75.00 | $88.89 | $67.62 |
| Signups | 45 | 24 | 36 | 105 |
| % del gasto | 30% | 25% | 45% | 100% |
| % de signups | 43% | 23% | 34% | 100% |

Fórmulas: CTR = clicks/impresiones, CPC = costo/clicks, CVR = signups/clicks, CPA = costo/signups.

## 2. Escalar y pausar

**Escalar: Campaña A.**
- Tiene el mejor CPA ($46.67), 48% menor que C y 38% menor que B.
- Genera 43% de los signups con solo 30% del gasto.
- Sus keywords tienen intención comercial ("software", "pymes").
- Cuidado: al escalar, el CPA suele subir porque entras a keywords o audiencias menos eficientes. Sube el presupuesto de forma gradual (~20-30% por semana) y vigila el CPA.

**Pausar o recortar fuerte: Campaña C en su forma actual.**
- Es la campaña más cara: 45% del gasto y el peor CPA ($88.89).
- El problema no es la conversión (4%, la mejor), sino el CPC de $3.56, que es 2.5x el de A.
- Es más recuperable que B porque el embudo funciona. Yo no la eliminaría, sino que la limitaría con un tope de CPA y pujas más bajas (ver punto 3).

**Reducir al mínimo: Campaña B.**
- Tiene el peor CVR (0.5%), 6x peor que A. Es tráfico informacional, de gente que busca "cómo hacer" algo y no comprar.
- Su CPA ($75) es mejor que el de C solo porque el clic es barato.
- Tiene valor como top-of-funnel y retargeting, pero no merece más del 10% del presupuesto como adquisición directa.

**Advertencia:** estos números son de signups, no de clientes de pago. Si los usuarios de C (alta intención, vienen comparando) pagan mucho más que los de A, la conclusión podría cambiar. Antes de decidir en firme, mira signup→pago y LTV por campaña.

## 3. Redistribución de $5,000

| Campaña | Actual | Propuesto | Cambio | Condición |
|---|---|---|---|---|
| A | $2,100 | **$2,800** | +33% | Escalar gradualmente |
| C | $3,200 | **$1,300** | -59% | Tope de CPA ~$65, pujas manuales o tCPA |
| B | $1,800 | **$500** | -72% | Solo las mejores queries + retargeting |
| Reserva de tests | n/a | **$400** | n/a | Nuevas keywords y landings |

**Resultado estimado** (supuestos, no garantías):
- A: con CPA degradado a ~$52, unos 54 signups.
- C: entre 15 y 20 signups, según si logras bajar el CPA a ~$65.
- B: ~7 signups.
- Tests: ~5 signups.
- **Total: ~80-85 signups con $5,000, para un CPA mezclado de ~$60**, frente a $67.62 actual con 42% más gasto.

Para mejorar B y C:
- **B:** agrega negative keywords ("gratis", "plantilla excel", "pdf"), revisa el reporte de términos de búsqueda y deja solo las queries que convierten.
- **C:** revisa el Quality Score, el copy y la landing. Una página de comparación dedicada suele bajar el CPC.

**Plan alternativo, más agresivo:** si tras 2 semanas el CPA de C sigue sobre $80, pásala a $0 y mueve ese dinero a A ($3,500) y a la reserva de tests.

## 4. A/B tests para el próximo mes

**Advertencia de volumen:** con un CVR de 3%, detectar una mejora del 30% requiere ~5,800 clicks por variante, lo cual es inviable en un mes. Opciones:
- Testea **cambios grandes** (mejora esperada ≥50%), que necesitan ~2,000 clicks por variante.
- En anuncios, usa **CTR** como métrica, que tiene una base más alta y converge más rápido.
- Haz **un solo test a la vez** por campaña.

**Prioridad alta**

1. **Landing A: propuesta de valor.** Control vs. headline orientado a un resultado concreto ("Reduce mermas 30% en tu inventario") con prueba social arriba del fold.
2. **Landing A: fricción del formulario.** Control vs. formulario mínimo (solo email) o signup con Google. Suele ser el test de mayor impacto.
3. **Campaña C: landing.** Landing genérica vs. página de comparación específica (tabla de features, precios y "migra en 1 día"). Mide CPC, Quality Score y CVR.

**Prioridad media**

4. **Copy de anuncios en A.** Beneficio ("Controla tu stock en tiempo real") vs. oferta ("Prueba gratis 14 días, sin tarjeta"). Métrica: CTR y CVR.
5. **Blog (B): CTA.** Banner genérico de "Prueba el software" vs. lead magnet (plantilla de inventario descargable) + email nurture. Aquí tu objetivo cambia de signup directo a captura de leads.
6. **Estrategia de puja en C.** Manual CPC con tope vs. Target CPA ($65). Corre ~3 semanas y no toques nada durante el aprendizaje.

**Tests de estructura**

7. **Match type en A.** Frase vs. exacta en "software gestion inventario", para ver si bajas el CPC sin perder volumen.
8. **Segmentación por dispositivo u horario.** Revisa si hay diferencias grandes de CVR (móvil vs. escritorio) antes de testear.

**Antes de empezar:**
- Verifica que el tracking de conversiones sea correcto (sin duplicados).
- Ajusta los límites de presupuesto para no volver a pasarte.
- Si puedes, importa a Google Ads la conversión de pago y no solo el signup, para que el algoritmo optimice por valor real.

Si me das el ratio signup→cliente de pago y el precio del plan, puedo calcular el CAC y ROI real por campaña, lo que podría cambiar el orden de prioridades.