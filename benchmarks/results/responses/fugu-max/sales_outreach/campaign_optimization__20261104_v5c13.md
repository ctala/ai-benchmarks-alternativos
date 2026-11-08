# Fugu Max — sales_outreach/campaign_optimization

- model_id: `sakana/fugu-max`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 44.554s | tokens_per_second: 217.6
- input_tokens: 390 | output_tokens: 9693

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

Asumo que el objetivo es **maximizar signups al menor CPA**. Ojo: los costos que das suman **$7,100**, no $5,000. Hay un sobre-gasto de **$2,100** vs tu tope. Para el próximo mes hay que recortar.

## 1. Métricas por campaña

| Campaña | CTR | CPC | CPA | Conversion rate |
|---|---:|---:|---:|---:|
| A — Landing principal | 1,500 / 50,000 = **3.00%** | $2,100 / 1,500 = **$1.40** | $2,100 / 45 = **$46.67** | 45 / 1,500 = **3.00%** |
| B — Blog content | 4,800 / 120,000 = **4.00%** | $1,800 / 4,800 = **$0.375** | $1,800 / 24 = **$75.00** | 24 / 4,800 = **0.50%** |
| C — Competidor | 900 / 15,000 = **6.00%** | $3,200 / 900 = **$3.56** | $3,200 / 36 = **$88.89** | 36 / 900 = **4.00%** |
| **Total** | 7,200 / 185,000 = **3.89%** | $7,100 / 7,200 = **$0.99** | $7,100 / 105 = **$67.62** | 105 / 7,200 = **1.46%** |

## 2. ¿Qué escalar y qué pausar?

**Escalar: Campaña A.**  
Tiene el **mejor CPA ($46.67)** y un conversion rate sólido del **3%**. Genera el **42.9% de los signups con solo el 29.6% del gasto**. Es la más eficiente.

**Pausar: Campaña C** si tu KPI es CPA puro.  
Aunque tiene el mejor conversion rate (**4%**), su CPC es **$3.56**, 2.5x el de A, y su CPA es **$88.89**, casi el doble que A. Para igualar el CPA de A con su CVR del 4%, C necesitaría un CPC de aproximadamente **$1.87**; está pagando $3.56.

**Campaña B: no la escalaría, pero tampoco la pausaría del todo de inmediato.**  
Tiene CTR alto y CPC barato, pero su conversion rate es **0.5%**: 4,800 clicks solo generaron 24 signups. Su CPA es **$75**, mejor que C pero muy lejos de A. La reestructuraría como campaña de contenido/retargeting, no como adquisición directa de signups.

**Decisión operativa:**  
- **Escalar A.**  
- **Pausar C como campaña general** o dejarla solo con exact match y tope de CPC muy agresivo.  
- **Reducir B** y exigirle CVR >1%; si no mejora, pausarla también.

## 3. Redistribución de $5,000/mes

Propuesta principal:

| Campaña | Presupuesto | % | Lógica |
|---|---:|---:|---|
| A — Landing principal | **$4,000** | 80% | Escalar la más eficiente, pero por fases |
| B — Blog/retargeting | **$1,000** | 20% | Solo retargeting y keywords con mejor CVR |
| C — Competidor | **$0** | 0% | Pausada por CPA alto |

Esto suma **$5,000**. A CPA constante, A daría ~**86 signups** y B ~**13**, total ~**99 signups**, vs 105 actuales con $7,100. Mejora el CPA mezclado, pero no metas los $4,000 a A de golpe: sube **20–30% por semana** y monitorea el CPA marginal. Si el CPA de A sube por encima de **$55–$60**, frena.

Si quieres mantener algo de C por su alto CVR, alternativa:
- A: **$3,500**
- B: **$1,000**
- C: **$500** solo exact match, con tope de CPC ~$2.50 y CPA objetivo <$70.

## 4. A/B tests sugeridos para el próximo mes

1. **Landing de A:** headline beneficio vs. feature, CTA “demo” vs. “crear cuenta”, formulario corto vs. formulario con calificación. Métrica: CVR y CPA.
2. **B: message match blog → oferta.** Testear lead magnet descargable vs. free trial para keywords como “cómo gestionar inventario”. Y una landing específica para “problemas inventario restaurante”.
3. **C: página de comparación.** Si la reactivas, testear tabla comparativa vs. página de migración/oferta de cambio, y ad copy “alternativa a [competidor]” vs. “[competidor] vs”. Métrica: CPC y CVR.
4. **Formulario:** email solo vs. email + empresa/tamaño. No solo mires signups; mide activación o signups calificados para no optimizar basura.
5. **Ad copy:** prueba social vs. urgencia vs. ahorro de tiempo. Un cambio por test y suficiente volumen; con 24–45 signups/mes, los resultados tardan.

**Resumen:** escala A, pausa C como campaña general, reduce y reestructura B, y reasigna hacia A de forma gradual.