# Seed 2.0 Code — creativity/analogy_generation

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.86 | quality: 8.0
- latency_total: 107.165s | tokens_per_second: 71.0
- input_tokens: 159 | output_tokens: 7608

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

### 1. Concepto: Modelo de Lenguaje (LLM)
Herramienta de inteligencia artificial entrenada con millones de textos de todo tipo (conversaciones, artículos, contratos) que aprende los patrones de cómo se combinan palabras y tonos para responder, generar o resumir contenido. No "entiende" el significado profundo de lo que dice, solo los patrones estadísticos del lenguaje que observó en sus datos de entrenamiento.
**Analogía**: Imagina que tenes una franquicia de hamburguesas y contratás a un ayudante que pasó 5 años escuchando TODAS las conversaciones, negociaciones y respuestas de la gerente matriz con franquiciados, proveedores y clientes. No sabe de contabilidad ni de la receta secreta de la hamburguesa, pero sabe exactamente qué combinación de frases, tonos y ejemplos usar para cualquier pregunta que le plantees, basado en los patrones que observó en esas conversaciones.

---

### 2. Concepto: API (Interfaz de Programación de Aplicaciones)
Conjunto de reglas estandarizadas que permiten que dos softwares o herramientas se comuniquen entre sí sin que el usuario toque su funcionamiento interno. Solo se pueden pedir o enviar datos según las opciones predefinidas por el proveedor.
**Analogía**: Imagina que tenes una cafetería y trabajas con un proveedor de café tostado especializado que creó una ficha de pedido exclusiva y estandarizada para sus clientes. No necesitas ir a la tostaduría, hablar con el tostador ni explicar detalles técnicos del grano: solo llenas la ficha con opciones predefinidas (tipo de grano, tostado, cantidad, horario de entrega) y el proveedor envía el pedido sin más trámite. Esa ficha es la API: el medio de comunicación estandarizado que conecta tu negocio sin tocar sus procesos internos.

---

### 3. Concepto: Fine-Tuning de un modelo
Proceso de ajustar un modelo de inteligencia artificial ya entrenado con datos generales (como un LLM que sabe hablar de todo) con datos EXCLUSIVOS de tu negocio (tus conversaciones con clientes, tus productos, tus reglas, tu tono). No se entrena un modelo desde cero, sino se afina uno ya listo para adaptarlo a tus necesidades.
**Analogía**: Imagina que tenes un local de tortas personalizadas para eventos y contratás a un pastelero que ya sabe hacer tortas generales (entrenado con recetas de todos los tipos y tonos de atención generales). No tenés que enseñarle a mezclar harina ni hornear desde cero: solo le das todas tus recetas exclusivas, tus reglas de pedidos (ej: no tortas sin gluten sin aviso de 48hs), tus ejemplos de tortas que vendés y tu tono de atención a clientes, para que ajuste su trabajo exclusivamente a tu local. Esa adaptación específica es el fine-tuning.

---

### 4. Concepto: Rate Limit
Límite de solicitudes (pedidos de datos, consultas, acciones) que puedes hacer a un servicio de software (como una API o un modelo de IA) en un tiempo determinado (ej: 100 consultas por minuto). Lo establece el proveedor para evitar que su servicio se colapse por demasiada demanda simultánea.
**Analogía**: Imagina que tenes un local de alquiler de bicicletas en un parque y tenés un acuerdo exclusivo con un taller de reparaciones rápidas cercano. El dueño del taller te dice: “No puedo atender más de 5 pedidos de reparación por hora, porque tengo solo un mecánico y si vienen más, no puedo atender a nadie bien, ni a vos ni a otros clientes”. Ese límite de 5 pedidos por hora es el rate limit: el tope de solicitudes que el proveedor establece para mantener su servicio funcionando sin colapsos.

---

### 5. Concepto: Prompt Engineering
Arte y técnica de formular consultas (llamadas "prompts") claras, específicas, con contexto, reglas y ejemplos para que un modelo de lenguaje (u otra IA) te dé la respuesta o resultado que NECESITAS, no una respuesta genérica o desalineada con tu negocio.
**Analogía**: Imagina que tenes un negocio de artesanías de madera por Instagram y contratás a un ayudante de atención al cliente que sabe responder, pero si le pedís “respondé a esta clienta” te da una respuesta genérica. En cambio, si le decís: “Responde a esta clienta que pregunta por un mueble de roble de 1.20m para su living, con estantes, presupuesto de $20.000, entrega en 15 días en CABA: usa mi tono amigable, menciona el envío gratis en CABA y nuestro modelo de estantes ajustables que entra en ese presupuesto”, él te da la respuesta exacta que necesitas. Esa forma de formular la instrucción con todo el contexto y reglas es el prompt engineering.

---
Todas las analogías evitan los clichés prohibidos, usan escenarios cotidianos para emprendedores y vinculan cada concepto técnico a una acción que ellos realizan o podrían realizar en su negocio.