# Inkling Small — creativity/depth_vs_superficial

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 7.96 | quality: 9.0
- latency_total: 39.255s | tokens_per_second: 133.0
- input_tokens: 147 | output_tokens: 5222

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

No uses IA para “optimizar rutas”. En Santiago, eso es un error de novato: Rappi, Uber Eats y PedidosYa ya tienen modelos de red con millones de eventos diarios en el valle central y la cordillera. Tú no vas a ganar optimizando 3 minutos de viaje por Ñuñoa o Las Condes con un algoritmo genérico. Si haces eso, te conviertes en una startup de “mejor delivery” que muere en 8 meses quemando capital en subsidios de descuento.

Aquí va lo que sí deberías hacer, con profundidad de Santiago:

**Primera idea no obvia: IA de “Capacidad de Cocina Real” (PCCR), no de demanda.**  
En Santiago, el 70 % de los restaurantes que entregan a domicilio son pequeños (1-3 locales, sin ERP, sin datos de producción). El problema no es que no sepan cuánto piden; es que no saben cuánto pueden *producir* en una ventana de 15 minutos sin que el plato se degrade. Tu IA no debe predecir “cuántos pedidos habrá hoy”, sino “cuántos platos de *ceviche de reineta* pueden salir de esa cocina a las 8:15 pm sin que el cocinero se sature y se retrasen todos”. Integra datos que nadie usa: tiempos de espera reportados por repartidores (el “wait time” oculto), mensajes de WhatsApp al cocinero (si dicen “ya estoy colapsado”), reservas en Instagram/Resy, y señales locales como clima o si hay evento en el Estadio Nacional o Movistar Arena. El modelo predice la capacidad real de producción por ventana horaria y recomienda al restaurante: *“Cierra la promoción de ese plato a las 8:30 pm; tienes 7 pedidos en cola y tu horno solo puede hacer 12 platos en 30 minutos”*. 

Número concreto: Un restaurante en Providencia o Barrio Italia recibe ~30 pedidos/día. Si el 15 % se retrasan y cada retraso genera una cancelación del 12 % de los pedidos posteriores en esa zona (porque los clientes empiezan a cancelar cuando ven que el pedido está “en cocina” 40 minutos), estás perdiendo ~5-6 pedidos efectivos por día. A un ticket promedio de $12.000-$15.000 CLP, eso son ~$60.000 CLP/día de volumen perdido. Si tu IA reduce los retrasos de 15 % a 4 %, recuperas ~$40.000 CLP/día, o ~$1,2M CLP/mes por restaurante. Pero lo clave: no cobras al cliente; cobras al restaurante un “fee de eficiencia” o participas del incremento de volumen. Eso es un modelo B2B que Rappi no tiene.

**Segunda idea: IA de “Abandono Predictivo por Repartidor” (APR) o zonas de fricción logística.**  
En Santiago, los repartidores no son agentes homogéneos; tienen “zonas de rechazo” por seguridad, tráfico, o dificultad física (subir sin ascensor a departamentos en Ñuñoa, calles estrechas de Bellavista, o el cruce del río Mapocho con tráfico saturado en Costanera Norte). Los gigantes usan IA para asignar pedidos, pero ignoran el “costo psicológico” del repartidor. Tu modelo debe predecir no demanda, sino *probabilidad de rechazo o demora crítica de un repartidor asignado a una comuna específica*, dado el clima, día de la semana y eventos locales. Ejemplo: hay concierto en Estadio Nacional a las 9 pm; un repartidor que vive en Maipú tiene 70 % de probabilidad de rechazar o retrasar críticamente un pedido en Ñuñoa a las 9:30 porque el tráfico en Vespucio y Autopista Central se congela. La IA entonces asigna a un repartidor local o activa una “micro-dark kitchen” local para evitar el cruce. 

Número: En una startup con ~500 pedidos/día, un 8 % de rechazos por falta de repartidor es 40 pedidos perdidos. Cada pedido perdido cuesta al restaurante ~$3.000-$4.000 CLP en insumos + reputación. Si reduces rechazos a 2 %, salvas 30 pedidos/día. A $3.500 CLP de costo de oportunidad, son $105.000 CLP/día, o ~$3,1M CLP/mes. Además, el repartidor no pierde tiempo de espera (el “double wait” que mata la rentabilidad: llega, espera 8 minutos porque el restaurante está saturado, luego cruza la ciudad), lo que aumenta su tasa de entregas por hora.

**El riesgo que nadie menciona:** No es que tu IA falle; es que funcione *demasiado bien* y te exponga a una responsabilidad algorítmica que no existe en los manuales de startup. Si usas geolocalización precisa de repartidores y clientes para predecir rechazos o asignar pedidos, estás haciendo “perfilado automatizado” de datos sensibles (ubicación en tiempo real, patrones de movimiento por comunas como Lo Barnechea vs. La Pintana, comportamiento de repartidores). Chile tiene la Ley 19.628 (y su fortalecimiento reciente con la Ley de Protección de Datos Personales y la influencia del GDPR chileno). Si tu algoritmo segmenta por zona socioeconómica implícitamente —por ejemplo, asignando precios dinámicos más altos o tiempos de entrega más lentos a zonas periféricas— puedes enfrentar una demanda de competencia desleal o discriminación ante el SERNAC, o una sanción de la Autoridad de Protección de Datos. Peor: si tu modelo usa datos de WhatsApp o redes sociales de restaurantes sin consentimiento explícito, los restaurantes pueden demandarte por uso de datos internos. El riesgo oculto es que tu startup puede ser forzada judicialmente a revelar su modelo (como pasó con algoritmos de Uber en Europa) o a pagar indemnizaciones a repartidores que son “gestionados por IA” sin transparencia contractual.

**La opinión contrarian:** No uses IA para hacer tu delivery más rápido. Usa IA para hacerlo *intencionalmente más lento y más caro* para ciertos segmentos, y *más eficiente* para otros, porque competir con Rappi en velocidad en Santiago es un hoyo sin fondo: ellos subsidian cada pedido para mantener la red. Tu IA debe servir para escapar de la guerra de precios, no para ganarla. Identifica los pedidos de “lujo” o alta cocina en Lo Barnechea o Las Condes, y ofrece “delivery de 90 minutos con control de temperatura y acompañamiento”, mientras usas la IA para agrupar pedidos de zonas periféricas (San Bernardo, Puente Alto, Maipú) en “ventanas de 2 horas” que permiten usar bicicletas en lugar de motos, reduciendo seguros y combustible. Si tu startup intenta ser “el Rappi de las comunas”, mueres. Si usa IA para ser “un servicio segmentado que Rappi no puede replicar porque su red es demasiado grande y homogénea”, ganas.

En resumen: no optimices rutas. Optimiza la *fricción entre cocina y repartidor* con datos locales de Santiago, y protege tu modelo legalmente antes de escalar.