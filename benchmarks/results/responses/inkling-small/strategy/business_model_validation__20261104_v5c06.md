# Inkling Small — strategy/business_model_validation

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 33.009s | tokens_per_second: 135.5
- input_tokens: 173 | output_tokens: 4473

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

Siéntate. Esto no es un *pitch*; es una autopsia antes de que nazcas. Tu “hipótesis” suena a proyecto de final de semestre de administración: *“Los restaurantes pierden tiempo llamando”*. No. Pierden **dinero** y **confianza**, no minutos en el celular. El problema que describes no existe como lo imaginas, o al menos no vale 15% de comisión.

Aquí está la paliza, sin abrazos.

---

### 1. LOS 5 RIESGOS PRINCIPALES (Y POR QUÉ TU MODELO SE DESANGRA)

**a) El “fiado” y la inspección física son sagrados.**
En este negocio no compras cilantro; compras **confianza**. El dueño del restaurante va al mercado o recibe al proveedor, toca la verdura, huele el pescado, regatea. Tu app exige que pague antes, sin tocar, y luego acepte lo que llega. Eso es un suicidio. Además: el proveedor le da **crédito a 30 días**; tú exiges pago inmediato o tarjeta. Mataste su flujo de caja.

**b) El 15% es un impuesto a la pobreza.**
Un restaurante pequeño opera con márgenes netos de 5-10% (a veces menos). Sus proveedores operan con márgenes de 20-30%. Si tú metes 15% en medio, **ambos te odian**. El restaurante ve que su costo sube y no puede pasarlo al cliente porque hay 10 taquerías al lado. El proveedor ve que tú te llevas más que su ganancia por venta. No eres un intermediario; eres un ladrón de margen.

**c) El problema de la gallina y el huevo con densidad baja.**
Para que funcione, necesitas **ambos lados críticos** en la misma zona. Si tienes 10 restaurantes y 3 proveedores, nadie compra porque no hay variedad. Si tienes 100 restaurantes, necesitas 50 proveedores entregando hoy, mañana y pasado. Eso requiere logística, inventario y garantías que tú no puedes pagar.

**d) La logística de última milla te convierte en transportista, no en marketplace.**
En LATAM los proveedores suelen entregar con su propio carrito, bicicleta o camioneta. Los restaurantes van a buscar. Si tu “app” no resuelve **quién lleva la mercancía, cuándo y a cuánto**, no es un marketplace; es un catálogo frustrado. Y si empiezas a contratar mototaxis o flotas, tu margen de 15% se lo come la gasolina.

**e) Tu competencia no es otra app; es WhatsApp y el mercado mayorista.**
Ya existe la solución: un grupo de WhatsApp con “el de las verduras”, “el del pollo” y “el de los abastos”. Coste: cero. Credibilidad: alta. Precio: negociable. Tú no estás innovando; estás intentando cobrar por algo que ya funciona de forma imperfecta pero **gratuita y confiable**.

---

### 2. POR QUÉ ESTO NO FUNCIONA EN LATAM (Y NO ES POR FALTA DE “INNOVACIÓN”)

- **WhatsApp es tu verdadero enemigo y tu verdadero marketplace.** En México, Colombia, Chile, Perú, el 90% de la compra B2B de pequeños restaurantes ocurre por mensaje, no por portal. No hay “fricción digital” que resolver; hay **fricción de confianza** que una app no puede simular.
- **La economía es informal y de efectivo.** Muchos proveedores no emiten factura, no quieren trazabilidad bancaria, y prefieren que les pagues en efectivo porque deben a sus propios proveedores. Tú exiges transacciones digitales para cobrar tu 15%. Eso los expulsa.
- **El crédito (“fiado”) es sangre del sistema.** Un restaurante pequeño no paga al proveedor el mismo día; paga cuando vende. Tu modelo de marketplace requiere un flujo de caja limpio. Si pones un intermediario que retiene dinero o exige pago inmediato, rompes la cadena.
- **Los mercados mayoristas (Central de Abasto, Corabastos, La Vega, etc.) ya hacen agregación.** Un restaurante va a las 4 AM, ve todo, compara precios y compra al contado. Tu app ofrece menos variedad, precios más altos por la comisión, y entrega diferida. No ganas.
- **El dueño del restaurante no es un “usuario digital”; es un operador de 55 años que confía en su proveedor de 20 años.** No va a dejar de llamar a Juan porque apareció una app. No hay *product-market fit* porque no hay adopción cultural.
- **La fragmentación es absurda, pero local.** En una ciudad hay 30 proveedores de cilantro, pero cada uno sirve 3 colonias. No puedes escalar sin una logística regional masiva, que requiere capital que no tienes.

