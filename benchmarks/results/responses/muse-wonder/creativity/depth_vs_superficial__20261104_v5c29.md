# Muse Wonder — creativity/depth_vs_superficial

- model_id: `meta/muse-wonder`
- success: True  | final: 8.05 | quality: 10.0
- latency_total: 46.885s | tokens_per_second: 71.6
- input_tokens: 140 | output_tokens: 3359

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

Si tu pitch es "delivery + IA en Santiago", mi opinión contrarian es esta: **estás muerto antes de partir, y la IA va a acelerar tu muerte si la pones frente al cliente.**

Rappi, Uber Eats y PedidosYa no te ganan por tener mejor algoritmo de rutas. Te ganan porque pueden perder $2.000 por pedido durante años. Tú no. En Santiago el ticket promedio anda en $13.500 CLP, el restaurante te puede pagar 20% de comisión ($2.700), y un repartidor te cuesta $2.800-$3.500 por viaje si no llevas más de 2 pedidos a la vez. O sea, partes perdiendo plata antes de pagar soporte, pasarela de pago (2,9% + IVA) y tu sueldo.

La ruta no es tu problema. Optimizarla te ahorra 2-3 minutos. Tu problema real es la varianza: una cocina dice "15 minutos" y se demora 9 un martes y 28 un viernes a las 20:30. Esa desviación te genera reclamos, reembolsos y recompra cero.

Por eso yo no construiría una app B2C. Haría IA invisible, aburrida y defensible, en dos lugares donde los gigantes son malos:

### 1. No predigas tráfico. Predice cocinas y direcciones chilenas sucias

Este es el dataset que nadie tiene y que un LLM de OpenAI no te resuelve.

En Santiago entre un 7% y un 11% de los pedidos fallan o se demoran brutalmente no por tráfico, sino por direcciones como: *"Los Militares 5890 dpto 1204 torre B, entrar por el costado, timbre malo"*, pasajes en Puente Alto sin numeración clara, o condominios en Ñuñoa con tres accesos distintos.

Un modelo —ni siquiera necesita ser generativo, un XGBoost bien hecho basta— entrenado con TUS datos de: tiempo real de preparación por plato (no por restaurante), hora, día de pago, clima y carga de cocina, te permite hacer algo que Rappi no hace porque su incentivo es mentir: **prometer 54 minutos cuando son 54 minutos.**

Suena contraintuitivo, pero prometer más y cumplir reduce reembolsos de un ~6% a un ~2,5%. En 10.000 pedidos mensuales de $13.500, pasar de 9% a 3% de entregas problemáticas son 600 pedidos salvados: más de $8 millones en venta que no se devuelve, sin contar el repartidor que no hizo el viaje dos veces.

Ese histórico —"la cocina X se demora 22 min con lomo saltado un viernes de quincena, pero 11 min con ensaladas un martes"— en 6 meses vale más que cualquier chatbot. Es tu único moat posible.

Y ojo con la quincena chilena: la demanda no es plana. Sube 30-40% entre el 30 y el 5, se desploma la cuarta semana. Súmale lluvia en Santiago (pocos días, pero esos días la demanda sube ~50% y la oferta de riders cae 30%) o un partido de Colo-Colo vs la U, y cualquier modelo gringo entrenado sin contexto local colapsa.

### 2. Ataca el pedido grupal de oficina por WhatsApp, no el antojo individual

El pedido individual ya está perdido. El pedido grupal es un infierno que nadie resolvió: 12 personas en una oficina en El Golf o Ciudad Empresarial, una pide sin cebolla, otro es celíaco, pagan separados, alguien transfiere tarde, y la secretaria termina haciendo una planilla.

Ahí sí un agente por WhatsApp con notas de voz tiene sentido. No para "conversar", sino para resolver coordinación: *"Mándanos lo de siempre, pero hoy somos 9, sin la Vale que está de vacaciones, y divide en 3 pagos"*.

Eso no lo puedes copiar en una app tradicional sin fricción brutal. Si logras que ese grupo repita 2 veces por semana, cambias la economía: no es 1 pedido de $13.500, son 10 almuerzos en un mismo edificio, un solo viaje, ticket de $85.000. El costo del rider pasa de representar 22% a 3,5%. Recién ahí el negocio respira.

Costo estimado: transcribir + procesar ese pedido con un LLM te sale $90-$180 CLP. Ridículo comparado con un CAC en Meta Ads en Santiago, que para delivery fácilmente te cuesta $8.000-$15.000 por primer cliente que nunca vuelve.

Tu métrica no es descargas. Es: ¿ese grupo vuelve en 14 días sin descuento? Si la repetición no supera el 35-40%, no tienes negocio, tienes una promoción.

### El riesgo que nadie te va a mencionar: los alérgenos y la nueva ley de datos

Si tu IA toma pedidos por voz y se le escapa un "sin maní", un "sin gluten" o transcribe mal una alergia, no es un bug. Es una urgencia médica, SERNAC, y potencialmente responsabilidad penal. Los LLMs alucinan justo en los detalles que importan. Necesitas confirmación humana estructurada para cualquier restricción alimentaria, siempre. Eso mata parte del margen si lo haces mal.

Y segundo: Chile ya aprobó la nueva Ley de Protección de Datos (21.719). Entra en vigencia en diciembre de 2026 y crea una Agencia con facultades para multar fuerte. Geolocalizar riders todo el día, guardar audios de WhatsApp, perfilar qué come cada empleado y dónde vive, ya no es "data para entrenar el modelo". Es tratamiento de datos sensibles. Si además tu modelo de riesgo aprende solo, va a terminar haciendo *redlining* por comuna: más fraude asumido en La Pintana, menos en Lo Barnechea, tiempos peores para unos que para otros. Eso, con el proyecto de ley de IA que se discute en Chile siguiendo el modelo europeo, te puede caer encima como discriminación algorítmica antes de que tengas product-market fit.

### Qué haría yo en las próximas 3 semanas

No programaría nada.

Ir a Ñuñoa/Providencia, conseguir 15 restaurantes chicos que odien a Rappi (no es difícil, pagan 25-30% de comisión) y 5 oficinas/clientes grupales. Operar el "agente de IA" a mano por WhatsApp, tú detrás haciendo de Wizard of Oz, y medir solo dos cosas: tiempo real de cocina por plato y tasa de repetición del grupo.

Si después de 300 pedidos no tienes datos que un competidor no pueda comprar en Google Maps, y no tienes grupos que repitan sin cupón, no construyas IA. No tienes una startup de IA. Tienes un delivery caro con un chatbot encima.

La oportunidad en Santiago no es ser más inteligente que Rappi. Es ser el dueño de un nicho denso, repetitivo y feo de operar, donde la IA trabaja en silencio para que no pierdas plata.