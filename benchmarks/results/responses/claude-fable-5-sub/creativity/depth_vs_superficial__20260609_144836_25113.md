# Claude Fable 5 (suscripción) — creativity/depth_vs_superficial

- model_id: `claude-fable-5`
- success: True  | final: 6.49 | quality: 8.94
- latency_total: 61.442s | tokens_per_second: 62.8
- input_tokens: 2 | output_tokens: 3858

## Respuesta completa

Primero lo incómodo: en delivery de comida, la IA no te va a diferenciar frente al consumidor. Tu moat en este negocio es densidad (restaurantes + repartidores + pedidos por km²), no inteligencia. Rappi y PedidosYa tienen equipos de ML de 100+ personas y años de data que tú no vas a alcanzar. Entonces la pregunta correcta no es "cómo uso IA", es "dónde la IA me baja costos fijos para sobrevivir más tiempo que mi caja". Ahí van las apuestas concretas:

**1. Mata la app. Vende por WhatsApp con un agente LLM.**

Chile tiene >90% de penetración de WhatsApp. Conseguir que alguien instale una app de delivery cuesta $4-8 USD por install, y solo ~20-25% de esos installs hacen un primer pedido. Estás pagando $20-30 USD por cliente activo antes de tu primer peso de margen.

Un agente conversacional que toma el pedido completo por WhatsApp (menú, modificaciones, dirección, link de pago vía Fintoc/Mercado Pago) te cuesta menos de $0.01 USD por conversación con un modelo tipo Gemini Flash o GPT mini. El pedido entra estructurado a tu sistema igual que desde una app. Eliminas la fricción del install, que es donde muere el 75% de tu funnel. Las cadenas grandes no pueden hacer esto bien porque su operación está casada con la app; tú no tienes ese legacy.

**2. Modela la mentira de los tiempos de preparación.**

El secreto sucio del delivery: los restaurantes mienten sistemáticamente sobre cuánto demoran. Dicen 15 minutos, demoran 28, y tu repartidor pasa 30-40% de su turno esperando parado afuera de una cocina. Cada minuto de espera son ~$0.05-0.08 USD de costo de repartidor quemado.

Con apenas 2-3 meses de data propia (plato × restaurante × hora × día) puedes entrenar un modelo simple — ni siquiera necesitas deep learning, un gradient boosting basta — que prediga el tiempo *real* y despache al repartidor más tarde. Con 300 pedidos/día y 5 minutos recuperados por pedido, son ~$2,500-3,500 USD/mes en eficiencia de flota. Eso en delivery es la diferencia entre margen positivo y negativo por pedido.

Bonus rápido: 8-12% de los pedidos generan un ticket de soporte ("falta un item", "llegó frío"). Un humano cuesta $1-2 USD por ticket. Un LLM con acceso a la foto del pedido y el historial del cliente resuelve 60-70% solo. Hazlo antes de contratar tu primera persona de soporte, no después.

**El riesgo que nadie te va a mencionar: la regulación chilena te aplica DOBLE.**

Uno: la Ley 21.431 (plataformas digitales, vigente desde 2022) te obliga a transparentar a los repartidores cómo funciona el algoritmo que les asigna pedidos. Si usas IA para dispatch, tienes obligaciones legales de transparencia algorítmica desde el día uno — no es opcional y la Dirección del Trabajo ya ha fiscalizado plataformas.

Dos, y más urgente: la nueva ley de protección de datos (21.719) entra en vigencia en **diciembre de 2026** — en seis meses. Multas de hasta 20,000 UTM (~$1.4M USD) para infracciones gravísimas. Si entrenas modelos con datos de clientes o perfilas comportamiento de compra sin base de consentimiento clara, estás construyendo un pasivo legal. Diseña el consentimiento ahora; migrar después es 10x más caro.

**Mi opinión contrarian:** a tu escala, usar IA para "optimización logística" es una trampa. La optimización de rutas y batching con ML necesita densidad de data que no vas a tener hasta los miles de pedidos diarios — antes de eso, una heurística decente más un humano despachando le gana al modelo, y vas a quemar 4-6 meses de ingeniería en algo que mueve 2%. La IA en una startup de delivery 2026 no es para ser más inteligente que Rappi: es para operar con 3 personas lo que a ellos les cuesta 30. Esa es la única ventaja real que te da.

Si tuviera que elegir una sola cosa: el agente de WhatsApp. Ataca CAC, que es lo que mata a las startups de delivery — no la logística.