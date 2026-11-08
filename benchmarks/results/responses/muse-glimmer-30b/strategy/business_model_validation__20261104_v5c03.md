# Muse Glimmer 30B — strategy/business_model_validation

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.84 | quality: 10.0
- latency_total: 14.677s | tokens_per_second: 116.0
- input_tokens: 217 | output_tokens: 1702

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

Tu idea suena a "Uber para verduras". Es decir, bonita en PowerPoint y mortal en la calle. Vamos a lo que duele:

**1. Los 5 riesgos principales de tu modelo**

1. **Comisión del 15% es suicidio.** Un restaurante pequeño opera con margen neto de 5-10%. Un proveedor de alimentos vive con 8-15%. ¿De dónde sacas el 15%? Te van a decir que sí en la demo y luego te van a pedir que lo bajes a 2% o te van a esquivar. Estás poniendo un impuesto a un mercado que no tiene margen para impuestos.
2. **Problema de doble cara sin incentivo.** Necesitas restaurantes Y proveedores al mismo tiempo. Los proveedores no se suman por "exposición", se suman si les llega pedido constante. Los restaurantes no se suman si no hay stock y precio mejor que su proveedor de confianza. Te quedas en el limbo del huevo y la gallina.
3. **No estás resolviendo un dolor real, estás resolviendo un dolor que tú crees que existe.** Llamar a 3 proveedores no es un dolor, es el trabajo. El dolor real es precio, crédito a 30 días, entrega a hora exacta y calidad consistente. WhatsApp ya resuelve la llamada. ¿Qué resuelve tu app que WhatsApp + una hoja de Excel no resuelva?
4. **Logística y calidad es tu problema aunque no quieras.** Si el tomate llega podrido, ¿quién responde? Tú. Si el proveedor no entrega, ¿quién pierde el servicio del restaurante? Tú. Te conviertes en call center de reclamos sin tener control de la cadena.
5. **Falta de defensibilidad.** ¿Qué impide que un proveedor grande te copie y te bloquee? ¿Qué impide que Mercado Libre o Rappi agregue "ingredientes para restaurantes" en 3 meses? No tienes data, no tienes red, no tienes barrera.

**2. Por qué podría NO funcionar en LATAM específicamente**

Porque LATAM no es Europa con restaurantes que usan SAP. Aquí el 70% de la compra es informal, en efectivo, con relación personal y con crédito. El proveedor le vende al restaurante porque es su primo, porque le fía hasta fin de mes, porque le lleva la verdura en moto a las 5 AM. 

Conectividad inestable, rotación de personal alta, analfabetismo digital en proveedores pequeños, facturación electrónica que muchos evaden, y una desconfianza brutal a pagar comisión a una plataforma que no conocen. Además, la fragmentación es infinita: no hay "proveedores locales", hay 200 verdulerías por barrio que no tienen ni email.

**3. Qué tendría que ser verdad para que funcione. Key assumptions que hoy son mentiras**

* Que los restaurantes pequeños están dispuestos a pagar por conveniencia, no solo por precio. Hoy no lo están.
* Que los proveedores locales tienen capacidad y ganas de digitalizarse y atender pedidos pequeños. La mayoría no tiene sistema, ni personal, ni quiere pedidos de 50 soles.
* Que puedes estandarizar precios y calidad en un mercado donde todo se negocia al día.
* Que la comisión la paga el proveedor y no se la pasa al restaurante. Si se la pasa, pierdes al restaurante.
* Que puedes escalar sin logística propia. No puedes.

Si una de esas falla, el modelo se cae.

**4. Escenario donde fracasas rápido y por qué**

Te gastas 6 meses y $40k en una app bonita. Consigues 30 restaurantes piloto en Lima. Les encanta la idea. Consigues 15 proveedores. Primer pedido real: el proveedor sube precio porque "es por la plataforma", el restaurante se queja, el pedido llega tarde porque el proveedor no tiene moto, el restaurante paga en efectivo y te debe la comisión. 

En 90 días tienes churn del 80%, proveedores que te piden que bajes comisión a 3% y restaurantes que vuelven a WhatsApp porque es gratis y más rápido. Fracasas rápido porque intentaste digitalizar una relación de confianza y crédito con una app.

**5. Con $10K para validar, qué haría un VC realista**

Ni una línea de código. 

Con $10K hago un concierge manual en UNA sola comuna y con UN solo producto: por ejemplo, pollo y verduras para 20 restaurantes de Miraflores/Surco. Yo mismo soy el marketplace. 

Llamo a restaurantes, les pregunto qué compran, a qué hora, cuánto pagan. Llamo a 5 proveedores, les cierro precio fijo por 2 semanas. Hago el match por WhatsApp y cobro la diferencia. Si no puedo generar $2k de GMV en 30 días sin app, con mi tiempo y WhatsApp, el modelo no existe. 

Si funciona, el siguiente paso no es una app, es un agente humano que hace el pedido por ellos. La app viene después, cuando el comportamiento ya está probado y pagando.

Tu turno: ¿cuál es el costo de adquisición de un restaurante y cuánto tiempo te toma que haga su primer pedido repetido? Si no sabes eso, no tienes negocio.