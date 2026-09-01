# Qwen 3.8 Flash — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 153.901s | tokens_per_second: 99.5
- input_tokens: 360 | output_tokens: 15308

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

## Nota importante sobre presupuesto

Tus costos del último mes suman **$7,100**:

- Campaña A: $2,100  
- Campaña B: $1,800  
- Campaña C: $3,200  
- **Total actual: $7,100**

Pero tu presupuesto es **$5,000/mes**. Por tanto, hay que recortar o redistribuir **$2,100** respecto al gasto real del último mes.

---

# 1. Cálculo de métricas

Fórmulas usadas:

- **CTR** = Clicks / Impresiones  
- **CPC** = Costo / Clicks  
- **CPA** = Costo / Signups  
- **CVR** = Signups / Clicks  
- **Signups por $1,000** = Signups / Costo × 1,000  
- **Clicks por signup** = Clicks / Signups

| Campaña | Impresiones | Clicks | Signups | Costo | CTR | CPC | CPA | CVR | Signups/$1,000 | Clicks/signup |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **A — Landing principal** | 50,000 | 1,500 | 45 | $2,100 | **3.00%** | **$1.40** | **$46.67** | **3.00%** | **21.4** | **33.3** |
| **B — Blog content** | 120,000 | 4,800 | 24 | $1,800 | **4.00%** | **$0.38** | **$75.00** | **0.50%** | **13.3** | **200.0** |
| **C — Competidor** | 15,000 | 900 | 36 | $3,200 | **6.00%** | **$3.56** | **$88.89** | **4.00%** | **11.3** | **25.0** |

Blended / promedio total del último mes:

| Métrica | Valor |
|---|---:|
| Impresiones totales | 185,000 |
| Clicks totales | 7,200 |
| Signups totales | 105 |
| Costo total | $7,100 |
| CTR promedio | 3.89% |
| CPC promedio | $0.99 |
| CPA promedio | $67.62 |
| CVR promedio | 1.46% |

---

# 2. ¿Qué campaña escalar y cuál pausar?

## Recomendación principal

### **Escalar: Campaña A**
### **Pausar o reducir fuerte: Campaña B**
### **Mantener pero optimizar/recortar: Campaña C**

---

## ¿Por qué escalar la Campaña A?

La Campaña A es la más eficiente para conseguir signups al costo actual.

Sus números:

- **CPA: $46.67** → el mejor de las tres.
- **CVR: 3.00%** → muy decente.
- **CPC: $1.40** → moderado.
- **Signups por $1,000: 21.4** → la mejor relación volumen/costo.
- **Clicks por signup: 33.3** → eficiente.

Además, tiene keywords con intención más directa:

- “software gestion inventario”
- “inventario pymes”

Son búsquedas más cercanas a una decisión de compra o evaluación activa, a diferencia de contenido informativo.

**Conclusión:** A es la candidata natural para escalar.

---

## ¿Por qué pausar o reducir mucho la Campaña B?

La Campaña B tiene tráfico barato, pero convierte muy mal.

Sus números:

- **CPC: $0.38** → muy barato.
- **CTR: 4.00%** → alto.
- **CVR: 0.50%** → muy bajo.
- **CPA: $75.00** → caro para lo que cuesta el clic.
- **Clicks por signup: 200** → necesitas 200 clics para conseguir un signup.

El problema no es el tráfico. El problema es la intención o la landing.

Keywords como:

- “como gestionar inventario”
- “problemas inventario restaurante”

son más informativas. La gente busca aprender, no necesariamente comprar un software.

Aunque el CPC sea bajo, la conversión de 0.5% hace que el costo por signup suba a $75.

**Conclusión:** Si tu objetivo principal son signups este mes, B es la primera candidata a pausar o reducir drásticamente.

---

## ¿Y la Campaña C?

La Campaña C tiene una paradoja:

- **CTR: 6.00%** → el más alto.
- **CVR: 4.00%** → el más alto.
- **CPA: $88.89** → el más caro.

