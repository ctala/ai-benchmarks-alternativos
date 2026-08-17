# Claude Opus 4.8 (suscripción) — creativity/depth_vs_superficial

- model_id: `claude-opus-4-8`
- success: True  | final: 7.07 | quality: 9.92
- latency_total: 66.73s | tokens_per_second: 57.7
- input_tokens: 2026 | output_tokens: 3847
- judge_score: 5.0 | justificación: 

## Respuesta completa

No necesito herramientas para esto. Te respondo directo, como si fuera tu socio técnico mirando la realidad del delivery en Santiago.

---

**Primero, la pregunta correcta no es "¿cómo uso IA?" sino "¿dónde la IA me da una ventaja que PedidosYa/Rappi/Uber Eats NO tienen ya?"**

Y la respuesta incómoda es: en el *core* del delivery (ruteo, matching, demanda) la IA premia escala y datos. Los incumbentes tienen 5+ años de data de Santiago comuna por comuna. Tu modelo de forecasting el día 1 vale cero — cold start brutal. Donde sí podés ganar es en los bordes que a ellos no les conviene atender. Ahí van mis ideas.

---

### Idea 1 — Toma de pedidos por nota de voz de WhatsApp en español chileno

El chileno manda **audios**, no escribe. Y miles de picadas / locales de barrio NO están en las apps grandes porque odian la comisión del 20-30%. Un agente que reciba la nota de voz ("oye, mándame dos completos italianos sin mayo, una pichanga pa' compartir y un mote con huesillo") la transcriba, entienda los **modismos y agregados** (palta, "sin ají", "agrandado") y arme el pedido estructurado + cobre por transferencia/MercadoPago.

- Costo real por pedido: transcripción + LLM chico ≈ **USD 0.003–0.01**. Versus la comisión de 25% sobre un ticket de ~$12.000 CLP = **$3.000 CLP (~USD 3.2)** que cobra PedidosYa. La diferencia es absurda.
- Lo no-obvio: el cuello de botella no es el modelo, es el **español chileno hablado con ruido de cocina**. Whisper genérico se equivoca con modismos. Ahí está tu foso: fine-tuning / glosario por rubro.

### Idea 2 — Detección de abuso de reembolsos y "gaming" de repartidores

Nadie habla de esto pero se come el margen vivo. El fraude de reembolsos ("llegó frío", "faltó un producto", GPS spoofeado, repartidor que marca entregado sin entregar) puede ser **2-5% del GMV** — y en un negocio con margen neto de un dígito bajo, eso es la diferencia entre quebrar o no.

- Un modelo que cruce patrones (cliente que reclama el 30% de sus pedidos, repartidor cuyo tiempo de "en local" es estadísticamente imposible, fotos de entrega duplicadas) y escale solo los casos sospechosos a revisión humana.
- Concreto: si tu GMV mensual es $50M CLP y recuperás aunque sea 2 puntos de fraude, son **$1M CLP/mes** que cae directo a la última línea. Eso paga el equipo.

---

### Riesgo no-obvio: la **Ley 21.431 de plataformas digitales**

Todos te van a advertir del riesgo de "depender de un solo proveedor de API". El que no te van a mencionar: en Chile rige desde 2022 la ley que regula a los trabajadores de apps de reparto (cotizaciones, jornada, clasificación dependiente/independiente). Si construís un sistema de IA que **asigna y optimiza turnos de repartidores de forma muy agresiva**, podés estar configurando una relación de subordinación y dependencia *de facto* — y generás contingencia laboral y previsional retroactiva. La eficiencia del algoritmo puede ser exactamente lo que te demanda la Dirección del Trabajo. Diseñá el scheduling con asesoría laboral *antes*, no después.

---

### Opinión contrarian

**No construyas otra app de delivery. Construí el copiloto de IA para los restaurantes que odian a las apps de delivery.**

El delivery de comida es un negocio de capital y logística, no de IA — competir en CAC contra Delivery Hero (dueño de PedidosYa) es suicidio financiero. Pero hay miles de restaurantes pagando 25-30% de comisión y operando con Excel y un cuaderno. Véndeles la capa de IA: toma de pedidos por WhatsApp, predicción de merma de insumos, generación automática de promos en horarios muertos (las 16:00 de un martes), y reconciliación de **boletas electrónicas del SII** (dolor 100% chileno que ningún LLM gringo resuelve out-of-the-box).

Pasás de pelear por GMV en un mercado de márgenes negativos, a un **SaaS B2B** con churn bajo y un foso real (la data y la integración SII). El delivery es el caballo de Troya, no el negocio.

---

Si querés, armo los números unitarios de cualquiera de estas en una mini-hoja (costo IA por pedido vs comisión ahorrada, breakeven de restaurantes) o te ayudo a stestear qué modelo barato maneja mejor el español chileno hablado — justo tengo el benchmark a mano para eso.