# Qwen 3.8 27B — strategy/business_model_validation

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 190.289s | tokens_per_second: 70.8
- input_tokens: 221 | output_tokens: 13467

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



Voy a ser brutal.

Si me presentas: **“app que conecta restaurantes pequeños con proveedores locales de ingredientes, marketplace con 15% de comisión”**, lo primero que pienso es:

> “¿Y qué? ¿Por qué no lo hacen por WhatsApp? ¿Quién entrega? ¿Quién responde si el proveedor no entrega? ¿Por qué no se van a saltar a ti después de 3 pedidos? ¿Cuánto gana realmente por transacción después de delivery, pagos, soporte y mermas?”

No tienes un marketplace todavía. Tienes una hipótesis de **densidad, confianza y logística** con una comisión pegada encima.

Aquí van las preguntas difíciles.

---

## 1. Los 5 riesgos principales de este modelo

### Riesgo 1: Cold start / liquidez de dos lados

No es un problema de “conectar”. Es un problema de **densidad**.

Si tienes 50 restaurantes y solo 3 proveedores de verduras, fallas.  
Si tienes 3 proveedores y 50 restaurantes, los proveedores no pueden cumplir, la calidad se cae y el restaurante te odia.

En un marketplace B2B de ingredientes, necesitas que el proveedor tenga:

- inventario estable,
- capacidad de entrega o retiro,
- precios claros,
- disponibilidad predecible,
- disposición a aceptar comisión,
- y que no se salte la plataforma.

Y necesitas que el restaurante tenga:

- proveedores suficientes en la misma zona,
- variedad mínima,
- entrega confiable,
- y motivo para no volver a llamar.

**Pregunta brutal:**  
¿Cuántos proveedores activos necesitas para que un restaurante pueda cubrir al menos 80% de su pedido semanal sin frustrarse?

Si no tienes esa densidad, no tienes marketplace. Tienes un directorio con problemas.

---

### Riesgo 2: El dolor puede no ser lo suficientemente monetizable

Tu hipótesis dice:

> “Los restaurantes pequeños pierden mucho tiempo llamando a múltiples proveedores.”

Eso puede ser verdad. Pero “pierden tiempo” no siempre significa “pagarán 15%”.

Llamar a 5 proveedores es molesto. Pero el restaurante pequeño probablemente ya lo hace porque le da:

- control de precio,
- negociación,
- crédito,
- relación personal,
- flexibilidad,
- conocimiento de qué proveedor le falla y cuál no.

Si tu app solo ahorra 1 hora a la semana, ¿vale 15% de su gasto en ingredientes?

Si el restaurante gasta $1,000 al mes en ingredientes, 15% son $150.  
¿Están dispuestos a pagar $150 al mes por ahorrar tiempo?  
¿O prefieren seguir llamando porque les da mejor precio y crédito?

**Pregunta brutal:**  
¿Tu solución ahorra tiempo, reduce costo, mejora margen, reduce riesgo de desabasto, o solo hace el proceso menos molesto?

Si solo es “menos molesto”, es difícil cobrar 15%.

---

### Riesgo 3: La comisión del 15% puede no dejar margen real

15% suena bien en el pitch. Pero no es tu margen. Es tu **take rate bruto**.

Por cada 100 de GMV, podrías tener:

| Concepto | Costo estimado |
|---|---:|
| Comisión | 15 |
| Delivery / última milla | 5 a 10 |
| Pagos / pasarela / efectivo | 2 a 4 |
| Soporte / quejas | 1 a 3 |
| Mermas / devoluciones / calidad | 1 a 3 |
| CAC amortizado | 2 a 6 |
| **Margen restante** | **0 o negativo** |

En restaurantes pequeños, el ticket puede ser bajo.  
En ingredientes locales, la logística puede ser cara.  
En LATAM, el pago puede ser más friccional.

Si tu ticket promedio es bajo y la frecuencia no es alta, el modelo se rompe.

**Pregunta brutal:**  
¿Cuál es tu ticket promedio, frecuencia de compra, costo de entrega, costo de pago y costo de soporte por pedido?

Si no puedes hacer ese cálculo con números reales, no tienes modelo unitario.

---

### Riesgo 4: Ingredientes locales = calidad variable, mermas, devoluciones y soporte

