# GPT-6.1 Terra — strategy/business_model_validation

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 36.376s | tokens_per_second: 64.1
- input_tokens: 165 | output_tokens: 2332

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

Voy a ser directo: **tu hipótesis todavía no describe un negocio; describe una molestia**. Que un dueño pierda tiempo llamando no significa que pague por resolverlo, ni que acepte cambiar proveedores que ya conoce y le dan crédito.

## 1. Los cinco riesgos principales

### 1. El problema no es suficientemente caro

¿Cuántas horas pierde realmente cada restaurante? ¿Quién hace los pedidos? ¿Cuánto pagaría por recuperar ese tiempo?

Si hoy resuelve todo por WhatsApp en 20 minutos, no estás eliminando un dolor urgente. Estás intentando cambiar un hábito por una mejora marginal.

**Pregunta de VC:** ¿Cuántos restaurantes te han pagado por resolver esto, no cuántos te dijeron que “usarían la app”?

### 2. El 15% puede destruir la economía del proveedor

Si un pedido vale $100 y cobras 15%, quedan $85 para el proveedor antes de sus costos. Si su margen bruto era 20%, pasa de $20 a $5 antes de reparto, cobranza y otros gastos.

Es un ejemplo, no una afirmación sobre todos los proveedores. Pero ilustra el problema: **tu comisión puede comerse la mayor parte de su margen**. Si se la trasladas al restaurante, este podría comprar más caro que por teléfono.

**Pregunta de VC:** ¿Quién paga realmente ese 15% y por qué aceptaría hacerlo de forma sostenida?

### 3. La logística y la calidad pueden comerte vivo

No estás vendiendo libros digitales. Los ingredientes llegan tarde, se dañan, varían de calidad y a veces faltan. Un fallo tuyo puede dejar a un restaurante sin menú.

Aunque el proveedor haga la entrega, el cliente probablemente te responsabilizará a ti. Atención al cliente, devoluciones y reposiciones pueden convertir una comisión atractiva en una pérdida.

**Pregunta de VC:** ¿Quién paga cuando llegan tomates malos a las 7 a. m. y el restaurante necesita abrir al mediodía?

### 4. El marketplace puede desintermediarse

Tú presentas al restaurante y al proveedor. En la segunda compra, ambos hacen el pedido por WhatsApp y se ahorran tu comisión.

**Pregunta de VC:** ¿Qué valor aportas en la décima transacción para justificar que siga pasando por ti? Si la respuesta es “una interfaz cómoda”, probablemente no alcanza.

### 5. Conseguir liquidez local puede ser lentísimo

Necesitas suficientes proveedores, con disponibilidad y precios competitivos, cerca de suficientes restaurantes que compren con frecuencia. Si falta oferta, no atraes demanda; si falta demanda, los proveedores no actualizan precios ni inventario.

**Pregunta de VC:** ¿Puedes dominar una zona y una categoría antes de gastar dinero en expandirte, o necesitas cobertura masiva desde el primer día?

## 2. ¿Por qué podría no funcionar en LATAM?

LATAM no es un solo mercado. Lo que pase en una ciudad no demuestra nada automáticamente sobre otra. Pero hay fricciones que debes investigar localmente:

- **WhatsApp ya es tu competidor.** Es gratis, conocido y permite negociar, mandar fotos, reclamar y pedir fiado. Tu producto tiene que ser claramente mejor, no solo más digital.
- **El crédito puede importar más que la conveniencia.** Un proveedor conocido puede cobrar días después. Si tu plataforma exige pago inmediato, podrías empeorar la situación del restaurante.
- **Informalidad y facturación.** Algunos participantes pueden tener dificultades o incentivos limitados para operar digitalmente, emitir comprobantes o aceptar ciertos medios de pago. Depende del país y del proveedor.
- **Precios y disponibilidad cambiantes.** Un catálogo desactualizado genera pedidos imposibles de cumplir y destruye confianza.
- **Reparto fragmentado y costoso.** Distancias, tráfico, cadena de frío y pedidos pequeños pueden hacer inviable la entrega, especialmente con tu comisión como único ingreso.
- **Relaciones personales.** El proveedor habitual no solo vende producto: puede dar prioridad cuando escasea, aceptar cambios de último minuto y financiar al cliente.

La pregunta incómoda es: **¿estás compitiendo contra llamadas telefónicas o contra una relación comercial completa?**

## 3. ¿Qué tendría que ser verdad?

Estas son las apuestas que debes demostrar, no asumir:

