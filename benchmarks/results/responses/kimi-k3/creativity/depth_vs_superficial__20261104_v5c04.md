# Kimi K3 — creativity/depth_vs_superficial

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.83 | quality: 10.0
- latency_total: 213.798s | tokens_per_second: 34.7
- input_tokens: 244 | output_tokens: 7427

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

La pregunta correcta no es "¿cómo uso IA?" sino "¿dónde la IA me da algo que PedidosYa no pueda copiar en seis meses?". Ellos llevan ~10 años acumulando datos de pedidos en Santiago; tú tienes cero. Cualquier jugada de IA que dependa de datos históricos de pedidos la pierdes antes de partir. Regla de filtro: solo construye IA donde los datos del incumbente no le sirvan de nada.

Con ese filtro, dos ideas:

**1. El canal WhatsApp con voz chilena, para el segmento que las apps abandonaron**

Miles de cocinerías y picadas en Santiago (La Vega, Puente Alto, Maipú, las periferias densas) operan por WhatsApp con cuaderno y lápiz porque no aguantan el 25-30% de comisión de las plataformas. Más del 90% de los chilenos con smartphone usa WhatsApp. El producto: un número donde el cliente manda un audio ("oye, dame dos italianos y una bebida, al tiro po"), un modelo de voz estructura el pedido, cobra con link de Webpay/Mercado Pago y despacha de un pool de repartidores. Cobras 8-12% en vez de 27%.

La matemática para el restaurante: una cocinería con 20 pedidos/día a $10.000 CLP de ticket mueve ~$6M/mes. Pasar de 27% a 10% le devuelve ~$1.000.000 CLP mensuales — el arriendo de la cocina en una comuna media. Ese argumento vende solo.

Y el foso es curioso: el español chileno rompe los modelos de voz globales (s aspirada, velocidad, "po/cachai/weá"). OpenAI y Google no van a ajustar un modelo para un mercado de 19 millones de personas. Si logras tasa de error baja en voz chilena, tienes algo que ni PedidosYa tiene.

**2. Vende inteligencia de demanda antes de tener demanda**

Tu problema real es el cold-start: no tienes datos porque no tienes pedidos, no tienes pedidos porque no tienes restaurantes. Solución: combina tu poca señal con señales públicas (tendencias de búsqueda, reseñas, actividad por comuna) y conviértela en producto B2B.

- **Mapa de hambre insatisfecha**: qué busca la gente en Ñuñoa a las 21:00 que no existe. Los grupos gastronómicos y dark kitchens pagan por saber dónde abrir y qué cocinar.
- **Alertas con gatillos chilenos**: lluvia (Santiago concentra sus lluvias en mayo-agosto; los días de lluvia la demanda sube 30-40% y las cocinas colapsan), fin de mes vs. semana de sueldo (Chile paga mensual; el ticket cae en la última semana y repunta tras el pago), clásicos Colo-Colo/U. Avisar 3-4 horas antes: "prepara 25% más, refuerza un cocinero". Las plataformas grandes se guardan esta señal; compartirla te convierte en aliado del restaurante, no en su verdugo.

Bonus barato: los repartidores esperando afuera son un sensor de saturación de cocina sin integrar nada con el restaurante. Pings GPS agrupados + tiempo de espera = ETA honesto y redespacho anticipado.

**El riesgo que nadie menciona**

Cuando compartes pronósticos con restaurantes, el error tiene factura. Si le dices a una sushi shop "prepárate +30% mañana" y el modelo falla, el restaurante se come la merma —el costo de alimento es ~30% de su P&L; una mala noche le borra la semana— y nunca más te cree. Y los dueños de restaurantes hablan entre ellos: gremios, grupos de WhatsApp por comuna. Tu negocio B2B no muere por churn, muere por rumor. La IA cara al consumidor falla en silencio; la IA cara al restaurante falla con boleta.

(Riesgos secundarios: la dependencia de Meta —la API de WhatsApp Business ya cambió precios antes y quemó startups— y que una transcripción mala de "sin maní" no es un bug, es una demanda y una funa.)

**La opinión contraria**

Mi respuesta honesta: quizás no deberías construir una app de delivery en Santiago en 2025. Entrar al marketplace de consumo contra PedidosYa, Rappi y Uber Eats —con densidad logística ya instalada y capacidad de subsidiarte hasta la muerte— es quemar decenas de millones de dólares. La empresa interesante es la del armero del bando contrario: venderle la infraestructura (pedidos por WhatsApp, inteligencia de demanda, despacho) a los miles de restaurantes que quieren escapar del 27%. No eres una startup de delivery que usa IA; eres una empresa de IA cuyo mercado inicial es el movimiento anti-plataforma. Y cuando el mercado se consolide, las plataformas pasan de competidores a clientes.

Un último dato: la Ley de Plataformas (21.431) subió el piso de costos del modelo gig. Cumplirla es caro, pero una vez cumplida es muralla contra competidores informales. Automatizar ese compliance con IA no es sexy — pero es barrera de entrada.