“Ingredientes locales” no es una categoría operativa. Es una frase bonita.

En la práctica, un proveedor local puede tener:

- calidad variable,
- precios que cambian diario,
- inventario que no está digitalizado,
- poca capacidad de empaque,
- problemas de frío,
- entregas tardías,
- productos que no llegan como se esperan,
- devoluciones complicadas,
- y poca disposición a aceptar responsabilidad.

Si el restaurante pide 10 kg de tomate y le llegan 8 kg, o llegan malos, o llegan tarde, **¿quién responde?**

Si dices “el proveedor”, el restaurante te va a decir:  
“Yo compré por tu plataforma, tú me debes la solución.”

Si tú respondes, te conviertes en una empresa de logística, calidad, soporte y disputas.

**Pregunta brutal:**  
¿Qué pasa si el producto llega malo, incompleto, tarde o no llega? ¿Quién paga? ¿Quién resuelve? ¿Cómo evitas que eso mate la confianza del restaurante?

Si no tienes respuesta operativa, no tienes marketplace. Tienes un problema de servicio.

---

### Riesgo 5: No tienes moat y pueden saltarse la plataforma

Después de la primera transacción, el restaurante conoce al proveedor.  
Después de la segunda, se saben los precios.  
Después de la tercera, pueden hablar por WhatsApp y saltarse tu comisión.

Eso es fatal.

Tu ventaja no puede ser solo “conectamos”.  
Tu ventaja tiene que ser algo que el restaurante y el proveedor no puedan replicar fácilmente:

- logística confiable,
- crédito,
- datos de demanda,
- calidad garantizada,
- pagos,
- cumplimiento,
- densidad,
- o una red tan líquida que salir sea más costoso que quedarse.

Si no hay eso, eres un intermediario frágil.

**Pregunta brutal:**  
¿Por qué el restaurante y el proveedor no se van a saltar después de 3 pedidos?

Si la respuesta es “porque les gusta la app”, no es una respuesta de VC. Es una esperanza.

---

## 2. Por qué podría NO funcionar en LATAM específicamente

Aquí va la parte incómoda.

En LATAM, este modelo puede fallar por razones culturales, operativas y económicas, no solo tecnológicas.

### 2.1. El competidor real no es otra app. Es WhatsApp + relaciones personales

En LATAM, el B2B pequeño funciona por:

- WhatsApp,
- llamadas,
- confianza personal,
- negociación,
- crédito,
- favores,
- y relaciones largas.

El restaurante pequeño no compra “eficiencia digital” primero. Compra:

- “que no me falten ingredientes”,
- “que me den buen precio”,
- “que me den crédito”,
- “que si hay problema me resuelvan”,
- “que me conozcan”.

WhatsApp ya hace eso. Gratis.

**Pregunta brutal:**  
¿Qué haces mejor que WhatsApp + el proveedor que ya le da crédito al restaurante?

---

### 2.2. Los proveedores pequeños pueden ser informales o muy fragmentados

Muchos proveedores locales pueden no tener:

- inventario digital,
- precios fijos,
- capacidad de facturar,
- empaque estándar,
- frío adecuado,
- capacidad de entrega,
- disposición a aceptar comisión,
- o estabilidad para cumplir pedidos semanales.

Si el proveedor no puede digitalizarse fácilmente, tu marketplace se vuelve un call center manual.

**Pregunta brutal:**  
¿Tu proveedor promedio puede recibir pedidos digitales, confirmar inventario, aceptar devoluciones y pagar comisión sin que tú tengas que hacer todo manualmente?

---

### 2.3. Los restaurantes pequeños tienen margen bajo y son sensibles al precio

Un restaurante pequeño no es un cliente ideal si:

- tiene ticket bajo,
- compra poco,
- exige precio,
- cambia de menú,
- tiene alta rotación,
- depende del dueño,
- no paga a tiempo,
- y te exige atención personalizada.

Puedes tener 100 restaurantes “interesados”, pero si cada uno compra poco, exige mucho y tiene churn alto, tu CAC se come tu LTV.

**Pregunta brutal:**  
¿Cuánto gasta al mes tu restaurante promedio en ingredientes? ¿Con qué frecuencia compra? ¿Cuánto te deja de margen neto después de todos los costos?