1. **El dolor es frecuente y costoso.** Los restaurantes hacen pedidos con suficiente frecuencia y valoran resolverlos más que el costo de cambiar de hábito.
2. **Hay disposición real a pagar.** Alguien acepta el 15% sin que el precio final deje de ser competitivo. Si nadie lo acepta, necesitas otra estructura de ingresos.
3. **Los proveedores tienen capacidad e incentivos para cumplir.** Mantienen precios y disponibilidad razonablemente actualizados y entregan lo prometido.
4. **La logística funciona con costos reales.** Después de entrega, pagos, soporte, pérdidas y devoluciones, cada pedido deja contribución positiva.
5. **Existe una razón para permanecer en la plataforma.** Por ejemplo, consolidación de pedidos, crédito, resolución de problemas o acceso constante a mejores proveedores. No basta con haber hecho la presentación inicial.
6. **Puedes concentrar oferta y demanda.** Una zona pequeña tiene suficientes restaurantes y proveedores para generar compras repetidas.
7. **Puedes adquirir clientes por menos de lo que dejan de contribución.** Una operación rentable por pedido aún puede ser un mal negocio si captar restaurantes cuesta demasiado.

## 4. El escenario de fracaso rápido

Lanzas en una ciudad, incorporas 30 proveedores y consigues 50 restaurantes interesados. Gastas los $10K en una app y promoción.

Llegan los primeros pedidos:

- Los proveedores suben precios para absorber tu comisión.
- Algunos productos no están disponibles.
- Las entregas se retrasan y tu equipo resuelve problemas manualmente.
- Los restaurantes comparan con su proveedor habitual y vuelven a WhatsApp.
- Los pocos clientes satisfechos compran directamente al proveedor después de la primera transacción.

En dos meses tienes usuarios registrados, pero pocos pedidos repetidos y una pérdida por cada uno. **Fracasarías porque construiste tecnología antes de demostrar disposición a pagar, cumplimiento y repetición.**

## 5. ¿Qué haría con $10K para validar?

Asumo **$10.000 USD**, seis semanas, una zona pequeña y una categoría concreta —por ejemplo, frutas y verduras—. No construiría una app. Operaría por WhatsApp y una hoja de cálculo.

### Presupuesto

| Uso | Monto |
|---|---:|
| Entrevistas y reclutamiento de restaurantes | $2.500 |
| Captación y verificación de proveedores | $1.500 |
| Coordinación y prueba de entregas | $3.500 |
| Operación manual, pagos y soporte | $1.500 |
| Reserva para incidencias | $1.000 |
| **Total** | **$10.000** |

Registraría todos los costos reales, aunque los cubra el presupuesto de prueba. **No subsidiaría secretamente los precios ni ocultaría la comisión:** eso fabricaría una demanda que desaparece cuando se acaba el dinero.

### La prueba

**Semanas 1–2: comprobar el dolor.** Entrevistaría al menos a 20 restaurantes y 10 proveedores. Pediría ver pedidos recientes, precios, frecuencia, tiempos de entrega y condiciones de pago. No preguntaría “¿usarías esta app?”. Preguntaría: “¿Qué compraste esta semana, a quién y por qué?”

**Semanas 3–6: vender y cumplir.** Intentaría conseguir al menos 10 restaurantes que hagan pedidos reales y pagados. Presentaría por adelantado las condiciones, incluido el 15%, dejando claro quién lo absorbe. Gestionaría disponibilidad, entrega, reclamos y cobro manualmente.

### Criterios para decidir

Son umbrales iniciales para aprender, no prueba estadística de un mercado:

- **Adopción:** al menos 10 restaurantes hacen un pedido pagado.
- **Repetición:** al menos la mitad vuelve a comprar durante la prueba.
- **Economía:** los pedidos dejan contribución positiva con la comisión del 15%, incluyendo costos variables reales de reparto, pagos, soporte e incidencias.
- **Cumplimiento:** los restaurantes reciben lo acordado con suficiente fiabilidad como para volver a comprar.
- **Proveedor:** varios proveedores aceptan seguir bajo las condiciones reales, sin precios artificiales.
- **Desintermediación:** investigo si restaurante y proveedor siguen comprando fuera de la plataforma y por qué.

Si hay interés, pero nadie acepta el 15%, **no validaste el modelo de negocio**. Si aceptan la comisión, pero no repiten, **no validaste el valor**. Si repiten, pero pierdes dinero en cada entrega, **no validaste la operación**.

Mi pregunta final de pitch sería: **¿qué evidencia tienes de que estás creando valor por el que alguien paga repetidamente, en vez de añadir un intermediario caro a una cadena que ya funciona?**