# Inkling Small — creativity/depth_vs_superficial

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 7.78 | quality: 9.0
- latency_total: 63.659s | tokens_per_second: 45.6
- input_tokens: 147 | output_tokens: 2900

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

No te voy a dar una lista. Te voy a dar una advertencia con números.

En Santiago, la mayoría de los “delivery con IA” mueren porque confunden **optimizar rutas** (que es un problema de tráfico, no de IA) con **predecir el contexto social del reparto**. Aquí hay dos ideas que no son obvias y que dependen de la geografía de Santiago:

**1. Modelo de “fallo de edificio”, no de ruta.**
En Las Condes y Providencia, el 30-35% de los retrasos no son por el taco de Apoquindo; son por edificios sin portero, ascensores rotos o conserjes que no abren a repartidores desconocidos. En vez de usar IA para la ruta, usa IA para predecir **qué edificio tendrá problemas de acceso en los próximos 15 minutos** (basado en datos de entregas previas, clima, y hasta si es día de pago de gastos comunes). Luego asigna no al rider más cercano, sino al rider que **ya conoce ese edificio** o que tiene un perfil de comunicación que funciona con ese conserje. Estimación: en zonas de alta densidad vertical, reducir los retrasos por acceso en un 15% aumenta la retención de clientes en ~10% y evita reentregas que te cuestan ~CLP 2.500 cada una. Eso es más valioso que una ruta 8% más corta.

**2. “Micro-menu de barrio” en zonas periféricas con datos de voz local, no con tendencias nacionales.**
En Maipú, Puente Alto o La Florida, el CAC (costo de adquisición) es ~CLP 12.000, casi el doble que en Ñuñoa. No intentes competir con Rappi en menú de 50 ítems. Usa IA para detectar, en un radio de 500 metros, qué se busca localmente (por ejemplo, “sándwich de chicharrón de cerdo los viernes a las 12:30” o “empanadas de pino después de lluvia”). Activa un cocinero local —no un restaurante formal— con un menú de 2-3 productos, entregado por un rider que vive a menos de 2 km. El costo de abrir un punto mínimo es ~CLP 3-5 millones, pero si tu modelo predice la demanda hiperlocal con un error menor al 20%, reduces el inventario muerto en ~40% comparado con un menú fijo. En Santiago, donde los restaurantes de esquina ya tienen su propio WhatsApp, tu ventaja no es el menú, es **el momento exacto en que el cliente quiere algo que no está en su menú habitual**.

**El riesgo no obvio que nadie menciona:**
No es la competencia ni la privacidad. Es la **asimetría de datos que destruye la confianza con los restaurantes pequeños**. Si tu IA aprende que un restaurante de Ñuñoa vende más cuando el precio baja 10% a las 3 PM, y tú le sugieres precios dinámicos, ese dueño de “picada” no entiende el modelo; siente que lo estás explotando y se va a su propio WhatsApp o a Rappi. En Chile, el delivery de comida no es una industria de datos; es una industria de **confianza de barrio**. Si tu IA no hace que ese restaurante gane más dinero que con su propia lista de contactos, tu startup es solo un intermediario con gastos de IA.

**La opinión contrarian:**
En Santiago, **no uses IA para escalar más rápido; úsala para hacer tu startup más pequeña, más cara y más defensiva**. Deberías usar la IA principalmente para **rechazar pedidos** que sabes que te van a costar más de lo que ganás (porque el edificio tiene ascensor roto, porque es zona de lluvia súbita, porque el cliente está en La Pintana y tu modelo sabe que ahí la densidad de riders no cubre el costo). Si tu IA no protege al restaurante de esquina de San Joaquín de tu propia plataforma, entonces estás construyendo una máquina de extraer valor de gente que no te necesita. La verdadera ventaja en Santiago no es ser más inteligente; es ser **menos anónimo** que Rappi. La IA debe servir para que un repartidor y un conserje se reconozcan, no para que un algoritmo decida que ese edificio no vale la pena.