---

### 2.4. La última milla puede destruir tu economía

Ingredientes locales pueden requerir:

- entregas frecuentes,
- ventanas horarias,
- frío,
- rutas cortas,
- retiro,
- inspección,
- y soporte.

Si no tienes densidad geográfica, el delivery se vuelve carísimo.

Si entregas a 10 restaurantes dispersos, tu costo por pedido puede ser insoportable.

**Pregunta brutal:**  
¿Cuál es tu costo de entrega por pedido? ¿Puedes mantenerlo debajo de 5-8% del GMV sin subsidios?

---

### 2.5. El pago puede ser más complicado de lo que crees

En LATAM puede haber:

- efectivo,
- transferencias,
- tarjetas,
- crédito,
- cheques,
- pagos diferidos,
- chargebacks,
- inflación,
- devaluación,
- y proveedores que prefieren cobrar cash.

Si no controlas el pago, no controlas la transacción.  
Y si no controlas la transacción, tu “marketplace” es solo un directorio.

**Pregunta brutal:**  
¿Quién paga primero? ¿El restaurante paga antes? ¿El proveedor acepta esperar? ¿Cómo evitas fraudes? ¿Cómo manejas devoluciones?

---

### 2.6. “Local” puede ser una limitante, no una ventaja

“Ingredientes locales” suena bien. Pero puede significar:

- estacionalidad,
- poca escala,
- calidad inconsistente,
- proveedores pequeños,
- baja capacidad,
- y dificultad para estandarizar.

Si “local” te limita la oferta, tu marketplace puede ser bonito pero frágil.

**Pregunta brutal:**  
¿“Local” te da ventaja operativa o solo te da una historia bonita?

---

### 2.7. El CAC puede ser alto porque la confianza no se construye con una app

En LATAM, la confianza B2B pequeña se construye con:

- ventas,
- visitas,
- referidos,
- pruebas,
- y relaciones.

No es un modelo product-led donde alguien descarga la app y compra solo.

Si necesitas vender puerta a puerta, hacer demos, convencer al dueño, convencer al proveedor y resolver quejas manualmente, tu CAC puede ser alto.

**Pregunta brutal:**  
¿Cuánto te cuesta adquirir un restaurante que realmente repita? ¿Y cuántos meses tardan en volver a tu modelo anterior?

---

## 3. Qué tendría que ser verdad para que funcione

Esto es lo importante.

Para que tu modelo funcione, no basta que “les guste la idea”. Tienen que cumplirse varias condiciones.

### A. Del lado del restaurante

Tiene que ser verdad que:

1. **Compra ingredientes con frecuencia suficiente.**  
   Ideal: al menos 2 veces por semana.

2. **Tiene ticket promedio razonable.**  
   Si el pedido promedio es muy bajo, la comisión no cubre costos.

3. **Gasta una cantidad significativa en ingredientes.**  
   Ejemplo orientativo: si gasta menos de $500-$1,000 al mes en ingredientes, tu comisión puede ser irrelevante o el CAC no se recupera.

4. **Pierde tiempo real, no solo “molestia”.**  
   Ideal: 2+ horas por semana gestionando proveedores.

5. **Está dispuesto a pagar por confiabilidad.**  
   No solo por “conectar”. Por que no le falten ingredientes, que llegue a tiempo, que haya calidad, que haya soporte.

6. **Puede pagar digitalmente o con anticipación.**  
   Si todo el mundo quiere crédito largo, tu flujo de caja se rompe.

7. **Repita.**  
   Si ordena una vez por curiosidad y vuelve a WhatsApp, no hay negocio.

---

### B. Del lado del proveedor

Tiene que ser verdad que:

1. **Tiene inventario relativamente estable.**

2. **Puede aceptar pedidos digitales.**  
   Aunque sea por WhatsApp al inicio.

3. **Puede entregar o permitir retiro en ventanas claras.**

4. **Acepta una comisión.**  
   Si el proveedor dice “sí, pero solo si me traes muchos clientes”, hay que medir si la comisión compensa.

5. **No te salta fácilmente.**  
   Si después de 2 pedidos el proveedor y el restaurante se comunican directo, tu modelo se muere.

