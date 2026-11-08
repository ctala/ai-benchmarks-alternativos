# Qwen 3.8 27B — strategy/business_model_validation

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.94 | quality: 10.0
- latency_total: 511.36s | tokens_per_second: 42.8
- input_tokens: 221 | output_tokens: 21872

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



Ok. Modo VC escéptico. No vengo a aplaudirte. Vengo a decirte por qué me costaría escribirte cheque.

Tu hipótesis —“los restaurantes pequeños pierden tiempo llamando a proveedores” — puede ser cierta. Pero tu modelo —“marketplace con 15% de comisión” — suena a software cuando el problema real es **abastecimiento B2B**: precio, crédito, entrega, calidad, disponibilidad y confianza.

Si no resuelves eso, el 15% no es una comisión: es un impuesto.

---

## 1. Los 5 riesgos principales de este modelo

### Riesgo 1: Frío bilateral y falta de densidad

No tienes un marketplace hasta que tengas:

- suficiente oferta: proveedores con stock, precios, capacidad de entrega;
- suficiente demanda: restaurantes comprando con frecuencia;
- suficiente densidad geográfica: pedidos concentrados en una zona para que la logística no te mate.

Si tienes 8 restaurantes y 6 proveedores dispersos, no tienes plataforma. Tienes un teléfono, una hoja de cálculo y mucho estrés.

**Pregunta de pitch que te va a matar:**

> “¿Cuántos pedidos por zona, por día, necesitas para que la entrega sea rentable?”

Si no tienes una respuesta numérica, no tienes unidad de negocio.

---

### Riesgo 2: El 15% puede no alcanzar para cubrir la operación

En food B2B los márgenes son apretados. Tu 15% debe cubrir:

- logística o coordinación de entrega;
- pagos electrónicos o transferencias;
- devoluciones y reclamos;
- soporte;
- fricción de onboarding;
- posible descuento inicial;
- costo de adquirir al restaurante.

Ejemplo cruel:

- Ticket promedio: $100.
- Comisión 15%: $15.
- Logística/entrega: $8.
- Pago: $2.
- Devoluciones/reclamos: $2.
- Soporte/operación: $2.

Margen bruto: $1.

Si tu CAC por restaurante es $80 o $100, necesitas muchos pedidos para recuperar ese costo. Si el restaurante no repite, no tienes negocio.

**Pregunta de pitch:**

> “¿Cuál es tu margen bruto por pedido después de logística, pagos, devoluciones y soporte? ¿Cuántos pedidos necesita un restaurante para que recuperes el CAC?”

---

### Riesgo 3: La calidad y la entrega se vuelven tu problema, aunque “solo conectes”

Si un proveedor entrega tarde, incompleto, mal empaquetado o con mala calidad, el restaurante no va a decir: “qué mal, el marketplace no era el responsable”. Va a decir:

> “Esta app es una basura, no me deja comprar bien.”

En alimentos, especialmente frescos, la promesa de entrega es promesa de operación.

Si el proveedor entrega, tú dependes de su disciplina.  
Si tú entregas, te conviertes en logística.  
Si el restaurante recoge, tu valor baja mucho.

**Pregunta de pitch:**

> “¿Quién responde cuando llega mala la mercadería? ¿Quién paga el reemplazo? ¿Quién garantiza el tiempo de entrega?”

Si no puedes responder eso, no eres marketplace. Eres un intermediario con problemas de cumplimiento.

---

### Riesgo 4: “Ahorrar tiempo” no siempre justifica un 15%

El dueño de un restaurante pequeño no compra por conveniencia. Compra por:

- precio;
- crédito;
- disponibilidad;
- que no le falten insumos;
- que el proveedor le responda;
- que le deje todo en un solo pedido;
- que le resuelva problemas.

Si tu plataforma le ahorra 30 minutos a la semana pero le sube el costo un 15%, puede no importarle.

Peor aún: si su proveedor actual le da crédito, entrega todos los días y conoce su menú, tu app tiene que ser mucho más que “conveniente”.

**Pregunta de pitch:**

> “¿Por qué un dueño dejaría WhatsApp, su relación personal y su proveedor con crédito para comprar por una plataforma que le cobra 15%?”

Si tu respuesta es “porque es digital”, te rechazan.

---

### Riesgo 5: Desintermediación y competencia de distribuidores/incumbentes

Este es el riesgo silencioso.

