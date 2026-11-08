# Kimi K3.1 Pro — creativity/depth_vs_superficial

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 7.68 | quality: 10.0
- latency_total: 418.207s | tokens_per_second: 22.9
- input_tokens: 244 | output_tokens: 9585

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

No empezaría por “delivery + chatbot” ni por otro estimador de rutas. **Usaría IA para reducir la varianza operacional y para atreverme a rechazar demanda que destruye margen.** En delivery, un pedido promedio puede parecer rentable mientras una cola de pedidos desastrosos —cocina atrasada, acceso imposible, reembolso, soporte— se come toda la contribución.

Asumo que operas como marketplace y controlas al menos parte del despacho. Los números siguientes son supuestos para dimensionar oportunidades, no benchmarks de Santiago.

## 1. Un “semáforo de cocina” por plato, no un recomendador de comida

La mayoría intenta predecir cuánto tardará un restaurante. Yo iría un nivel más abajo: **estimar el p90 de preparación de cada pedido según su mezcla de platos y la cola actual de cocina, y usarlo para modular qué se vende.**

A las 13:15, por ejemplo, no necesariamente conviene cerrar un restaurante completo. Puede bastar con:

- Ocultar temporalmente el plato que agrega 18 minutos y tiene alta varianza.
- Mantener disponibles los platos que salen en 8 minutos y pueden prepararse en lote.
- Reducir el radio de entrega solo para ese restaurante.
- Ofrecer un descuento en el menú ejecutivo que la cocina puede absorber, en vez de subsidiar indiscriminadamente todo el catálogo.

El modelo también debería calcular la **contribución esperada antes de aceptar**:

> comisión + fee de entrega − reparto esperado − pagos − promoción − soporte y reembolsos esperados.

Así, la IA no solo predice demoras: decide qué demanda conviene aceptar. Eso es mucho más valioso que recomendar sushi porque el usuario suele pedir sushi.

**El detalle que determina si esto funciona:** necesitas una marca temporal confiable de “pedido listo”. Si usas “repartidor retiró” como sustituto, mezclarás preparación, llegada del repartidor y decisiones de despacho. Empezaría con un botón simple para el restaurante y auditorías manuales; sin esa etiqueta, no compraría ningún modelo sofisticado.

**Tamaño del premio:** supón 1.500 pedidos diarios. Si en 60% de ellos reduces 2 minutos de espera en restaurante:

- 1.500 × 60% × 2 min = **30 horas de reparto liberadas al día**.
- A un costo ilustrativo de CLP 4.000/hora: **CLP 120.000 diarios**, unos **CLP 3,6 millones mensuales**.
- Equivale a aproximadamente **CLP 80 por pedido** sobre 45.000 pedidos mensuales.

Eso es capacidad liberada, no ahorro automático: solo se convierte en caja si reduces horas pagadas o logras completar más entregas con la misma flota.

## 2. Construir una memoria del “último tramo” de cada edificio

En sectores con torres y condominios de Providencia, Las Condes, Ñuñoa o Santiago Centro, el trayecto puede terminar en el mapa y la entrega seguir atascada: entrada equivocada, conserjería que no recibe, citófono sin respuesta, torre confundida o instrucciones que solo conoce un repartidor experimentado.

Aquí sí usaría un LLM, pero **no para conversar con clientes**: lo usaría para convertir notas desordenadas y audios posteriores a la entrega en conocimiento estructurado:

- Acceso correcto y política de conserjería.
- Si el repartidor debe esperar al cliente o puede dejar el pedido.
- Tiempo observado entre “llegué a la dirección” y “entregué”.
- Instrucción breve validada por repartidores, sin almacenar teléfonos ni códigos de acceso.

Con eso obtienes dos activos: una instrucción operacional por edificio y una distribución real del tiempo de entrega en ese lugar. Tu promesa puede distinguir entre dos direcciones separadas por 200 metros pero con cinco minutos de diferencia en el acceso.

Supongamos nuevamente 1.500 pedidos diarios, 35% hacia edificios o condominios, y que logras recuperar 2 minutos en solo la mitad de ellos. Son **8,75 horas diarias**, aproximadamente **CLP 1 millón mensual** bajo el mismo costo horario. El beneficio mayor probablemente no sea ese ahorro, sino reducir los casos extremos de 15–20 minutos y evitar que el conocimiento desaparezca cada vez que rota un repartidor. Tampoco sumaría este beneficio al anterior sin medirlo: ambos se solapan.

## El riesgo no obvio: tu modelo aprenderá de datos censurados por tus propias decisiones

Si solo entrenas con pedidos entregados, excluyes muchos de los peores casos: cancelados, abandonados o nunca aceptados. Luego, cuando el semáforo empieza a restringir restaurantes o zonas, cambia nuevamente los datos que recoges. El modelo puede terminar aprendiendo su propia profecía y mostrando mejoras ficticias.

Además, puedes reducir el error promedio de promesa de 8 a 6 minutos y, simultáneamente, empeorar el retraso p95 de 25 a 40 minutos. El dashboard se ve mejor mientras empeora exactamente la experiencia que genera reclamos y abandono.

Por eso mantendría registros de pedidos rechazados y cancelados, una fracción de tráfico con la política anterior y métricas de **p90/p95, contribución por pedido y contactos de soporte**, no solamente precisión promedio del modelo.

## Mi opinión contrarian

**“Un Rappi o PedidosYa con mejor IA” no es una estrategia defendible para una startup.** La IA probablemente fortalece a los incumbentes: pueden copiar la funcionalidad y tienen más densidad, datos y capacidad de subsidiar errores. Un chatbot o un modelo entrenado con tus primeros miles de pedidos no constituye una ventaja competitiva.

Yo haría algo menos atractivo para un pitch: dominar un caso estrecho —por ejemplo, almuerzos en El Golf–Providencia—, limitar radio y horarios, y usar IA inicialmente para **decir que no**: no vender cierto plato en cierta franja, no prometer 30 minutos cuando el p90 dice 50 y no aceptar una cesta cuya contribución esperada sea negativa. Menos GMV puede significar un mejor negocio.

Durante las primeras dos semanas instrumentaría eventos; durante las siguientes cuatro ejecutaría los modelos en modo sombra, sin cambiar decisiones; después haría una prueba por restaurante-día o bloques de 30–60 minutos. Un A/B por pedido contamina el experimento porque los pedidos comparten cocina y repartidores. Escalaría solo si, por ejemplo, el p90 de espera cae al menos 20%, no aumentan cancelaciones ni soporte, y la contribución mejora alrededor de CLP 100 por pedido. Si no, detendría el proyecto.

**La IA no resolverá tu falta de densidad. Puede evitar que compres crecimiento con pedidos que nunca debiste aceptar.**