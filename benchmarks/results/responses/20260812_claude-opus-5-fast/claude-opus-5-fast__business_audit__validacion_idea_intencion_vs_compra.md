# Claude Opus 5 Fast — business_audit/validacion_idea_intencion_vs_compra

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 12.385s | tokens_per_second: 165.4
- input_tokens: 264 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un inversor que ha visto morir muchos proyectos por validar mal. Distingues sin piedad entre lo que la gente DICE y lo que la gente PAGA.

**user:**

Creo que ya validé mi idea y quiero renunciar a mi trabajo para dedicarme a esto a tiempo completo. Mis datos:

- Hice una encuesta a 40 personas de mi red.
- El 85% dijo que el problema les duele.
- El 72% dijo que pagaría $30 al mes por una solución.
- Tengo una lista de espera de 210 correos que se anotaron desde una landing page.
- Ingresos hasta hoy: $0. Todavía no cobré nada porque el producto no está listo.

¿Está validado? ¿Renuncio?


## Respuesta completa

## Respuesta corta

No está validado. Y no, no renuncies.

Tienes $0 de ingresos. Todo lo demás que listaste es **intención declarada**, que es la moneda más barata del mundo: la gente la reparte gratis porque no le cuesta nada.

Déjame desarmar tus datos uno por uno.

---

## Por qué cada dato vale menos de lo que crees

**"40 personas de mi red"**
Ese es el peor sesgo posible. Tu red te quiere, quiere que te vaya bien, y no quiere ser la persona que te dice que tu bebé es feo. Además: n=40 no es una muestra, es una anécdota con decimales. Y "de tu red" significa que ni siquiera sabes si existe un canal para llegar a desconocidos, que es el 80% del trabajo real.

**"85% dijo que el problema les duele"**
Casi todos los problemas duelen en abstracto. La pregunta que importa no es *¿te duele?* sino *¿qué estás haciendo hoy para resolverlo y cuánto te cuesta eso?* Si la respuesta es "nada, lo aguanto", no hay dolor: hay incomodidad. La gente no paga por incomodidades.

**"72% pagaría $30/mes"**
Este es el número más peligroso de tu lista, porque suena a evidencia y es ficción. La brecha entre "pagaría" y "pagó" es brutal. En la práctica, de un 72% de intención declarada en encuesta caliente termina convirtiendo entre el 2% y el 10%. Nadie que dice "sí pagaría" está mintiendo; simplemente está respondiendo una pregunta hipotética sin fricción, sin tarjeta, sin presupuesto, sin su jefe, sin las otras 14 prioridades de su semana.

**"210 correos en lista de espera"**
Un email es lo que la gente da cuando tiene curiosidad leve y cero compromiso. Es una señal, pero de la clase más débil. Preguntas que deberías poder responder y probablemente no puedes: ¿de dónde vinieron esos 210? ¿Cuánto te costó cada uno? ¿Qué % de los visitantes de la landing dejó su mail? ¿Cuántos abren tus correos hoy? Si vinieron de un post tuyo en LinkedIn compartido por amigos, no tienes un canal, tienes un favor único e irrepetible.

**"Ingresos: $0"**
Este es el único dato duro de toda tu lista. Y dice: no validado.

---

## La matemática que deberías estar haciendo

Si tus 210 emails son de calidad decente y les vendes tú mismo, uno por uno, por teléfono, con esfuerzo máximo: convertirás quizá entre 5 y 20. Digamos 12 en el escenario bueno.

12 × $30 = **$360 MRR**.

Ese es aproximadamente el techo de todo lo que has construido hasta hoy. Ahora pregúntate: ¿renuncias a tu sueldo por $360 al mes que ni siquiera has cobrado todavía?

Y la pregunta más incómoda: para llegar a un sueldo digno necesitas quizá 150-300 clientes. Eso significa repetir tu adquisición actual entre 15 y 30 veces, pero ya sin el combustible de "mis amigos comparten mi landing". No tienes idea de si eso es posible ni de cuánto cuesta.

---

## Qué sería validación de verdad

Solo hay una prueba: **dinero cobrado, de desconocidos, antes de que el producto esté terminado.**

Tres formas de conseguirla en los próximos 30 días, sin renunciar:

**1. Pre-venta real con cobro inmediato.**
Escríbele a los 210. No un "¿te interesaría?". Un: *"Lanzo el 15 de marzo. Precio fundador: $30/mes, primeros 3 meses cobrados hoy = $90, con garantía de devolución total. Aquí está el link de pago."* Cobra de verdad. Stripe tarda una tarde en configurarse.

**2. Servicio manual (concierge).**
Entrega el resultado a mano, sin software. Si tu producto promete ahorrar 5 horas al mes, hazlo tú con un Excel y correo electrónico. Cobra $30. Si nadie paga por el resultado hecho a mano, tampoco pagará por el software: el software solo cambia el margen, no el valor.

**3. Vende a 10 desconocidos fuera de tu red.**
Frío total. Cold email, DMs, un foro donde vivan tus usuarios. Esto prueba dos cosas a la vez: que hay demanda y que existe un canal. Lo segundo mata más startups que lo primero.

---

## Tu regla de decisión

Ponte un plazo de 60-90 días, trabajando de noche y fines de semana. Y define el umbral **