# Qwen 3.8 Max 0902 — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.81 | quality: 10.0
- latency_total: 458.034s | tokens_per_second: 39.6
- input_tokens: 360 | output_tokens: 18155

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

Antes de calcular: hay una inconsistencia importante. La suma de costos de las 3 campañas es:

**$2,100 + $1,800 + $3,200 = $7,100**

Eso supera tu presupuesto declarado de **$5,000/mes**. Para el análisis asumiré que el próximo mes quieres operar con **$5,000** y que el objetivo principal es conseguir **signups al menor costo posible**.

---

## 1) Métricas por campaña

Fórmulas usadas:

- **CTR** = Clicks / Impresiones  
- **CPC** = Costo / Clicks  
- **CPA** = Costo / Signups  
- **Conversion Rate** = Signups / Clicks  

| Campaña | Impresiones | Clicks | CTR | Costo | CPC | Signups | CPA | Conversion Rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A** | 50,000 | 1,500 | **3.00%** | $2,100 | **$1.40** | 45 | **$46.67** | **3.00%** |
| **B** | 120,000 | 4,800 | **4.00%** | $1,800 | **$0.38** | 24 | **$75.00** | **0.50%** |
| **C** | 15,000 | 900 | **6.00%** | $3,200 | **$3.56** | 36 | **$88.89** | **4.00%** |

### Totales actuales

| Métrica | Valor |
|---|---:|
| Impresiones totales | 185,000 |
| Clicks totales | 7,200 |
| Signups totales | 105 |
| Costo total | $7,100 |
| CTR global | **3.89%** |
| CPC global | **$0.99** |
| CPA global | **$67.62** |
| Conversion Rate global | **1.46%** |

---

## 2) ¿Qué campaña escalar y cuál pausar?

### Recomendación directa

- **Escalar:** Campaña **A**
- **Pausar o reducir a test mínimo:** Campaña **C**
- **No escalar:** Campaña **B**; solo mantenerla si tienes un objetivo de awareness/remarketing o si puedes mejorar mucho su conversión.

### Justificación con números

#### Campaña A: la más eficiente

- CPA: **$46.67**
- Conversion Rate: **3.00%**
- Genera **45 signups** con solo **$2,100**
- Representa aproximadamente **29.6%** del gasto actual, pero genera **42.9%** de los signups.

Es la campaña con mejor costo por signup. Además, sus keywords parecen de mayor intención comercial:

- “software gestion inventario”
- “inventario pymes”

Esta es la campaña que deberías priorizar.

---

#### Campaña B: muchos clicks, poca conversión

- CTR alto: **4.00%**
- CPC bajo: **$0.38**
- Pero conversion rate muy bajo: **0.50%**
- CPA: **$75.00**

El problema no es que no atraiga tráfico; el problema es que ese tráfico no convierte. Su CPA es **60.7% más alto** que el de la Campaña A.

Comparación:

| Campaña | CPA | Diferencia vs A |
|---|---:|---:|
| A | $46.67 | base |
| B | $75.00 | +60.7% |
| C | $88.89 | +90.5% |

Para que la Campaña B iguale el CPA de A manteniendo su CPC actual de $0.38, necesitaría un conversion rate de aproximadamente:

**$0.38 / $46.67 = 0.81%**

Hoy está en **0.50%**. Es decir, necesita mejorar conversión en más de **60%** solo para igualar a A.

Por eso, no la escalaría. Si la mantienes, debería ser con presupuesto pequeño y con un test claro para subir conversión.

---

#### Campaña C: buena conversión, pero demasiado cara

La Campaña C tiene el mejor CTR y el mejor conversion rate:

- CTR: **6.00%**
- Conversion Rate: **4.00%**
- CPC: **$3.56**
- CPA: **$88.89**

El problema es el costo por click. Aunque convierte bien, el CPC es tan alto que el CPA termina siendo el peor de las tres.

Para que la Campaña C iguale el CPA de la Campaña A manteniendo su conversion rate de 4%, necesitaría un CPC máximo aproximado de:

**$46.67 × 4% = $1.87**

Hoy paga **$3.56** por click, casi el doble.

Además, consume mucho presupuesto:

- Campaña C representa **45.1%** del gasto actual
- Pero solo genera **34.3%** de los signups

Conclusión: la intención parece buena, pero la campaña está sobrepujada o mal segmentada. No la escalaría como está.

---

### Si tienes que pausar una campaña hoy, pausa C

Aunque B convierte peor, C tiene el peor CPA y además consume mucho más presupuesto.

Simulación simple asumiendo que los CPAs se mantienen:

#### Si pausas C

- Pierdes 36 signups
- Liberas $3,200
- Si mueves esos $3,200 a Campaña A:
  - $3,200 / $46.67 = **68.6 signups adicionales**
