# Claude Opus 5.5 — strategy/business_model_validation

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 70.232s | tokens_per_second: 89.1
- input_tokens: 290 | output_tokens: 6258

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

# Modo VC escéptico activado

Antes de las 5 preguntas, lo que te diría en los primeros 30 segundos del pitch:

**"Tu hipótesis describe una molestia, no un dolor. Y cobras 15% por resolver una molestia en una industria que opera con márgenes de 3-8%. Convénceme de que no estoy perdiendo el tiempo."**

---

## 1. Los 5 riesgos principales

### Riesgo #1: El 15% es matemáticamente insostenible
Haz las cuentas:
- Un restaurante pequeño gasta 28-35% de sus ventas en insumos y tiene margen neto de 3-10% (si le va bien).
- Un proveedor de verduras o carnes opera con margen bruto de 10-25%.
- **Tu comisión del 15% se come casi todo el margen del proveedor.** Si la paga el restaurante, le subes el costo de insumos 15% y le borras la utilidad.

Los marketplaces B2B de alimentos que funcionan suelen cobrar entre 2% y 8%, o compran y revenden inventario para capturar margen. ¿Por qué tú puedes cobrar el doble? ¿Qué valor entregas que justifique eso?

### Riesgo #2: Desintermediación (el asesino de marketplaces B2B)
Esta es la pregunta que más te van a hacer: **¿qué impide que, después del tercer pedido, el restaurante le escriba directo al proveedor por WhatsApp y ambos se ahorren tu 15%?**

En B2C (Uber, Airbnb) la transacción es esporádica y con desconocidos. Aquí es **recurrente, entre las mismas dos partes, cada semana**. Es el escenario perfecto para que te saquen de la ecuación. Tu propio éxito (conectarlos bien) acelera tu muerte.

### Riesgo #3: Tu hipótesis probablemente ataca el dolor equivocado
"Pierden tiempo llamando a proveedores." ¿Lo validaste o lo asumiste? Lo que suele importarle de verdad a un dueño de restaurante pequeño:
1. **Precio**: quiere pagar menos.
2. **Crédito**: el proveedor le fía a 15-30 días. Esto es enorme.
3. **Confiabilidad**: que llegue a tiempo y con la calidad pedida.
4. **Devoluciones fáciles**: "este tomate está malo, me lo cambias mañana."

"Ahorrar tiempo" casi nunca está en el top 3. Y la relación con su proveedor de toda la vida ya le resuelve crédito, confianza y devoluciones. Tú no.

### Riesgo #4: No controlas la operación, pero cargas con la culpa
Si eres marketplace puro (no tocas producto ni logística):
- El proveedor local llega tarde → el restaurante te culpa a ti.
- La lechuga llega marchita → te culpa a ti.
- El proveedor no actualiza su inventario y no tiene lo que ofreció → te culpa a ti.

Los proveedores locales pequeños no tienen catálogos digitales, inventario en tiempo real ni precios estables (cambian según la cosecha y la central de abasto de esa mañana). Vas a vender una experiencia digital montada sobre una operación analógica y caótica.

### Riesgo #5: Unit economics de un negocio hiperlocal y de ticket bajo
- **CAC alto**: a los dueños de fondas y restaurantes pequeños no los adquieres con Instagram ads. Necesitas vendedores de campo, visitas presenciales, demos. Eso cuesta.
- **Ticket bajo**: un pedido de $150-400 USD con 15% te deja $22-60 brutos, antes de pagos, soporte y reclamos.
- **Mortalidad alta**: una proporción enorme de restaurantes pequeños cierra en sus primeros años. Tu cohorte de clientes se muere sola.
- **Densidad**: necesitas liquidez barrio por barrio. Escalar a otra ciudad es casi empezar de cero.

---

## 2. Por qué podría NO funcionar en LATAM específicamente

**a) WhatsApp ya es tu competidor y ya ganó.**
El restaurante ya hace pedidos "digitales": un mensaje de voz a su proveedor a las 6 am. Costo: cero. Fricción: casi cero. Tu app tiene que ser mejor que eso, no mejor que llamar por teléfono.

**b) Informalidad.**
Muchos proveedores no facturan, cobran en efectivo y no quieren dejar rastro. Una plataforma digital con pagos trazables es, para ellos, una amenaza fiscal, no un beneficio. ¿Cómo cobras tu 15% si la transacción se paga en efectivo al momento de la entrega?

