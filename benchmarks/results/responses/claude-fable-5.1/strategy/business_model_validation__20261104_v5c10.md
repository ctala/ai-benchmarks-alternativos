# Claude Fable 5.1 — strategy/business_model_validation

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.8 | quality: 10.0
- latency_total: 82.295s | tokens_per_second: 59.5
- input_tokens: 290 | output_tokens: 4894

## Entrada exacta (lo que recibió el modelo)

**user:**

Quiero crear una app que conecta restaurantes pequenos con proveedores de ingredientes locales. El modelo es marketplace con 15% de comision por transaccion.

Mi hipotesis: los restaurantes pequenos pierden mucho tiempo llamando a multiples proveedores y quieren una solucion digital.

Actua como un VC esceperico. Hazme las preguntas dificiles que me harian en un pitch:
1. Identifica los 5 riesgos principales de este modelo
2. Por que podria NO funcionar en LATAM especificamente?
3. Que tendria que ser verdad para que funcione? (key assumptions)
4. Cual es el escenario donde fracaso rapido y por que?
5. Si solo tuviera $10K para validar, que harias?

No seas amable. Se brutalmente honesto.


## Respuesta completa

Bien. Me pongo el sombrero. Antes de tus 5 puntos, el problema de fondo:

**Tu hipótesis está mal planteada.** "Pierden tiempo llamando proveedores" es una molestia, no un dolor. El dueño de una fonda no se despierta a las 5am pensando "ojalá existiera una app". Se despierta pensando en que el proveedor de pollo le subió el precio, que no tiene efectivo hasta el viernes, y que el de verduras le mandó jitomate podrido. Tu app resuelve el problema que tú ves, no el que él tiene. Y "quieren una solución digital" nadie lo quiere. Quieren más margen, crédito y que no les fallen.

---

## 1. Los 5 riesgos principales

**Riesgo 1: Tu take rate es más grande que el margen del proveedor.**
La distribución de alimentos frescos opera con márgenes brutos de 8-15% y netos de 2-5%. Pedirle 15% a un proveedor es pedirle que te entregue toda su utilidad. ¿Quién paga? Si lo paga el restaurante, tu app es 15% más cara que ir al mercado. Si lo paga el proveedor, no tiene incentivo para estar ahí. Si lo dividen, ambos lo odian. Este número solo lo mata el modelo. ¿De dónde salió el 15%? ¿De un spreadsheet o de que alguien aceptó pagarlo?

**Riesgo 2: Desintermediación inmediata.**
Marketplace de servicios recurrentes con partes que se conocen físicamente = la plataforma dura exactamente una transacción. El proveedor entrega, le deja su WhatsApp al cocinero, y la segunda compra ya no pasa por ti. No tienes ningún mecanismo de retención. Uber lo resuelve porque nunca repites chofer. Tú estás conectando gente que se verá tres veces por semana.

**Riesgo 3: Chicken-and-egg con dos lados que no te necesitan.**
Los proveedores ya tienen clientes. Los restaurantes ya tienen proveedores. No estás creando demanda ni oferta nueva, estás tratando de meterte en medio de una relación que ya existe. ¿Qué le das al proveedor que justifique subir su catálogo, actualizar precios diario (los precios de fresco cambian todos los días) y atender pedidos de una app?

**Riesgo 4: No controlas la calidad ni la entrega, pero te van a culpar.**
Si eres puro marketplace, el jitomate llega podrido y el restaurante te reclama a ti. Si no lo resuelves, te deja. Si lo resuelves, ahora eres distribuidor con inventario, logística y capital de trabajo. Todos los que han intentado esto en LATAM (Frubana, Chiper, Jüsto B2B) terminaron teniendo bodegas y camiones. Ya no es un marketplace de 15%, es un negocio de distribución con margen de 10% y CAPEX.

**Riesgo 5: El competidor es WhatsApp, y es gratis.**
Tu competencia no es otra app. Es un grupo de WhatsApp donde el proveedor manda la lista de precios en foto a las 6am y el cocinero contesta "mándame 10kg de cebolla". Funciona, es gratis, tiene confianza construida y no cobra 15%. ¿Qué haces 10x mejor que eso?

---

## 2. Por qué podría NO funcionar en LATAM específicamente

**Informalidad.** Un porcentaje enorme de restaurantes pequeños y proveedores operan parcial o totalmente en efectivo y sin factura. Tu plataforma crea un registro digital de cada transacción. Para muchos, eso no es una feature, es una amenaza fiscal. Les estás pidiendo que formalicen su cadena de suministro para ahorrarse unas llamadas.

**El fiado.** La relación proveedor-restaurante en LATAM está construida sobre crédito informal. "Te pago el viernes" o "págame cuando cobres". Esa confianza tardó años en construirse. Tu app con pago digital inmediato rompe el único mecanismo de financiamiento que tiene el restaurante. ¿Vas a dar crédito tú? Con qué balance y con qué modelo de riesgo.

**Las centrales de abasto ya resolvieron el problema.** La Central de Abasto en CDMX, CEASA en Brasil, Corabastos en Bogotá. El dueño o su gente va a las 5am, ve el producto, negocia, paga, se lleva todo en una camioneta. Eso es descubrimiento, comparación de precios y logística en un solo lugar. No perdieron tiempo llamando porque no llaman: van.

**Confianza es presencial.** En fresco, la calidad varía por lote. El cocinero quiere ver, tocar, oler. Comprar fresco por catálogo digital a un proveedor que no conoces es una apuesta que pocos van a hacer con su margen del día.

**Logística cara y caótica.** Entregas de última milla en ciudades latinoamericanas con tráfico, inseguridad y direcciones imprecisas. Si el proveedor es pequeño, no tiene flota para entregar a 15 restaurantes dispersos. Si tú la pones, ver Riesgo 4.

