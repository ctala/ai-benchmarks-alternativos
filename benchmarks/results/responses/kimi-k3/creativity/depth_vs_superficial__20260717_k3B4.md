# Kimi K3 — creativity/depth_vs_superficial

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.86 | quality: 10.0
- latency_total: 148.038s | tokens_per_second: 36.7
- input_tokens: 244 | output_tokens: 5432
- judge_score: 5 | justificación: La respuesta proporciona ideas específicas y profundas, con ejemplos concretos y consideraciones legales, todo presentado de manera clara y relevante para un emprendedor en el contexto de Santiago.

## Respuesta completa

La pregunta correcta no es "¿cómo uso IA?" sino "¿qué sabe mi sistema que PedidosYa no puede saber?" Con eso en mente:

**Idea 1: Pedidos por notas de voz de WhatsApp, afinados al español chileno**

Hay un segmento enorme que las apps abandonaron: adultos 55+, gente con baja alfabetización digital, y comunas donde nadie quiere bajar Rappi pero todos mandan audios de WhatsApp (penetración en Chile: ~90-95% de los usuarios de internet). El truco técnico: los modelos de transcripción estándar fallan feo con el chileno — "¿cómo estái?", la 's' aspirada, "po", "al tiro". Fine-tunear sobre dialecto chileno real es un foso defensible que un competidor no copia en un fin de semana.

La matemática ilustrativa: un restaurante que pierde 15 pedidos diarios por WhatsApp ocupado × ticket de $12.000 CLP × comisión del 10% (vs. el 20-30% que cobran las apps) = ~$540.000 CLP/mes de ingreso para ti por restaurante. Con 50 restaurantes en una sola comuna (La Florida, Puente Alto — esta última tiene +600 mil habitantes y está mal atendida en oferta gastronómica), estás en ~$27M CLP/mes antes de escalar. Sin app store, sin UI, sin call center.

**Idea 2: Predicción de tiempo de cocina, no de rutas**

Todos optimizan el despacho; casi nadie modela lo que pasa *dentro* del restaurante. El repartidor espera en promedio 8-15 minutos por retiro. Y aquí Chile es único: la Ley de Repartidores (21.431) garantiza piso de pago por tiempo de espera/conexión, seguros y cotizaciones. Cada minuto de espera mal predicho es ahora un costo regulado directo — algo que no enfrentan igual en mercados vecinos.

Un modelo que prediga por plato y por hora cuánto demora la cocina (usando velocidad de pedidos entrantes, composición de la orden, historial) te permite despachar al repartidor "justo a tiempo". Cortar 5 minutos de espera en 2.000 pedidos/día son ~167 horas-repartidor diarias: a ~$3.500/hora efectiva, eso supera los US$200.000 anuales. Bonus: la comida llega más caliente y bajan los reembolsos (típicamente 1-3% del GMV).

**Extra rápido: arbitraje de días de lluvia.** En Santiago llueve pocas decenas de días al año, concentrados en invierno. Cuando llueve, la demanda salta 30-50% justo cuando la oferta de repartidores colapsa. Como la lluvia es rara, los modelos genéricos la subponderan. Incentivos dinámicos lanzados 2-3 horas *antes* de la tormenta pronosticada capturan las horas más rentables del año.

**El riesgo que nadie menciona:** tu IA puede convertirse en evidencia legal en tu contra. Si tu modelo asigna, prioriza o penaliza repartidores, un inspector de la Dirección del Trabajo o un tribunal puede argumentar que ejerces subordinación algorítmica — el núcleo del test de relación laboral. Chile ya legisló una vez sobre esto; la próxima pelea regulatoria será sobre gestión algorítmica. Diseña la IA de repartidores como *asesora* (sugiere, no castiga), documenta la lógica de decisiones, y separa los modelos de eficiencia de cualquier consecuencia disciplinaria.

**Mi opinión contrarian:** no construyas un marketplace, y olvida el routing — OSRM y Google te dan el 90% gratis. El delivery no es un problema de logística; es un problema de predicción de humanos: cocineros que se atrasan y clientes que mienten. Tu moat no es el modelo (cualquiera llama la API de OpenAI); son 12 meses de datos propietarios sobre cuánto demora *realmente* la cocina del sushi del barrio un viernes lluvioso a las 13:30, y qué pedidos huelen a fraude. La jugada ganadora en Santiago es venderle armas a los restaurantes ya agregados por las apps, y capturar al cliente que las apps dieron por perdido porque atenderlo con operación humana-era cara. La IA es precisamente lo que hace rentable a ese cliente otra vez.

Si tuviera que elegir una sola cosa para validar en 30 días: pararme en 20 restaurantes de una comuna y contar cuántos pedidos de WhatsApp pierden por día. Ese número te dice si Idea 1 es negocio o fantasía.