Es decir: atrae clics muy calificados, pero paga demasiado por cada clic.

Keywords de competidor como:

- “alternativa a [competidor]”
- “[competidor] vs”

suelen tener alta intención. La gente ya está comparando.

Por eso no recomendaría pausarla completamente, pero sí recortarla y optimizarla.

Su problema no es la intención. Su problema es el CPC:

- **CPC actual: $3.56**

Si reduces el CPC a $2.40 manteniendo el 4% de conversión, el CPA bajaría a:

\[
CPC / CVR = 2.40 / 0.04 = $60
\]

Eso la haría mucho más competitiva.

**Conclusión:** C no se escala agresivamente. Se mantiene como campaña de alta intención, pero con presupuesto menor, pujas más estrictas y pruebas de keywords/landing.

---

## Matiz importante

Si tu único objetivo fuera **CPA mínimo**, y todos los signups valieran exactamente lo mismo, entonces la peor campaña sería **C**, porque tiene el CPA más alto: **$88.89**.

Pero como C tiene **4% de conversión** y busca comparaciones de competidor, es probable que genere leads con más intención comercial. Por eso la estrategia más sensata es:

> **Escalar A, pausar/reducir B, y optimizar C con presupuesto limitado.**

---

# 3. Cómo redistribuir el presupuesto de $5,000

## Opción recomendada: maximizar signups con calidad

| Campaña | Presupuesto actual | Nuevo presupuesto | Cambio | Objetivo |
|---|---:|---:|---:|---|
| **A — Landing principal** | $2,100 | **$3,500** | +$1,400 / +67% | Escalar campaña ganadora |
| **B — Blog content** | $1,800 | **$0** | -$1,800 / -100% | Pausar temporalmente |
| **C — Competidor** | $3,200 | **$1,500** | -$1,700 / -53% | Optimizar alta intención |
| **Total** | **$7,100** | **$5,000** | -$2,100 | Ajustar presupuesto |

### Proyección con CPA actual

| Campaña | Presupuesto | CPA actual | Signups proyectados |
|---|---:|---:|---:|
| A | $3,500 | $46.67 | ~75.0 |
| B | $0 | $75.00 | 0 |
| C | $1,500 | $88.89 | ~16.9 |
| **Total** | **$5,000** | — | **~91.9 signups** |

CPA blended proyectado:

\[
5,000 / 91.9 = $54.41
\]

Comparado con tu CPA promedio actual:

\[
$67.62
\]

Eso sería una mejora aproximada de:

\[
(67.62 - 54.41) / 67.62 = 19.5\%
\]

menor CPA, asumiendo que las tasas se mantienen.

---

## Opción más conservadora: mantener B como prueba pequeña

Si no quieres pausar B por completo porque el blog puede tener valor de nurturing o SEO, puedes probar esto:

| Campaña | Presupuesto |
|---|---:|
| A | $3,500 |
| C | $1,000 |
| B | $500 |
| **Total** | **$5,000** |

Proyección:

| Campaña | Presupuesto | CPA actual | Signups proyectados |
|---|---:|---:|---:|
| A | $3,500 | $46.67 | ~75.0 |
| C | $1,000 | $88.89 | ~11.3 |
| B | $500 | $75.00 | ~6.7 |
| **Total** | **$5,000** | — | **~93.0 signups** |

CPA blended:

\[
5,000 / 93.0 = $53.76
\]

Esta opción mantiene tráfico informativo, pero solo con $500 para B, lo cual es mucho más prudente.

---

## Opción agresiva: si A todavía tiene inventario

Si crees que A puede absorber más presupuesto sin subir mucho el CPA:

| Campaña | Presupuesto |
|---|---:|
| A | $4,000 |
| C | $1,000 |
| B | $0 |
| **Total** | **$5,000** |

Proyección:

| Campaña | Signups |
|---|---:|
| A | ~85.7 |
| C | ~11.3 |
| **Total** | **~97.0** |

CPA blended:

\[
5,000 / 97.0 = $51.55
\]

Pero esta opción es más arriesgada porque escalar A demasiado rápido puede aumentar su CPC o bajar su CVR. Yo la usaría solo si A tiene más volumen de búsqueda disponible y puedes monitorear el CPA semanalmente.

---

# 4. A/B tests sugeridos para el próximo mes

Con pocos signups, no hagas 10 tests pequeños. Haz pocos tests de alto impacto.

Prioridad:

1. **Campaña B:** mejorar conversión de tráfico informativo.
2. **Campaña C:** bajar CPC y CPA sin perder intención.
3. **Campaña A:** escalar manteniendo CPA.

---

## A/B tests para la Campaña A

La Campaña A ya funciona. El objetivo es escalar sin romper el CPA.

### Test 1: Headline de la landing

**Control:**  
“Software de gestión de inventario para pymes”

**Variante:**  
“Reduce quiebres de stock y controla tu inventario en tiempo real”

**Hipótesis:**  
Un beneficio específico mejorará el conversion rate.

**Métrica principal:**  
CVR de landing.

**Meta:**  
Subir CVR de 3% a 3.5%+ sin subir CPA más allá de $55.

---

### Test 2: Formulario de signup

**Control:**  
Formulario con 4-5 campos.

**Variante:**  
Formulario con 2 campos: email + nombre.

**Hipótesis:**  
Menos fricción aumentará signups.

**Métrica principal:**  
Form completion rate / CVR.

**Meta:**  
Aumentar conversiones sin bajar calidad del lead.

---

### Test 3: CTA principal

**Control:**  
“Regístrate gratis”

**Variante:**  
“Solicita una demo” o “Empieza tu prueba gratis”

**Hipótesis:**  
Dependiendo del producto, un CTA más específico puede mejorar intención.

**Métrica principal:**  
CTR del CTA y CVR final.

---

### Test 4: Expansión de keywords

**Control:**  
Keywords actuales:

- “software gestion inventario”
- “inventario pymes”

**Variante:**  
Añadir keywords exactas o frases relacionadas:

- “software inventario para pequeñas empresas”
- “sistema de control de inventario”
- “app para gestionar inventario”
- “programa de inventario para pymes”

**Hipótesis:**  
Hay más volumen de búsqueda con intención similar.

**Métrica principal:**  
CPA y CVR por keyword.

**Guardrail:**  
Si el CPA supera $60, pausar esa keyword.

---

## A/B tests para la Campaña B

La Campaña B tiene tráfico barato pero convierte muy mal. El problema es intención o landing.

### Test 1: Ofrecer un lead magnet en lugar de signup directo

**Control:**  
CTA hacia registro al software.

**Variante:**  
CTA hacia recurso:

- “Descarga checklist de gestión de inventario para restaurantes”
- “Plantilla Excel para controlar inventario”
- “Guía: cómo evitar quiebres de stock”

**Hipótesis:**  
Los usuarios informativos responden mejor a un recurso gratuito que a un signup comercial.

**Métrica principal:**  
Conversion rate de captura de email.

**Meta:**  
Subir CVR de 0.5% a 1.0%+.

---

### Test 2: Landing dedicada vs. blog post

**Control:**  
Enviar tráfico del blog a un artículo.

**Variante:**  
Enviar tráfico a una landing optimizada con lead magnet.

**Hipótesis:**  
Una landing con intención comercial mejorará la conversión.

**Métrica principal:**  
CVR y CPA.

---

### Test 3: CTA dentro del artículo

**Control:**  
CTA al final del artículo.

**Variante:**  
CTA intermedio después de la primera sección + banner sticky.

**Hipótesis:**  
Capturar atención antes de que el usuario abandone.

**Métrica principal:**  
Click rate del CTA y conversion rate.

---

