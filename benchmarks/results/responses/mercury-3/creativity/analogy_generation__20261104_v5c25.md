# Mercury 3 — creativity/analogy_generation

- model_id: `inception/mercury-3`
- success: True  | final: 7.8 | quality: 8.0
- latency_total: 5.202s | tokens_per_second: 329.5
- input_tokens: 122 | output_tokens: 1714

## Entrada exacta (lo que recibió el modelo)

**user:**

Crea una analogia ORIGINAL y memorable para explicar cada concepto a un emprendedor no-tecnico.
Las analogias deben ser sorprendentes, no las tipicas.
NO uses: "es como un cerebro", "es como una autopista", "es como una biblioteca".

1. Como funciona un modelo de lenguaje (LLM)
2. Que es una API
3. Que es el fine-tuning de un modelo
4. Que es un rate limit
5. Que es el prompt engineering

Para cada uno: concepto + analogia en 2-3 oraciones.


## Respuesta completa

**1. Cómo funciona un modelo de lenguaje (LLM)**  
Es como un crítico gastronómico que ha leído millones de reseñas, pero nunca ha probado un plato. Sabe qué palabras suelen aparecer juntas y puede generar menús convincentes, pero no sabe si el resultado sabe bien. Por eso a veces inventa combinaciones que suenan perfectas pero son absurdas.

**2. Qué es una API**  
Imagina que contratas a un electricista para que encienda las luces de tu oficina. No necesitas saber cómo llega la electricidad desde la central ni qué cables hay dentro de la pared: solo usas el interruptor. Una API es ese interruptor: un acuerdo estándar para pedir un servicio sin tener que entender ni tocar la infraestructura interna del proveedor.

**3. Qué es el fine-tuning de un modelo**  
Es como tomar a un actor de reparto que domina muchos acentos y meterlo en un set donde solo habla con acento argentino y usa jerga de startups. No aprende a actuar desde cero, pero ajusta su actuación a tu guion y a tu público específico. El resultado es un modelo que sigue siendo general, pero que ahora suena como si hubiera trabajado en tu industria toda la vida.

**4. Qué es un rate limit**  
Piensa en un cajero automático que solo permite diez retiros por hora. Si intentas sacar dinero cincuenta veces seguidas, no es que el banco esté enfadado contigo: simplemente protege sus sistemas y a los demás clientes. Un rate limit funciona igual: la API te dice cuántas peticiones puedes hacer en un tiempo determinado para que no colapses el servicio.

**5. Qué es el prompt engineering**  
Es como programar una lavadora: no puedes cambiar la máquina, pero eliges el ciclo, la temperatura y el centrifugado para obtener la ropa que necesitas. Si solo dices “lava esto”, obtendrás un resultado genérico; si especificas el programa, la duración y las instrucciones, el resultado será exactamente el que querías. El prompt es el panel de control: no cambias el motor, pero decides cómo debe trabajar.