---

### 3. QUÉ TENDRÍA QUE SER VERDADERO PARA QUE FUNCIONE (LAS ASUNCIONES QUE DEBES PROBAR, NO ASUMIR)

No es suficiente que “hagan pedidos”. Debe ser verdad que:

1. **El “ahorro de tiempo” de no llamar vale más del 15% de su compra mensual.** Si compra $10,000/mes, debe pagar $1,500 por no hacer 10 llamadas. Eso es absurdo; él hace esas llamadas mientras fuma.
2. **Los proveedores aceptarán pagar tu comisión y dejar de dar crédito.** Eso implica que tú les entregues clientes nuevos que ellos no pueden conseguir solos. Pero los restaurantes ya tienen sus proveedores.
3. **Puedes garantizar calidad sin que el restaurante toque el producto.** Si falla una vez (pescado pasado, verdura seca), el restaurante vuelve a WhatsApp para siempre.
4. **Puedes resolver logística a costo cero o muy bajo.** Si necesitas una flota o centros de distribución, tu modelo de 15% colapsa.
5. **El restaurante está dispuesto a usar una tarjeta o transferencia para pagar al instante.** Eso es falso para el 70% de los pequeños restaurantes que operan en efectivo y crédito.

---

### 4. EL ESCENARIO DE FRACASO RÁPIDO (Y POR QUÉ SUCEDERÁ EN 90 DÍAS)

Lanzas en una zona (ej. una colonia de CDMX o un barrio de Medellín).

- **Semana 1-2:** Logras 15 restaurantes y 8 proveedores. Hacen un pedido de prueba por curiosidad.
- **Semana 3:** Se dan cuenta de que el precio es 15% mayor que llamando a Juan directamente. Además, no pueden pedir “fiado”. El cilantro llegó en 3 horas, pero no estaba tan fresco porque no lo eligieron.
- **Semana 4-6:** Los restaurantes hacen un pedido más, luego otro. Pero cada vez que comparan, ganan más comprando directo. El proveedor se da cuenta de que tú te llevas 15% y que el restaurante podría haber comprado directo. Empieza a ignorarte.
- **Semana 8-12:** El volumen cae a cero. Los proveedores vuelven al mercado mayorista. Los restaurantes vuelven a sus grupos de WhatsApp. Tú gastaste $8,000 en desarrollo, $2,000 en promoción y te quedaste con un Excel lleno de datos inútiles.

**Moraleja:** No fallaste por ejecución técnica. Fallaste porque **el problema que resolviste (llamar a proveedores) no es un problema costoso; es una costumbre cultural.** Y el problema real (crédito, confianza, precio, logística) es más duro que una app.

---

### 5. SI SOLO TUVIESES $10K PARA VALIDAR: NO HAGAS LA APP. HAZ UN MANUAL

**Regla de oro:** Si no puedes vender esto con WhatsApp y un mototaxi, no lo construyas.

1. **No escribas una línea de código.** Crea un grupo de WhatsApp Business o una página simple (Carrd o Notion). Usa Excel.
2. **Elige UNA categoría y UNA zona:** Ej. “verduras frescas” en una sola colonia o mercado.
3. **Encuentra 3 proveedores reales y 10 restaurantes reales** manualmente, no por marketing.
4. **Tú eres el marketplace.** Tomas pedidos por WhatsApp, compras al proveedor (o le dices que entregue), y tú entregas con una moto alquilada o tu propia.
5. **Cobra el 15% o un fee fijo.** Anota quién paga, quién pide fiado, quién se queja de calidad.
6. **Tu métrica de éxito:** ¿En la semana 4, más del 50% de los restaurantes repiten sin que tú les recuerdes? ¿El proveedor te prefiere a ti sobre sus clientes directos?
7. **Si la respuesta es “no” o si te dicen *“por qué no solo llamo a Juan”*, destruye el proyecto.** Ese $10K te enseñó que el modelo es irrelevante. No lo desperdicies en un MVP tecnológico.

---

**Veredicto final:** Tu idea no es “mala”; es **incompleta y probablemente irrelevante**. No estás construyendo un marketplace; estás intentando digitalizar una relación de confianza que funciona por WhatsApp, crédito y tacto. Si quieres que funcione, no necesitas una app; necesitas **cambiar la economía del crédito y la logística**, y eso cuesta millones, no $10K.

Si insistes, empieza manual. Si no funciona manual, no funcionará digital. Ahora, deja de perder mi tiempo y ve a validar. No a programar.