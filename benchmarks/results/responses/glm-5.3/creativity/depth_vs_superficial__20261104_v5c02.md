# GLM 5.3 — creativity/depth_vs_superficial

- model_id: `z-ai/glm-5.3`
- success: True  | final: 7.45 | quality: 9.0
- latency_total: 131.925s | tokens_per_second: 69.0
- input_tokens: 152 | output_tokens: 9100

## Entrada exacta (lo que recibió el modelo)

**user:**

Un emprendedor te dice: "Estoy pensando en usar IA para mi startup de delivery de comida en Santiago. Que deberia hacer?"

Da una respuesta que demuestre PROFUNDIDAD real, no consejos genericos.
Incluye:
- Al menos 2 ideas especificas que NO sean obvias (no digas "usa IA para optimizar rutas", eso lo sabe cualquiera)
- Numeros o estimaciones concretas cuando sea posible
- Un riesgo no obvio que otros no mencionarian
- Una opinion contrarian o controversia sobre el tema

No me des una lista generica de "5 formas de usar IA". Quiero pensamiento original.


## Respuesta completa

Primero, un reframe incómodo: la pregunta no es "dónde meto IA", sino "¿qué negocio soy realmente?". Porque la economía del delivery en Santiago es brutal: comisiones de mercado de 20-30% (PedidosYa/Rappi/Uber Eats), costo de reparto de ~CLP 2.500-4.000 por entrega, ticket promedio de ~CLP 15-18.000, y margen neto de 3-5% si lo haces todo bien. En ese contexto, la mayoría de las aplicaciones de IA son decoración. Aquí van las que no lo son.

**Idea 1: No compitas con PedidosYa. Véndele a los restaurantes el arma para dejarlos.**

En Chile, una fracción enorme de pedidos ya ocurre por WhatsApp — los restaurantes lo hacen informalmente precisamente para evitarse la comisión del 25%. El cuello de botella no es logístico: es que alguien tiene que estar contestando mensajes, y se pierden pedidos en horas punta o de noche.

Un agente de IA sobre WhatsApp que contesta el 100% de los pedidos, arma la orden de forma estructurada, manda link de prepago (Khipu o Webpay) para eliminar el no-show —que en canales informales puede ser 5-15% de los pedidos— y hace upsell inteligente ("¿le agrego una bebida?") es un empleado que trabaja 24/7. El contador de WhatsApp cuesta ~CLP 800.000-1.000.000/mes costo total; tu SaaS se vende a CLP 120-180.000/mes. Upsell bien hecho sube el ticket 10-15%. ROI inmediato, no promesa.

Santiago tiene del orden de 20.000+ locales de comida. Si capturas 2.000 a CLP 150.000/mes, tienes ~US$300k de MRR con márgenes de software. Y un detalle técnico importante: hazlo texto-primero. El español chileno (rapidez, voseo, "cachai", "al tiro") sigue siendo un campo minado para IA de voz; el texto es donde la tecnología ya es confiable hoy.

**Idea 2: La IA que importa no es rutas, es desplazar demanda fuera del peak.**

~60-65% de los pedidos ocurren en unas 5 horas (almuerzo + cena). Tu cocina está infrautilizada el resto del día y saturada justo cuando más ganas. La jugada: forecasting de demanda por SKU/comuna/día para **pre-producir los top sellers fuera de hora**. La comida chilena es ideal para esto — empanadas, cazuelas, pastel de choclo, bowls aguantan producción anticipada sin degradarse.

Efecto estimado: +20-30% de capacidad en hora punta (de cocinar a solo empaquetar), tiempo de entrega de ~40 a ~25 minutos, y capturas los pedidos que hoy se rechazan o demoran justo cuando el cliente más paga.

Nota por qué esto importa más en Chile que en Silicon Valley: el repartidor cuesta ~US$6-7/hora. La tesis clásica de IA ("reemplazar trabajo caro") es débil aquí. El ROI real de IA en Chile es del lado de **ingresos** (upsell, conversión, captura de pedidos perdidos), no del lado de costos laborales.

Bonus rápido con matemática que casi nadie hace: el fraude y abuso de promociones en delivery en LatAm se come 1-3% del GMV. Si tu margen neto es 3-5%, recuperar 1 punto de GMV con ML de detección es **~25% de tu utilidad**. Es la única IA "de costos" con ROI claro a pequeña escala.

**El riesgo que nadie te va a decir: tu IA factura en pesos y cuesta en dólares.**

Inferencia, APIs, cómputo: todo cotizado en USD. Si cada orden pasa por 3-5 puntos de contacto con IA, estás gastando ~US$0,05-0,15 por pedido contra ingresos en CLP. El peso chileno se movió ~20% en 2022 y movimientos de 15-25% en un año son históricamente normales. Y acá lo perverso: **el éxito escala tu exposición** — cada mes que creces, tu factura en dólares crece con los pedidos, mientras la competencia te impide subir precios. Mitigaciones: modelos pequeños para el 80% del tráfico (y los grandes solo para casos difíciles), y cotizar tu SaaS indexado a USD/UF en contratos B2B — es práctica estándar en Chile y los compradores la aceptan.

**Mi opinión contrarian: la IA no va a crear el próximo PedidosYa. Va a destruirlo.**

Los marketplaces existen porque el stack software + soporte + pagos + matching costaba millones y requería escala. Ese costo se colapsó a ~CLP 150.000/mes por restaurante. La comisión del 25% es una ballena esperando ser fileteada, y la IA nativa es el cuchillo. No construyas "un delivery con IA"; construye la capa que vuelve innecesario al marketplace. Y segundo punto contrarian: **"IA para optimizar rutas" es humo a tu escala**. El valor del dispatch no está en el algoritmo, está en la densidad para batchear pedidos — PedidosYa recibe miles por hora, tú recibirás 15. La IA de rutas amplifica la densidad que ya tienes; tú no tienes ninguna. Cada punto porcentual que optimizas, el incumbente lo multiplica.

**Qué haría yo:**

1. Meses 1-6: 30-50 restaurantes en 2-3 comunas contiguas (Providencia-Ñuñoa, o Santiago Centro), CLP 150.000/mes flat, promesa medible: 100% de WhatsApp contestado + prepago + upsell.
2. Métrica de éxito: "+15% en ventas directas del local". Si la demuestras, tienes una máquina de ventas, no un pitch.
3. Integración con POS locales (Toteat y similares) para que la orden caiga directo a cocina — eso es lo que separa juguete de herramienta.
4. El endgame: poseer el canal directo y sus datos. Si algún día la densidad emerge orgánicamente, recién ahí el marketplace se reabre como opción — con una estructura de costos de ~5% contra el 25% del incumbente.

La disyuntiva real no es "¿cuánta IA uso?", es "¿ataco la comisión o la pago?".