# Muse Glimmer 30B — sales_outreach/campaign_optimization

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.75 | quality: 10.0
- latency_total: 17.583s | tokens_per_second: 152.8
- input_tokens: 309 | output_tokens: 2687

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

**1. Métricas por campaña**

*Fórmulas: CTR = Clicks/Impresiones, CPC = Costo/Clicks, CPA = Costo/Signups, CR = Signups/Clicks*

**Campaña A - Landing principal**
* CTR = 1.500 / 50.000 = **3.0%**
* CPC = 2.100 / 1.500 = **$1.40**
* CPA = 2.100 / 45 = **$46.67**
* CR = 45 / 1.500 = **3.0%**

**Campaña B - Blog content**
* CTR = 4.800 / 120.000 = **4.0%**
* CPC = 1.800 / 4.800 = **$0.38**
* CPA = 1.800 / 24 = **$75.00**
* CR = 24 / 4.800 = **0.5%**

**Campaña C - Competidor**
* CTR = 900 / 15.000 = **6.0%**
* CPC = 3.200 / 900 = **$3.56**
* CPA = 3.200 / 36 = **$88.89**
* CR = 36 / 900 = **4.0%**

**2. Qué escalar y qué pausar**

**Escalar: Campaña A.** Es la única eficiente en costo por resultado.
CPA $46.67 vs $75 de B y $88.89 de C. Con un CR de 3.0% es 6x mejor que B y con CPC $1.40 es 2.5x más barato que C.

**Pausar / Reducir drásticamente: Campaña B.** 
Tiene el CPC más barato $0.38 y CTR 4%, pero la intención es informativa. El CR es solo 0.5% y el CPA $75 es +61% más caro que A. Estás comprando mucho tráfico barato que no convierte.

**Campaña C mantener en test reducido.** 
Es la mejor en calidad: CTR 6% y CR 4.0% el más alto. El problema es el CPC $3.56 que dispara el CPA a $88.89, +90% vs A. Tiene valor por intención de compra alta, pero no es escalable así.

**3. Redistribución del presupuesto $5.000/mes**

Con el gasto actual de $7.100 estás sobre presupuesto. Prioridad a CPA bajo y volumen.

Propuesta conservadora:

* **Campaña A: $3.500 = 70%** 
  Proyección con CPC actual: ~2.500 clicks -> ~75 signups a CPA $46.67
* **Campaña C: $1.250 = 25%**
  Proyección: ~350 clicks -> ~14 signups. Se mantiene para validar calidad y optimizar CPC.
* **Campaña B: $250 = 5%** o pausar
  Solo para remarketing o como fuente de datos. Si se pausa totalmente, los $250 van a A.

Alternativa agresiva si quieres maximizar signups:
A $3.200 + C $1.800 + B $0. Esperas ~68 signups de A y ~10 de C = ~78 signups vs los 105 actuales con $7.100.

**4. A/B tests para el próximo mes**

**Para Campaña A - Escalar con eficiencia**
* Landing Page: Formulario corto 3 campos vs formulario largo con campos de empresa + email corporativo. Hipótesis: menos fricción sube CR.
* Anuncio: Headline con beneficio directo "Software de inventario para pymes" vs prueba social "Usado por +500 pymes". Testear CTR y CR.

**Para Campaña C - Bajar CPC y CPA**
* Anuncio: Mensaje de diferenciación vs mensaje de ataque. Ej: "Alternativa a [Competidor] sin costo de implementación" vs "Menos errores de inventario que [Competidor]".
* Extensiones: Testear con y sin sitelinks de comparativa y testimonios. Mejora CTR y calidad.

**Para Campaña B - Si decides mantener**
* Separar intención: Crear grupo de anuncios solo para keywords transaccionales tipo "precio software inventario" y mandar a landing principal, no a blog.
* Test de destino: Blog post vs landing principal para las mismas keywords. Medir CR real.

Recomendación extra: Añade keywords negativas a B como "gratis", "pdf", "ejemplo" y crea lista de remarketing de visitantes de blog para impactarlos con Campaña A.

¿Quieres que te modele la proyección de signups con la redistribución propuesta y un objetivo de CPA máximo?