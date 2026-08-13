# Tencent Hy3 — strategy/business_model_validation

- model_id: `tencent/hy3`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 56.001s | tokens_per_second: 77.2
- input_tokens: 204 | output_tokens: 4322

## Entrada exacta (lo que recibió el modelo)

**user:**

Quiero crear una app que conecta restaurantes pequenos con proveedores de ingredientes locales. El modelo es marketplace con 15% de comision por transaccion.

Mi hipotesis: los restaurantes pequenos pierden mucho tiempo llamando a multiples proveedores y quieren una solucion digital.

Actua como un VC esceperico. Hazme las preguntas dificiles que me harian en un pitch:
1. Identifica los 5 riesgos principales de este modelo
2. Por que podria NO funcionar en LATAM especificamente?
3. Que tendria que ser verdad para que funcione? (key assumptions)
4. Cual es el escenario donde fracaso rapido y por que?
5. Si solo tuviera $10K para validar, que harias?

No seas amable. Se brutalmente honesto.


## Respuesta completa

Mira, siéntate. Antes de que saques tu deck de 20 diapositivas con logos de unicornios y proyecciones a 5 años, vamos a destripar tu idea. El modelo de marketplace de ingredientes para restaurantes no es nuevo; de hecho, docenas de startups con millones de dólares detrás quebraron intentando exactamente lo mismo. Tu hipótesis de que "pierden tiempo llamando y quieren digitalización" es el cliché más vendido en el ecosistema desde 2014. 

La realidad es que al restaurante le importa una mierda tu app si el tomate le llega barato y a tiempo. Vamos a los golpes:

### 1. Los 5 riesgos principales de este modelo (y por qué tu 15% es una fantasía)
1. **El problema del "chicken and egg", pero en modo hardcore:** Los proveedores locales son informales, no tienen catálogos digitales ni usan sistemas de pago electrónico. Si no tienes oferta (proveedores) al instante, el restaurante se va. Si no tienes demanda, el proveedor ni te contesta. Tu 15% de comisión es un costo que ninguno de los dos quiere absorber al principio.
2. **Commoditización y "Shedding" (saltarse la plataforma):** Si un restaurante consigue un buen proveedor de aguacates por tu app, ¿qué crees que va a pasar en el pedido número tres? Se van a intercambiar el número de celular y te van a sacar. Los ingredientes no son SaaS; no hay fidelidad por software cuando se trata de papas y cebollas.
3. **Logística y última milla:** ¿Quién lleva los ingredientes? Los proveedores locales no hacen entregas eficientes ni ruteo. Si tu app tiene que encargarse de la logística para que funcione, dejaste de ser un marketplace del 15% y te volviste una empresa de distribución con márgenes de miseria y camiones que mantener.
4. **Ticket promedio bajo vs. CAC (Costo de Adquisición) alto:** Un restaurante pequeño compra quizás $300 al mes de ingredientes específicos. Con tu 15%, ganas $45. ¿Cuánto te va a costar adquirir ese restaurante y ese proveedor? Probablemente $80-$150. Vas a perder dinero en cada transacción hasta que te quedes sin capital.
5. **Fricción de calidad y devoluciones:** La comida fresca se daña, llega tarde o no es lo prometido. Cuando un chef se queda sin ajo a las 10 AM porque tu app falló, no le importa tu "política de reembolso"; te va a odiar, borrará la app y volverá a su proveedor de toda la vida. La gestión de calidad en perecederos es una pesadilla operativa.

### 2. Por qué podría NO funcionar en LATAM específicamente (donde la informalidad manda)
* **Efectivo y confianza sobre eficiencia:** En LATAM, los negocios pequeños operan al contado y a base de relaciones personales. "El de la esquina me fía los plátanos hasta el viernes porque conoce a mi mamá". Tu app no fía y encima cobra comisión. El proveedor informal no va a bancarizar sus ventas ni pagar fees de tarjeta solo por tu interfaz.
* **Las Centrales de Abasto (Mercados):** En casi toda LATAM existe un mercado central donde el restaurante compra todo en un solo lugar, negociando precio cara a cara. Tu app fragmenta esa compra y le pone un *markup* del 15%. ¿Por qué pagar más por lo mismo?
* **Penetración y hábitos:** Muchos de estos pequeños proveedores ni siquiera tienen un smartphone decente o datos suficientes para usar tu app. Y el restaurante, en plena hora pico, no tiene tiempo de estar scrolleando para encontrar cilantro; marca al que sabe que se lo resuelve en 10 minutos.

### 3. Qué tendría que ser verdad para que funcionara (Key Assumptions)
Para que esta idea no sea basura, tendría que ser incuestionablemente verdad que:
* Los restaurantes valoran su tiempo por encima del ahorro de unos pesos (en márgenes bajos, esto es falso; el restaurante pequeño es obsesivamente ahorrativo).
* Los proveedores locales tienen un excedente de inventario real y necesitan desesperadamente un canal de venta digital para justificar tu comisión (la mayoría ya vende todo por teléfono).
* Existe una categoría de ingredientes *difíciles de conseguir* (orgánicos, especializados, importados) donde el restaurante SÍ paga la conveniencia. Si compites por ingredientes básicos, pierdes por goleada.

### 4. El escenario donde fracasas rápido y por qué
Fracasas en los primeros 6 meses así: Consigues 15 restaurantes "interesados". Tú llamas a 30 proveedores; solo 4 entran porque "no entienden el celular". Esos 4 proveedores suben precios un 15% para no perder su margen, o directamente ignoran los pedidos de la app. El restaurante hace un pedido, el proveedor entrega tarde o mal, el chef se enoja. El restaurante vuelve a llamar a su proveedor de confianza. Tú te quedas con una app vacía, gastaste $5k en desarrollo y no puedes pagar el CAC de los siguientes. Cerraste.

### 5. Si solo tuvieras $10K para validar, qué harías (sin escribir código)
* **No construyas la app. Construye un "Concierge MVP" en WhatsApp o Excel.** Usa $2K para contratar a un estudiante que actúe como tu "plataforma humana" llamando a proveedores y restaurantes.
* **Compra un listado de restaurantes y llámalos.** Ofrece ser su "departamento de compras". Por $8K restantes, pagas a alguien para que sea el intermediario manual durante 2 meses.
* **Mide la retención, no los "leads".** Si después de 30 días los restaurantes siguen pidiéndote que les consigas cosas (aunque tu margen sea 0 porque lo haces manual), tienes algo de tracción real. Si en 30 días vuelven a sus viejos hábitos, tu hipótesis era basura y te ahorraste $100k en desarrollo.
* **Testea el WTP (Willingness To Pay):** Pídeles a los restaurantes que te paguen por adelantado un fee mensual por "ahorrarles tiempo". Si nadie te paga un centavo por adelantado, no tienen tanto dolor como dices y la app es solo un capricho, no una necesidad.

Ahora, responde: ¿tienes realmente acceso a estos restaurantes o solo es una idea en tu cabeza?