Si el restaurante conoce al proveedor por primera vez a través de tu app, después del primer pedido puede decir:

> “Ok, ya sé quién es, ya sé dónde está, ya sé cuánto cobra. Le compro directo.”

Y tú quedas fuera.

El proveedor también puede pensar:

> “Esta plataforma me da clientes, pero me saca 15% y me expone precios. Cuando tenga los contactos, me los llevo.”

Y además, en LATAM, tu competencia real no es otra startup. Tu competencia es:

- el distribuidor grande que le deja todo a la mañana;
- el proveedor con quien ya trabaja;
- el supermercado mayorista;
- el grupo de WhatsApp de dueños de restaurantes;
- el “colega que me vende lo que le sobra”.

**Pregunta de pitch:**

> “¿Cómo evitas que el restaurante y el proveedor negocien directo después de 2 o 3 pedidos?”

Si no tienes una respuesta real, no tienes defensibilidad.

---

## 2. Por qué podría NO funcionar en LATAM específicamente

Te lo digo directo: en LATAM este modelo puede morir por la cultura B2B, la logística y la caja.

### 2.1. Tu “proveedor local” suele ser micro y no está listo para plataforma

Muchos proveedores locales son:

- pequeños;
- sin facturación completa;
- sin sistema de inventario;
- sin capacidad de empaque consistente;
- sin capacidad de entrega en ventanas cortas;
- sin disciplina de precios;
- operados por WhatsApp y memoria.

No es una API. Es un humano con un negocio familiar.

Si tu modelo depende de que 20 proveedores locales respondan rápido, cumplan stock, entreguen a tiempo y acojan una comisión, vas a sufrir.

---

### 2.2. La competencia real no es “falta de app”, es el distribuidor con crédito

Un restaurante pequeño en LATAM probablemente ya tiene un distribuidor que le resuelve varias cosas:

- entrega frecuente;
- factura;
- crédito;
- surtido amplio;
- relación personal;
- que no se le quede sin productos clave.

Si ese distribuidor le deja todo por $100 y le paga a 15 o 30 días, tu marketplace no gana por “ahorrar tiempo”. Gana solo si:

- es más barato;
- tiene mejores proveedores;
- entrega más rápido;
- tiene mejor calidad;
- o le da un servicio que el distribuidor no da.

Un 15% de comisión, si lo paga el restaurante, puede hacerte más caro.  
Si lo paga el proveedor, puede reducir su margen y no tener incentivos para competir.

---

### 2.3. La caja puede romperte antes que el producto

En LATAM, el restaurante pequeño suele querer crédito.  
El proveedor local suele querer cobro rápido.

Si el restaurante te paga a 30 días y el proveedor te exige pago al contado o a 7 días, tú te conviertes en un banco informal.

Y si encima tienes devoluciones, disputas, pedidos parciales y reclamos, tu flujo de caja se pone feo.

**Pregunta incómoda:**

> “¿Quién financia el float si el restaurante pide crédito y el proveedor necesita cash?”

Si la respuesta es “nosotros”, cuidado.

---

### 2.4. La logística no es un detalle, es el negocio

Un marketplace B2B de alimentos en LATAM no escala como SaaS. Escala como operación local.

Cada ciudad tiene:

- zonas;
- tráfico;
- seguridad;
- horarios;
- proveedores distintos;
- restaurantes distintos;
- costos de última milla distintos;
- densidad distinta.

Si no tienes densidad, cada pedido es caro.  
Si no tienes densidad, no puedes competir con un distribuidor que ya tiene rutas.

---

### 2.5. “Local” puede ser una limitación, no una ventaja

Si vendes “ingredientes locales”, puede ser atractivo. Pero también puede significar:

- estacionalidad;
- menos consistencia;
- menor capacidad de producción;
- más variabilidad de calidad;
- más dependencia de productores pequeños;
- menos disponibilidad 7 días a la semana.

Un restaurante necesita consistencia. Si el proveedor local no puede garantizar disponibilidad, el restaurante vuelve al distribuidor grande.

---

### 2.6. En LATAM, el B2B no paga por “plataforma”

El dueño de un restaurante pequeño no quiere “plataforma digital”. Quiere:

- que le llegue lo que pidió;
- que no le falte nada;
- que no le suban el precio sin avisar;
- que le resuelvan si algo llega mal;
- que le den condiciones de pago;
- que sea más barato o más confiable.

