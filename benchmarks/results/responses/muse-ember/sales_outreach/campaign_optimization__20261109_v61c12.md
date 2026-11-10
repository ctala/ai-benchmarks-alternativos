# Muse Ember — sales_outreach/campaign_optimization

- model_id: `meta/muse-ember`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 9.213s | tokens_per_second: 476.6
- input_tokens: 261 | output_tokens: 4391

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

Aquí tienes el análisis completo. Hay un dato importante antes de empezar: **gastaste $7,100 en total, un 42% por encima de tu presupuesto de $5,000.**

### 1. Métricas por campaña

|  | **A - Landing** | **B - Blog** | **C - Competidor** |
| :--- | :--- | :--- | :--- |
| **CTR** (Clicks/Impres.) | **3.0%** (1,500/50,000) | **4.0%** (4,800/120,000) | **6.0%** (900/15,000) |
| **CPC** (Costo/Clicks) | **$1.40** | **$0.38** | **$3.56** |
| **Conv. Rate** (Signups/Clicks) | **3.0%** (45/1,500) | **0.5%** (24/4,800) | **4.0%** (36/900) |
| **CPA** (Costo/Signup) | **$46.67** | **$75.00** | **$88.89** |

**Lectura rápida:**
* **A** es la más eficiente en dinero. CPC medio y conversión 6x mejor que B.
* **B** es barata en clicks, pero terrible en intención. Mucho tráfico curioso, poca compra.
* **C** tiene la intención más alta (CTR y CVR máximos), pero es carísima. Su CPC es 2.5x el de A y 9x el de B.

### 2. ¿Qué escalar y qué pausar?

**ESCALAR: Campaña A**
Es tu única campaña con CPA sano. Por cada signup pagas $46.67 vs $75 en B y $88.89 en C. Además tiene volumen (50k impresiones) para crecer sin saturarte el primer día. Es keyword transaccional pura: "software gestion inventario".

**PAUSAR (como adquisición): Campaña B**
No es un problema de anuncios, es un problema de intención. "como gestionar inventario" es informacional, no compra. Su tasa de conversión de 0.5% es 6 veces peor que A y 8 veces peor que C. Estás pagando $1,800 por 24 signups de bajísima calidad probable.

No la borres: úsala para remarketing y nurturing. Un lector de blog no se registra el primer día, pero sí puede hacerlo en 30 días si le impactas un anuncio.

**NI ESCALAR NI PAUSAR: Campaña C - Optimizar y recortar**
C es un caso especial. Convierte muy bien (4%) y tiene un CTR del 6%, señal de que hay Product-Market Fit contra tu competidor. El problema es el precio: CPC de $3.56.

Si tu LTV es alto (ej. >$300) y los signups de C se vuelven clientes 2x más que los de A, podría ser rentable. Si no, hoy estás pagando 90% más caro por signup que en A. No la escales hasta bajar su CPA.

**Revisa esto en tu CRM antes de decidir:** % de Signups que pasan a SQL / Demo / Cliente por campaña. Si C tiene mucha mejor calidad, su CPA alto se justifica. Si no, es solo tráfico caro.

### 3. Redistribución propuesta de $5,000

No pases de $2,100 a $5,000 en A de golpe. Escala 20-30% por semana para no disparar el CPC.

| Campaña | Gasto Actual | **Nuevo Presupuesto** | % |
| :--- | :--- | :--- | :--- |
| **A - Escalar** | $2,100 | **$3,250** | 65% |
| **C - Controlada** | $3,200 | **$1,250** | 25% |
| **B - Solo Remarketing** | $1,800 | **$500** | 10% |
| **Total** | **$7,100** | **$5,000** | 100% |

**Proyección si se mantiene el CPA actual:**
A: $3,250 / $46.67 = **~70 signups**
C: $1,250 / $88.89 = **~14 signups**
B/Remarketing: $500 / $75 = **~7 signups**
**Total: ~91 signups por $5,000** (CPA blended ~$55) vs. 105 signups por $7,100 hoy (CPA $67.62). Menos volumen, mucha más eficiencia.

En C, no gastes los $1,250 en las dos keywords juntas. Dale el 80% a "alternativa a [competidor]" (exacta, suele convertir mejor) y 20% a "[competidor] vs".

### 4. A/B Tests para el próximo mes

Prioriza tests que ataquen el problema de cada campaña:

**Test 1 - Campaña C: Landing de comparación (Prioridad 1)**
* **Hipótesis:** Mandar a la landing genérica de A está matando el CPA de C.
* **A (Control):** Landing principal actual.
* **B (Variante):** Landing específica: tabla comparativa de precios/funciones, "Migra en 1 día", prueba social de ex-clientes del competidor.
* **Métrica de éxito:** Bajar CPA de $88.89 a <$65 y subir CVR de 4% a 6%.

**Test 2 - Campaña B: Cambiar la oferta (Prioridad 2)**
* **Hipótesis:** Un lector de blog no quiere "Regístrate", quiere resolver su problema.
* **A (Control):** Artículo del blog sin CTA fuerte.
* **B (Variante):** Mismo artículo + CTA contextual: Checklist descargable "Control de inventario para restaurantes en PDF" a cambio de email, luego nurture de 5 emails.
* **Métrica de éxito:** Subir CVR de 0.5% a >2%. Si no lo logras, confirmas que B debe ser solo SEO/remarketing.

**Test 3 - Campaña A: Oferta Demo vs. Trial**
* **A:** "Pide una demo"
* **B:** "Prueba gratis 14 días, sin tarjeta"
* **Métrica:** CPA y % de demos completadas. El trial suele dar más signups pero de menor calidad.

**Test 4 - Campaña A: Copy de anuncios**
* **A:** Beneficio: "Ahorra 10h/semana en inventario"
* **B:** Prueba social + Específico: "+1,200 pymes ya lo usan | Software en español"
* **Métrica:** CTR y CPC. Buscas bajar el CPC de $1.40.

**Test 5 - Campaña C: Separar keywords**
Crea 2 campañas separadas con presupuestos independientes: "alternativa a" vs "vs". Casi seguro que una está subsidiando a la otra. Pausa la perdedora a la semana 2.

**Regla de oro:** 1 test activo por campaña a la vez, mínimo 2 semanas o 1,000 clicks por variante antes de declarar ganador.

**Resumen TL;DR:** Escala A, pausa B como captación, recorta C y optimiza su landing. Con $5,000 bien repartidos deberías bajar tu CPA blended de $67 a ~$55 y conseguir signups de mucha mayor intención.