- Ganancia neta aproximada:
  - +68.6 - 36 = **+32.6 signups**

#### Si pausas B

- Pierdes 24 signups
- Liberas $1,800
- Si mueves esos $1,800 a Campaña A:
  - $1,800 / $46.67 = **38.6 signups adicionales**
- Ganancia neta aproximada:
  - +38.6 - 24 = **+14.6 signups**

Por impacto directo en signups, **pausar C parece más eficiente**, siempre que no haya datos de LTV o calidad de signup que indiquen que los usuarios de C valen mucho más.

Dicho eso: si los signups de la Campaña C se convierten luego en clientes de mayor valor, quizás valga la pena mantenerla con un CPA más alto. Pero con la información actual, es la menos eficiente.

---

## 3) Redistribución del presupuesto de $5,000

Mi recomendación base sería:

| Campaña | Presupuesto | Rol |
|---|---:|---|
| **A** | **$4,500** | Escalar la campaña principal |
| **B** | **$500** | Test pequeño para mejorar conversión o remarketing |
| **C** | **$0** | Pausada como está actualmente |

### Proyección aproximada si se mantienen los rendimientos actuales

#### Campaña A con $4,500

- CPC: $1.40
- Clicks estimados: $4,500 / $1.40 = **3,214 clicks**
- Conversion Rate: 3%
- Signups estimados: 3,214 × 3% = **96 signups**

#### Campaña B con $500

- CPC: $0.375
- Clicks estimados: $500 / $0.375 = **1,333 clicks**
- Conversion Rate: 0.5%
- Signups estimados: 1,333 × 0.5% = **7 signups**

#### Total

- Presupuesto: $5,000
- Signups estimados: **103**
- CPA estimado: $5,000 / 103 = **$48.5**

Esto sería mejor que el CPA global actual de **$67.62**.

---

### Alternativa más agresiva

Si tu objetivo es únicamente maximizar signups y no necesitas mantener tráfico informativo:

| Campaña | Presupuesto |
|---|---:|
| A | $5,000 |
| B | $0 |
| C | $0 |

Proyección:

- $5,000 / $46.67 = **107 signups aproximados**
- CPA estimado: **$46.67**

El riesgo es concentrar todo en una sola campaña. Si A se satura, el CPC puede subir. Por eso mi recomendación principal es mantener una pequeña porción para test, pero si quieres máxima eficiencia de corto plazo, esta opción es válida.

---

### Alternativa si quieres mantener un test de competidor

Si te interesa defender términos de competencia, podrías relanzar C solo como experimento:

| Campaña | Presupuesto |
|---|---:|
| A | $4,000 |
| B | $0 |
| C | $1,000 |

Pero solo debería funcionar si aplicas condiciones estrictas:

- Keywords en exact match
- Negativos agresivos: login, soporte, gratis, precios, tutorial, etc.
- CPC objetivo menor a **$2.00**
- Landing específica de comparación
- Pausar si CPA supera tu objetivo durante 2 semanas

Con CPC actual de $3.56, C no es escalable. Con CPC cercano a $1.80-$2.00, podría empezar a tener sentido.

---

## 4) A/B tests sugeridos para el próximo mes

Te dejaría los tests priorizados por impacto potencial.

---

### Test 1: Landing page de la Campaña A

La Campaña A ya es la mejor, así que mejorarla puede tener el mayor impacto absoluto.

**Hipótesis:**  
Si la landing comunica mejor el beneficio principal y reduce fricción, puedes subir el conversion rate de 3.0% a 3.5% o más.

**Variantes a probar:**

- Variante actual vs variante con formulario más corto
- Variante actual vs variante con testimonios/casos de éxito
- Variante actual vs variante con mensaje más específico para pymes
- Variante actual vs variante con CTA más claro: “Prueba gratis” vs “Agenda demo”

**Impacto potencial:**

Si mantienes CPC de $1.40:

- CR actual: 3.0% → CPA = $46.67
- CR nueva: 3.5% → CPA = $1.40 / 3.5% = **$40.00**

Eso reduciría CPA en aproximadamente **14%**.

---

### Test 2: Intención y CTA en la Campaña B

La Campaña B trae clicks baratos, pero no convierte. Hay que validar si el problema es intención o landing.

**Hipótesis:**  
El tráfico de blog/content es demasiado informativo. Necesitas filtrar mejor o cambiar el puente hacia signup.

**Qué probar:**

1. Pausar keywords demasiado genéricas.
2. Agregar negativas como:
   - gratis
   - excel
   - plantilla
   - manual
   - curso
   - pdf
   - ejemplo
   - qué es
3. Dejar solo keywords con dolor o intención más cercana:
   - “problemas inventario restaurante”
   - “cómo controlar inventario en restaurante”
   - “software para control de inventario”