Si tu propuesta de valor es “digitaliza tu compra de insumos”, no es suficiente.  
Si tu propuesta es “te ahorro X por semana y te entrego mejor que tu proveedor actual”, eso puede funcionar.

---

## 3. Lo que tendría que ser verdad para que funcione: key assumptions

Esto no es opinión. Esto debe ser verdad y debes medirlo.

### 3.1. El restaurante gasta suficiente en las categorías que tú cubres

No sirve cualquier restaurante pequeño.

Tu ICP ideal debería tener gasto recurrente real en las categorías que tú vendes.

Debería ser verdad algo como:

- gasta al menos lo equivalente a $1,000-$3,000 mensuales en las categorías que cubres;
- realiza varios pedidos por semana, no uno al mes;
- tiene operación estandarizada: café, brunch, hamburguesas, cocina local, food truck, etc.

Si el restaurante gasta poco, tu CAC y tu logística no se pagan.

**Test:**

> “¿Este restaurante gastaría al menos $X al mes en productos que puedo servir?”

---

### 3.2. El restaurante repite, no solo prueba

La validación no es que un restaurante haga un pedido.  
La validación es que vuelva.

Debería ser verdad:

- 50% de los restaurantes piloto hacen 2+ pedidos por semana durante 4 semanas;
- o al menos 3+ pedidos en 2 semanas;
- o tu categoría representa 20-30% de su gasto en esas categorías a los 30 días.

Si solo compran una vez, no tienes adopción. Tienes curiosidad.

**Test:**

> “¿Cuántos restaurantes vuelven a comprar a los 7, 14 y 30 días?”

---

### 3.3. Los proveedores son confiables

Tu modelo no funciona con proveedores entusiastas pero caóticos.

Debería ser verdad:

- 90-95% de disponibilidad de stock en los productos clave;
- 90%+ de entregas a tiempo;
- menos de 5% de reclamos de calidad;
- aceptan un take rate de 8-15%;
- aceptan transparencia de precios;
- no se van a vender directo después del primer pedido.

Si el proveedor no cumple, tú pierdes al restaurante.

**Test:**

> “¿Qué porcentaje de pedidos sale completo y a tiempo? ¿Cuántos reclamos generamos?”

---

### 3.4. La logística es rentable con la densidad que tienes

Debería ser verdad:

- el costo de entrega es menor que un porcentaje manejable del ticket;
- hay suficiente concentración de pedidos por zona;
- puedes hacer rutas o entregas eficientes;
- el ticket promedio no es tan bajo que la entrega se coma la comisión.

Ejemplo:

- Si el ticket es $50 y la entrega cuesta $12, ya estás en problemas.
- Si el ticket es $150 y la entrega cuesta $10, todavía puedes respirar.

**Test:**

> “¿Cuál es el costo variable de servir un pedido? ¿Cuántos pedidos por ruta necesitas para que funcione?”

---

### 3.5. El 15% no es suficiente por sí solo, o tienes que justificarlo

Esta es una verdad incómoda:

> En muchos casos, 15% de comisión pura es alto si solo conectas.  
> Pero puede ser razonable si además entregas, garantizas calidad, resuelves disputas y das condiciones de pago.

Debería ser verdad:

- tu take rate total, incluyendo comisión + tarifa logística + posible servicio, deja margen positivo;
- el cliente entiende por qué paga;
- el proveedor entiende por qué acepta.

Si el 15% no genera valor claro, no funciona.

**Test:**

> “¿Qué recibe exactamente el cliente por el 15%? ¿Qué recibe el proveedor?”

---

### 3.6. El cobro no te rompe la caja

Debería ser verdad:

- el restaurante paga prepago, tarjeta, transferencia inmediata o a 7 días;
- o tienes capacidad real de asumir riesgo de crédito;
- o no extender crédito es parte del modelo.

Si tu modelo depende de que el restaurante pague a 30 días, no es una startup, es una operación con riesgo financiero.

**Test:**

> “¿Cuál es tu ciclo de caja? ¿Cuánto tiempo entre que pagas al proveedor y cobras al restaurante?”

---

### 3.7. No hay desintermediación masiva

Debería ser verdad:

- 70% del GMV sigue transaccionando por la plataforma 60 días después;
- los restaurantes no empiezan a comprar directo;
- los proveedores no se llevan los clientes;
- no se convierte en un simple directorio.

**Test:**

