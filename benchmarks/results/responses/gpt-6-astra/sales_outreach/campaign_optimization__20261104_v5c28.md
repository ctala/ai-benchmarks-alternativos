# GPT-6 Astra — sales_outreach/campaign_optimization

- model_id: `openai/gpt-6-astra`
- success: True  | final: 6.46 | quality: 8.0
- latency_total: 41.161s | tokens_per_second: 39.6
- input_tokens: 261 | output_tokens: 1628

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

## 1. Métricas por campaña

Fórmulas:
- **CTR** = clics / impresiones
- **CPC** = costo / clics
- **CPA** = costo / signups
- **Tasa de conversión** = signups / clics

| Campaña | CTR | CPC | CPA por signup | Tasa de conversión |
|---|---:|---:|---:|---:|
| **A — Landing principal** | 3,00 % | $1,40 | **$46,67** | 3,00 % |
| **B — Blog** | 4,00 % | $0,375 ≈ $0,38 | **$75,00** | 0,50 % |
| **C — Competidor** | 6,00 % | $3,56 | **$88,89** | 4,00 % |

**Importante:** el gasto reportado suma **$7.100**, no $5.000. En conjunto, conseguiste **105 signups**, con un CPA promedio de **$67,62**. La nueva distribución implica reducir el gasto un **29,6 %**.

## 2. ¿Qué escalar y qué pausar?

**Si el objetivo es maximizar signups y todos tienen un valor similar, escalaría A, mantendría B con presupuesto limitado y pausaría C.**

### A: escalar
Es la más eficiente por resultado:
- Su CPA es **38 % menor que el de B** y **47,5 % menor que el de C**.
- Por cada $1.000 genera aproximadamente **21,4 signups**, frente a **13,3 de B** y **11,3 de C**, a los costos actuales.

Subiría su presupuesto gradualmente: al ampliar cobertura o pujar más, el CPA puede empeorar.

### B: reducir y optimizar, no escalar todavía
Tiene clics baratos, pero convierte solo **1 de cada 200 visitas**.

Eso sugiere una oportunidad de mejorar el recorrido del blog al registro, aunque también puede reflejar búsquedas informativas con poca intención de compra. Su CPA sigue siendo mejor que el de C, por lo que conservaría una partida pequeña para validarlo.

### C: pausar inicialmente
Aunque tiene el mejor CTR y la mejor conversión, **sus clics cuestan 2,54 veces lo que cuestan en A**. Esa diferencia supera la ventaja de conversión y produce el CPA más alto.

**Excepción importante:** si los signups de C se convierten en clientes con mayor frecuencia o generan más ingresos, podría merecer presupuesto. Para igualar la eficiencia de A, cada signup de C tendría que aportar aproximadamente **1,90 veces el valor esperado** de uno de A.

## 3. Redistribución de los $5.000

Propondría este punto de partida:

| Campaña | Presupuesto mensual | Porcentaje | Signups estimados* |
|---|---:|---:|---:|
| **A** | **$4.000** | **80 %** | ≈ 86 |
| **B** | **$1.000** | **20 %** | ≈ 13 |
| **C** | **$0** | **0 %** | 0 |
| **Total** | **$5.000** | **100 %** | **≈ 99** |

\*Proyección usando los CPA actuales, **no una garantía**. Supone que existe suficiente demanda y que el rendimiento no cambia con el presupuesto.

Eso daría un CPA combinado aproximado de **$50,48**, frente a los **$67,62** actuales.

**Cómo ejecutarlo:**
- Aumentar A por etapas, comprobando el CPA de los resultados adicionales.
- Revisar términos de búsqueda y añadir negativas para evitar tráfico irrelevante.
- Mantener B como prueba controlada de mejora de conversión.
- Si A no puede absorber el presupuesto eficientemente, no forzar el gasto solo por agotarlo.

## 4. A/B tests para el próximo mes

Priorizaría **un test por campaña activa**, para no fragmentar demasiado el tráfico.

### Test 1 — A: reducir fricción del registro
- **Control:** formulario actual.
- **Variante:** formulario con menos campos obligatorios; pedir el resto después del registro.
- **Hipótesis:** reducir el esfuerzo aumenta los signups.
- **Métrica principal:** tasa de signup.
- **Métrica de control:** porcentaje de registros que activan el producto o se convierten en leads cualificados.

**Referencia numérica:** con el CPC actual de $1,40, subir la conversión del **3 % al 4 %** bajaría el CPA de **$46,67 a $35**. Es un escenario ilustrativo, no una predicción.

### Test 2 — B: conectar el artículo con una necesidad concreta
- **Control:** CTA actual del blog.
- **Variante:** CTA contextual dentro del contenido, conectado con el problema del artículo y dirigido a una landing relevante.
- **Ejemplo:** en un artículo sobre inventario de restaurantes, ofrecer conocer cómo el producto ayuda a controlar existencias y mermas, si realmente tiene esa función.
- **Métrica principal:** signups por visita al artículo, no solo clics en el CTA.
- **Métrica de control:** calidad o activación de esos signups.

**Referencia numérica:** con CPC de $0,375, pasar de **0,50 % a 0,75 %** de conversión reduciría el CPA de **$75 a $50**. B necesitaría aproximadamente **0,80 %** de conversión para igualar el CPA actual de A.

### Precaución al evaluar
Con **45 y 24 signups mensuales históricos** en A y B, puede faltar muestra para detectar mejoras moderadas en un solo mes. Usa una división aleatoria del tráfico, define la métrica antes de empezar y no declares un ganador por unos pocos registros.

**Conclusión:** A merece la mayor inversión; B necesita demostrar una mejora del recorrido a signup; C no justifica su costo actual salvo que aporte clientes de mayor valor.