4. Probar una CTA más directa:
   - “Empieza gratis”
   - “Controla tu inventario hoy”
   - “Prueba el software”

**Objetivo mínimo:**  
Para que B sea comparable a A, debería llegar a un conversion rate cercano a **0.80%** con el CPC actual, o bajar el CPC a **$0.23**.

Si no logra algo cercano a eso, pausa la campaña o déjala solo para remarketing.

---

### Test 3: Reducir CPC en Campaña C

Si decides mantener C como test, el objetivo no es escalarla de inmediato, sino bajar el CPC.

**Hipótesis:**  
La campaña está pagando demasiado por términos de competidor o está atrayendo búsquedas no deseadas.

**Qué probar:**

- Cambiar keywords a exact match
- Agregar negativas:
  - login
  - soporte
  - atención al cliente
  - precios
  - tutorial
  - manual
  - gratis
  - descargar
- Probar anuncios con posicionamiento de alternativa:
  - “Alternativa a [Competidor]”
  - “[Competidor] vs [Tu producto]”
  - “Cambia de [Competidor] en minutos”
- Crear landing específica de comparación
- Usar bid cap o target CPA conservador

**Objetivo:**

Para que C tenga sentido, necesitas bajar el CPC.

Con conversion rate actual de 4%:

- CPC $3.56 → CPA $88.89
- CPC $2.50 → CPA $62.50
- CPC $2.00 → CPA $50.00
- CPC $1.87 → CPA $46.75

Yo no escalaría C mientras no pueda acercarse a un CPC de **$2.00 o menos**.

---

### Test 4: Mensaje del anuncio según intención

Las tres campañas tienen intenciones distintas. El anuncio debería reflejar eso.

#### Para Campaña A

Mensaje comercial directo:

- “Software de gestión de inventario para pymes”
- “Controla tu inventario sin planillas”
- “Empieza hoy con tu inventario organizado”

#### Para Campaña B

Mensaje educativo con puente a producto:

- “¿Problemas con tu inventario? Descubre cómo automatizarlo”
- “Deja de gestionar inventario manualmente”
- “Guía + software para controlar tu inventario”

#### Para Campaña C

Mensaje comparativo:

- “¿Buscas alternativa a [Competidor]?”
- “[Tu producto] vs [Competidor]: compara en 1 minuto”
- “Cambia de [Competidor] sin perder tu información”

**Métrica a observar:**  
No solo CTR. Debes mirar conversion rate y CPA. Un CTR alto que no convierte puede salir caro, como pasa en B.

---

### Test 5: Estrategia de pujas

Con 105 signups/mes en total, puede que tengas suficiente volumen para probar estrategias automáticas, pero no demasiada data por campaña individual.

Opciones:

1. **Maximize Conversions** si quieres volumen y todavía estás aprendiendo.
2. **Target CPA** si ya tienes claro tu CPA objetivo.
3. **Portfolio bidding** juntando campañas para darle más data al algoritmo.

Si tu CPA objetivo fuera, por ejemplo, **$50**, entonces:

- A debería poder escalar cerca de ese CPA.
- B tendría que mejorar mucho.
- C tendría que bajar CPC drásticamente.

Una regla práctica:

- Si una campaña supera tu CPA objetivo durante varios días y no hay señales de mejora, pausa o reduce.
- Si una campaña está por debajo del CPA objetivo con espacio para crecer, aumenta presupuesto gradualmente, por ejemplo 15-20% por semana.

---

## Resumen ejecutivo

### Métricas clave

| Campaña | CTR | CPC | CPA | Conv. Rate |
|---|---:|---:|---:|---:|
| A | 3.00% | $1.40 | $46.67 | 3.00% |
| B | 4.00% | $0.38 | $75.00 | 0.50% |
| C | 6.00% | $3.56 | $88.89 | 4.00% |

### Decisión recomendada

- **Escalar A:** mejor CPA y buena conversión.
- **Pausar C como está:** peor CPA y CPC demasiado alto.
- **No escalar B:** solo mantener con presupuesto pequeño si puedes testear mejoras de conversión o usarla para awareness/remarketing.

### Presupuesto sugerido

| Campaña | Presupuesto |
|---|---:|
| A | $4,500 |
| B | $500 |
| C | $0 |

Con esta distribución, manteniendo rendimientos actuales, podrías esperar aproximadamente **103 signups** con un CPA cercano a **$48.5**, mejor que el CPA global actual de **$67.62**.

### Próximos tests prioritarios

1. Optimizar landing de Campaña A.
2. Mejorar intención y CTA de Campaña B.
3. Si mantienes C, bajar CPC a menos de $2.00 con exact match y negativos.
4. Probar mensajes diferenciados por intención de búsqueda.
5. Evaluar estrategia de pujas con CPA objetivo.