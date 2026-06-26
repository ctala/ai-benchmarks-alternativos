# Kimi K2.7 Code — creativity/depth_vs_superficial

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.83 | quality: 9.09
- latency_total: 153.459s | tokens_per_second: 29.9
- input_tokens: 167 | output_tokens: 4581
- judge_score: 4.6 | justificación: 

## Respuesta completa

Primero, olvida el *pitch* habitual. En Santiago no vas a ganarle a Rappi, PedidosYa o Uber Eats poniendo un chatbot con ChatGPT ni “optimizando rutas”. Esos son costos de entrada, no diferenciadores. La pregunta útil es: **¿en qué puntos del negocio de delivery la varianza te mata más que la competencia?** Porque el delivery en Santiago es bajo margen, alta volatilidad y densidad desigual: tienes picos violentos, lluvias inesperadas, marchas, partidos de Colo-Colo y una geografía donde viajar de Las Condes a Puente Alto no es lo mismo que de Providencia a Ñuñoa. La IA que realmente importa es la que reduce varianza, no la que impresiona a inversores.

Aquí van dos ideas que casi nadie está haciendo bien:

### 1. Modelo de “fragilidad de red”: rechazar o retrasar pedidos antes de que contagien el sistema

En lugar de predecir solo el ETA, predice cuánto daño hará un pedido aceptado al resto de la red. En Santiago, un solo pedido mal ubicado —por ejemplo, un sushi en el Costanera Center a las 13:00 con una moto que ya lleva dos pedidos— puede retrasar 5 a 7 pedidos subsecuentes en 8-12 minutos. Eso es una “fragilidad de red”.

La idea es entrenar un modelo que, antes de confirmar un pedido, estime la probabilidad de que ese pedido genere un efecto cascada: cocina saturada, moto atascada en Apoquindo, cliente que cancela, etc. Si el riesgo supera un umbral, el sistema no rechaza necesariamente, pero puede: (a) ofrecer un descuento por recoger 20 minutos después, (b) redirigir al usuario a un restaurant equivalente menos congestionado, o (c) cobrar un “precio de congestión” dinámico. Esto es distinto a la optimización de rutas: es **control de admisión basado en estado de red**.

Números concretos para Santiago: si una plataforma mueve 5.000 pedidos diarios y el 8 % son “pedidos cascada”, evitarlos o reasignarlos inteligentemente puede bajar el tiempo promedio de entrega de ~38 a ~30 minutos, reducir cancelaciones en un 20 % y aumentar la utilización real de los repartidores en un 15-20 %. Con un costo promedio de repartidor de CLP 3.000 por pedido y una comisión neta del 20 %, eso puede significar unos CLP 400-600 adicionales de margen por pedido en horas pico. El problema: necesitas datos de aceptación de restaurantes, GPS de motos en tiempo real y una política clara con los comercios, porque decirle “no” a un restaurante es políticamente difícil.

### 2. Menú generativo para “dark kitchens” de rescate alimentario

En vez de recomendar platos de restaurantes a clientes, usa IA para **diseñar cada día qué cocinar en pequeñas cocinas fantasma** según qué sobra barato en La Vega, Lo Valledor o centrales mayoristas. El modelo recibe precios diarios de insumos sobrantes, predice demanda por comuna y genera un menú reducido —por ejemplo, “bowl de pollo con arroz y verduras del día” o “cazuela familiar económica”— que se puede producir y entregar a menos de CLP 6.000.

El twist no es la cocina fantasma, que ya existe; es usar IA para **emparejar oferta de desperdicio con demanda local en tiempo real**. En Santiago, un local de 25 m² en Puente Alto, La Pintana o Recoleta puede producir combos a un costo de insumo de CLP 2.000-2.500 y venderlos a CLP 5.500-6.500. Si el modelo mejora la venta efectiva en un 25 % y reduce el desperdicio en un 15 %, elevas el margen bruto de ~35 % a ~45 %. Con 200 combos diarios, eso es una diferencia de CLP 1,5-2 millones al mes por cocina. Además, te abre una base de clientes distinta a la de los delivery tradicionales: familias que buscan precio, no conveniencia premium.

---

### Un riesgo que casi nadie menciona: la “optimización distributiva” puede volver tu servicio inexistente en comunas periféricas

Santiago no es homogéneo. Si dejas que un algoritmo estilo “maximizar utilidad” decida dónde operar, naturalmente favorecerá comunas de alto ticket y alta densidad: Providencia, Las Condes, Ñuñoa, La Reina. Las comunas del sur y el poniente —Puente Alto, La Pintana, San Bernardo, El Bosque— tienen menos poder adquisitivo, distancias más largas y peor señalización, por lo que el modelo comenzará a “recomendar” no atenderlas: tiempos de entrega más altos, menos restaurantes disponibles, cupones dirigidos solo al norte. Terminas creando **desiertos de delivery algorítmicos**, aunque ahí viva la mayoría de la población metropolitana.

En Santiago, donde ya existe una tensión fuerte entre repartidores y plataformas, esto no es solo un problema de equidad: es un riesgo regulatorio y reputacional. Un municipio o el gobierno regional podría obligarte a servir ciertas comunas, o los repartidores —que muchas veces viven en esas mismas zonas periféricas— podrían boicotearte. La IA tiene que tener explícitamente una métrica de **equidad geográfica**, no solo de rentabilidad.

---

### Opinión contrarian: en Santiago, la IA más valiosa es la que te ayuda a decir “no”

La mayoría de los emprendedores quieren usar IA para crecer: más pedidos, más usuarios, más conversión. Yo diría lo opuesto. En el delivery santiaguino, el crecimiento sin control es una trampa. Márgenes bajos + tráfico impredecible + comisiones agresivas = cada pedido mal tomado te quema plata real.

Por eso, mi opinión controversial es: **la mejor aplicación de IA en tu startup no es generar más demanda, sino rechazar o reconfigurar la demanda mala**. Un modelo que te diga “este pedido probablemente te perderá CLP 1.200”, “esta zona no tiene densidad suficiente hoy” o “este restaurante no cumplirá el tiempo prometido” es más valioso que cualquier chatbot o recomendador. La IA debe encargarse de **achicar tu superficie de fracaso**, no de impresionar con features. En un mercado saturado como Santiago, ser el más confiable en un territorio pequeño y bien definido es mejor que ser el más grande e inconsistente.

En resumen: no empieces con IA por la IA. Empieza midiendo dónde la volatilidad te está sangrando. Luego construye modelos que reduzcan esa varianza, incluso si eso significa negar pedidos. Eso sí es ventaja competitiva.