> “¿Cuántos pedidos se hacen directo después de conocerse? ¿Cómo lo mides?”

---

### 3.8. El tiempo ahorrado vale más que el costo

Tu hipótesis dice que el restaurante pierde tiempo. Ok. Pero debe ser verdad cuantitativamente.

Debería ser verdad:

- el dueño dedica al menos 30 minutos a 2 horas por semana a coordinar compras;
- tu solución reduce eso de forma real;
- el valor percibido es mayor que la tarifa.

Si le ahorras 10 minutos al mes y le cobras 15%, no funciona.

**Test:**

> “¿Cuánto tiempo ahorras por semana? ¿El cliente estaría dispuesto a pagar por ese ahorro?”

No con NPS. Con comportamiento: que siga pagando.

---

### 3.9. La categoría elegida no es imposible operativamente

“Ingredientes locales” es demasiado amplio.

Deberías empezar con categorías que sean manejables:

- no tan perecibles;
- no tan pesadas;
- no tan frágiles;
- con demanda recurrente;
- con proveedores capaces;
- con margen suficiente.

Ejemplos más manejables:

- café, té, condimentos, salsas, miel;
- panificados;
- embutidos/quesos de proveedores formales;
- conservas;
- productos de despensa con valor local.

Si empiezas con verduras frescas, carne, pollo y hortalizas, ya no eres marketplace. Eres distribuidor o empresa de logística con riesgo sanitario.

**Test:**

> “¿Qué categoría específica validas primero?”

Si respondes “todo”, no validas nada.

---

### 3.10. Los proveedores ven volumen incremental, no solo pérdida de margen

El proveedor local debe pensar:

> “Esta plataforma me da pedidos nuevos que no tendría.”

No:

> “Me quitan 15% y exponen mis precios a competidores.”

Debería ser verdad:

- el proveedor acepta la comisión porque el volumen extra compensa;
- no depende de pocos restaurantes grandes que pueden irse;
- no tiene incentivos para saltarse la plataforma.

---

## 4. El escenario donde fracasas rápido, y por qué

Tu fracaso rápido más probable no será por falta de inversores. Será por operaciones.

Vamos a narrarlo:

### Mes 1: Te sientes validado

Lanzas la app. Consigues:

- 20 restaurantes;
- 10 proveedores;
- 50 pedidos;
- algunos pedidos grandes;
- capturas de pantalla de dueños diciendo “me gustó”.

Piensas: “Ok, hay tracción.”

### Mes 2: Empiezan los problemas

- 25% de las entregas llegan tarde.
- 20% llegan incompletas.
- 10% generan reclamos de calidad.
- Un restaurante quiere devolver café malo.
- Otro proveedor no aceptó el 15% y sube el precio.
- Un restaurante te dice: “Ya hablé directo con el proveedor, ahora me cobra 10% menos.”
- Otro restaurante te pide crédito a 30 días.
- Tienes que adelantarles plata a proveedores.
- Tu soporte se vuelve call center.
- Tu logística cuesta más de lo estimado.

### Mes 3: El modelo no cierra

Ves los números:

- ticket promedio: $100;
- comisión: $15;
- logística: $10;
- pago: $3;
- devoluciones: $4;
- soporte: $3;
- margen: -5.

Y encima:

- churn de restaurantes alto;
- proveedores renuentes;
- CAC de $100 por restaurante;
- tiempo del fundador consumido por operaciones.

Ahí descubres que no tienes un marketplace. Tienes una empresa de coordinación de compras, logística y reclamos, sin densidad y sin ventaja clara.

### ¿Por qué fallaste?

Porque asumiste que el problema era falta de conexión digital.  
Pero el problema real era:

- disponibilidad;
- confianza;
- logística;
- calidad;
- precio;
- crédito;
- densidad.

Y tú no tenías control sobre ninguno de esos factores.

---

## 5. Si solo tuviera $10K para validar, esto haría

No construiría app.  
No contrataría equipo.  
No haría branding bonito.

Haría validación concierge, manual, con cobro desde el día 1.

La regla:

> Si no puedes validar esto manualmente, una app no te va a salvar.

---

## Fase 1: Elige un micro-muerto y una categoría

No hagas “restaurantes pequeños con proveedores locales”. Eso es demasiado.

Haz esto:

- 1 ciudad;
- 1 zona de 2-4 km;
- 8-12 restaurantes;
- 2 categorías máximo;
- 10-15 SKUs.