6. **Puede cumplir calidad mínima.**  
   No puedes depender de “a ver qué llega hoy”.

7. **Acepta reglas de devolución o compensación.**  
   Si no, el restaurante no confiará.

---

### C. De la operación

Tiene que ser verdad que:

1. **Fill rate alto.**  
   Ideal: 85-90%+ de los productos pedidos disponibles.

2. **Entrega a tiempo.**  
   Ideal: 80-85%+ dentro de la ventana acordada.

3. **Mermas controladas.**  
   Ideal: menos de 2% del GMV.

4. **Costo de delivery controlado.**  
   Ideal: menos de 5-8% del GMV, dependiendo del ticket.

5. **Soporte bajo.**  
   Si más de 10% de los pedidos generan quejas, tienes un problema operativo.

6. **Densidad geográfica.**  
   Necesitas restaurantes y proveedores en una zona razonablemente concentrada.

---

### D. De la unit economics

Tiene que ser verdad que:

1. **CAC < 1/3 del LTV.**  
   Si te cuesta $100 adquirir un restaurante, su LTV a 6-12 meses debería ser al menos $300.

2. **Churn bajo.**  
   Si el 30% de los restaurantes se va cada mes, no hay negocio.

3. **Frecuencia suficiente.**  
   Si compran una vez al mes, tu modelo de comisión puede no cubrir costos.

4. **Ticket suficiente.**  
   Si el pedido promedio es muy bajo, necesitas muchísimos pedidos.

5. **Net take positivo.**  
   No solo 15% bruto. Necesitas margen neto después de delivery, pagos, soporte, mermas y CAC.

---

### E. De la confianza

Tiene que ser verdad que:

1. **El restaurante confía en que el producto llegará.**

2. **El proveedor confía en que el restaurante pagará.**

3. **Tú puedes resolver disputas.**

4. **Hay consecuencia si alguien no cumple.**

Si no hay confianza operativa, no hay marketplace.

---

## 4. El escenario donde fracasas rápido y por qué

Te lo pongo concreto.

### Escenario de fracaso rápido

Lanzas en una ciudad con:

- 30 restaurantes registrados,
- 20 proveedores registrados,
- una app o landing bonita,
- 15% de comisión,
- y mucha expectativa.

Semana 1:  
Hay curiosidad. Hacen 15 pedidos.  
Todo parece bien.

Semana 2:  
Los pedidos caen a 6.

¿Por qué?

- Un proveedor no tenía producto.
- Otro cambió el precio.
- Otro entregó tarde.
- Otro mandó calidad mala.
- Un restaurante tuvo una queja y no volvió.
- Otro restaurante descubrió que el proveedor le responde directo por WhatsApp.
- El delivery costó más de lo esperado.
- El dueño pasó todo el día resolviendo pedidos en lugar de “escalar”.
- El CAC fue $100-$150 por restaurante.
- El LTV a 2 meses es $50-$80.
- El churn es 25-30% mensual.
- El fill rate está en 60-70%.
- El costo de delivery es 10%+ del GMV.

Al final del mes, te das cuenta de que no tienes un marketplace.  
Tienes un **directorio con problema de courier y soporte**.

### ¿Por qué fracasas?

Porque:

1. **No había densidad suficiente.**
2. **No controlabas calidad ni fulfillment.**
3. **El problema no era lo suficientemente doloroso para pagar 15%.**
4. **Los proveedores usaron la plataforma para conseguir leads y luego se saltaron.**
5. **Los restaurantes volvieron a WhatsApp porque era más flexible y personal.**
6. **Tu costo operativo fue mayor que tu comisión.**
7. **No tenías moat real.**

### Señal de muerte temprana

Fracasas rápido si después de 4-6 semanas ves:

- menos de 50% de restaurantes que hacen un segundo pedido,
- menos de 3 restaurantes que repiten 3 veces,
- fill rate debajo de 75%,
- delivery cost arriba de 8-10%,
- CAC arriba de $75-$100,
- churn mensual arriba de 20%,
- proveedores que no quieren pagar comisión,
- restaurantes que solo usan la primera vez por curiosidad.

Si eso pasa, no hay que “mejorar la app”.  
Hay que matar o pivotar.

---

