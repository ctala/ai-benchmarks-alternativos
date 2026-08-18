# Claude Opus 5 Fast — creativity/depth_vs_superficial

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.5 | quality: 9.5
- latency_total: 43.925s | tokens_per_second: 186.5
- input_tokens: 247 | output_tokens: 8192

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

Antes de responder: "startup de delivery" puede significar tres negocios completamente distintos (marketplace propio, dark kitchen, o software para que restaurantes vendan por canal propio tipo Justo/Fudo). Voy a asumir marketplace/operación logística, pero si es otro, la mitad de esto cambia.

Y una advertencia: los números de abajo son estimaciones de orden de magnitud para forzar el razonamiento, no verdades. Valídalos con tu data.

---

## Primero: dónde está la plata realmente

Un pedido típico en Santiago: ticket CLP 13.000–16.000, comisión al restaurante 18–28%, fee al cliente CLP 1.200–3.000, costo del repartidor CLP 1.800–3.200. Tu contribución por pedido oscila entre **CLP -300 y +1.200**. Eso significa que la IA solo importa si mueve una de cuatro palancas: pedidos por hora por repartidor, tasa de pedidos que se van a la basura (refund/cancelación), conversión del carrito, o costo de operación humana (soporte, onboarding de locales).

Todo lo demás es decorado para el pitch deck. Con esa vara:

---

## Idea 1: El modelo que importa no es de rutas, es de tiempo de preparación

En una ciudad densa como Santiago centro-oriente, la optimización de rutas te da 3–5%. La **espera del repartidor en el local** te da 15–20%.

El repartidor llega y espera 6–9 minutos porque el sushi todavía no sale. Ese tiempo es puro costo. Con la Ley 21.431, además, tienes un piso legal por hora de trabajo efectivo (ingreso mínimo proporcional +20%, del orden de CLP 3.200–3.400/hora al día de hoy), así que el tiempo muerto es cada vez menos "problema del repartidor" y cada vez más problema tuyo.

Lo no obvio: casi todos predicen tiempo de preparación como un promedio por restaurante. Lo que sirve es predecirlo **por plato, por hora del día, condicionado a la cola actual de la cocina**. Un pad thai a las 21:15 de un viernes con 7 comandas adelante no es el mismo plato que a las 15:00 de un martes.

Eso requiere integrarte al POS (Toteat, Fudo, Bsale, Ubiquo) para ver el estado real de la cocina. **Ese es el verdadero trabajo: la integración, no el modelo.** El modelo es un gradient boosting aburrido de 200 líneas.

Matemática rápida: si el ciclo del repartidor pasa de 27 a 23 minutos, subes de ~2,2 a ~2,6 entregas/hora (+18%). Eso baja el costo logístico unos **CLP 200–250 por pedido**. Con 1.000 pedidos/día son ~CLP 7 millones al mes. Con 5.000/día, ~CLP 35 millones. Es probablemente el único proyecto de IA que se paga solo en el primer trimestre.

---

## Idea 2: Santiago tiene un problema de geocodificación y de topografía que nadie está modelando

Dos cosas específicas de esta ciudad:

**a) La dirección no es el punto de entrega.** "Av. Providencia 1234, depto 502" tiene un punto de entrega real que es la portería, no la coordenada de Google. En condominios de Chicureo, La Dehesa o Peñalolén alto, o en villas con pasajes y blocks en La Pintana o Puente Alto, Google te deja a 300 metros del destino. Solución: no compres geocoding, **apréndelo**. Toma los GPS traces de tus repartidores, clusteriza los puntos donde efectivamente se detienen más de 90 segundos por cada string de dirección, y construye tu propio índice de "delivery points". A los 50.000 pedidos ya tienes algo que Google no tiene. Bonus: un clasificador binario de "este edificio requiere entrega en portería" te permite ajustar el ETA y dejar de notificar al cliente que "el repartidor llegó" cuando en realidad está peleando con el conserje.

**b) Santiago tiene 400 metros de desnivel.** Maipú está a ~500 msnm, Lo Barnechea a ~900. Un trayecto en bici o e-bike hacia el oriente es 30–40% más lento que el mismo trayecto hacia el poniente, y ningún ETA basado en distancia plana lo captura. Meterle **delta de elevación con signo** como feature a tu modelo de ETA es una línea de código que probablemente reduce tu error abs