Ejemplos de wedge:

Opción A:

- Cafeterías / brunch / pequeños restaurantes;
- productos: café, té, azúcar, salsas, panificados, embutidos, quesos.

Opción B:

- Comida local / comida por encargo / food trucks;
- productos: salsas, conservas, café, miel, embutidos, quesos, panificados.

Evita al inicio:

- verduras frescas;
- carne;
- pollo;
- productos muy perecibles;
- productos muy pesados;
- cadena de frío compleja.

Tu primera validación no puede depender de que tú domines logística pesada.

---

## Fase 2: Consigue 5-8 proveedores, no 50

Busca proveedores que cumplan:

- facturan o pueden facturar;
- entregan en 4-24 horas;
- tienen stock de 5-10 productos;
- aceptan una comisión de 8-12% o una tarifa por pedido;
- no necesitan que les expliques qué es un precio;
- pueden operar por WhatsApp.

No persigas al proveedor “local” más bonito si no puede operar con consistencia.

Preguntas clave:

> “Si te doy 10 pedidos nuevos por semana, ¿estás dispuesto a aceptar 8-10% de comisión?”

> “¿Puedes confirmar stock en 15 minutos?”

> “¿Puedes entregar antes de las 11 de la mañana 4 días por semana?”

> “¿Qué pasa si un restaurante recibe algo mal?”

Si no pueden responder, no son tu proveedor piloto.

---

## Fase 3: 20 entrevistas y 5 pre-commits

Antes de operar, habla con 20 restaurantes.

Preguntas:

1. ¿Qué compran cada semana?
2. ¿A quién le compran?
3. ¿Cuánto gastan?
4. ¿Cuánto tiempo pierden coordinando compras?
5. ¿Qué les molesta más: precio, entrega, calidad, faltantes, crédito?
6. ¿Si te ahorro 1 hora por semana y te entrego en 4 horas, cuánto pagarías por pedido?
7. ¿Aceptarías un 10% de tarifa? ¿Un 15%? ¿Una tarifa fija?
8. ¿Qué tendría que pasar para que cambieras de proveedor?
9. ¿Pagas prepago o pides crédito?
10. ¿Qué porcentaje de su gasto actual estaría dispuesto a mover a tu servicio?

Tu objetivo no es que te digan “me parece bien”.  
Tu objetivo es que te digan:

> “Ok, pruébalo 30 días. Si funciona, te compro.”

Consigue 5 restaurantes que acepten un piloto de 30 días.

Aún mejor: que paguen la primera orden o den un anticipo.

Si nadie paga, no tienes cliente.

---

## Fase 4: Piloto manual de 4-6 semanas

No uses app.

Usa:

- WhatsApp Business;
- Google Sheets;
- Google Forms;
- catálogo simple;
- formulario de pedido;
- seguimiento manual.

Tú o una persona coordina todo:

- recibe pedido;
- confirma stock;
- confirma precio;
- coordina entrega;
- cobra al restaurante;
- paga al proveedor;
- resuelve reclamos.

Esto es deliberadamente feo. Debe ser feo para que sientas la operación.

### Cobro

No valides “gratis”. Cobra desde el día 1.

Modelo sugerido:

- 8-12% de comisión, o
- tarifa fija por pedido, o
- comisión más tarifa logística passthrough.

Si quieres validar el 15%, hazlo en una subcelda:

- 3 restaurantes con 15%;
- 2 con 8-10% o tarifa fija.

Pero no te enamores del 15%.

Si no pagan 8%, no van a pagar 15%.

### Pago

Lo ideal:

- restaurante paga antes de despachar;
- o paga al recibir;
- tú pagas al proveedor a T+2 o T+7.

No entres al juego de crédito a 30 días en esta fase.

---

## Fase 5: Métricas que decidirían si continúas o mato

Lleva registro de:

### Demanda

- número de restaurantes activos;
- pedidos por restaurante por semana;
- ticket promedio;
- share of wallet: % de su gasto en esas categorías;
- reorder a 7, 14 y 30 días.

### Operación

- % de pedidos completos;
- % de entregas a tiempo;
- % de reclamos;
- tiempo de resolución de reclamos;
- costo por entrega;
- costo variable por pedido.

### Económico

- CAC por restaurante;
- margen bruto por pedido;
- margen bruto por restaurante al mes;
- payback de CAC;
- cash conversion.

