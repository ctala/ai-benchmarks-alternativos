# Claude Opus 5 — integridad_idioma/jerga_tecnica_densa

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 7.94 | quality: 9.62
- latency_total: 20.721s | tokens_per_second: 57.6
- input_tokens: 281 | output_tokens: 1193

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

Imagina que tu modelo de inteligencia artificial es un escritor muy talentoso pero lento: cada palabra que produce le cuesta tiempo y dinero. La técnica llamada *decodificación especulativa* intenta resolver eso con una idea sencilla: poner a trabajar a un asistente rápido y modesto junto al escritor experto. El asistente —un modelo pequeño, de unos mil millones de parámetros, al que se le llama "modelo borrador"— arriesga varias palabras de golpe. Luego el modelo grande, de setenta mil millones de parámetros, revisa esa propuesta de una sola pasada y decide qué acepta y qué corrige. Cuando el asistente adivina bien, el experto avanza en bloque en vez de palabra por palabra, y el usuario ve la primera respuesta en pantalla mucho más rápido.

La cifra concreta es atractiva para cualquier producto: el tiempo hasta el primer token —es decir, lo que el usuario espera mirando el cursor antes de ver aparecer algo— cae un 40%. En términos de negocio, eso es la diferencia entre un chat que se siente ágil y uno que se siente roto. Pero hay una condición, y es la parte que conviene entender antes de prometerle nada al equipo o a un inversionista.

Esa ganancia solo existe si la tasa de aceptación se mantiene por encima de 0,7; o sea, si al menos siete de cada diez palabras que propone el asistente sobreviven la revisión del experto. Por debajo de ese umbral, el esquema se da vuelta. Revisar también cuesta: cada propuesta rechazada es trabajo tirado a la basura, y llega un punto en que el costo de verificar supera el ahorro de adivinar. El resultado es paradójico pero real: el sistema termina siendo más lento que si simplemente hubieras dejado al modelo grande escribir palabra por palabra, sin ayudante. No es una mejora gradual que se desvanece, es un interruptor que puede jugar en contra.

Hay un segundo detalle, menos obvio y más incómodo. Todo esto funciona bien cuando atiendes pocas solicitudes a la vez. En cuanto empiezas a procesar treinta y dos conversaciones simultáneas o más —lo que en la jerga se llama *batch size* o tamaño de lote—, el modelo borrador deja de ser un aliado gratuito y se convierte en un competidor. Ambos modelos necesitan leer y escribir en la misma memoria rápida de la tarjeta gráfica, la llamada caché KV, y ese canal tiene un ancho limitado. Es como dos personas intentando pasar al mismo tiempo por una puerta angosta: ninguna avanza bien.

La lectura práctica para un fundador es esta. La decodificación especulativa es una optimización excelente para una demo, para un producto con tráfico moderado o para casos donde las respuestas son predecibles y el asistente acierta seguido. Pero no es una palanca que se active y ya. Si tu plan es escalar a miles de usuarios concurrentes, el beneficio puede evaporarse o volverse negativo justo cuando más lo necesitas. Antes de incluirla en tu modelo de costos, pide dos números a tu equipo técnico: la tasa de aceptación real con tus propios datos y el comportamiento con el volumen de tráfico que esperas en seis meses. Esa conversación vale más que la cifra del 40%.