**c) El crédito informal es el verdadero producto.**
"Don José me fía hasta el viernes." Si tu plataforma exige pago por adelantado o al momento, eres peor que la alternativa actual. Si ofreces crédito, ya no eres una app de pedidos, eres una fintech con riesgo crediticio, y eso requiere otro capital y otro equipo.

**d) La central de abastos.**
Muchos dueños o sus empleados van personalmente a la central (Central de Abasto en CDMX, Corabastos en Bogotá, CEAGESP en São Paulo) porque ven, tocan y negocian el producto. Para ellos eso no es "perder tiempo", es control de calidad y precio.

**e) Hay cadáveres y heridos en este espacio.**
Investiga a fondo **Frubana** (B2B de frutas y verduras para restaurantes en Colombia, México y Brasil). Levantó cientos de millones de dólares, tuvo despidos masivos y salió de mercados. También revisa **Cayena** (Brasil) y **Choco** (Europa, app de pedidos restaurante-proveedor que también levantó mucho y luego tuvo que recortar). Si no puedes explicar en una frase por qué tú no vas a terminar igual, no estás listo para el pitch.

**f) Volatilidad.**
Precios de insumos que cambian semanalmente, inflación (Argentina es el caso extremo) y monedas inestables hacen muy difícil mantener catálogos y precios confiables en una app.

**g) Sensibilidad al precio vs. "local".**
"Ingredientes locales" suena a propuesta premium. El restaurante pequeño latinoamericano promedio compra lo más barato que cumpla. ¿Tu mercado es la fonda de barrio o el bistró farm-to-table de Palermo, Roma Norte o Chapinero? Son negocios completamente distintos, y el segundo es mucho más pequeño.

---

## 3. Qué tendría que ser verdad (key assumptions)

Formúlalas como hipótesis falsables, con números:

| # | Supuesto | Cómo se ve "verdadero" |
|---|---|---|
| 1 | El dolor es real y prioritario | >40% de restaurantes entrevistados lo menciona **sin que tú lo sugieras** como top 3 de problemas |
| 2 | Pagarán por resolverlo | Restaurantes o proveedores aceptan un take rate que cubra tus costos (probablemente 5-10%, no 15%) |
| 3 | Hay retención en plataforma | >60% de restaurantes repiten pedido en el mes 3 **a través de ti**, no por fuera |
| 4 | No te desintermedian | La plataforma da algo que no obtienen yendo directo: crédito, consolidación de proveedores, mejor precio por volumen, garantía de calidad |
| 5 | Los proveedores pueden operar digitalmente | Actualizan precios y disponibilidad, y cumplen >90% de pedidos a tiempo |
| 6 | Unit economics funcionan por barrio | LTV/CAC > 3 dentro de una sola zona densa antes de expandirte |
| 7 | Hay suficiente oferta "local" | Existen suficientes productores locales con volumen y consistencia para abastecer restaurantes cada semana |

**El supuesto #4 es el más importante.** Si no tienes una respuesta sólida, el resto no importa.

---

## 4. El escenario de fracaso rápido

Así se ve, y es el escenario más probable si ejecutas el plan tal como lo describiste:

- **Mes 1-2:** Consigues 15 proveedores y 50 restaurantes con mucho esfuerzo de campo. Primeros pedidos. Te emocionas con el GMV.
- **Mes 2-3:** Problemas de cumplimiento. Un proveedor no llega, otro manda producto de baja calidad. Atiendes reclamos por WhatsApp a las 7 am. Tú eres el servicio al cliente de operaciones que no controlas.
- **Mes 3-4:** Los restaurantes que tuvieron buena experiencia ya tienen el número del proveedor. Empiezan a pedirle directo. El proveedor acepta encantado porque se ahorra 15%. **Tus mejores matches son los primeros en irse.**
- **Mes 4-5:** El GMV se estanca o cae. Bajas la comisión a 5% para retener. Ahora tus unit economics no cubren ni el costo de adquisición.
- **Mes 6:** Te quedan los restaurantes que nadie más quiere atender (malos pagadores, pedidos chicos) y los proveedores que nadie más quiere (poco confiables). **Selección adversa.** Se acaba el runway.

