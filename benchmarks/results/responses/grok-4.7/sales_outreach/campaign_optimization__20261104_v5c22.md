# Grok 4.7 — sales_outreach/campaign_optimization

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 34.138s | tokens_per_second: 60.0
- input_tokens: 1498 | output_tokens: 2049

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

Estos son los números del mes y cómo los usaría para decidir. El gasto real fue **$7,100**, no $5,000, así que la reasignación asume que hay que volver al tope mensual.

## 1. Métricas

| Campaña | CTR | CPC | CPA | Conv. rate |
|---|---:|---:|---:|---:|
| A – Landing | 3.00% (1,500 / 50,000) | $1.40 | **$46.67** | 3.00% (45 / 1,500) |
| B – Blog | 4.00% (4,800 / 120,000) | $0.38 | $75.00 | 0.50% (24 / 4,800) |
| C – Competidor | **6.00%** (900 / 15,000) | $3.56 | $88.89 | **4.00%** (36 / 900) |

Totales del mes: 7,200 clics, 105 signups, CPA blended **$67.62**, CR blended 1.46%.

## 2. Qué escalar y qué cortar

**Escalar A.** Es la única con intención comercial clara y el CPA más bajo: **$46.67**, un 31% por debajo del blended y casi la mitad del de C. Cada $1,000 en A, a la tasa actual, compra ~21 signups; en B ~13 y en C ~11.

**No pausar C del todo, sí recortarla.** Tiene el mejor CTR (6%) y la mejor conversión (4%): la gente que busca alternativa al competidor sí quiere el producto. El problema es el precio del clic ($3.56), no la intención. A $88.89 de CPA solo se justifica si el valor de un signup (LTV o margen del primer mes) supera eso con holgura. Si tu objetivo está cerca de los ~$50 de A, C está cara.

**Pausar o dejar en mínimo B para adquisición directa.** El CPC barato engaña: con 0.5% de conversión el CPA es $75, peor que A, y se llevó el 67% de los clics para el 23% de los signups. Keywords de “cómo…” y “problemas…” son investigación, no compra. Solo tendría sentido un presupuesto chico si mides conversiones asistidas o remarketing; como canal de signup directo, no.

## 3. Redistribución de $5,000

Asumiendo que el objetivo es **signups al menor CPA**, no alcance:

| Campaña | Presupuesto | % | Signups esperados* | Notas |
|---|---:|---:|---:|---|
| A | $3,200 | 64% | ~60–68 | Subir respecto a $2,100; vigilar que el CPA no pase de ~$55 |
| C | $1,300 | 26% | ~12–15 | Menos que los $3,200 actuales; solo keywords y anuncios que conviertan |
| B | $500 | 10% | ~5–7 | Solo si hay remarketing; si no, $0 y ese dinero a A |
| **Total** | **$5,000** | | **~77–90** | Menos signups que los 105, pero con ~$2,100 menos de gasto |

\*Lineal respecto al CPA actual. En búsqueda el escalado no es lineal: al subir puja en A el CPC y el CPA suelen empeorar. Si el CPA de A sube por encima de ~$60 de forma sostenida, frena el aumento y no “compres” volumen en C solo por llenar el presupuesto.

Si B no alimenta remarketing, yo pondría **$3,500 en A y $1,500 en C**.

## 4. Tests para el próximo mes

Prioriza lo que mueve CPA, no el CTR de B.

1. **A – landing vs. landing.** Misma campaña, dos URLs: formulario corto (email + empresa) contra el actual. Métrica: CR y CPA, no CTR. Corre hasta ~100 signups combinados o 2 semanas, lo que llegue después.
2. **A – coincidencia y negativas.** Separa “software gestión inventario” (compra) de variantes informativas que se estén colando. Test: frase/exacta con negativas (“gratis”, “excel”, “plantilla”, “qué es”) contra la estructura actual. Éxito = CPC estable y CPA ≤ $50.
3. **C – anuncio de comparación.** RSA con prueba social o diferencia concreta (“sin contrato anual”, “migración en X días”) contra el anuncio genérico de “alternativa a…”. El CTR ya es alto; el test vale si baja el CPC o sube el CR, no si solo sube el CTR.
4. **C – tope de puja / tCPA.** Si puedes fijar un CPA objetivo (~1.3× el de A, o sea ~$60), deja que el sistema corte las subastas caras en vez de gastar los $3,200 de antes. Compara signups y CPA contra el mes base, no impresiones.
5. **B – solo si la mantienes.** No optimices el blog para signup. Mándala a una pieza con lead magnet y remarketing, y mide signups asistidos a 30 días. Si a las 4 semanas el CPA asistido sigue por encima del de A, apágala.

No tengo tu LTV ni un CPA objetivo. Si un signup vale menos de ~$70, C debería bajar más de lo que puse arriba; si vale $150+, C se puede mantener más cerca de $2,000 siempre que el CPA no se dispare al escalar.