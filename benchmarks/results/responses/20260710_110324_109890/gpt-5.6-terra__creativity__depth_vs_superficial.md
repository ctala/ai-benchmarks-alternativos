# GPT-5.6 Terra — creativity/depth_vs_superficial

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 37.995s | tokens_per_second: 83.2
- input_tokens: 139 | output_tokens: 3160
- judge_score: 5 | justificación: La respuesta proporciona un análisis profundo y específico, con ideas innovadoras y un enfoque práctico, evitando consejos genéricos y ofreciendo soluciones concretas y estimaciones numéricas.

## Respuesta completa

Mi recomendación no es “poner IA” como capa de marketing. En delivery, la IA vale si reduce una de estas tres fugas: **cancelaciones, minutos improductivos o pérdida de recompra**. Todo lo demás —chatbots, imágenes de comida generadas, recomendaciones genéricas— suele ser distracción.

Mi tesis contrarian: **tu mejor modelo probablemente debería ayudarte a rechazar o retrasar pedidos, no a captar más pedidos**. En delivery, crecer GMV con promesas poco realistas destruye margen y confianza.

## El primer producto de IA que construiría: un “motor de promesa honesta”

No es un predictor de ETA bonito. Es un sistema que decide, antes de que el cliente pague:

- ¿Este restaurante realmente podrá aceptar y preparar este SKU ahora?
- ¿Qué probabilidad hay de que llegue dentro del rango prometido?
- ¿Conviene mostrarlo, extender la promesa, quitar ciertos platos o sugerir una alternativa?

La diferencia importa. La mayoría estima “tiempo esperado”; tú deberías estimar una **distribución de riesgo**.

Ejemplo: una hamburguesería puede tener promedio de preparación de 18 minutos, pero entre 20:30 y 21:30 los viernes su p90 puede ser 42 minutos. Si prometes “30–40 min”, no es que tu ETA esté levemente mal: estás vendiendo una experiencia que tiene alta probabilidad de terminar en reclamo, cancelación o devolución.

El modelo debería usar variables poco obvias:

- restaurante + hora + día + evento local;
- plato o combinación de platos, no sólo restaurante;
- cantidad de modificadores (“sin cebolla”, “extra queso”) como proxy de complejidad;
- tiempo desde que el restaurante abrió;
- cantidad de órdenes ya aceptadas pero aún no listas;
- patrón histórico de aceptación del local;
- disponibilidad real de repartidores en un radio corto;
- lluvia, congestión y comuna;
- si el pedido va a un edificio con acceso lento.

### La acción no es sólo cambiar la ETA

El sistema puede hacer una de cuatro cosas:

1. mostrar un rango más largo pero creíble;
2. bajar temporalmente el ranking del restaurante;
3. ocultar sólo los ítems problemáticos —por ejemplo, sushi o pizzas con alta carga de preparación—;
4. ofrecer al cliente una alternativa equivalente con descuento pequeño.

Esto puede parecer que reduce conversión, y a veces la reduce. Pero puede aumentar margen y recompra.

Supongamos una operación de 3.000 pedidos diarios. Si reduces cancelaciones evitables en sólo 1,5 puntos porcentuales, son **45 pedidos salvados al día**. Si una cancelación cuesta, entre subsidio, soporte, reembolso y comida perdida, unos CLP $3.000–$5.000 de contribución, estás hablando de **CLP $135.000–$225.000 diarios**, o aproximadamente **$4–$6,7 millones al mes**, antes de contar el efecto en retención.

La métrica no debe ser “ETA más precisa”. Debe ser:

> margen de contribución por pedido mostrado, incluyendo cancelación, compensación, soporte y probabilidad de segunda compra.

## Segunda idea menos obvia: construir inteligencia del “último 80 metros”, no del último kilómetro

En Santiago, muchas demoras no ocurren en la ruta. Ocurren al llegar:

- torre sin número visible;
- conserjería que llama al residente;
- ascensor lento;
- acceso por calle distinta;
- edificio con dos entradas;
- oficina dentro de un centro empresarial;
- cliente que no dejó departamento ni instrucciones.

Eso no se resuelve con optimización de rutas. Se resuelve con un **grafo operativo de edificios y puntos de entrega**.