## 5. Si solo tuviera $10K para validar, qué haría

No construiría una app.

Con $10K, si construyes una app, probablemente fracasas antes de validar.

Haría un **MVP concierge** de 6 semanas.

### Objetivo

No validar que “le gusta la idea”.  
Validar que:

1. Hacen transacciones reales.
2. Repiten.
3. Pagan comisión.
4. Los proveedores cumplen.
5. La logística es viable.
6. El costo no destruye el modelo.

---

### Paso 1: Elige un wedge muy específico

No valides “restaurantes pequeños con proveedores locales de ingredientes”.

Eso es demasiado amplio.

Elige:

- una ciudad,
- un barrio o zona de 3-5 km,
- una categoría,
- 10 restaurantes,
- 10 proveedores.

Ejemplos de wedge:

- “Verduras y hortalizas para 10 restaurantes en [barrio]”.
- “Carnes y aves para 10 restaurantes en [zona]”.
- “Insumos secos para 10 restaurantes en [zona]”.
- “Lácteos y panadería para 10 restaurantes en [zona]”.

La categoría debe tener:

- frecuencia decente,
- ticket suficiente,
- proveedores identificables,
- y dolor claro.

Mi preferencia para validar rápido: **carnes o insumos secos**.  
Verduras son más locales, pero más perecederas y variables. Carnes tienen ticket más alto. Insumos secos son más fáciles de operar.

---

### Paso 2: No uses app. Usa WhatsApp + hojas + pagos

Stack mínimo:

- WhatsApp Business,
- Google Sheets o Notion,
- Mercado Pago / Stripe / transferencia local,
- formulario simple,
- calendario de entregas,
- y tú como sistema operativo.

Tú serás el marketplace.

Tú recibes el pedido.  
Tú confirmas con el proveedor.  
Tú coordinas entrega o retiro.  
Tú cobras.  
Tú resuelves quejas.

Si no funciona con tú como sistema operativo, no funcionará con una app.

---

### Paso 3: Consigue 10 restaurantes con compromiso real

No me digas “10 restaurantes interesados”.

Necesito:

- 10 restaurantes que acepten hacer al menos 3 pedidos en 4 semanas,
- con pago anticipado o depósito,
- en una categoría específica,
- en una zona específica.

Pregunta clave:

> “Si te cobro 15% por gestionar tu compra con proveedores locales, ¿harías una primera compra de prueba pagando hoy?”

Si no pagan hoy, no hay validación.

---

### Paso 4: Consigue 10 proveedores que cumplan

No 50 proveedores “registrados”.

Necesito 10 proveedores que:

- tengan inventario estable,
- acepten pedidos por WhatsApp,
- puedan entregar o permitir retiro en ventana clara,
- acepten comisión,
- y no te salten fácilmente.

Pregunta clave:

> “Si te traemos restaurantes que compren 2 veces por semana, ¿aceptas una comisión de 15% o un split 10/5?”

Si el proveedor dice “sí, pero solo si me garantizan volumen”, hay que medir si puedes generar ese volumen.

---

### Paso 5: Crea un catálogo mínimo

No intentes tener todo.

Elige 30-50 SKUs.

Ejemplo:

- tomate,
- cebolla,
- ajo,
- lechuga,
- pollo,
- res molida,
- queso,
- arroz,
- aceite,
- etc.

Cada SKU debe tener:

- proveedor,
- precio,
- unidad,
- disponibilidad,
- método de entrega/retiro,
- y condición de calidad básica.

---

### Paso 6: Define días de entrega

No intentes entregar todos los días.

Empieza con:

- martes,
- jueves,
- y sábado.

O lo que tenga sentido por categoría.

El objetivo es crear densidad y predecibilidad.

---

### Paso 7: Cobra desde el día 1

No valides con “comisión gratis”.

Puedes dar un incentivo, pero no regales el modelo.

Opciones:

- 15% al restaurante.
- 10% al restaurante + 5% al proveedor.
- 15% al proveedor.
- 10% total en el primer mes, 15% después.

La idea es medir disposición a pagar.

Si nadie acepta pagar 10% después de la primera experiencia, no hay negocio.

---

## Presupuesto de $10K

