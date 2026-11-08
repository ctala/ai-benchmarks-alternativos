# Kimi K2.7 Code — strategy/business_model_validation

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 51.791s | tokens_per_second: 57.7
- input_tokens: 201 | output_tokens: 2987

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

Bien. Deja de lado la presentación. Te voy a tratar como a un founder que acaba de entrar a mi oficina con una idea “de plataforma” sin tener ni idea de cómo se mueve la comida en la calle. Aquí va.

---

## 1. Los 5 riesgos principales de tu modelo

**1. El marketplace es una trampa de doble captación en un mercado B2B de baja frecuencia**
No es como pedir comida a domicilio. Un restaurante pequeño no compra tomates 3 veces al día en una app. Compra cada 1-3 días, pero con el mismo proveedor, siempre. Eso significa que tu plataforma tiene muy pocas transacciones por usuario y un enorme incentivo a que ambos lados te evadan después de la primera compra. Si el restaurante y el proveedor se conocen, ¿por qué pagarían tu 15% dos veces?

**2. Tu comisión del 15% es probablemente imposible de cobrar**
En LATAM, los márgenes de restaurantes pequeños suelen estar entre 5-15%. Un 15% de comisión no es un “pequeño fee”, es una amputación. Y si se lo cobras al proveedor, lo más probable es que simplemente suba el precio y el restaurante compare con su proveedor habitual al que le paga en efectivo, sin IVA y con crédito de 7-15 días. Tu “conveniencia digital” no compite solo contra el teléfono: compite contra precio, crédito y confianza.

**3. No estás resolviendo el problema más doloroso: la logística y el crédito**
Tu hipótesis es “pierden tiempo llamando”. Eso es un problema de segundo orden. El verdadero dolor es: ¿llega la mercancía a tiempo? ¿Está en buen estado? ¿Me fían? ¿Me aceptan pago en 8 días? Tu app no resuelve eso magicamente. De hecho, lo empeora porque introduces un intermediario entre quien produce y quien recibe.

**4. Fragmentación asimétrica y saturación de la oferta**
Para ser útil, necesitas muchos proveedores. Pero en LATAM la oferta local de ingredientes suele ser muy fragmentada, informal y de capacidad limitada. Un campesino que vende 20 kg de aguacate a la semana no puede escalar ni cumplir con la demanda de 30 restaurantes. Y si usas mayoristas disfrazados de “locales”, entonces no eres diferente a Cornershop para restaurantes.

**5. Captura de valor débil y alto costo de retención**
Incluso si consigues que usen la app una vez, no hay lock-in. No hay datos que no puedan replicar en WhatsApp. No hay financiamiento. No hay logística propia. No hay exclusividad. Terminas siendo un catálogo caro que ambos lados abandonan en cuanto hacen match.

---

## 2. ¿Por qué podría NO funcionar específicamente en LATAM?

**Porque LATAM no compra ingredientes como compra ropa en Mercado Libre.**

- **El efectivo y el crédito informal dominan.** Muchos restaurantes pequeños no pagan con tarjeta. Pagan “a crédito” con su proveedor de toda la vida. Tu app con pago inmediato les quita liquidez, no se la da.
- **WhatsApp es el verdadero OS del comercio.** El tendero, el proveedor de pollo, el de verduras… todos operan por WhatsApp, con notas de voz, fotos y confianza personal. Tu app tiene que ser significativamente mejor que eso para vencer la inercia. Hasta ahora, no lo es.
- **La informalidad te mata la unit economics.** Si el proveedor no factura, no quiere pagar comisión, no tiene cuenta bancaria formal, no puede recibir transferencias, tu plataforma se atora.
- **La logística urbana es un infierno.** Tráfico, inseguridad, falta de direcciones formales, horarios de entrega imposibles en ciudades como CDMX, Bogotá, Lima. Si no controlas la última milla, fracasas por culpa de terceros.
- **El “local” suena bonito, pero escala mal.** El restaurante quiere consistencia: mismo tamaño, mismo sabor, mismo precio. El proveedor local suele ser inestable por temporada, clima, capacidad. Eso genera quejas, devoluciones y churn.
- **Cultura de relación vs. transacción.** El dueño del restaurante no elige al proveedor por la app. Lo elige porque le conoce, le debe un favor, le fía, o porque son familia. Tu “eficiencia digital” no compite con eso.

---

## 3. ¿Qué tendría que ser verdad para que funcione? (Key assumptions)

Para no ser un cadáver en 12 meses, *todas* estas cosas tienen que ser ciertas, no solo algunas:

1. **Que exista un segmento de restaurantes suficientemente grande que realmente valore el tiempo más que el precio/crédito.** Y que esté dispuesto a cambiar su comportamiento de compra.
2. **Que haya proveedores locales con capacidad real de surtir a múltiples restaurantes de forma consistente** (calidad, volumen, puntualidad, trazabilidad).
3. **Que puedas cobrar una comisión sostenible sin que el restaurante o el proveedor te evadan.** Eso probablemente requiera que agregues valor real que no se pueda replicar fuera: logística, crédito, financiamiento, inventario garantizado.
4. **Que la densidad geográfica sea suficiente** para que una ruta de entrega pueda servir a muchos restaurantes con bajo costo logístico. Si no hay densidad, pierdes plata en cada entrega.
5. **Que el pago digital sea aceptado y preferido** por ambas partes. En LATAM, eso no es obvio.
6. **Que la alternativa (llamar/ WhatsApp) sea realmente peor y más cara** que tu solución, inclusive con tu comisión incluida.
7. **Que puedas retener a ambos lados sin que hagan la transacción directamente después del primer match.** Necesitas un mecanismo de retención real.

Si falla una sola de estas, el modelo se desploma.

---

## 4. Escenario de fracaso rápido: ¿cómo se ve y por qué?

**Mes 1-3:** Lanzas la app. Consigues 50 restaurantes y 30 proveedores. Haces un par de transacciones con descuentos agresivos.

**Mes 4-6:** Los restaurantes empiezan a quejarse: la lechuga llegó marchita, el proveedor llegó 2 horas tarde, el precio subió, no les fían. Los proveedores se quejan de que les cobras 15% y les pagas tarde. Algunos restaurantes piden crédito; tú no se lo puedes dar.

**Mes 7-9:** El 60% de los restaurantes descubren que pueden llamar al proveedor directamente, negociar mejor precio y pagarle en efectivo a 15 días. Te evaden. Tu GMV se desploma. Gastaste en adquisición de usuarios para construir una agenda telefónica ajena.

**Mes 10:** Cierras o pivoteas a “software para proveedores”, que tampoco tienes.

**Por qué fracasaste:** Porque resolviste un problema que *tú* creías que era importante (llamadas), no el problema que el mercado paga por resolver (confiabilidad, crédito, logística, precio). Y porque tu modelo de comisión no tiene defensas contra la evasión.

---

## 5. Si solo tuvieras $10K para validar, ¿qué haría?

No tocaría código. Ni una sola línea.

Haría un **MVP conserje falso a mano**, con esto:

**Semanas 1-2: Investigación dura**
- Entrevistar a 30 dueños de restaurantes pequeños. No amigos. Restaurantes reales en una sola zona.
- Preguntar: ¿a quién le compran? ¿con qué frecuencia? ¿cuánto gastan? ¿les fían? ¿cómo pagan? ¿qué les falla?
- Entrevistar a 15 proveedores. ¿a cuántos restaurantes surten? ¿cómo consiguen clientes? ¿les pagan a tiempo? ¿aceptarían vender por una app con comisión?

**Semanas 3-6: Concierge MVP con WhatsApp y Excel**
- Crear un grupo/catalogue de WhatsApp con 5-10 proveedores y 10-15 restaurantes.
- Yo mismo (o un community manager) coordinaría pedidos, entregas y pagos a mano.
- Cobraría la comisión del 15% real. No descuentos falsos. Si no la pueden pagar, el modelo es inviable.
- Medir: número de pedidos repetidos, tasa de retención a 30 días, frecuencia de compra, ticket promedio, quejas, evasión, costo logístico.

**Semanas 7-8: Validar si hay negocio**
- Si después de 30 días menos de 40% de los restaurantes hace un segundo pedido, o si más de 30% evade la plataforma, mata la idea.
- Si hay tracción real, diseñaría el producto mínimo en torno al dolor real detectado, no a la idea original.

**Con el dinero restante:**
- Pago de incentivos para entrevistas (almuerzos, descuentos).
- Un diseñador freelance para una landing falsa de captura.
- Ads geo-localizados muy baratos para medir interés real.
- Un community manager part-time para operar el WhatsApp.

**No gastaría ni un dólar en app, ni en backend, ni en branding bonito**, hasta no saber si alguien está dispuesto a pagar comisión por esto más de una vez.

---

## Mi veredicto como VC escéptico

Tu idea no es mala por ser un marketplace. Es mala porque **estás atacando un problema débil con una solución costosa en un mercado donde las relaciones personales, el crédito informal y el efectivo son el verdadero sistema operativo**.

Si quieres que esto funcione, probablemente tengas que dejar de ser un “Uber de proveedores” y convertirte en algo más parecido a un **financiamiento + logística + abastecimiento garantizado** para restaurantes. Eso sí es doloroso, difícil de replicar en WhatsApp, y por lo tanto defensible.

De lo contrario, estás construyendo una app que resuelve una molestia menor y cobra como si resolviera un problema existencial.

¿Tienes datos reales de restaurantes, o esto sigue siendo una hipótesis de escritorio?