# Muse Spark 1.3 — sales_outreach/campaign_optimization

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 23.398s | tokens_per_second: 132.9
- input_tokens: 261 | output_tokens: 3109

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

Aquí tienes el análisis completo de tus 3 campañas. Estás gastando **$7,100/mes** para un presupuesto de $5,000, así que tienes que recortar sí o sí.

### 1. Cálculo de métricas

Fórmulas:
**CTR = Clicks / Impresiones | CPC = Costo / Clicks | CR = Signups / Clicks | CPA = Costo / Signups**

| Campaña | CTR | CPC | Conv. Rate (Click -> Signup) | CPA |
| :--- | :--- | :--- | :--- | :--- |
| **A - Landing principal** | 1,500 / 50,000 = **3.0%** | $2,100 / 1,500 = **$1.40** | 45 / 1,500 = **3.0%** | $2,100 / 45 = **$46.67** |
| **B - Blog content** | 4,800 / 120,000 = **4.0%** | $1,800 / 4,800 = **$0.38** | 24 / 4,800 = **0.5%** | $1,800 / 24 = **$75.00** |
| **C - Competidor** | 900 / 15,000 = **6.0%** | $3,200 / 900 = **$3.56** | 36 / 900 = **4.0%** | $3,200 / 36 = **$88.89** |

**Total actual:** 105 signups por $7,100 = **CPA promedio de $67.62**

### 2. ¿Qué escalar y qué pausar?

**ESCALAR: Campaña A. Es tu ganadora.**
Tiene el mejor CPA por lejos: **$46.67**, un 38% más barato que B y un 47% más barato que C. Su Conversion Rate de 3.0% demuestra intención comercial real ("software gestion inventario"). CPC razonable de $1.40.

**PAUSAR (como captación directa): Campaña B. Es una trampa de vanity metrics.**
Te engaña porque tiene CTR alto (4.0%) y CPC baratísimo ($0.38). Pero su CR es terrible: **0.5%**. Es 6x peor que A y 8x peor que C. Las keywords son informacionales ("como gestionar...", "problemas..."), la gente quiere aprender, no comprar. Estás pagando $1,800 por solo 24 signups.

**MANTENER PERO OPTIMIZAR Y CAPEAR: Campaña C. No la pauses.**
Tiene la mejor calidad de tráfico: CTR 6.0% y CR 4.0% (el más alto). La intención es altísima ("alternativa a [competidor]"). El problema es el costo: CPC de $3.56 te lleva a un CPA de **$88.89, el peor de todos**, casi 2x el de A. No puedes escalarla a ciegas porque además tiene poco volumen (solo 15,000 impresiones).

> Conclusión: A gana en eficiencia, C gana en intención pero es muy cara, B trae clics baratos que no convierten.

### 3. Cómo redistribuir los $5,000

No puedes poner todo a C porque no tiene volumen, y no puedes poner todo a A sin antes revisar impression share. Mi propuesta:

**A: $3,250 (65%) | C: $1,500 (30%) | B: $250 (5% solo test)**

1.  **Campaña A: $3,250.** Es donde cada dólar rinde más. Aumentas +55% vs ahora.
2.  **Campaña C: $1,500.** La recortas a menos de la mitad (-53%). La mantienes por su alta intención, pero con budget cap diario y puja máxima para forzar a Google a bajar el CPC.
3.  **Campaña B: $250 o $0.** Pausala como campaña de Signups. Deja $250 solo para remarketing o para captar emails con un lead magnet, no para pedir signup directo. Te ahorras $1,550 al instante.

**Proyección con el mismo rendimiento:**
A: ~70 signups + C: ~17 signups + B: ~3 signups = **~90 signups por $5,000 = CPA de $55.5**
vs. ahora: 105 signups por $7,100 = CPA de $67.6
**Gastas 30% menos y solo pierdes 14% de signups.** Y ese CPA bajará más cuando optimices C.

### 4. A/B Tests para el próximo mes

No testees todo a la vez. Prioriza por impacto:

**Test 1 [Prioridad Alta - Campaña A]: Landing acorta fricción**
Hipótesis: El CR de 3% puede subir a 4%+.
A: Landing actual (formulario largo)
B: Mismo hero, pero formulario solo Email + Nombre empresa + CTA "Probar 14 días gratis" + prueba social arriba (logos + "4.8/5 en Capterra")
Métrica éxito: Conversion Rate. Necesitas ~1,000 clics por variante.

**Test 2 [Prioridad Alta - Campaña C]: Landing comparativa**
Hipótesis: Mandar tráfico de competidor a tu landing genérica baja el Quality Score y sube el CPC.
A: Landing principal actual
B: Landing "/vs-[competidor]" con tabla comparativa, headline "La alternativa a [Competidor] sin [dolor principal]" y CTA "Migrar en 1 clic"
Métrica éxito: Bajar CPA de $88.89 a <$60 y subir CR de 4% a 6%.

**Test 3 [Prioridad Media - Campaña C]: Frenar CPC**
Hipótesis: Estás en guerra de pujas.
A: Puja manual / Maximizar clics actual
B: Cambiar a tCPA a $60 con CPC máximo de $2.50 + solo Exact Match + horario laboral B2B (Lun-Vie 8-19h)
Métrica éxito: CPC y CPA.

**Test 4 [Prioridad Media - Campaña B]: Cambiar el objetivo**
Hipótesis: Pedir signup a lector de blog no funciona.
A: CTA actual "Crear cuenta"
B: CTA "Descargar Plantilla de Inventario Gratis [Excel]" -> entra a flujo de email nurturing de 5 correos -> luego pide signup.
Métrica éxito: Costo por Email (<$2) y tasa Email -> Signup a 30 días. Mide B por otro funnel, no por CPA directo.

Empieza pausando B esta semana y moviendo ese presupuesto a A. Con eso solo ya vuelves a tu presupuesto de $5k.