Para cada ubicación, no guardaría notas libres tipo “portero pesado” —eso es un riesgo legal y reputacional—, sino variables estructuradas y agregadas:

- precisión del pin;
- tiempo típico desde llegada a entrega;
- tasa de llamadas al cliente;
- probabilidad de que requiera conserjería;
- mejor punto de encuentro;
- franja horaria con mayor demora;
- entrada recomendada;
- si conviene pedir instrucciones antes de despachar.

La IA puede detectar que un edificio específico agrega, por ejemplo, 4 minutos de espera promedio y alta varianza. Entonces, antes de asignar repartidor, el sistema pide al cliente una instrucción concreta: “¿Torre A o B? ¿Departamento? ¿Se entrega en conserjería?” No un chatbot genérico: un formulario mínimo, activado sólo cuando el riesgo lo justifica.

Si reduces apenas **1,5 minutos improductivos** en 3.000 entregas diarias, son 4.500 minutos, o **75 horas de capacidad diaria**. Con un costo marginal de repartidor de CLP $80–$120 por minuto, el impacto bruto puede ser del orden de **$360.000–$540.000 diarios**. La cifra exacta depende de tu modelo laboral, pero el orden de magnitud justifica el experimento.

Además, esto mejora algo que los dashboards tradicionales no ven: la experiencia del repartidor. Menos llamadas, menos esperas, menos conflictos en edificios.

## El riesgo no obvio: tus datos pueden enseñarle al modelo exactamente lo contrario de la realidad

Si entrenas con pedidos completados, el modelo verá principalmente casos exitosos. Los pedidos cancelados —que muchas veces eran los más lentos o problemáticos— quedan truncados.

Ejemplo: un restaurante promete 20 minutos, se atrasa 50, el cliente cancela al minuto 35. Si sólo registras entregas completadas, tu modelo puede concluir que ese restaurante “entrega en 25 minutos” porque los peores casos desaparecieron del dataset.

Eso genera un ciclo peligroso:

1. subestimas su demora;
2. le mandas más pedidos;
3. empeora la cocina;
4. aumentan cancelaciones;
5. el modelo sigue sin aprender bien porque los pedidos fallidos no se observan como entregas.

Necesitas registrar eventos completos: cotización, pago, aceptación, inicio de preparación, listo para retiro, asignación, llegada, retiro, llegada al destino, entrega, cancelación y motivo. Técnicamente, esto exige modelos de tiempo a evento o supervivencia, no sólo regresión simple de ETA.

Y hay un segundo riesgo: si automatizas ranking según desempeño histórico, podrías terminar castigando sistemáticamente restaurantes o comunas con peor infraestructura, menor densidad de repartidores o edificios más complejos. Es una forma de **redlining algorítmico**: rentable a corto plazo, pero mala para expansión, reputación y regulación. Pon límites explícitos: no dejar que el algoritmo simplemente “abandone” zonas; distinguir entre riesgo que puedes corregir y riesgo que sólo estás evitando.

## Lo que haría en 90 días

No construiría un LLM propio ni un motor de routing.

1. **Semanas 1–3:** instrumentar datos operativos. Sin timestamps confiables por estado, no hay IA útil.
2. **Semanas 4–6:** crear un modelo simple de riesgo de cancelación/retraso por restaurante-hora-SKU, usando reglas y modelos tabulares antes que deep learning.
3. **Semanas 7–10:** probar en 20–40 restaurantes y 2–3 comunas. A un grupo le muestras ETA tradicional; a otro, promesa calibrada + throttling de menú/ranking.
4. **Semanas 11–12:** evaluar contra un grupo control con métricas económicas: margen por pedido mostrado, cancelación, reembolso, tiempo de soporte, retención a 30 días y horas productivas de repartidor.

No optimices “más pedidos” primero. Optimiza **pedidos que debieron existir y que podían cumplirse bien**.

La opinión controversial es esta: en una startup de delivery pequeña, la IA no debe usarse para parecer más tecnológica que Rappi, Uber Eats o PedidosYa. Debe usarse para ser más disciplinada que ellos en una zona, una categoría o un tipo de cliente. Tu ventaja no será un modelo sofisticado; será tener mejores señales operativas y atreverte a decir “no” a pedidos que parecen buenos en GMV pero destruyen confianza y margen.