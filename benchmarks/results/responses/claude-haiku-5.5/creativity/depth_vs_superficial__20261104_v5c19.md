# Claude Haiku 5.5 — creativity/depth_vs_superficial

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 18.101s | tokens_per_second: 170.5
- input_tokens: 249 | output_tokens: 3086

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

Mi respuesta corta: **la IA no debería ser el producto de tu startup, sino una herramienta para bajar costos y retener restaurantes.** Routing y pricing ya son commodities que tienen PedidosYa, Rappi y Uber Eats con mucha más data que tú. Tu ventaja, si la tienes, estará en nichos que ellos no atienden bien. Estas son las ideas que yo exploraría, con cifras que son estimaciones gruesas y deberías validar con tus propios datos.

**Idea 1: Venderle a los restaurantes el "por qué" de sus pérdidas, no solo pedidos**
Un restaurante de Santiago típico pierde entre 5% y 10% de sus insumos en mermas, muchas veces porque prepara de más para un peak que no llega o porque no tiene visibilidad de qué platos se venden por franja horaria. Con datos de pedidos de tu plataforma (y, si te integras, del POS), un modelo de pronóstico por plato y por hora puede sugerir cuánto cocinar y qué sacar del menú a las 14:30 en un día de lluvia. Si logras reducir mermas en 2 o 3 puntos sobre un costo de insumos de 30% de las ventas, eso son entre 0,6% y 0,9% de ingresos del restaurante, pero visible en su caja. Es un argumento de venta concreto que no depende de que tu app sea la más rápida.

**Idea 2: Disputas y reembolsos como problema de visión, no de atención al cliente**
Los reclamos ("llegó fría", "faltó un ítem", "el pedido estaba mal") suelen costar entre 3% y 6% del GMV en reembolsos y créditos, según el tipo de operación. Hoy la mayoría se resuelve con reglas simples y reembolsos generosos. Un modelo que cruza la foto que sube el repartidor al entregar, el ticket original y el historial del cliente puede distinguir fraude de error legítimo. El riesgo de hacerlo mal es alto: un sistema que desconfía de los clientes destruye la conversión. Pero bien usado puede bajar esos costos a la mitad sin que nadie lo note.

**Idea 3: Un agente de pedidos por WhatsApp e Instagram para restaurantes pequeños**
Aquí va la parte más controvertida. Muchos restaurantes de barrio pagan comisiones de 20% a 30% y resienten esa dependencia. Un agente conversacional que toma pedidos por WhatsApp, cobra por link de pago (Khipu, Mercado Pago) y asigna el despacho a repartidores propios o a un tercero barato podría capturar a clientes recurrentes que hoy ya piden directo al restaurante por teléfono. Es un negocio de disintermediación, no de IA. La IA solo hace viable atender ese canal sin contratar un operador.

**Un riesgo que casi nadie menciona: la gestión algorítmica de repartidores**
En Chile, la Ley 21.431 (2022) regula a las plataformas de reparto e incluye obligaciones de transparencia sobre los criterios de asignación y evaluación, y reglas para la desconexión o desactivación de trabajadores. Si tu IA asigna pedidos, puntúa a los repartidores o decide quién se queda sin turnos, estás haciendo gestión laboral algorítmica. Si no puedes explicar por qué un repartidor fue desactivado y no tienes un proceso de reclamo, te expones a demandas y a fiscalización de la Dirección del Trabajo. Muchos fundadores modelan la productividad del repartidor como un problema técnico cuando es, en realidad, un problema legal y reputacional. Si contratas a tus repartidores o usas terceros, esto debe estar en el diseño desde el día uno.

**Mi opinión contrarian: el momento de la IA en tu startup es más tarde, no más temprano**
La mayoría de los fundadores quiere mostrar "somos una startup de IA" en el pitch. Yo creo que eso te distrae. En delivery, las ventajas las dan la densidad (muchos restaurantes y clientes en 2 o 3 comunas, por ejemplo Providencia, Ñuñoa y Las Condes), la retención de repartidores y el margen por pedido. Un modelo de routing 5% mejor vale menos que retener a un restaurante que hoy paga 25% de comisión y quiere irse. Antes de gastar en modelos, mide cuánto contribuye cada pedido después de comisiones, despacho, reembolsos y mermas. Si ese número es negativo, ningún algoritmo lo arregla.

**Si tuviera que empezar en 90 días:**
1. Elige 2 comunas y 20 a 30 restaurantes donde tengas tracción real.
2. Mide margen por pedido y reclamos por tipo, sin modelos todavía.
3. Prueba la Idea 1 con 5 restaurantes: pronóstico simple por plato y franja, medido contra mermas reales.
4. Si el margen mejora, construye el canal de la Idea 3 para los restaurantes que ya te piden comisión menor.

¿Cuántos pedidos al mes tienes hoy y en qué comunas? Con eso puedo afinar las estimaciones.