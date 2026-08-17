# Claude Fable 5 — creativity/depth_vs_superficial

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.92 | quality: 8.5
- latency_total: 35.371s | tokens_per_second: 57.9
- input_tokens: 247 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta proporciona ideas específicas y profundas, como modelar el tiempo de cocina y predecir el desbalance oferta-demanda por lluvia, con ejemplos concretos y estimaciones, abordando riesgos no obvios y ofreciendo una perspectiva contraria sobre el uso de IA.

## Respuesta completa

Primero, una advertencia honesta: la pregunta "¿cómo uso IA?" es la pregunta equivocada. La pregunta correcta es "¿dónde está mi varianza operacional?" — porque ahí es donde la IA paga. Dicho eso, vamos a lo concreto.

## Idea 1: Modela el tiempo de cocina, no el tiempo de ruta

Todo el mundo obsesiona con optimizar rutas, pero en delivery urbano de comida, entre el 40% y 60% de la varianza del tiempo total de entrega viene de la cocina, no de la calle. Un sushi en viernes a las 21:00 puede tardar 35 minutos en salir; el mismo sushi un martes a las 15:00, 12 minutos.

Si tu repartidor llega 15 minutos antes de que el pedido esté listo, quemaste CLP $1.500–2.500 de su tiempo (o su paciencia, si le pagas por entrega). Si llega tarde, la comida se enfría y tu NPS se desploma. Un modelo de predicción de prep-time por restaurante × plato × hora × día te permite despachar al repartidor justo a tiempo. DoorDash construyó esto y es de sus ventajas más defendibles. Con 50 restaurantes y 3 meses de datos ya tienes señal suficiente para un modelo simple (gradient boosting, nada exótico). El impacto realista: reducir el tiempo muerto del repartidor 20–30%, lo que en la práctica es como contratar un 15% más de flota gratis.

## Idea 2: Predice el desbalance oferta-demanda por lluvia, no la demanda a secas

Santiago tiene una particularidad: cuando llueve (esos 15–25 días al año concentrados en junio-agosto), la demanda de delivery sube 25–40%... y la oferta de repartidores en moto y bici cae simultáneamente porque nadie quiere pedalear bajo el agua. Es un doble golpe que revienta los tiempos de entrega justo cuando tienes más pedidos.

El modelo no-obvio no es predecir demanda: es predecir el **gap** entre demanda y supply de repartidores con 24–48 horas de anticipación, y usar eso para activar incent