# Claude Opus 5 — integridad_idioma/jerga_tecnica_densa

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.83 | quality: 9.56
- latency_total: 27.423s | tokens_per_second: 61.0
- input_tokens: 281 | output_tokens: 1672

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un periodista que escribe para un medio digital latinoamericano.
Escribes para lectores hispanohablantes de México, Chile, Argentina, Colombia y España.
Tu trabajo es tomar material de origen y redactar en español neutro, claro y directo.

**user:**

Explica en 400-500 palabras, para un fundador sin
formación técnica, qué significa este cambio y por qué le importa:

"Speculative decoding with a 1B draft model cuts time-to-first-token by 40% on 70B
targets, but only when the acceptance rate stays above 0.7. Below that, the verification
overhead dominates and you end up slower than greedy decoding. Batch size interacts
badly: at batch 32+ the draft model contends for the same KV cache bandwidth."

No uses viñetas, escribe en párrafos.


## Respuesta completa

**El asistente que adivina lo que sigue**

Imagine que su modelo de lenguaje grande —el de 70.000 millones de parámetros, el caro— es un editor senior que escribe palabra por palabra. Cada palabra le cuesta tiempo y dinero. La técnica que está sobre la mesa, llamada *speculative decoding* (decodificación especulativa), agrega un segundo modelo mucho más pequeño y barato, de unos 1.000 millones de parámetros, que actúa como un asistente junior: se adelanta y propone varias palabras de golpe. El modelo grande no las escribe, solo las revisa de una sola pasada y decide si las acepta o las corrige. Revisar es más rápido que escribir, y de ahí sale el ahorro.

El número que promete el material de origen es atractivo: hasta 40% menos de tiempo hasta que el usuario ve la primera respuesta en pantalla. Para un producto conversacional, esa es la diferencia entre una interfaz que se siente viva y una que se siente trabada. La latencia percibida es, en la práctica, una característica del producto.

**La letra chica: la tasa de aceptación**

El ahorro depende de qué tan bueno sea el asistente junior adivinando. Esa métrica se llama tasa de aceptación: qué proporción de las palabras propuestas sobrevive a la revisión. Si supera el 0,7 —es decir, si siete de cada diez propuestas son correctas—, el sistema gana velocidad. Si cae por debajo de ese umbral, el costo de revisar y descartar se come el beneficio y el resultado es *más lento* que no haber hecho nada. No es una mejora gradual que se degrada suavemente: es un interruptor. Por encima del umbral, gana; por debajo, pierde.

Esto importa porque la tasa de aceptación no es un dato fijo del proveedor, depende de su caso de uso. Texto predecible y repetitivo —código, formularios, respuestas con estructura fija— se adivina bien. Texto creativo, dominios muy específicos o jerga interna se adivinan mal. Nadie puede decirle de antemano en qué lado del 0,7 va a caer su producto: hay que medirlo con tráfico real.

**El problema que aparece cuando el producto crece**

Hay una segunda trampa, y es la más relevante para planificar. Cuando el sistema atiende muchas conversaciones simultáneas —a partir de unas 32 en paralelo—, los dos modelos empiezan a competir por el mismo recurso escaso: el ancho de banda de memoria de la GPU. El asistente junior deja de ser gratis y empieza a estorbar. Traducido a lenguaje de negocio: la optimización que se ve espectacular en la demo, con pocos usuarios, puede desvanecerse justo cuando el producto empieza a tener tracción.

**Qué hacer con esto**

No es una decisión de comprar o no comprar, es una palanca de configuración con condiciones. Pídale a su equipo técnico tres cosas concretas: la tasa de aceptación medida con sus propios datos, la curva de latencia a distintos niveles de concurrencia, y un mecanismo que desactive la técnica automáticamente cuando esas condiciones no se cumplan. Sin eso, está comprando un 40% que existe solo en el escenario ideal.