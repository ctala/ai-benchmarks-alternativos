# Muse Ember — strategy/business_model_validation

- model_id: `meta/muse-ember`
- success: True  | final: 8.89 | quality: 10.0
- latency_total: 11.234s | tokens_per_second: 360.1
- input_tokens: 169 | output_tokens: 4045

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

Te voy a hacer el pitch que te haría un VC que ya vio morir 20 ideas como esta. No es un problema de ejecución. Es un problema de modelo.

Tu hipótesis es falsa: **el restaurante pequeño no tiene un problema de descubrimiento. Tiene un problema de precio, crédito y confiabilidad.** Ya conoce a sus proveedores. Compra lo mismo cada semana. No necesita una app para encontrar un tomate nuevo.

### 1. Los 5 riesgos que te matan

**1. Desintermediación inmediata (el riesgo #1)**
En cuanto presentas a un restaurante con un proveedor, ¿por qué van a seguir pagándote 15% para pedir lo mismo por WhatsApp? En un marketplace de commodities repetitivos, la fuga es del 80-90%. No tienes moat, no controlas la relación, no controlas la logística. Solo eres un directorio caro.

Pregunta de pitch: *¿Qué impide que te salteen en la semana 2?*

**2. Tu unit economics es imposible**
Hagamos la matemática que no hiciste:

Restaurante pequeño LATAM: vende ~$8k-12k USD/mes. Su food cost es 30%. Compra ~$3k en ingredientes.
Tu 15% = $450/mes = **4.5% extra sobre sus ventas.**

El margen neto de un restaurante pequeño es 5-10%. Tú le acabas de borrar la mitad o todo el margen. O el proveedor absorbe tu comisión (su margen en perecederos es 15-25%, lo destruyes) o la traslada al precio y el restaurante te ve 15% más caro que en el mercado.

15% solo funciona en marketplaces de alto margen y baja frecuencia. En B2B de alimentos, lo viable es 3-7% *si* además das logística y crédito. Tú no das nada.

**3. Cold start doble y brutal**
Necesitas densidad en un radio de 3-5 km. No en una ciudad. En un barrio. Porque nadie paga delivery de $15 por un pedido de $60 de verduras. Cada barrio es un marketplace nuevo. Cada ciudad es empezar de cero. Tu CAC offline para conseguir un restaurante es $150-300. Para un proveedor que no tiene ni email, más. Con un LTV realista de $50-80/mes después de pasarela, soporte y devoluciones, tardas 6 meses en recuperar CAC. Y los restaurantes pequeños cierran y cambian de proveedor cada 3 meses.

**4. Logística, calidad y responsabilidad legal**
Si el pescado llega mal o se rompe la cadena de frío, ¿de quién es la culpa? Tuya. Tú no controlas al proveedor, no tienes bodega, no tienes camión refrigerado. En alimentos perecederos, 1 mala entrega te quema la reputación en el barrio entero. Y en LATAM, sin permisos sanitarios claros, tú te vuelves el responsable.

No eres una app. Eres una cadena de frío sin cadena de frío.

**5. No hay dolor de "llamar a múltiples proveedores"**
Eso lo inventaste tú. El dolor real es: "mi proveedor me quedó mal, me subió el precio, no me fía este mes". Una app no resuelve eso. De hecho, lo empeora: le quitas la negociación, el fiado y la relación personal que es su verdadero seguro.

### 2. Por qué en LATAM específicamente es peor

**WhatsApp ES la app.** No compites contra otro startup. Compites contra un grupo de WhatsApp que ya funciona, es gratis y tiene la confianza. Pedirle a un señor de 55 años que vende tacos que instale tu app, cargue tarjeta y aprenda un flujo nuevo para ahorrar 10 minutos de llamadas... no va a pasar.

**Informalidad y fiado:** Gran parte de la compra es en efectivo, contra entrega, o a crédito de 15-30 días. Tu proveedor informal no tiene RUC/factura electrónica, no acepta pasarela, no quiere dejar rastro. El restaurante necesita factura para su contabilidad. Estás en un callejón: si formalizas, excluyes a la mitad de la oferta.

**Cultura de tocar el producto:** El cocinero va al mercado a las 5am a elegir el pescado, oler el pollo, regatear. Eso no es ineficiencia para él. Es control de calidad. Digitalizarlo sin resolver eso es venderle un problema.

**Fragmentación y seguridad:** Mover perecederos en CDMX, Bogotá, Lima o Buenos Aires sin logística propia es un caos. Tráfico, inseguridad, rutas imposibles para pedidos de $50.

### 3. Qué tendría que ser verdad para que funcione

Todas. Si falla UNA, mueres:

1. Los restaurantes están dispuestos a pagar 15% extra por ahorrar tiempo, y no buscarán el mismo precio en otro lado.
2. Los proveedores aceptan pagar 15% y además esperar a que les pagues tú, en vez de cobrar directo.
3. Ambos aceptan pagar con tarjeta/transferencia digital y renunciar al efectivo/fiados.
4. Las transacciones se quedan en tu plataforma >70% después del primer pedido.
5. Puedes garantizar calidad y entrega a tiempo sin tener logística propia.
6. Hay densidad suficiente en 1 zona para que el delivery no te coma el margen.
7. El restaurante compra con frecuencia suficiente (8-12 veces/mes) y no cierra/churnea en 90 días.
8. Puedes conseguir CAC < $50 de forma repetible.

¿Te suena realista? A mí no.

### 4. Escenario de fracaso rápido (el más probable)

**Mes 0-2:** Lanzas en una ciudad. Consigues 80 restaurantes curiosos con ads y visitas en frío. 25 proveedores se registran.
**Mes 2-3:** Primeros 40 pedidos. La mitad son por impulso. A la semana 2, el restaurante y el proveedor ya tienen el WhatsApp del otro. Los pedidos desaparecen de tu app.
**Mes 3-4:** Los proveedores te dicen: "la comisión es muy alta, súbela a 5% o me voy". Los restaurantes te dicen: "está más caro que en el mercado".
**Mes 6:** Tienes 100 usuarios registrados, 3 pedidos al mes en la plataforma, y llevas 6 meses construyendo una app que nadie quiere usar dos veces.

No fracasas por falta de usuarios. Fracasas porque nadie tiene incentivo para quedarse.

### 5. Si tuviera $10K, qué haría (y qué NO haría)

**NO construyas la app. Ni contrates un dev. Ni hagas logo.**

Con $10K validas si existe disposición a pagar, no si sabes programar.

**Plan de 30 días:**

**$2K - Entrevistas de problema, no de solución:** 50 entrevistas en persona en 2 barrios. No les muestres la idea. Pregunta: ¿a quién le compras, cuánto, cómo pagas, qué te cagó la última vez? Si no mencionan "tiempo buscando proveedores" como top 3 dolor, tu hipótesis está muerta.

**$3K - Concierge manual en WhatsApp:** Elige UNA categoría (ej: solo panaderías o solo mariscos) y UN barrio. Tú eres la app. Grupo de WhatsApp. Tú tomas pedidos en Google Sheets, coordinas por teléfono, cobras por link de Mercado Pago/Stripe y te quedas con 15% manualmente. Entrega el proveedor.

**$5K - Incentivo para la prueba real:** No pagues ads masivos. Paga para conseguir 20 restaurantes que hagan SU PRIMER PEDIDO PAGADO a través de ti. Si no puedes conseguir 20 que paguen, no hay negocio.

**Criterio de muerte:** Si en 30 días no tienes 10 restaurantes que repitan un segundo pedido pagado a través de ti (sin que se fuguen a WhatsApp directo), y 5 proveedores que acepten el 15% dos veces, aborta. No es "necesito más tiempo". Es no hay mercado.

Si lo logras, recién ahí piensas en tecnología. Y probablemente pivotarás a un modelo de logística + crédito, porque la comisión por conectar no se sostiene.

**Veredicto brutal:** Esto es una idea de 2014 que ya fracasó en EE.UU. y Europa con mejores tarjetas, mejor logística y más digitalización. En LATAM tienes todos los problemas multiplicados por dos.

Si sigues enamorado, no me vengas con descargas o registros. Vuelve cuando tengas 10 restaurantes que te hayan pagado 15% dos veces seguidas por WhatsApp.