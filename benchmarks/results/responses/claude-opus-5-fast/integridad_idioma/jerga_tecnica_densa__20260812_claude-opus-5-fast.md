# Claude Opus 5 Fast — integridad_idioma/jerga_tecnica_densa

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 7.71 | quality: 9.34
- latency_total: 11.41s | tokens_per_second: 135.4
- input_tokens: 281 | output_tokens: 1545

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

## El truco de los dos modelos: por qué tu chatbot puede sentirse el doble de rápido (y cuándo deja de funcionar)

Imagina que tienes a un experto muy caro y muy lento escribiendo respuestas palabra por palabra. Cada palabra cuesta tiempo y dinero. Ahora imagina que le pones al lado a un asistente junior, rapidísimo y barato, que se adelanta y escribe cinco palabras de un tirón adivinando lo que diría el experto. El experto ya no escribe: solo revisa el bloque completo de una sola pasada y dice "sí, yo habría escrito exactamente eso" o "no, a partir de la tercera palabra te equivocaste". Revisar cinco palabras juntas es mucho más rápido que generarlas una por una. Eso es, en esencia, el *speculative decoding* o decodificación especulativa: un modelo pequeño (de mil millones de parámetros, el "borrador") propone y un modelo grande (de setenta mil millones, el que realmente te importa) verifica.

El resultado que reporta el material de origen es contundente: el usuario empieza a ver texto en pantalla un 40% más rápido. Para un producto conversacional eso no es un detalle de ingeniería, es percepción de calidad. La diferencia entre esperar tres segundos y esperar menos de dos es la diferencia entre una herramienta que se siente viva y una que se siente rota.

Pero hay una condición, y aquí está lo que un fundador debe entender antes de prometerle nada a su equipo o a sus inversionistas. El truco solo funciona si el asistente junior acierta la mayoría de las veces. La métrica se llama tasa de aceptación y el umbral es 0,7: siete de cada diez palabras propuestas tienen que sobrevivir la revisión del modelo grande. Por debajo de ese número, el sistema pasa más tiempo descartando trabajo inútil que generando texto, y terminas más lento que si nunca hubieras metido al modelo pequeño. Es el equivalente a contratar a un asistente que se equivoca tanto que corregirlo cuesta más que hacerlo tú mismo.

Esa tasa de aceptación no es un número fijo que te venga en la caja: depende de tu dominio. Si el modelo pequeño fue entrenado con texto general y tu producto responde consultas legales, médicas o de código muy específico, las predicciones fallarán más y la ganancia se evapora. Por eso hay que medirla con tu tráfico real, no con el demo.

El segundo límite es el que más suele sorprender. Cuando el sistema atiende a muchos usuarios al mismo tiempo —a partir de treinta y dos solicitudes simultáneas—, los dos modelos empiezan a pelearse por el mismo recurso escaso: el ancho de banda de memoria donde se guarda el contexto de cada conversación. La optimización que brillaba con un usuario se degrada justo cuando el producto empieza a crecer.

La lección práctica es incómoda pero valiosa: esta técnica es una ganancia real en escenarios de baja concurrencia y dominio acotado, y una promesa frágil bajo carga. Antes de construir tu propuesta de valor sobre la velocidad, exige a tu equipo dos números: la tasa de aceptación con datos reales y el comportamiento a tu volumen proyectado, no al de hoy.