**Causa raíz:** construiste un directorio con cobro de peaje, no un producto que genere valor recurrente.

---

## 5. Con solo $10K para validar

**Regla #1: No construyas la app.** Gastar $10K en desarrollo es la forma más cara de descubrir que nadie la quiere.

### Fase 1: Discovery (semanas 1-3) | ~$1,000
- 40-50 entrevistas presenciales con dueños de restaurantes pequeños en **un solo barrio**.
- 15-20 entrevistas con proveedores.
- **No menciones tu solución.** Pregunta: "¿Cuéntame cómo hiciste tu último pedido de insumos?", "¿Qué fue lo peor que te pasó con un proveedor este mes?", "¿Cuánto pagas, cómo pagas, a cuántos días?"
- Gasto: transporte, cafés, comidas en los mismos restaurantes (la mejor forma de que te den 20 minutos).

**Criterio para matar o seguir:** si "pierdo tiempo pidiendo" no aparece espontáneamente en el top 3 de al menos un tercio de los entrevistados, tu hipótesis está muerta. Pivotea hacia el dolor que sí apareció (probablemente precio o crédito).

### Fase 2: Concierge MVP (semanas 4-10) | ~$6,000
- Un número de WhatsApp Business + Google Sheets. **Tú eres la "app".**
- 10-15 restaurantes y 5-8 proveedores en un radio pequeño.
- Los restaurantes te mandan su pedido; tú lo consolidas, lo envías a proveedores, das seguimiento a la entrega y resuelves problemas.
- **Cobra desde el día 1.** Prueba diferentes take rates (5%, 10%, 15%) con diferentes clientes. Prueba quién paga: restaurante, proveedor o ambos.
- Presupuesto: pequeño ingreso para ti o un ayudante, transporte para resolver incidencias, fondo para garantizar calidad (reponer pedidos malos y aprender cuánto cuesta realmente).

**Métricas que importan:**
- Retención semanal de pedidos en semanas 6-10.
- Cuántos restaurantes intentan pedir por fuera (pregúntales directamente al final).
- Take rate máximo que aceptan sin irse.
- Tasa de cumplimiento de proveedores.
- Horas que te toma operar cada pedido (tu costo real de servicio).

### Fase 3: Probar el moat (semanas 8-12) | ~$2,000
Prueba qué hace que se queden **aunque podrían ir directo**:
- **Consolidación:** un solo pedido y una sola factura para 5 proveedores.
- **Crédito:** ¿pagan más por pagar a 15 días? (Pruébalo en pequeño, con dinero que puedas perder.)
- **Precio por volumen:** agrega la demanda de 15 restaurantes y negocia mejor precio.
- **Garantía de calidad:** "si llega mal, lo reponemos en 2 horas."

### Reserva | ~$1,000
Para imprevistos. Siempre los hay.

**Lo que quieres llevar al pitch después de esto:**
> "Durante 10 semanas operé manualmente para 15 restaurantes. 11 siguen pidiendo cada semana. El take rate sostenible es X%. Lo que los retiene no es el ahorro de tiempo sino [Y]. Esta es la evidencia."

Eso vale más que cualquier deck.

---

## Mi veredicto como VC

**Hoy no invierto.** No porque el espacio sea malo, sino porque el modelo como está planteado (marketplace puro, 15%, propuesta de "ahorro de tiempo") tiene un defecto estructural de desintermediación y una comisión que la industria no soporta.

**Donde sí me interesaría escucharte:**
- **SaaS para proveedores:** herramienta de pedidos, cobranza y catálogo por suscripción. Si el proveedor la usa para todos sus clientes, la desintermediación deja de importar.
- **Embedded finance:** el crédito a restaurantes como producto central, con el marketplace como canal para originar préstamos.
- **Compra agrupada:** agregas demanda de muchos restaurantes pequeños para que accedan a precios de cadena grande. Ahí el valor es claro y medible: "pagas 12% menos."
- **Modelo con inventario:** compras y revendes, controlas calidad y capturas margen. Es más capital-intensivo, pero el valor no se puede saltar.

Vuelve cuando tengas datos de retención. Mientras tanto, la pregunta que tienes que poder responder en una frase es:

**"¿Por qué el restaurante seguirá usando tu plataforma en el pedido número 20, si ya tiene el WhatsApp del proveedor desde el pedido número 2?"**