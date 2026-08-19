# Step 3.5 Flash — sales_outreach/campaign_optimization

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.56 | quality: 8.0
- latency_total: 29.515s | tokens_per_second: 69.4
- input_tokens: 280 | output_tokens: 2048

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

Vamos a analizar los datos paso a paso.

Primero, calcularemos las métricas solicitadas para cada campaña:

**Campaña A:**
- Impresiones: 50,000
- Clicks: 1,500
- Signups (conversiones): 45
- Costo: $2,100

CTR = (Clicks / Impresiones) * 100 = (1,500 / 50,000) * 100 = 3%
CPC = Costo / Clicks = $2,100 / 1,500 = $1.40
CPA = Costo / Signups = $2,100 / 45 = $46.67
Conversion Rate = (Signups / Clicks) * 100 = (45 / 1,500) * 100 = 3%

**Campaña B:**
- Impresiones: 120,000
- Clicks: 4,800
- Signups: 24
- Costo: $1,800

CTR = (4,800 / 120,000) * 100 = 4%
CPC = $1,800 / 4,800 = $0.375
CPA = $1,800 / 24 = $75
Conversion Rate = (24 / 4,800) * 100 = 0.5%

**Campaña C:**
- Impresiones: 15,000
- Clicks: 900
- Signups: 36
- Costo: $3,200

CTR = (900 / 15,000) * 100 = 6%
CPC = $3,200 / 900 ≈ $3.56
CPA = $3,200 / 36 ≈ $88.89
Conversion Rate = (36 / 900) * 100 = 4%

Resumen de métricas:

| Campaña | CTR  | CPC    | CPA     | Conversion Rate |
|---------|------|--------|---------|-----------------|
| A       | 3%   | $1.40  | $46.67  | 3%              |
| B       | 4%   | $0.375 | $75.00  | 0.5%            |
| C       | 6%   | $3.56  | $88.89  | 4%              |

Ahora, para decidir qué campaña escalar y cuál pausar, debemos considerar la eficiencia en términos de CPA (costo por adquisición) y la tasa de conversión. El objetivo es maximizar los signups dentro del presupuesto.

- La Campaña A tiene el CPA más bajo ($46.67) y una tasa de conversión decente (3%).
- La Campaña B tiene el CPC más bajo ($0.375) pero una tasa de conversión muy baja (0.5%), lo que resulta en un CPA alto ($75).
- La Campaña C tiene la tasa de conversión más alta (4%) pero el CPC y CPA más altos ($3.56 y $88.89 respectivamente).

Dado que el CPA de la Campaña A es significativamente menor que el de las otras, y su tasa de conversión es buena, parece la más eficiente para generar signups. La Campaña C tiene una buena tasa de conversión pero un costo por click muy alto, lo que encarece el CPA. La Campaña B tiene muchos clicks pero casi no convierte, por lo que es ineficiente.

Por lo tanto, sugeriría **escalar la Campaña A** y **pausar la Campaña B** (por su bajo rendimiento en conversiones). La Campaña C podría mantenerse o ajustarse, pero su CPA es alto, así que habría que evaluar si el valor de los signups justifica el costo. Como el presupuesto total es $5,000 y actualmente se gastan $2,100 + $1,800 + $3,200 = $7,100 (más del presupuesto), necesitamos redistribuir.

Nota: El gasto actual total es $2,100 + $1,800 + $3,200 = $7,100, pero el presupuesto es $5,000, así que ya están sobrepresupuestados. Debemos ajustar para cumplir con $5,000.

Para redistribuir el presupuesto de $5,000, debemos asignar más a la campaña más eficiente (A) y menos a las menos eficientes. Dado que la Campaña B es la que peor rendimiento tiene (CPA alto y conversión baja), la pausaríamos. La Campaña C tiene un CPA alto pero una tasa de conversión decente, así que podríamos mantenerla pero con menos presupuesto.

Propuesta de redistribución:
- Pausar Campaña B (ahorra $1,800).
- Ahora tenemos $5,000 para asignar a A y C. Actualmente A gasta $2,100 y C gasta $3,200, total $5,300. Pero debemos reducirlo a $5,000. 
- Podemos reducir C ligeramente y aumentar A, pero A ya es eficiente. Sin embargo, si A puede escalar más (más impresiones/clicks sin perder eficiencia), podríamos asignarle más.

Pero primero, calculemos el número de signups que genera cada campaña con su gasto actual:
- A: 45 signups con $2,100 -> costo por signup $46.67.
- B: 24 signups con $1,800 -> $75.
- C: 36 signups con $3,200 -> $88.89.

Si pausamos B, ahorramos $1,800. Entonces, para quedarnos en $5,000, debemos reducir el gasto total en $200 (ya que $7,100 - $1,800 = $5,300, y necesitamos $5,000, así que recortar $300 de A y C combinados).

Pero en lugar de recortar, podríamos reasignar el presupuesto de B a A y C, pero manteniendo el total en $5,000. Dado que A es la más eficiente, le asignaríamos más. Supongamos que queremos maximizar signups dentro de $5,000.

Si solo invertimos en A, con $5,000, el número de signups sería: $5,000 / $46.67 ≈ 107 signups.
Si solo invertimos en C, sería: $5,000 / $88.89 ≈ 56 signups.
Si invertimos en A y C, necesitamos encontrar la combinación óptima. Pero como A tiene un CPA mucho menor, lo ideal es poner la mayor parte en A, siempre que A pueda escalar (es decir, que haya suficiente volumen de búsqueda para las keywords de A). Las keywords de A son "software gestion inventario" e "inventario pymes", que son más genéricas y de intención comercial. Las de C son de competidor, que pueden tener volumen limitado.

Según los datos actuales, A tiene 50,000 impresiones con $2,100, lo que sugiere que puede haber más impresiones disponibles. C tiene solo 15,000 impresiones con $3,200, lo que indica que el inventario de impresiones para esas keywords es limitado (o el presupuesto actual ya las agota). B tiene 120,000 impresiones con $1,800, pero convierte muy mal.

Por lo tanto, redistribuiría:
- Pausar B completamente.
- Asignar la mayor parte del presupuesto a A, pero también un poco a C si hay oportunidad.

Calculemos el gasto por impresión para cada campaña (CPM aproximado):
- A: $2,100 / 50,000 = $0.042 por impresión.
- B: $1,800 / 120,000 = $0.015 por impresión.
- C: $3,200 / 15,000 ≈ $0.213 por impresión.

A y B tienen CPM bajo, C tiene CPM alto. Pero la conversión de B es terrible.

Ahora, con $5,000, si asignamos todo a A, podríamos obtener impresiones adicionales. Pero el CTR de A es 3%, y su tasa de conversión 3%. Si aumentamos el presupuesto en A, ¿se mantendrán el CTR y la tasa de conversión? Asumamos que sí a corto plazo.

Entonces, con $5,000 en A, clicks = $5,000 / $1.40 ≈ 3,571 clicks (actualmente 1,500). Impresiones = clicks / CTR = 3,571 / 0.03 ≈ 119,033 impresiones. Eso es más del doble de las impresiones actuales (50,000). ¿Hay suficiente volumen de búsqueda para esas keywords? Posiblemente sí, ya que son términos amplios.

Pero también podríamos considerar mantener un poco de C si su tasa de conversión es mejor (4% vs 3% de A). Sin embargo, su CPA es casi el doble. Veamos el costo por impresión: en A, cada signup