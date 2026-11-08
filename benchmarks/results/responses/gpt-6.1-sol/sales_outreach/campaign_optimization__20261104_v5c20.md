# GPT-6.1 Sol — sales_outreach/campaign_optimization

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 6.93 | quality: 8.0
- latency_total: 24.169s | tokens_per_second: 65.2
- input_tokens: 261 | output_tokens: 1577

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

Las fórmulas son:

- **CTR** = clics ÷ impresiones
- **CPC** = costo ÷ clics
- **CPA** = costo ÷ signups
- **Tasa de conversión** = signups ÷ clics

| Campaña | CTR | CPC | CPA por signup | Tasa de conversión |
|---|---:|---:|---:|---:|
| **A — Landing principal** | 3,00% | $1,40 | **$46,67** | 3,00% |
| **B — Blog** | 4,00% | **$0,375** | $75,00 | 0,50% |
| **C — Competidor** | **6,00%** | $3,56 | $88,89 | **4,00%** |
| **Total** | 3,89% | $0,99 | $67,62 | 1,46% |

**Ojo con el presupuesto:** el gasto reportado suma **$7.100**, no $5.000. La redistribución propuesta abajo implica reducir el gasto mensual en **$2.100**, aproximadamente un 29,6%.

## 2. ¿Qué escalar y qué pausar?

**Si el objetivo es maximizar signups y estos tienen una calidad similar, escalaría A, pausaría C y mantendría B con un presupuesto pequeño de optimización.**

### Escalar A
Es la campaña más eficiente para generar registros:

- CPA de **$46,67**, frente a $75 de B y $88,89 de C.
- Su CPA es **37,8% menor que el de B** y **47,5% menor que el de C**.
- Las keywords sugieren una intención comercial más directa que las búsquedas informativas de B.

Aumentaría el presupuesto gradualmente: al captar más tráfico, el CPA podría subir.

### Pausar C, de forma provisional
Aunque tiene el mejor CTR y la mejor conversión, el clic es demasiado caro:

- Su CPC es **2,54 veces** el de A.
- Su CPA es **90,5% mayor** que el de A.

La buena conversión no compensa el costo del tráfico. **La excepción:** si sus registros se convierten en clientes o generan ingresos a una tasa significativamente superior, podría merecer mantenerla. Hoy solo tenemos datos de signups.

### Reducir B y optimizarla
B consigue tráfico barato, pero convierte poco:

- Solo **1 de cada 200 clics** termina en signup.
- Su CPA es **60,7% mayor** que el de A.
- Con su CPC actual, necesitaría subir la conversión del **0,50% al 0,80%** para igualar aproximadamente el CPA actual de A.

Antes de pausarla por completo, revisaría si contribuye a conversiones posteriores o asistidas, dado que lleva al blog.

## 3. Redistribución de los $5.000

Mi propuesta inicial sería:

| Campaña | Presupuesto mensual | Participación | Función |
|---|---:|---:|---|
| **A** | **$4.500** | 90% | Principal fuente de signups |
| **B** | **$500** | 10% | Validar mejoras de conversión |
| **C** | **$0** | 0% | Pausada hasta revisar calidad y costos |
| **Total** | **$5.000** | **100%** | |

**Proyección orientativa si los CPA se mantuvieran:**

- A: $4.500 ÷ $46,67 ≈ **96 signups**.
- B: $500 ÷ $75 ≈ **7 signups**.
- Total: **103 signups**, con un CPA combinado cercano a **$48,50**.

No es un pronóstico garantizado: más que duplicar el gasto de A puede cambiar su mezcla de tráfico y elevar su CPA. Antes de hacerlo, revisaría si pierde impresiones por presupuesto y aumentaría la inversión por etapas.

**Regla de decisión:** mover presupuesto según el **CPA marginal** —el costo de los registros adicionales—, no solo según el promedio histórico.

## 4. A/B tests para el próximo mes

Con este volumen, priorizaría **un test principal en A y uno exploratorio en B**, evitando repartir los datos entre muchas variantes.

### Test 1 — A: propuesta de valor de la landing
- **Control:** landing actual.
- **Variante:** encabezado alineado con la búsqueda, beneficio concreto y prueba social visible.
- **Ejemplo:** “Software de inventario para pymes” acompañado de beneficios demostrables y testimonios reales.
- **Métrica principal:** tasa de signup.
- **Control de calidad:** activación del usuario después del registro.

Mantendría anuncios y segmentación estables para aislar el efecto de la landing.

### Test 2 — B: puente entre contenido y producto
- **Control:** artículo actual.
- **Variante:** CTA contextual dentro del artículo que conecte el problema con el producto. Por ejemplo, en contenido sobre restaurantes: “Controla tu inventario de restaurante con [producto]”.
- **Métrica principal:** signups por visitante del artículo.
- **Métrica de diagnóstico:** clics en el CTA.
- **Referencia económica:** alcanzar aproximadamente **0,80% de conversión** al CPC actual igualaría el CPA histórico de A.

Con $500 y una conversión tan baja, este test podría necesitar más de un mes para dar una conclusión fiable.

### Siguiente test en A: fricción del formulario
Después del primer test, compararía el formulario actual con una versión más corta, solicitando solo los campos imprescindibles. Mediría **signup y activación**, porque más registros no necesariamente significan mejores usuarios.

**Antes de ejecutar:** verificaría el tracking de conversiones, la ventana de atribución y la calidad de los registros por campaña. La decisión final debería basarse en **costo por cliente e ingresos**, no únicamente en costo por signup.