**Ya hubo muertos.** Frubana levantó más de $100M y tuvo que reducir operaciones y países. Chiper, Jüsto y otros quemaron capital brutal en este espacio con equipos y dinero que tú no tienes. ¿Qué sabes tú que ellos no supieron?

---

## 3. Qué tendría que ser verdad para que funcione

Si no puedes demostrar estas con datos reales (no encuestas), no tienes negocio:

1. **Existe un segmento donde el restaurante paga sobreprecio hoy por mala información.** Es decir, hay restaurantes pagando 20-30% más que el precio de mercado porque no tienen acceso al proveedor correcto. Si ese spread existe, tu 15% cabe ahí. Si no existe, no cabe.

2. **El proveedor tiene capacidad ociosa y no sabe cómo conseguir clientes.** Si está vendiendo todo lo que produce, no te necesita.

3. **Algo te hace necesario después de la primera transacción.** Crédito, garantía de calidad, consolidación de pedidos, pago asegurado al proveedor. Sin esto, eres una agencia de citas que cobra renta mensual.

4. **La frecuencia justifica el hábito.** Un restaurante pide 3-6 veces por semana. ¿Van a abrir tu app 5 veces por semana en lugar de mandar un audio?

5. **Puedes operar sin tocar el producto.** Si para funcionar necesitas controlar calidad y entrega, tu modelo no es marketplace. Admítelo ahora, no en 18 meses.

6. **El restaurante puede pagar digitalmente y el proveedor quiere cobrar digitalmente.** Ambas cosas, en el mismo segmento, en la misma ciudad.

---

## 4. El escenario donde fracasas rápido

Te lo narro porque es exactamente lo que pasa:

Mes 1-3: Construyes la app. Consigues 40 restaurantes y 15 proveedores a punta de visitas y favores. Todos dicen "qué buena idea".

Mes 4: Primeras 30 transacciones. Celebras. GMV de $8K. Tu comisión: $1,200, pero el 60% la perdonaste para que probaran.

Mes 5: Las transacciones bajan a 12. Los restaurantes activos siguen comprando a los mismos proveedores que conocieron en tu app, pero por WhatsApp y en efectivo. Lo descubres cuando un proveedor te dice "ah sí, el de la taquería me pide todos los martes" y en tu app lleva 3 semanas sin ordenar.

Mes 6: Para retener, empiezas a resolver quejas de calidad tú mismo. Vas personalmente a cambiar un pedido. Ya eres operador de logística sin cobrar por ello.

Mes 7: Decides que necesitas dar crédito para competir con el fiado. No tienes capital. Decides tener inventario propio de 5 productos "ancla". Ahora eres Frubana con $0 de funding.

Mes 9: Te quedas sin dinero. La diapositiva de tu deck dice "pivot a SaaS de gestión de compras para restaurantes".

**Por qué:** porque nunca validaste que alguien pague por la intermediación. Validaste que la gente es amable cuando le muestras una app.

---

## 5. Si solo tuviera $10K para validar

**No construyo nada de software. Cero. Ni un landing page.**

**Semana 1-2 ($500): Descubrimiento real, no encuestas.**
Me paro en la Central de Abasto (o equivalente) a las 5am tres días seguidos y hablo con 30 compradores de restaurantes. No les pregunto "¿usarías una app?". Les pregunto: ¿cuánto pagaste por la cebolla hoy? ¿A quién le compras y desde cuándo? ¿Cuándo fue la última vez que cambiaste de proveedor y por qué? ¿Te dan crédito? ¿Cuántos días? Busco el spread de precios entre lo que paga un restaurante y otro por lo mismo. Si no hay spread de al menos 15-20%, me detengo aquí y me ahorro $9,500.

**Semana 3-6 ($3,000): Concierge manual. Yo soy la app.**
Elijo UNA categoría (fresco de alto valor y alta frecuencia: proteína o verdura premium) y UNA zona de 2 km. Consigo 10 restaurantes y 3 proveedores. Todo por WhatsApp. Yo tomo pedidos, yo consolido, yo negocio precio, yo coordino entrega. Cobro desde el pedido número uno, 15% o lo que aguante. Si tengo que perdonar la comisión para que ordenen, ya tengo mi respuesta.

**Semana 7-10 ($4,000): Mido una sola cosa: retención con pago.**
No mido signups, no mido "interés". Mido: de los 10 restaurantes, ¿cuántos hicieron su pedido número 5 pagando comisión completa? ¿Cuántos intentaron saltarme para ir directo con el proveedor? Les pregunto abiertamente a los que se fueron por qué. Uso ese dinero para subsidiar los errores operativos que seguro cometeré y para pagar a alguien que me ayude con entregas.

**Semana 11-12 ($2,500): Probar el lado proveedor.**
Le ofrezco a 5 proveedores nuevos acceso a "mis" restaurantes a cambio de comisión. Si ninguno acepta pagar, el modelo tiene que ser cobrado al restaurante. Si el restaurante tampoco paga, no hay modelo.

**Criterio de éxito brutal:** 6 de 10 restaurantes siguen ordenando por mí en semana 12, pagando comisión completa, y al menos 2 proveedores aceptaron pagar por acceso. Si no llego a eso, no construyo nada. Si llego, lo que construya después no es una app, es el sistema para hacer lo que ya hice a mano con 10 clientes, para 100.

---

Última pregunta, la que te harían en la sala: **¿Has operado un restaurante o un negocio de distribución de alimentos?** Si la respuesta es no, tu primer paso no es levantar capital. Es ir a trabajar tres meses en la compra de uno. Te va a costar menos que fracasar y vas a aprender más que con cualquier deck.