| Concepto | Monto |
|---|---:|
| Preparación, legal básico, branding, herramientas | $2,000 |
| Incentivos / subsidio inicial | $3,000 |
| Delivery, combustible, empaque, logística | $3,000 |
| Publicidad local / ventas / referidos | $1,000 |
| Contingencia | $1,000 |
| **Total** | **$10,000** |

### Incentivos recomendados

No regales todo.

Ejemplo:

- Primera comisión reducida a 5%.
- O $10 de crédito en la primera compra.
- O delivery gratis solo en el primer pedido.
- O comisión 10% el primer mes, 15% después.

Pero si necesitas subsidios grandes para que repitan, no hay negocio.

---

## Métricas de validación

Después de 6 semanas, necesitas esto para decir “sigue”:

### Métricas de restaurante

- 10+ restaurantes hayan hecho al menos 1 transacción.
- 5+ hayan hecho al menos 2 transacciones.
- 3+ hayan hecho al menos 3 transacciones.
- Churn bajo: que no se vayan todos después de la primera compra.
- NPS decente: que lo recomienden a otro restaurante.
- Disposición a pagar 10%+ después de la primera experiencia.

### Métricas de proveedor

- 10+ proveedores activos.
- 85%+ de fill rate.
- 80%+ de entregas a tiempo.
- Menos de 10% de pedidos con queja.
- Proveedores que no se salten sistemáticamente.

### Métricas económicas

- Costo de delivery < 8% del GMV.
- CAC < $75 por restaurante.
- LTV a 6 meses > 3x CAC.
- Comisión neta positiva después de costos.
- Ticket promedio suficiente.
- Frecuencia mínima: 2+ pedidos por semana por restaurante.

---

## Criterio de muerte

Matarías o pivotarías si después de 6 semanas ves:

- menos de 5 restaurantes transaccionando,
- menos de 3 restaurantes repitiendo,
- fill rate debajo de 70%,
- delivery cost arriba de 10%,
- CAC arriba de $100,
- proveedores que no aceptan comisión,
- restaurantes que vuelven a WhatsApp,
- proveedores que se saltan la plataforma,
- o si tú pasas más tiempo resolviendo quejas que creciendo.

Si necesitas que tú hagas todo manualmente y aun así no repiten, no hay escalamiento.

---

## Lo que yo te preguntaría en el pitch

Si me presentas esta idea, estas son las preguntas que te matarían:

1. **¿A quién le cobras 15%? ¿Al restaurante, al proveedor, o a ambos?**
2. **¿Quién entrega? ¿Tú, el proveedor, o el restaurante retira?**
3. **¿Qué pasa si el proveedor no entrega?**
4. **¿Qué pasa si el producto llega malo?**
5. **¿Quién paga la devolución?**
6. **¿Cuál es el ticket promedio?**
7. **¿Cuántas veces por semana compra el restaurante?**
8. **¿Cuál es tu costo de delivery por pedido?**
9. **¿Cuál es tu CAC?**
10. **¿Cuál es tu LTV?**
11. **¿Por qué no lo hacen por WhatsApp?**
12. **¿Por qué no se van a saltar después de 3 pedidos?**
13. **¿Qué tienes que no pueda copiar un distribuidor local?**
14. **¿Por qué los proveedores aceptarían 15%?**
15. **¿Por qué los restaurantes pagarían 15% si ya llaman y negocian?**

---

## Mi veredicto brutal

Tu idea **puede** funcionar, pero no como “app que conecta”.

Puede funcionar si te conviertes en:

> **una red confiable de compra de ingredientes para restaurantes pequeños en una zona específica, con logística, calidad, pagos y soporte.**

No una app.  
Una operación.

Tu ventaja no es la tecnología.  
Tu ventaja tiene que ser:

- densidad,
- confianza,
- cumplimiento,
- datos,
- y que el restaurante no pueda replicar fácilmente esa experiencia por WhatsApp.

Si solo conectas, eres frágil.  
Si controlas la transacción y el cumplimiento, puedes tener algo.

Pero si no puedes validar con 10 restaurantes, 10 proveedores, una categoría, una zona y 6 semanas, no levantes. No construyas. No contrates. No gastes en app.

Valida con dinero, repeticiones y operación.  
Si no pasa ahí, no pasará con inversionistas.