### Test 4: Segmentar keywords informativas

**Control:**  
Keywords amplias:

- “como gestionar inventario”
- “problemas inventario restaurante”

**Variante:**  
Separar campañas:

- “como gestionar inventario” → lead magnet.
- “problemas inventario restaurante” → caso de uso para restaurantes.

**Hipótesis:**  
El tráfico de restaurantes puede convertirse mejor con una página específica para restaurantes.

**Métrica principal:**  
CVR por segmento.

---

## A/B tests para la Campaña C

La Campaña C tiene alta intención pero CPC y CPA altos.

### Test 1: Reducir pujas

**Control:**  
Pujas actuales.

**Variante:**  
Reducir CPC máximo a $2.50-$2.80.

**Hipótesis:**  
Puedes mantener conversiones con menor CPC.

**Métrica principal:**  
CPA.

**Meta:**  
Bajar CPA de $88.89 a menos de $75.

---

### Test 2: Keywords exactas vs. frase/amplia

**Control:**  
Keywords actuales.

**Variante:**  
Probar match exacto para:

- “alternativa a [competidor]”
- “[competidor] vs”

Y pausar variantes de bajo rendimiento.

**Hipótesis:**  
Exact match puede reducir CPC y mejorar relevancia.

**Métrica principal:**  
CPC, CTR, CVR, CPA.

---

### Test 3: Landing de comparación

**Control:**  
Landing principal.

**Variante:**  
Landing específica:

- “[Tu producto] vs [competidor]”
- “Migración desde [competidor]”
- “Precios, diferencias y alternativas”

**Hipótesis:**  
Una página comparativa aumentará conversión y reducirá CPC.

**Métrica principal:**  
CVR y CPA.

---

### Test 4: Negativos para reducir tráfico caro

Añadir o revisar negative keywords como:

- “empleos”
- “trabajo”
- “login”
- “soporte”
- “facturación”
- “gratis”
- “curso”
- “plantilla”

**Hipótesis:**  
Muchas búsquedas de competidor no están buscando cambiar de software, sino resolver soporte o buscar empleo.

**Métrica principal:**  
CPA y waste spend.

---

# Estrategia sugerida para el próximo mes

## Semana 1

- Pausar Campaña B o reducirla a $500.
- Mantener Campaña A en $3,500.
- Reducir Campaña C a $1,500.
- Revisar search terms de las tres campañas.
- Añadir negative keywords urgentes.

## Semana 2

- Lanzar test de lead magnet en B.
- Lanzar test de landing comparativa en C.
- Revisar CPA semanal de A.

## Semana 3

- Si A mantiene CPA menor a $55, subir presupuesto a $3,800 o $4,000.
- Si A sube CPA por encima de $60, reducir expansión de keywords.
- Si B sube CVR a 1%+, mantenerla como campaña de nurturing.
- Si C baja CPC a $2.50-$2.80, considerar subir presupuesto.

## Semana 4

- Evaluar CPA final.
- Decidir si B vuelve, si C se escala o si A sigue siendo la campaña principal.

---

# Resumen ejecutivo

| Campaña | Veredicto | Por qué |
|---|---|---|
| **A** | **Escalar** | Mejor CPA: $46.67; mejor relación volumen/costo: 21.4 signups/$1,000. |
| **B** | **Pausar o reducir mucho** | CVR muy bajo: 0.5%; 200 clicks por signup; tráfico barato pero poco calificado. |
| **C** | **Mantener y optimizar** | Alta intención: 6% CTR y 4% CVR, pero CPC y CPA altos: $3.56 y $88.89. |

## Presupuesto recomendado inicial

| Campaña | Presupuesto |
|---|---:|
| A | $3,500 |
| B | $0 |
| C | $1,500 |
| **Total** | **$5,000** |

Con CPA actual, esto proyecta aproximadamente **92 signups** y un CPA blended de **$54.41**, mejor que el CPA promedio actual de **$67.62**.