### Relación

- NPS;
- intentos de desintermediación;
- proveedores que quieren irse;
- restaurantes que quieren irse.

---

## Criterios para seguir escalando

Con $10K, no necesitas unicorno. Necesitas evidencia.

Te tomaría en serio si a las 4-6 semanas ves:

- 5 restaurantes activos;
- 2+ pedidos por semana por restaurante durante 4 semanas;
- ticket promedio que permite cubrir logística;
- margen bruto positivo después de variable costs;
- 90%+ de pedidos completos;
- 85%+ de entregas a tiempo;
- 70%+ de GMV sigue pasando por tu canal;
- NPS > 40;
- 80% dice que seguiría pagando;
- CAC manual no absurdo: recuperable en menos de 60-90 días si la retención existe.

Si no ves eso, no es “ajustar el modelo”. Es matar o pivotar fuerte.

---

## Criterios para matar o pivotar

Mataría o pivotaría si:

- menos de 3 restaurantes repiten;
- el costo de entrega supera 25-30% del ticket;
- los proveedores no aceptan la tarifa;
- los restaurantes solo compran cuando hay descuento;
- la calidad/entrega es caótica;
- todos piden crédito a 30 días;
- la desintermediación es alta;
- tu fundador gasta el 80% del tiempo apagando incendios.

Posibles pivotes:

1. **De marketplace a servicio de compras**  
   Tú compras a proveedores locales y vendes tú al restaurante. Ya no eres marketplace; eres comprador/distribuidor.

2. **De muchos productos a una categoría**  
   Ej: solo café local. Solo panificados. Solo salsas/condimentos.

3. **De comisión a tarifa logística + servicio**  
   Cobra una tarifa clara por entrega y una tarifa menor por matching.

4. **De marketplace a agregador premium**  
   En vez de “proveedores locales”, vendes “insumos locales seleccionados con garantía de entrega y calidad”.

5. **De restaurante pequeño a ICP más específico**  
   Cafeterías, food trucks, brunch, restaurantes con menú estandarizado, no “todo restaurante pequeño”.

---

## Presupuesto de $10K

No lo gastes en app.

### Descubrimiento y entrevistas: $1,500

- transporte;
- muestras;
- reuniones con dueños;
- pequeños incentivos no distorsivos;
- impresiones/catálogo simple.

### Operación del piloto: $3,500

- entregas;
- empaque;
- combustible;
- motobike/bike si aplica;
- materiales mínimos;
- eventual apoyo operativo.

### Incentivos: $1,500

- primera entrega gratis;
- crédito de $10-$20;
- no descuentos grandes, porque distorsionan la validación.

### Legal y pagos: $1,500

- contratos simples;
- cuenta de pagos;
- términos básicos;
- protección mínima para disputas.

### Buffer: $2,500

- devoluciones;
- adelantarle al proveedor;
- pedidos cancelados;
- imprevistos.

Total: $10,000.

---

## Las 10 preguntas de pitch que tienes que poder responder

Si no puedes responder esto con números, no presentes.

1. ¿Quién paga el 15%? ¿El proveedor, el restaurante, o ambos?

2. ¿Cuánto gasta por mes tu restaurante ideal en las categorías que tú cubres?

3. ¿Cuál es tu ticket promedio?

4. ¿Cuál es tu costo de entregar un pedido?

5. ¿Cuál es tu margen bruto por pedido?

6. ¿Quién entrega?

7. ¿Quién responde si llega mal o tarde?

8. ¿Por qué no lo resuelve WhatsApp + proveedor actual?

9. ¿Por qué no lo resuelve un distribuidor grande?

10. ¿Cómo evitas que el restaurante y el proveedor se compren directo?

---

## Mi veredicto

No te tomaría en serio si me dices:

> “Es un marketplace que conecta restaurantes pequeños con proveedores locales y cobra 15%.”

Te tomaría en serio si me dices algo como:

> “Somos un servicio de abastecimiento para [café/brunch/food trucks] en [zona específica], con [10-15 SKUs] de alta rotación, [proveedores locales fiables], entrega en [4 horas], margen bruto de [X%], y evitamos la desintermediación porque [controlamos la operación / garantizamos SLA / ofrecemos datos / manejamos pagos / proveemos productos exclusivos / logísticas superiores].”

Tu mayor riesgo no es que la app no funcione.  
Es que no exista un negocio detrás que justifique una app.