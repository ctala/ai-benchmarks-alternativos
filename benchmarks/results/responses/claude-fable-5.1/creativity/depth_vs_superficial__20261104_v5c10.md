# Claude Fable 5.1 — creativity/depth_vs_superficial

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.09 | quality: 9.0
- latency_total: 82.761s | tokens_per_second: 61.8
- input_tokens: 249 | output_tokens: 5114

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

Primero una pregunta que cambia toda la respuesta: ¿vas a competir con Rappi/PedidosYa/Uber Eats de frente, o vas a atacar un segmento que ellos ignoran? Porque si es lo primero, la IA no te va a salvar y te explico por qué al final. Asumo lo segundo.

**Idea 1: El cuello de botella en Santiago no es la ruta, es la cocina**

Todo el mundo habla de optimizar rutas, pero mira dónde se va el tiempo en un pedido típico: 15-20 minutos de preparación en el restaurante, 5-10 minutos del rider esperando en la puerta, 10-15 minutos de viaje. El rider pasa a veces un cuarto de su turno parado afuera de un local esperando que salga la bolsa. Ningún algoritmo de ruteo arregla eso.

Lo que sí lo arregla: un modelo de predicción de demanda **a nivel de ítem y por local**, con 30-45 minutos de anticipación, que le diga a la cocina "a las 20:15 te van a entrar 6 pedidos de pollo al jugo y 4 de pastel de choclo, empieza ahora". Esto es factible con pocos meses de datos porque la demanda de almuerzo/cena en una comuna es muy regular (día de semana, hora, clima, si hay partido de la Roja).

El número: si bajas el tiempo de ciclo de ~35 a ~29 minutos, el rider pasa de ~2 a ~2.3 entregas por hora. Eso es ~15% menos costo de rider por pedido, y en un negocio donde el margen por orden es de cientos de pesos, 15% es la diferencia entre perder y empatar. Nadie hace esto bien porque requiere integración con la operación del restaurante, no solo con la app.

**Idea 2: WhatsApp es el verdadero competidor, no las apps**

Miles de picadas, cocinerías, sushis de barrio y rotiserías en Santiago no están en ninguna plataforma. Reciben pedidos por WhatsApp, los anotan en un cuaderno, y mandan al sobrino en moto. No se suben a Rappi porque el 25-30% de comisión los mata (su margen es 10-15%) y porque el onboarding es engorroso.

Un agente de IA en WhatsApp que tome el pedido en lenguaje natural ("hola, me manda 2 completos italianos y una bebida a Irarrázaval 1234, pago transferencia"), lo estructure, confirme dirección, proponga sustitución si algo se acabó, y lo despache a tu red de riders, convierte ese universo informal en tu catálogo. Súmale visión computacional para digitalizar el menú desde una foto del pizarrón en 10 minutos.

¿Por qué esto es defendible? Porque los datos de Rappi sobre Las Condes no le sirven para nada en una cocinería de San Miguel. Es el único lugar donde una startup chica tiene ventaja de datos sobre los incumbentes: el territorio que ellos no mapearon.

**Idea 3 (bonus corto): el día de lluvia**

Santiago tiene 10-15 días de lluvia real al año y en esos días pasan dos cosas simultáneas: la demanda sube brutalmente y la oferta de riders en moto colapsa. Un modelo que combine pronóstico meteorológico + histórico y preasigne bonos por zona 3 horas antes (no cuando ya se cayó el servicio) te da una ventaja táctica que los grandes, con sus procesos centralizados en Bogotá o Berlín, reaccionan tarde.

**El riesgo que nadie te va a mencionar: tu algoritmo es evidencia judicial**

La Ley 21.431 (2022) regula el trabajo en plataformas digitales. Dos cosas concretas:

1. Estás obligado a informar a los riders los criterios del algoritmo de asignación de pedidos. Si tu modelo es una caja negra, tienes un problema de cumplimiento desde el día uno.
2. Si tus riders son "independientes", la ley dice que no pueden ser sancionados por rechazar pedidos. Y aquí está la trampa: cualquier modelo de asignación medianamente inteligente va a aprender solo que los riders que rechazan mucho son menos confiables, y los va a deprioritizar. Eso es una sanción implícita. Un abogado laboral usa los logs de tu modelo para demostrar subordinación y dependencia, y de repente tienes 300 trabajadores dependientes con cotizaciones, vacaciones e indemnizaciones retroactivas.

Agrega la Ley 21.719 de datos personales (vigente desde diciembre 2026, multas hasta 20.000 UTM, unos $1.300 millones), que exige explicabilidad en decisiones automatizadas que afecten a personas. Diseña el sistema con eso en mente ahora, no cuando te llegue la notificación.

Y un riesgo secundario del mismo tipo: tu modelo de demanda va a aprender que Puente Alto y La Pintana tienen peor conversión y más incidentes, y va a dejar de asignarles riders. Eso se llama discriminación algorítmica por territorio y en Chile es una bomba reputacional.

**La opinión incómoda: la IA no arregla la economía unitaria del delivery**

El ticket promedio de comida en Santiago anda en $12.000-15.000. El cliente tolera pagar $2.000-3.000 de despacho. Pagarle al rider cuesta $2.500-3.500 por entrega. La matemática es negativa antes de pagar soporte, marketing, fraude y tu sueldo. Rappi perdió plata durante años con los mejores ingenieros de la región.

Toda la IA del mundo te mejora eficiencia en un 10-20%. No cambia el signo. Lo único que cambia el signo es **densidad**: muchos pedidos en pocas cuadras para poder agrupar 2-3 entregas por viaje. Y la densidad se consigue con foco geográfico brutal (una comuna, no "Santiago") y con una propuesta que el restaurante prefiera (comisión que no lo mate), no con un modelo mejor.

Así que mi consejo real: no construyas "una app de delivery con IA". Construye la capa de operación para restaurantes que hoy viven en WhatsApp, en 2-3 comunas contiguas, y usa IA donde genuinamente reemplaza costo (toma de pedidos, soporte, digitalización de menús) y donde los incumbentes no tienen datos. Si eso funciona, la IA de ruteo la compras después, no la inventas.